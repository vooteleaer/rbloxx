#!/bin/sh
set -e

start_rnsd() {
    echo "[bloxx] Starting rnsd..."
    rnsd &
    RNSD_PID=$!
}

# Check for the abstract Unix socket rnsd creates when sharing.
# Format in /proc/net/unix: "@rns/<instance_name>"
rns_ready() {
    grep -q '@rns/' /proc/net/unix 2>/dev/null
}

start_rnsd

echo "[bloxx] Waiting for rnsd shared instance..."
WAIT=0
until rns_ready; do
    sleep 1
    WAIT=$((WAIT + 1))
    if [ $WAIT -ge 120 ]; then
        echo "[bloxx] rnsd not ready after 120s, restarting..."
        kill -9 $RNSD_PID 2>/dev/null || true
        start_rnsd
        WAIT=0
    fi
done
echo "[bloxx] rnsd ready"

# ------------------------------------------------------------------
# Bootstrap local node agent
# Create server identity (if absent) and write agent.json pointing
# at the server's own dest hash, then start the agent in background.
# ------------------------------------------------------------------

mkdir -p /etc/bloxx

SERVER_HASH=$(python3 - 2>/dev/null <<'PYEOF'
import sys, os
sys.path.insert(0, '/app/server/backend')
sys.path.insert(0, '/app/shared')
import RNS
from pathlib import Path
from protocol import APP_NAME, SERVER_ASPECT

# Suppress shared-instance RPC digest bug
if hasattr(RNS.Reticulum, "_used_destination_data"):
    _orig = RNS.Reticulum._used_destination_data
    def _safe(self, dh):
        try: _orig(self, dh)
        except (EOFError, BrokenPipeError, OSError): pass
    RNS.Reticulum._used_destination_data = _safe

RNS.Reticulum(require_shared_instance=True, loglevel=0)
identity_path = Path('/etc/bloxx/server_identity')
if identity_path.exists():
    identity = RNS.Identity.from_file(str(identity_path))
else:
    identity = RNS.Identity()
    identity.to_file(str(identity_path))
dest = RNS.Destination(identity, RNS.Destination.OUT, RNS.Destination.SINGLE, APP_NAME, SERVER_ASPECT)
print(dest.hash.hex())
PYEOF
) || SERVER_HASH=""

if [ -n "$SERVER_HASH" ]; then
    # Write agent.json only if absent or server_dest_hashes is empty/placeholder
    NEEDS_WRITE=1
    if [ -f /etc/bloxx/agent.json ]; then
        if python3 -c "
import json, sys
c = json.load(open('/etc/bloxx/agent.json'))
hashes = c.get('server_dest_hashes', [])
sys.exit(0 if hashes and hashes[0] not in ('', 'YOUR_SERVER_DEST_HASH') else 1)
" 2>/dev/null; then
            NEEDS_WRITE=0
        fi
    fi

    if [ "$NEEDS_WRITE" = "1" ]; then
        echo "[bloxx] Writing local agent config (server hash: $SERVER_HASH)"
        cat > /etc/bloxx/agent.json <<EOF
{
  "server_dest_hashes": ["$SERVER_HASH"],
  "identity_path": "/etc/bloxx/agent_identity",
  "announce_interval": 60
}
EOF
    fi

    echo "[bloxx] Starting local node agent..."
    python3 /app/node/bloxx_agent.py /etc/bloxx/agent.json &
else
    echo "[bloxx] Warning: could not compute server hash — local agent skipped"
fi

echo "[bloxx] Starting Bloxx server..."
exec uvicorn main:app --host 0.0.0.0 --port 8200 --workers 1
