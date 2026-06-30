interface SparkLineProps {
  /** (timestamp_sec, value) samples for this field, any order, nulls dropped by caller. */
  points: { ts: number; value: number }[];
  /** Shared time window (unix seconds) -- the SAME for every card, so x position
   * means the same thing on every graph instead of being index-within-this-fields-
   * own-sparse-array (which made differently-sparse metrics look like they spanned
   * different windows even when reading from the same underlying buffer). */
  domainStart: number;
  domainEnd: number;
  label: string;
  unit: string;
  latest: number | null;
  color?: string;
  width?: number;
  height?: number;
  min?: number;
  max?: number;
}

export default function SparkLine({
  points: rawPoints,
  domainStart,
  domainEnd,
  label,
  unit,
  latest,
  color = "#3b82f6",
  width = 100,
  height = 56,
  min,
  max,
}: SparkLineProps) {
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

  const fmt = (v: number) =>
    Math.abs(v) >= 1000 ? v.toFixed(0) : v.toFixed(1);
  // Only show an axis scale when it means something -- either real data to
  // derive a range from, or an explicit fixed min/max (e.g. 0-100%).
  const showScale = values.length > 0 || (min != null && max != null);

  return (
    <div className="flex flex-col gap-0.5 flex-1 min-w-0 h-full rounded-lg border border-gray-100 bg-gray-50/60 px-2.5 py-2">
      <div className="flex justify-between items-baseline flex-shrink-0">
        <span className="text-xs text-gray-500">{label}</span>
        <span className="text-xs font-mono font-medium text-gray-900">
          {latest != null ? `${fmt(latest)}${unit}` : "—"}
        </span>
      </div>
      {/* relative wrapper so the hi/lo labels can be plain HTML, positioned
          by CSS percentage -- SVG <text> would get horizontally squashed by
          the viewBox's non-uniform stretch (preserveAspectRatio="none"),
          but a straight horizontal <line> looks the same either way. */}
      <div className="relative flex-1 min-h-0">
        <svg viewBox={`0 0 ${width} ${height}`} preserveAspectRatio="none" className="w-full h-full">
          {showScale && (
            <>
              <line x1="0" y1="0" x2={width} y2="0" stroke="#e5e7eb" strokeWidth="1" vectorEffect="non-scaling-stroke" />
              <line x1="0" y1={height / 2} x2={width} y2={height / 2} stroke="#e5e7eb" strokeWidth="1" strokeDasharray="2,2" vectorEffect="non-scaling-stroke" />
              <line x1="0" y1={height} x2={width} y2={height} stroke="#e5e7eb" strokeWidth="1" vectorEffect="non-scaling-stroke" />
            </>
          )}
          <polyline
            points={pts}
            fill="none"
            stroke={color}
            strokeWidth="1.5"
            strokeLinejoin="round"
            strokeLinecap="round"
            vectorEffect="non-scaling-stroke"
          />
          {singlePoint && (
            <circle cx={singlePoint.x} cy={singlePoint.y} r="2" fill={color} vectorEffect="non-scaling-stroke" />
          )}
        </svg>
        {showScale && (
          <>
            <span className="absolute top-0 right-0 text-[9px] leading-none text-gray-400 bg-gray-50/80 px-0.5 rounded-bl">{fmt(hi)}</span>
            <span className="absolute bottom-0 right-0 text-[9px] leading-none text-gray-400 bg-gray-50/80 px-0.5 rounded-tl">{fmt(lo)}</span>
          </>
        )}
      </div>
    </div>
  );
}
