"""SQLite node registry — nodes, telemetry time-series, config snapshots."""

import json
import os
import time

import aiosqlite

DB_PATH = os.environ.get("BLOXX_DB", "bloxx.db")

CREATE_NODES = """
CREATE TABLE IF NOT EXISTS nodes (
    dest_hash   TEXT PRIMARY KEY,
    identity_hash TEXT,
    label       TEXT,
    hostname    TEXT,
    version     TEXT,
    first_seen  REAL,
    last_seen   REAL,
    last_errors TEXT DEFAULT '[]'
)
"""

CREATE_TELEMETRY = """
CREATE TABLE IF NOT EXISTS telemetry (
    id          INTEGER PRIMARY KEY AUTOINCREMENT,
    dest_hash   TEXT NOT NULL,
    ts          REAL NOT NULL,
    cpu_pct     REAL,
    ram_pct     REAL,
    disk_pct    REAL,
    temp_c      REAL,
    batt_soc_pct REAL,
    batt_voltage_v REAL,
    batt_power_w  REAL,
    solar_power_w REAL,
    rns_rtt_ms  REAL,
    rns_rxb     INTEGER,
    rns_txb     INTEGER,
    rns_rxs     REAL,
    rns_txs     REAL,
    rnode_airtime_short      REAL,
    rnode_airtime_long       REAL,
    rnode_channel_load_short REAL,
    rnode_channel_load_long  REAL,
    rnode_bitrate            REAL,
    rnode_noise_floor        REAL,
    rnode_interference_dbm   REAL,
    rnode_announce_in        REAL,
    rnode_announce_out       REAL,
    rnode_held_announces     INTEGER,
    interfaces  TEXT,
    errors      TEXT DEFAULT '[]'
)
"""

CREATE_TELEMETRY_IDX = """
CREATE INDEX IF NOT EXISTS idx_telemetry_dest_ts ON telemetry (dest_hash, ts)
"""

CREATE_CONFIG_SNAPSHOTS = """
CREATE TABLE IF NOT EXISTS config_snapshots (
    id          INTEGER PRIMARY KEY AUTOINCREMENT,
    dest_hash   TEXT NOT NULL,
    cfg_type    TEXT NOT NULL,
    ts          REAL NOT NULL,
    content     TEXT NOT NULL
)
"""

CREATE_CONFIG_IDX = """
CREATE INDEX IF NOT EXISTS idx_config_dest_type ON config_snapshots (dest_hash, cfg_type)
"""

# Stores the latest topology snapshot per node (path table + link quality)
CREATE_TOPOLOGY = """
CREATE TABLE IF NOT EXISTS topology_snapshots (
    dest_hash   TEXT PRIMARY KEY,
    ts          REAL NOT NULL,
    paths       TEXT NOT NULL    -- JSON: [{dest_hash, hops, interface, bitrate, rssi, snr}]
)
"""

_RNODE_COLUMNS = [
    ("rnode_airtime_short",      "REAL"),
    ("rnode_airtime_long",       "REAL"),
    ("rnode_channel_load_short", "REAL"),
    ("rnode_channel_load_long",  "REAL"),
    ("rnode_bitrate",            "REAL"),
    ("rnode_noise_floor",        "REAL"),
    ("rnode_interference_dbm",   "REAL"),
    ("rnode_announce_in",        "REAL"),
    ("rnode_announce_out",       "REAL"),
    ("rnode_held_announces",     "INTEGER"),
]


async def init_db(db_path: str = DB_PATH) -> None:
    async with aiosqlite.connect(db_path) as db:
        await db.execute(CREATE_NODES)
        await db.execute(CREATE_TELEMETRY)
        await db.execute(CREATE_TELEMETRY_IDX)
        await db.execute(CREATE_CONFIG_SNAPSHOTS)
        await db.execute(CREATE_CONFIG_IDX)
        await db.execute(CREATE_TOPOLOGY)
        # Migrate: add columns that didn't exist in earlier schema versions
        async with db.execute("PRAGMA table_info(nodes)") as cur:
            node_cols = {row[1] async for row in cur}
        if "label" not in node_cols:
            await db.execute("ALTER TABLE nodes ADD COLUMN label TEXT")
        async with db.execute("PRAGMA table_info(telemetry)") as cur:
            existing = {row[1] async for row in cur}
        for col, typ in _RNODE_COLUMNS:
            if col not in existing:
                await db.execute(f"ALTER TABLE telemetry ADD COLUMN {col} {typ}")
        await db.commit()


