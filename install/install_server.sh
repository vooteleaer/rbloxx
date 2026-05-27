#!/bin/bash
set -e

BLOXX_DIR="$(cd "$(dirname "$0")/.." && pwd)"
BACKEND_DIR="$BLOXX_DIR/server/backend"
FRONTEND_DIR="$BLOXX_DIR/server/frontend"

echo "=== Bloxx server installer ==="

# Backend venv
python3 -m venv "$BACKEND_DIR/.venv"
"$BACKEND_DIR/.venv/bin/pip" install -q -r "$BACKEND_DIR/requirements.txt"

# Frontend build
cd "$FRONTEND_DIR"
npm install --silent
npm run build

mkdir -p /etc/bloxx
mkdir -p /var/lib/bloxx

# Systemd service
cat > /etc/systemd/system/bloxx-server.service << EOF
[Unit]
Description=Bloxx Server
After=network.target rnsd.service

[Service]
ExecStart=$BACKEND_DIR/.venv/bin/uvicorn main:app --host 0.0.0.0 --port 8000
Restart=on-failure
User=root
WorkingDirectory=$BACKEND_DIR
Environment=BLOXX_DB=/var/lib/bloxx/bloxx.db

[Install]
WantedBy=multi-user.target
EOF

systemctl daemon-reload
systemctl enable bloxx-server
systemctl start bloxx-server

echo ""
echo "Server running on port 8000"
echo "Server destination hash (add this to agent.json on each node):"
SERVER_DEST_HASH=$("$BACKEND_DIR/.venv/bin/python" -c "
import sys; sys.path.insert(0, '$BACKEND_DIR')
import os; os.environ.setdefault('BLOXX_DB', '/var/lib/bloxx/bloxx.db')
import rns_service, RNS
RNS.Reticulum(require_shared_instance=True)
rns_service.init()
info = rns_service.get_server_info()
print(info['dest_hash'])
" 2>/dev/null) || true

if [ -n "$SERVER_DEST_HASH" ]; then
    echo "  Destination hash: $SERVER_DEST_HASH"
    echo ""
    echo "In agent.json on each node, set:"
    echo "  \"server_dest_hashes\": [\"$SERVER_DEST_HASH\"]"
else
    echo "  (start the server to see destination hash)"
fi

# Optional: install local node agent so this server appears in the UI
echo ""
if [ "${1}" = "--with-agent" ] || { [ -t 0 ] && read -r -p "Also install local node agent on this machine? [y/N] " _reply && [[ "$_reply" =~ ^[Yy]$ ]]; }; then
    echo "Installing local node agent..."
    bash "$(dirname "$0")/install_node.sh"
    echo ""
    echo "IMPORTANT: Edit /etc/bloxx/agent.json and set:"
    if [ -n "$SERVER_DEST_HASH" ]; then
        echo "  \"server_dest_hashes\": [\"$SERVER_DEST_HASH\"]"
    else
        echo "  \"server_dest_hashes\": [\"<this server's dest_hash from above>\"]"
    fi
    echo "Then: systemctl start bloxx-agent"
fi
