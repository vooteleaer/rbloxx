"""Bloxx node agent — runs alongside rnsd on each remote node."""

import os
import sys
import socket
import subprocess
import threading
import time
from pathlib import Path

import json

try:
    import msgpack
except ImportError:
    from RNS.vendor import umsgpack as msgpack
import RNS

sys.path.insert(0, str(Path(__file__).parent.parent / "shared"))
from protocol import (
    APP_NAME, NODE_ASPECT, SERVER_ASPECT, VERSION,
    PATH_CMD, PATH_TELEMETRY, PATH_TIME,
    CMD_GET_CONFIG, CMD_PUT_CONFIG, CMD_PATCH_CONFIG,
    CMD_SVC_RESTART, CMD_SVC_STOP, CMD_SVC_START,
    CMD_WIFI_SET, CMD_LOG_PULL, CMD_REBOOT, CMD_SHUTDOWN,
    CMD_RNODE_RESET, CMD_RNODE_UPDATE, CMD_RNS_ANNOUNCE,
    CMD_DISK_CLEANUP, CMD_CONNECTIVITY_CHECK, CMD_AGENT_UPDATE,
    CMD_SHUTDOWN_THRESHOLD,
)
from config_handler import ConfigHandler
from system_handler import SystemHandler
from power_handler import PowerHandler