async def upsert_node(dest_hash: str, data: dict, db_path: str = DB_PATH) -> None:
    now = time.time()
    # Allow callers to force last_seen=0 so the node starts offline (e.g. pre-registration)
    last_seen = data.get("last_seen", now)
    async with aiosqlite.connect(db_path) as db:
        await db.execute("""
            INSERT INTO nodes (dest_hash, identity_hash, label, hostname, version, first_seen, last_seen, last_errors)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
            ON CONFLICT(dest_hash) DO UPDATE SET
                identity_hash = COALESCE(excluded.identity_hash, identity_hash),
                label         = COALESCE(excluded.label, label),
                hostname      = COALESCE(excluded.hostname, hostname),
                version       = COALESCE(excluded.version, version),
                last_seen     = excluded.last_seen,
                last_errors   = excluded.last_errors
        """, (
            dest_hash,
            data.get("identity_hash"),
            data.get("label"),
            data.get("hostname"),
            data.get("version"),
            now,
            last_seen,
            json.dumps(data.get("errors", [])),
        ))
        await db.commit()


async def record_telemetry(dest_hash: str, data: dict, db_path: str = DB_PATH) -> None:
    ts = data.get("timestamp", time.time())
    now = time.time()  # server receipt time — used for last_seen so it never precedes first_seen
    async with aiosqlite.connect(db_path) as db:
        await db.execute("""
            INSERT INTO telemetry
                (dest_hash, ts, cpu_pct, ram_pct, disk_pct, temp_c,
                 batt_soc_pct, batt_voltage_v, batt_power_w, solar_power_w,
                 rns_rtt_ms, rns_rxb, rns_txb, rns_rxs, rns_txs,
                 rnode_airtime_short, rnode_airtime_long,
                 rnode_channel_load_short, rnode_channel_load_long,
                 rnode_bitrate, rnode_noise_floor, rnode_interference_dbm,
                 rnode_announce_in, rnode_announce_out, rnode_held_announces,
                 interfaces, errors)
            VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)
        """, (
            dest_hash, ts,
            data.get("cpu_pct"), data.get("ram_pct"), data.get("disk_pct"), data.get("temp_c"),
            data.get("batt_soc_pct"), data.get("batt_voltage_v"),
            data.get("batt_power_w"), data.get("solar_power_w"),
            data.get("rns_rtt_ms"), data.get("rns_rxb"), data.get("rns_txb"),
            data.get("rns_rxs"), data.get("rns_txs"),
            data.get("rnode_airtime_short"), data.get("rnode_airtime_long"),
            data.get("rnode_channel_load_short"), data.get("rnode_channel_load_long"),
            data.get("rnode_bitrate"), data.get("rnode_noise_floor"),
            data.get("rnode_interference_dbm"),
            data.get("rnode_announce_in"), data.get("rnode_announce_out"),
            data.get("rnode_held_announces"),
            json.dumps(data.get("interfaces")),
            json.dumps(data.get("errors", [])),
        ))
        # Use server receipt time so last_seen is never earlier than first_seen
        await db.execute("""
            UPDATE nodes SET last_seen = ?, last_errors = ? WHERE dest_hash = ?
        """, (now, json.dumps(data.get("errors", [])), dest_hash))
        await db.commit()


async def get_all_nodes(announce_interval: int = 300, db_path: str = DB_PATH) -> list[dict]:
    offline_threshold = time.time() - announce_interval * 2
    async with aiosqlite.connect(db_path) as db:
        db.row_factory = aiosqlite.Row
        async with db.execute("SELECT * FROM nodes ORDER BY last_seen DESC") as cur:
            rows = await cur.fetchall()
    return [
        {**dict(r), "online": r["last_seen"] > offline_threshold, "last_errors": json.loads(r["last_errors"])}
        for r in rows
    ]


async def get_node(dest_hash: str, announce_interval: int = 300, db_path: str = DB_PATH) -> dict | None:
    offline_threshold = time.time() - announce_interval * 2
    async with aiosqlite.connect(db_path) as db:
        db.row_factory = aiosqlite.Row
        async with db.execute("SELECT * FROM nodes WHERE dest_hash = ?", (dest_hash,)) as cur:
            row = await cur.fetchone()
    if row is None:
        return None
    return {**dict(row), "online": row["last_seen"] > offline_threshold, "last_errors": json.loads(row["last_errors"])}


