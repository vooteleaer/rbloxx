"""Shared MeshCore-style CLI grammar for RBloxx node <-> server communication.

Every LXMF message's purpose is read from the leading verb(s) of its
LXMessage.title via parse_cli() -- there is no separate envelope/type-tag
concept. Command verbs (svc, get, set, put, patch, reboot, shutdown, wifi,
announce, ping, log, disk, agent, rnode, trust, untrust) flow server->node;
report verbs (tel, cfg) flow node->server. Results are just "OK"/"ERR" and
are not parsed here (checked directly against the literal title).

Pure string/dict logic only -- no RNS/LXMF imports, so this module is fully
unit-testable in isolation.
"""

import re
import shlex

# Radio-parameter aliases for the `set` verb, resolved against the live `rns`
# config's RNodeInterface section. Keys are matched case-insensitively.
RADIO_ALIASES = {
    "cr": "codingrate",
    "sf": "spreadingfactor",
    "bw": "bandwidth",
    "txp": "txpower",
    "freq": "frequency",  # input in MHz, converted to Hz before writing
}

# `set` keys that are applied to in-memory agent state only, never persisted
# (matches today's shutdown_threshold behavior).
RUNTIME_KEYS = {"shutdown_threshold", "tel_update", "tel_max_interval"}

# `set` keys that apply directly to the OS (hostnamectl/timedatectl), not to
# any config file or in-memory agent state.
SYSTEM_KEYS = {"hostname", "clock", "date"}

# `set` keys for wifi network credentials -- can be set independently of each
# other (remembered in memory until both are known), then connect via nmcli.
# Separate from the existing "wifi on|off" bare verb, which only toggles the
# radio and is unaffected by these.
WIFI_CRED_KEYS = {"wifi_network", "wifi_psk"}

# One-line usage text per command, keyed by its CLI prefix -- doubles as the
# source for ValueError usage messages and for the `help`/`help <command>` verb.
HELP_TEXT = {
    "svc": "svc restart|stop|start <service> -- restart/stop/start a systemd unit",
    "get": "get config <type> -- fetch full config (rns|agent|system); "
           "get telem -- force an immediate resend of every telemetry value "
           "(each still arrives as its own separate tel message, not in the reply); "
           "get ifstatus -- online/offline per interface, one 'name=online|offline' "
           "line per interface, keyed by the [[Section Name]] used in the rns config; "
           "get <key> -- read one runtime/radio/system/wifi value "
           "(shutdown_threshold, tel_update, tel_max_interval, cr, sf, bw, txp, freq, hostname, clock, date, "
           "wifi_network -- wifi_psk is never read back)",
    "put": "put config <type> -- replace full config; content = file text",
    "patch": "patch config <type> -- patch config; content = '<section> <key>=<value>' lines",
    "reboot": "reboot [delay_s] -- reboot the node (default delay 5s)",
    "shutdown": "shutdown [delay_s] -- shut down the node (default delay 5s)",
    "wifi": "wifi on|off [profile] -- toggle wifi, optionally selecting a profile",
    "announce": "announce -- send an RNS/LXMF announce now",
    "ping": "ping <dest_hash> -- connectivity check against a destination",
    "log": "log pull [lines] [unit] -- pull last N log lines (default 100), optionally for one systemd unit",
    "disk": "disk cleanup -- run disk cleanup routine",
    "agent": "agent update -- update and restart the rbloxx-agent",
    "rnode": "rnode reset|update <port> -- reset/update RNode firmware on a serial port",
    "trust": "trust <hash> -- add a destination hash to the trusted-server list",
    "untrust": "untrust <hash> -- remove a destination hash from the trusted-server list",
    "set": "set KEY=VALUE [KEY=VALUE ...] -- set runtime/radio/system/wifi params "
           "(shutdown_threshold, tel_update, tel_max_interval, cr, sf, bw, txp, freq, hostname, clock, date, "
           "wifi_network, wifi_psk -- quote values with spaces, e.g. wifi_network=\"cafa tech\"); "
           "wifi_network/wifi_psk can be set in separate commands -- nmcli connects once both are known; "
           "tel_max_interval is the heartbeat cap -- a metric is resent after this many seconds even "
           "with no qualifying change (default 300s)",
    "help": "help [command] -- list all commands, or show usage for one command",
}


def help_text(topic: str | None = None) -> str:
    """Return help text: full command list, or usage for a single verb."""
    if topic:
        line = HELP_TEXT.get(topic.lower())
        if line is None:
            return f"no help for '{topic}' -- try 'help' for the full list"
        return line
    return "\n".join(HELP_TEXT.values())


