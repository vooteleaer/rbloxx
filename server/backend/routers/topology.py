"""Topology graph endpoint."""

from fastapi import APIRouter
import node_registry
import rns_service

router = APIRouter(prefix="/api/v1/topology", tags=["topology"])


@router.get("")
async def get_topology():
    return await node_registry.get_topology_graph()


@router.get("/hub")
async def get_hub_topology():
    """Hub-spoke topology centred on this server, showing how each managed node connects."""
    info = rns_service.get_server_info()
    server_dest_hash = info.get("dest_hash", "")
    return await node_registry.get_hub_topology(server_dest_hash)
