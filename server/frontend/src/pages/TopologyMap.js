import { jsx as _jsx, jsxs as _jsxs } from "react/jsx-runtime";
import { useEffect, useState } from "react";
const W = 800;
const H = 800;
const CX = W / 2;
const CY = H / 2;
const SERVER_R = 42;
const NODE_R = 30;
const RELAY_R = 18;
const SPOKE_R = 280;
const COLOR_LORA = "#f59e0b";
const COLOR_MULTI = "#6b7280";
const COLOR_NONE = "#d1d5db";
const COLOR_MANAGED_RELAY = "#3b82f6";
const COLOR_UNKNOWN_RELAY = "#9ca3af";
function shortHash(h) {
    return h.slice(0, 8) + "…";
}
function spokePoint(angle, r) {
    return { x: CX + r * Math.cos(angle), y: CY + r * Math.sin(angle) };
}
function lerp(a, b, t) {
    return { x: a.x + (b.x - a.x) * t, y: a.y + (b.y - a.y) * t };
}
export default function TopologyMap() {
    const [graph, setGraph] = useState(null);
    const [status, setStatus] = useState("Loading…");
    useEffect(() => {
        let cancelled = false;
        async function load() {
            try {
                const res = await fetch("/api/v1/topology/hub");
                if (!res.ok)
                    throw new Error(`HTTP ${res.status}`);
                const data = await res.json();
                if (!cancelled) {
                    setGraph(data);
                    setStatus("");
                }
            }
            catch (e) {
                if (!cancelled)
                    setStatus(`Error: ${e.message}`);
            }
        }
        load();
        const iv = setInterval(load, 60000);
        return () => { cancelled = true; clearInterval(iv); };
    }, []);
    const nodes = graph?.nodes ?? [];
    const n = nodes.length;
    const angles = nodes.map((_, i) => (2 * Math.PI * i) / Math.max(n, 1) - Math.PI / 2);
    const serverPt = { x: CX, y: CY };
    return (_jsxs("div", { className: "flex flex-col h-[calc(100vh-56px)]", children: [_jsxs("div", { className: "flex items-center gap-4 px-6 py-3 border-b border-gray-200 bg-white text-sm flex-shrink-0", children: [_jsx("h1", { className: "font-semibold text-gray-900", children: "Network Topology" }), graph && _jsxs("span", { className: "text-gray-500", children: [n, " node", n !== 1 ? "s" : ""] }), _jsxs("div", { className: "ml-auto flex items-center gap-5 text-xs text-gray-500", children: [_jsxs("span", { className: "flex items-center gap-1.5", children: [_jsx("svg", { width: "24", height: "10", children: _jsx("line", { x1: "0", y1: "5", x2: "24", y2: "5", stroke: COLOR_LORA, strokeWidth: "2" }) }), "Direct link"] }), _jsxs("span", { className: "flex items-center gap-1.5", children: [_jsx("svg", { width: "24", height: "10", children: _jsx("line", { x1: "0", y1: "5", x2: "24", y2: "5", stroke: COLOR_MULTI, strokeWidth: "2" }) }), "Multi-hop"] }), _jsxs("span", { className: "flex items-center gap-1.5", children: [_jsx("span", { className: "inline-block h-3 w-3 rounded-full bg-green-500" }), " Online"] }), _jsxs("span", { className: "flex items-center gap-1.5", children: [_jsx("span", { className: "inline-block h-3 w-3 rounded-full bg-gray-300" }), " Offline"] })] })] }), status ? (_jsx("div", { className: "flex-1 flex items-center justify-center text-gray-400 text-sm", children: status })) : (_jsx("div", { className: "flex-1 flex items-center justify-center bg-gray-50 overflow-hidden p-4", children: _jsxs("svg", { viewBox: `0 0 ${W} ${H}`, className: "w-full", style: { maxWidth: `${W}px`, maxHeight: "100%" }, children: [nodes.map((node, i) => {
                            const angle = angles[i];
                            const nodePt = spokePoint(angle, SPOKE_R);
                            const chain = node.chain ?? [];
                            const totalSegs = chain.length + 1;
                            const lineColor = node.hops === null ? COLOR_NONE : node.hops <= 1 ? COLOR_LORA : COLOR_MULTI;
                            const dashed = node.hops === null;
                            // Line endpoints clipped to circle edges
                            const lineStart = lerp(serverPt, nodePt, SERVER_R / SPOKE_R);
                            const lineEnd = lerp(nodePt, serverPt, NODE_R / SPOKE_R);
                            return (_jsxs("g", { children: [_jsx("line", { x1: lineStart.x, y1: lineStart.y, x2: lineEnd.x, y2: lineEnd.y, stroke: lineColor, strokeWidth: 2, strokeDasharray: dashed ? "6 4" : undefined, strokeLinecap: "round" }), chain.map((relay, j) => {
                                        const t = (j + 1) / totalSegs;
                                        const pt = lerp(serverPt, nodePt, t);
                                        if (relay === null) {
                                            return (_jsxs("g", { children: [_jsx("circle", { cx: pt.x, cy: pt.y, r: RELAY_R, fill: "#f9fafb", stroke: COLOR_UNKNOWN_RELAY, strokeWidth: 1.5, strokeDasharray: "3 2" }), _jsx("text", { x: pt.x, y: pt.y + 5, textAnchor: "middle", fontSize: 13, fill: COLOR_UNKNOWN_RELAY, fontWeight: "700", children: "?" })] }, j));
                                        }
                                        return (_jsxs("g", { children: [_jsx("circle", { cx: pt.x, cy: pt.y, r: RELAY_R, fill: relay.managed ? "#dbeafe" : "#f3f4f6", stroke: relay.managed ? COLOR_MANAGED_RELAY : COLOR_UNKNOWN_RELAY, strokeWidth: 1.5 }), _jsx("text", { x: pt.x, y: pt.y + 4, textAnchor: "middle", fontSize: 8, fill: "#374151", children: relay.hostname ?? relay.dest_hash.slice(0, 7) })] }, j));
                                    }), _jsx("circle", { cx: nodePt.x, cy: nodePt.y, r: NODE_R, fill: node.online ? "#22c55e" : "#d1d5db", stroke: node.online ? "#15803d" : "#9ca3af", strokeWidth: 2 }), _jsx("text", { x: nodePt.x, y: nodePt.y + (node.hops !== null ? -4 : 4), textAnchor: "middle", fontSize: 10, fill: node.online ? "#fff" : "#6b7280", fontWeight: "600", children: node.hostname ?? shortHash(node.dest_hash) }), node.hops !== null && (_jsxs("text", { x: nodePt.x, y: nodePt.y + 9, textAnchor: "middle", fontSize: 8, fill: node.online ? "#bbf7d0" : "#9ca3af", children: [node.hops, " hop", node.hops !== 1 ? "s" : ""] }))] }, node.dest_hash));
                        }), _jsx("circle", { cx: CX, cy: CY, r: SERVER_R, fill: "#1e40af", stroke: "#1e3a8a", strokeWidth: 3 }), _jsx("text", { x: CX, y: CY - 6, textAnchor: "middle", fontSize: 13, fill: "white", fontWeight: "700", children: "server" }), _jsxs("text", { x: CX, y: CY + 10, textAnchor: "middle", fontSize: 8, fill: "#bfdbfe", children: [graph?.server_dest_hash.slice(0, 12), "\u2026"] })] }) }))] }));
}
