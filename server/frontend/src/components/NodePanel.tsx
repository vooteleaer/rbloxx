import { useEffect, useState } from "react";
import { api, type Node, type TelemetryRow } from "../api/client";
import SparkLine from "./SparkLine";
import { parse as parseIni, serialize as serializeIni, getBool, setBool, type RnsConfig, type RnsInterface } from "../utils/iniParser";
import { latLonToTile, TILE_SIZE } from "../utils/tileMap";

// ---------------------------------------------------------------------------
// Constants
// ---------------------------------------------------------------------------

const ZOOM = 13;
const GRID = 3; // 3×3 tile grid

const REGIONS = [
  { label: "EU 433", default: 433_175_000, min: 433_000_000, max: 434_000_000 },
  { label: "EU 868", default: 869_525_000, min: 863_000_000, max: 870_000_000 },
  { label: "US 915", default: 915_000_000, min: 902_000_000, max: 928_000_000 },
  { label: "2.4 GHz", default: 2_400_000_000, min: 2_400_000_000, max: 2_500_000_000 },
];

const MODEM_PRESETS = [
  { label: "Long Slow",     sf: 12, bw: 125_000, cr: 8 },
  { label: "Long Moderate", sf: 11, bw: 125_000, cr: 8 },
  { label: "Long Fast",     sf: 11, bw: 250_000, cr: 5 },
  { label: "Long Turbo",    sf: 11, bw: 500_000, cr: 8 },
  { label: "Medium Slow",   sf: 10, bw: 250_000, cr: 5 },
  { label: "Medium Fast",   sf:  9, bw: 250_000, cr: 5 },
  { label: "Short Slow",    sf:  8, bw: 250_000, cr: 5 },
  { label: "Short Fast",    sf:  7, bw: 250_000, cr: 5 },
  { label: "Short Turbo",   sf:  7, bw: 500_000, cr: 5 },
];

const BANDWIDTHS = [7_800, 10_400, 15_600, 20_800, 31_250, 41_700, 62_500, 125_000, 250_000, 500_000];

const LOG_LEVELS: Record<number, string> = {
  1: "Critical", 2: "Error", 3: "Warning", 4: "Notice",
  5: "Info", 6: "Verbose", 7: "Debug", 8: "Extreme",
};

const COMMANDS = [
  { value: "svc_restart",         label: "Restart service" },
  { value: "svc_stop",            label: "Stop service" },
  { value: "svc_start",           label: "Start service" },
  { value: "wifi_set",            label: "Set WiFi" },
  { value: "log_pull",            label: "Pull logs" },
  { value: "disk_cleanup",        label: "Disk cleanup" },
  { value: "rns_announce",        label: "RNS announce" },
  { value: "reboot",              label: "Reboot" },
  { value: "shutdown",            label: "Shutdown" },
  { value: "agent_update",        label: "Update agent" },
  { value: "connectivity_check",  label: "Connectivity check" },
  { value: "rnode_reset",         label: "RNode reset" },
  { value: "rnode_update",        label: "RNode update" },
  { value: "shutdown_threshold",  label: "Set shutdown threshold" },
];

// ---------------------------------------------------------------------------
// Helpers
// ---------------------------------------------------------------------------

function fmt(ts: number) {
  return new Date(ts * 1000).toLocaleString();
}

function detectRegion(freq: number) {
  return REGIONS.find((r) => freq >= r.min && freq <= r.max) ?? REGIONS[1];
}

function detectModemPreset(sf: number, bw: number, cr: number) {
  return MODEM_PRESETS.find((p) => p.sf === sf && p.bw === bw && p.cr === cr)?.label ?? "Custom";
}

function Row({ label, value }: { label: string; value: string | number | null | undefined }) {
  return (
    <div className="flex justify-between py-1 border-b border-gray-100 text-sm">
      <span className="text-gray-500">{label}</span>
      <span className="font-mono text-gray-900">{value ?? "—"}</span>
    </div>
  );
}

const inputCls = "rounded border border-gray-200 bg-white px-2 py-1 text-sm font-mono focus:outline-none focus:ring-2 focus:ring-blue-300 w-full";
const selectCls = inputCls;

// ---------------------------------------------------------------------------
// Location map (static OSM tiles)
// ---------------------------------------------------------------------------

function LocationMap({ lat, lon }: { lat: number; lon: number }) {
  const center = latLonToTile(lat, lon, ZOOM);
  const half = Math.floor(GRID / 2);
  const totalPx = GRID * TILE_SIZE;
  const dotX = half * TILE_SIZE + center.px;
  const dotY = half * TILE_SIZE + center.py;

  return (
    <div className="relative overflow-hidden rounded-lg border border-gray-200 flex-shrink-0"
         style={{ width: totalPx, height: totalPx }}>
      {Array.from({ length: GRID }, (_, row) =>
        Array.from({ length: GRID }, (_, col) => {
          const tx = center.x - half + col;
          const ty = center.y - half + row;
          return (
            <img
              key={`${row}-${col}`}
              src={`https://tile.openstreetmap.org/${ZOOM}/${tx}/${ty}.png`}
              alt=""
              width={TILE_SIZE}
              height={TILE_SIZE}
              style={{ position: "absolute", left: col * TILE_SIZE, top: row * TILE_SIZE }}
            />
          );
        })
      )}
      <div
        className="absolute w-3 h-3 rounded-full bg-red-500 border-2 border-white shadow"
        style={{ left: dotX - 6, top: dotY - 6 }}
      />
    </div>
  );
}

// ---------------------------------------------------------------------------
// RNode interface card
// ---------------------------------------------------------------------------

