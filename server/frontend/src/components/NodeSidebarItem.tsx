import { useEffect, useState } from "react";
import type { Node } from "../api/client";

interface Props {
  node: Node;
  isSelected: boolean;
  isServer: boolean;
  onSelect(): void;
  onToggle(): void;
  /** Bumped (Date.now()) each time an announce arrives for this node — flashes the heart. */
  lastAnnounce?: number;
}

export default function NodeSidebarItem({ node, isSelected, isServer, onSelect, onToggle, lastAnnounce }: Props) {
  const [beat, setBeat] = useState(false);

  useEffect(() => {
    if (!lastAnnounce) return;
    setBeat(true);
    const t = setTimeout(() => setBeat(false), 600);
    return () => clearTimeout(t);
  }, [lastAnnounce]);

  const dotColor = !node.online
    ? "bg-red-500"
    : node.last_errors.length > 0
    ? "bg-amber-400"
    : "bg-green-500";

  const label = node.label ?? node.hostname ?? node.dest_hash.slice(0, 12);

  return (
    <div
      onClick={onSelect}
      className={`flex items-center gap-2 px-3 py-2 cursor-pointer select-none hover:bg-gray-50 ${
        isSelected ? "bg-blue-50" : ""
      }`}
    >
      <span className={`w-2 h-2 rounded-full flex-shrink-0 ${dotColor}`} />
      <span className="flex-1 text-sm text-gray-900 truncate">
        {label}
        {isServer && (
          <span className="ml-1.5 text-xs text-gray-400 font-normal">server</span>
        )}
      </span>
      <svg
        viewBox="0 0 24 24"
        fill="currentColor"
        className={`w-3.5 h-3.5 flex-shrink-0 transition-all duration-150 ${
          beat ? "text-red-500 scale-125" : "text-gray-200 scale-100"
        }`}
      >
        <title>Flashes on each received announce</title>
        <path d="M12 21s-6.7-4.34-9.33-8.2C1.02 10.3 1.52 7 4.2 5.3c2.2-1.3 4.8-.7 6.3 1.4L12 8.6l1.5-1.9c1.5-2.1 4.1-2.7 6.3-1.4 2.68 1.7 3.18 5 1.53 7.5C18.7 16.66 12 21 12 21z" />
      </svg>
      <input
        type="checkbox"
        checked={isSelected}
        onChange={onToggle}
        onClick={(e) => e.stopPropagation()}
        className="w-3.5 h-3.5 flex-shrink-0 accent-blue-600"
      />
    </div>
  );
}
