# RBloxx

Remote administration system for a fleet of [Reticulum](https://reticulum.network) nodes.

- **Node agent** — runs on each device alongside `rnsd`; sends telemetry, accepts commands over RNS
- **Server** — FastAPI backend + React UI; receives telemetry, manages config, pushes commands
- **All traffic over Reticulum** — works over LoRa (RNode), TCP, or any RNS interface; no separate cloud dependency

---

## Server

The server image is published to Docker Hub. You only need the `docker-compose.yml` — no build step required.

```bash
# Download just the compose file
curl -O https://raw.githubusercontent.com/vooteleaer/rbloxx/main/server/docker-compose.yml

# Start (pulls image automatically)
docker compose up -d
```

The server destination hash is shown in the container log on first start:

```bash
docker logs server-rbloxx-1 | grep "dest"
```

Open `http://server-ip:8200` in a browser.

---

## Node

Run on each device you want to manage (Raspberry Pi or any Linux machine with Python 3):

```bash
git clone https://github.com/vooteleaer/rbloxx
cd rbloxx
sudo bash install/install_node.sh
```

The script will:
1. Install Python 3 if missing
2. Install Reticulum (`rns` + `rnodeconf`)
3. Probe serial ports (`ttyUSB*`, `ttyACM*`, `ttyS*`) and auto-detect RNode hardware
4. Ask for the RNode frequency band if an RNode is found
5. Write `/root/.reticulum/config` with the detected interface
6. On Raspberry Pi: disable the serial console (frees up `ttyAMA0`/`serial0` for RNode) and enable the hardware watchdog
7. Create the node identity at `/etc/bloxx/identity`
8. Set up and start `rnsd` and `bloxx-agent` systemd services
9. Print the **node destination hash** — paste this into the RBloxx server UI

### Adding the node to the server

1. Open the RBloxx web UI
2. Click **+ Add node** in the sidebar
3. Paste the destination hash printed by the install script

The node will appear as offline until it connects. Once `rnsd` on the node finds a path to the server, the agent pushes telemetry and the node goes online.

### Show the hash again later

```bash
sudo bash install/install_node.sh --show-hash
```

### Set the server destination hash

Edit `/etc/bloxx/agent.json` and fill in `server_dest_hashes`:

```json
{
  "server_dest_hashes": ["PASTE_SERVER_DEST_HASH_HERE"],
  ...
}
```

Then restart the agent:
```bash
sudo systemctl restart bloxx-agent
```

---

## Project layout

```
rbloxx/
├── node/               Node agent (Python)
│   ├── bloxx_agent.py
│   ├── config_handler.py
│   ├── power_handler.py
│   └── system_handler.py
├── server/
│   ├── backend/        FastAPI backend
│   ├── frontend/       React + Vite + Tailwind UI
│   ├── Dockerfile
│   ├── docker-compose.yml
│   └── entrypoint.sh
├── shared/             Protocol constants (used by both node and server)
│   └── protocol.py
└── install/
    ├── install_server.sh   Server setup (optional, Docker is preferred)
    └── install_node.sh     Node setup wizard
```

---

## Development

**Backend:**
```bash
cd server/backend
python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
uvicorn main:app --reload --port 8200
```

**Frontend:**
```bash
cd server/frontend
npm install
npm run dev   # proxies /api to localhost:8200
```