function RNodeCard({ iface, onChange }: {
  iface: RnsInterface;
  onChange(fields: Record<string, string>): void;
}) {
  const f = iface.fields;
  const freq = parseInt(f.frequency ?? "869525000", 10);
  const sf = parseInt(f.spreadingfactor ?? "11", 10);
  const bw = parseInt(f.bandwidth ?? "250000", 10);
  const cr = parseInt(f.codingrate ?? "5", 10);

  const [region, setRegion] = useState(() => detectRegion(freq));
  const [modemPreset, setModemPreset] = useState(() => detectModemPreset(sf, bw, cr));
  const [showAdvanced, setShowAdvanced] = useState(false);
  const [showLocation, setShowLocation] = useState(
    () => !!(f.latitude || f.longitude)
  );

  function set(key: string, value: string) {
    onChange({ ...f, [key]: value });
  }

  function applyModemPreset(label: string) {
    setModemPreset(label);
    const p = MODEM_PRESETS.find((p) => p.label === label);
    if (p) onChange({ ...f, spreadingfactor: String(p.sf), bandwidth: String(p.bw), codingrate: String(p.cr) });
  }

  function applyRegion(r: typeof REGIONS[0]) {
    setRegion(r);
    onChange({ ...f, frequency: String(r.default) });
  }

  return (
    <div className="rounded-lg border border-gray-200 p-4 space-y-3">
      <h4 className="font-medium text-gray-800 text-sm">{iface.name} <span className="text-gray-400 font-normal">RNodeInterface</span></h4>

      <div className="flex items-center gap-2">
        <label className="text-xs text-gray-500 w-24 flex-shrink-0">Enabled</label>
        <input type="checkbox" checked={getBool(f.enabled)} onChange={(e) => set("enabled", setBool(e.target.checked))} className="accent-blue-600" />
      </div>

      <div className="flex items-center gap-2">
        <label className="text-xs text-gray-500 w-24 flex-shrink-0">Port</label>
        <input value={f.port ?? ""} onChange={(e) => set("port", e.target.value)} className={inputCls} placeholder="/dev/ttyACM0" />
      </div>

      {/* Region + modem preset */}
      <div className="grid grid-cols-2 gap-2">
        <div>
          <label className="text-xs text-gray-500 block mb-1">Region</label>
          <select value={region.label} onChange={(e) => applyRegion(REGIONS.find((r) => r.label === e.target.value)!)} className={selectCls}>
            {REGIONS.map((r) => <option key={r.label}>{r.label}</option>)}
          </select>
        </div>
        <div>
          <label className="text-xs text-gray-500 block mb-1">Modem preset</label>
          <select value={modemPreset} onChange={(e) => applyModemPreset(e.target.value)} className={selectCls}>
            {MODEM_PRESETS.map((p) => <option key={p.label}>{p.label}</option>)}
            <option>Custom</option>
          </select>
        </div>
      </div>

      {/* Core radio fields */}
      <div className="grid grid-cols-2 gap-2">
        <div>
          <label className="text-xs text-gray-500 block mb-1">Frequency (Hz)</label>
          <input
            type="number"
            value={f.frequency ?? ""}
            min={region.min}
            max={region.max}
            onChange={(e) => { setModemPreset("Custom"); set("frequency", e.target.value); }}
            className={inputCls}
          />
          <p className="text-xs text-gray-400 mt-0.5">{(region.min/1e6).toFixed(0)}–{(region.max/1e6).toFixed(0)} MHz</p>
        </div>
        <div>
          <label className="text-xs text-gray-500 block mb-1">TX power (dBm)</label>
          <input type="number" value={f.txpower ?? ""} min={-9} max={22} onChange={(e) => set("txpower", e.target.value)} className={inputCls} />
        </div>
        <div>
          <label className="text-xs text-gray-500 block mb-1">Spreading factor</label>
          <select value={f.spreadingfactor ?? "11"} onChange={(e) => { setModemPreset("Custom"); set("spreadingfactor", e.target.value); }} className={selectCls}>
            {[5,6,7,8,9,10,11,12].map((v) => <option key={v}>{v}</option>)}
          </select>
        </div>
        <div>
          <label className="text-xs text-gray-500 block mb-1">Bandwidth (Hz)</label>
          <select value={f.bandwidth ?? "250000"} onChange={(e) => { setModemPreset("Custom"); set("bandwidth", e.target.value); }} className={selectCls}>
            {BANDWIDTHS.map((v) => <option key={v} value={v}>{(v/1000).toFixed(v < 10000 ? 1 : 0)} kHz</option>)}
          </select>
        </div>
        <div>
          <label className="text-xs text-gray-500 block mb-1">Coding rate</label>
          <select value={f.codingrate ?? "5"} onChange={(e) => { setModemPreset("Custom"); set("codingrate", e.target.value); }} className={selectCls}>
            {[5,6,7,8].map((v) => <option key={v} value={v}>4/{v}</option>)}
          </select>
        </div>
        <div>
          <label className="text-xs text-gray-500 block mb-1">Callsign</label>
          <input value={f.id_callsign ?? ""} onChange={(e) => set("id_callsign", e.target.value)} className={inputCls} placeholder="NOCALL" />
        </div>
        <div>
          <label className="text-xs text-gray-500 block mb-1">ID interval (s)</label>
          <input type="number" value={f.id_interval ?? ""} min={0} onChange={(e) => set("id_interval", e.target.value)} className={inputCls} />
        </div>
        <div>
          <label className="text-xs text-gray-500 block mb-1">Airtime limit long (%)</label>
          <input type="number" value={f.airtime_limit_long ?? ""} min={0} max={100} onChange={(e) => set("airtime_limit_long", e.target.value)} className={inputCls} />
        </div>
        <div>
          <label className="text-xs text-gray-500 block mb-1">Airtime limit short (%)</label>
          <input type="number" value={f.airtime_limit_short ?? ""} min={0} max={100} onChange={(e) => set("airtime_limit_short", e.target.value)} className={inputCls} />
        </div>
        <div className="flex items-center gap-2 col-span-2">
          <label className="text-xs text-gray-500">Flow control</label>
          <input type="checkbox" checked={getBool(f.flow_control)} onChange={(e) => set("flow_control", setBool(e.target.checked))} className="accent-blue-600" />
        </div>
      </div>

      {/* Location */}
      <button onClick={() => setShowLocation((v) => !v)} className="text-xs text-blue-600 hover:underline">
        {showLocation ? "▾" : "▸"} Location
      </button>
      {showLocation && (
        <div className="grid grid-cols-3 gap-2">
          <div>
            <label className="text-xs text-gray-500 block mb-1">Latitude</label>
            <input type="number" value={f.latitude ?? ""} min={-90} max={90} step="any" onChange={(e) => set("latitude", e.target.value)} className={inputCls} />
          </div>
          <div>
            <label className="text-xs text-gray-500 block mb-1">Longitude</label>
            <input type="number" value={f.longitude ?? ""} min={-180} max={180} step="any" onChange={(e) => set("longitude", e.target.value)} className={inputCls} />
          </div>
          <div>
            <label className="text-xs text-gray-500 block mb-1">Height (m)</label>
            <input type="number" value={f.height ?? ""} step="any" onChange={(e) => set("height", e.target.value)} className={inputCls} />
          </div>
          <div className="flex items-center gap-2 col-span-3">
            <label className="text-xs text-gray-500">Discoverable</label>
            <input type="checkbox" checked={getBool(f.discoverable)} onChange={(e) => set("discoverable", setBool(e.target.checked))} className="accent-blue-600" />
            {getBool(f.discoverable) && (
              <input value={f.discovery_name ?? ""} onChange={(e) => set("discovery_name", e.target.value)} className={`${inputCls} ml-2`} placeholder="Discovery name" />
            )}
          </div>
        </div>
      )}

      {/* Advanced (common fields) */}
      <button onClick={() => setShowAdvanced((v) => !v)} className="text-xs text-blue-600 hover:underline">
        {showAdvanced ? "▾" : "▸"} Advanced
      </button>
      {showAdvanced && (
        <div className="grid grid-cols-2 gap-2">
          <div>
            <label className="text-xs text-gray-500 block mb-1">Mode</label>
            <select value={f.mode ?? "full"} onChange={(e) => set("mode", e.target.value)} className={selectCls}>
              {["full", "gateway", "access_point", "roaming", "boundary"].map((v) => <option key={v}>{v}</option>)}
            </select>
          </div>
          <div>
            <label className="text-xs text-gray-500 block mb-1">Network name</label>
            <input value={f.network_name ?? ""} onChange={(e) => set("network_name", e.target.value)} className={inputCls} />
          </div>
          <div>
            <label className="text-xs text-gray-500 block mb-1">Passphrase</label>
            <input type="password" value={f.passphrase ?? ""} onChange={(e) => set("passphrase", e.target.value)} className={inputCls} />
          </div>
          <div>
            <label className="text-xs text-gray-500 block mb-1">Announce cap (%)</label>
            <input type="number" value={f.announce_cap ?? ""} min={1} max={100} onChange={(e) => set("announce_cap", e.target.value)} className={inputCls} />
          </div>
          <div className="flex items-center gap-2 col-span-2">
            <label className="text-xs text-gray-500">Outgoing</label>
            <input type="checkbox" checked={getBool(f.outgoing ?? "yes")} onChange={(e) => set("outgoing", setBool(e.target.checked))} className="accent-blue-600" />
          </div>
        </div>
      )}
    </div>
  );
}

