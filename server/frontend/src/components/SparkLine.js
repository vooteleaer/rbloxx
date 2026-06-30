import { jsx as _jsx, jsxs as _jsxs, Fragment as _Fragment } from "react/jsx-runtime";
export default function SparkLine({ points: rawPoints, domainStart, domainEnd, label, unit, latest, color = "#3b82f6", width = 100, height = 56, min, max, }) {
    const values = rawPoints.map((p) => p.value);
    // Card is always rendered (hardcoded metric list) even with zero data yet --
    // just skip the point math and leave the graph blank in that case.
    const lo = min ?? (values.length ? Math.min(...values) : 0);
    const hi = max ?? (values.length ? Math.max(...values) : 1);
    const range = hi - lo || 1;
    const domainRange = domainEnd - domainStart || 1;
    const points = [...rawPoints]
        .sort((a, b) => a.ts - b.ts)
        .map((p) => ({
        x: ((p.ts - domainStart) / domainRange) * width,
        y: height - ((p.value - lo) / range) * height,
    }));
    const pts = points.map((p) => `${p.x.toFixed(1)},${p.y.toFixed(1)}`).join(" ");
    // A <polyline> with a single point has no segment to draw, so a metric
    // that's only sampled once in the current window would show its value but
    // no visible mark at all -- draw a dot for that case instead.
    const singlePoint = points.length === 1 ? points[0] : null;
    const fmt = (v) => Math.abs(v) >= 1000 ? v.toFixed(0) : v.toFixed(1);
    // Only show an axis scale when it means something -- either real data to
    // derive a range from, or an explicit fixed min/max (e.g. 0-100%).
    const showScale = values.length > 0 || (min != null && max != null);
    return (_jsxs("div", { className: "flex flex-col gap-0.5 flex-1 min-w-0 h-full rounded-lg border border-gray-100 bg-gray-50/60 px-2.5 py-2", children: [_jsxs("div", { className: "flex justify-between items-baseline flex-shrink-0", children: [_jsx("span", { className: "text-xs text-gray-500", children: label }), _jsx("span", { className: "text-xs font-mono font-medium text-gray-900", children: latest != null ? `${fmt(latest)}${unit}` : "—" })] }), _jsxs("div", { className: "relative flex-1 min-h-0", children: [_jsxs("svg", { viewBox: `0 0 ${width} ${height}`, preserveAspectRatio: "none", className: "w-full h-full", children: [showScale && (_jsxs(_Fragment, { children: [_jsx("line", { x1: "0", y1: "0", x2: width, y2: "0", stroke: "#e5e7eb", strokeWidth: "1", vectorEffect: "non-scaling-stroke" }), _jsx("line", { x1: "0", y1: height / 2, x2: width, y2: height / 2, stroke: "#e5e7eb", strokeWidth: "1", strokeDasharray: "2,2", vectorEffect: "non-scaling-stroke" }), _jsx("line", { x1: "0", y1: height, x2: width, y2: height, stroke: "#e5e7eb", strokeWidth: "1", vectorEffect: "non-scaling-stroke" })] })), _jsx("polyline", { points: pts, fill: "none", stroke: color, strokeWidth: "1.5", strokeLinejoin: "round", strokeLinecap: "round", vectorEffect: "non-scaling-stroke" }), singlePoint && (_jsx("circle", { cx: singlePoint.x, cy: singlePoint.y, r: "2", fill: color, vectorEffect: "non-scaling-stroke" }))] }), showScale && (_jsxs(_Fragment, { children: [_jsx("span", { className: "absolute top-0 right-0 text-[9px] leading-none text-gray-400 bg-gray-50/80 px-0.5 rounded-bl", children: fmt(hi) }), _jsx("span", { className: "absolute bottom-0 right-0 text-[9px] leading-none text-gray-400 bg-gray-50/80 px-0.5 rounded-tl", children: fmt(lo) })] }))] })] }));
}
