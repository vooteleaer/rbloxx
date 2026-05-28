"""RNS service layer for the Bloxx server."""

import asyncio
import sys
import threading
import time
import uuid
from pathlib import Path
from typing import Callable

import msgpack
import RNS

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
from protocol import (
    APP_NAME, SERVER_ASPECT, NODE_ASPECT, VERSION,
    PKT_TELEMETRY, PKT_RTELEMETRY, PKT_CONFIG, PKT_CMD, PKT_RESULT,
    CHUNK_SIZE,
)

import node_registry

_reticulum: RNS.Reticulum | None = None
_destination: RNS.Destination | None = None
_loop: asyncio.AbstractEventLoop | None = None
_identity_path = Path("/etc/bloxx/server_identity")
_announce_interval = 300
_ws_broadcast: Callable | None = None

# Pending command futures: cmd_id → asyncio.Future
_pending_commands: dict[str, asyncio.Future] = {}
_pending_lock = threading.Lock()

# Result chunk reassembly buffers: cmd_id → {"chunks": {}, "total": n, "ok": bool}
_result_chunks: dict[str, dict] = {}
_result_chunks_lock = threading.Lock()

# Config chunk reassembly buffers: (dest_hash, cfg_type) → {"chunks": {}, "total": n}
_config_chunks: dict[tuple, dict] = {}
_config_chunks_lock = threading.Lock()


def init(
    identity_path: Path | None = None,
    announce_interval: int = 300,
    db_path: str = node_registry.DB_PATH,
) -> None:
    global _reticulum, _destination, _loop, _identity_path, _announce_interval

    if identity_path:
        _identity_path = identity_path
    _announce_interval = announce_interval

    _loop = asyncio.get_event_loop()
    _reticulum = RNS.Reticulum(require_shared_instance=True)

    identity = _load_or_create_identity()

    _destination = RNS.Destination(
        identity,
        RNS.Destination.IN,
        RNS.Destination.SINGLE,
        APP_NAME,
        SERVER_ASPECT,
    )

    # Receive plain packets from nodes (telemetry, configs, command results)
    _destination.set_packet_callback(_handle_packet)

    # Listen for node announces
    RNS.Transport.register_announce_handler(_NodeAnnounceHandler(db_path))

    # Announce server presence periodically
    threading.Thread(target=_announce_loop, daemon=True, name="srv-announce").start()

    RNS.log(
        f"Bloxx server started — dest {RNS.prettyhexrep(_destination.hash)}  "
        f"identity {_destination.identity.hash.hex()}",
        RNS.LOG_NOTICE,
    )


