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
    PKT_TELEMETRY, PKT_RTELEMETRY, PKT_CONFIG, PKT_CMD, PKT_RESULT,
    CHUNK_SIZE,
)
from config_handler import ConfigHandler
from system_handler import SystemHandler
from power_handler import PowerHandler


class BloxxAgent:
    def __init__(self, config_path: str = "/etc/bloxx/agent.json"):
        self.cfg = self._load_config(config_path)
        self.identity_path = Path(self.cfg.get("identity_path", "/etc/bloxx/identity"))
        self.announce_interval: int = self.cfg.get("announce_interval", 300)
        self.server_dest_hashes: list[str] = self.cfg.get("server_dest_hashes", [])
        self.shutdown_soc_pct: float = self.cfg.get("shutdown_soc_pct", 0)

        # Reassembly buffer for chunked incoming commands keyed by command id
        self._cmd_chunks: dict[str, dict] = {}
        self._cmd_chunks_lock = threading.Lock()

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
        # Receive plain packets from the server (commands)
        self._dest.set_packet_callback(self._handle_incoming_packet)

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
        self._wait_for_server_identity()
        first = True
        while self._running:
            self._announce()
            self._push_telemetry_all(include_configs=first)
            first = False
            self._check_auto_shutdown()
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
        app_data = msgpack.packb(
            {"hostname": socket.gethostname(), "version": VERSION},
            use_bin_type=True,
        )
        self._dest.announce(app_data=app_data)

    def _push_telemetry_all(self, include_configs: bool = False) -> None:
        sys_tel, rnode_tel = self._collect_telemetry()
        for dest_hash_hex in self.server_dest_hashes:
            self._send_packet(dest_hash_hex, {
                "t": PKT_TELEMETRY, "h": self._dest.hash.hex(), "d": sys_tel,
            })
            if rnode_tel:
                self._send_packet(dest_hash_hex, {
                    "t": PKT_RTELEMETRY, "h": self._dest.hash.hex(), "d": rnode_tel,
                })
            if include_configs:
                self._push_configs(dest_hash_hex)

    def _collect_telemetry(self) -> tuple[dict, dict | None]:
        """Return (system_telemetry, rnode_telemetry). rnode_telemetry is None if no RNode data."""
        sys_info = self.system_handler.collect()
        power_info = self.power_handler.collect()
        rns_stats = self._get_rns_stats()
        errors = self.system_handler.get_errors() + self.power_handler.get_errors()

        rnode_keys = {
            "rnode_airtime_short", "rnode_airtime_long",
            "rnode_channel_load_short", "rnode_channel_load_long",
            "rnode_noise_floor", "rnode_interference_dbm",
            "rnode_bitrate", "rnode_announce_in", "rnode_announce_out",
            "rnode_held_announces",
        }
        rnode_tel = {k: v for k, v in rns_stats.items() if k in rnode_keys and v is not None}

        sys_tel = {
            "hostname": socket.gethostname(),
            "version": VERSION,
            "timestamp": int(time.time()),
            **sys_info,
            **power_info,
            "rns_rxb": rns_stats.get("rns_rxb"),
            "rns_txb": rns_stats.get("rns_txb"),
            "rns_rxs": rns_stats.get("rns_rxs"),
            "rns_txs": rns_stats.get("rns_txs"),
            "topology": self._get_topology(),
            "errors": errors,
        }

        return sys_tel, rnode_tel if rnode_tel else None

    def _get_rns_stats(self) -> dict:
        try:
            stats = self._rns.get_interface_stats()
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
                "interfaces": [
                    {"name": i.get("name"), "rxb": i.get("rxb"), "txb": i.get("txb")}
                    for i in ifaces
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
    # Plain-packet transport
    # ------------------------------------------------------------------

    def _server_dest(self, dest_hash_hex: str) -> RNS.Destination | None:
        identity = RNS.Identity.recall(bytes.fromhex(dest_hash_hex))
        if identity is None:
            return None
        return RNS.Destination(
            identity, RNS.Destination.OUT, RNS.Destination.SINGLE, APP_NAME, SERVER_ASPECT,
        )

    def _send_packet(self, dest_hash_hex: str, data: dict) -> bool:
        server_dest = self._server_dest(dest_hash_hex)
        if server_dest is None:
            return False
        try:
            payload = msgpack.packb(data, use_bin_type=True)
            receipt = RNS.Packet(server_dest, payload, create_receipt=False).send()
            return receipt is not False
        except Exception as e:
            RNS.log(f"Packet send error to {dest_hash_hex}: {e}", RNS.LOG_DEBUG)
            return False

    def _push_configs(self, dest_hash_hex: str) -> None:
        for cfg_type in ("rns", "agent"):
            try:
                content = self.config_handler.get_config(cfg_type)
                encoded = content.encode("utf-8")
                chunks = [encoded[i:i + CHUNK_SIZE] for i in range(0, len(encoded), CHUNK_SIZE)]
                for i, chunk in enumerate(chunks):
                    self._send_packet(dest_hash_hex, {
                        "t": PKT_CONFIG,
                        "h": self._dest.hash.hex(),
                        "ct": cfg_type,
                        "i": i,
                        "n": len(chunks),
                        "c": chunk.decode("utf-8"),
                    })
            except Exception as e:
                RNS.log(f"Config push failed for {cfg_type}: {e}", RNS.LOG_WARNING)

    # ------------------------------------------------------------------
    # Incoming packet handler (commands from server)
    # ------------------------------------------------------------------

    def _handle_incoming_packet(self, data: bytes, packet) -> None:
        try:
            msg = msgpack.unpackb(data, raw=False)
        except Exception:
            return

        if msg.get("t") != PKT_CMD:
            return

        server_hash = msg.get("sh", "")
        if server_hash not in self.server_dest_hashes:
            RNS.log(f"Rejected cmd from untrusted hash {server_hash[:12]}", RNS.LOG_WARNING)
            return

        cmd_id = msg.get("id", "")
        cmd = msg.get("cmd", "")

        # Handle chunked put_config reassembly
        if msg.get("i") is not None:
            self._accumulate_cmd_chunk(server_hash, cmd_id, msg)
            return

        threading.Thread(
            target=self._execute_and_respond,
            args=(server_hash, cmd_id, msg),
            daemon=True,
        ).start()

    def _accumulate_cmd_chunk(self, server_hash: str, cmd_id: str, msg: dict) -> None:
        with self._cmd_chunks_lock:
            buf = self._cmd_chunks.setdefault(cmd_id, {"chunks": {}, "total": msg["n"], "meta": msg})
            buf["chunks"][msg["i"]] = msg.get("c", "")
            if len(buf["chunks"]) == buf["total"]:
                del self._cmd_chunks[cmd_id]
                full = buf["meta"].copy()
                full["content"] = "".join(buf["chunks"][i] for i in range(buf["total"]))
                full.pop("i", None); full.pop("n", None); full.pop("c", None)
                threading.Thread(
                    target=self._execute_and_respond,
                    args=(server_hash, cmd_id, full),
                    daemon=True,
                ).start()

    def _execute_and_respond(self, server_hash: str, cmd_id: str, msg: dict) -> None:
        try:
            result = self._dispatch(msg.get("cmd", ""), msg)
        except Exception as e:
            result = {"ok": False, "error": str(e)}

        output = result.get("output") or result.get("content") or result.get("error") or ""
        encoded = output.encode("utf-8")
        chunks = [encoded[i:i + CHUNK_SIZE] for i in range(0, len(encoded), CHUNK_SIZE)] or [b""]
        for i, chunk in enumerate(chunks):
            self._send_packet(server_hash, {
                "t": PKT_RESULT,
                "h": self._dest.hash.hex(),
                "id": cmd_id,
                "ok": result.get("ok", False),
                "i": i, "n": len(chunks),
                "c": chunk.decode("utf-8"),
            })

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
        """Check if we can send a packet to dest_hash (identity must be known)."""
        identity = RNS.Identity.recall(bytes.fromhex(dest_hash))
        if identity is None:
            return {"ok": False, "error": "identity unknown"}
        target = RNS.Destination(
            identity, RNS.Destination.OUT, RNS.Destination.SINGLE, APP_NAME, SERVER_ASPECT,
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