def _parse_set_pairs(remainder: str) -> list[tuple[str, str]]:
    """Tokenize `set`'s argument list into KEY=VALUE pairs.

    Uses shlex so quoted values can contain spaces ('KEY="some value"'),
    then walks tokens to reassemble a pair regardless of how `=` is spaced:
    "KEY=VALUE" (one token), "KEY= VALUE" / "KEY =VALUE" (two tokens), or
    "KEY = VALUE" (three tokens).
    """
    try:
        tokens = shlex.split(remainder)
    except ValueError as e:
        raise ValueError(f"usage: set KEY=VALUE [KEY=VALUE ...] ({e})")

    pairs: list[tuple[str, str]] = []
    i = 0
    while i < len(tokens):
        token = tokens[i]
        if "=" in token:
            key, _, val = token.partition("=")
            if not key:
                raise ValueError(f"usage: set KEY=VALUE [KEY=VALUE ...] (bad token: {token!r})")
            if val:
                pairs.append((key, val))
                i += 1
            else:
                if i + 1 >= len(tokens):
                    raise ValueError(f"usage: set KEY=VALUE [KEY=VALUE ...] (missing value for {key!r})")
                pairs.append((key, tokens[i + 1]))
                i += 2
        else:
            key = token
            if i + 1 >= len(tokens):
                raise ValueError(f"usage: set KEY=VALUE [KEY=VALUE ...] (missing '=' for {key!r})")
            nxt = tokens[i + 1]
            if nxt == "=":
                if i + 2 >= len(tokens):
                    raise ValueError(f"usage: set KEY=VALUE [KEY=VALUE ...] (missing value for {key!r})")
                pairs.append((key, tokens[i + 2]))
                i += 3
            elif nxt.startswith("="):
                pairs.append((key, nxt[1:]))
                i += 2
            else:
                raise ValueError(f"usage: set KEY=VALUE [KEY=VALUE ...] (expected '=' after {key!r})")
    return pairs


def parse_cli(line: str) -> tuple[str, dict]:
    """Parse one CLI line into (name, kwargs).

    `name` is the same identifier the old structured-dict commands used
    (e.g. "svc_restart", "get_config") so callers' existing dispatch tables
    and key lookups don't need to change. Raises ValueError on malformed or
    unknown input.
    """
    line = line.strip()
    if not line:
        raise ValueError("empty command")

    # `set` takes one or more KEY=VALUE pairs, shlex-tokenized so quoted
    # values can contain spaces (e.g. wifi_network="cafa tech"), while still
    # accepting any spacing around `=` ("CR=7", "CR = 7", "CR= 7", "CR =7").
    m = re.match(r"(?i)^set(\s+.*)?$", line)
    if m:
        pairs = _parse_set_pairs(m.group(1) or "")
        if not pairs:
            raise ValueError("usage: set KEY=VALUE [KEY=VALUE ...]")
        return "set", {"pairs": pairs}

    tokens = shlex.split(line)
    if not tokens:
        raise ValueError("empty command")
    verb = tokens[0].lower()
    rest = tokens[1:]

    if verb == "svc":
        if len(rest) != 2 or rest[0] not in ("restart", "stop", "start"):
            raise ValueError("usage: svc restart|stop|start <service>")
        return f"svc_{rest[0]}", {"service": rest[1]}

    if verb == "get" and rest[:1] == ["config"]:
        if len(rest) != 2:
            raise ValueError("usage: get config <type>")
        return "get_config", {"type": rest[1]}

    if verb == "get" and rest == ["telem"]:
        return "get_telemetry", {}

    if verb == "get" and rest == ["ifstatus"]:
        return "get_ifstatus", {}

    if verb == "get":
        if len(rest) != 1:
            raise ValueError("usage: get config <type> | get <key>")
        return "get_value", {"key": rest[0]}

    if verb == "put" and rest[:1] == ["config"]:
        if len(rest) != 2:
            raise ValueError("usage: put config <type>")
        return "put_config", {"type": rest[1]}

    if verb == "patch" and rest[:1] == ["config"]:
        if len(rest) != 2:
            raise ValueError("usage: patch config <type>")
        return "patch_config", {"type": rest[1]}

    if verb == "reboot":
        if len(rest) > 1:
            raise ValueError("usage: reboot [delay_s]")
        return "reboot", {"delay_s": int(rest[0]) if rest else 5}

    if verb == "shutdown":
        if len(rest) > 1:
            raise ValueError("usage: shutdown [delay_s]")
        return "shutdown", {"delay_s": int(rest[0]) if rest else 5}

    if verb == "wifi":
        if not rest or rest[0] not in ("on", "off") or len(rest) > 2:
            raise ValueError("usage: wifi on|off [profile]")
        return "wifi_set", {
            "enabled": rest[0] == "on",
            "profile": rest[1] if len(rest) > 1 else None,
        }

    if verb == "announce":
        if rest:
            raise ValueError("usage: announce")
        return "rns_announce", {}

    if verb == "ping":
        if len(rest) != 1:
            raise ValueError("usage: ping <dest_hash>")
        return "connectivity_check", {"dest_hash": rest[0]}

    if verb == "log" and rest[:1] == ["pull"]:
        args = rest[1:]
        if len(args) > 2:
            raise ValueError("usage: log pull [lines] [unit]")
        return "log_pull", {
            "lines": int(args[0]) if len(args) > 0 else 100,
            "unit": args[1] if len(args) > 1 else None,
        }

    if verb == "disk":
        if rest != ["cleanup"]:
            raise ValueError("usage: disk cleanup")
        return "disk_cleanup", {}

    if verb == "agent":
        if rest != ["update"]:
            raise ValueError("usage: agent update")
        return "agent_update", {}

    if verb == "rnode":
        if len(rest) != 2 or rest[0] not in ("reset", "update"):
            raise ValueError("usage: rnode reset|update <port>")
        return f"rnode_{rest[0]}", {"port": rest[1]}

    if verb == "trust":
        if len(rest) != 1:
            raise ValueError("usage: trust <hash>")
        return "trust", {"hash": rest[0]}

    if verb == "untrust":
        if len(rest) != 1:
            raise ValueError("usage: untrust <hash>")
        return "untrust", {"hash": rest[0]}

    if verb == "tel":
        if len(rest) != 1 or "=" not in rest[0]:
            raise ValueError("usage: tel <key>=<value>")
        key, _, value = rest[0].partition("=")
        return "tel", {"key": key, "value": value}

    if verb == "cfg":
        if len(rest) != 1:
            raise ValueError("usage: cfg <type>")
        return "cfg", {"type": rest[0]}

    if verb == "help":
        if len(rest) > 1:
            raise ValueError("usage: help [command]")
        return "help", {"topic": rest[0] if rest else None}

    raise ValueError(f"unknown command: {verb}")