def get_server_info() -> dict:
    if _destination is None:
        return {}
    return {
        "dest_hash": _destination.hash.hex(),
        "identity_hash": _destination.identity.hash.hex(),
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
        if _destination:
            app_data = msgpack.packb({"version": VERSION}, use_bin_type=True)
            _destination.announce(app_data=app_data)
        time.sleep(_announce_interval)


# ------------------------------------------------------------------
# Inbound packet dispatcher (called from RNS thread)
# ------------------------------------------------------------------

def _handle_packet(data: bytes, packet) -> None:
    try:
        msg = msgpack.unpackb(data, raw=False)
    except Exception:
        return

    pkt_type = msg.get("t")
    node_hash = msg.get("h", "")  # node's own dest hash (self-reported in packet)

    if pkt_type == PKT_TELEMETRY:
        if _loop:
            asyncio.run_coroutine_threadsafe(_store_telemetry(node_hash, msg.get("d", {})), _loop)

    elif pkt_type == PKT_RTELEMETRY:
        if _loop:
            asyncio.run_coroutine_threadsafe(_store_rtelemetry(node_hash, msg.get("d", {})), _loop)

    elif pkt_type == PKT_CONFIG:
        _handle_config_chunk(node_hash, msg)

    elif pkt_type == PKT_RESULT:
        _handle_result_chunk(msg)


# ------------------------------------------------------------------
# Telemetry storage
# ------------------------------------------------------------------

async def _store_telemetry(dest_hash: str, payload: dict) -> None:
    await node_registry.upsert_node(dest_hash, payload)
    await node_registry.record_telemetry(dest_hash, payload)
    topo = payload.get("topology", {})
    if topo and topo.get("paths"):
        await node_registry.upsert_topology(dest_hash, topo["paths"])
    if _ws_broadcast:
        await _ws_broadcast({"type": "telemetry", "dest_hash": dest_hash, "data": payload})


async def _store_rtelemetry(dest_hash: str, payload: dict) -> None:
    # rtelemetry has no hostname/errors — only record the radio stats time-series row
    await node_registry.record_telemetry(dest_hash, payload)
    if _ws_broadcast:
        await _ws_broadcast({"type": "rtelemetry", "dest_hash": dest_hash, "data": payload})


# ------------------------------------------------------------------
# Config chunk reassembly
# ------------------------------------------------------------------

def _handle_config_chunk(dest_hash: str, msg: dict) -> None:
    cfg_type = msg.get("ct", "")
    total = msg.get("n", 1)
    idx = msg.get("i", 0)
    chunk = msg.get("c", "")
    key = (dest_hash, cfg_type)

    with _config_chunks_lock:
        buf = _config_chunks.setdefault(key, {"chunks": {}, "total": total})
        buf["chunks"][idx] = chunk
        if len(buf["chunks"]) < buf["total"]:
            return
        content = "".join(buf["chunks"][i] for i in range(buf["total"]))
        del _config_chunks[key]

    if _loop:
        asyncio.run_coroutine_threadsafe(
            node_registry.save_config_snapshot(dest_hash, cfg_type, content), _loop
        )


# ------------------------------------------------------------------
# Command result chunk reassembly
# ------------------------------------------------------------------

def _handle_result_chunk(msg: dict) -> None:
    cmd_id = msg.get("id", "")
    total = msg.get("n", 1)
    idx = msg.get("i", 0)
    chunk = msg.get("c", "")
    ok = msg.get("ok", False)

    with _result_chunks_lock:
        buf = _result_chunks.setdefault(cmd_id, {"chunks": {}, "total": total, "ok": ok})
        buf["chunks"][idx] = chunk
        if len(buf["chunks"]) < buf["total"]:
            return
        output = "".join(buf["chunks"][i] for i in range(buf["total"]))
        result_ok = buf["ok"]
        del _result_chunks[cmd_id]

    result = {"ok": result_ok, "output": output} if result_ok else {"ok": False, "error": output}

    with _pending_lock:
        fut = _pending_commands.get(cmd_id)

    if fut and _loop:
        _loop.call_soon_threadsafe(_resolve_future, fut, result)


def _resolve_future(fut: asyncio.Future, result: dict) -> None:
    if not fut.done():
        fut.set_result(result)


# ------------------------------------------------------------------
# Node announce handler
# ------------------------------------------------------------------

class _NodeAnnounceHandler:
    aspect_filter = f"{APP_NAME}.{NODE_ASPECT}"

    def __init__(self, db_path: str):
        self._db_path = db_path

    def received_announce(
        self,
        destination_hash: bytes,
        announced_identity: RNS.Identity,
        app_data: bytes | None,
    ) -> None:
        dest_hash_hex = destination_hash.hex()
        data: dict = {"hostname": None, "version": None}
        if app_data:
            try:
                data = msgpack.unpackb(app_data, raw=False)
            except Exception:
                pass

        data["identity_hash"] = announced_identity.hash.hex() if announced_identity else None

        if _loop:
            asyncio.run_coroutine_threadsafe(
                node_registry.upsert_node(dest_hash_hex, data, self._db_path), _loop
            )
            if _ws_broadcast:
                asyncio.run_coroutine_threadsafe(
                    _ws_broadcast({"type": "announce", "dest_hash": dest_hash_hex, "data": data}),
                    _loop,
                )


# ------------------------------------------------------------------
# Send command to a node (async — fire plain packet, await result)
# ------------------------------------------------------------------

async def send_command(node_dest_hash: str, cmd: dict, timeout: float = 60.0) -> dict:
    """Send a command packet to a node and await the result."""
    if _destination is None:
        return {"ok": False, "error": "server not initialised"}

    dest_hash_bytes = bytes.fromhex(node_dest_hash)

    # Resolve node identity — rnsd persists this across restarts; no path table needed.
    identity = RNS.Identity.recall(dest_hash_bytes)
    if identity is None:
        return {"ok": False, "error": "no_path: node identity unknown — node has not announced yet"}

    node_dest = RNS.Destination(
        identity, RNS.Destination.OUT, RNS.Destination.SINGLE, APP_NAME, NODE_ASPECT,
    )

    cmd_id = uuid.uuid4().hex
    loop = asyncio.get_running_loop()
    fut: asyncio.Future = loop.create_future()

    with _pending_lock:
        _pending_commands[cmd_id] = fut

    try:
        _send_cmd_packets(node_dest, cmd_id, cmd)
    except Exception as e:
        with _pending_lock:
            _pending_commands.pop(cmd_id, None)
        return {"ok": False, "error": f"send error: {e}"}

    try:
        return await asyncio.wait_for(fut, timeout=timeout)
    except asyncio.TimeoutError:
        return {"ok": False, "error": "timeout: no response from node"}
    finally:
        with _pending_lock:
            _pending_commands.pop(cmd_id, None)
        with _result_chunks_lock:
            _result_chunks.pop(cmd_id, None)


def _send_cmd_packets(node_dest: RNS.Destination, cmd_id: str, cmd: dict) -> None:
    """Serialise and send one or more PKT_CMD packets to the node destination."""
    content = cmd.get("content")
    base = {
        "t": PKT_CMD,
        "sh": _destination.hash.hex(),
        "id": cmd_id,
        **{k: v for k, v in cmd.items() if k != "content"},
    }

    if content is not None:
        encoded = content.encode("utf-8")
        chunks = [encoded[i:i + CHUNK_SIZE] for i in range(0, len(encoded), CHUNK_SIZE)] or [b""]
        for i, chunk in enumerate(chunks):
            payload = msgpack.packb(
                {**base, "i": i, "n": len(chunks), "c": chunk.decode("utf-8")},
                use_bin_type=True,
            )
            RNS.Packet(node_dest, payload, create_receipt=False).send()
    else:
        payload = msgpack.packb(base, use_bin_type=True)
        sent = RNS.Packet(node_dest, payload, create_receipt=False).send()
        if sent is False:
            raise RuntimeError("packet rejected — no path to node")
