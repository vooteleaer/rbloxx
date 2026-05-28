"""Node list and status endpoints."""

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

import node_registry
import rns_service

router = APIRouter(prefix="/api/v1/nodes", tags=["nodes"])


class AddNodeBody(BaseModel):
    dest_hash: str
    label: str | None = None


class PatchNodeBody(BaseModel):
    label: str | None = None


@router.get("")
async def list_nodes():
    return await node_registry.get_all_nodes()


@router.post("")
async def add_node(body: AddNodeBody):
    """Pre-register a node by its destination hash so it appears in the UI before it connects."""
    dest_hash = body.dest_hash.strip().lower()
    if not dest_hash:
        raise HTTPException(400, "dest_hash is required")
    existing = await node_registry.get_node(dest_hash)
    if existing:
        if body.label and not existing.get("label"):
            await node_registry.upsert_node(dest_hash, {"label": body.label})
        return await node_registry.get_node(dest_hash)
    await node_registry.upsert_node(dest_hash, {
        "label": body.label or None,
        "last_seen": 0,
    })
    return await node_registry.get_node(dest_hash)


@router.patch("/{dest_hash}")
async def patch_node(dest_hash: str, body: PatchNodeBody):
    """Update mutable node fields (currently: label)."""
    node = await node_registry.get_node(dest_hash)
    if node is None:
        raise HTTPException(404, "Node not found")
    await node_registry.upsert_node(dest_hash, {"label": body.label})
    return await node_registry.get_node(dest_hash)


@router.get("/server-info")
def server_info():
    return rns_service.get_server_info()


@router.get("/{dest_hash}")
async def get_node(dest_hash: str):
    node = await node_registry.get_node(dest_hash)
    if node is None:
        raise HTTPException(404, "Node not found")
    return node


@router.get("/{dest_hash}/telemetry")
async def get_telemetry(dest_hash: str, limit: int = 100):
    return await node_registry.get_telemetry(dest_hash, limit=limit)


@router.delete("/{dest_hash}")
async def delete_node(dest_hash: str):
    node = await node_registry.get_node(dest_hash)
    if node is None:
        raise HTTPException(404, "Node not found")
    await node_registry.delete_node(dest_hash)
    return {"ok": True}


@router.post("/{dest_hash}/command")
async def send_command(dest_hash: str, body: dict):
    """Send an arbitrary command to a node. Body must include 'cmd' key."""
    if "cmd" not in body:
        raise HTTPException(400, "'cmd' is required")
    return await rns_service.send_command(dest_hash, body)
