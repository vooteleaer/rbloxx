const BASE = "/api/v1";

async function req<T>(path: string, options?: RequestInit): Promise<T> {
  const res = await fetch(BASE + path, options);
  if (!res.ok) throw new Error(`${res.status} ${res.statusText}`);
  return res.json();
}

export const api = {
  status: () => req<Record<string, unknown>>("/status"),
  nodes: {
    list: () => req<Node[]>("/nodes"),
    get: (hash: string) => req<Node>(`/nodes/${hash}`),
    telemetry: (hash: string, limit = 100) =>
      req<TelemetryRow[]>(`/nodes/${hash}/telemetry?limit=${limit}`),
    add: (destHash: string, label?: string) =>
      req<Node>("/nodes", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ dest_hash: destHash, label: label || null }),
      }),
    patch: (hash: string, label: string | null) =>
      req<Node>(`/nodes/${hash}`, {
        method: "PATCH",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ label }),
      }),
    delete: (hash: string) =>
      req<{ ok: boolean }>(`/nodes/${hash}`, { method: "DELETE" }),
    command: (hash: string, cmd: Record<string, unknown>) =>
      req<CommandResult>(`/nodes/${hash}/command`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(cmd),
      }),
  },
  config: {
    pull: (hash: string, type: string) =>
      req<{ cfg_type: string; content: string }>(`/nodes/${hash}/config/${type}`),
    snapshot: (hash: string, type: string) =>
      req<{ content: string; ts: number }>(`/nodes/${hash}/config/${type}/snapshot`),
    put: (hash: string, type: string, content: string) =>
      req<CommandResult>(`/nodes/${hash}/config/${type}`, {
        method: "PUT",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ content }),
      }),
    patch: (hash: string, type: string, patches: Patch[]) =>
      req<CommandResult>(`/nodes/${hash}/config/${type}`, {
        method: "PATCH",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ patches }),
      }),
    bulkPatch: (destHashes: string[], type: string, patches: Patch[]) =>
      req<Record<string, CommandResult>>("/nodes/bulk/config/" + type, {
        method: "PATCH",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ dest_hashes: destHashes, patches }),
      }),
  },
};

export interface Node {
  dest_hash: string;
  identity_hash: string | null;
  label: string | null;
  hostname: string | null;
  version: string | null;
  first_seen: number;
  last_seen: number;
  online: boolean;
  last_errors: string[];
}

export interface TelemetryRow {
  ts: number;
  cpu_pct: number | null;
  ram_pct: number | null;
  disk_pct: number | null;
  temp_c: number | null;
  batt_soc_pct: number | null;
  batt_voltage_v: number | null;
  batt_power_w: number | null;
  solar_power_w: number | null;
  rns_rtt_ms: number | null;
  rns_rxb: number | null;
  rns_txb: number | null;
  rnode_airtime_short: number | null;
  rnode_airtime_long: number | null;
  rnode_channel_load_short: number | null;
  rnode_channel_load_long: number | null;
  rnode_bitrate: number | null;
  rnode_noise_floor: number | null;
  rnode_interference_dbm: number | null;
  rnode_announce_in: number | null;
  rnode_announce_out: number | null;
  rnode_held_announces: number | null;
  errors: string[];
}

export interface Patch {
  section: string;
  key: string;
  value: string;
}

export interface CommandResult {
  ok: boolean;
  error?: string;
  output?: string;
  status?: string;
}
