import { useEffect, useRef, useState } from "react";
import { api, type Node } from "../api/client";
import NodeSidebarItem from "../components/NodeSidebarItem";
import NodePanel from "../components/NodePanel";
import MultiNodePanel from "../components/MultiNodePanel";

export default function NodesView() {
  const [nodes, setNodes] = useState<Node[]>([]);
  const [selected, setSelected] = useState<Set<string>>(new Set());
  const [serverDestHash, setServerDestHash] = useState<string>("");
  const [liveTelemetry, setLiveTelemetry] = useState<Record<string, Record<string, unknown>>>({});
  const [showAddModal, setShowAddModal] = useState(false);
  const [addHash, setAddHash] = useState("");
  const [addName, setAddName] = useState("");
  const [addError, setAddError] = useState("");
  const [addBusy, setAddBusy] = useState(false);
  const [copied, setCopied] = useState(false);
  const wsRef = useRef<WebSocket | null>(null);
  const pollRef = useRef<ReturnType<typeof setInterval> | null>(null);

  // Fetch server's own dest_hash so we can label it
  useEffect(() => {
    api.status().then((s) => {
      if (typeof s.dest_hash === "string") setServerDestHash(s.dest_hash);
    }).catch(() => {});
  }, []);

  async function loadNodes() {
    try {
      const list = await api.nodes.list();
      setNodes(list);
    } catch {
      // ignore — keep stale data
    }
  }

  // WebSocket for live telemetry + node updates
  function connectWs() {
    const proto = window.location.protocol === "https:" ? "wss" : "ws";
    const ws = new WebSocket(`${proto}://${window.location.host}/api/v1/ws`);
    wsRef.current = ws;

    ws.onmessage = (ev) => {
      try {
        const msg = JSON.parse(ev.data);
        const hash: string = msg.dest_hash;
        if (!hash) return;

        if (msg.type === "telemetry" && msg.data) {
          const d = msg.data;
          setLiveTelemetry((prev) => ({ ...prev, [hash]: d }));
          setNodes((prev) => {
            const idx = prev.findIndex((n) => n.dest_hash === hash);
            const patch = {
              hostname: d.hostname ?? undefined,
              version: d.version ?? undefined,
              last_errors: Array.isArray(d.errors) ? d.errors : [],
              last_seen: Date.now() / 1000,
              online: true,
            };
            if (idx >= 0) {
              const next = [...prev];
              next[idx] = { ...next[idx], ...patch };
              return next;
            }
            return prev;
          });
        }

        if (msg.type === "announce" && msg.data) {
          const d = msg.data;
          setNodes((prev) => {
            const idx = prev.findIndex((n) => n.dest_hash === hash);
            const patch = {
              hostname: d.hostname ?? undefined,
              version: d.version ?? undefined,
              identity_hash: d.identity_hash ?? undefined,
              last_seen: Date.now() / 1000,
              online: true,
            };
            if (idx >= 0) {
              const next = [...prev];
              next[idx] = { ...next[idx], ...patch };
              return next;
            }
            return prev;
          });
        }
      } catch {
        // malformed message — ignore
      }
    };

    ws.onclose = () => {
      wsRef.current = null;
      // reconnect after 5s
      setTimeout(() => { if (!wsRef.current) connectWs(); }, 5000);
    };
  }

  useEffect(() => {
    loadNodes();
    connectWs();
    pollRef.current = setInterval(loadNodes, 30_000);
    return () => {
      if (pollRef.current) clearInterval(pollRef.current);
      if (wsRef.current) wsRef.current.close();
    };
  }, []);

  // Selection helpers
  function selectOnly(hash: string) {
    setSelected(new Set([hash]));
  }

  function toggleSelect(hash: string) {
    setSelected((prev) => {
      const next = new Set(prev);
      if (next.has(hash)) next.delete(hash);
      else next.add(hash);
      return next;
    });
  }

  function handleDelete(hash: string) {
    setNodes((prev) => prev.filter((n) => n.dest_hash !== hash));
    setSelected((prev) => {
      const next = new Set(prev);
      next.delete(hash);
      return next;
    });
  }

  async function submitAddNode(e: React.FormEvent) {
    e.preventDefault();
    const hash = addHash.trim().toLowerCase();
    if (!hash) { setAddError("Destination hash is required"); return; }
    setAddError("");
    setAddBusy(true);
    try {
      const node = await api.nodes.add(hash, addName.trim() || undefined);
      setNodes((prev) => {
        if (prev.some((n) => n.dest_hash === node.dest_hash)) return prev;
        return [...prev, node];
      });
      setAddHash("");
      setAddName("");
      setShowAddModal(false);
      setSelected(new Set([node.dest_hash]));
    } catch (err: any) {
      setAddError(err.message ?? "Failed to add node");
    } finally {
      setAddBusy(false);
    }
  }

  // Server node first, then alphabetical by hostname/hash
  const sortedNodes = [...nodes].sort((a, b) => {
    if (a.dest_hash === serverDestHash) return -1;
    if (b.dest_hash === serverDestHash) return 1;
    const la = a.hostname ?? a.dest_hash;
    const lb = b.hostname ?? b.dest_hash;
    return la.localeCompare(lb);
  });

  const selectedArray = [...selected].filter((h) => nodes.some((n) => n.dest_hash === h));
  const singleSelected = selectedArray.length === 1 ? selectedArray[0] : null;
  const selectedNode = singleSelected ? nodes.find((n) => n.dest_hash === singleSelected) : null;

  return (
    <div className="flex" style={{ height: "calc(100vh - 49px)" }}>
      {/* Sidebar */}
      <div className="w-52 flex-shrink-0 flex flex-col border-r border-gray-200 bg-white">
        <div className="flex-1 overflow-y-auto">
          {sortedNodes.length === 0 && (
            <p className="px-3 py-4 text-xs text-gray-400">No nodes registered yet.</p>
          )}
          {sortedNodes.map((node) => (
            <NodeSidebarItem
              key={node.dest_hash}
              node={node}
              isSelected={selected.has(node.dest_hash)}
              isServer={node.dest_hash === serverDestHash}
              onSelect={() => selectOnly(node.dest_hash)}
              onToggle={() => toggleSelect(node.dest_hash)}
            />
          ))}
        </div>
        <div className="p-2 border-t border-gray-100">
          <button
            onClick={() => { setShowAddModal(true); setAddError(""); }}
            className="w-full text-xs text-gray-500 hover:text-gray-900 hover:bg-gray-50 rounded px-2 py-1.5 text-left"
          >
            + Add node
          </button>
        </div>
      </div>

      {/* Add node modal */}
      {showAddModal && (
        <div className="fixed inset-0 z-50 flex items-center justify-center bg-black/30">
          <div className="bg-white rounded-xl shadow-xl p-5 w-80 space-y-3">
            <h3 className="text-sm font-semibold text-gray-800">Add node</h3>

            {/* Server hash — paste this into agent.json on the node */}
            {serverDestHash && (
              <div className="rounded-lg bg-gray-50 border border-gray-200 px-3 py-2 space-y-1">
                <p className="text-xs text-gray-500">Server destination hash — paste into <span className="font-mono">agent.json</span> on the node:</p>
                <div className="flex items-center gap-2">
                  <span className="flex-1 font-mono text-xs text-gray-800 break-all select-all">{serverDestHash}</span>
                  <button
                    type="button"
                    onClick={() => {
                      const write = (text: string) => {
                        if (navigator.clipboard) {
                          navigator.clipboard.writeText(text);
                        } else {
                          const el = document.createElement("textarea");
                          el.value = text;
                          el.style.cssText = "position:fixed;opacity:0";
                          document.body.appendChild(el);
                          el.select();
                          document.execCommand("copy");
                          document.body.removeChild(el);
                        }
                      };
                      write(serverDestHash);
                      setCopied(true);
                      setTimeout(() => setCopied(false), 2000);
                    }}
                    className="flex-shrink-0 text-xs px-1.5 py-0.5 rounded hover:bg-gray-200 transition-colors"
                    style={{ color: copied ? "#16a34a" : undefined }}
                    title="Copy to clipboard"
                  >
                    {copied ? "Copied!" : "Copy"}
                  </button>
                </div>
              </div>
            )}

            <form onSubmit={submitAddNode} className="space-y-3">
              <div>
                <label className="text-xs text-gray-500 block mb-1">Node destination hash</label>
                <input
                  autoFocus
                  value={addHash}
                  onChange={(e) => setAddHash(e.target.value)}
                  className="w-full rounded border border-gray-200 px-2 py-1.5 text-xs font-mono focus:outline-none focus:ring-2 focus:ring-blue-300"
                  placeholder="e.g. a3f1b2c4d5e6…"
                  spellCheck={false}
                />
                <p className="mt-1 text-xs text-gray-400">Printed at the end of <span className="font-mono">install_node.sh</span>, or run it with <span className="font-mono">--show-hash</span>.</p>
              </div>
              <div>
                <label className="text-xs text-gray-500 block mb-1">Label (optional)</label>
                <input
                  value={addName}
                  onChange={(e) => setAddName(e.target.value)}
                  className="w-full rounded border border-gray-200 px-2 py-1.5 text-xs focus:outline-none focus:ring-2 focus:ring-blue-300"
                  placeholder="e.g. rtr1"
                />
                <p className="mt-1 text-xs text-gray-400">Shown in the sidebar instead of the system hostname.</p>
              </div>
              {addError && <p className="text-xs text-red-600">{addError}</p>}
              <div className="flex gap-2 justify-end pt-1">
                <button
                  type="button"
                  onClick={() => { setShowAddModal(false); setAddHash(""); setAddName(""); setAddError(""); }}
                  className="px-3 py-1.5 text-xs text-gray-600 hover:text-gray-900"
                >
                  Cancel
                </button>
                <button
                  type="submit"
                  disabled={addBusy}
                  className="px-3 py-1.5 rounded bg-gray-800 text-white text-xs hover:bg-gray-700 disabled:opacity-50"
                >
                  {addBusy ? "Adding…" : "Add"}
                </button>
              </div>
            </form>
          </div>
        </div>
      )}

      {/* Right panel */}
      <div className="flex-1 overflow-y-auto">
        {selectedArray.length === 0 && (
          <div className="flex items-center justify-center h-full text-sm text-gray-400 select-none">
            Select a node from the sidebar
          </div>
        )}
        {selectedArray.length === 1 && selectedNode && (
          <NodePanel
            key={singleSelected!}
            destHash={singleSelected!}
            node={selectedNode}
            onDelete={() => handleDelete(singleSelected!)}
            liveTelemetry={liveTelemetry[singleSelected!]}
          />
        )}
        {selectedArray.length > 1 && (
          <MultiNodePanel
            destHashes={selectedArray}
            nodes={nodes}
          />
        )}
      </div>
    </div>
  );
}