// ---------------------------------------------------------------------------
// TCP/UDP interface cards
// ---------------------------------------------------------------------------

function TcpClientCard({ iface, onChange }: { iface: RnsInterface; onChange(f: Record<string, string>): void }) {
  const f = iface.fields;
  const set = (k: string, v: string) => onChange({ ...f, [k]: v });
  const [showAdvanced, setShowAdvanced] = useState(false);
  return (
    <div className="rounded-lg border border-gray-200 p-4 space-y-3">
      <h4 className="font-medium text-gray-800 text-sm">{iface.name} <span className="text-gray-400 font-normal">TCPClientInterface</span></h4>
      <div className="flex items-center gap-2"><label className="text-xs text-gray-500 w-24">Enabled</label><input type="checkbox" checked={getBool(f.enabled)} onChange={(e) => set("enabled", setBool(e.target.checked))} className="accent-blue-600" /></div>
      <div className="grid grid-cols-2 gap-2">
        <div><label className="text-xs text-gray-500 block mb-1">Host</label><input value={f.target_host ?? ""} onChange={(e) => set("target_host", e.target.value)} className={inputCls} /></div>
        <div><label className="text-xs text-gray-500 block mb-1">Port</label><input type="number" value={f.target_port ?? ""} min={1} max={65535} onChange={(e) => set("target_port", e.target.value)} className={inputCls} /></div>
      </div>
      <button onClick={() => setShowAdvanced((v) => !v)} className="text-xs text-blue-600 hover:underline">{showAdvanced ? "▾" : "▸"} Advanced</button>
      {showAdvanced && (
        <div className="grid grid-cols-2 gap-2">
          <div><label className="text-xs text-gray-500 block mb-1">Mode</label><select value={f.mode ?? "full"} onChange={(e) => set("mode", e.target.value)} className={selectCls}>{["full","gateway","access_point","roaming","boundary"].map((v) => <option key={v}>{v}</option>)}</select></div>
          <div><label className="text-xs text-gray-500 block mb-1">Network name</label><input value={f.network_name ?? ""} onChange={(e) => set("network_name", e.target.value)} className={inputCls} /></div>
          <div><label className="text-xs text-gray-500 block mb-1">Passphrase</label><input type="password" value={f.passphrase ?? ""} onChange={(e) => set("passphrase", e.target.value)} className={inputCls} /></div>
        </div>
      )}
    </div>
  );
}

