# Stage 1: Build React frontend
FROM node:20-alpine AS frontend-builder
WORKDIR /build
COPY server/frontend/package*.json ./
RUN npm ci --silent
COPY server/frontend/ ./
RUN npm run build

# Stage 2: Runtime (rnsd + uvicorn)
FROM debian:bookworm-slim

RUN apt-get update && apt-get install -y --no-install-recommends \
        python3 \
        python3-pip \
        gcc \
        libffi-dev \
        procps \
        ca-certificates \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app/server/backend

# Install Python dependencies first (cache layer)
COPY server/backend/requirements.txt ./
RUN pip3 install --no-cache-dir --break-system-packages -r requirements.txt

# Copy shared protocol module (must be at /app/shared/ so rns_service.py's
# sys.path.insert(0, ...parent.parent.parent/shared) resolves correctly)
COPY shared/ /app/shared/

# Copy node agent (runs inside container as the local "Server" node)
COPY node/ /app/node/

# Copy backend source
COPY server/backend/ ./

# Copy built frontend into backend/dist (where main.py serves it from)
COPY --from=frontend-builder /build/dist/ ./dist/

COPY server/entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

# /etc/bloxx   — server RNS identity (must survive restarts)
# /var/lib/bloxx — SQLite database
# /root/.reticulum — RNS config and transport data
VOLUME ["/etc/bloxx", "/var/lib/bloxx", "/root/.reticulum"]

EXPOSE 8200

ENV BLOXX_DB=/var/lib/bloxx/bloxx.db

ENTRYPOINT ["/entrypoint.sh"]
