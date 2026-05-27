"""Config pull/push endpoints."""

import asyncio
import logging

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

import node_registry
import rns_service

logger = logging.getLogger(__name__)

router = APIRouter(prefix="/api/v1/nodes", tags=["config"])


class PutConfigBody(BaseModel):
    content: str


class PatchConfigBody(BaseModel):
    patches: list[dict]


@router.get("/{dest_hash}/config/{cfg_type}")
async def get_config(dest_hash: str, cfg_type: str):
    """Pull config from node and store snapshot."""
    result = await asyncio.to_thread(
        rns_service.send_command, dest_hash, {"cmd": "get_config", "type": cfg_type}
    )
    if not result.get("ok"):
        logger.warning("config pull failed for %s type=%s: %s", dest_hash, cfg_type, result.get("error"))
        raise HTTPException(502, result.get("error", "node error"))
    content = result["content"]
    await node_registry.save_config_snapshot(dest_hash, cfg_type, content)
    return {"cfg_type": cfg_type, "content": content}


@router.get("/{dest_hash}/config/{cfg_type}/snapshot")
async def get_config_snapshot(dest_hash: str, cfg_type: str):
    """Return last pulled config snapshot (no node contact)."""
    snap = await node_registry.get_latest_config(dest_hash, cfg_type)
    if snap is None:
        raise HTTPException(404, "No snapshot — pull from node first")
    return snap


@router.put("/{dest_hash}/config/{cfg_type}")
async def put_config(dest_hash: str, cfg_type: str, body: PutConfigBody):
    """Push full config file to node."""
    result = await asyncio.to_thread(
        rns_service.send_command, dest_hash,
        {"cmd": "put_config", "type": cfg_type, "content": body.content},
    )
    if not result.get("ok"):
        raise HTTPException(502, result.get("error", "node error"))
    await node_registry.save_config_snapshot(dest_hash, cfg_type, body.content)
    return result


@router.patch("/{dest_hash}/config/{cfg_type}")
async def patch_config(dest_hash: str, cfg_type: str, body: PatchConfigBody):
    """Apply targeted INI patches to node config (bulk-friendly)."""
    result = await asyncio.to_thread(
        rns_service.send_command, dest_hash,
        {"cmd": "patch_config", "type": cfg_type, "patches": body.patches},
    )
    if not result.get("ok"):
        raise HTTPException(502, result.get("error", "node error"))
    return result


@router.patch("/bulk/config/{cfg_type}")
async def bulk_patch_config(cfg_type: str, body: dict):
    """
    Apply the same patches to multiple nodes.
    Body: {"dest_hashes": [...], "patches": [{section, key, value}, ...]}
    """
    dest_hashes = body.get("dest_hashes", [])
    patches = body.get("patches", [])
    tasks = [
        asyncio.to_thread(
            rns_service.send_command, dh,
            {"cmd": "patch_config", "type": cfg_type, "patches": patches},
        )
        for dh in dest_hashes
    ]
    results_list = await asyncio.gather(*tasks, return_exceptions=True)
    return {
        dh: (r if not isinstance(r, Exception) else {"ok": False, "error": str(r)})
        for dh, r in zip(dest_hashes, results_list)
    }