function UdpCard({ iface, onChange }: { iface: RnsInterface; onChange(f: Record<string, string>): void }) {
  const f = iface.fields;
  const set = (k: string, v: string) => onChange({ ...f, [k]: v });
  const [showAdvanced, setShowAdvanced] = useState(false);
  return (
    <div className="rounded-lg border border-gray-200 p-4 space-y-3">
      <h4 className="font-medium text-gray-800 text-sm">{iface.name} <span className="text-gray-400 font-normal">UDPInterface</span></h4>
      <div className="flex items-center gap-2"><label className="text-xs text-gray-500 w-24">Enabled</label><input type="checkbox" checked={getBool(f.enabled)} onChange={(e) => set("enabled", setBool(e.target.checked))} className="accent-blue-600" /></div>
      <div className="grid grid-cols-2 gap-2">
        <div><label className="text-xs text-gray-500 block mb-1">Listen IP</label><input value={f.listen_ip ?? ""} onChange={(e) => set("listen_ip", e.target.value)} className={inputCls} /></div>
        <div><label className="text-xs text-gray-500 block mb-1">Listen port</label><input type="number" value={f.listen_port ?? ""} min={1} max={65535} onChange={(e) => set("listen_port", e.target.value)} className={inputCls} /></div>
        <div><label className="text-xs text-gray-500 block mb-1">Forward IP</label><input value={f.forward_ip ?? ""} onChange={(e) => set("forward_ip", e.target.value)} className={inputCls} /></div>
        <div><label className="text-xs text-gray-500 block mb-1">Forward port</label><input type="number" value={f.forward_port ?? ""} min={1} max={65535} onChange={(e) => set("forward_port", e.target.value)} className={inputCls} /></div>
      </div>
      <button onClick={() => setShowAdvanced((v) => !v)} className="text-xs text-blue-600 hover:underline">{showAdvanced ? "▾" : "▸"} Advanced</button>
      {showAdvanced && (
        <div className="grid grid-cols-2 gap-2">
          <div><label className="text-xs text-gray-500 block mb-1">Mode</label><select value={f.mode ?? "full"} onChange={(e) => set("mode", e.target.value)} className={selectCls}>{["full","gateway","access_point","roaming","boundary"].map((v) => <option key={v}>{v}</option>)}</select></div>
          <div><label className="text-xs text-gray-500 block mb-1">Network name</label><input value={f.network_name ?? ""} onChange={(e) => set("network_name", e.target.value)} className={inputCls} /></div>
        </div>
      )}
    </div>
  );
}

function UnknownCard({ iface }: { iface: RnsInterface }) {
  return (
    <div className="rounded-lg border border-gray-200 p-4 space-y-1">
      <h4 className="font-medium text-gray-800 text-sm">{iface.name} <span className="text-gray-400 font-normal">{iface.fields.type ?? "unknown type"}</span></h4>
      {Object.entries(iface.fields).map(([k, v]) => (
        <div key={k} className="flex justify-between text-xs font-mono text-gray-600 border-b border-gray-100 py-0.5">
          <span className="text-gray-400">{k}</span><span>{v}</span>
        </div>
      ))}
    </div>
  );
}

// ---------------------------------------------------------------------------
// RNS Config tab
// ---------------------------------------------------------------------------

