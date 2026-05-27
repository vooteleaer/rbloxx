"""Battery/power telemetry. Pluggable backends: ina226, ina219, ups_hat, none."""

from __future__ import annotations

import time
from abc import ABC, abstractmethod

from protocol import ERR_BATT_CRITICAL, ERR_BATT_SENSOR_UNAVAIL, ERR_NO_CHARGING


class PowerReading:
    __slots__ = ("soc_pct", "voltage_v", "power_w", "solar_power_w")

    def __init__(
        self,
        soc_pct: float | None = None,
        voltage_v: float | None = None,
        power_w: float | None = None,
        solar_power_w: float | None = None,
    ):
        self.soc_pct = soc_pct
        self.voltage_v = voltage_v
        self.power_w = power_w           # positive = charging, negative = discharging
        self.solar_power_w = solar_power_w


class PowerBackend(ABC):
    @abstractmethod
    def read(self) -> PowerReading:
        ...


class NoneBackend(PowerBackend):
    def read(self) -> PowerReading:
        return PowerReading()


class INA226Backend(PowerBackend):
    """INA226 current/power monitor over I2C."""

    # Full-charge and cutoff voltages — tune per battery chemistry
    V_FULL = 4.2
    V_EMPTY = 3.0

    def __init__(self, bus: int, addr: int):
        import smbus2
        self._bus = smbus2.SMBus(bus)
        self._addr = addr
        self._configure()

    def _configure(self) -> None:
        # Default config: 16 averages, 1.1ms conversion, shunt + bus continuous
        self._bus.write_word_data(self._addr, 0x00, self._swap(0x4127))

    def _swap(self, val: int) -> int:
        return ((val & 0xFF) << 8) | ((val >> 8) & 0xFF)

    def _read_word(self, reg: int) -> int:
        raw = self._bus.read_word_data(self._addr, reg)
        return self._swap(raw)

    def read(self) -> PowerReading:
        # Bus voltage register 0x02, LSB = 1.25mV
        bus_raw = self._read_word(0x02)
        voltage_v = bus_raw * 0.00125

        # Power register 0x03, LSB = 25mW (depends on calibration)
        power_raw = self._read_word(0x03)
        # Shunt current register 0x01, LSB = 2.5µV / Rshunt
        current_raw = self._read_word(0x01)
        if current_raw > 32767:
            current_raw -= 65536
        # Assume 10mΩ shunt → 1 LSB = 0.00025A
        current_a = current_raw * 0.00025
        power_w = voltage_v * current_a  # positive = into battery = charging

        soc_pct = max(0.0, min(100.0, (voltage_v - self.V_EMPTY) / (self.V_FULL - self.V_EMPTY) * 100))
        return PowerReading(soc_pct=soc_pct, voltage_v=voltage_v, power_w=power_w)


class INA219Backend(PowerBackend):
    """INA219 over I2C (simpler, 12-bit)."""

    V_FULL = 4.2
    V_EMPTY = 3.0

    def __init__(self, bus: int, addr: int):
        import smbus2
        self._bus = smbus2.SMBus(bus)
        self._addr = addr

    def _read_signed(self, reg: int) -> int:
        raw = self._bus.read_word_data(self._addr, reg)
        val = ((raw & 0xFF) << 8) | ((raw >> 8) & 0xFF)
        return val if val < 32768 else val - 65536

    def read(self) -> PowerReading:
        bus_v = (self._read_signed(0x02) >> 3) * 0.004
        shunt_v = self._read_signed(0x01) * 0.00001
        current_a = shunt_v / 0.1  # 100mΩ shunt
        power_w = bus_v * current_a
        soc_pct = max(0.0, min(100.0, (bus_v - self.V_EMPTY) / (self.V_FULL - self.V_EMPTY) * 100))
        return PowerReading(soc_pct=soc_pct, voltage_v=bus_v, power_w=power_w)


def _build_backend(cfg: dict) -> PowerBackend:
    backend = cfg.get("power_backend", "none")
    if backend == "none":
        return NoneBackend()
    bus = cfg.get("power_i2c_bus", 1)
    addr = int(cfg.get("power_i2c_addr", "0x40"), 16) if isinstance(cfg.get("power_i2c_addr"), str) else cfg.get("power_i2c_addr", 0x40)
    if backend == "ina226":
        return INA226Backend(bus, addr)
    if backend == "ina219":
        return INA219Backend(bus, addr)
    return NoneBackend()


class PowerHandler:
    def __init__(self, cfg: dict):
        self._cfg = cfg
        self._thresholds = cfg.get("thresholds", {})
        self._sensor_error = False
        self._last_readings: list[tuple[float, float | None]] = []  # (timestamp, power_w)
        try:
            self._backend = _build_backend(cfg)
        except Exception:
            self._backend = NoneBackend()
            self._sensor_error = cfg.get("power_backend", "none") != "none"

    def collect(self) -> dict:
        try:
            reading = self._backend.read()
            self._sensor_error = False
            self._track_charging(reading.power_w)
            return {
                "batt_soc_pct": reading.soc_pct,
                "batt_voltage_v": reading.voltage_v,
                "batt_power_w": reading.power_w,
                "solar_power_w": reading.solar_power_w,
            }
        except Exception:
            self._sensor_error = True
            return {
                "batt_soc_pct": None,
                "batt_voltage_v": None,
                "batt_power_w": None,
                "solar_power_w": None,
            }

    def _track_charging(self, power_w: float | None) -> None:
        if power_w is None:
            return
        now = time.time()
        self._last_readings.append((now, power_w))
        # Keep last 30 minutes
        cutoff = now - 1800
        self._last_readings = [(t, p) for t, p in self._last_readings if t >= cutoff]

    def get_errors(self) -> list[str]:
        errors = []
        if self._sensor_error:
            errors.append(ERR_BATT_SENSOR_UNAVAIL)
            return errors

        reading = None
        try:
            reading = self._backend.read()
        except Exception:
            pass

        if reading is None:
            return errors

        if reading.soc_pct is not None:
            threshold = self._thresholds.get("batt_critical_pct", 10)
            if reading.soc_pct <= threshold:
                errors.append(ERR_BATT_CRITICAL)

        if self._is_not_charging(reading):
            errors.append(ERR_NO_CHARGING)

        return errors

    def _is_not_charging(self, reading: PowerReading) -> bool:
        """Detect battery draining when it should be charging (solar present but SoC falling)."""
        if reading.solar_power_w is None or reading.solar_power_w < 1.0:
            return False  # No solar — normal discharge expected
        if not self._last_readings or len(self._last_readings) < 3:
            return False
        recent = [p for _, p in self._last_readings[-10:] if p is not None]
        if not recent:
            return False
        return sum(recent) / len(recent) < 0  # Averaging negative = discharging despite solar
