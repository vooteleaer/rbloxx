import type { Node } from "../api/client";

interface Props {
  node: Node;
  isSelected: boolean;
  isServer: boolean;
  onSelect(): void;
  onToggle(): void;
}

export default function NodeSidebarItem({ node, isSelected, isServer, onSelect, onToggle }: Props) {
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