def cmd_dict_to_cli(cmd: dict) -> tuple[str, bytes | None]:
    """Translate an old structured-dict command (REST body shape) into a
    (cli_line, content_bytes_or_None) pair. The one and only call site is
    server-side send_command(); content is always plain UTF-8 text, never
    msgpack/binary.
    """
    name = cmd.get("cmd", "")

    if name in ("svc_restart", "svc_stop", "svc_start"):
        action = name.split("_")[1]
        return f"svc {action} {cmd['service']}", None
    if name == "get_config":
        return f"get config {cmd['type']}", None
    if name == "get_telemetry":
        return "get telem", None
    if name == "get_ifstatus":
        return "get ifstatus", None
    if name == "put_config":
        return f"put config {cmd['type']}", cmd["content"].encode("utf-8")
    if name == "patch_config":
        return f"patch config {cmd['type']}", encode_patches(cmd["patches"])
    if name == "reboot":
        return f"reboot {cmd.get('delay_s', 5)}", None
    if name == "shutdown":
        return f"shutdown {cmd.get('delay_s', 5)}", None
    if name == "wifi_set":
        line = f"wifi {'on' if cmd['enabled'] else 'off'}"
        if cmd.get("profile"):
            line += f" {cmd['profile']}"
        return line, None
    if name == "rns_announce":
        return "announce", None
    if name == "connectivity_check":
        return f"ping {cmd['dest_hash']}", None
    if name == "log_pull":
        line = f"log pull {cmd.get('lines', 100)}"
        if cmd.get("unit"):
            line += f" {cmd['unit']}"
        return line, None
    if name == "disk_cleanup":
        return "disk cleanup", None
    if name == "agent_update":
        return "agent update", None
    if name == "rnode_reset":
        return f"rnode reset {cmd['port']}", None
    if name == "rnode_update":
        return f"rnode update {cmd['port']}", None
    if name == "shutdown_threshold":
        return f"set shutdown_threshold={cmd['soc_pct']}", None

    raise ValueError(f"unknown command dict: {name!r}")


def encode_patches(patches: list[dict]) -> bytes:
    """[{section,key,value}, ...] -> plain text, one '<section> <key>=<value>' per line."""
    lines = [f"{p['section']} {p['key']}={p['value']}" for p in patches]
    return "\n".join(lines).encode("utf-8")


def decode_patches(content: bytes) -> list[dict]:
    """Inverse of encode_patches()."""
    patches = []
    for line in content.decode("utf-8").splitlines():
        line = line.strip()
        if not line:
            continue
        section, _, rest = line.partition(" ")
        key, _, value = rest.partition("=")
        patches.append({"section": section, "key": key, "value": value})
    return patches
