import { jsx as _jsx, jsxs as _jsxs } from "react/jsx-runtime";
import { useEffect, useRef, useState } from "react";
import { Network } from "vis-network";
import { DataSet } from "vis-data";
function ifaceType(iface) {
    const s = iface.toLowerCase();
    if (s.includes("rnode") || s.includes("lora"))
        return "lora";
    if (s.includes("auto") || s.includes("wifi") || s.includes("wlan"))
        return "wifi";
    if (s.includes("tcp") || s.includes("udp"))
        return "tcp";
    return "other";
}
const IFACE_COLOR = {
    lora: "#f59e0b",
    wifi: "#3b82f6",
    tcp: "#8b5cf6",
    other: "#9ca3af",
};
const VIS_OPTIONS = {
    physics: {
        solver: "forceAtlas2Based",
        forceAtlas2Based: { gravitationalConstant: -50, springLength: 120 },
        stabilization: { iterations: 150 },
    },
    nodes: {
        shape: "dot",
        size: 16,
        font: { size: 12, color: "#1f2937" },
        borderWidth: 2,
    },
    edges: {
        width: 2,
        smooth: { type: "continuous", enabled: true, roundness: 0.2 },
        font: { size: 10, align: "middle" },
    },
    interaction: { hover: true, tooltipDelay: 100 },
};
function edgeLabel(e) {
    const parts = [];
    if (e.rssi !== null)
        parts.push(`${e.rssi} dBm`);
    if (e.snr !== null)
        parts.push(`SNR ${e.snr.toFixed(1)}`);
    if (e.bitrate !== null)
        parts.push(`${(e.bitrate / 1000).toFixed(1)} kbps`);
    return parts.join(" · ");
}
function edgeTitle(e) {
    return [
        `Interface: ${e.interface}`,
        e.rssi !== null ? `RSSI: ${e.rssi} dBm` : null,
        e.snr !== null ? `SNR: ${e.snr.toFixed(1)} dB` : null,
        e.bitrate !== null ? `Rate: ${(e.bitrate / 1000).toFixed(1)} kbps` : null,
    ]
        .filter(Boolean)
        .join("\n");
}
export default function TopologyMap() {
    const containerRef = useRef(null);
    const networkRef = useRef(null);
    const [status, setStatus] = useState("Loading topology…");
    const [nodeCount, setNodeCount] = useState(0);
    const [edgeCount, setEdgeCount] = useState(0);
    useEffect(() => {
        let cancelled = false;
        async function load() {
            try {
                const res = await fetch("/api/v1/topology");
                const graph = await res.json();
                if (cancelled || !containerRef.current)
                    return;
                setNodeCount(graph.nodes.length);
                setEdgeCount(graph.edges.length);
                const visNodes = new DataSet(graph.nodes.map((n) => ({
                    id: n.id,
                    label: n.hostname ?? n.id.slice(0, 8) + "…",
                    title: `${n.id}\n${n.managed ? "Managed" : "Unmanaged"}`,
                    color: {
                        background: n.online ? (n.managed ? "#22c55e" : "#86efac") : "#d1d5db",
                        border: n.managed ? "#15803d" : "#6b7280",
                    },
                    font: { color: n.online ? "#111827" : "#9ca3af" },
                    size: n.managed ? 18 : 12,
                })));
                const visEdges = new DataSet(graph.edges.map((e, i) => {
                    const type = ifaceType(e.interface);
                    return {
                        id: i,
                        from: e.from,
                        to: e.to,
                        label: edgeLabel(e),
                        title: edgeTitle(e),
                        color: { color: IFACE_COLOR[type], highlight: IFACE_COLOR[type] },
                        dashes: type === "tcp",
                    };
                }));
                if (networkRef.current) {
                    networkRef.current.destroy();
                }
                networkRef.current = new Network(containerRef.current, { nodes: visNodes, edges: visEdges }, VIS_OPTIONS);
                setStatus(graph.nodes.length === 0 ? "No topology data yet — waiting for nodes to report." : "");
            }
            catch (e) {
                if (!cancelled)
                    setStatus(`Error: ${e.message}`);
            }
        }
        load();
        const interval = setInterval(load, 60000);
        return () => {
            cancelled = true;
            clearInterval(interval);
            networkRef.current?.destroy();
        };
    }, []);
    return (_jsxs("div", { className: "flex flex-col h-[calc(100vh-56px)]", children: [_jsxs("div", { className: "flex items-center gap-4 px-6 py-3 border-b border-gray-200 bg-white text-sm", children: [_jsx("h1", { className: "font-semibold text-gray-900", children: "Network Topology" }), nodeCount > 0 && (_jsxs("span", { className: "text-gray-500", children: [nodeCount, " nodes \u00B7 ", edgeCount, " links"] })), _jsxs("div", { className: "ml-auto flex items-center gap-4", children: [[
                                { label: "LoRa", color: IFACE_COLOR.lora },
                                { label: "WiFi/Auto", color: IFACE_COLOR.wifi },
                                { label: "TCP/UDP", color: IFACE_COLOR.tcp },
                            ].map(({ label, color }) => (_jsxs("span", { className: "flex items-center gap-1.5 text-xs text-gray-600", children: [_jsx("span", { className: "inline-block h-2.5 w-6 rounded", style: { background: color } }), label] }, label))), _jsxs("span", { className: "flex items-center gap-1.5 text-xs text-gray-600", children: [_jsx("span", { className: "inline-block h-3 w-3 rounded-full bg-green-500" }), " Managed online"] }), _jsxs("span", { className: "flex items-center gap-1.5 text-xs text-gray-600", children: [_jsx("span", { className: "inline-block h-3 w-3 rounded-full bg-gray-300" }), " Offline / unmanaged"] })] })] }), status && (_jsx("div", { className: "flex-1 flex items-center justify-center text-gray-400", children: status })), _jsx("div", { ref: containerRef, className: "flex-1", style: { display: status ? "none" : "block" } })] }));
}
