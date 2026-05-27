#!/bin/bash
set -e

BLOXX_DIR="$(cd "$(dirname "$0")/.." && pwd)"
NODE_DIR="$BLOXX_DIR/node"

# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------
_info()  { echo "  $*"; }
_ok()    { echo "  [ok] $*"; }
_warn()  { echo "  [!!] $*" >&2; }
_step()  { echo; echo "--- $*"; }
_ask()   { read -r -p "      $1 " "$2"; }

# ---------------------------------------------------------------------------
# Root check
# ---------------------------------------------------------------------------
if [ "$(id -u)" -ne 0 ]; then
    echo "Must run as root: sudo $0"
    exit 1
fi

# --show-hash mode: just print the hash of the existing identity and exit
if [ "${1}" = "--show-hash" ]; then
    IDENTITY_PATH=/etc/bloxx/identity
    if [ ! -f "$IDENTITY_PATH" ]; then
        echo "Identity not found at $IDENTITY_PATH — run the installer first."
        exit 1
    fi
    # Find a Python that has RNS (mirrors the main install detection)
    PYTHON=$(command -v python3 2>/dev/null || echo python3)
    if ! "$PYTHON" -c "import RNS" 2>/dev/null; then
        [ -x /opt/rns-venv/bin/python3 ] && PYTHON=/opt/rns-venv/bin/python3
    fi
    if ! "$PYTHON" -c "import RNS" 2>/dev/null; then
        _svc=$(systemctl cat rnsd.service 2>/dev/null \
            | grep -m1 '^ExecStart=' | sed 's/^ExecStart=//' | awk '{print $1}')
        if [ -n "$_svc" ] && "$_svc" -c "import RNS" 2>/dev/null; then
            PYTHON="$_svc"
        elif [ -n "$_svc" ]; then
            _interp=$(head -1 "$_svc" 2>/dev/null | sed 's|^#!||;s| .*||')
            [ -x "$_interp" ] && "$_interp" -c "import RNS" 2>/dev/null && PYTHON="$_interp"
        fi
    fi
    "$PYTHON" - << PYEOF
import RNS
RNS.Reticulum(loglevel=0)
identity = RNS.Identity.from_file('$IDENTITY_PATH')
dest = RNS.Destination(identity, RNS.Destination.IN, RNS.Destination.SINGLE, 'bloxx', 'node')
print(dest.hash.hex())
PYEOF
    exit 0
fi

echo "=== Bloxx node agent installer ==="

# ---------------------------------------------------------------------------
# [1/7] Python
# ---------------------------------------------------------------------------
_step "[1/7] Checking Python..."
if command -v python3 &>/dev/null; then
    PYTHON=$(command -v python3)
    _ok "python3 at $PYTHON  ($(python3 --version 2>&1))"
else
    _warn "python3 not found — installing via apt"
    apt-get update -qq
    apt-get install -y -qq python3 python3-pip
    PYTHON=$(command -v python3)
    _ok "python3 installed at $PYTHON"
fi

# ---------------------------------------------------------------------------
# [2/7] Reticulum (RNS + rnodeconf)
# ---------------------------------------------------------------------------
_step "[2/7] Installing Reticulum Network Stack..."

# Given a binary path, return the Python interpreter from its shebang
_python_from_shebang() {
    local bin="$1"
    local interp
    interp=$(head -1 "$bin" 2>/dev/null | sed 's|^#!||;s| .*||')
    [ -x "$interp" ] && echo "$interp"
}

# Try to find Python that already has RNS — check in priority order:
#   1. system python3 directly
#   2. ExecStart of existing rnsd.service (handles venv installs with systemd)
#   3. rnsd binary in PATH (shebang)
_find_rns_python() {
    # 1. system python already works
    "$PYTHON" -c "import RNS" 2>/dev/null && echo "$PYTHON" && return

    # 2. existing rnsd.service — extract the executable from ExecStart
    local svc_exec
    svc_exec=$(systemctl cat rnsd.service 2>/dev/null \
        | grep -m1 '^ExecStart=' | sed 's/^ExecStart=//' | awk '{print $1}')
    if [ -n "$svc_exec" ] && [ -x "$svc_exec" ]; then
        # ExecStart might be rnsd directly or a python interpreter
        local candidate
        if "$svc_exec" -c "import RNS" 2>/dev/null; then
            echo "$svc_exec" && return       # ExecStart is the python binary
        fi
        candidate=$(_python_from_shebang "$svc_exec")
        if [ -n "$candidate" ] && "$candidate" -c "import RNS" 2>/dev/null; then
            echo "$candidate" && return      # shebang in the rnsd script
        fi
    fi

    # 3. rnsd in PATH
    local rnsd_path
    rnsd_path=$(command -v rnsd 2>/dev/null)
    if [ -n "$rnsd_path" ]; then
        local candidate
        candidate=$(_python_from_shebang "$rnsd_path")
        if [ -n "$candidate" ] && "$candidate" -c "import RNS" 2>/dev/null; then
            echo "$candidate" && return
        fi
    fi
}