function RnsConfigTab({ destHash }: { destHash: string }) {
  const [rnsConfig, setRnsConfig] = useState<RnsConfig | null>(null);
  const [status, setStatus] = useState("");
  const [noPath, setNoPath] = useState(false);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    setLoading(true);
    loadConfig();
  }, [destHash]);

  async function loadConfig(forceRefresh = false) {
    setStatus("");
    setNoPath(false);
    try {
      let content: string;
      if (!forceRefresh) {
        try {
          const snap = await api.config.snapshot(destHash, "rns");
          content = snap.content;
        } catch {
          const pulled = await api.config.pull(destHash, "rns");
          content = pulled.content;
        }
      } else {
        setStatus("Pulling from node…");
        const pulled = await api.config.pull(destHash, "rns");
        content = pulled.content;
        setStatus("Pulled from node");
      }
      setRnsConfig(parseIni(content));
    } catch (e: any) {
      if ((e.message as string).startsWith("no_path:")) {
        setNoPath(true);
      } else {
        setStatus(`Error: ${e.message}`);
      }
    } finally {
      setLoading(false);
    }
  }

  function validate(cfg: RnsConfig): string[] {
    const errors: string[] = [];
    for (const iface of cfg.interfaces) {
      const f = iface.fields;
      if (f.type === "RNodeInterface") {
        const freq = parseInt(f.frequency ?? "0", 10);
        const region = detectRegion(freq);
        if (freq < region.min || freq > region.max)
          errors.push(`${iface.name}: frequency ${freq} out of range for ${region.label}`);
        const tx = parseInt(f.txpower ?? "0", 10);
        if (tx < -9 || tx > 22) errors.push(`${iface.name}: txpower ${tx} out of range (−9–22)`);
        const sf = parseInt(f.spreadingfactor ?? "0", 10);
        if (sf < 5 || sf > 12) errors.push(`${iface.name}: spreadingfactor must be 5–12`);
        const lat = parseFloat(f.latitude ?? "0");
        const lon = parseFloat(f.longitude ?? "0");
        if (f.latitude && (lat < -90 || lat > 90)) errors.push(`${iface.name}: latitude out of range`);
        if (f.longitude && (lon < -180 || lon > 180)) errors.push(`${iface.name}: longitude out of range`);
      }
    }
    return errors;
  }

  async function save() {
    if (!rnsConfig) return;
    const errors = validate(rnsConfig);
    if (errors.length) { setStatus(errors.join("; ")); return; }
    setStatus("Saving…");
    try {
      const content = serializeIni(rnsConfig);
      const r = await api.config.put(destHash, "rns", content);
      setStatus(r.status === "pending_commit" ? "Saved — awaiting commit confirmation" : "Saved ✓");
    } catch (e: any) {
      setStatus(`Error: ${e.message}`);
    }
  }

  function updateIface(idx: number, fields: Record<string, string>) {
    if (!rnsConfig) return;
    const interfaces = rnsConfig.interfaces.map((iface, i) =>
      i === idx ? { ...iface, fields } : iface
    );
    setRnsConfig({ ...rnsConfig, interfaces });
  }

  function setReticulumField(k: string, v: string) {
    if (!rnsConfig) return;
    setRnsConfig({ ...rnsConfig, reticulum: { ...rnsConfig.reticulum, [k]: v } });
  }

  function setLoggingField(k: string, v: string) {
    if (!rnsConfig) return;
    setRnsConfig({ ...rnsConfig, logging: { ...rnsConfig.logging, [k]: v } });
  }

  // Collect location from first RNode with lat/lon
  const locationIface = rnsConfig?.interfaces.find(
    (i) => i.fields.type === "RNodeInterface" && i.fields.latitude && i.fields.longitude
  );
  const lat = locationIface ? parseFloat(locationIface.fields.latitude!) : null;
  const lon = locationIface ? parseFloat(locationIface.fields.longitude!) : null;

  if (loading) return <p className="text-sm text-gray-400 p-4">Loading…</p>;

  if (noPath) return (
    <div className="rounded-lg border border-amber-200 bg-amber-50 p-4 space-y-2">
      <p className="text-sm text-amber-800 font-medium">No path to node</p>
      <p className="text-xs text-amber-700">The node may be offline or has not announced yet. If it just came online, wait a moment for its announce to propagate.</p>
      <button onClick={() => { setLoading(true); loadConfig(true); }} className="text-xs px-3 py-1.5 rounded border border-amber-300 text-amber-800 hover:bg-amber-100">
        Retry
      </button>
    </div>
  );

  return (
    <div className="space-y-4">
      {/* Location map */}
      {lat != null && lon != null && !isNaN(lat) && !isNaN(lon) && (
        <div className="flex justify-center">
          <LocationMap lat={lat} lon={lon} />
        </div>
      )}

      {rnsConfig && (
        <>
          {/* [reticulum] */}
          <div className="rounded-lg border border-gray-200 p-4 space-y-2">
            <h4 className="font-medium text-gray-700 text-sm">[reticulum]</h4>
            {[
              { k: "enable_transport", label: "Enable transport" },
              { k: "share_instance", label: "Share instance" },
              { k: "use_implicit_proof", label: "Use implicit proof" },
              { k: "panic_on_interface_error", label: "Panic on interface error" },
            ].map(({ k, label }) => (
              <div key={k} className="flex items-center gap-2">
                <label className="text-xs text-gray-500 w-44">{label}</label>
                <input type="checkbox" checked={getBool(rnsConfig.reticulum[k])} onChange={(e) => setReticulumField(k, setBool(e.target.checked))} className="accent-blue-600" />
              </div>
            ))}
            <div className="flex items-center gap-2">
              <label className="text-xs text-gray-500 w-44">Shared instance expiry</label>
              <input type="number" value={rnsConfig.reticulum.shared_instance_expiry ?? ""} onChange={(e) => setReticulumField("shared_instance_expiry", e.target.value)} className={`${inputCls} w-28`} />
            </div>
          </div>

          {/* [logging] */}
          <div className="rounded-lg border border-gray-200 p-4 space-y-2">
            <h4 className="font-medium text-gray-700 text-sm">[logging]</h4>
            <div className="flex items-center gap-2">
              <label className="text-xs text-gray-500 w-24">Log level</label>
              <select value={rnsConfig.logging.loglevel ?? "4"} onChange={(e) => setLoggingField("loglevel", e.target.value)} className={`${selectCls} w-48`}>
                {Object.entries(LOG_LEVELS).map(([v, l]) => <option key={v} value={v}>{v} — {l}</option>)}
              </select>
            </div>
          </div>

          {/* Interfaces */}
          {rnsConfig.interfaces.map((iface, idx) => {
            const type = iface.fields.type ?? "";
            if (type === "RNodeInterface")
              return <RNodeCard key={iface.name} iface={iface} onChange={(f) => updateIface(idx, f)} />;
            if (type === "TCPClientInterface")
              return <TcpClientCard key={iface.name} iface={iface} onChange={(f) => updateIface(idx, f)} />;
            if (type === "UDPInterface")
              return <UdpCard key={iface.name} iface={iface} onChange={(f) => updateIface(idx, f)} />;
            return <UnknownCard key={iface.name} iface={iface} />;
          })}
        </>
      )}

      {status && <p className={`text-xs ${status.startsWith("Error") ? "text-red-600" : "text-gray-500"}`}>{status}</p>}

      <div className="flex gap-2 pt-1">
        <button onClick={() => loadConfig(true)} className="px-3 py-1.5 rounded border border-gray-200 text-xs text-gray-700 hover:bg-gray-50">
          Refresh from node
        </button>
        <button onClick={save} className="px-3 py-1.5 rounded bg-blue-600 text-white text-xs hover:bg-blue-700 ml-auto">
          Save
        </button>
      </div>
    </div>
  );
}

// ---------------------------------------------------------------------------
// Agent Config tab
// ---------------------------------------------------------------------------

