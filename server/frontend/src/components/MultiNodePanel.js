import { jsx as _jsx, jsxs as _jsxs } from "react/jsx-runtime";
import { useState } from "react";
import { api } from "../api/client";
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
    { value: "rnode_reset", label: "RNode reset" },
    { value: "rnode_update", label: "RNode update" },
    { value: "shutdown_threshold", label: "Set shutdown threshold" },
];
const inputCls = "rounded border border-gray-200 bg-white px-2 py-1 text-sm font-mono focus:outline-none focus:ring-2 focus:ring-blue-300";
const selectCls = inputCls;
export default function MultiNodePanel({ destHashes, nodes }) {
    // Bulk command state
    const [cmd, setCmd] = useState("svc_restart");
    const [params, setParams] = useState({ service: "rnsd" });
    const [cmdResults, setCmdResults] = useState({});
    const [cmdRunning, setCmdRunning] = useState(false);
    // Bulk config patch state
    const [patchType, setPatchType] = useState("rns");
    const [patchSection, setPatchSection] = useState("");
    const [patchKey, setPatchKey] = useState("");
    const [patchValue, setPatchValue] = useState("");
    const [patchResult, setPatchResult] = useState("");
    function setParam(k, v) { setParams((p) => ({ ...p, [k]: v })); }
    function handleCmdChange(newCmd) {
        setCmd(newCmd);
        setCmdResults({});
        const defaults = {
            svc_restart: { service: "rnsd" }, svc_stop: { service: "rnsd" }, svc_start: { service: "rnsd" },
            wifi_set: { enabled: true }, log_pull: { lines: 50 },
            reboot: { delay_s: 5 }, shutdown: { delay_s: 5 },
            shutdown_threshold: { soc_pct: 20 }, rnode_reset: { port: "" }, rnode_update: { port: "" },
        };
        setParams(defaults[newCmd] ?? {});
    }
    async function executeAll() {
        setCmdRunning(true);
        setCmdResults({});
        const results = {};
        for (const hash of destHashes) {
            try {
                const r = await api.nodes.command(hash, { cmd, ...params });
                results[hash] = r.output ?? (r.ok ? "OK" : r.error ?? "Failed");
            }
            catch (e) {
                results[hash] = `Error: ${e.message}`;
            }
        }
        setCmdResults(results);
        setCmdRunning(false);
    }
    async function applyPatch() {
        if (!patchSection || !patchKey) {
            setPatchResult("Section and key are required");
            return;
        }
        setPatchResult("Applying…");
        try {
            const results = await api.config.bulkPatch(destHashes, patchType, [
                { section: patchSection, key: patchKey, value: patchValue },
            ]);
            const failed = Object.entries(results).filter(([, r]) => !r.ok);
            if (failed.length === 0) {
                setPatchResult(`Applied to all ${destHashes.length} nodes ✓`);
            }
            else {
                setPatchResult(`${failed.length} failed: ${failed.map(([h]) => h.slice(0, 8)).join(", ")}`);
            }
        }
        catch (e) {
            setPatchResult(`Error: ${e.message}`);
        }
    }
    const hostname = (h) => nodes.find((n) => n.dest_hash === h)?.hostname ?? h.slice(0, 12);
    const P = ({ label, children }) => (_jsxs("div", { className: "flex items-center gap-2", children: [_jsx("label", { className: "text-xs text-gray-500 w-28 flex-shrink-0", children: label }), children] }));
    return (_jsxs("div", { className: "p-5 space-y-5", children: [_jsxs("div", { children: [_jsxs("h2", { className: "text-xl font-bold text-gray-900 mb-1", children: [destHashes.length, " nodes selected"] }), _jsx("p", { className: "text-sm text-gray-500", children: destHashes.map(hostname).join(", ") })] }), _jsxs("div", { className: "rounded-xl border border-gray-200 bg-white p-4 shadow-sm space-y-3", children: [_jsx("h3", { className: "text-sm font-semibold text-gray-700", children: "Bulk command" }), _jsxs("div", { children: [_jsx("label", { className: "text-xs text-gray-500 block mb-1", children: "Command" }), _jsx("select", { value: cmd, onChange: (e) => handleCmdChange(e.target.value), className: `${selectCls} w-56`, children: COMMANDS.map((c) => _jsx("option", { value: c.value, children: c.label }, c.value)) })] }), ["svc_restart", "svc_stop", "svc_start"].includes(cmd) && (_jsx(P, { label: "Service", children: _jsx("input", { value: params.service ?? "", onChange: (e) => setParam("service", e.target.value), className: `${inputCls} w-40` }) })), cmd === "wifi_set" && (_jsx(P, { label: "Enable", children: _jsxs("select", { value: String(params.enabled), onChange: (e) => setParam("enabled", e.target.value === "true"), className: `${selectCls} w-24`, children: [_jsx("option", { value: "true", children: "On" }), _jsx("option", { value: "false", children: "Off" })] }) })), cmd === "log_pull" && (_jsx(P, { label: "Lines", children: _jsx("input", { type: "number", value: params.lines ?? 50, min: 1, onChange: (e) => setParam("lines", Number(e.target.value)), className: `${inputCls} w-24` }) })), ["reboot", "shutdown"].includes(cmd) && (_jsx(P, { label: "Delay (s)", children: _jsx("input", { type: "number", value: params.delay_s ?? 5, min: 0, onChange: (e) => setParam("delay_s", Number(e.target.value)), className: `${inputCls} w-24` }) })), cmd === "shutdown_threshold" && (_jsx(P, { label: "Battery SoC %", children: _jsx("input", { type: "number", value: params.soc_pct ?? 20, min: 0, max: 100, onChange: (e) => setParam("soc_pct", Number(e.target.value)), className: `${inputCls} w-24` }) })), ["rnode_reset", "rnode_update"].includes(cmd) && (_jsx(P, { label: "Port", children: _jsx("input", { value: params.port ?? "", onChange: (e) => setParam("port", e.target.value), className: `${inputCls} w-40`, placeholder: "/dev/ttyACM0" }) })), _jsx("button", { onClick: executeAll, disabled: cmdRunning, className: "px-4 py-1.5 rounded bg-gray-800 text-white text-xs hover:bg-gray-700 disabled:opacity-50", children: cmdRunning ? "Running…" : `Execute on ${destHashes.length} nodes` }), Object.keys(cmdResults).length > 0 && (_jsx("div", { className: "space-y-1", children: destHashes.map((h) => (_jsxs("div", { className: "rounded bg-gray-900 px-3 py-1.5 flex gap-2 text-xs font-mono", children: [_jsx("span", { className: "text-gray-400 flex-shrink-0", children: hostname(h) }), _jsx("span", { className: "text-green-300 break-all", children: cmdResults[h] ?? "…" })] }, h))) }))] }), _jsxs("div", { className: "rounded-xl border border-gray-200 bg-white p-4 shadow-sm space-y-3", children: [_jsx("h3", { className: "text-sm font-semibold text-gray-700", children: "Bulk config patch" }), _jsx("p", { className: "text-xs text-gray-400", children: "Apply the same key change to all selected nodes." }), _jsxs("div", { className: "grid grid-cols-2 gap-2", children: [_jsxs("div", { children: [_jsx("label", { className: "text-xs text-gray-500 block mb-1", children: "Config type" }), _jsxs("select", { value: patchType, onChange: (e) => setPatchType(e.target.value), className: `${selectCls} w-full`, children: [_jsx("option", { value: "rns", children: "RNS config" }), _jsx("option", { value: "agent", children: "Agent config" })] })] }), _jsxs("div", { children: [_jsx("label", { className: "text-xs text-gray-500 block mb-1", children: "Section" }), _jsx("input", { value: patchSection, onChange: (e) => setPatchSection(e.target.value), className: `${inputCls} w-full`, placeholder: "MyRNode" })] }), _jsxs("div", { children: [_jsx("label", { className: "text-xs text-gray-500 block mb-1", children: "Key" }), _jsx("input", { value: patchKey, onChange: (e) => setPatchKey(e.target.value), className: `${inputCls} w-full`, placeholder: "txpower" })] }), _jsxs("div", { children: [_jsx("label", { className: "text-xs text-gray-500 block mb-1", children: "Value" }), _jsx("input", { value: patchValue, onChange: (e) => setPatchValue(e.target.value), className: `${inputCls} w-full`, placeholder: "14" })] })] }), _jsx("button", { onClick: applyPatch, className: "px-4 py-1.5 rounded bg-blue-600 text-white text-xs hover:bg-blue-700", children: "Apply to all nodes" }), patchResult && _jsx("p", { className: `text-xs ${patchResult.startsWith("Error") || patchResult.includes("failed") ? "text-red-600" : "text-gray-500"}`, children: patchResult })] })] }));
}
