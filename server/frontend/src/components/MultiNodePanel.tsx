import { useState } from "react";
import { api, type Node } from "../api/client";

const COMMANDS = [
  { value: "svc_restart",        label: "Restart service" },
  { value: "svc_stop",           label: "Stop service" },
  { value: "svc_start",          label: "Start service" },
  { value: "wifi_set",           label: "Set WiFi" },
  { value: "log_pull",           label: "Pull logs" },
  { value: "disk_cleanup",       label: "Disk cleanup" },
  { value: "rns_announce",       label: "RNS announce" },
  { value: "reboot",             label: "Reboot" },
  { value: "shutdown",           label: "Shutdown" },
  { value: "agent_update",       label: "Update agent" },
  { value: "rnode_reset",        label: "RNode reset" },
  { value: "rnode_update",       label: "RNode update" },
  { value: "shutdown_threshold", label: "Set shutdown threshold" },
];

const inputCls = "rounded border border-gray-200 bg-white px-2 py-1 text-sm font-mono focus:outline-none focus:ring-2 focus:ring-blue-300";
const selectCls = inputCls;

interface Props {
  destHashes: string[];
  nodes: Node[];
}

export default function MultiNodePanel({ destHashes, nodes }: Props) {
  // Bulk command state
  const [cmd, setCmd] = useState("svc_restart");
  const [params, setParams] = useState<Record<string, any>>({ service: "rnsd" });
  const [cmdResults, setCmdResults] = useState<Record<string, string>>({});
  const [cmdRunning, setCmdRunning] = useState(false);

  // Bulk config patch state
  const [patchType, setPatchType] = useState("rns");
  const [patchSection, setPatchSection] = useState("");
  const [patchKey, setPatchKey] = useState("");
  const [patchValue, setPatchValue] = useState("");
  const [patchResult, setPatchResult] = useState("");

  function setParam(k: string, v: any) { setParams((p) => ({ ...p, [k]: v })); }

  function handleCmdChange(newCmd: string) {
    setCmd(newCmd);
    setCmdResults({});
    const defaults: Record<string, Record<string, any>> = {
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
    const results: Record<string, string> = {};
    for (const hash of destHashes) {
      try {
        const r = await api.nodes.command(hash, { cmd, ...params });
        results[hash] = r.output ?? (r.ok ? "OK" : r.error ?? "Failed");
      } catch (e: any) {
        results[hash] = `Error: ${e.message}`;
      }
    }
    setCmdResults(results);
    setCmdRunning(false);
  }

  async function applyPatch() {
    if (!patchSection || !patchKey) { setPatchResult("Section and key are required"); return; }
    setPatchResult("Applying…");
    try {
      const results = await api.config.bulkPatch(destHashes, patchType, [
        { section: patchSection, key: patchKey, value: patchValue },
      ]);
      const failed = Object.entries(results).filter(([, r]: any) => !r.ok);
      if (failed.length === 0) {
        setPatchResult(`Applied to all ${destHashes.length} nodes ✓`);
      } else {
        setPatchResult(`${failed.length} failed: ${failed.map(([h]) => h.slice(0, 8)).join(", ")}`);
      }
    } catch (e: any) {
      setPatchResult(`Error: ${e.message}`);
    }
  }

  const hostname = (h: string) => nodes.find((n) => n.dest_hash === h)?.hostname ?? h.slice(0, 12);

  const P = ({ label, children }: { label: string; children: React.ReactNode }) => (
    <div className="flex items-center gap-2">
      <label className="text-xs text-gray-500 w-28 flex-shrink-0">{label}</label>
      {children}
    </div>
  );

  return (
    <div className="p-5 space-y-5">
      <div>
        <h2 className="text-xl font-bold text-gray-900 mb-1">{destHashes.length} nodes selected</h2>
        <p className="text-sm text-gray-500">{destHashes.map(hostname).join(", ")}</p>
      </div>

      {/* Bulk command */}
      <div className="rounded-xl border border-gray-200 bg-white p-4 shadow-sm space-y-3">
        <h3 className="text-sm font-semibold text-gray-700">Bulk command</h3>

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
        {cmd === "log_pull" && (
          <P label="Lines"><input type="number" value={params.lines ?? 50} min={1} onChange={(e) => setParam("lines", Number(e.target.value))} className={`${inputCls} w-24`} /></P>
        )}
        {["reboot","shutdown"].includes(cmd) && (
          <P label="Delay (s)"><input type="number" value={params.delay_s ?? 5} min={0} onChange={(e) => setParam("delay_s", Number(e.target.value))} className={`${inputCls} w-24`} /></P>
        )}
        {cmd === "shutdown_threshold" && (
          <P label="Battery SoC %"><input type="number" value={params.soc_pct ?? 20} min={0} max={100} onChange={(e) => setParam("soc_pct", Number(e.target.value))} className={`${inputCls} w-24`} /></P>
        )}
        {["rnode_reset","rnode_update"].includes(cmd) && (
          <P label="Port"><input value={params.port ?? ""} onChange={(e) => setParam("port", e.target.value)} className={`${inputCls} w-40`} placeholder="/dev/ttyACM0" /></P>
        )}

        <button onClick={executeAll} disabled={cmdRunning} className="px-4 py-1.5 rounded bg-gray-800 text-white text-xs hover:bg-gray-700 disabled:opacity-50">
          {cmdRunning ? "Running…" : `Execute on ${destHashes.length} nodes`}
        </button>

        {Object.keys(cmdResults).length > 0 && (
          <div className="space-y-1">
            {destHashes.map((h) => (
              <div key={h} className="rounded bg-gray-900 px-3 py-1.5 flex gap-2 text-xs font-mono">
                <span className="text-gray-400 flex-shrink-0">{hostname(h)}</span>
                <span className="text-green-300 break-all">{cmdResults[h] ?? "…"}</span>
              </div>
            ))}
          </div>
        )}
      </div>

      {/* Bulk config patch */}
      <div className="rounded-xl border border-gray-200 bg-white p-4 shadow-sm space-y-3">
        <h3 className="text-sm font-semibold text-gray-700">Bulk config patch</h3>
        <p className="text-xs text-gray-400">Apply the same key change to all selected nodes.</p>

        <div className="grid grid-cols-2 gap-2">
          <div>
            <label className="text-xs text-gray-500 block mb-1">Config type</label>
            <select value={patchType} onChange={(e) => setPatchType(e.target.value)} className={`${selectCls} w-full`}>
              <option value="rns">RNS config</option>
              <option value="agent">Agent config</option>
            </select>
          </div>
          <div>
            <label className="text-xs text-gray-500 block mb-1">Section</label>
            <input value={patchSection} onChange={(e) => setPatchSection(e.target.value)} className={`${inputCls} w-full`} placeholder="MyRNode" />
          </div>
          <div>
            <label className="text-xs text-gray-500 block mb-1">Key</label>
            <input value={patchKey} onChange={(e) => setPatchKey(e.target.value)} className={`${inputCls} w-full`} placeholder="txpower" />
          </div>
          <div>
            <label className="text-xs text-gray-500 block mb-1">Value</label>
            <input value={patchValue} onChange={(e) => setPatchValue(e.target.value)} className={`${inputCls} w-full`} placeholder="14" />
          </div>
        </div>

        <button onClick={applyPatch} className="px-4 py-1.5 rounded bg-blue-600 text-white text-xs hover:bg-blue-700">
          Apply to all nodes
        </button>

        {patchResult && <p className={`text-xs ${patchResult.startsWith("Error") || patchResult.includes("failed") ? "text-red-600" : "text-gray-500"}`}>{patchResult}</p>}
      </div>
    </div>
  );
}
