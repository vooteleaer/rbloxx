const BASE = "/api/v1";
async function req(path, options) {
    const res = await fetch(BASE + path, options);
    if (!res.ok) {
        let detail = res.statusText;
        try {
            const body = await res.json();
            if (body?.detail)
                detail = typeof body.detail === "string" ? body.detail : JSON.stringify(body.detail);
        }
        catch { /* non-JSON body */ }
        throw new Error(detail);
    }
    return res.json();
}
export const api = {
    status: () => req("/status"),
    nodes: {
        list: () => req("/nodes"),
        get: (hash) => req(`/nodes/${hash}`),
        telemetry: (hash, limit = 100, since) => req(`/nodes/${hash}/telemetry?limit=${limit}${since != null ? `&since=${since}` : ""}`),
        add: (destHash, label) => req("/nodes", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ dest_hash: destHash, label: label || null }),
        }),
        patch: (hash, label) => req(`/nodes/${hash}`, {
            method: "PATCH",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ label }),
        }),
        delete: (hash) => req(`/nodes/${hash}`, { method: "DELETE" }),
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