_RNS_PYTHON=$(_find_rns_python)

if [ -n "$_RNS_PYTHON" ]; then
    PYTHON="$_RNS_PYTHON"
    _ok "RNS already installed  ($("$PYTHON" -c "import RNS; print(RNS.__version__)" 2>/dev/null))  [$PYTHON]"
else
    # Try to install — handle externally-managed-environment (PEP 668)
    _pip_install() {
        "$PYTHON" -m pip install --quiet "$@" 2>/dev/null && return 0
        "$PYTHON" -m pip install --quiet --break-system-packages "$@" 2>/dev/null && return 0
        return 1
    }
    if _pip_install rns; then
        _ok "RNS installed"
    else
        # Fall back: create a venv and install there
        _warn "pip install failed (externally managed env) — creating venv at /opt/rns-venv"
        apt-get install -y -qq python3-venv 2>/dev/null || true
        python3 -m venv /opt/rns-venv
        PYTHON=/opt/rns-venv/bin/python3
        "$PYTHON" -m pip install --quiet rns
        _ok "RNS installed in /opt/rns-venv"
    fi
fi

# Optional: smbus2 for I²C battery monitoring
if ! "$PYTHON" -c "import smbus2" 2>/dev/null; then
    "$PYTHON" -m pip install --quiet smbus2 2>/dev/null \
        || "$PYTHON" -m pip install --quiet --break-system-packages smbus2 2>/dev/null \
        || _warn "smbus2 install failed — I²C battery monitoring unavailable"
fi

# Locate binaries — prefer ones that match our chosen $PYTHON's venv
_find_bin() {
    local name="$1"
    local found
    # Check venv bin dir first (same dir as $PYTHON)
    local venv_bin
    venv_bin="$(dirname "$PYTHON")/$name"
    [ -x "$venv_bin" ] && { echo "$venv_bin"; return; }
    found=$(command -v "$name" 2>/dev/null) && { echo "$found"; return; }
    "$PYTHON" -c "import sysconfig; print(sysconfig.get_path('scripts')+'/$name')" 2>/dev/null \
        || echo "$name"
}
RNSD=$(_find_bin rnsd)
RNODECONF=$(_find_bin rnodeconf)
_ok "rnsd: $RNSD"

# ---------------------------------------------------------------------------
# [3/7] Serial port / RNode detection
# ---------------------------------------------------------------------------
_step "[3/7] Scanning serial ports for RNode hardware..."

RNODE_PORT=""
FOUND_PORTS=()

for pat in /dev/ttyUSB* /dev/ttyACM* /dev/ttyS0 /dev/ttyS1 /dev/ttyS2 /dev/ttyS3; do
    [ -c "$pat" ] && FOUND_PORTS+=("$pat")
done

