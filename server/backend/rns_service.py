"""RNS service layer for the RBloxx server.

Transport is LXMF, same as node/rbloxx_agent.py: the message kind is read
from the leading verb of LXMessage.content (see shared/cli_grammar.py), not
a type tag. Nodes announce/deliver on LXMF's own hardcoded ("lxmf","delivery")
destination -- there is no custom app/aspect anymore.
"""

import asyncio
import socket
import sys
import threading
import time
import uuid
from pathlib import Path
from typing import Callable

import RNS
import LXMF

# RNS 1.2.5 + Python 3.13 bug: _used_destination_data incorrectly calls
# rpc_connection.recv() in shared-instance client mode, where rnsd never
# sends a response, causing an EOFError that aborts packet processing.
# Suppress it so inbound() completes normally and announces are cached.
if hasattr(RNS.Reticulum, "_used_destination_data"):
    _rns_orig_udd = RNS.Reticulum._used_destination_data
    def _rns_safe_udd(self, dest_hash):
        try:
            _rns_orig_udd(self, dest_hash)
        except (EOFError, BrokenPipeError, OSError):
            pass
    RNS.Reticulum._used_destination_data = _rns_safe_udd

sys.path.insert(0, str(Path(__file__).parent.parent.parent / "shared"))
from protocol import VERSION, FIELD_TXN
from cli_grammar import cmd_dict_to_cli

import node_registry

_reticulum: RNS.Reticulum | None = None
_router: LXMF.LXMRouter | None = None
_dest: RNS.Destination | None = None
_loop: asyncio.AbstractEventLoop | None = None
_identity_path = Path("/etc/rbloxx/server_identity")
_announce_interval = 300
_ws_broadcast: Callable | None = None
_db_path = node_registry.DB_PATH

# Pending command futures: txn → asyncio.Future
_pending_commands: dict[str, asyncio.Future] = {}
_pending_lock = threading.Lock()


def init(
    identity_path: Path | None = None,
    announce_interval: int = 300,
    db_path: str = node_registry.DB_PATH,
) -> None:
    global _reticulum, _router, _dest, _loop, _identity_path, _announce_interval, _db_path

    if identity_path:
        _identity_path = identity_path
    _announce_interval = announce_interval
    _db_path = db_path

    _loop = asyncio.get_event_loop()
    _reticulum = RNS.Reticulum(require_shared_instance=True)

    identity = _load_or_create_identity()

    # Dedicated subdirectory, distinct from a co-located node agent's own
    # LXMF storage (which lives directly in *its* identity's parent dir) --
    # lets server and agent run on the same box without colliding.
    storagepath = _identity_path.parent / "server_lxmf"
    _router = LXMF.LXMRouter(identity=identity, storagepath=str(storagepath))
    _dest = _router.register_delivery_identity(identity, display_name=socket.gethostname())
    _router.register_delivery_callback(_handle_lxm)

    # Listen for node announces -- nodes announce on LXMF's own hardcoded
    # ("lxmf", "delivery") destination, not a custom app/aspect.
    RNS.Transport.register_announce_handler(_NodeAnnounceHandler(db_path))

    # Announce server presence periodically, so nodes can recall its identity.
    threading.Thread(target=_announce_loop, daemon=True, name="srv-announce").start()

    RNS.log(
        f"RBloxx server started — dest {RNS.prettyhexrep(_dest.hash)}  "
        f"identity {identity.hash.hex()}",
        RNS.LOG_NOTICE,
    )


def get_server_info() -> dict:
    if _dest is None:
        return {}
    return {
        "dest_hash": _dest.hash.hex(),
        "identity_hash": _dest.identity.hash.hex(),
        "version": VERSION,
    }


def set_ws_broadcast(fn: Callable) -> None:
    global _ws_broadcast
    _ws_broadcast = fn


# ------------------------------------------------------------------
# Identity
# ------------------------------------------------------------------

def _load_or_create_identity() -> RNS.Identity:
    if _identity_path.exists():
        return RNS.Identity.from_file(str(_identity_path))
    identity = RNS.Identity()
    _identity_path.parent.mkdir(parents=True, exist_ok=True)
    identity.to_file(str(_identity_path))
    RNS.log(f"Created new server identity: {identity.hash.hex()}", RNS.LOG_NOTICE)
    return identity


# ------------------------------------------------------------------
# Announce loop
# ------------------------------------------------------------------

def _announce_loop() -> None:
    while True:
        if _dest:
            _dest.announce()
        time.sleep(_announce_interval)


# ------------------------------------------------------------------
# Inbound LXMF dispatcher (called from RNS thread)
# ------------------------------------------------------------------

def _handle_lxm(message: "LXMF.LXMessage") -> None:
    if not message.signature_validated:
        RNS.log("Rejected unsigned/invalid LXM from node", RNS.LOG_WARNING)
        return

    node_hash = message.source_hash.hex()
    raw = message.content_as_string() or ""
    txn = (message.fields or {}).get(FIELD_TXN, "")

    # Command results are unambiguous by their literal "OK"/"ERR" prefix --
    # checked first and sliced precisely (not partitioned on "\n"), since
    # the output body (e.g. a get_config file dump) may itself be multi-line.
    if raw == "OK":
        _handle_result(True, "", txn)
        return
    if raw.startswith("OK: "):
        _handle_result(True, raw[4:], txn)
        return
    if raw == "ERR":
        _handle_result(False, "", txn)
        return
    if raw.startswith("ERR: "):
        _handle_result(False, raw[5:], txn)
        return

    # Reports (node → server, one-way): first line is the verb, an optional
    # bulk payload follows after the first newline.
    line, _, rest = raw.partition("\n")
    line = line.strip()

    if line.startswith("tel "):
        key, _, value = line[4:].partition("=")
        if _loop:
            asyncio.run_coroutine_threadsafe(_store_telemetry(node_hash, key, value), _loop)
    elif line.startswith("cfg "):
        cfg_type = line[4:].strip()
        if _loop:
            asyncio.run_coroutine_threadsafe(_store_config_snapshot(node_hash, cfg_type, rest), _loop)
    else:
        RNS.log(f"Unrecognized message from {node_hash[:12]}: {line!r}", RNS.LOG_WARNING)