async def get_telemetry(dest_hash: str, limit: int = 100, db_path: str = DB_PATH) -> list[dict]:
    async with aiosqlite.connect(db_path) as db:
        db.row_factory = aiosqlite.Row
        async with db.execute("""
            SELECT * FROM telemetry WHERE dest_hash = ? ORDER BY ts DESC LIMIT ?
        """, (dest_hash, limit)) as cur:
            rows = await cur.fetchall()
    return [
        {**dict(r), "interfaces": json.loads(r["interfaces"] or "null"), "errors": json.loads(r["errors"])}
        for r in rows
    ]


async def delete_node(dest_hash: str, db_path: str = DB_PATH) -> None:
    async with aiosqlite.connect(db_path) as db:
        await db.execute("DELETE FROM telemetry WHERE dest_hash = ?", (dest_hash,))
        await db.execute("DELETE FROM config_snapshots WHERE dest_hash = ?", (dest_hash,))
        await db.execute("DELETE FROM nodes WHERE dest_hash = ?", (dest_hash,))
        await db.commit()


async def save_config_snapshot(dest_hash: str, cfg_type: str, content: str, db_path: str = DB_PATH) -> None:
    async with aiosqlite.connect(db_path) as db:
        await db.execute("""
            INSERT INTO config_snapshots (dest_hash, cfg_type, ts, content) VALUES (?, ?, ?, ?)
        """, (dest_hash, cfg_type, time.time(), content))
        await db.commit()


async def get_latest_config(dest_hash: str, cfg_type: str, db_path: str = DB_PATH) -> dict | None:
    async with aiosqlite.connect(db_path) as db:
        db.row_factory = aiosqlite.Row
        async with db.execute("""
            SELECT * FROM config_snapshots WHERE dest_hash = ? AND cfg_type = ?
            ORDER BY ts DESC LIMIT 1
        """, (dest_hash, cfg_type)) as cur:
            row = await cur.fetchone()
    return dict(row) if row else None


# ------------------------------------------------------------------
# Retention
# ------------------------------------------------------------------

async def prune(retention_days: int = 30, db_path: str = DB_PATH) -> dict[str, int]:
    """Delete old rows. Returns counts of deleted rows per table."""
    cutoff = time.time() - retention_days * 86400
    deleted = {}
    async with aiosqlite.connect(db_path) as db:
        cur = await db.execute("DELETE FROM telemetry WHERE ts < ?", (cutoff,))
        deleted["telemetry"] = cur.rowcount
        # Keep only the latest 10 config snapshots per (node, type)
        cur = await db.execute("""
            DELETE FROM config_snapshots WHERE id NOT IN (
                SELECT id FROM config_snapshots cs2
                WHERE cs2.dest_hash = config_snapshots.dest_hash
                  AND cs2.cfg_type  = config_snapshots.cfg_type
                ORDER BY ts DESC LIMIT 10
            )
        """)
        deleted["config_snapshots"] = cur.rowcount
        await db.commit()
    return deleted


# ------------------------------------------------------------------
# Topology
# ------------------------------------------------------------------

async def upsert_topology(dest_hash: str, paths: list[dict], db_path: str = DB_PATH) -> None:
    async with aiosqlite.connect(db_path) as db:
        await db.execute("""
            INSERT INTO topology_snapshots (dest_hash, ts, paths)
            VALUES (?, ?, ?)
            ON CONFLICT(dest_hash) DO UPDATE SET ts = excluded.ts, paths = excluded.paths
        """, (dest_hash, time.time(), json.dumps(paths)))
        await db.commit()


