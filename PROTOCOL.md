# RBloxx Protocol Reference

All RBloxx communication runs over [LXMF](https://github.com/markqvist/LXMF) on top of
[Reticulum (RNS)](https://reticulum.network). No external cloud or broker is required —
traffic works over LoRa (RNode), TCP, or any RNS interface.

For a hands-on guide to the command syntax see [COMMANDS.md](COMMANDS.md).

---

## Addresses

Both the server and every node agent listen on the same LXMF-standard destination:

```
RNS.Destination(identity, IN, SINGLE, "lxmf", "delivery")
```

This is the destination that `LXMRouter.register_delivery_identity()` hardcodes. It means
the address (destination hash) of any participant is determined solely by its RNS identity
key — not by any app/aspect names. Two consequences:

- The destination hash **changes** when the identity changes. Keep the identity file safe.
- After upgrading from a pre-LXMF version of RBloxx, re-paste all hashes (they changed).

To see a node's current destination hash:
```bash
sudo bash install/install_node.sh --show-hash
```

The server's destination hash is printed in the log on startup, and shown in the UI under
*Server info*.

---

## Wire format

LXMF messages carry three user-accessible fields: `title`, `content`, and `fields` (a
dict). RBloxx uses them as follows:

- **`content`** — the payload, always plain UTF-8 text. For commands this is the CLI line
  (`svc restart rnsd`). For results it is the reply (`OK`, `OK: output text`, or
  `ERR: message`). For telemetry and config reports it is the report verb line, optionally
  followed by a newline and a multi-line body.
- **`title`** — not used. Set to empty string. (Many LXMF clients, including MeshChat,
  don't surface the title, so putting command text there would make manual operation
  impossible.)
- **`fields`** — used only for request/response correlation: `{"txn": "<hex uuid4>"}`.
  One-way messages (telemetry, config snapshots) carry no `fields` at all.

**Everything is human-readable plain text.** No msgpack, no binary encoding.

---

## Message types

### Command (server → node)

```
content:  <CLI line>
fields:   {"txn": "<hex uuid4>"}
```

The CLI line is the full command, e.g. `svc restart rnsd` or `set CR=7 SF=5`. The `txn`
field lets the server correlate the reply that arrives on a separate inbound message.

See [COMMANDS.md](COMMANDS.md) for the full command reference.

### Result (node → server)

```
content:  OK
          OK: <output text>       (command produced text output)
          ERR: <error message>    (command failed)
fields:   {"txn": "<same hex uuid4>"}
```

The `txn` value echoes the one from the command, so the server can match it to the
waiting request.

### Telemetry report (node → server)

```
content:  tel <key>=<value>
fields:   (none)
```

One message per changed metric. Never batched. See [Telemetry model](#telemetry-model)
below for the full key list and change rules.

### Config snapshot (node → server)

```
content:  cfg <type>\n<file text>
fields:   (none)
```

The node pushes a fresh snapshot of each config file on startup and after any
`put_config`/`patch_config` change. `<type>` is `rns` or `agent`.

### Announce

Nodes announce via LXMF's own announce mechanism. The announce `app_data` is formatted
by LXMF itself (`[display_name, stamp_cost]`), with `display_name` set to the node's
current hostname. The server parses incoming announces with
`LXMF.display_name_from_app_data()` and updates the node registry.

The announce is the **liveness heartbeat** — the server's online/offline status derives
from announce timing, not from telemetry arrival. "No telemetry for a while" simply
means nothing changed, not that the node is dead.

---

## Telemetry model

Telemetry is **event-driven**: the agent polls metrics every `telemetry_poll_interval`
seconds (default 10 s) and sends one `tel <key>=<value>` message per field that has
changed enough to warrant a report. A metric is reported when it crosses its rule:

| Rule class | Keys | Trigger |
|---|---|---|
| Event-like | `hostname`, `version`, `errors` | Any change, immediately |
| Threshold + min-interval gauge | `cpu_pct`, `ram_pct`, `disk_pct`, `temp_c`, `batt_*`, `solar_*`, `rnode_noise_floor`, `rnode_interference_dbm`, `rnode_airtime_*`, `rnode_channel_load_*`, `rns_rtt_ms` | `abs(new - last) >= threshold` **and** ≥ `tel_update` s since last send |
| Min-interval counter | `uptime_s`, `rns_rxb`, `rns_txb`, `rns_rxs`, `rns_txs`, `rnode_bitrate`, `rnode_announce_*`, `rnode_held_announces` | Any change, ≥ `tel_update` s since last send |
| Topology | `path.<peer_hash>` | One message per peer whose path entry changed |

**Heartbeat cap**: regardless of the above rules, any metric that hasn't been sent in
`tel_max_interval` seconds (default 300 s) is re-sent unconditionally. This bounds the
maximum staleness visible in the UI even for stable metrics.

`tel_update` (minimum resend interval) and `tel_max_interval` (heartbeat cap) are both
runtime-configurable via `set` without restarting the agent.

### Telemetry keys

| Key | Type | Description |
|---|---|---|
| `hostname` | str | System hostname |
| `version` | str | Agent version |
| `uptime_s` | int | Seconds since boot |
| `cpu_pct` | float | CPU usage 0–100 |
| `ram_pct` | float | RAM usage 0–100 |
| `disk_pct` | float | Root filesystem usage 0–100 |
| `temp_c` | float | CPU temperature °C (null if unavailable) |
| `batt_soc_pct` | float | Battery state of charge 0–100 |
| `batt_voltage_v` | float | Battery voltage |
| `batt_power_w` | float | Battery power (positive = charging) |
| `solar_power_w` | float | Solar input power |
| `rns_rxb` | int | Total bytes received by RNS |
| `rns_txb` | int | Total bytes transmitted by RNS |
| `rns_rxs` | int | Total packets received |
| `rns_txs` | int | Total packets transmitted |
| `rnode_airtime_short` | float | RNode airtime % (short window) |
| `rnode_airtime_long` | float | RNode airtime % (long window) |
| `rnode_channel_load_short` | float | Channel load % (short window) |
| `rnode_channel_load_long` | float | Channel load % (long window) |
| `rnode_bitrate` | int | Current bitrate bits/s |
| `rnode_noise_floor` | float | Noise floor dBm |
| `rnode_interference_dbm` | float | Interference level dBm |
| `rnode_announce_in` | float | Incoming announce rate announces/s |
| `rnode_announce_out` | float | Outgoing announce rate announces/s |
| `rnode_held_announces` | int | Queued announces |
| `path.<peer_hash>` | str | `<hops>,<iface>,<bitrate>,<rssi>,<snr>` |
| `rns_rtt_ms` | float | Round-trip time to server in ms (updated after each timesync) |
| `errors` | str | Comma-separated active error codes |

## Time sync

The node runs NTP-style clock sync against each server (default every 12 hours, first
sync ~90 seconds after startup). Four timestamps are exchanged:

```
Node                              Server
 |                                  |
 |-- timesync t1=<T1_ns> --------> |  T2 = server receive time
 |                                  |  T3 = server send time
 |<- timesync t1=<T1> t2=<T2_ns> t3=<T3_ns> --
T4 = node receive time (now)       |
```

All timestamps are Unix nanoseconds (`time.time_ns()`).

**Clock offset and RTT** computed on the node:
```
offset = ((T2 - T1) + (T3 - T4)) / 2     # nanoseconds
rtt    = (T4 - T1) - (T3 - T2)            # nanoseconds
```

The reply echoes T1 so the node can verify it matches the most recent request (stale
or duplicate replies are silently discarded).

**Clock correction**: if `abs(offset) >= 500ms` and `abs(offset) <= 24h`, the node
corrects its system clock via `date -s`. Offsets under 500ms are considered network
jitter; offsets over 24h are more likely a misconfiguration than drift.

**RTT telemetry**: after each sync, `rns_rtt_ms` is stored and picked up by the
normal telemetry loop on the next poll, sent to the server as `tel rns_rtt_ms=<value>`
subject to the same threshold gate (5ms change) as other gauges.

**`time_sync_interval`** in `agent.json` controls the repeat period (default 43200 s
= 12h). There is no user-visible command to trigger a manual sync — add one if needed.

---

## Security model

- **Signature validation**: both sides check `message.signature_validated` before
  processing any inbound message. Unsigned or invalid-signature messages are silently
  dropped.
- **Source hash allowlist**: the node only executes commands from source hashes listed in
  `server_dest_hashes` (in `agent.json`). The server only stores telemetry from source
  hashes in its node registry. In both cases the hash comes from LXMF's cryptographically
  verified `message.source_hash`, not from any self-reported field in the payload.
- **Runtime trust management**: `trust <hash>` / `untrust <hash>` commands let a trusted
  server update the node's `server_dest_hashes` list at runtime without editing
  `agent.json` by hand. `untrust` refuses to remove the last remaining entry.
- **Root context**: the agent runs as root. Issued commands execute with full system
  privileges. Deploy nodes only in controlled physical environments.
- **No extra encryption layer**: RNS/LXMF links are end-to-end encrypted using identity
  public keys. No additional application-layer encryption is applied.

---

## Agent config (`/etc/rbloxx/agent.json`)

```json
{
  "identity_path":            "/etc/rbloxx/identity",
  "announce_interval":        300,
  "server_dest_hashes":       ["<hex dest hash of server>"],
  "rnode_ports":              ["/dev/ttyUSB0"],
  "shutdown_soc_pct":         0,
  "watchdog_feed_interval_s": 10,
  "watchdog_timeout_s":       300,
  "telemetry_poll_interval":  10,
  "tel_update":               30,
  "tel_max_interval":         300,
  "time_sync_interval":       43200,
  "rns_configdir":            "/etc/rbloxx/rns_agent",
  "power_backend":            "none",
  "power_i2c_bus":            1,
  "power_i2c_addr":           "0x40",
  "thresholds": {
    "disk_full_pct":          90,
    "temp_critical_c":        80,
    "load_high_factor":       2.0,
    "swap_high_pct":          80,
    "batt_critical_pct":      10,
    "zero_traffic_minutes":   15
  }
}
```

| Field | Default | Description |
|---|---|---|
| `identity_path` | `/etc/rbloxx/identity` | RNS identity file |
| `announce_interval` | `300` | Seconds between LXMF announces |
| `server_dest_hashes` | `[]` | Destination hashes of trusted server(s) |
| `rnode_ports` | `[]` | Serial ports monitored for stuck RNode |
| `shutdown_soc_pct` | `0` | Auto-shutdown when battery SoC ≤ this value; `0` = disabled |
| `watchdog_feed_interval_s` | `10` | `/dev/watchdog` heartbeat interval |
| `watchdog_timeout_s` | `300` | Config-rollback window after `put_config` (seconds) |
| `telemetry_poll_interval` | `10` | How often to sample metrics (seconds) |
| `tel_update` | `30` | Minimum seconds between re-sends of any one metric |
| `tel_max_interval` | `300` | Force-resend interval even with no change (heartbeat cap) |
| `time_sync_interval` | `43200` | Seconds between NTP-style time sync attempts (12 h) |
| `rns_configdir` | `/etc/rbloxx/rns_agent` | RNS config dir for the standalone agent RNS instance |
| `power_backend` | `none` | `none` / `ina226` / `ina219` |
| `power_i2c_bus` | `1` | I²C bus for power backend |
| `power_i2c_addr` | `"0x40"` | I²C address for power backend |

---

## Error codes

Reported in `tel errors=<code1>,<code2>,...` whenever the active-errors set changes.

| Code | Trigger |
|---|---|
| `batt_critical` | Battery SoC ≤ threshold (default 10%) |
| `batt_sensor_unavail` | Power backend failed to initialise or read |
| `disk_full` | Root filesystem usage ≥ threshold (default 90%) |
| `temp_critical` | CPU temperature ≥ threshold (default 80 °C) |
| `config_apply_failed` | `put_config` service restart failed |
| `config_rollback` | Config rolled back after failed restart |
| `rnode_update_failed` | `rnodeconf --update` returned non-zero |
| `rnode_usb_reset` | RNode stuck (zero traffic) — USB reset attempted |
| `rnode_restart` | USB reset failed, rnsd restarted instead |
| `fs_readonly` | Root filesystem mounted read-only |
| `fs_errors` | I/O or ext4 errors seen in dmesg |
| `oom_killed` | OOM killer fired (journalctl, last 5 min) |
| `watchdog_reboot` | Previous boot ended by hardware watchdog |
| `load_high` | 1-min load average / CPU count ≥ threshold (default 2.0) |
| `swap_high` | Swap usage ≥ threshold (default 80%) |
| `no_charging` | Solar present but battery power is negative |

---

## RNode auto-recovery

The agent monitors each port in `rnode_ports` once per minute. If byte counts (rx + tx)
have not changed for `thresholds.zero_traffic_minutes` (default 15):

1. Attempt `usbreset <port>` (USB level reset)
2. Wait 5 seconds; check if the interface reappears in RNS stats
3. If not recovered: `systemctl restart rnsd`

Transient error codes `rnode_usb_reset` / `rnode_restart` appear in the next telemetry
error report and clear automatically on the following poll.
