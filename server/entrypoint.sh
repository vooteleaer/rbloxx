#!/bin/sh
set -e

start_rnsd() {
    echo "[bloxx] Starting rnsd..."
    rnsd &
    RNSD_PID=$!
}

start_rnsd

echo "[bloxx] Waiting for rnsd shared instance..."
WAIT=0
until rnstatus >/dev/null 2>&1; do
    sleep 1
    WAIT=$((WAIT + 1))
    if [ $WAIT -ge 60 ]; then
        echo "[bloxx] rnsd not ready after 60s, restarting..."
        kill $RNSD_PID 2>/dev/null || true
        wait $RNSD_PID 2>/dev/null || true
        start_rnsd
        WAIT=0
    fi
done
echo "[bloxx] rnsd ready"

echo "[bloxx] Starting Bloxx server..."
exec uvicorn main:app --host 0.0.0.0 --port 8200 --workers 1
