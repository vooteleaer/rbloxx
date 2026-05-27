interface SparkLineProps {
  data: (number | null)[];
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
  data,
  label,
  unit,
  latest,
  color = "#3b82f6",
  width = 120,
  height = 36,
  min,
  max,
}: SparkLineProps) {
  const valid = data.filter((v): v is number => v != null);
  if (valid.length === 0) return null;

  const lo = min ?? Math.min(...valid);
  const hi = max ?? Math.max(...valid);
  const range = hi - lo || 1;

  const pts = data
    .map((v, i) => {
      if (v == null) return null;
      const x = (i / (data.length - 1 || 1)) * width;
      const y = height - ((v - lo) / range) * height;
      return `${x.toFixed(1)},${y.toFixed(1)}`;
    })
    .filter(Boolean)
    .join(" ");

  const fmt = (v: number) =>
    Math.abs(v) >= 1000 ? v.toFixed(0) : v.toFixed(1);

  return (
    <div className="flex flex-col gap-0.5">
      <div className="flex justify-between items-baseline">
        <span className="text-xs text-gray-500">{label}</span>
        <span className="text-xs font-mono font-medium text-gray-900">
          {latest != null ? `${fmt(latest)}${unit}` : "—"}
        </span>
      </div>
      <svg width={width} height={height} className="overflow-visible">
        <polyline
          points={pts}
          fill="none"
          stroke={color}
          strokeWidth="1.5"
          strokeLinejoin="round"
          strokeLinecap="round"
        />
      </svg>
    </div>
  );
}
