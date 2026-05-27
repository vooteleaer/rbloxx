# RBloxx Protocol Reference

All RBloxx communication runs over [Reticulum Network Stack (RNS)](https://reticulum.network). No external cloud or broker is required — traffic works over LoRa (RNode), TCP, or any RNS interface.

## Addresses

Every participant is identified by an RNS destination hash, derived from the identity key and the app/aspect names.

| Role | App name | Aspect | Listens on |
|---|---|---|---|
| Server | `bloxx` | `server` | `PATH_TELEMETRY`, `PATH_TIME` |
| Node agent | `bloxx` | `node` | `PATH_CMD` |

### Request paths

| Constant | Path |
|---|---|
| `PATH_CMD` | `/cmd` |
| `PATH_TELEMETRY` | `/telemetry` |
| `PATH_TIME` | `/time` |

## Encoding

All request and response payloads are **msgpack** (`use_bin_type=True`). Strings are UTF-8. Missing optional fields are `null`/`None` (not omitted).

---

## Announce

Nodes announce themselves periodically (default every 300 seconds) using the RNS announce mechanism. The announce `app_data` field is a msgpack-encoded object:

```
{
  "hostname": str,   // system hostname
  "version":  str    // agent version, e.g. "0.1.0"
}
```

The server parses incoming announces and updates its node registry.

---

## Node → Server: Telemetry push

**Path:** `/telemetry` on the server destination

**Direction:** node initiates a link to the server, then sends a request.

### Request payload

```
{
  "hostname":   str,
  "version":    str,
  "timestamp":  int,          // Unix epoch seconds

  // System
  "uptime_s":   int,
  "cpu_pct":    float,        // 0.0 – 100.0
  "ram_pct":    float,        // 0.0 – 100.0
  "disk_pct":   float,        // 0.0 – 100.0
  "temp_c":     float|null,   // CPU temperature, null if unavailable
  "rns_rtt_ms": float|null,   // last NTP-style RTT to server, null until first sync

  // Power (null if no power backend configured)
  "batt_soc_pct":   float|null,   // 0.0 – 100.0
  "batt_voltage_v": float|null,
  "batt_power_w":   float|null,   // positive = charging, negative = discharging
  "solar_power_w":  float|null,

  // RNS interface totals
  "rns_rxb":    int|null,     // total bytes received
  "rns_txb":    int|null,     // total bytes transmitted
  "rns_rxs":    int|null,     // packets received
  "rns_txs":    int|null,     // packets transmitted

  // Per-interface list
  "interfaces": [
    { "name": str, "rxb": int, "txb": int }
  ] | null,

  // RNode stats (populated when an RNodeInterface is present)
  "rnode_airtime_short":      float|null,  // % airtime, short window
  "rnode_airtime_long":       float|null,  // % airtime, long window
  "rnode_channel_load_short": float|null,
  "rnode_channel_load_long":  float|null,
  "rnode_bitrate":            int|null,    // bits/s
  "rnode_noise_floor":        float|null,  // dBm
  "rnode_interference_dbm":   float|null,
  "rnode_announce_in":        float|null,  // announces/s incoming
  "rnode_announce_out":       float|null,  // announces/s outgoing
  "rnode_held_announces":     int|null,

  // Topology
  "topology": {
    "paths": [
      {
        "dest_hash": str,    // hex
        "hops":      int,
        "interface": str,
        "bitrate":   int|null,
        // present only for direct neighbors (hops == 1):
        "rssi": float|null,  // dBm
        "snr":  float|null   // dB
      }
    ]
  },

  // Active errors
  "errors": [ str ]   // list of error code strings (see Error Codes section)
}
```

### Response

The server does not return a meaningful response body; the node ignores it.

---

## Node → Server: Time sync

**Path:** `/time` on the server destination

Uses an NTP-style four-timestamp exchange to compute clock offset and round-trip time. Runs on startup and every 12 hours (configurable via `time_sync_interval`).

### Request payload
```
{ "t1": int }   // node send time, nanoseconds (time.time_ns())
```

### Response payload
```
{
  "t2": int,    // server receive time, nanoseconds
  "t3": int     // server send time, nanoseconds
}
```

### Offset calculation (node side)
```
t4     = time.time_ns()                    // node receive time
offset = ((t2 - t1) + (t3 - t4)) / 2      // nanoseconds
rtt_ms = ((t4 - t1) - (t3 - t2)) / 1e6   // milliseconds
```

If `|offset| > 500 ms`, the node corrects its system clock via `date -s`.

---

## Server → Node: Commands

**Path:** `/cmd` on the node destination

**Direction:** server opens a link to the node, identifies itself, then sends a request. The node only accepts commands from identities it has previously seen as the server (cached after a successful telemetry push).

### Authentication

On every outbound link to a server, the node calls `link.identify()` to present its identity. The server's identity hash is cached in `trusted_server_identities`. Inbound `/cmd` requests from identities not in this set are rejected with `{"ok": false, "error": "not authorized"}`.

### Request envelope
```
{
  "cmd": str,    // command name (see below)
  ...            // command-specific fields
}
```

### Response envelope
```
{
  "ok":     bool,
  "error":  str,     // present on failure
  "output": str,     // present for commands that return text
  ...                // command-specific fields
}
```

---

## Command Reference

### Service control

| Command | Extra fields | Description |
|---|---|---|
| `svc_restart` | `"service": str` | `systemctl restart <service>` |
| `svc_stop` | `"service": str` | `systemctl stop <service>` |
| `svc_start` | `"service": str` | `systemctl start <service>` |

Response: `{ "ok": bool, "output": str }`

---

### Config management

| Command | Extra fields | Description |
|---|---|---|
| `get_config` | `"type": str` | Read a config file; returns raw content |
| `put_config` | `"type": str, "content": str` | Overwrite a config file (with rollback failsafe) |
| `patch_config` | `"type": str, "patches": [...]` | Apply key-value patches to a config |

Config types:

| Type constant | File |
|---|---|
| `rns` | `/root/.reticulum/config` (Reticulum INI) |
| `agent` | `/etc/bloxx/agent.json` |
| `system` | (reserved) |

`put_config` writes to a staging path and restarts the relevant service. If the service fails to come back within the watchdog window, the agent rolls back to the previous file and reports `ERR_CONFIG_ROLLBACK`.

`patch_config` patches format: `[{"section": str, "key": str, "value": str}, ...]`

`get_config` response: `{ "ok": true, "content": str }`

---

### Reboot / shutdown

| Command | Extra fields | Description |
|---|---|---|
| `reboot` | `"delay_s": int` (default 5) | Schedule `systemctl reboot` |
| `shutdown` | `"delay_s": int` (default 5) | Schedule `systemctl poweroff` |

---

### Networking

| Command | Extra fields | Description |
|---|---|---|
| `wifi_set` | `"enabled": bool, "profile": str\|null` | Enable/disable WiFi via `nmcli` |
| `rns_announce` | — | Trigger an immediate RNS announce |
| `connectivity_check` | `"dest_hash": str` | Open a link to `dest_hash`, return RTT |

`connectivity_check` response: `{ "ok": bool, "rtt_ms": float|null }`

---

### Diagnostics

| Command | Extra fields | Description |
|---|---|---|
| `log_pull` | `"lines": int` (default 100), `"unit": str\|null` | Return `journalctl` output |
| `disk_cleanup` | — | Run `journalctl --vacuum-time=7d` |
| `agent_update` | — | `git pull` in the repo root, restart agent |

`log_pull` response: `{ "ok": bool, "content": str }`

---

### RNode hardware

| Command | Extra fields | Description |
|---|---|---|
| `rnode_reset` | `"port": str` | Run `rnodeconf <port> --reset` |
| `rnode_update` | `"port": str` | Run `rnodeconf <port> --update` (up to 5 min) |

---

### Auto-shutdown threshold

| Command | Extra fields | Description |
|---|---|---|
| `shutdown_threshold` | `"soc_pct": float` | Set in-memory battery SoC% shutdown threshold (0 = disabled). Does not persist across agent restarts. |

---

## Error Codes

Reported in the `errors` array of every telemetry payload.

| Code | Trigger |
|---|---|
| `batt_critical` | Battery SoC ≤ threshold (default 10%) |
| `batt_sensor_unavail` | Configured power backend failed to initialise or read |
| `disk_full` | Root filesystem usage ≥ threshold (default 90%) |
| `temp_critical` | CPU temperature ≥ threshold (default 80 °C) |
| `config_apply_failed` | `put_config` service restart failed |
| `config_rollback` | Config rolled back after failed restart |
| `rnode_update_failed` | `rnodeconf --update` returned non-zero |
| `rnode_usb_reset` | RNode stuck (zero traffic) — USB reset attempted |
| `rnode_restart` | USB reset failed, rnsd restarted instead |
| `fs_readonly` | Root filesystem mounted read-only |
| `fs_errors` | I/O errors or ext4 errors seen in dmesg |
| `oom_killed` | OOM killer fired (from journalctl, last 5 min) |
| `watchdog_reboot` | Previous boot ended by hardware watchdog |
| `no_peers` | (reserved) |
| `interface_down` | (reserved) |
| `load_high` | 1-min load average / CPU count ≥ threshold (default 2.0) |
| `swap_high` | Swap usage ≥ threshold (default 80%) |
| `no_charging` | Solar input present but battery power is negative (averaged over recent readings) |

---

## Agent config (`/etc/bloxx/agent.json`)

```json
{
  "identity_path":            "/etc/bloxx/identity",
  "announce_interval":        300,
  "time_sync_interval":       43200,
  "server_dest_hashes":       ["<hex>"],
  "trusted_server_identities": [],
  "rnode_ports":              ["/dev/ttyUSB0"],
  "shutdown_soc_pct":         0,
  "watchdog_feed_interval_s": 10,
  "zero_traffic_minutes":     15,
  "power_backend":            "none",
  "power_i2c_bus":            1,
  "power_i2c_addr":           "0x40",
  "thresholds": {
    "disk_full_pct":     90,
    "temp_critical_c":   80,
    "load_high_factor":  2.0,
    "swap_high_pct":     80,
    "batt_critical_pct": 10
  }
}
```

| Field | Default | Description |
|---|---|---|
| `identity_path` | `/etc/bloxx/identity` | RNS identity file |
| `announce_interval` | `300` | Seconds between announces and telemetry pushes |
| `time_sync_interval` | `43200` | Seconds between NTP-style time sync attempts (12 h) |
| `server_dest_hashes` | `[]` | Hex destination hashes of server(s) to push telemetry to |
| `trusted_server_identities` | `[]` | Auto-populated; persisted across restarts if desired |
| `rnode_ports` | `[]` | Serial ports monitored for stuck RNode (zero-traffic watchdog) |
| `shutdown_soc_pct` | `0` | Auto-shutdown when battery SoC falls to this value; `0` = disabled |
| `watchdog_feed_interval_s` | `10` | Interval for `/dev/watchdog` heartbeat |
| `zero_traffic_minutes` | `15` | Minutes of zero RNode traffic before USB reset is attempted |
| `power_backend` | `none` | `none` / `ina226` / `ina219` |
| `power_i2c_bus` | `1` | I²C bus number for power backend |
| `power_i2c_addr` | `0x40` | I²C address for power backend |

---

## RNode auto-recovery

The agent monitors each port in `rnode_ports` once per minute. If byte counts (rx + tx) have not changed for `zero_traffic_minutes`:

1. Attempt `usbreset <port>` (USB level reset)
2. Wait 5 seconds; check if the interface reappears in RNS stats
3. If not recovered: `systemctl restart rnsd`

Transient error codes `rnode_usb_reset` and `rnode_restart` are added to the next telemetry payload.

---

## Security model

- **Identity-based trust**: the server's RNS identity is the only credential. Any process that can establish an RNS link and identify as a known server identity can issue commands.
- **Trust bootstrapping**: the node caches the server's identity hash after the first successful telemetry push (outbound link). Commands from unknown identities are rejected.
- **No encryption layer above RNS**: RNS links are end-to-end encrypted by default using the identity's public key. No additional application-layer encryption is applied.
- **Root context**: the agent runs as root; issued commands execute with full system privileges. Deploy nodes only in controlled environments.