function AgentConfigTab({ destHash }: { destHash: string }) {
  const [cfg, setCfg] = useState<Record<string, any> | null>(null);
  const [status, setStatus] = useState("");
  const [noPath, setNoPath] = useState(false);
  const [loading, setLoading] = useState(true);

  useEffect(() => { setLoading(true); loadConfig(); }, [destHash]);

  async function loadConfig(forceRefresh = false) {
    setStatus("");
    setNoPath(false);
    try {
      let content: string;
      if (!forceRefresh) {
        try {
          const snap = await api.config.snapshot(destHash, "agent");
          content = snap.content;
        } catch {
          const pulled = await api.config.pull(destHash, "agent");
          content = pulled.content;
        }
      } else {
        setStatus("Pulling from node…");
        const pulled = await api.config.pull(destHash, "agent");
        content = pulled.content;
        setStatus("Pulled from node");
      }
      setCfg(JSON.parse(content));
    } catch (e: any) {
      if ((e.message as string).startsWith("no_path:")) {
        setNoPath(true);
      } else {
        setStatus(`Error: ${e.message}`);
      }
    } finally {
      setLoading(false);
    }
  }

  function set(k: string, v: any) { setCfg((c) => ({ ...c!, [k]: v })); }

  function setListItem(k: string, idx: number, v: string) {
    const arr = [...(cfg![k] ?? [])];
    arr[idx] = v;
    set(k, arr);
  }

  function addListItem(k: string) { set(k, [...(cfg![k] ?? []), ""]); }
  function removeListItem(k: string, idx: number) { set(k, (cfg![k] ?? []).filter((_: any, i: number) => i !== idx)); }

  function validate(): string[] {
    if (!cfg) return ["No config loaded"];
    const errs: string[] = [];
    if ((cfg.announce_interval ?? 0) < 30) errs.push("Announce interval must be ≥ 30s");
    if ((cfg.shutdown_soc_pct ?? 0) < 0 || (cfg.shutdown_soc_pct ?? 0) > 100) errs.push("Shutdown SoC must be 0–100");
    return errs;
  }

  async function save() {
    if (!cfg) return;
    const errs = validate();
    if (errs.length) { setStatus(errs.join("; ")); return; }
    setStatus("Saving…");
    try {
      const r = await api.config.put(destHash, "agent", JSON.stringify(cfg, null, 2));
      setStatus(r.status === "pending_commit" ? "Saved — awaiting commit" : "Saved ✓");
    } catch (e: any) {
      setStatus(`Error: ${e.message}`);
    }
  }

  if (loading) return <p className="text-sm text-gray-400 p-4">Loading…</p>;

  if (noPath) return (
    <div className="rounded-lg border border-amber-200 bg-amber-50 p-4 space-y-2">
      <p className="text-sm text-amber-800 font-medium">No path to node</p>
      <p className="text-xs text-amber-700">The node may be offline or has not announced yet. If it just came online, wait a moment for its announce to propagate.</p>
      <button onClick={() => { setLoading(true); loadConfig(true); }} className="text-xs px-3 py-1.5 rounded border border-amber-300 text-amber-800 hover:bg-amber-100">
        Retry
      </button>
    </div>
  );

  if (!cfg) return <p className="text-sm text-gray-400 p-4">No config. <button onClick={() => loadConfig(true)} className="text-blue-600 underline">Pull from node</button></p>;

  const ListField = ({ k, label }: { k: string; label: string }) => (
    <div className="space-y-1">
      <label className="text-xs text-gray-500">{label}</label>
      {(cfg[k] ?? []).map((v: string, i: number) => (
        <div key={i} className="flex gap-1">
          <input value={v} onChange={(e) => setListItem(k, i, e.target.value)} className={`${inputCls} flex-1`} />
          <button onClick={() => removeListItem(k, i)} className="text-red-500 text-xs px-1 hover:text-red-700">✕</button>
        </div>
      ))}
      <button onClick={() => addListItem(k)} className="text-xs text-blue-600 hover:underline">+ Add</button>
    </div>
  );

  return (
    <div className="space-y-3">
      <div className="grid grid-cols-2 gap-3">
        {[
          { k: "announce_interval", label: "Announce interval (s)", min: 30 },
          { k: "shutdown_soc_pct", label: "Shutdown battery % (0=off)", min: 0, max: 100 },
          { k: "watchdog_feed_interval_s", label: "Watchdog feed interval (s)", min: 1 },
          { k: "zero_traffic_minutes", label: "Zero traffic timeout (min)", min: 1 },
          { k: "time_sync_interval", label: "Time sync interval (s)", min: 60 },
        ].map(({ k, label, min, max }) => (
          <div key={k}>
            <label className="text-xs text-gray-500 block mb-1">{label}</label>
            <input type="number" value={cfg[k] ?? ""} min={min} max={max} onChange={(e) => set(k, Number(e.target.value))} className={inputCls} />
          </div>
        ))}
      </div>
      <ListField k="server_dest_hashes" label="Server destination hashes" />
      <ListField k="rnode_ports" label="RNode ports" />

      {status && <p className={`text-xs ${status.startsWith("Error") ? "text-red-600" : "text-gray-500"}`}>{status}</p>}
      <div className="flex gap-2 pt-1">
        <button onClick={() => loadConfig(true)} className="px-3 py-1.5 rounded border border-gray-200 text-xs text-gray-700 hover:bg-gray-50">Refresh from node</button>
        <button onClick={save} className="px-3 py-1.5 rounded bg-blue-600 text-white text-xs hover:bg-blue-700 ml-auto">Save</button>
      </div>
    </div>
  );
}

// ---------------------------------------------------------------------------
// Commands section
// ---------------------------------------------------------------------------

