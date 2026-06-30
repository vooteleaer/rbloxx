# RBloxx command tutorial

This is a practical, by-example guide to the node agent's command-line
grammar — what to type, what comes back, and the gotchas. For wire-format
details (LXMF envelope, authentication model), see `PROTOCOL.md`.

## How to send a command

Address an LXMF message directly to the node's destination hash, with the
command line as the message **content** (not the title/subject — many LXMF
clients, including MeshChat, don't render `title`, so the node ignores it
entirely). Only messages with a valid signature from a hash in the node's
`server_dest_hashes` trust list are accepted — everything else is silently
dropped.

The reply comes back the same way: content starts with `OK:` or `ERR:`,
followed by any output text.

```
You send:    svc restart rnsd
Node replies: OK                          (bare OK/ERR when there's no output text)

You send:    get cr
Node replies: OK: cr=7

You send:    frobnicate
Node replies: ERR: unknown command: frobnicate
```

If you don't remember a command, just ask:

```
help              -> lists every command, one line each
help svc          -> usage for just "svc"
```

## Quick reference

| Command | What it does |
|---|---|
| `help [command]` | List all commands, or show usage for one |
| `get config <type>` | Fetch a full config file (`rns`, `agent`, or `system`) |
| `get <key>` | Read one runtime/radio/system/wifi value (quote multi-word values) |
| `set KEY=VALUE [...]` | Set one or more runtime/radio/system/wifi values (quote multi-word values) |
| `put config <type>` | Replace a full config file |
| `patch config <type>` | Patch specific INI keys without rewriting the whole file |
| `svc restart\|stop\|start <service>` | Control a systemd unit |
| `reboot [delay_s]` | Reboot the node |
| `shutdown [delay_s]` | Power off the node |
| `wifi on\|off [profile]` | Toggle Wi-Fi |
| `announce` | Send an RNS/LXMF announce immediately |
| `ping <dest_hash>` | Lightweight reachability probe |
| `log pull [lines] [unit]` | Pull recent systemd journal lines |
| `disk cleanup` | Vacuum old journal logs to free disk space |
| `agent update` | `git pull` the agent code, then restart it |
| `rnode reset\|update <port>` | Reset or flash firmware on an RNode |
| `get telem` | Ask the node to immediately resend all current telemetry values |
| `get ifstatus` | Get online/offline status for every RNS interface |
| `trust <hash>` / `untrust <hash>` | Manage the trusted-server list |

## Everyday admin

**Restart a service:**
```
svc restart rnsd
svc restart rbloxx-agent
```
Service name is whatever systemd unit you want — not limited to RBloxx's own
services.

**Pull recent logs:**
```
log pull              -> last 100 lines, all units
log pull 300           -> last 300 lines
log pull 300 rnsd      -> last 300 lines from rnsd specifically
```

**Free up disk space** (vacuums journal logs older than 7 days):
```
disk cleanup
```

**Reboot or power off**, optionally delayed (default 5s either way):
```
reboot
reboot 30
shutdown
```

**Update the agent itself** (`git pull` + restart):
```
agent update
```

**Toggle Wi-Fi**, optionally bringing up a specific NetworkManager profile:
```
wifi off
wifi on
wifi on home-network
```

**Check reachability** to some other destination (1-byte probe, not a full
LXMF round trip):
```
ping a2202951bf268e16ce90235f7dcd16d0
```

**RNode firmware maintenance** (port is the serial device):
```
rnode reset /dev/ttyUSB0
rnode update /dev/ttyUSB0
```

## Reading and writing config

```
get config rns         -> full text of the reticulum config file
get config agent        -> full text of agent.json
get config system       -> ip addr / nmcli device output
```

`put config <type>` replaces a config file wholesale — the message content
*after the command line* (everything past the first newline) becomes the new
file. `patch config <type>` is the surgical alternative: content is plain
text, one `<section> <key>=<value>` per line, applied as INI patches without
touching anything else in the file. Both go through a commit-or-rollback
safety net — if the node can't reach a trusted server again within
`watchdog_timeout_s` (default 300s) after applying the change, it
automatically restores the previous file.

For routine radio tuning, prefer `set` (below) over hand-crafting a `patch
config rns` — it's shorter and doesn't require knowing the INI section name.

## `set` / `get` — runtime, radio, system, and wifi values

