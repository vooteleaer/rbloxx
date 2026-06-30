#!/bin/sh
set -e

start_rnsd() {
    echo "[rbloxx] Starting rnsd..."
    rnsd &
    RNSD_PID=$!
}

# Check for the abstract Unix socket rnsd creates when sharing.
# Format in /proc/net/unix: "@rns/<instance_name>"
rns_ready() {
    grep -q '@rns/' /proc/net/unix 2>/dev/null
}

start_rnsd

echo "[rbloxx] Waiting for rnsd shared instance..."
WAIT=0
until rns_ready; do
    sleep 1
    WAIT=$((WAIT + 1))
    if [ $WAIT -ge 120 ]; then
        echo "[rbloxx] rnsd not ready after 120s, restarting..."
        kill -9 $RNSD_PID 2>/dev/null || true
        start_rnsd
        WAIT=0
    fi
done
echo "[rbloxx] rnsd ready"

# ------------------------------------------------------------------
# Bootstrap local node agent
# Create server identity (if absent) and write agent.json pointing
# at the server's own dest hash, then start the agent in background.
# ------------------------------------------------------------------

mkdir -p /etc/rbloxx

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
        except Exception: pass
    RNS.Reticulum._used_destination_data = _safe

RNS.Reticulum(require_shared_instance=True, loglevel=0)
identity_path = Path('/etc/rbloxx/server_identity')
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
    # ------------------------------------------------------------------
    # Write a standalone Reticulum config for the agent.
    # Uses TCPClientInterface to the local rnsd instead of shared-instance
    # RPC, avoiding the multiprocessing authkey mismatch that breaks
    # _used_destination_data and causes the agent thread to go silent.
    # ------------------------------------------------------------------
    RNSD_LOCAL_PORT="${RNSD_LOCAL_PORT:-4965}"
    mkdir -p /etc/rbloxx/rns_agent
    cat > /etc/rbloxx/rns_agent/config <<EOF
[reticulum]
  enable_transport = False
  share_instance = No

[logging]
  loglevel = 4

[interfaces]

  [[local-rnsd]]
    type = TCPClientInterface
    interface_enabled = True
    target_host = 127.0.0.1
    target_port = $RNSD_LOCAL_PORT
EOF

    # Write agent.json only if absent or server_dest_hashes is empty/placeholder
    NEEDS_WRITE=1
    if [ -f /etc/rbloxx/agent.json ]; then
        if python3 -c "
import json, sys
c = json.load(open('/etc/rbloxx/agent.json'))
hashes = c.get('server_dest_hashes', [])
sys.exit(0 if hashes and hashes[0] not in ('', 'YOUR_SERVER_DEST_HASH') else 1)
" 2>/dev/null; then
            NEEDS_WRITE=0
        fi
    fi

    if [ "$NEEDS_WRITE" = "1" ]; then
        echo "[rbloxx] Writing local agent config (server hash: $SERVER_HASH)"
        cat > /etc/rbloxx/agent.json <<EOF
{
  "server_dest_hashes": ["$SERVER_HASH"],
  "identity_path": "/etc/rbloxx/agent_identity",
  "rns_configdir": "/etc/rbloxx/rns_agent",
  "announce_interval": 60
}
EOF
    else
        # Existing agent.json — ensure rns_configdir is set
        python3 -c "
import json
path = '/etc/rbloxx/agent.json'
c = json.load(open(path))
if 'rns_configdir' not in c:
    c['rns_configdir'] = '/etc/rbloxx/rns_agent'
    json.dump(c, open(path, 'w'), indent=2)
" 2>/dev/null || true
    fi

    echo "[rbloxx] Starting local node agent..."
    python3 /app/node/rbloxx_agent.py /etc/rbloxx/agent.json &
    AGENT_PID=$!
else
    echo "[rbloxx] Warning: could not compute server hash — local agent skipped"
    AGENT_PID=""
fi

# Background watchdog: restart rnsd and agent if they die
(
    while true; do
        sleep 15
        # Reap any zombie children so kill -0 reflects actual liveness
        wait -n 2>/dev/null || true
        if ! kill -0 "$RNSD_PID" 2>/dev/null || [ "$(cat /proc/$RNSD_PID/status 2>/dev/null | grep '^State:' | awk '{print $2}')" = "Z" ]; then
            echo "[rbloxx-wd] rnsd died, restarting..."
            rnsd &
            RNSD_PID=$!
            WAIT=0
            until rns_ready || [ $WAIT -ge 60 ]; do
                sleep 1; WAIT=$((WAIT + 1))
            done
            echo "[rbloxx-wd] rnsd restarted (PID $RNSD_PID)"
        fi
        if [ -n "$AGENT_PID" ] && { ! kill -0 "$AGENT_PID" 2>/dev/null || [ "$(cat /proc/$AGENT_PID/status 2>/dev/null | grep '^State:' | awk '{print $2}')" = "Z" ]; }; then
            echo "[rbloxx-wd] agent died, restarting..."
            python3 /app/node/rbloxx_agent.py /etc/rbloxx/agent.json &
            AGENT_PID=$!
            echo "[rbloxx-wd] agent restarted (PID $AGENT_PID)"
        fi
    done
) &

echo "[rbloxx] Starting RBloxx server..."
exec uvicorn main:app --host 0.0.0.0 --port 80 --workers 1