function CommandsSection({ destHash }: { destHash: string }) {
  const [cmd, setCmd] = useState("svc_restart");
  const [params, setParams] = useState<Record<string, any>>({ service: "rnsd" });
  const [output, setOutput] = useState("");

  function handleCmdChange(newCmd: string) {
    setCmd(newCmd);
    setOutput("");
    const defaults: Record<string, Record<string, any>> = {
      svc_restart: { service: "rnsd" },
      svc_stop: { service: "rnsd" },
      svc_start: { service: "rnsd" },
      wifi_set: { enabled: true },
      log_pull: { lines: 50 },
      reboot: { delay_s: 5 },
      shutdown: { delay_s: 5 },
      shutdown_threshold: { soc_pct: 20 },
      connectivity_check: { dest_hash: "" },
      rnode_reset: { port: "" },
      rnode_update: { port: "" },
    };
    setParams(defaults[newCmd] ?? {});
  }

  function setParam(k: string, v: any) { setParams((p) => ({ ...p, [k]: v })); }

  async function execute() {
    setOutput("Sending…");
    try {
      const r = await api.nodes.command(destHash, { cmd, ...params });
      setOutput(r.output ?? (r.ok ? "OK" : r.error ?? "Failed"));
    } catch (e: any) {
      setOutput(`Error: ${e.message}`);
    }
  }

  const P = ({ label, children }: { label: string; children: React.ReactNode }) => (
    <div className="flex items-center gap-2">
      <label className="text-xs text-gray-500 w-28 flex-shrink-0">{label}</label>
      {children}
    </div>
  );

  return (
    <div className="space-y-3">
      <div>
        <label className="text-xs text-gray-500 block mb-1">Command</label>
        <select value={cmd} onChange={(e) => handleCmdChange(e.target.value)} className={`${selectCls} w-56`}>
          {COMMANDS.map((c) => <option key={c.value} value={c.value}>{c.label}</option>)}
        </select>
      </div>

      {["svc_restart","svc_stop","svc_start"].includes(cmd) && (
        <P label="Service"><input value={params.service ?? ""} onChange={(e) => setParam("service", e.target.value)} className={`${inputCls} w-40`} /></P>
      )}
      {cmd === "wifi_set" && (
        <P label="Enable"><select value={String(params.enabled)} onChange={(e) => setParam("enabled", e.target.value === "true")} className={`${selectCls} w-24`}><option value="true">On</option><option value="false">Off</option></select></P>
      )}
      {cmd === "log_pull" && (<>
        <P label="Lines"><input type="number" value={params.lines ?? 50} min={1} max={1000} onChange={(e) => setParam("lines", Number(e.target.value))} className={`${inputCls} w-24`} /></P>
        <P label="Unit (optional)"><input value={params.unit ?? ""} onChange={(e) => setParam("unit", e.target.value || undefined)} className={`${inputCls} w-40`} placeholder="bloxx-agent" /></P>
      </>)}
      {["reboot","shutdown"].includes(cmd) && (
        <P label="Delay (s)"><input type="number" value={params.delay_s ?? 5} min={0} onChange={(e) => setParam("delay_s", Number(e.target.value))} className={`${inputCls} w-24`} /></P>
      )}
      {cmd === "shutdown_threshold" && (
        <P label="Battery SoC %"><input type="number" value={params.soc_pct ?? 20} min={0} max={100} onChange={(e) => setParam("soc_pct", Number(e.target.value))} className={`${inputCls} w-24`} /></P>
      )}
      {cmd === "connectivity_check" && (
        <P label="Dest hash"><input value={params.dest_hash ?? ""} onChange={(e) => setParam("dest_hash", e.target.value)} className={`${inputCls} w-64`} /></P>
      )}
      {["rnode_reset","rnode_update"].includes(cmd) && (
        <P label="Port"><input value={params.port ?? ""} onChange={(e) => setParam("port", e.target.value)} className={`${inputCls} w-40`} placeholder="/dev/ttyACM0" /></P>
      )}

      <button onClick={execute} className="px-4 py-1.5 rounded bg-gray-800 text-white text-xs hover:bg-gray-700">Execute</button>

      {output && (
        <pre className="rounded-lg bg-gray-900 text-green-300 text-xs p-3 overflow-auto max-h-48 whitespace-pre-wrap">{output}</pre>
      )}
    </div>
  );
}

// ---------------------------------------------------------------------------
// Main NodePanel
// ---------------------------------------------------------------------------

interface Props {
  destHash: string;
  node: Node;
  onDelete(): void;
  liveTelemetry?: Record<string, unknown>;
}

type Tab = "rns" | "agent";

