"""Config read/write with commit-or-rollback failsafe."""

import configparser
import io
import shutil
import subprocess
import threading
import time
from pathlib import Path

import RNS

CONFIG_PATHS = {
    "rns": Path.home() / ".reticulum" / "config",
    "agent": Path("/etc/bloxx/agent.json"),
}

BACKUP_SUFFIX = ".bloxx_backup"


class ConfigHandler:
    def __init__(self, cfg: dict, config_path: str = "/etc/bloxx/agent.json"):
        self._cfg = cfg
        self._agent_config_path = Path(config_path)
        self._rollback_timer: threading.Thread | None = None
        self._watchdog_dest_hashes: list[str] = cfg.get("server_dest_hashes", [])
        self._watchdog_timeout: int = cfg.get("watchdog_timeout_s", 300)

    # ------------------------------------------------------------------
    # Read
    # ------------------------------------------------------------------

    def get_config(self, cfg_type: str) -> str:
        if cfg_type == "rns":
            return self._read_file(self._rns_path())
        if cfg_type == "agent":
            return self._read_file(self._agent_config_path)
        if cfg_type == "system":
            return self._system_info()
        raise ValueError(f"Unknown config type: {cfg_type}")

    def _rns_path(self) -> Path:
        custom = self._cfg.get("rns_config_path")
        if custom:
            return Path(custom).expanduser()
        return CONFIG_PATHS["rns"]

    def _read_file(self, path: Path) -> str:
        if not path.exists():
            raise FileNotFoundError(f"{path} not found")
        return path.read_text(encoding="utf-8")

    def _system_info(self) -> str:
        lines = []
        try:
            r = subprocess.run(["ip", "addr"], capture_output=True, text=True, timeout=5)
            lines.append("=== ip addr ===\n" + r.stdout)
        except Exception:
            pass
        try:
            r = subprocess.run(["nmcli", "device"], capture_output=True, text=True, timeout=5)
            lines.append("=== nmcli device ===\n" + r.stdout)
        except Exception:
            pass
        return "\n".join(lines)

    # ------------------------------------------------------------------
    # Write — full replace
    # ------------------------------------------------------------------

    def put_config_safe(self, cfg_type: str, content: str) -> dict:
        path = self._resolve_path(cfg_type)
        backup = Path(str(path) + BACKUP_SUFFIX)
        try:
            if path.exists():
                shutil.copy2(path, backup)
            path.write_text(content, encoding="utf-8")
            self._restart_service(cfg_type)
            self._start_commit_watchdog(path, backup)
            return {"ok": True, "status": "pending_commit"}
        except Exception as e:
            self._restore_backup(path, backup)
            return {"ok": False, "error": str(e)}

    # ------------------------------------------------------------------
    # Write — patch (INI key/value)
    # ------------------------------------------------------------------

    def patch_config_safe(self, cfg_type: str, patches: list[dict]) -> dict:
        path = self._resolve_path(cfg_type)
        if not path.exists():
            return {"ok": False, "error": f"{path} not found"}
        backup = Path(str(path) + BACKUP_SUFFIX)
        try:
            original = path.read_text(encoding="utf-8")
            patched = self._apply_ini_patches(original, patches)
            shutil.copy2(path, backup)
            path.write_text(patched, encoding="utf-8")
            self._restart_service(cfg_type)
            self._start_commit_watchdog(path, backup)
            return {"ok": True, "status": "pending_commit"}
        except Exception as e:
            self._restore_backup(path, backup)
            return {"ok": False, "error": str(e)}

    def _apply_ini_patches(self, content: str, patches: list[dict]) -> str:
        """Apply [{section, key, value}] patches to an INI-style config, preserving comments."""
        parser = configparser.RawConfigParser()
        parser.optionxform = str  # preserve key case
        parser.read_string(content)
        for patch in patches:
            section = patch["section"]
            key = patch["key"]
            value = str(patch["value"])
            if not parser.has_section(section):
                parser.add_section(section)
            parser.set(section, key, value)
        buf = io.StringIO()
        parser.write(buf)
        return buf.getvalue()

    # ------------------------------------------------------------------
    # Commit-or-rollback watchdog
    # ------------------------------------------------------------------

    def _start_commit_watchdog(self, path: Path, backup: Path) -> None:
        if self._rollback_timer:
            self._rollback_timer.cancel()

        # Poll the server every 30s; commit on first success, rollback on timeout.
        # A brief server restart (e.g. maintenance) won't trigger a rollback as long
        # as connectivity is restored before the deadline.
        self._rollback_timer = threading.Thread(
            target=self._commit_or_rollback_loop,
            args=(path, backup),
            daemon=True,
            name=f"commit-watchdog-{path.name}",
        )
        self._rollback_timer.start()

    def _commit_or_rollback_loop(self, path: Path, backup: Path) -> None:
        probe_interval = 30
        deadline = time.time() + self._watchdog_timeout
        while time.time() < deadline:
            time.sleep(probe_interval)
            if self._can_reach_server():
                self._commit_config(path, backup)
                return
        # Timeout expired — roll back
        self._rollback_config(path, backup)

    def _can_reach_server(self) -> bool:
        """Try to open a link to any configured server. Returns True if one responds."""
        import RNS as _RNS
        for dest_hash_hex in self._watchdog_dest_hashes:
            try:
                dest_hash = bytes.fromhex(dest_hash_hex)
                if not _RNS.Transport.has_path(dest_hash):
                    continue
                identity = _RNS.Identity.recall(dest_hash)
                if identity is None:
                    continue
                from protocol import APP_NAME, SERVER_ASPECT
                dest = _RNS.Destination(
                    identity, _RNS.Destination.OUT, _RNS.Destination.SINGLE,
                    APP_NAME, SERVER_ASPECT,
                )
                link = _RNS.Link(dest)
                deadline = time.time() + 15
                while link.status != _RNS.Link.ACTIVE and time.time() < deadline:
                    time.sleep(0.2)
                reachable = link.status == _RNS.Link.ACTIVE
                link.teardown()
                if reachable:
                    return True
            except Exception:
                pass
        return False

    def _commit_config(self, path: Path, backup: Path) -> None:
        if backup.exists():
            backup.unlink()
        RNS.log(f"Config committed: {path}", RNS.LOG_NOTICE)

    def _rollback_config(self, path: Path, backup: Path) -> None:
        RNS.log(f"Commit watchdog expired — rolling back {path}", RNS.LOG_WARNING)
        self._restore_backup(path, backup)
        cfg_type = "rns" if "reticulum" in str(path) else "agent"
        self._restart_service(cfg_type)

    def _restore_backup(self, path: Path, backup: Path) -> None:
        if backup.exists():
            shutil.copy2(backup, path)
            backup.unlink()

    def rollback_if_pending(self) -> None:
        """Called at agent startup — rolls back any config that never committed."""
        for cfg_type, path in [("rns", self._rns_path()), ("agent", self._agent_config_path)]:
            backup = Path(str(path) + BACKUP_SUFFIX)
            if backup.exists():
                RNS.log(
                    f"Found uncommitted backup for {cfg_type} — rolling back",
                    RNS.LOG_WARNING,
                )
                self._restore_backup(path, backup)

    # ------------------------------------------------------------------
    # Helpers
    # ------------------------------------------------------------------

    def _resolve_path(self, cfg_type: str) -> Path:
        if cfg_type == "rns":
            return self._rns_path()
        if cfg_type == "agent":
            return self._agent_config_path
        raise ValueError(f"Cannot write config type: {cfg_type}")

    def _restart_service(self, cfg_type: str) -> None:
        service = "rnsd" if cfg_type == "rns" else "bloxx-agent"
        try:
            subprocess.run(["sudo", "systemctl", "restart", service], timeout=15)
        except Exception as e:
            RNS.log(f"Service restart failed for {service}: {e}", RNS.LOG_WARNING)