if [ ${#FOUND_PORTS[@]} -eq 0 ]; then
    _warn "No serial ports found — skipping RNode setup"
else
    _info "Ports found: ${FOUND_PORTS[*]}"

    if [ -x "$RNODECONF" ] || command -v "$RNODECONF" &>/dev/null; then
        for port in "${FOUND_PORTS[@]}"; do
            _info "Probing $port ..."
            if timeout 5 "$RNODECONF" "$port" --info &>/dev/null 2>&1; then
                RNODE_PORT="$port"
                _ok "RNode detected on $port"
                break
            fi
        done
    fi

    if [ -z "$RNODE_PORT" ]; then
        _warn "Could not auto-detect RNode via rnodeconf"
        if [ -t 0 ]; then
            echo
            echo "      Available ports:"
            for i in "${!FOUND_PORTS[@]}"; do
                echo "        $((i+1))) ${FOUND_PORTS[$i]}"
            done
            echo "        0) None / skip"
            _ask "Select port number [0]:" _pidx
            if [ -n "$_pidx" ] && [ "$_pidx" -gt 0 ] 2>/dev/null; then
                RNODE_PORT="${FOUND_PORTS[$((_pidx-1))]}"
                _ok "Selected: $RNODE_PORT"
            fi
        fi
    fi
fi

# ---------------------------------------------------------------------------
# [4/7] Reticulum config
# ---------------------------------------------------------------------------
_step "[4/7] Configuring Reticulum..."

RNS_CFG_DIR="/root/.reticulum"
RNS_CFG_FILE="$RNS_CFG_DIR/config"

if [ -f "$RNS_CFG_FILE" ]; then
    _ok "RNS config already exists at $RNS_CFG_FILE — leaving untouched"
else
    mkdir -p "$RNS_CFG_DIR"
    IFACE_BLOCK=""

    if [ -n "$RNODE_PORT" ]; then
        echo
        echo "      RNode frequency band:"
        echo "        1) EU 433 MHz  (433.175 MHz)"
        echo "        2) EU 868 MHz  (869.525 MHz)  ← default"
        echo "        3) US 915 MHz  (915.000 MHz)"
        echo "        4) 2.4 GHz     (2400.000 MHz)"
        if [ -t 0 ]; then
            _ask "Band [2]:" _band
        fi
        case "${_band:-2}" in
            1) FREQ=433175000  ;;
            3) FREQ=915000000  ;;
            4) FREQ=2400000000 ;;
            *)  FREQ=869525000 ;;
        esac

        IFACE_BLOCK="
[[RNode]]
  type = RNodeInterface
  enabled = yes
  port = $RNODE_PORT
  frequency = $FREQ
  bandwidth = 125000
  txpower = 14
  spreadingfactor = 7
  codingrate = 5
"
    fi

    cat > "$RNS_CFG_FILE" << EOF
[reticulum]
  enable_transport = yes
  share_instance = yes
  shared_instance_expiry = 1800
  use_implicit_proof = yes
  panic_on_interface_error = no

[logging]
  loglevel = 4
$IFACE_BLOCK
EOF
    _ok "RNS config written to $RNS_CFG_FILE"
fi

# ---------------------------------------------------------------------------
# Raspberry Pi tweaks (serial console + watchdog)
# ---------------------------------------------------------------------------
if grep -q "Raspberry Pi" /proc/cpuinfo 2>/dev/null; then

    # Disable serial console — it conflicts with ttyAMA0/ttyS0 RNode connections.
    # Remove console=serial0,... and console=ttyAMA0,... from boot cmdline.
    _CMDLINE=""
    [ -f /boot/firmware/cmdline.txt ] && _CMDLINE=/boot/firmware/cmdline.txt
    [ -f /boot/cmdline.txt ]          && _CMDLINE=/boot/cmdline.txt

    if [ -n "$_CMDLINE" ]; then
        _orig=$(cat "$_CMDLINE")
        _new=$(echo "$_orig" \
            | sed 's/console=serial0,[0-9]*\s*//g' \
            | sed 's/console=ttyAMA0,[0-9]*\s*//g' \
            | sed 's/console=ttyS0,[0-9]*\s*//g' \
            | sed 's/  */ /g' | sed 's/^ //;s/ $//')
        if [ "$_orig" != "$_new" ]; then
            echo "$_new" > "$_CMDLINE"
            _ok "Removed serial console from $_CMDLINE (reboot required)"
        else
            _ok "Serial console already disabled in $_CMDLINE"
        fi
        # Also disable the getty service if present
        systemctl disable --quiet serial-getty@ttyAMA0.service 2>/dev/null || true
        systemctl disable --quiet serial-getty@serial0.service  2>/dev/null || true
        systemctl stop    --quiet serial-getty@ttyAMA0.service 2>/dev/null || true
        systemctl stop    --quiet serial-getty@serial0.service  2>/dev/null || true
    fi

    # Hardware watchdog
    _BOOT=""
    [ -f /boot/firmware/config.txt ] && _BOOT=/boot/firmware/config.txt
    [ -f /boot/config.txt ]          && _BOOT=/boot/config.txt
    if [ -n "$_BOOT" ] && ! grep -q "dtparam=watchdog=on" "$_BOOT"; then
        echo "dtparam=watchdog=on" >> "$_BOOT"
        _ok "Enabled hardware watchdog in $_BOOT (reboot required)"
    fi
fi

# ---------------------------------------------------------------------------
# [5/7] Create node identity
# ---------------------------------------------------------------------------
_step "[5/7] Creating node identity..."

mkdir -p /etc/bloxx