# ------------------------------------------------------------------
# Telemetry storage
# ------------------------------------------------------------------

async def _store_telemetry(dest_hash: str, key: str, value: str) -> None:
    # Only track telemetry for admin-registered nodes (added via POST /api/v1/nodes
    # or a prior accepted announce) -- otherwise every LXMF-speaking device on the
    # mesh that happens to send a "tel ..." line would get silently auto-registered.
    if not await node_registry.node_exists(dest_hash, _db_path):
        return
    try:
        parsed_value: object = float(value)
    except ValueError:
        parsed_value = value
    payload = {"timestamp": time.time(), key: parsed_value}
    await node_registry.upsert_node(dest_hash, {}, _db_path)
    await node_registry.record_telemetry(dest_hash, payload, _db_path)
    if _ws_broadcast:
        await _ws_broadcast({"type": "telemetry", "dest_hash": dest_hash, "data": payload})


async def _store_config_snapshot(dest_hash: str, cfg_type: str, content: str) -> None:
    if not await node_registry.node_exists(dest_hash, _db_path):
        return
    await node_registry.save_config_snapshot(dest_hash, cfg_type, content, _db_path)


# ------------------------------------------------------------------
# Command result correlation
# ------------------------------------------------------------------

def _handle_result(ok: bool, output: str, txn: str) -> None:
    result = {"ok": ok, "output": output} if ok else {"ok": False, "error": output}

    with _pending_lock:
        fut = _pending_commands.get(txn)

    if fut and _loop:
        _loop.call_soon_threadsafe(_resolve_future, fut, result)


def _resolve_future(fut: asyncio.Future, result: dict) -> None:
    if not fut.done():
        fut.set_result(result)


# ------------------------------------------------------------------
# Node announce handler
# ------------------------------------------------------------------

class _NodeAnnounceHandler:
    # "lxmf.delivery" is the generic destination every LXMF client (not just
    # RBloxx nodes) announces on -- so this handler sees all LXMF traffic on
    # the mesh, not just our fleet. _handle_announce filters to admin-registered
    # nodes only, so random mesh/chat peers never get auto-added to the registry.
    aspect_filter = "lxmf.delivery"

    def __init__(self, db_path: str):
        self._db_path = db_path

    def received_announce(
        self,
        destination_hash: bytes,
        announced_identity: RNS.Identity,
        app_data: bytes | None,
    ) -> None:
        dest_hash_hex = destination_hash.hex()
        data: dict = {
            "hostname": LXMF.display_name_from_app_data(app_data),
            "identity_hash": announced_identity.hash.hex() if announced_identity else None,
        }
        if _loop:
            asyncio.run_coroutine_threadsafe(_handle_announce(dest_hash_hex, data, self._db_path), _loop)


async def _handle_announce(dest_hash_hex: str, data: dict, db_path: str) -> None:
    if not await node_registry.node_exists(dest_hash_hex, db_path):
        return
    await node_registry.upsert_node(dest_hash_hex, data, db_path)
    if _ws_broadcast:
        await _ws_broadcast({"type": "announce", "dest_hash": dest_hash_hex, "data": data})


# ------------------------------------------------------------------
# Send command to a node (async — fire LXMF message, await result)
# ------------------------------------------------------------------

async def send_command(node_dest_hash: str, cmd: dict, timeout: float = 60.0) -> dict:
    """Send a command to a node and await the result."""
    if _dest is None:
        return {"ok": False, "error": "server not initialised"}

    dest_hash_bytes = bytes.fromhex(node_dest_hash)

    # Resolve node identity — rnsd persists this across restarts; no path table needed.
    identity = RNS.Identity.recall(dest_hash_bytes)
    if identity is None:
        return {"ok": False, "error": "no_path: node identity unknown — node has not announced yet"}

    try:
        cli_line, content_bytes = cmd_dict_to_cli(cmd)
    except ValueError as e:
        return {"ok": False, "error": str(e)}

    node_dest = RNS.Destination(
        identity, RNS.Destination.OUT, RNS.Destination.SINGLE, "lxmf", "delivery",
    )

    txn = uuid.uuid4().hex
    loop = asyncio.get_running_loop()
    fut: asyncio.Future = loop.create_future()

    with _pending_lock:
        _pending_commands[txn] = fut

    body = cli_line if content_bytes is None else f"{cli_line}\n{content_bytes.decode('utf-8')}"
    lxm = LXMF.LXMessage(
        node_dest, _dest, body.encode("utf-8"),
        fields={FIELD_TXN: txn}, desired_method=LXMF.LXMessage.OPPORTUNISTIC,
    )

    try:
        _router.handle_outbound(lxm)
    except Exception as e:
        with _pending_lock:
            _pending_commands.pop(txn, None)
        return {"ok": False, "error": f"send error: {e}"}

    try:
        return await asyncio.wait_for(fut, timeout=timeout)
    except asyncio.TimeoutError:
        return {"ok": False, "error": "timeout: no response from node"}
    finally:
        with _pending_lock:
            _pending_commands.pop(txn, None)