One unified key space, read with `get <key>`, written with `set
KEY=VALUE [KEY=VALUE ...]`. Spacing around `=` doesn't matter, you can set
several keys in one line, and values with spaces just need quoting (single
or double quotes both work):

```
set CR = 7 SF = 5 Freq = 896.5
set CR=7
get freq
set wifi_network="cafa tech" wifi_psk="my password"
```

**Radio params** (resolved against the live `rns` config's RNodeInterface
section, applied atomically via the same commit-or-rollback path as `patch
config`):

| Key | Maps to | Notes |
|---|---|---|
| `cr` | `codingrate` | |
| `sf` | `spreadingfactor` | |
| `bw` | `bandwidth` | Hz |
| `txp` | `txpower` | dBm |
| `freq` | `frequency` | **input in MHz** (e.g. `869.5`), stored as Hz |

**Runtime keys** (in-memory only, take effect immediately, not persisted to
any file — reset to their `agent.json` default on next restart):

| Key | Meaning |
|---|---|
| `shutdown_threshold` | Battery % below which the node auto-shuts-down (0 disables) |
| `tel_update` | Minimum seconds between re-sends of any one telemetry metric (default 30) |
| `tel_max_interval` | Force-resend interval — a metric is sent after this many seconds even with no change (default 300, the heartbeat cap) |

**System keys** (applied directly to the OS, not via systemd's dbus —
deliberately avoided since not every image runs one):

| Key | Format | Effect |
|---|---|---|
| `hostname` | any valid hostname | Updates OS hostname **and** the RNode's `id_callsign`/`discovery_name`, restarts the agent so the next announce carries it |
| `clock` | `HH:MM` or `HH:MM:SS` (24h) | Sets time of day, keeps current date |
| `date` | `YYYY-MM-DD` | Sets the date, keeps current time of day |

```
set hostname=Relay-North
set clock=14:30
set date=2026-07-01
```

Unknown keys, or malformed values (e.g. `set clock=99:99`), are rejected
*before* anything is applied — a `set` line with one bad key changes nothing,
not just the bad one.

**Wi-Fi credentials** (separate from the `wifi on|off` toggle above, which
only controls the radio — these control which network it connects to):

| Key | Notes |
|---|---|
| `wifi_network` | The SSID to connect to. Quote it if it has spaces. |
| `wifi_psk` | The network password. Quote it if it has spaces. Never readable back. |

`wifi_network` and `wifi_psk` can be set together in one line or in separate
commands — whichever arrives, the node just remembers it and waits for the
other:

```
set wifi_network="cafa tech"        -> staged, waiting for wifi_psk
set wifi_psk="my password"          -> both known now, connects via nmcli

set wifi_network="cafa tech" wifi_psk="my password"   -> connects immediately
```

`get wifi_network` shows the currently staged/last-used SSID. `get
wifi_psk` always refuses — the agent will never echo a password back over
the wire, even to a trusted server. A failed connection attempt keeps both
values in memory so you can retry just the wrong one (e.g. fix `wifi_psk`
without retyping `wifi_network`); a successful connection clears both.

## Telemetry and interface status

**Force a full telemetry resend** — the node immediately sends a `tel <key>=<value>`
message for every metric it knows about, regardless of whether anything has changed.
Values still arrive as separate messages, not in the command reply:

```
get telem
```

This is useful when the UI is showing stale or missing values, or right after adding a
new node, without having to wait for the heartbeat cap to fire.

**Check interface status** — returns one line per RNS interface, showing whether it
is currently online or offline (keyed by the `[[Section Name]]` from the RNS config):

```
get ifstatus
-> OK: RNode=online
   Local TCP=online
   AutoInterface=offline
```

## Trust management

The node only accepts commands from destination hashes in its
`server_dest_hashes` list. Manage that list live, without editing
`agent.json` by hand:

```
trust 90bf8c417cd52103815eaf370387adb5
untrust 90bf8c417cd52103815eaf370387adb5
```

`untrust` refuses to remove the last remaining trusted hash — there's no
command that can lock the node out of remote administration.

## What you'll never need to send

`tel <key>=<value>` and `cfg <type>` are real verbs in the same grammar, but
they only ever flow *node → server* (telemetry reports and periodic config
snapshots) — you'll see them arrive, never send them yourself.
