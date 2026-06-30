"""RBloxx node agent — runs alongside rnsd on each remote node."""

import os
import re
import sys
import socket
import subprocess
import threading
import time
from datetime import datetime
from pathlib import Path

import json

import RNS
import LXMF

# Suppress shared-instance RPC digest bug (RNS 1.2.5–1.3.x):
# _used_destination_data calls rpc_connection.recv() but rnsd never
# sends a response in client mode, raising EOFError that propagates
# through announce() / Packet.send() and kills the calling thread.
if hasattr(RNS.Reticulum, "_used_destination_data"):
    _rns_orig_udd = RNS.Reticulum._used_destination_data
    def _rns_safe_udd(self, dest_hash):
        try:
            _rns_orig_udd(self, dest_hash)
        except Exception:
            pass
    RNS.Reticulum._used_destination_data = _rns_safe_udd

sys.path.insert(0, str(Path(__file__).parent.parent / "shared"))
from protocol import FIELD_TXN
from cli_grammar import (
    parse_cli, decode_patches, help_text,
    RADIO_ALIASES, RUNTIME_KEYS, SYSTEM_KEYS, WIFI_CRED_KEYS,
)
from config_handler import ConfigHandler
from system_handler import SystemHandler
from power_handler import PowerHandler

# Telemetry delta-send rules (see PROTOCOL.md / plan §1.1).
# Gauges: send only past this absolute delta, rate-limited to telemetry_min_interval.
TELEMETRY_THRESHOLDS = {
    "cpu_pct": 1.0, "ram_pct": 1.0, "disk_pct": 1.0, "temp_c": 1.0,
    "batt_soc_pct": 1.0, "batt_power_w": 0.5,
    "rnode_noise_floor": 1.0, "rnode_interference_dbm": 1.0,
    "rnode_airtime_short": 1.0, "rnode_airtime_long": 1.0,
    "rnode_channel_load_short": 1.0, "rnode_channel_load_long": 1.0,
}
# Monotonic counters: any change counts, rate-limited to telemetry_min_interval.
TELEMETRY_COUNTER_KEYS = {
    "rnode_bitrate", "rnode_announce_in", "rnode_announce_out", "rnode_held_announces",
}
TELEMETRY_MIN_INTERVAL_DEFAULT = 30
# Heartbeat cap: force a resend of a threshold/counter-gated metric after this
# long even with no qualifying change, so a quiet value (RAM/disk/bitrate on an
# idle node) doesn't go stale in the UI for an unbounded amount of time.
TELEMETRY_MAX_INTERVAL_DEFAULT = 300