export default function NodePanel({ destHash, node, onDelete, liveTelemetry }: Props) {
  const [telemetry, setTelemetry] = useState<TelemetryRow[]>([]);
  const [tab, setTab] = useState<Tab>("rns");
  const [labelEdit, setLabelEdit] = useState<string | null>(null);
  const [labelSaving, setLabelSaving] = useState(false);

  useEffect(() => {
    api.nodes.telemetry(destHash, 60).then(setTelemetry).catch(() => {});
  }, [destHash]);

  // Prepend live WS telemetry to sparkline data
  useEffect(() => {
    if (!liveTelemetry) return;
    const row = liveTelemetry as unknown as TelemetryRow;
    setTelemetry((prev) => [row, ...prev].slice(0, 60));
  }, [liveTelemetry]);

  async function handleDelete() {
    if (!window.confirm("Delete this node and all its telemetry? This cannot be undone.")) return;
    await api.nodes.delete(destHash);
    onDelete();
  }

  async function saveLabel() {
    if (labelEdit === null) return;
    setLabelSaving(true);
    try {
      await api.nodes.patch(destHash, labelEdit.trim() || null);
    } catch { /* ignore */ } finally {
      setLabelSaving(false);
      setLabelEdit(null);
    }
  }

  const spark = (field: keyof TelemetryRow, label: string, unit: string, color?: string, min?: number, max?: number) => {
    const data = [...telemetry].reverse().map((r) => r[field] as number | null);
    const latest = telemetry[0]?.[field] as number | null ?? null;
    if (data.every((v) => v == null)) return null;
    return <SparkLine key={field as string} data={data} label={label} unit={unit} latest={latest} color={color} min={min} max={max} />;
  };

  const dotColor = !node.online ? "text-red-500" : node.last_errors.length ? "text-amber-400" : "text-green-500";
  const displayName = node.label ?? node.hostname ?? "Unknown";

  return (
    <div className="p-5 space-y-5">
      {/* Header */}
      <div className="flex items-center gap-3 flex-wrap">
        {labelEdit === null ? (
          <h2
            className="text-xl font-bold text-gray-900 cursor-pointer hover:text-blue-600"
            title="Click to rename"
            onClick={() => setLabelEdit(node.label ?? "")}
          >
            {displayName}
          </h2>
        ) : (
          <div className="flex items-center gap-1">
            <input
              autoFocus
              value={labelEdit}
              onChange={(e) => setLabelEdit(e.target.value)}
              onKeyDown={(e) => { if (e.key === "Enter") saveLabel(); if (e.key === "Escape") setLabelEdit(null); }}
              className="text-xl font-bold rounded border border-blue-300 px-1 focus:outline-none focus:ring-2 focus:ring-blue-300 w-48"
              placeholder={node.hostname ?? "Label"}
            />
            <button onClick={saveLabel} disabled={labelSaving} className="text-xs text-blue-600 px-2 py-1 hover:underline disabled:opacity-50">Save</button>
            <button onClick={() => setLabelEdit(null)} className="text-xs text-gray-400 px-1 hover:text-gray-700">✕</button>
          </div>
        )}
        {node.label && node.hostname && node.label !== node.hostname && (
          <span className="text-sm text-gray-400 font-mono">{node.hostname}</span>
        )}
        <span className={`text-xs font-medium ${dotColor}`}>● {node.online ? "online" : "offline"}</span>
        {node.last_errors.length > 0 && (
          <div className="flex gap-1 flex-wrap">
            {node.last_errors.map((e) => (
              <span key={e} className="rounded-full bg-red-100 px-2 py-0.5 text-xs text-red-700 font-mono">{e}</span>
            ))}
          </div>
        )}
        <button onClick={handleDelete} className="ml-auto text-xs text-red-600 border border-red-200 rounded px-2 py-1 hover:bg-red-50">Delete</button>
      </div>

      {/* Info rows */}
      <div className="rounded-xl border border-gray-200 bg-white p-4 shadow-sm">
        <Row label="Destination hash" value={node.dest_hash} />
        <Row label="Identity hash" value={node.identity_hash} />
        <Row label="Version" value={node.version} />
        <Row label="First seen" value={fmt(node.first_seen)} />
        <Row label="Last seen" value={fmt(node.last_seen)} />
      </div>

      {/* Telemetry sparklines */}
      {telemetry.length > 0 && (
        <div className="rounded-xl border border-gray-200 bg-white p-4 shadow-sm space-y-4">
          <div className="flex flex-wrap gap-6">
            {spark("cpu_pct",     "CPU",     "%",  "#3b82f6", 0, 100)}
            {spark("ram_pct",     "RAM",     "%",  "#8b5cf6", 0, 100)}
            {spark("disk_pct",   "Disk",    "%",  "#f59e0b", 0, 100)}
            {spark("temp_c",     "Temp",    "°C", "#ef4444")}
            {spark("rns_rtt_ms", "RTT",     "ms", "#64748b")}
            {spark("batt_soc_pct",   "Battery",  "%", "#22c55e", 0, 100)}
            {spark("batt_power_w",   "Bat power", "W", "#16a34a")}
            {spark("solar_power_w",  "Solar",    "W", "#eab308")}
          </div>

          {/* RNode section — only rendered when the node has RNode data */}
          {(() => {
            const rnodeSparks = [
              spark("rnode_airtime_short",      "Airtime (short)", "%",   "#06b6d4", 0, 100),
              spark("rnode_airtime_long",       "Airtime (long)",  "%",   "#0891b2", 0, 100),
              spark("rnode_channel_load_short", "Ch load",         "%",   "#7c3aed", 0, 100),
              spark("rnode_noise_floor",        "Noise floor",     "dBm", "#94a3b8"),
              spark("rnode_interference_dbm",   "Interference",    "dBm", "#f43f5e"),
              spark("rnode_bitrate",            "Bitrate",         "bps", "#10b981"),
            ].filter(Boolean);
            if (!rnodeSparks.length) return null;
            return (
              <div>
                <p className="text-xs text-gray-400 mb-3">RNode</p>
                <div className="flex flex-wrap gap-6">{rnodeSparks}</div>
              </div>
            );
          })()}
        </div>
      )}

      {/* Settings tabs */}
      <div className="rounded-xl border border-gray-200 bg-white shadow-sm">
        <div className="flex border-b border-gray-100">
          {(["rns", "agent"] as Tab[]).map((t) => (
            <button
              key={t}
              onClick={() => setTab(t)}
              className={`px-4 py-2.5 text-sm font-medium border-b-2 -mb-px transition-colors ${
                tab === t ? "border-blue-600 text-blue-600" : "border-transparent text-gray-500 hover:text-gray-700"
              }`}
            >
              {t === "rns" ? "RNS Config" : "Agent Config"}
            </button>
          ))}
        </div>
        <div className="p-4">
          {tab === "rns" ? <RnsConfigTab destHash={destHash} /> : <AgentConfigTab destHash={destHash} />}
        </div>
      </div>

      {/* Commands */}
      <div className="rounded-xl border border-gray-200 bg-white p-4 shadow-sm">
        <h3 className="text-sm font-semibold text-gray-700 mb-3">Commands</h3>
        <CommandsSection destHash={destHash} />
      </div>
    </div>
  );
}
