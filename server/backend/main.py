"""Bloxx server — FastAPI application entry point."""

import asyncio
import json
import os
from contextlib import asynccontextmanager
from pathlib import Path

import RNS
from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles

import node_registry
import rns_service
from routers import nodes as nodes_router
from routers import config as config_router
from routers import topology as topology_router

RETENTION_DAYS = int(os.environ.get("BLOXX_RETENTION_DAYS", "30"))


class _WSManager:
    def __init__(self):
        self._clients: list[WebSocket] = []

    async def connect(self, ws: WebSocket) -> None:
        await ws.accept()
        self._clients.append(ws)

    def disconnect(self, ws: WebSocket) -> None:
        self._clients = [c for c in self._clients if c is not ws]

    async def broadcast(self, data: dict) -> None:
        text = json.dumps(data)
        dead = []
        for ws in self._clients:
            try:
                await ws.send_text(text)
            except Exception:
                dead.append(ws)
        for ws in dead:
            self.disconnect(ws)


_ws_manager = _WSManager()


async def _retention_loop() -> None:
    while True:
        await asyncio.sleep(86400)  # run once a day
        try:
            deleted = await node_registry.prune(RETENTION_DAYS)
            RNS.log(
                f"Retention pruned — telemetry: {deleted['telemetry']} rows, "
                f"config snapshots: {deleted['config_snapshots']} rows "
                f"(policy: {RETENTION_DAYS} days)",
                RNS.LOG_NOTICE,
            )
        except Exception as e:
            RNS.log(f"Retention pruning failed: {e}", RNS.LOG_WARNING)


@asynccontextmanager
async def lifespan(app: FastAPI):
    await node_registry.init_db()
    rns_service.init()
    rns_service.set_ws_broadcast(_ws_manager.broadcast)
    asyncio.create_task(_retention_loop())
    yield


app = FastAPI(title="Bloxx", lifespan=lifespan)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(nodes_router.router)
app.include_router(config_router.router)
app.include_router(topology_router.router)


@app.get("/api/v1/status")
async def status():
    return {"status": "ok", "retention_days": RETENTION_DAYS, **rns_service.get_server_info()}


@app.post("/api/v1/maintenance/prune")
async def manual_prune():
    deleted = await node_registry.prune(RETENTION_DAYS)
    return {"ok": True, "deleted": deleted, "retention_days": RETENTION_DAYS}


@app.websocket("/api/v1/ws")
async def websocket_endpoint(ws: WebSocket):
    await _ws_manager.connect(ws)
    try:
        while True:
            await ws.receive_text()  # keep alive
    except WebSocketDisconnect:
        _ws_manager.disconnect(ws)


# Serve React frontend — must be last so API routes take priority
_dist = Path(__file__).parent / "dist"
if _dist.exists():
    app.mount("/assets", StaticFiles(directory=_dist / "assets"), name="assets")

    @app.get("/{full_path:path}", include_in_schema=False)
    async def serve_spa(_full_path: str = ""):
        return FileResponse(_dist / "index.html")
