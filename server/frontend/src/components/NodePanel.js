import { jsx as _jsx, jsxs as _jsxs, Fragment as _Fragment } from "react/jsx-runtime";
import { useEffect, useState } from "react";
import { api } from "../api/client";
import SparkLine from "./SparkLine";
import { parse as parseIni, serialize as serializeIni, getBool, setBool } from "../utils/iniParser";
import { latLonToTile, TILE_SIZE } from "../utils/tileMap";
// ---------------------------------------------------------------------------
// Constants
// ---------------------------------------------------------------------------
const ZOOM = 13;
const GRID = 3; // 3×3 tile grid
const REGIONS = [
    { label: "EU 433", default: 433175000, min: 433000000, max: 434000000 },
    { label: "EU 868", default: 869525000, min: 863000000, max: 870000000 },
    { label: "US 915", default: 915000000, min: 902000000, max: 928000000 },
    { label: "2.4 GHz", default: 2400000000, min: 2400000000, max: 2500000000 },
];
const MODEM_PRESETS = [
    { label: "Long Slow", sf: 12, bw: 125000, cr: 8 },
    { label: "Long Moderate", sf: 11, bw: 125000, cr: 8 },
    { label: "Long Fast", sf: 11, bw: 250000, cr: 5 },
    { label: "Long Turbo", sf: 11, bw: 500000, cr: 8 },
    { label: "Medium Slow", sf: 10, bw: 250000, cr: 5 },
    { label: "Medium Fast", sf: 9, bw: 250000, cr: 5 },
    { label: "Short Slow", sf: 8, bw: 250000, cr: 5 },
    { label: "Short Fast", sf: 7, bw: 250000, cr: 5 },
    { label: "Short Turbo", sf: 7, bw: 500000, cr: 5 },
];
const BANDWIDTHS = [7800, 10400, 15600, 20800, 31250, 41700, 62500, 125000, 250000, 500000];
const LOG_LEVELS = {
    1: "Critical", 2: "Error", 3: "Warning", 4: "Notice",
    5: "Info", 6: "Verbose", 7: "Debug", 8: "Extreme",
};
const COMMANDS = [
    { value: "svc_restart", label: "Restart service" },
    { value: "svc_stop", label: "Stop service" },
    { value: "svc_start", label: "Start service" },
    { value: "wifi_set", label: "Set WiFi" },
    { value: "log_pull", label: "Pull logs" },
    { value: "disk_cleanup", label: "Disk cleanup" },
    { value: "rns_announce", label: "RNS announce" },
    { value: "reboot", label: "Reboot" },
    { value: "shutdown", label: "Shutdown" },
    { value: "agent_update", label: "Update agent" },
    { value: "connectivity_check", label: "Connectivity check" },
    { value: "rnode_reset", label: "RNode reset" },
    { value: "rnode_update", label: "RNode update" },
    { value: "shutdown_threshold", label: "Set shutdown threshold" },
];
// ---------------------------------------------------------------------------
// Helpers
// ---------------------------------------------------------------------------
function fmt(ts) {
    return new Date(ts * 1000).toLocaleString();
}
function detectRegion(freq) {
    return REGIONS.find((r) => freq >= r.min && freq <= r.max) ?? REGIONS[1];
}
function detectModemPreset(sf, bw, cr) {
    return MODEM_PRESETS.find((p) => p.sf === sf && p.bw === bw && p.cr === cr)?.label ?? "Custom";
}
function Row({ label, value }) {
    return (_jsxs("div", { className: "flex justify-between py-1 border-b border-gray-100 text-sm", children: [_jsx("span", { className: "text-gray-500", children: label }), _jsx("span", { className: "font-mono text-gray-900", children: value ?? "—" })] }));
}
const inputCls = "rounded border border-gray-200 bg-white px-2 py-1 text-sm font-mono focus:outline-none focus:ring-2 focus:ring-blue-300 w-full";
const selectCls = inputCls;
// ---------------------------------------------------------------------------
// Location map (static OSM tiles)
// ---------------------------------------------------------------------------
function LocationMap({ lat, lon }) {
    const center = latLonToTile(lat, lon, ZOOM);
    const half = Math.floor(GRID / 2);
    const totalPx = GRID * TILE_SIZE;
    const displayPx = Math.round(totalPx / 2);
    const dotX = half * TILE_SIZE + center.px;
    const dotY = half * TILE_SIZE + center.py;
    return (_jsx("div", { className: "rounded-lg border border-gray-200 flex-shrink-0 overflow-hidden", style: { width: displayPx, height: displayPx }, children: _jsxs("div", { style: { transform: "scale(0.5)", transformOrigin: "top left",
                position: "relative", width: totalPx, height: totalPx }, children: [Array.from({ length: GRID }, (_, row) => Array.from({ length: GRID }, (_, col) => {
                    const tx = center.x - half + col;
                    const ty = center.y - half + row;
                    return (_jsx("img", { src: `https://tile.openstreetmap.org/${ZOOM}/${tx}/${ty}.png`, alt: "", width: TILE_SIZE, height: TILE_SIZE, style: { position: "absolute", left: col * TILE_SIZE, top: row * TILE_SIZE } }, `${row}-${col}`));
                })), _jsx("div", { className: "absolute w-3 h-3 rounded-full bg-red-500 border-2 border-white shadow", style: { left: dotX - 6, top: dotY - 6 } })] }) }));
}
// ---------------------------------------------------------------------------
// RNode interface card
// ---------------------------------------------------------------------------
function RNodeCard({ iface, onChange }) {
    const f = iface.fields;
    const freq = parseInt(f.frequency ?? "869525000", 10);
    const sf = parseInt(f.spreadingfactor ?? "11", 10);
    const bw = parseInt(f.bandwidth ?? "250000", 10);
    const cr = parseInt(f.codingrate ?? "5", 10);
    const [region, setRegion] = useState(() => detectRegion(freq));
    const [modemPreset, setModemPreset] = useState(() => detectModemPreset(sf, bw, cr));
    const [showAdvanced, setShowAdvanced] = useState(false);
    const [showLocation, setShowLocation] = useState(() => !!(f.latitude || f.longitude));
    function set(key, value) {
        onChange({ ...f, [key]: value });
    }
    function applyModemPreset(label) {
        setModemPreset(label);
        const p = MODEM_PRESETS.find((p) => p.label === label);
        if (p)
            onChange({ ...f, spreadingfactor: String(p.sf), bandwidth: String(p.bw), codingrate: String(p.cr) });
    }
    function applyRegion(r) {
        setRegion(r);
        onChange({ ...f, frequency: String(r.default) });
    }
    return (_jsxs("div", { className: "rounded-lg border border-gray-200 p-4 space-y-3", children: [_jsxs("h4", { className: "font-medium text-gray-800 text-sm", children: [iface.name, " ", _jsx("span", { className: "text-gray-400 font-normal", children: "RNodeInterface" })] }), _jsxs("div", { className: "flex items-center gap-2", children: [_jsx("label", { className: "text-xs text-gray-500 w-24 flex-shrink-0", children: "Enabled" }), _jsx("input", { type: "checkbox", checked: getBool(f.enabled), onChange: (e) => set("enabled", setBool(e.target.checked)), className: "accent-blue-600" })] }), _jsxs("div", { className: "flex items-center gap-2", children: [_jsx("label", { className: "text-xs text-gray-500 w-24 flex-shrink-0", children: "Port" }), _jsx("input", { value: f.port ?? "", onChange: (e) => set("port", e.target.value), className: inputCls, placeholder: "/dev/ttyACM0" })] }), _jsxs("div", { className: "grid grid-cols-2 gap-2", children: [_jsxs("div", { children: [_jsx("label", { className: "text-xs text-gray-500 block mb-1", children: "Region" }), _jsx("select", { value: region.label, onChange: (e) => applyRegion(REGIONS.find((r) => r.label === e.target.value)), className: selectCls, children: REGIONS.map((r) => _jsx("option", { children: r.label }, r.label)) })] }), _jsxs("div", { children: [_jsx("label", { className: "text-xs text-gray-500 block mb-1", children: "Modem preset" }), _jsxs("select", { value: modemPreset, onChange: (e) => applyModemPreset(e.target.value), className: selectCls, children: [MODEM_PRESETS.map((p) => _jsx("option", { children: p.label }, p.label)), _jsx("option", { children: "Custom" })] })] })] }), _jsxs("div", { className: "grid grid-cols-2 gap-2", children: [_jsxs("div", { children: [_jsx("label", { className: "text-xs text-gray-500 block mb-1", children: "Frequency (Hz)" }), _jsx("input", { type: "number", value: f.frequency ?? "", min: region.min, max: region.max, onChange: (e) => { setModemPreset("Custom"); set("frequency", e.target.value); }, className: inputCls }), _jsxs("p", { className: "text-xs text-gray-400 mt-0.5", children: [(region.min / 1e6).toFixed(0), "\u2013", (region.max / 1e6).toFixed(0), " MHz"] })] }), _jsxs("div", { children: [_jsx("label", { className: "text-xs text-gray-500 block mb-1", children: "TX power (dBm)" }), _jsx("input", { type: "number", value: f.txpower ?? "", min: -9, max: 22, onChange: (e) => set("txpower", e.target.value), className: inputCls })] }), _jsxs("div", { children: [_jsx("label", { className: "text-xs text-gray-500 block mb-1", children: "Spreading factor" }), _jsx("select", { value: f.spreadingfactor ?? "11", onChange: (e) => { setModemPreset("Custom"); set("spreadingfactor", e.target.value); }, className: selectCls, children: [5, 6, 7, 8, 9, 10, 11, 12].map((v) => _jsx("option", { children: v }, v)) })] }), _jsxs("div", { children: [_jsx("label", { className: "text-xs text-gray-500 block mb-1", children: "Bandwidth (Hz)" }), _jsx("select", { value: f.bandwidth ?? "250000", onChange: (e) => { setModemPreset("Custom"); set("bandwidth", e.target.value); }, className: selectCls, children: BANDWIDTHS.map((v) => _jsxs("option", { value: v, children: [(v / 1000).toFixed(v < 10000 ? 1 : 0), " kHz"] }, v)) })] }), _jsxs("div", { children: [_jsx("label", { className: "text-xs text-gray-500 block mb-1", children: "Coding rate" }), _jsx("select", { value: f.codingrate ?? "5", onChange: (e) => { setModemPreset("Custom"); set("codingrate", e.target.value); }, className: selectCls, children: [5, 6, 7, 8].map((v) => _jsxs("option", { value: v, children: ["4/", v] }, v)) })] }), _jsxs("div", { children: [_jsx("label", { className: "text-xs text-gray-500 block mb-1", children: "Callsign" }), _jsx("input", { value: f.id_callsign ?? "", onChange: (e) => set("id_callsign", e.target.value), className: inputCls, placeholder: "NOCALL" })] }), _jsxs("div", { children: [_jsx("label", { className: "text-xs text-gray-500 block mb-1", children: "ID interval (s)" }), _jsx("input", { type: "number", value: f.id_interval ?? "", min: 0, onChange: (e) => set("id_interval", e.target.value), className: inputCls })] }), _jsxs("div", { children: [_jsx("label", { className: "text-xs text-gray-500 block mb-1", children: "Airtime limit long (%)" }), _jsx("input", { type: "number", value: f.airtime_limit_long ?? "", min: 0, max: 100, onChange: (e) => set("airtime_limit_long", e.target.value), className: inputCls })] }), _jsxs("div", { children: [_jsx("label", { className: "text-xs text-gray-500 block mb-1", children: "Airtime limit short (%)" }), _jsx("input", { type: "number", value: f.airtime_limit_short ?? "", min: 0, max: 100, onChange: (e) => set("airtime_limit_short", e.target.value), className: inputCls })] }), _jsxs("div", { className: "flex items-center gap-2 col-span-2", children: [_jsx("label", { className: "text-xs text-gray-500", children: "Flow control" }), _jsx("input", { type: "checkbox", checked: getBool(f.flow_control), onChange: (e) => set("flow_control", setBool(e.target.checked)), className: "accent-blue-600" })] })] }), _jsxs("button", { onClick: () => setShowLocation((v) => !v), className: "text-xs text-blue-600 hover:underline", children: [showLocation ? "▾" : "▸", " Location"] }), showLocation && (_jsxs("div", { className: "grid grid-cols-3 gap-2", children: [_jsxs("div", { children: [_jsx("label", { className: "text-xs text-gray-500 block mb-1", children: "Latitude" }), _jsx("input", { type: "number", value: f.latitude ?? "", min: -90, max: 90, step: "any", onChange: (e) => set("latitude", e.target.value), className: inputCls })] }), _jsxs("div", { children: [_jsx("label", { className: "text-xs text-gray-500 block mb-1", children: "Longitude" }), _jsx("input", { type: "number", value: f.longitude ?? "", min: -180, max: 180, step: "any", onChange: (e) => set("longitude", e.target.value), className: inputCls })] }), _jsxs("div", { children: [_jsx("label", { className: "text-xs text-gray-500 block mb-1", children: "Height (m)" }), _jsx("input", { type: "number", value: f.height ?? "", step: "any", onChange: (e) => set("height", e.target.value), className: inputCls })] }), _jsxs("div", { className: "flex items-center gap-2 col-span-3", children: [_jsx("label", { className: "text-xs text-gray-500", children: "Discoverable" }), _jsx("input", { type: "checkbox", checked: getBool(f.discoverable), onChange: (e) => set("discoverable", setBool(e.target.checked)), className: "accent-blue-600" }), getBool(f.discoverable) && (_jsx("input", { value: f.discovery_name ?? "", onChange: (e) => set("discovery_name", e.target.value), className: `${inputCls} ml-2`, placeholder: "Discovery name" }))] })] })), _jsxs("button", { onClick: () => setShowAdvanced((v) => !v), className: "text-xs text-blue-600 hover:underline", children: [showAdvanced ? "▾" : "▸", " Advanced"] }), showAdvanced && (_jsxs("div", { className: "grid grid-cols-2 gap-2", children: [_jsxs("div", { children: [_jsx("label", { className: "text-xs text-gray-500 block mb-1", children: "Mode" }), _jsx("select", { value: f.mode ?? "full", onChange: (e) => set("mode", e.target.value), className: selectCls, children: ["full", "gateway", "access_point", "roaming", "boundary"].map((v) => _jsx("option", { children: v }, v)) })] }), _jsxs("div", { children: [_jsx("label", { className: "text-xs text-gray-500 block mb-1", children: "Network name" }), _jsx("input", { value: f.network_name ?? "", onChange: (e) => set("network_name", e.target.value), className: inputCls })] }), _jsxs("div", { children: [_jsx("label", { className: "text-xs text-gray-500 block mb-1", children: "Passphrase" }), _jsx("input", { type: "password", value: f.passphrase ?? "", onChange: (e) => set("passphrase", e.target.value), className: inputCls })] }), _jsxs("div", { children: [_jsx("label", { className: "text-xs text-gray-500 block mb-1", children: "Announce cap (%)" }), _jsx("input", { type: "number", value: f.announce_cap ?? "", min: 1, max: 100, onChange: (e) => set("announce_cap", e.target.value), className: inputCls })] }), _jsxs("div", { className: "flex items-center gap-2 col-span-2", children: [_jsx("label", { className: "text-xs text-gray-500", children: "Outgoing" }), _jsx("input", { type: "checkbox", checked: getBool(f.outgoing ?? "yes"), onChange: (e) => set("outgoing", setBool(e.target.checked)), className: "accent-blue-600" })] })] }))] }));
}
// ---------------------------------------------------------------------------
// TCP/UDP interface cards
// ---------------------------------------------------------------------------
function TcpClientCard({ iface, onChange }) {
    const f = iface.fields;
    const set = (k, v) => onChange({ ...f, [k]: v });
    const [showAdvanced, setShowAdvanced] = useState(false);
    return (_jsxs("div", { className: "rounded-lg border border-gray-200 p-4 space-y-3", children: [_jsxs("h4", { className: "font-medium text-gray-800 text-sm", children: [iface.name, " ", _jsx("span", { className: "text-gray-400 font-normal", children: "TCPClientInterface" })] }), _jsxs("div", { className: "flex items-center gap-2", children: [_jsx("label", { className: "text-xs text-gray-500 w-24", children: "Enabled" }), _jsx("input", { type: "checkbox", checked: getBool(f.enabled), onChange: (e) => set("enabled", setBool(e.target.checked)), className: "accent-blue-600" })] }), _jsxs("div", { className: "grid grid-cols-2 gap-2", children: [_jsxs("div", { children: [_jsx("label", { className: "text-xs text-gray-500 block mb-1", children: "Host" }), _jsx("input", { value: f.target_host ?? "", onChange: (e) => set("target_host", e.target.value), className: inputCls })] }), _jsxs("div", { children: [_jsx("label", { className: "text-xs text-gray-500 block mb-1", children: "Port" }), _jsx("input", { type: "number", value: f.target_port ?? "", min: 1, max: 65535, onChange: (e) => set("target_port", e.target.value), className: inputCls })] })] }), _jsxs("button", { onClick: () => setShowAdvanced((v) => !v), className: "text-xs text-blue-600 hover:underline", children: [showAdvanced ? "▾" : "▸", " Advanced"] }), showAdvanced && (_jsxs("div", { className: "grid grid-cols-2 gap-2", children: [_jsxs("div", { children: [_jsx("label", { className: "text-xs text-gray-500 block mb-1", children: "Mode" }), _jsx("select", { value: f.mode ?? "full", onChange: (e) => set("mode", e.target.value), className: selectCls, children: ["full", "gateway", "access_point", "roaming", "boundary"].map((v) => _jsx("option", { children: v }, v)) })] }), _jsxs("div", { children: [_jsx("label", { className: "text-xs text-gray-500 block mb-1", children: "Network name" }), _jsx("input", { value: f.network_name ?? "", onChange: (e) => set("network_name", e.target.value), className: inputCls })] }), _jsxs("div", { children: [_jsx("label", { className: "text-xs text-gray-500 block mb-1", children: "Passphrase" }), _jsx("input", { type: "password", value: f.passphrase ?? "", onChange: (e) => set("passphrase", e.target.value), className: inputCls })] })] }))] }));
}
function UdpCard({ iface, onChange }) {
    const f = iface.fields;
    const set = (k, v) => onChange({ ...f, [k]: v });
    const [showAdvanced, setShowAdvanced] = useState(false);
    return (_jsxs("div", { className: "rounded-lg border border-gray-200 p-4 space-y-3", children: [_jsxs("h4", { className: "font-medium text-gray-800 text-sm", children: [iface.name, " ", _jsx("span", { className: "text-gray-400 font-normal", children: "UDPInterface" })] }), _jsxs("div", { className: "flex items-center gap-2", children: [_jsx("label", { className: "text-xs text-gray-500 w-24", children: "Enabled" }), _jsx("input", { type: "checkbox", checked: getBool(f.enabled), onChange: (e) => set("enabled", setBool(e.target.checked)), className: "accent-blue-600" })] }), _jsxs("div", { className: "grid grid-cols-2 gap-2", children: [_jsxs("div", { children: [_jsx("label", { className: "text-xs text-gray-500 block mb-1", children: "Listen IP" }), _jsx("input", { value: f.listen_ip ?? "", onChange: (e) => set("listen_ip", e.target.value), className: inputCls })] }), _jsxs("div", { children: [_jsx("label", { className: "text-xs text-gray-500 block mb-1", children: "Listen port" }), _jsx("input", { type: "number", value: f.listen_port ?? "", min: 1, max: 65535, onChange: (e) => set("listen_port", e.target.value), className: inputCls })] }), _jsxs("div", { children: [_jsx("label", { className: "text-xs text-gray-500 block mb-1", children: "Forward IP" }), _jsx("input", { value: f.forward_ip ?? "", onChange: (e) => set("forward_ip", e.target.value), className: inputCls })] }), _jsxs("div", { children: [_jsx("label", { className: "text-xs text-gray-500 block mb-1", children: "Forward port" }), _jsx("input", { type: "number", value: f.forward_port ?? "", min: 1, max: 65535, onChange: (e) => set("forward_port", e.target.value), className: inputCls })] })] }), _jsxs("button", { onClick: () => setShowAdvanced((v) => !v), className: "text-xs text-blue-600 hover:underline", children: [showAdvanced ? "▾" : "▸", " Advanced"] }), showAdvanced && (_jsxs("div", { className: "grid grid-cols-2 gap-2", children: [_jsxs("div", { children: [_jsx("label", { className: "text-xs text-gray-500 block mb-1", children: "Mode" }), _jsx("select", { value: f.mode ?? "full", onChange: (e) => set("mode", e.target.value), className: selectCls, children: ["full", "gateway", "access_point", "roaming", "boundary"].map((v) => _jsx("option", { children: v }, v)) })] }), _jsxs("div", { children: [_jsx("label", { className: "text-xs text-gray-500 block mb-1", children: "Network name" }), _jsx("input", { value: f.network_name ?? "", onChange: (e) => set("network_name", e.target.value), className: inputCls })] })] }))] }));
}
function UnknownCard({ iface }) {
    return (_jsxs("div", { className: "rounded-lg border border-gray-200 p-4 space-y-1", children: [_jsxs("h4", { className: "font-medium text-gray-800 text-sm", children: [iface.name, " ", _jsx("span", { className: "text-gray-400 font-normal", children: iface.fields.type ?? "unknown type" })] }), Object.entries(iface.fields).map(([k, v]) => (_jsxs("div", { className: "flex justify-between text-xs font-mono text-gray-600 border-b border-gray-100 py-0.5", children: [_jsx("span", { className: "text-gray-400", children: k }), _jsx("span", { children: v })] }, k)))] }));
}
// ---------------------------------------------------------------------------
// RNS Config tab
// ---------------------------------------------------------------------------
function RnsConfigTab({ destHash, onLatLon }) {
    const [rnsConfig, setRnsConfig] = useState(null);
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
            let content;
            if (!forceRefresh) {
                try {
                    const snap = await api.config.snapshot(destHash, "rns");
                    content = snap.content;
                }
                catch {
                    const pulled = await api.config.pull(destHash, "rns");
                    content = pulled.content;
                }
            }
            else {
                setStatus("Pulling from node…");
                const pulled = await api.config.pull(destHash, "rns");
                content = pulled.content;
                setStatus("Pulled from node");
            }
            setRnsConfig(parseIni(content));
        }
        catch (e) {
            if (e.message.startsWith("no_path:")) {
                setNoPath(true);
            }
            else {
                setStatus(`Error: ${e.message}`);
            }
        }
        finally {
            setLoading(false);
        }
    }
    function validate(cfg) {
        const errors = [];
        for (const iface of cfg.interfaces) {
            const f = iface.fields;
            if (f.type === "RNodeInterface") {
                const freq = parseInt(f.frequency ?? "0", 10);
                const region = detectRegion(freq);
                if (freq < region.min || freq > region.max)
                    errors.push(`${iface.name}: frequency ${freq} out of range for ${region.label}`);
                const tx = parseInt(f.txpower ?? "0", 10);
                if (tx < -9 || tx > 22)
                    errors.push(`${iface.name}: txpower ${tx} out of range (−9–22)`);
                const sf = parseInt(f.spreadingfactor ?? "0", 10);
                if (sf < 5 || sf > 12)
                    errors.push(`${iface.name}: spreadingfactor must be 5–12`);
                const lat = parseFloat(f.latitude ?? "0");
                const lon = parseFloat(f.longitude ?? "0");
                if (f.latitude && (lat < -90 || lat > 90))
                    errors.push(`${iface.name}: latitude out of range`);
                if (f.longitude && (lon < -180 || lon > 180))
                    errors.push(`${iface.name}: longitude out of range`);
            }
        }
        return errors;
    }
    async function save() {
        if (!rnsConfig)
            return;
        const errors = validate(rnsConfig);
        if (errors.length) {
            setStatus(errors.join("; "));
            return;
        }
        setStatus("Saving…");
        try {
            const content = serializeIni(rnsConfig);
            const r = await api.config.put(destHash, "rns", content);
            setStatus(r.status === "pending_commit" ? "Saved — awaiting commit confirmation" : "Saved ✓");
        }
        catch (e) {
            setStatus(`Error: ${e.message}`);
        }
    }
    function updateIface(idx, fields) {
        if (!rnsConfig)
            return;
        const interfaces = rnsConfig.interfaces.map((iface, i) => i === idx ? { ...iface, fields } : iface);
        setRnsConfig({ ...rnsConfig, interfaces });
    }
    function setReticulumField(k, v) {
        if (!rnsConfig)
            return;
        setRnsConfig({ ...rnsConfig, reticulum: { ...rnsConfig.reticulum, [k]: v } });
    }
    function setLoggingField(k, v) {
        if (!rnsConfig)
            return;
        setRnsConfig({ ...rnsConfig, logging: { ...rnsConfig.logging, [k]: v } });
    }
    // Collect location from first RNode with lat/lon
    const locationIface = rnsConfig?.interfaces.find((i) => i.fields.type === "RNodeInterface" && i.fields.latitude && i.fields.longitude);
    const lat = locationIface ? parseFloat(locationIface.fields.latitude) : null;
    const lon = locationIface ? parseFloat(locationIface.fields.longitude) : null;
    useEffect(() => { onLatLon?.(lat, lon); }, [lat, lon]);
    if (loading)
        return _jsx("p", { className: "text-sm text-gray-400 p-4", children: "Loading\u2026" });
    if (noPath)
        return (_jsxs("div", { className: "rounded-lg border border-amber-200 bg-amber-50 p-4 space-y-2", children: [_jsx("p", { className: "text-sm text-amber-800 font-medium", children: "No path to node" }), _jsx("p", { className: "text-xs text-amber-700", children: "The node may be offline or has not announced yet. If it just came online, wait a moment for its announce to propagate." }), _jsx("button", { onClick: () => { setLoading(true); loadConfig(true); }, className: "text-xs px-3 py-1.5 rounded border border-amber-300 text-amber-800 hover:bg-amber-100", children: "Retry" })] }));
    return (_jsxs("div", { className: "space-y-4", children: [rnsConfig && (_jsxs(_Fragment, { children: [_jsxs("div", { className: "rounded-lg border border-gray-200 p-4 space-y-2", children: [_jsx("h4", { className: "font-medium text-gray-700 text-sm", children: "[reticulum]" }), [
                                { k: "enable_transport", label: "Enable transport" },
                                { k: "share_instance", label: "Share instance" },
                                { k: "use_implicit_proof", label: "Use implicit proof" },
                                { k: "panic_on_interface_error", label: "Panic on interface error" },
                            ].map(({ k, label }) => (_jsxs("div", { className: "flex items-center gap-2", children: [_jsx("label", { className: "text-xs text-gray-500 w-44", children: label }), _jsx("input", { type: "checkbox", checked: getBool(rnsConfig.reticulum[k]), onChange: (e) => setReticulumField(k, setBool(e.target.checked)), className: "accent-blue-600" })] }, k))), _jsxs("div", { className: "flex items-center gap-2", children: [_jsx("label", { className: "text-xs text-gray-500 w-44", children: "Shared instance expiry" }), _jsx("input", { type: "number", value: rnsConfig.reticulum.shared_instance_expiry ?? "", onChange: (e) => setReticulumField("shared_instance_expiry", e.target.value), className: `${inputCls} w-28` })] })] }), _jsxs("div", { className: "rounded-lg border border-gray-200 p-4 space-y-2", children: [_jsx("h4", { className: "font-medium text-gray-700 text-sm", children: "[logging]" }), _jsxs("div", { className: "flex items-center gap-2", children: [_jsx("label", { className: "text-xs text-gray-500 w-24", children: "Log level" }), _jsx("select", { value: rnsConfig.logging.loglevel ?? "4", onChange: (e) => setLoggingField("loglevel", e.target.value), className: `${selectCls} w-48`, children: Object.entries(LOG_LEVELS).map(([v, l]) => _jsxs("option", { value: v, children: [v, " \u2014 ", l] }, v)) })] })] }), rnsConfig.interfaces.map((iface, idx) => {
                        const type = iface.fields.type ?? "";
                        if (type === "RNodeInterface")
                            return _jsx(RNodeCard, { iface: iface, onChange: (f) => updateIface(idx, f) }, iface.name);
                        if (type === "TCPClientInterface")
                            return _jsx(TcpClientCard, { iface: iface, onChange: (f) => updateIface(idx, f) }, iface.name);
                        if (type === "UDPInterface")
                            return _jsx(UdpCard, { iface: iface, onChange: (f) => updateIface(idx, f) }, iface.name);
                        return _jsx(UnknownCard, { iface: iface }, iface.name);
                    })] })), status && _jsx("p", { className: `text-xs ${status.startsWith("Error") ? "text-red-600" : "text-gray-500"}`, children: status }), _jsxs("div", { className: "flex gap-2 pt-1", children: [_jsx("button", { onClick: () => loadConfig(true), className: "px-3 py-1.5 rounded border border-gray-200 text-xs text-gray-700 hover:bg-gray-50", children: "Refresh from node" }), _jsx("button", { onClick: save, className: "px-3 py-1.5 rounded bg-blue-600 text-white text-xs hover:bg-blue-700 ml-auto", children: "Save" })] })] }));
}
// ---------------------------------------------------------------------------
// Agent Config tab
// ---------------------------------------------------------------------------
function AgentConfigTab({ destHash }) {
    const [cfg, setCfg] = useState(null);
    const [status, setStatus] = useState("");
    const [noPath, setNoPath] = useState(false);
    const [loading, setLoading] = useState(true);
    useEffect(() => { setLoading(true); loadConfig(); }, [destHash]);
    async function loadConfig(forceRefresh = false) {
        setStatus("");
        setNoPath(false);
        try {
            let content;
            if (!forceRefresh) {
                try {
                    const snap = await api.config.snapshot(destHash, "agent");
                    content = snap.content;
                }
                catch {
                    const pulled = await api.config.pull(destHash, "agent");
                    content = pulled.content;
                }
            }
            else {
                setStatus("Pulling from node…");
                const pulled = await api.config.pull(destHash, "agent");
                content = pulled.content;
                setStatus("Pulled from node");
            }
            setCfg(JSON.parse(content));
        }
        catch (e) {
            if (e.message.startsWith("no_path:")) {
                setNoPath(true);
            }
            else {
                setStatus(`Error: ${e.message}`);
            }
        }
        finally {
            setLoading(false);
        }
    }
    function set(k, v) { setCfg((c) => ({ ...c, [k]: v })); }
    function setListItem(k, idx, v) {
        const arr = [...(cfg[k] ?? [])];
        arr[idx] = v;
        set(k, arr);
    }
    function addListItem(k) { set(k, [...(cfg[k] ?? []), ""]); }
    function removeListItem(k, idx) { set(k, (cfg[k] ?? []).filter((_, i) => i !== idx)); }
    function validate() {
        if (!cfg)
            return ["No config loaded"];
        const errs = [];
        if ((cfg.announce_interval ?? 0) < 30)
            errs.push("Announce interval must be ≥ 30s");
        if ((cfg.shutdown_soc_pct ?? 0) < 0 || (cfg.shutdown_soc_pct ?? 0) > 100)
            errs.push("Shutdown SoC must be 0–100");
        return errs;
    }
    async function save() {
        if (!cfg)
            return;
        const errs = validate();
        if (errs.length) {
            setStatus(errs.join("; "));
            return;
        }
        setStatus("Saving…");
        try {
            const r = await api.config.put(destHash, "agent", JSON.stringify(cfg, null, 2));
            setStatus(r.status === "pending_commit" ? "Saved — awaiting commit" : "Saved ✓");
        }
        catch (e) {
            setStatus(`Error: ${e.message}`);
        }
    }
    if (loading)
        return _jsx("p", { className: "text-sm text-gray-400 p-4", children: "Loading\u2026" });
    if (noPath)
        return (_jsxs("div", { className: "rounded-lg border border-amber-200 bg-amber-50 p-4 space-y-2", children: [_jsx("p", { className: "text-sm text-amber-800 font-medium", children: "No path to node" }), _jsx("p", { className: "text-xs text-amber-700", children: "The node may be offline or has not announced yet. If it just came online, wait a moment for its announce to propagate." }), _jsx("button", { onClick: () => { setLoading(true); loadConfig(true); }, className: "text-xs px-3 py-1.5 rounded border border-amber-300 text-amber-800 hover:bg-amber-100", children: "Retry" })] }));
    if (!cfg)
        return _jsxs("p", { className: "text-sm text-gray-400 p-4", children: ["No config. ", _jsx("button", { onClick: () => loadConfig(true), className: "text-blue-600 underline", children: "Pull from node" })] });
    const ListField = ({ k, label }) => (_jsxs("div", { className: "space-y-1", children: [_jsx("label", { className: "text-xs text-gray-500", children: label }), (cfg[k] ?? []).map((v, i) => (_jsxs("div", { className: "flex gap-1", children: [_jsx("input", { value: v, onChange: (e) => setListItem(k, i, e.target.value), className: `${inputCls} flex-1` }), _jsx("button", { onClick: () => removeListItem(k, i), className: "text-red-500 text-xs px-1 hover:text-red-700", children: "\u2715" })] }, i))), _jsx("button", { onClick: () => addListItem(k), className: "text-xs text-blue-600 hover:underline", children: "+ Add" })] }));
    return (_jsxs("div", { className: "space-y-3", children: [_jsx("div", { className: "grid grid-cols-2 gap-3", children: [
                    { k: "announce_interval", label: "Announce interval (s)", min: 30 },
                    { k: "shutdown_soc_pct", label: "Shutdown battery % (0=off)", min: 0, max: 100 },
                    { k: "watchdog_feed_interval_s", label: "Watchdog feed interval (s)", min: 1 },
                    { k: "zero_traffic_minutes", label: "Zero traffic timeout (min)", min: 1 },
                    { k: "time_sync_interval", label: "Time sync interval (s)", min: 60 },
                ].map(({ k, label, min, max }) => (_jsxs("div", { children: [_jsx("label", { className: "text-xs text-gray-500 block mb-1", children: label }), _jsx("input", { type: "number", value: cfg[k] ?? "", min: min, max: max, onChange: (e) => set(k, Number(e.target.value)), className: inputCls })] }, k))) }), _jsx(ListField, { k: "server_dest_hashes", label: "Server destination hashes" }), _jsx(ListField, { k: "rnode_ports", label: "RNode ports" }), status && _jsx("p", { className: `text-xs ${status.startsWith("Error") ? "text-red-600" : "text-gray-500"}`, children: status }), _jsxs("div", { className: "flex gap-2 pt-1", children: [_jsx("button", { onClick: () => loadConfig(true), className: "px-3 py-1.5 rounded border border-gray-200 text-xs text-gray-700 hover:bg-gray-50", children: "Refresh from node" }), _jsx("button", { onClick: save, className: "px-3 py-1.5 rounded bg-blue-600 text-white text-xs hover:bg-blue-700 ml-auto", children: "Save" })] })] }));
}
// ---------------------------------------------------------------------------
// Commands section
// ---------------------------------------------------------------------------
function CommandsSection({ destHash }) {
    const [cmd, setCmd] = useState("svc_restart");
    const [params, setParams] = useState({ service: "rnsd" });
    const [output, setOutput] = useState("");
    function handleCmdChange(newCmd) {
        setCmd(newCmd);
        setOutput("");
        const defaults = {
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
    function setParam(k, v) { setParams((p) => ({ ...p, [k]: v })); }
    async function execute() {
        setOutput("Sending…");
        try {
            const r = await api.nodes.command(destHash, { cmd, ...params });
            setOutput(r.output ?? (r.ok ? "OK" : r.error ?? "Failed"));
        }
        catch (e) {
            setOutput(`Error: ${e.message}`);
        }
    }
    const P = ({ label, children }) => (_jsxs("div", { className: "flex items-center gap-2", children: [_jsx("label", { className: "text-xs text-gray-500 w-28 flex-shrink-0", children: label }), children] }));
    return (_jsxs("div", { className: "space-y-3", children: [_jsxs("div", { children: [_jsx("label", { className: "text-xs text-gray-500 block mb-1", children: "Command" }), _jsx("select", { value: cmd, onChange: (e) => handleCmdChange(e.target.value), className: `${selectCls} w-56`, children: COMMANDS.map((c) => _jsx("option", { value: c.value, children: c.label }, c.value)) })] }), ["svc_restart", "svc_stop", "svc_start"].includes(cmd) && (_jsx(P, { label: "Service", children: _jsx("input", { value: params.service ?? "", onChange: (e) => setParam("service", e.target.value), className: `${inputCls} w-40` }) })), cmd === "wifi_set" && (_jsx(P, { label: "Enable", children: _jsxs("select", { value: String(params.enabled), onChange: (e) => setParam("enabled", e.target.value === "true"), className: `${selectCls} w-24`, children: [_jsx("option", { value: "true", children: "On" }), _jsx("option", { value: "false", children: "Off" })] }) })), cmd === "log_pull" && (_jsxs(_Fragment, { children: [_jsx(P, { label: "Lines", children: _jsx("input", { type: "number", value: params.lines ?? 50, min: 1, max: 1000, onChange: (e) => setParam("lines", Number(e.target.value)), className: `${inputCls} w-24` }) }), _jsx(P, { label: "Unit (optional)", children: _jsx("input", { value: params.unit ?? "", onChange: (e) => setParam("unit", e.target.value || undefined), className: `${inputCls} w-40`, placeholder: "bloxx-agent" }) })] })), ["reboot", "shutdown"].includes(cmd) && (_jsx(P, { label: "Delay (s)", children: _jsx("input", { type: "number", value: params.delay_s ?? 5, min: 0, onChange: (e) => setParam("delay_s", Number(e.target.value)), className: `${inputCls} w-24` }) })), cmd === "shutdown_threshold" && (_jsx(P, { label: "Battery SoC %", children: _jsx("input", { type: "number", value: params.soc_pct ?? 20, min: 0, max: 100, onChange: (e) => setParam("soc_pct", Number(e.target.value)), className: `${inputCls} w-24` }) })), cmd === "connectivity_check" && (_jsx(P, { label: "Dest hash", children: _jsx("input", { value: params.dest_hash ?? "", onChange: (e) => setParam("dest_hash", e.target.value), className: `${inputCls} w-64` }) })), ["rnode_reset", "rnode_update"].includes(cmd) && (_jsx(P, { label: "Port", children: _jsx("input", { value: params.port ?? "", onChange: (e) => setParam("port", e.target.value), className: `${inputCls} w-40`, placeholder: "/dev/ttyACM0" }) })), _jsx("button", { onClick: execute, className: "px-4 py-1.5 rounded bg-gray-800 text-white text-xs hover:bg-gray-700", children: "Execute" }), output && (_jsx("pre", { className: "rounded-lg bg-gray-900 text-green-300 text-xs p-3 overflow-auto max-h-48 whitespace-pre-wrap", children: output }))] }));
}
export default function NodePanel({ destHash, node, onDelete, liveTelemetry }) {
    const [telemetry, setTelemetry] = useState([]);
    const [tab, setTab] = useState("rns");
    const [labelEdit, setLabelEdit] = useState(null);
    const [labelSaving, setLabelSaving] = useState(false);
    const [latLon, setLatLon] = useState(null);
    useEffect(() => {
        api.nodes.telemetry(destHash, 60).then(setTelemetry).catch(() => { });
    }, [destHash]);
    // Prepend live WS telemetry to sparkline data
    useEffect(() => {
        if (!liveTelemetry)
            return;
        const row = liveTelemetry;
        setTelemetry((prev) => [row, ...prev].slice(0, 60));
    }, [liveTelemetry]);
    async function handleDelete() {
        if (!window.confirm("Delete this node and all its telemetry? This cannot be undone."))
            return;
        await api.nodes.delete(destHash);
        onDelete();
    }
    async function saveLabel() {
        if (labelEdit === null)
            return;
        setLabelSaving(true);
        try {
            await api.nodes.patch(destHash, labelEdit.trim() || null);
        }
        catch { /* ignore */ }
        finally {
            setLabelSaving(false);
            setLabelEdit(null);
        }
    }
    const spark = (field, label, unit, color, min, max) => {
        const data = [...telemetry].reverse().map((r) => r[field]);
        const latest = telemetry[0]?.[field] ?? null;
        if (data.every((v) => v == null))
            return null;
        return _jsx(SparkLine, { data: data, label: label, unit: unit, latest: latest, color: color, min: min, max: max }, field);
    };
    const dotColor = !node.online ? "text-red-500" : node.last_errors.length ? "text-amber-400" : "text-green-500";
    const displayName = node.label ?? node.hostname ?? "Unknown";
    return (_jsxs("div", { className: "p-5 space-y-5", children: [_jsxs("div", { className: "flex items-center gap-3 flex-wrap", children: [labelEdit === null ? (_jsx("h2", { className: "text-xl font-bold text-gray-900 cursor-pointer hover:text-blue-600", title: "Click to rename", onClick: () => setLabelEdit(node.label ?? ""), children: displayName })) : (_jsxs("div", { className: "flex items-center gap-1", children: [_jsx("input", { autoFocus: true, value: labelEdit, onChange: (e) => setLabelEdit(e.target.value), onKeyDown: (e) => { if (e.key === "Enter")
                                    saveLabel(); if (e.key === "Escape")
                                    setLabelEdit(null); }, className: "text-xl font-bold rounded border border-blue-300 px-1 focus:outline-none focus:ring-2 focus:ring-blue-300 w-48", placeholder: node.hostname ?? "Label" }), _jsx("button", { onClick: saveLabel, disabled: labelSaving, className: "text-xs text-blue-600 px-2 py-1 hover:underline disabled:opacity-50", children: "Save" }), _jsx("button", { onClick: () => setLabelEdit(null), className: "text-xs text-gray-400 px-1 hover:text-gray-700", children: "\u2715" })] })), node.label && node.hostname && node.label !== node.hostname && (_jsx("span", { className: "text-sm text-gray-400 font-mono", children: node.hostname })), _jsxs("span", { className: `text-xs font-medium ${dotColor}`, children: ["\u25CF ", node.online ? "online" : "offline"] }), node.last_errors.length > 0 && (_jsx("div", { className: "flex gap-1 flex-wrap", children: node.last_errors.map((e) => (_jsx("span", { className: "rounded-full bg-red-100 px-2 py-0.5 text-xs text-red-700 font-mono", children: e }, e))) })), _jsx("button", { onClick: handleDelete, className: "ml-auto text-xs text-red-600 border border-red-200 rounded px-2 py-1 hover:bg-red-50", children: "Delete" })] }), _jsxs("div", { className: "rounded-xl border border-gray-200 bg-white p-4 shadow-sm", children: [_jsx(Row, { label: "Destination hash", value: node.dest_hash }), _jsx(Row, { label: "Identity hash", value: node.identity_hash }), _jsx(Row, { label: "Version", value: node.version }), _jsx(Row, { label: "First seen", value: fmt(node.first_seen) }), _jsx(Row, { label: "Last seen", value: fmt(node.last_seen) })] }), telemetry.length > 0 && (() => {
                const newestTs = telemetry[0]?.ts;
                const oldestTs = telemetry[telemetry.length - 1]?.ts;
                const windowSec = newestTs && oldestTs ? newestTs - oldestTs : null;
                const windowLabel = windowSec
                    ? windowSec >= 3600
                        ? `${(windowSec / 3600).toFixed(1)}h window`
                        : `${Math.round(windowSec / 60)}m window`
                    : null;
                return (_jsxs("div", { className: "rounded-xl border border-gray-200 bg-white p-4 shadow-sm space-y-4", children: [windowLabel && (_jsxs("p", { className: "text-xs text-gray-400 -mb-2", children: [windowLabel, " \u00B7 ", telemetry.length, " samples"] })), _jsxs("div", { className: "flex gap-4 items-start", children: [_jsxs("div", { className: "flex-1 space-y-4", children: [_jsxs("div", { className: "flex flex-wrap gap-6", children: [spark("cpu_pct", "CPU", "%", "#3b82f6", 0, 100), spark("ram_pct", "RAM", "%", "#8b5cf6", 0, 100), spark("disk_pct", "Disk", "%", "#f59e0b", 0, 100), spark("temp_c", "Temp", "°C", "#ef4444"), spark("rns_rtt_ms", "RTT", "ms", "#64748b"), spark("batt_soc_pct", "Battery", "%", "#22c55e", 0, 100), spark("batt_power_w", "Bat power", "W", "#16a34a"), spark("solar_power_w", "Solar", "W", "#eab308")] }), (() => {
                                            const rnodeSparks = [
                                                spark("rnode_airtime_short", "Airtime (short)", "%", "#06b6d4", 0, 100),
                                                spark("rnode_airtime_long", "Airtime (long)", "%", "#0891b2", 0, 100),
                                                spark("rnode_channel_load_short", "Ch load", "%", "#7c3aed", 0, 100),
                                                spark("rnode_noise_floor", "Noise floor", "dBm", "#94a3b8"),
                                                spark("rnode_interference_dbm", "Interference", "dBm", "#f43f5e"),
                                                spark("rnode_bitrate", "Bitrate", "bps", "#10b981"),
                                            ].filter(Boolean);
                                            if (!rnodeSparks.length)
                                                return null;
                                            return (_jsxs("div", { children: [_jsx("p", { className: "text-xs text-gray-400 mb-3", children: "RNode" }), _jsx("div", { className: "flex flex-wrap gap-6", children: rnodeSparks })] }));
                                        })()] }), latLon && !isNaN(latLon.lat) && !isNaN(latLon.lon) && (_jsx(LocationMap, { lat: latLon.lat, lon: latLon.lon }))] })] }));
            })(), _jsxs("div", { className: "rounded-xl border border-gray-200 bg-white shadow-sm", children: [_jsx("div", { className: "flex border-b border-gray-100", children: ["rns", "agent"].map((t) => (_jsx("button", { onClick: () => setTab(t), className: `px-4 py-2.5 text-sm font-medium border-b-2 -mb-px transition-colors ${tab === t ? "border-blue-600 text-blue-600" : "border-transparent text-gray-500 hover:text-gray-700"}`, children: t === "rns" ? "RNS Config" : "Agent Config" }, t))) }), _jsx("div", { className: "p-4", children: tab === "rns" ? _jsx(RnsConfigTab, { destHash: destHash, onLatLon: (lat, lon) => setLatLon(lat != null && lon != null ? { lat, lon } : null) }) : _jsx(AgentConfigTab, { destHash: destHash }) })] }), _jsxs("div", { className: "rounded-xl border border-gray-200 bg-white p-4 shadow-sm", children: [_jsx("h3", { className: "text-sm font-semibold text-gray-700 mb-3", children: "Commands" }), _jsx(CommandsSection, { destHash: destHash })] })] }));
}
