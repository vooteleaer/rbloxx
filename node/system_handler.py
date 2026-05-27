"""System telemetry — zero extra dependencies, pure stdlib + /proc."""

import os
import subprocess
import threading
import time
from pathlib import Path

from protocol import (
    ERR_DISK_FULL, ERR_TEMP_CRITICAL, ERR_LOAD_HIGH, ERR_SWAP_HIGH,
    ERR_FS_READONLY, ERR_FS_ERRORS,
    ERR_OOM_KILLED, ERR_WATCHDOG_REBOOT,
)


# ------------------------------------------------------------------
# Low-level /proc readers (no psutil)
# ------------------------------------------------------------------

def _read_meminfo() -> dict[str, int]:
    info: dict[str, int] = {}
    try:
        with open("/proc/meminfo") as f:
            for line in f:
                k, _, v = line.partition(":")
                info[k.strip()] = int(v.strip().split()[0])  # kB
    except Exception:
        pass
    return info


def _cpu_percent(interval: float = 1.0) -> float:
    def _stat() -> tuple[int, int]:
        try:
            with open("/proc/stat") as f:
                parts = f.readline().split()
            vals = [int(x) for x in parts[1:8]]
            user, nice, system, idle, iowait, irq, softirq = vals
            total = sum(vals)
            return total, idle + iowait
        except Exception:
            return 0, 0

    t1, i1 = _stat()
    time.sleep(interval)
    t2, i2 = _stat()
    delta_total = t2 - t1
    if delta_total == 0:
        return 0.0
    return round(100.0 * (1.0 - (i2 - i1) / delta_total), 1)


def _ram_percent() -> float:
    m = _read_meminfo()
    total = m.get("MemTotal", 0)
    if total == 0:
        return 0.0
    available = m.get("MemAvailable", 0)
    return round(100.0 * (total - available) / total, 1)


def _swap_percent() -> float:
    m = _read_meminfo()
    total = m.get("SwapTotal", 0)
    if total == 0:
        return 0.0
    free = m.get("SwapFree", 0)
    return round(100.0 * (total - free) / total, 1)


def _disk_percent(path: str = "/") -> float:
    try:
        st = os.statvfs(path)
        total = st.f_blocks * st.f_frsize
        free = st.f_bfree * st.f_frsize
        if total == 0:
            return 0.0
        return round(100.0 * (total - free) / total, 1)
    except Exception:
        return 0.0


def _uptime_s() -> int:
    try:
        with open("/proc/uptime") as f:
            return int(float(f.read().split()[0]))
    except Exception:
        return 0


def _cpu_temp() -> float | None:
    try:
        tz = Path("/sys/class/thermal/thermal_zone0/temp")
        if tz.exists():
            return int(tz.read_text().strip()) / 1000.0
    except Exception:
        pass
    return None


def _load_avg() -> tuple[float, float, float]:
    try:
        return os.getloadavg()
    except Exception:
        return (0.0, 0.0, 0.0)


# ------------------------------------------------------------------
# SystemHandler
# ------------------------------------------------------------------

class SystemHandler:
    def __init__(self, cfg: dict):
        self._cfg = cfg
        self._thresholds = cfg.get("thresholds", {})
        self.rns_rtt_ms: float | None = None
        self._transient_errors: list[str] = []
        self._persistent_errors: set[str] = set()
        self._lock = threading.Lock()

    def collect(self) -> dict:
        return {
            "uptime_s": _uptime_s(),
            "cpu_pct": _cpu_percent(interval=0.5),
            "ram_pct": _ram_percent(),
            "disk_pct": _disk_percent(),
            "temp_c": _cpu_temp(),
            "rns_rtt_ms": self.rns_rtt_ms,
        }

    def get_errors(self) -> list[str]:
        errors: list[str] = []
        errors += self._check_thresholds()
        errors += self._check_fs()
        errors += self._check_oom()
        errors += self._check_watchdog_reboot()
        with self._lock:
            errors += list(self._transient_errors)
            self._transient_errors.clear()
            errors += list(self._persistent_errors)
        return list(set(errors))

    def add_transient_error(self, code: str) -> None:
        with self._lock:
            self._transient_errors.append(code)

    def set_persistent_error(self, code: str) -> None:
        with self._lock:
            self._persistent_errors.add(code)

    def clear_persistent_error(self, code: str) -> None:
        with self._lock:
            self._persistent_errors.discard(code)

    def _check_thresholds(self) -> list[str]:
        errors = []
        t = self._thresholds

        if _disk_percent() >= t.get("disk_full_pct", 90):
            errors.append(ERR_DISK_FULL)

        temp = _cpu_temp()
        if temp is not None and temp >= t.get("temp_critical_c", 80):
            errors.append(ERR_TEMP_CRITICAL)

        load1, _, _ = _load_avg()
        cpu_count = os.cpu_count() or 1
        if load1 / cpu_count >= t.get("load_high_factor", 2.0):
            errors.append(ERR_LOAD_HIGH)

        if _swap_percent() >= t.get("swap_high_pct", 80):
            errors.append(ERR_SWAP_HIGH)

        return errors

    def _check_fs(self) -> list[str]:
        errors = []
        try:
            for line in Path("/proc/mounts").read_text().splitlines():
                parts = line.split()
                if len(parts) >= 4 and parts[1] == "/" and "ro" in parts[3].split(","):
                    errors.append(ERR_FS_READONLY)
                    break
        except Exception:
            pass
        try:
            r = subprocess.run(
                ["dmesg", "--level=err,crit", "--since", "1 hour ago"],
                capture_output=True, text=True, timeout=5,
            )
            if any(k in r.stdout.lower() for k in ("i/o error", "ext4-fs error", "filesystem error")):
                errors.append(ERR_FS_ERRORS)
        except Exception:
            pass
        return errors

    def _check_oom(self) -> list[str]:
        try:
            r = subprocess.run(
                ["journalctl", "-k", "--since", "5 minutes ago", "--no-pager", "-q"],
                capture_output=True, text=True, timeout=5,
            )
            if "oom" in r.stdout.lower() or "out of memory" in r.stdout.lower():
                return [ERR_OOM_KILLED]
        except Exception:
            pass
        return []

    def _check_watchdog_reboot(self) -> list[str]:
        flag = Path("/run/bloxx_watchdog_reboot")
        if flag.exists():
            flag.unlink(missing_ok=True)
            return [ERR_WATCHDOG_REBOOT]
        try:
            r = subprocess.run(
                ["journalctl", "-b", "-1", "--no-pager", "-q", "-n", "5"],
                capture_output=True, text=True, timeout=5,
            )
            if "watchdog" in r.stdout.lower():
                return [ERR_WATCHDOG_REBOOT]
        except Exception:
            pass
        return []