async def get_topology_graph(db_path: str = DB_PATH) -> dict:
    """
    Aggregate topology snapshots from all nodes into a unified graph.

    Returns:
        {
          "nodes": [{"id": dest_hash, "hostname": str|None, "managed": bool, "online": bool}],
          "edges": [{"from": dest_hash, "to": dest_hash, "interface": str,
                     "bitrate": float|None, "rssi": int|None, "snr": float|None}]
        }

    Edge deduplication: if both A→B and B→A are reported, merge them
    and prefer the entry with RSSI (i.e. the receiving side on LoRa).
    """
    async with aiosqlite.connect(db_path) as db:
        db.row_factory = aiosqlite.Row

        # All managed nodes (for hostname lookup and online status)
        offline_cutoff = time.time() - 600  # 2× default announce interval
        async with db.execute("SELECT dest_hash, hostname, last_seen FROM nodes") as cur:
            managed_rows = await cur.fetchall()
        managed: dict[str, dict] = {
            r["dest_hash"]: {"hostname": r["hostname"], "online": r["last_seen"] > offline_cutoff}
            for r in managed_rows
        }

        # All topology snapshots
        async with db.execute("SELECT dest_hash, paths FROM topology_snapshots") as cur:
            topo_rows = await cur.fetchall()

    # Build node + edge sets
    node_set: dict[str, dict] = {}
    # edge key = frozenset({from, to}) → best edge dict
    edge_map: dict[frozenset, dict] = {}

    def _add_node(h: str, managed_info: dict | None = None) -> None:
        if h not in node_set:
            node_set[h] = {
                "id": h,
                "hostname": None,
                "managed": False,
                "online": False,
            }
        if managed_info:
            node_set[h].update({"managed": True, **managed_info})

    for row in topo_rows:
        reporter = row["dest_hash"]
        _add_node(reporter, managed.get(reporter))
        paths = json.loads(row["paths"])

        for p in paths:
            peer = p["dest_hash"]
            _add_node(peer, managed.get(peer))

            if p["hops"] != 1:
                continue  # only direct links become edges

            key = frozenset({reporter, peer})
            existing = edge_map.get(key)
            candidate = {
                "from": reporter,
                "to": peer,
                "interface": p.get("interface", ""),
                "bitrate": p.get("bitrate"),
                "rssi": p.get("rssi"),
                "snr": p.get("snr"),
            }
            # Prefer the candidate that has RSSI data (the receiving node)
            if existing is None or (candidate["rssi"] is not None and existing["rssi"] is None):
                edge_map[key] = candidate

    return {
        "nodes": list(node_set.values()),
        "edges": list(edge_map.values()),
    }


async def get_hub_topology(server_dest_hash: str, db_path: str = DB_PATH) -> dict:
    """
    Hub-spoke topology centred on the server.

    Returns:
        {
          "server_dest_hash": str,
          "nodes": [
            {
              "dest_hash": str, "hostname": str|None, "online": bool,
              "hops": int|None,   # hops from this node to server; None = no path info
              "chain": [          # intermediate nodes between this node and server
                {"dest_hash": str, "hostname": str|None, "managed": bool}
                | null            # null = unknown relay
              ] | null            # null = no path info at all
            }
          ]
        }
    """
    async with aiosqlite.connect(db_path) as db:
        db.row_factory = aiosqlite.Row

        offline_cutoff = time.time() - 600

        async with db.execute("SELECT dest_hash, hostname, last_seen FROM nodes") as cur:
            managed_rows = await cur.fetchall()
        managed: dict[str, dict] = {
            r["dest_hash"]: {"hostname": r["hostname"], "online": r["last_seen"] > offline_cutoff}
            for r in managed_rows
        }

        async with db.execute("SELECT dest_hash, paths FROM topology_snapshots") as cur:
            topo_rows = await cur.fetchall()

    paths_by_reporter: dict[str, dict[str, dict]] = {}
    for row in topo_rows:
        reporter = row["dest_hash"]
        if reporter == "unknown":
            continue
        paths = json.loads(row["paths"])
        paths_by_reporter[reporter] = {p["dest_hash"]: p for p in paths}

    nodes_out = []
    for dest_hash, info in managed.items():
        reporter_paths = paths_by_reporter.get(dest_hash, {})
        server_path = reporter_paths.get(server_dest_hash)
        if server_path is None:
            nodes_out.append({"dest_hash": dest_hash, **info, "hops": None, "chain": None})
        else:
            hops = server_path["hops"]
            chain = _infer_chain(dest_hash, server_dest_hash, hops, paths_by_reporter, managed)
            nodes_out.append({"dest_hash": dest_hash, **info, "hops": hops, "chain": chain})

    return {"server_dest_hash": server_dest_hash, "nodes": nodes_out}


def _infer_chain(
    node_hash: str,
    server_hash: str,
    total_hops: int,
    paths_by_reporter: dict[str, dict[str, dict]],
    managed: dict[str, dict],
    depth: int = 0,
) -> list:
    if total_hops <= 1 or depth > 8:
        return []

    node_paths = paths_by_reporter.get(node_hash, {})
    direct_neighbors = {h for h, p in node_paths.items() if p["hops"] == 1}

    for neighbor in direct_neighbors:
        neighbor_paths = paths_by_reporter.get(neighbor, {})
        neighbor_server = neighbor_paths.get(server_hash)
        if neighbor_server is None:
            continue
        if neighbor_server.get("hops") == total_hops - 1:
            sub = _infer_chain(neighbor, server_hash, total_hops - 1, paths_by_reporter, managed, depth + 1)
            return [{"dest_hash": neighbor, "hostname": managed.get(neighbor, {}).get("hostname"), "managed": neighbor in managed}] + sub

    return [None] * (total_hops - 1)

