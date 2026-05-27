"""RNS service layer for the Bloxx server."""

import asyncio
import sys
import threading
import time
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
from protocol import APP_NAME, SERVER_ASPECT, NODE_ASPECT, PATH_TELEMETRY, PATH_CONFIG, PATH_TIME, VERSION

import node_registry

_reticulum: RNS.Reticulum | None = None
_destination: RNS.Destination | None = None
_loop: asyncio.AbstractEventLoop | None = None
_identity_path = Path("/etc/bloxx/server_identity")
_announce_interval = 300
_ws_broadcast: Callable | None = None


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

    # Handle telemetry pushes from nodes
    _destination.register_request_handler(
        PATH_TELEMETRY,
        response_generator=_handle_telemetry,
        allow=RNS.Destination.ALLOW_ALL,
    )

    # Handle config pushes from nodes (node → server on startup)
    _destination.register_request_handler(
        PATH_CONFIG,
        response_generator=_handle_config_push,
        allow=RNS.Destination.ALLOW_ALL,
    )

    # Handle time sync requests from nodes
    _destination.register_request_handler(
        PATH_TIME,
        response_generator=_handle_time_sync,
        allow=RNS.Destination.ALLOW_ALL,
    )

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
# Telemetry handler (nodes push here)
# ------------------------------------------------------------------

def _handle_telemetry(path, data, request_id, remote_identity, requested_at):
    try:
        payload = msgpack.unpackb(data, raw=False)
    except Exception:
        return msgpack.packb({"ok": False, "error": "bad payload"}, use_bin_type=True)

    dest_hash = remote_identity.hash.hex() if remote_identity else "unknown"

    # Enrich with identity hash
    if remote_identity:
        payload["identity_hash"] = remote_identity.hash.hex()
        dest_hash = _dest_hash_for_identity(remote_identity)

    if _loop:
        asyncio.run_coroutine_threadsafe(
            _store_telemetry(dest_hash, payload), _loop
        )

    return msgpack.packb({"ok": True}, use_bin_type=True)


async def _store_telemetry(dest_hash: str, payload: dict) -> None:
    await node_registry.upsert_node(dest_hash, payload)
    await node_registry.record_telemetry(dest_hash, payload)
    topo = payload.get("topology", {})
    if topo.get("paths"):
        await node_registry.upsert_topology(dest_hash, topo["paths"])
    if _ws_broadcast:
        await _ws_broadcast({"type": "telemetry", "dest_hash": dest_hash, "data": payload})


def _dest_hash_for_identity(identity: RNS.Identity) -> str:
    dest = RNS.Destination(identity, RNS.Destination.OUT, RNS.Destination.SINGLE, APP_NAME, NODE_ASPECT)
    return dest.hash.hex()


# ------------------------------------------------------------------
# Config push handler (node pushes config to server on startup)
# ------------------------------------------------------------------

def _handle_config_push(path, data, request_id, remote_identity, requested_at):
    try:
        payload = msgpack.unpackb(data, raw=False)
    except Exception:
        return msgpack.packb({"ok": False, "error": "bad payload"}, use_bin_type=True)

    if remote_identity is None:
        return msgpack.packb({"ok": False, "error": "no identity"}, use_bin_type=True)

    dest_hash = _dest_hash_for_identity(remote_identity)
    cfg_type = payload.get("type")
    content = payload.get("content")

    if cfg_type and isinstance(content, str) and content:
        if _loop:
            asyncio.run_coroutine_threadsafe(
                node_registry.save_config_snapshot(dest_hash, cfg_type, content), _loop
            )

    return msgpack.packb({"ok": True}, use_bin_type=True)


# ------------------------------------------------------------------
# Time sync handler
# ------------------------------------------------------------------

def _handle_time_sync(path, data, request_id, remote_identity, requested_at):
    t2 = time.time_ns()
    try:
        payload = msgpack.unpackb(data, raw=False)
    except Exception:
        payload = {}
    t3 = time.time_ns()
    return msgpack.packb({"ok": True, "t2": t2, "t3": t3}, use_bin_type=True)


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
# Send command to a node
# ------------------------------------------------------------------

def send_command(node_dest_hash: str, cmd: dict, timeout: float = 60.0) -> dict:
    """Blocking — opens a link to the node, sends a command, returns the response."""
    if _destination is None:
        return {"ok": False, "error": "server not initialised"}

    dest_hash = bytes.fromhex(node_dest_hash)

    # Step 1 — resolve identity.
    # In shared-instance mode, Identity.recall() reads rnsd's persisted store and
    # works even right after server restart. has_path() reflects the client-process
    # path table which is empty until announces arrive, so we don't use it here.
    identity = RNS.Identity.recall(dest_hash)
    if identity is None:
        RNS.Transport.request_path(dest_hash)
        deadline = time.time() + min(timeout / 2, 30)
        while identity is None and time.time() < deadline:
            time.sleep(2)
            identity = RNS.Identity.recall(dest_hash)
    if identity is None:
        return {"ok": False, "error": "no_path: node identity unknown — node has not announced yet"}

    # Step 2 — ensure a routing path exists.
    # After a server restart the client-side path table is empty even though rnsd
    # may still have the path. request_path() broadcasts a path request; if the
    # node is reachable it will respond with an announce and rnsd will populate
    # the path table in both the daemon and this client process.
    if not RNS.Transport.has_path(dest_hash):
        RNS.Transport.request_path(dest_hash)
        path_deadline = time.time() + 15
        while not RNS.Transport.has_path(dest_hash) and time.time() < path_deadline:
            time.sleep(1)
        if not RNS.Transport.has_path(dest_hash):
            return {"ok": False, "error": "no_path: node is offline or out of range"}

    try:
        node_dest = RNS.Destination(
            identity, RNS.Destination.OUT, RNS.Destination.SINGLE, APP_NAME, NODE_ASPECT,
        )
        link = RNS.Link(node_dest)
        link_deadline = time.time() + min(timeout, 30)
        while link.status != RNS.Link.ACTIVE and time.time() < link_deadline:
            time.sleep(0.1)
        if link.status != RNS.Link.ACTIVE:
            link.teardown()
            return {"ok": False, "error": "no_path: link establishment timed out"}

        link.identify(_destination.identity)
        time.sleep(0.3)

        result: dict = {"ok": False, "error": "no response"}
        done = threading.Event()

        def _resp(receipt):
            nonlocal result
            if receipt.response:
                try:
                    result = msgpack.unpackb(receipt.response, raw=False)
                except Exception:
                    pass
            done.set()

        link.request(
            "/cmd",
            data=msgpack.packb(cmd, use_bin_type=True),
            response_callback=_resp,
            failed_callback=lambda r: done.set(),
            timeout=timeout,
        )
        done.wait(timeout=timeout + 5)
        link.teardown()
        return result

    except Exception as e:
        return {"ok": False, "error": str(e)}