class BloxxAgent:
    def __init__(self, config_path: str = "/etc/bloxx/agent.json"):
        self.cfg = self._load_config(config_path)
        self.identity_path = Path(self.cfg.get("identity_path", "/etc/bloxx/identity"))
        self.announce_interval: int = self.cfg.get("announce_interval", 300)
        self.time_sync_interval: int = self.cfg.get("time_sync_interval", 43200)  # 12h default
        self.server_dest_hashes: list[str] = self.cfg.get("server_dest_hashes", [])
        self.shutdown_soc_pct: float = self.cfg.get("shutdown_soc_pct", 0)
        self._last_time_sync: float = 0

        # Trusted server identity hashes; auto-populated when we successfully push telemetry
        self._trusted: set[str] = set(self.cfg.get("trusted_server_identities", []))
        self._trusted_lock = threading.Lock()

        self.config_handler = ConfigHandler(self.cfg, config_path=config_path)
        self.system_handler = SystemHandler(self.cfg)
        self.power_handler = PowerHandler(self.cfg)

        self._rns: RNS.Reticulum | None = None
        self._dest: RNS.Destination | None = None
        self._running = False

    # ------------------------------------------------------------------
    # Startup
    # ------------------------------------------------------------------

    def start(self) -> None:
        identity = self._load_or_create_identity()
        self._rns = RNS.Reticulum(require_shared_instance=True)

        self._dest = RNS.Destination(
            identity,
            RNS.Destination.IN,
            RNS.Destination.SINGLE,
            APP_NAME,
            NODE_ASPECT,
        )
        self._dest.register_request_handler(
            PATH_CMD,
            response_generator=self._handle_cmd,
            allow=RNS.Destination.ALLOW_ALL,
        )

        self._running = True
        threading.Thread(target=self._watchdog_loop, daemon=True, name="watchdog").start()
        threading.Thread(target=self._rnode_monitor_loop, daemon=True, name="rnode-monitor").start()
        threading.Thread(target=self._main_loop, daemon=True, name="main-loop").start()

        RNS.log(f"Bloxx agent started — dest {RNS.prettyhexrep(self._dest.hash)}", RNS.LOG_NOTICE)

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

    # ------------------------------------------------------------------
    # Main loop — announce + telemetry push
    # ------------------------------------------------------------------

    def _main_loop(self) -> None:
        self._check_pending_rollback()
        self._wait_for_server_path()
        self._time_sync()
        while self._running:
            self._announce()
            self._push_telemetry_all()
            if time.time() - self._last_time_sync >= self.time_sync_interval:
                self._wait_for_server_path()
                self._time_sync()
            self._check_auto_shutdown()
            self._sleep_interruptible(self.announce_interval)

    def _wait_for_server_path(self) -> None:
        """Block until a path to at least one server is known."""
        if not self.server_dest_hashes:
            return
        while self._running:
            for dest_hash_hex in self.server_dest_hashes:
                dest_hash = bytes.fromhex(dest_hash_hex)
                # In shared-instance mode, Transport.known_paths is empty in the
                # client process. Use Identity.recall() (from rnsd's persistent
                # storage) instead of has_path() to detect when the server is known.
                if RNS.Identity.recall(dest_hash) is not None:
                    return
                RNS.Transport.request_path(dest_hash)
            for _ in range(30):
                if not self._running:
                    return
                for dest_hash_hex in self.server_dest_hashes:
                    if RNS.Identity.recall(bytes.fromhex(dest_hash_hex)) is not None:
                        return
                time.sleep(1)

    def _sleep_interruptible(self, seconds: int) -> None:
        for _ in range(seconds):
            if not self._running:
                break
            time.sleep(1)

    def _announce(self) -> None:
        app_data = msgpack.packb(
            {"hostname": socket.gethostname(), "version": VERSION},
            use_bin_type=True,
        )
        self._dest.announce(app_data=app_data)

    def _push_telemetry_all(self) -> None:
        telemetry = self._collect_telemetry()
        for dest_hash_hex in self.server_dest_hashes:
            self._push_to_server(dest_hash_hex, PATH_TELEMETRY, telemetry)

    def _collect_telemetry(self) -> dict:
        sys_info = self.system_handler.collect()
        power_info = self.power_handler.collect()
        rns_stats = self._get_rns_stats()
        errors = self.system_handler.get_errors() + self.power_handler.get_errors()
        return {
            "hostname": socket.gethostname(),
            "version": VERSION,
            "timestamp": int(time.time()),
            **sys_info,
            **power_info,
            **rns_stats,
            "topology": self._get_topology(),
            "errors": errors,
        }

    def _get_rns_stats(self) -> dict:
        try:
            stats = self._rns.get_interface_stats()
            result: dict = {
                "rns_rxb": stats.get("rxb"),
                "rns_txb": stats.get("txb"),
                "rns_rxs": stats.get("rxs"),
                "rns_txs": stats.get("txs"),
                "interfaces": [
                    {"name": i.get("name"), "rxb": i.get("rxb"), "txb": i.get("txb")}
                    for i in stats.get("interfaces", [])
                ],
            }
            for iface in stats.get("interfaces", []):
                if iface.get("type") == "RNodeInterface":
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
        except Exception:
            return {
                "rns_rxb": None, "rns_txb": None,
                "rns_rxs": None, "rns_txs": None, "interfaces": None,
            }

    def _get_topology(self) -> dict:
        """Collect path table, link rates, and per-neighbor signal quality."""
        try:
            paths_raw = self._rns.get_path_table()
            rates_raw = self._rns.get_rate_table()
            iface_stats = self._rns.get_interface_stats()
        except Exception:
            return {"paths": []}

        def _h(b) -> str:
            return b.hex() if isinstance(b, bytes) else str(b)

        rate_by_hash = {_h(r["hash"]): r.get("rate") for r in (rates_raw or [])}

        # last RSSI/SNR per interface name (best approximation for neighbor signal quality)
        rssi_by_iface = {
            i["name"]: {"rssi": i.get("last_rx_rssi"), "snr": i.get("last_rx_snr")}
            for i in iface_stats.get("interfaces", [])
            if i.get("name")
        }

        paths = []
        for p in (paths_raw or []):
            dest = _h(p["hash"])
            hops = p.get("hops", 0)
            iface = p.get("interface", "")
            entry: dict = {
                "dest_hash": dest,
                "hops": hops,
                "interface": iface,
                "bitrate": rate_by_hash.get(dest),
            }
            if hops == 1:
                sig = rssi_by_iface.get(iface, {})
                entry["rssi"] = sig.get("rssi")
                entry["snr"] = sig.get("snr")
            paths.append(entry)

        return {"paths": paths}

    # ------------------------------------------------------------------
    # RNS link helpers
    # ------------------------------------------------------------------

    def _open_link_to_server(self, dest_hash_hex: str, timeout: float = 60.0) -> RNS.Link | None:
        dest_hash = bytes.fromhex(dest_hash_hex)
        # In shared-instance mode, Transport.known_paths is empty in the client process.
        # Use Identity.recall() (persisted by rnsd) as the readiness check instead.
        identity = RNS.Identity.recall(dest_hash)
        if identity is None:
            RNS.Transport.request_path(dest_hash)
            deadline = time.time() + timeout / 2
            while identity is None and time.time() < deadline:
                time.sleep(2)
                identity = RNS.Identity.recall(dest_hash)
        if identity is None:
            RNS.log(f"Cannot recall identity for {dest_hash_hex}", RNS.LOG_WARNING)
            return None
        try:
            server_dest = RNS.Destination(
                identity, RNS.Destination.OUT, RNS.Destination.SINGLE,
                APP_NAME, SERVER_ASPECT,
            )
            link = RNS.Link(server_dest)
            deadline = time.time() + timeout / 2
            while link.status != RNS.Link.ACTIVE and time.time() < deadline:
                time.sleep(0.1)
            if link.status != RNS.Link.ACTIVE:
                link.teardown()
                return None
            # Identify ourselves so the server can attribute telemetry/requests
            link.identify(self._dest.identity)
            time.sleep(0.2)
            # Cache the server's identity hash for inbound auth
            remote_id = link.get_remote_identity()
            if remote_id:
                with self._trusted_lock:
                    self._trusted.add(remote_id.hash.hex())
            return link
        except Exception as e:
            RNS.log(f"Link error to {dest_hash_hex}: {e}", RNS.LOG_WARNING)
            return None

    def _push_to_server(self, dest_hash_hex: str, path: str, data: dict) -> bool:
        link = self._open_link_to_server(dest_hash_hex)
        if link is None:
            return False
        try:
            done = threading.Event()

            def _resp(receipt):
                done.set()

            def _fail(receipt):
                done.set()

            link.request(
                path,
                data=msgpack.packb(data, use_bin_type=True),
                response_callback=_resp,
                failed_callback=_fail,
                timeout=30,
            )
            done.wait(timeout=35)
            return True
        except Exception as e:
            RNS.log(f"Request error to {dest_hash_hex}{path}: {e}", RNS.LOG_WARNING)
            return False
        finally:
            link.teardown()

    # ------------------------------------------------------------------
    # Incoming command handler
    # ------------------------------------------------------------------

    def _handle_cmd(self, path, data, request_id, remote_identity, requested_at):
        if remote_identity is None:
            return msgpack.packb({"ok": False, "error": "no identity"}, use_bin_type=True)

        with self._trusted_lock:
            trusted = remote_identity.hash.hex() in self._trusted

        if not trusted:
            RNS.log(
                f"Rejected command from untrusted identity {remote_identity.hash.hex()}",
                RNS.LOG_WARNING,
            )
            return msgpack.packb({"ok": False, "error": "not authorized"}, use_bin_type=True)

        try:
            payload = msgpack.unpackb(data, raw=False)
            result = self._dispatch(payload.get("cmd", ""), payload)
        except Exception as e:
            result = {"ok": False, "error": str(e)}

        return msgpack.packb(result, use_bin_type=True)

    def _dispatch(self, cmd: str, data: dict) -> dict:
        match cmd:
            case "get_config":
                return {"ok": True, "content": self.config_handler.get_config(data["type"])}
            case "put_config":
                return self.config_handler.put_config_safe(data["type"], data["content"])
            case "patch_config":
                return self.config_handler.patch_config_safe(data["type"], data["patches"])
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
            case "shutdown_threshold":
                self.shutdown_soc_pct = float(data["soc_pct"])
                return {"ok": True}
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
            threading.Timer(2, lambda: self._systemctl("restart", "bloxx-agent")).start()
            return {"ok": True, "output": r.stdout.strip()}
        except Exception as e:
            return {"ok": False, "error": str(e)}

    def _connectivity_check(self, dest_hash: str) -> dict:
        t0 = time.time()
        link = self._open_link_to_server(dest_hash, timeout=30)
        if link is None:
            return {"ok": False, "rtt_ms": None}
        rtt_ms = (time.time() - t0) * 1000
        link.teardown()
        return {"ok": True, "rtt_ms": round(rtt_ms, 1)}

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

    # ------------------------------------------------------------------
    # Time sync
    # ------------------------------------------------------------------

    def _time_sync(self) -> None:
        self._last_time_sync = time.time()
        for dest_hash_hex in self.server_dest_hashes:
            try:
                t1 = time.time_ns()
                link = self._open_link_to_server(dest_hash_hex, timeout=60)
                if link is None:
                    continue

                result: dict = {}
                done = threading.Event()

                def _resp(receipt):
                    nonlocal result
                    if receipt.response:
                        result = msgpack.unpackb(receipt.response, raw=False)
                    done.set()

                link.request(
                    PATH_TIME,
                    data=msgpack.packb({"t1": t1}, use_bin_type=True),
                    response_callback=_resp,
                    failed_callback=lambda r: done.set(),
                    timeout=30,
                )
                done.wait(timeout=35)
                link.teardown()

                if "t2" not in result or "t3" not in result:
                    continue

                t4 = time.time_ns()
                t2, t3 = result["t2"], result["t3"]
                offset_ns = ((t2 - t1) + (t3 - t4)) // 2
                rtt_ms = ((t4 - t1) - (t3 - t2)) / 1_000_000
                self.system_handler.rns_rtt_ms = rtt_ms

                if abs(offset_ns) > 500_000_000:  # >0.5s — worth correcting
                    offset_s = offset_ns / 1_000_000_000
                    new_time_s = time.time() + offset_s
                    subprocess.run(
                        ["date", "-s", f"@{new_time_s:.3f}"],
                        capture_output=True, timeout=5,
                    )
                    RNS.log(f"Time corrected by {offset_s:.3f}s, RTT {rtt_ms:.1f}ms", RNS.LOG_NOTICE)
                break
            except Exception as e:
                RNS.log(f"Time sync failed to {dest_hash_hex}: {e}", RNS.LOG_WARNING)

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
    cfg_path = sys.argv[1] if len(sys.argv) > 1 else "/etc/bloxx/agent.json"
    BloxxAgent(cfg_path).start()