class RBloxxAgent:
    def __init__(self, config_path: str = "/etc/rbloxx/agent.json"):
        self.cfg = self._load_config(config_path)
        self.identity_path = Path(self.cfg.get("identity_path", "/etc/rbloxx/identity"))
        self.announce_interval: int = self.cfg.get("announce_interval", 300)
        self.telemetry_poll_interval: int = self.cfg.get("telemetry_poll_interval", 10)
        # Single cap on how often a changed metric may be re-sent, for both
        # threshold-gated gauges and rate-limited counters -- set live via
        # `set tel_update=<seconds>` / read via `get tel_update`.
        self.telemetry_min_interval: float = self.cfg.get("tel_update", TELEMETRY_MIN_INTERVAL_DEFAULT)
        # Heartbeat cap -- set live via `set tel_max_interval=<seconds>` /
        # read via `get tel_max_interval`.
        self.telemetry_max_interval: float = self.cfg.get("tel_max_interval", TELEMETRY_MAX_INTERVAL_DEFAULT)
        self.server_dest_hashes: list[str] = self.cfg.get("server_dest_hashes", [])
        self.shutdown_soc_pct: float = self.cfg.get("shutdown_soc_pct", 0)
        # NomadNet status page: the real `nomadnet` daemon owns the RNS side
        # (its own nomadnetwork.node destination, announces, Link handling --
        # all the production-tested protocol code). This agent just answers
        # over a local socket so an executable index.mu page (node/nomadnet_page.py)
        # can ask it to render the page / apply a submitted field, reusing the
        # exact same state and _set()/_get_value() logic as the LXMF commands.
        self.nomadnet_enabled: bool = self.cfg.get("nomadnet_page", True)
        self.nomadnet_socket_path: str = self.cfg.get("nomadnet_socket", "/run/rbloxx/nomadnet.sock")

        # wifi_network/wifi_psk can arrive in separate `set` commands -- held
        # here until both are known, then nmcli connects. Never persisted,
        # never read back (wifi_psk especially, to avoid echoing a secret).
        self._wifi_network: str | None = None
        self._wifi_psk: str | None = None

        # Event-driven telemetry: last value/time sent per metric key.
        self._last_sent: dict[str, str] = {}
        self._last_sent_time: dict[str, float] = {}

        self.config_handler = ConfigHandler(self.cfg, config_path=config_path)
        self.system_handler = SystemHandler(self.cfg)
        self.power_handler = PowerHandler(self.cfg)

        self._rns: RNS.Reticulum | None = None
        self._router: LXMF.LXMRouter | None = None
        self._dest: RNS.Destination | None = None
        self._running = False

    # ------------------------------------------------------------------
    # Startup
    # ------------------------------------------------------------------

    def start(self) -> None:
        identity = self._load_or_create_identity()
        rns_configdir = self.cfg.get("rns_configdir")
        if rns_configdir:
            # Standalone mode with custom config dir (TCPClientInterface to local rnsd).
            # Avoids shared-instance RPC auth issues that break get_interface_stats().
            self._ensure_standalone_rns_config(rns_configdir)
            self._rns = RNS.Reticulum(configdir=rns_configdir)
        else:
            self._rns = RNS.Reticulum(require_shared_instance=True)

        self._router = LXMF.LXMRouter(
            identity=identity,
            storagepath=str(self.identity_path.parent),
        )
        self._dest = self._router.register_delivery_identity(
            identity, display_name=socket.gethostname(),
        )
        self._router.register_delivery_callback(self._handle_lxm)

        self._running = True
        threading.Thread(target=self._watchdog_loop, daemon=True, name="watchdog").start()
        threading.Thread(target=self._rnode_monitor_loop, daemon=True, name="rnode-monitor").start()
        threading.Thread(target=self._telemetry_loop, daemon=True, name="telemetry-loop").start()
        threading.Thread(target=self._main_loop, daemon=True, name="main-loop").start()
        if self.nomadnet_enabled:
            threading.Thread(target=self._nomadnet_socket_loop, daemon=True, name="nomadnet-socket").start()

        RNS.log(f"RBloxx agent started — dest {RNS.prettyhexrep(self._dest.hash)}", RNS.LOG_NOTICE)

        try:
            while self._running:
                time.sleep(1)
        except KeyboardInterrupt:
            self._running = False

    def _load_config(self, path: str) -> dict:
        try:
            with open(path) as f:
                return json.load(f)
        except FileNotFoundError:
            return {}
        except json.JSONDecodeError as e:
            raise SystemExit(f"Config parse error in {path}: {e}")

    def _load_or_create_identity(self) -> RNS.Identity:
        if self.identity_path.exists():
            return RNS.Identity.from_file(str(self.identity_path))
        identity = RNS.Identity()
        self.identity_path.parent.mkdir(parents=True, exist_ok=True)
        identity.to_file(str(self.identity_path))
        RNS.log(f"Created new node identity: {identity.hash.hex()}", RNS.LOG_NOTICE)
        return identity

    def _ensure_standalone_rns_config(self, configdir: str) -> None:
        """Auto-create a standalone RNS config using TCPClientInterface to local rnsd.

        rnsd must have a TCPServerInterface on localhost:{port} (4965 by default).
        This lets the agent call get_interface_stats() without the shared-instance
        RPC auth failure that blocks RNode stat collection.
        """
        config_path = Path(configdir) / "config"
        if config_path.exists():
            return
        port = self.cfg.get("rns_local_port", 4965)
        Path(configdir).mkdir(parents=True, exist_ok=True)
        config_path.write_text(
            "[reticulum]\n"
            "  enable_transport = False\n"
            "  share_instance = No\n\n"
            "[logging]\n"
            "  loglevel = 4\n\n"
            "[interfaces]\n\n"
            "  [[local-rnsd]]\n"
            "    type = TCPClientInterface\n"
            "    interface_enabled = True\n"
            "    target_host = 127.0.0.1\n"
            f"    target_port = {port}\n",
            encoding="utf-8",
        )
        RNS.log(f"Created standalone RNS config at {config_path} (port {port})", RNS.LOG_NOTICE)

    # ------------------------------------------------------------------
    # Main loop — announce + one-time config push + auto-shutdown check
    # ------------------------------------------------------------------

    def _main_loop(self) -> None:
        self._check_pending_rollback()
        self._wait_for_server_identity()
        first = True
        while self._running:
            try:
                self._announce()
                if first:
                    for dest_hash_hex in self.server_dest_hashes:
                        self._push_configs(dest_hash_hex)
                    first = False
                self._check_auto_shutdown()
            except Exception as e:
                RNS.log(f"Main loop error (will retry): {e}", RNS.LOG_ERROR)
            self._sleep_interruptible(self.announce_interval)

    def _wait_for_server_identity(self) -> None:
        """Block until we can recall at least one server's identity (needed to send packets)."""
        if not self.server_dest_hashes:
            return
        while self._running:
            for h in self.server_dest_hashes:
                if RNS.Identity.recall(bytes.fromhex(h)) is not None:
                    return
                RNS.Transport.request_path(bytes.fromhex(h))
            for _ in range(30):
                if not self._running:
                    return
                if any(RNS.Identity.recall(bytes.fromhex(h)) is not None
                       for h in self.server_dest_hashes):
                    return
                time.sleep(1)

    def _sleep_interruptible(self, seconds: int) -> None:
        for _ in range(seconds):
            if not self._running:
                break
            time.sleep(1)

    def _announce(self) -> None:
        self._dest.announce()

    # ------------------------------------------------------------------
    # Telemetry — event-driven, one message per changed metric
    # ------------------------------------------------------------------

    def _telemetry_loop(self) -> None:
        while self._running:
            try:
                self._sample_and_send_telemetry()
            except Exception as e:
                RNS.log(f"Telemetry sample error (will retry): {e}", RNS.LOG_WARNING)
            self._sleep_interruptible(self.telemetry_poll_interval)

    def _sample_and_send_telemetry(self) -> None:
        host_tel, rnode_tel = self._collect_telemetry()
        merged = {**host_tel, **(rnode_tel or {})}
        now = time.time()

        candidates = {k: str(v) for k, v in merged.items() if v is not None}

        for key, value in candidates.items():
            if self._telemetry_send_due(key, value, now):
                line = f"tel {key}={value}".encode("utf-8")
                for dest_hash_hex in self.server_dest_hashes:
                    self._send_lxm(dest_hash_hex, content=line)

    def _send_full_telemetry(self) -> dict:
        """`get telem` -- force-resend every currently known metric right now,
        bypassing the usual threshold/rate-limit gate. Each metric still goes
        out as its own separate "tel key=value" message (same as the regular
        poll loop), not bundled into this command's OK reply.
        """
        host_tel, rnode_tel = self._collect_telemetry()
        merged = {**host_tel, **(rnode_tel or {})}
        now = time.time()
        sent = 0
        for key, value in merged.items():
            if value is None:
                continue
            value = str(value)
            line = f"tel {key}={value}".encode("utf-8")
            for dest_hash_hex in self.server_dest_hashes:
                self._send_lxm(dest_hash_hex, content=line)
            self._last_sent[key] = value
            self._last_sent_time[key] = now
            sent += 1
        return {"ok": True, "output": f"sent {sent} telemetry values"}

    def _telemetry_send_due(self, key: str, value: str, now: float) -> bool:
        """Decide if `key` should be (re)sent given its last-sent value/time, and
        record the send if so. One rule set per metric kind (see module-level
        TELEMETRY_THRESHOLDS/TELEMETRY_COUNTER_KEYS): threshold+rate-limited
        gauges, rate-limited monotonic counters/interface byte counts, or
        event-like (send on any change — hostname/version/errors). Threshold/
        counter keys also get a heartbeat: forced due once telemetry_max_interval
        has passed, even with no qualifying change, so a quiet value (RAM/disk/
        bitrate on an idle node) doesn't go stale in the UI indefinitely.
        """
        last_value = self._last_sent.get(key)
        last_time = self._last_sent_time.get(key, 0.0)
        heartbeat_due = (now - last_time) >= self.telemetry_max_interval

        if key in TELEMETRY_THRESHOLDS:
            try:
                changed = last_value is None or abs(float(value) - float(last_value)) >= TELEMETRY_THRESHOLDS[key]
            except (TypeError, ValueError):
                changed = last_value != value
            due = (changed and (now - last_time) >= self.telemetry_min_interval) or heartbeat_due
        elif key in TELEMETRY_COUNTER_KEYS:
            due = ((last_value != value) and (now - last_time) >= self.telemetry_min_interval) or heartbeat_due
        else:
            due = last_value != value

        if due:
            self._last_sent[key] = value
            self._last_sent_time[key] = now
        return due

    def _collect_telemetry(self) -> tuple[dict, dict | None]:
        """Return (host_telemetry, rnode_telemetry). rnode_telemetry is None if no RNode data."""
        sys_info = self.system_handler.collect()
        power_info = self.power_handler.collect()
        rns_stats = self._get_rns_stats()

        rnode_keys = {
            "rnode_airtime_short", "rnode_airtime_long",
            "rnode_channel_load_short", "rnode_channel_load_long",
            "rnode_noise_floor", "rnode_interference_dbm",
            "rnode_bitrate", "rnode_announce_in", "rnode_announce_out",
            "rnode_held_announces",
        }
        rnode_tel = {k: v for k, v in rns_stats.items() if k in rnode_keys and v is not None}

        # Host telemetry is deliberately narrow -- physical radio (above) and
        # these few host vitals only, no interface/connection byte counters.
        host_tel = {
            "cpu_pct": sys_info.get("cpu_pct"),
            "ram_pct": sys_info.get("ram_pct"),
            "disk_pct": sys_info.get("disk_pct"),
            "temp_c": sys_info.get("temp_c"),
            "batt_soc_pct": power_info.get("batt_soc_pct"),
            "batt_power_w": power_info.get("batt_power_w"),
        }

        return host_tel, rnode_tel if rnode_tel else None

    def _get_rnsd_authkey(self) -> bytes | None:
        """Compute the RPC authkey from rnsd's transport identity file.

        rnsd uses the default RNS configdir for the user it runs as.
        The agent typically runs as the same user, so Path.home() is tried first.
        """
        candidates = [
            Path.home() / ".reticulum" / "storage" / "transport_identity",
            Path("/home/reticulum/.reticulum/storage/transport_identity"),
            Path("/root/.reticulum/storage/transport_identity"),
        ]
        for path in candidates:
            if path.exists():
                try:
                    ti = RNS.Identity.from_file(str(path))
                    return RNS.Identity.full_hash(ti.get_private_key())
                except Exception:
                    pass
        return None

    def _get_interface_stats_via_rpc(self) -> dict | None:
        """Get interface stats from rnsd via direct authenticated RPC.

        Works even when the agent uses a different configdir than rnsd (standalone
        mode), because we compute the authkey from rnsd's own transport identity.
        """
        from multiprocessing.connection import Client
        authkey = self._get_rnsd_authkey()
        if not authkey:
            return None
        try:
            conn = Client(b"\x00rns/default/rpc", family="AF_UNIX", authkey=authkey)
            conn.send({"get": "interface_stats"})
            result = conn.recv()
            conn.close()
            return result
        except Exception:
            return None

    def _raw_interface_stats(self) -> dict | None:
        """RNS.Reticulum.get_interface_stats(), unfiltered -- every interface
        rnsd knows about (this node's own + any transport-discovered peers),
        with whatever fields RNS itself reports (name/short_name/type/status/...).
        Shared by _get_rns_stats() (which narrows to this node's own RNode for
        telemetry) and _get_ifstatus() (which needs every interface by name).
        """
        # In standalone mode the agent's RNS instance only sees its own
        # TCPClientInterface, not the RNode or bnZ interfaces in rnsd.
        # Always prefer the direct RPC call to rnsd so we get the full
        # interface list; fall back to the local instance if RPC fails.
        stats = self._get_interface_stats_via_rpc()
        if not stats:
            try:
                stats = self._rns.get_interface_stats()
            except Exception:
                stats = None
        return stats

    def _get_ifstatus(self) -> dict:
        """`get ifstatus` -- online/offline per interface, keyed by the exact
        [[Section Name]] used in the rns config, one "name=online|offline"
        line per interface, so the UI can match it against the parsed config.
        """
        stats = self._raw_interface_stats()
        ifaces = stats.get("interfaces") or [] if stats else []
        lines = [
            f"{i.get('short_name')}={'online' if i.get('status') else 'offline'}"
            for i in ifaces if i.get("short_name")
        ]
        return {"ok": True, "output": "\n".join(lines)}

    def _get_rns_stats(self) -> dict:
        stats = self._raw_interface_stats()

        if not stats:
            return {
                "rns_rxb": None, "rns_txb": None,
                "rns_rxs": None, "rns_txs": None, "interfaces": None,
            }

        ifaces = stats.get("interfaces", [])

        # Top-level rxb/txb may not exist in shared-instance client mode —
        # fall back to summing per-interface counters.
        def _sum(key):
            v = stats.get(key)
            if v is not None:
                return v
            vals = [i.get(key) for i in ifaces if i.get(key) is not None]
            return sum(vals) if vals else None

        result: dict = {
            "rns_rxb": _sum("rxb"),
            "rns_txb": _sum("txb"),
            "rns_rxs": _sum("rxs"),
            "rns_txs": _sum("txs"),
            # Only the node's own radio is reported per-interface -- on a
            # transport node `ifaces` also includes every dynamically
            # discovered backbone/TCP peer link (other people's servers),
            # which isn't this node's telemetry to report.
            "interfaces": [
                {"name": i.get("name"), "rxb": i.get("rxb"), "txb": i.get("txb")}
                for i in ifaces
                if "RNodeInterface" in (i.get("type") or "")
            ],
        }

        for iface in ifaces:
            # Type field may be the short class name or the full dotted path
            itype = iface.get("type") or ""
            if "RNodeInterface" in itype:
                result["rnode_airtime_short"]      = iface.get("airtime_short")
                result["rnode_airtime_long"]        = iface.get("airtime_long")
                result["rnode_channel_load_short"]  = iface.get("channel_load_short")
                result["rnode_channel_load_long"]   = iface.get("channel_load_long")
                result["rnode_bitrate"]             = iface.get("bitrate")
                result["rnode_noise_floor"]         = iface.get("noise_floor")
                result["rnode_interference_dbm"]    = iface.get("interference_last_dbm")
                result["rnode_announce_in"]         = iface.get("incoming_announce_frequency")
                result["rnode_announce_out"]        = iface.get("outgoing_announce_frequency")
                result["rnode_held_announces"]      = iface.get("held_announces")
                break

        return result

    # ------------------------------------------------------------------
    # LXMF transport
    # ------------------------------------------------------------------

    def _send_lxm(self, dest_hash_hex: str, content: bytes = b"",
                  fields: dict | None = None) -> bool:
        """Send a plain-text LXMF message. `content` is the only field relied on
        for rendering — many LXMF clients (e.g. MeshChat) show content but not
        title, so title is left empty rather than used to carry data.
        """
        identity = RNS.Identity.recall(bytes.fromhex(dest_hash_hex))
        if identity is None:
            return False
        dest = RNS.Destination(
            identity, RNS.Destination.OUT, RNS.Destination.SINGLE, "lxmf", "delivery",
        )
        lxm = LXMF.LXMessage(
            dest, self._dest, content,
            fields=fields or {}, desired_method=LXMF.LXMessage.OPPORTUNISTIC,
        )
        self._router.handle_outbound(lxm)
        return True

    def _push_configs(self, dest_hash_hex: str) -> None:
        for cfg_type in ("rns", "agent"):
            try:
                content = self.config_handler.get_config(cfg_type)
                line = f"cfg {cfg_type}\n{content}".encode("utf-8")
                self._send_lxm(dest_hash_hex, content=line)
            except Exception as e:
                RNS.log(f"Config push failed for {cfg_type}: {e}", RNS.LOG_WARNING)

    # ------------------------------------------------------------------
    # NomadNet status page — the real `nomadnet` daemon owns the RNS side
    # (its own destination, announces, Link/Resource handling); this agent
    # just answers a tiny local socket that an executable index.mu page
    # (node/nomadnet_page.py) proxies through, passing along the requester's
    # identity hash and any submitted form fields. Reuses _collect_telemetry/
    # _get_value/_set, so there's exactly one code path for "what the
    # agent's state is" and "how a value changes", whether the request came
    # in over LXMF or via the NomadNet page.
    #
    # micron has a "partial" auto-refresh embed directive, but it's specific
    # to the nomadnet TUI's own renderer -- MeshChat (the client actually in
    # use) doesn't implement it and renders it as garbled literal text. So
    # this stays a plain single page: full content per request, refreshed
    # by reloading, which works the same everywhere.
    # ------------------------------------------------------------------

    # (key, editable, masked, width)
    _NN_RADIO_FIELDS = [("cr", True, False, 8), ("sf", True, False, 8),
                         ("bw", True, False, 12), ("txp", True, False, 8),
                         ("freq", True, False, 12)]
    _NN_RUNTIME_FIELDS = [("shutdown_threshold", True, False, 8),
                           ("tel_update", True, False, 8),
                           ("tel_max_interval", True, False, 8)]
    _NN_SYSTEM_FIELDS = [("hostname", True, False, 32),
                          ("clock", True, False, 10),
                          ("date", True, False, 12)]

    def _nomadnet_socket_loop(self) -> None:
        sock_path = Path(self.nomadnet_socket_path)
        sock_path.parent.mkdir(parents=True, exist_ok=True)
        if sock_path.exists():
            sock_path.unlink()
        srv = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
        srv.bind(str(sock_path))
        srv.listen(8)
        RNS.log(f"NomadNet page socket listening on {sock_path}", RNS.LOG_NOTICE)
        while self._running:
            try:
                conn, _ = srv.accept()
            except OSError:
                break
            threading.Thread(target=self._handle_nomadnet_conn, args=(conn,), daemon=True).start()

    def _handle_nomadnet_conn(self, conn: "socket.socket") -> None:
        try:
            conn.settimeout(10)
            buf = b""
            while not buf.endswith(b"\n"):
                chunk = conn.recv(4096)
                if not chunk:
                    break
                buf += chunk
            request = json.loads(buf.decode("utf-8")) if buf.strip() else {}
            response = self._build_nomadnet_page(request.get("remote_identity"), request.get("fields") or {})
            conn.sendall(response)
        except Exception as e:
            RNS.log(f"NomadNet socket request error: {e}", RNS.LOG_WARNING)
        finally:
            conn.close()

    def _build_nomadnet_page(self, remote_identity_hex: str | None, fields: dict) -> bytes:
        # NomadNet passes only the requester's bare identity hash (env var
        # `remote_identity`), not a destination object -- but Destination.hash()
        # accepts raw identity-hash bytes directly, so the equivalent
        # lxmf.delivery destination hash (what server_dest_hashes stores, the
        # same trust list already used for LXMF commands) can be derived
        # without needing the full identity/public key.
        trusted = bool(remote_identity_hex) and (
            RNS.Destination.hash(bytes.fromhex(remote_identity_hex), "lxmf", "delivery").hex()
            in self.server_dest_hashes
        )

        status_line = ""
        if trusted:
            for field_key, value in fields.items():
                if not field_key.startswith("field_") or not value:
                    continue
                key = field_key[len("field_"):]
                result = self._set([(key, value)])
                outcome = result.get("output") or result.get("error") or ""
                status_line = f"{'OK' if result.get('ok') else 'ERR'}: {outcome}\n-\n"
                break  # each Save link submits exactly one field

        return (status_line + self._render_nomadnet_page(trusted)).encode("utf-8")

    def _render_nomadnet_page(self, trusted: bool) -> str:
        lines = [">RBloxx Node Status", ""]
        if not trusted:
            lines.append("(read-only — identify with a trusted hash to edit values)")
            lines.append("")

        def section(title: str, rows: list[tuple[str, object, bool, bool, int]]) -> None:
            lines.append(f">{title}")
            for key, value, editable, masked, width in rows:
                if trusted and editable:
                    spec = "!" if masked else str(width)
                    # Never prefill a placeholder display string (e.g. "not
                    # set") into the input box -- submitting unedited would
                    # write that literal text as the new value.
                    initial = "" if masked or value in ("not set", "n/a") else value
                    # Field/link tags are only recognized while micron's
                    # parser is in "formatting mode", entered by a *leading
                    # backtick* -- without it, `<...>`/`[...]` are just
                    # literal text. (A bare leading '<' with no backtick is
                    # also separately reserved as a "heading depth reset"
                    # directive, so it has to be kept off column 0 too.)
                    lines.append(f"{key}: `<{spec}|{key}`{initial}>")
                    lines.append(f"`[Save`/page/index.mu`{key}]")
                else:
                    lines.append(f"{key}: {value}")
            lines.append("")

        host_tel, rnode_tel = self._collect_telemetry()
        section("Host vitals", [
            (k, host_tel.get(k, "n/a"), False, False, 0)
            for k in ("cpu_pct", "ram_pct", "disk_pct", "temp_c", "batt_soc_pct", "batt_power_w")
        ])

        if rnode_tel:
            section("Radio stats (live)", [
                (k, rnode_tel.get(k, "n/a"), False, False, 0) for k in sorted(rnode_tel)
            ])

        def get_value_or(key: str) -> str:
            result = self._get_value(key)
            return result["output"].split("=", 1)[1] if result.get("ok") else "error"

        section("Radio config", [
            (key, get_value_or(key), editable, masked, width)
            for key, editable, masked, width in self._NN_RADIO_FIELDS
        ])
        section("Runtime", [
            (key, get_value_or(key), editable, masked, width)
            for key, editable, masked, width in self._NN_RUNTIME_FIELDS
        ])
        section("System", [
            (key, get_value_or(key), editable, masked, width)
            for key, editable, masked, width in self._NN_SYSTEM_FIELDS
        ])
        section("Wi-Fi", [
            ("wifi_network", get_value_or("wifi_network"), True, False, 32),
            ("wifi_psk", "never shown", True, True, 32),
        ])

        return "\n".join(lines)

    # ------------------------------------------------------------------
    # Incoming LXMF handler (commands from server)
    # ------------------------------------------------------------------

    def _handle_lxm(self, message: "LXMF.LXMessage") -> None:
        if not message.signature_validated:
            RNS.log("Rejected unsigned/invalid LXM", RNS.LOG_WARNING)
            return

        server_hash = message.source_hash.hex()
        if server_hash not in self.server_dest_hashes:
            RNS.log(f"Rejected cmd from untrusted hash {server_hash[:12]}", RNS.LOG_WARNING)
            return

        # title is ignored entirely -- many LXMF clients don't render it, so
        # the command line always comes from content. If there's a bulk
        # payload (put_config file text, patch_config patch lines), it's the
        # remainder of content after the first newline.
        raw = message.content_as_string() or ""
        cli_line, _, rest = raw.partition("\n")
        cli_line = cli_line.strip()
        payload = rest.encode("utf-8")
        txn = (message.fields or {}).get(FIELD_TXN, "")

        threading.Thread(
            target=self._execute_and_respond,
            args=(server_hash, txn, cli_line, payload),
            daemon=True,
        ).start()

    def _execute_and_respond(self, server_hash: str, txn: str, cli_line: str, content: bytes) -> None:
        try:
            name, kwargs = parse_cli(cli_line)
            kwargs["_content"] = content
            result = self._dispatch(name, kwargs)
        except Exception as e:
            result = {"ok": False, "error": str(e)}

        ok = result.get("ok", False)
        status = "OK" if ok else "ERR"
        output = result.get("output") or result.get("content") or result.get("error") or ""
        # Some LXMF clients (e.g. MeshChat) render only `content`, not `title` --
        # never send an empty content body, or the reply looks like a blank bubble.
        body = f"{status}: {output}" if output else status
        self._send_lxm(server_hash, content=body.encode("utf-8"), fields={FIELD_TXN: txn})

    def _dispatch(self, cmd: str, data: dict) -> dict:
        match cmd:
            case "get_config":
                return {"ok": True, "content": self.config_handler.get_config(data["type"])}
            case "get_value":
                return self._get_value(data["key"])
            case "get_telemetry":
                return self._send_full_telemetry()
            case "get_ifstatus":
                return self._get_ifstatus()
            case "put_config":
                return self.config_handler.put_config_safe(data["type"], data["_content"].decode("utf-8"))
            case "patch_config":
                patches = decode_patches(data["_content"])
                return self.config_handler.patch_config_safe(data["type"], patches)
            case "svc_restart" | "svc_stop" | "svc_start":
                action = cmd.split("_")[1]
                return self._systemctl(action, data["service"])
            case "wifi_set":
                return self._wifi_set(data["enabled"], data.get("profile"))
            case "log_pull":
                return self._log_pull(data.get("lines", 100), data.get("unit"))
            case "disk_cleanup":
                return self._disk_cleanup()
            case "reboot":
                return self._delayed_reboot(data.get("delay_s", 5))
            case "shutdown":
                return self._delayed_shutdown(data.get("delay_s", 5))
            case "rns_announce":
                self._announce()
                return {"ok": True}
            case "agent_update":
                return self._agent_update()
            case "connectivity_check":
                return self._connectivity_check(data["dest_hash"])
            case "rnode_reset":
                return self._rnode_reset(data["port"])
            case "rnode_update":
                return self._rnode_update(data["port"])
            case "set":
                return self._set(data["pairs"])
            case "trust":
                return self._trust(data["hash"])
            case "untrust":
                return self._untrust(data["hash"])
            case "help":
                return {"ok": True, "output": help_text(data.get("topic"))}
            case _:
                return {"ok": False, "error": f"unknown command: {cmd}"}

    # ------------------------------------------------------------------
    # Command implementations
    # ------------------------------------------------------------------

    def _systemctl(self, action: str, service: str) -> dict:
        try:
            r = subprocess.run(
                ["systemctl", action, service],
                capture_output=True, text=True, timeout=30,
            )
            return {"ok": r.returncode == 0, "output": (r.stdout + r.stderr).strip()}
        except Exception as e:
            return {"ok": False, "error": str(e)}

    def _wifi_set(self, enabled: bool, profile: str | None) -> dict:
        try:
            if enabled:
                subprocess.run(["nmcli", "radio", "wifi", "on"], check=True, timeout=10)
                if profile:
                    subprocess.run(["nmcli", "connection", "up", profile], check=True, timeout=30)
            else:
                subprocess.run(["nmcli", "radio", "wifi", "off"], check=True, timeout=10)
            return {"ok": True}
        except subprocess.CalledProcessError as e:
            return {"ok": False, "error": str(e)}

    def _log_pull(self, lines: int, unit: str | None) -> dict:
        cmd = ["journalctl", f"-n{lines}", "--no-pager"]
        if unit:
            cmd += ["-u", unit]
        try:
            r = subprocess.run(cmd, capture_output=True, text=True, timeout=15)
            return {"ok": True, "content": r.stdout}
        except Exception as e:
            return {"ok": False, "error": str(e)}

    def _disk_cleanup(self) -> dict:
        try:
            r = subprocess.run(
                ["journalctl", "--vacuum-time=7d"],
                capture_output=True, text=True, timeout=30,
            )
            return {"ok": r.returncode == 0, "output": (r.stdout + r.stderr).strip()}
        except Exception as e:
            return {"ok": False, "error": str(e)}

    def _delayed_reboot(self, delay_s: int) -> dict:
        threading.Timer(delay_s, lambda: subprocess.run(["systemctl", "reboot"])).start()
        return {"ok": True}

    def _delayed_shutdown(self, delay_s: int) -> dict:
        threading.Timer(delay_s, lambda: subprocess.run(["systemctl", "poweroff"])).start()
        return {"ok": True}

    def _agent_update(self) -> dict:
        try:
            r = subprocess.run(["git", "pull"], capture_output=True, text=True, timeout=60,
                                cwd=Path(__file__).parent.parent)
            if r.returncode != 0:
                return {"ok": False, "output": r.stderr.strip()}
            threading.Timer(2, lambda: self._systemctl("restart", "rbloxx-agent")).start()
            return {"ok": True, "output": r.stdout.strip()}
        except Exception as e:
            return {"ok": False, "error": str(e)}

    def _connectivity_check(self, dest_hash: str) -> dict:
        """Check if we can send a packet to dest_hash (identity must be known).

        Deliberately stays a raw 1-byte RNS.Packet (not LXMF) — it's a
        lightweight reachability probe, not a command/result exchange.
        """
        identity = RNS.Identity.recall(bytes.fromhex(dest_hash))
        if identity is None:
            return {"ok": False, "error": "identity unknown"}
        target = RNS.Destination(
            identity, RNS.Destination.OUT, RNS.Destination.SINGLE, "lxmf", "delivery",
        )
        pkt = RNS.Packet(target, b"\x00", create_receipt=False)
        sent = pkt.send()
        return {"ok": sent is not False}

    def _rnode_reset(self, port: str) -> dict:
        try:
            r = subprocess.run(["rnodeconf", port, "--reset"], capture_output=True, text=True, timeout=30)
            return {"ok": r.returncode == 0, "output": (r.stdout + r.stderr).strip()}
        except Exception as e:
            return {"ok": False, "error": str(e)}

    def _rnode_update(self, port: str) -> dict:
        try:
            r = subprocess.run(
                ["rnodeconf", port, "--update"],
                capture_output=True, text=True, timeout=300,
            )
            ok = r.returncode == 0
            if not ok:
                self.system_handler.set_persistent_error("rnode_update_failed")
            return {"ok": ok, "output": (r.stdout + r.stderr).strip()}
        except Exception as e:
            return {"ok": False, "error": str(e)}

    def _set(self, pairs: list[tuple[str, str]]) -> dict:
        """`set KEY=VALUE [KEY=VALUE ...]` — runtime keys apply in-memory,
        radio-alias keys are resolved to the rns config's RNodeInterface
        section and patched atomically via the existing rollback-safe path,
        system keys (hostname/clock/date) apply directly to the OS.
        """
        runtime_updates: list[tuple[str, str]] = []
        radio_patches: list[dict] = []
        system_updates: list[tuple[str, str]] = []
        wifi_cred_updates: list[tuple[str, str]] = []
        unknown: list[str] = []
        section: str | None = None

        for key, value in pairs:
            key_lower = key.lower()
            if key_lower in RUNTIME_KEYS:
                runtime_updates.append((key_lower, value))
            elif key_lower in RADIO_ALIASES:
                if section is None:
                    section = self.config_handler.find_section_by_type("rns", "RNodeInterface")
                    if section is None:
                        return {"ok": False, "error": "no RNodeInterface section found in rns config"}
                ini_key = RADIO_ALIASES[key_lower]
                ini_value = value
                if key_lower == "freq":
                    try:
                        ini_value = str(int(float(value) * 1_000_000))
                    except ValueError:
                        return {"ok": False, "error": f"invalid FREQ value: {value}"}
                radio_patches.append({"section": section, "key": ini_key, "value": ini_value})
            elif key_lower in SYSTEM_KEYS:
                system_updates.append((key_lower, value))
            elif key_lower in WIFI_CRED_KEYS:
                wifi_cred_updates.append((key_lower, value))
            else:
                unknown.append(key)

        if unknown:
            return {"ok": False, "error": f"unknown key(s): {', '.join(unknown)}"}

        # Validate all system keys before applying anything (atomic — no
        # partial application — same rule as the unknown-key check above).
        for key, value in system_updates:
            error = self._validate_system_setting(key, value)
            if error:
                return {"ok": False, "error": error}

        outputs = []
        for key, value in runtime_updates:
            if key == "shutdown_threshold":
                try:
                    self.shutdown_soc_pct = float(value)
                except ValueError:
                    return {"ok": False, "error": f"invalid shutdown_threshold value: {value}"}
                outputs.append(f"shutdown_threshold={value}")
            elif key == "tel_update":
                try:
                    interval = float(value)
                except ValueError:
                    return {"ok": False, "error": f"invalid tel_update value: {value}"}
                if interval < 0:
                    return {"ok": False, "error": f"invalid tel_update value: {value}"}
                self.telemetry_min_interval = interval
                outputs.append(f"tel_update={value}")
            elif key == "tel_max_interval":
                try:
                    interval = float(value)
                except ValueError:
                    return {"ok": False, "error": f"invalid tel_max_interval value: {value}"}
                if interval < 0:
                    return {"ok": False, "error": f"invalid tel_max_interval value: {value}"}
                self.telemetry_max_interval = interval
                outputs.append(f"tel_max_interval={value}")

        if radio_patches:
            result = self.config_handler.patch_config_safe("rns", radio_patches)
            if not result.get("ok"):
                return result
            radio_desc = ", ".join(f"{p['key']}={p['value']}" for p in radio_patches)
            outputs.append(f"radio: {radio_desc} (pending_commit)")

        for key, value in system_updates:
            result = self._apply_system_setting(key, value)
            if not result.get("ok"):
                return result
            outputs.append(result["output"])

        for key, value in wifi_cred_updates:
            result = self._set_wifi_cred(key, value)
            if not result.get("ok"):
                return result
            outputs.append(result["output"])

        return {"ok": True, "output": "; ".join(outputs) if outputs else "no changes"}

    def _set_wifi_cred(self, key: str, value: str) -> dict:
        """wifi_network/wifi_psk can arrive in separate `set` commands --
        remembered here until both are known, then nmcli connects. Output
        never echoes wifi_psk's value back.
        """
        if key == "wifi_network":
            self._wifi_network = value
        else:
            self._wifi_psk = value

        if self._wifi_network is None or self._wifi_psk is None:
            pending = "wifi_psk" if self._wifi_network is not None else "wifi_network"
            return {"ok": True, "output": f"{key} set (awaiting {pending})"}

        try:
            r = subprocess.run(
                ["nmcli", "device", "wifi", "connect", self._wifi_network, "password", self._wifi_psk],
                capture_output=True, text=True, timeout=30,
            )
            ok = r.returncode == 0
            output = (r.stdout + r.stderr).strip()
            if ok:
                # Credentials consumed -- clear so a future single-key update
                # doesn't silently reconnect with a stale stored value.
                self._wifi_network = None
                self._wifi_psk = None
            return {"ok": ok, "output": output or ("connected" if ok else "connect failed")}
        except Exception as e:
            return {"ok": False, "error": str(e)}

    def _validate_system_setting(self, key: str, value: str) -> str | None:
        """Return an error message if `value` is malformed for `key`, else None."""
        if key == "hostname" and not re.match(r"^[A-Za-z0-9]([A-Za-z0-9-]{0,61}[A-Za-z0-9])?$", value):
            return f"invalid hostname: {value}"
        if key == "clock" and not re.match(r"^([01]?\d|2[0-3]):[0-5]\d(:[0-5]\d)?$", value):
            return f"invalid clock value (expected HH:MM[:SS], 24h): {value}"
        if key == "date" and not re.match(r"^\d{4}-(0[1-9]|1[0-2])-(0[1-9]|[12]\d|3[01])$", value):
            return f"invalid date value (expected YYYY-MM-DD): {value}"
        return None

    def _apply_system_setting(self, key: str, value: str) -> dict:
        try:
            if key == "hostname":
                try:
                    subprocess.run(["hostname", value], check=True, timeout=10)
                    Path("/etc/hostname").write_text(value + "\n", encoding="utf-8")
                except Exception as e:
                    return {"ok": False, "error": f"hostname change failed: {e}"}

                # Reticulum has its own node-name fields (RNode beacon identity)
                # independent of the OS hostname -- keep them in sync so renaming
                # the node renames it everywhere, not just at the OS level.
                radio_note = ""
                section = self.config_handler.find_section_by_type("rns", "RNodeInterface")
                if section is not None:
                    patches = [
                        {"section": section, "key": "id_callsign", "value": value},
                        {"section": section, "key": "discovery_name", "value": value},
                    ]
                    result = self.config_handler.patch_config_safe("rns", patches)
                    if not result.get("ok"):
                        return result
                    radio_note = "; id_callsign/discovery_name updated (pending_commit)"

                # LXMF's announced display_name was fixed to the old hostname at
                # startup -- restart so the next announce picks up the new one.
                self._systemctl("restart", "rbloxx-agent")
                return {"ok": True, "output": f"hostname={value} (agent restarting){radio_note}"}

            # clock/date both set the full wall-clock time via `date -s`,
            # combining the requested field with the other (currently-unset)
            # field's existing value -- avoids depending on a running system
            # dbus, which timedatectl needs but isn't always present on
            # minimal/embedded images (confirmed missing on the test box).
            now = datetime.now()
            if key == "clock":
                dt_str = f"{now.strftime('%Y-%m-%d')} {value}"
            else:  # date
                dt_str = f"{value} {now.strftime('%H:%M:%S')}"
            r = subprocess.run(["date", "-s", dt_str], capture_output=True, text=True, timeout=10)
            if r.returncode != 0:
                return {"ok": False, "error": (r.stdout + r.stderr).strip() or "date -s failed"}
            return {"ok": True, "output": f"{key}={value}"}
        except Exception as e:
            return {"ok": False, "error": str(e)}

    def _get_value(self, key: str) -> dict:
        """`get <key>` — read-only counterpart to `set`, same key namespace
        (runtime/radio-alias/system), one value at a time.
        """
        key_lower = key.lower()

        if key_lower == "shutdown_threshold":
            return {"ok": True, "output": f"shutdown_threshold={self.shutdown_soc_pct}"}
        if key_lower == "tel_update":
            return {"ok": True, "output": f"tel_update={self.telemetry_min_interval}"}
        if key_lower == "tel_max_interval":
            return {"ok": True, "output": f"tel_max_interval={self.telemetry_max_interval}"}

        if key_lower in RADIO_ALIASES:
            section = self.config_handler.find_section_by_type("rns", "RNodeInterface")
            if section is None:
                return {"ok": False, "error": "no RNodeInterface section found in rns config"}
            ini_key = RADIO_ALIASES[key_lower]
            value = self.config_handler.get_ini_value("rns", section, ini_key)
            if value is None:
                return {"ok": False, "error": f"{ini_key} not set in {section}"}
            if key_lower == "freq":
                value = str(float(value) / 1_000_000)
            return {"ok": True, "output": f"{key_lower}={value}"}

        if key_lower == "hostname":
            return {"ok": True, "output": f"hostname={socket.gethostname()}"}
        if key_lower == "clock":
            return {"ok": True, "output": f"clock={datetime.now().strftime('%H:%M:%S')}"}
        if key_lower == "date":
            return {"ok": True, "output": f"date={datetime.now().strftime('%Y-%m-%d')}"}

        if key_lower == "wifi_network":
            value = self._wifi_network or "not set"
            return {"ok": True, "output": f"wifi_network={value}"}
        if key_lower == "wifi_psk":
            return {"ok": False, "error": "wifi_psk is never read back"}

        return {"ok": False, "error": f"unknown key: {key}"}

    def _trust(self, hash_hex: str) -> dict:
        hash_hex = hash_hex.lower()
        try:
            bytes.fromhex(hash_hex)
        except ValueError:
            return {"ok": False, "error": f"not valid hex: {hash_hex}"}
        if hash_hex in self.server_dest_hashes:
            return {"ok": True, "output": f"{hash_hex} already trusted"}
        result = self._persist_trust_list(self.server_dest_hashes + [hash_hex])
        if result.get("ok"):
            self.server_dest_hashes.append(hash_hex)
            result["output"] = f"trusted {hash_hex}"
        return result

    def _untrust(self, hash_hex: str) -> dict:
        hash_hex = hash_hex.lower()
        if hash_hex not in self.server_dest_hashes:
            return {"ok": False, "error": f"not currently trusted: {hash_hex}"}
        if len(self.server_dest_hashes) <= 1:
            return {"ok": False, "error": "refused: would remove last trusted server"}
        new_hashes = [h for h in self.server_dest_hashes if h != hash_hex]
        result = self._persist_trust_list(new_hashes)
        if result.get("ok"):
            self.server_dest_hashes = new_hashes
            result["output"] = f"untrusted {hash_hex}"
        return result

    def _persist_trust_list(self, new_hashes: list[str]) -> dict:
        try:
            current = json.loads(self.config_handler.get_config("agent"))
        except Exception as e:
            return {"ok": False, "error": f"could not read agent config: {e}"}
        current["server_dest_hashes"] = new_hashes
        return self.config_handler.put_config_safe("agent", json.dumps(current, indent=2))

    # ------------------------------------------------------------------
    # Config rollback failsafe
    # ------------------------------------------------------------------

    def _check_pending_rollback(self) -> None:
        self.config_handler.rollback_if_pending()

    # ------------------------------------------------------------------
    # Auto-shutdown on low battery
    # ------------------------------------------------------------------

    def _check_auto_shutdown(self) -> None:
        if self.shutdown_soc_pct <= 0:
            return
        power = self.power_handler.collect()
        soc = power.get("batt_soc_pct")
        if soc is not None and soc <= self.shutdown_soc_pct:
            RNS.log(f"Battery at {soc:.1f}% — initiating shutdown", RNS.LOG_CRITICAL)
            self._delayed_shutdown(10)

    # ------------------------------------------------------------------
    # Hardware watchdog feeder
    # ------------------------------------------------------------------

    def _watchdog_loop(self) -> None:
        wd_path = Path("/dev/watchdog")
        if not wd_path.exists():
            return
        interval = self.cfg.get("watchdog_feed_interval_s", 10)
        try:
            with open(wd_path, "wb", buffering=0) as wd:
                while self._running:
                    wd.write(b"1")
                    time.sleep(interval)
        except Exception as e:
            RNS.log(f"Watchdog feeder stopped: {e}", RNS.LOG_ERROR)

    # ------------------------------------------------------------------
    # RNode health monitor
    # ------------------------------------------------------------------

    def _rnode_monitor_loop(self) -> None:
        ports = self.cfg.get("rnode_ports", [])
        if not ports:
            return
        zero_threshold = self.cfg.get("zero_traffic_minutes", 15) * 60
        last_stats: dict[str, tuple[int, float]] = {}  # port -> (rxb+txb, timestamp)

        while self._running:
            time.sleep(60)
            try:
                rns_stats = self._get_rns_stats()
                ifaces = {i["name"]: i for i in (rns_stats.get("interfaces") or [])}

                for port in ports:
                    iface = ifaces.get(port)
                    if iface is None:
                        continue
                    traffic = (iface.get("rxb") or 0) + (iface.get("txb") or 0)
                    now = time.time()
                    prev_traffic, prev_time = last_stats.get(port, (traffic, now))

                    if traffic == prev_traffic and (now - prev_time) > zero_threshold:
                        RNS.log(f"RNode {port} appears stuck — attempting USB reset", RNS.LOG_WARNING)
                        self._usb_reset(port)
                        last_stats[port] = (traffic, now)
                    elif traffic != prev_traffic:
                        last_stats[port] = (traffic, now)
            except Exception as e:
                RNS.log(f"RNode monitor error: {e}", RNS.LOG_WARNING)

    def _usb_reset(self, port: str) -> None:
        try:
            subprocess.run(["usbreset", port], timeout=10)
            self.system_handler.add_transient_error("rnode_usb_reset")
            time.sleep(5)
            if not self._rnode_recovers(port):
                RNS.log(f"USB reset failed for {port} — restarting rnsd", RNS.LOG_WARNING)
                self._systemctl("restart", "rnsd")
                self.system_handler.add_transient_error("rnode_restart")
        except Exception as e:
            RNS.log(f"USB reset error for {port}: {e}", RNS.LOG_WARNING)

    def _rnode_recovers(self, port: str, wait_s: int = 10) -> bool:
        """Returns True if the interface shows traffic within wait_s seconds."""
        time.sleep(wait_s)
        stats = self._get_rns_stats()
        ifaces = {i["name"]: i for i in (stats.get("interfaces") or [])}
        return port in ifaces


if __name__ == "__main__":
    cfg_path = sys.argv[1] if len(sys.argv) > 1 else "/etc/rbloxx/agent.json"
    RBloxxAgent(cfg_path).start()