if [ -f /etc/bloxx/identity ]; then
    _ok "Identity already exists at /etc/bloxx/identity"
else
    "$PYTHON" - << PYEOF
import RNS, os
os.makedirs('/etc/bloxx', exist_ok=True)
identity = RNS.Identity()
identity.to_file('/etc/bloxx/identity')
print("  [ok] Identity created  (hash: " + identity.hash.hex() + ")")
PYEOF
fi

# (DEST_HASH computed after rnsd starts in step 7)

# ---------------------------------------------------------------------------
# [6/7] Systemd services
# ---------------------------------------------------------------------------
_step "[6/7] Setting up systemd services..."

# rnsd
if [ ! -f /etc/systemd/system/rnsd.service ]; then
    cat > /etc/systemd/system/rnsd.service << EOF
[Unit]
Description=Reticulum Network Stack daemon
After=network.target

[Service]
ExecStart=$RNSD
Restart=on-failure
RestartSec=5
User=root

[Install]
WantedBy=multi-user.target
EOF
    _ok "Created rnsd.service"
else
    _ok "rnsd.service already exists"
fi

# agent.json
if [ ! -f /etc/bloxx/agent.json ]; then
    SERVER_HASH=""
    if [ -t 0 ]; then
        echo
        _ask "Server destination hash (leave blank to fill in later):" SERVER_HASH
    fi
    SERVER_HASH="${SERVER_HASH:-PASTE_SERVER_DEST_HASH_HERE}"

    if [ -n "$RNODE_PORT" ]; then
        RNODE_PORTS_JSON="\"$RNODE_PORT\""
    else
        RNODE_PORTS_JSON=""
    fi

    cat > /etc/bloxx/agent.json << EOF
{
  "identity_path": "/etc/bloxx/identity",
  "announce_interval": 300,
  "server_dest_hashes": ["$SERVER_HASH"],
  "rnode_ports": [$RNODE_PORTS_JSON],
  "shutdown_soc_pct": 0,
  "watchdog_feed_interval_s": 10
}
EOF
    _ok "Created /etc/bloxx/agent.json"
else
    _ok "/etc/bloxx/agent.json already exists"
fi

# bloxx-agent
if [ ! -f /etc/systemd/system/bloxx-agent.service ]; then
    cat > /etc/systemd/system/bloxx-agent.service << EOF
[Unit]
Description=Bloxx Node Agent
After=network.target rnsd.service
Wants=rnsd.service

[Service]
ExecStart=$PYTHON $NODE_DIR/bloxx_agent.py /etc/bloxx/agent.json
Restart=on-failure
RestartSec=10
User=root
WorkingDirectory=$NODE_DIR

[Install]
WantedBy=multi-user.target
EOF
    _ok "Created bloxx-agent.service"
else
    _ok "bloxx-agent.service already exists"
fi

# ---------------------------------------------------------------------------
# [7/7] Start services
# ---------------------------------------------------------------------------
_step "[7/7] Starting services..."

systemctl daemon-reload
systemctl enable rnsd        --quiet
systemctl restart rnsd
_ok "rnsd running"
sleep 3
systemctl enable bloxx-agent --quiet
systemctl restart bloxx-agent
_ok "bloxx-agent running"

# Compute destination hash now that rnsd shared instance is up
DEST_HASH=$("$PYTHON" - << PYEOF 2>/dev/null || true
import RNS
RNS.Reticulum(loglevel=0)
identity = RNS.Identity.from_file('/etc/bloxx/identity')
dest = RNS.Destination(identity, RNS.Destination.IN, RNS.Destination.SINGLE, 'bloxx', 'node')
print(dest.hash.hex())
PYEOF
)

# ---------------------------------------------------------------------------
# Done
# ---------------------------------------------------------------------------
echo
echo "============================================================"
echo " Node configured!"
echo "============================================================"
if [ -n "$DEST_HASH" ]; then
    echo ""
    echo "  Destination hash:"
    echo ""
    echo "    $DEST_HASH"
    echo ""
    echo "  Open your RBloxx server, click '+ Add node',"
    echo "  and paste this hash."
else
    echo ""
    echo "  Could not compute destination hash."
    echo "  Once services are running, re-run:  sudo $0 --show-hash"
fi
if grep -q "Raspberry Pi" /proc/cpuinfo 2>/dev/null; then
    echo ""
    echo "  NOTE: A reboot is required to apply serial console and"
    echo "  watchdog changes."
fi
echo "============================================================"
