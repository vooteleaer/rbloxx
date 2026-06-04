import { jsx as _jsx, jsxs as _jsxs } from "react/jsx-runtime";
export default function SparkLine({ data, label, unit, latest, color = "#3b82f6", width = 120, height = 36, min, max, }) {
    const valid = data.filter((v) => v != null);
    if (valid.length === 0)
        return null;
    const lo = min ?? Math.min(...valid);
    const hi = max ?? Math.max(...valid);
    const range = hi - lo || 1;
    const pts = data
        .map((v, i) => {
        if (v == null)
            return null;
        const x = (i / (data.length - 1 || 1)) * width;
        const y = height - ((v - lo) / range) * height;
        return `${x.toFixed(1)},${y.toFixed(1)}`;
    })
        .filter(Boolean)
        .join(" ");
    const fmt = (v) => Math.abs(v) >= 1000 ? v.toFixed(0) : v.toFixed(1);
    return (_jsxs("div", { className: "flex flex-col gap-0.5", children: [_jsxs("div", { className: "flex justify-between items-baseline", children: [_jsx("span", { className: "text-xs text-gray-500", children: label }), _jsx("span", { className: "text-xs font-mono font-medium text-gray-900", children: latest != null ? `${fmt(latest)}${unit}` : "—" })] }), _jsx("svg", { width: width, height: height, className: "overflow-visible", children: _jsx("polyline", { points: pts, fill: "none", stroke: color, strokeWidth: "1.5", strokeLinejoin: "round", strokeLinecap: "round" }) })] }));
}
