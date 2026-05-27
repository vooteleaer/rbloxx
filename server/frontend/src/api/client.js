const BASE = "/api/v1";
async function req(path, options) {
    const res = await fetch(BASE + path, options);
    if (!res.ok)
        throw new Error(`${res.status} ${res.statusText}`);
    return res.json();
}
export const api = {
    nodes: {
        list: () => req("/nodes"),
        get: (hash) => req(`/nodes/${hash}`),
        telemetry: (hash, limit = 100) => req(`/nodes/${hash}/telemetry?limit=${limit}`),
        command: (hash, cmd) => req(`/nodes/${hash}/command`, {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify(cmd),
        }),
    },
    config: {
        pull: (hash, type) => req(`/nodes/${hash}/config/${type}`),
        snapshot: (hash, type) => req(`/nodes/${hash}/config/${type}/snapshot`),
        put: (hash, type, content) => req(`/nodes/${hash}/config/${type}`, {
            method: "PUT",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ content }),
        }),
        patch: (hash, type, patches) => req(`/nodes/${hash}/config/${type}`, {
            method: "PATCH",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ patches }),
        }),
        bulkPatch: (destHashes, type, patches) => req("/nodes/bulk/config/" + type, {
            method: "PATCH",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ dest_hashes: destHashes, patches }),
        }),
    },
};
