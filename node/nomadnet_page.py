#!/usr/bin/env python3
"""NomadNet executable page — thin proxy to the running rbloxx-agent.

Deploy as (a symlink to) ~/.nomadnetwork/storage/pages/index.mu with the
execute bit set. NomadNet runs it as a subprocess per page request, passing
the requester's identity hash and any submitted form fields as environment
variables (its own built-in mechanism for executable pages); this just
forwards them to the agent's local socket and prints back whatever micron
text the agent renders. Stdlib-only on purpose -- no RNS/LXMF import here,
so it has nothing to break independent of the agent process itself.
"""
import json
import os
import socket
import sys

SOCKET_PATH = os.environ.get("RBLOXX_NN_SOCKET", "/run/rbloxx/nomadnet.sock")

FALLBACK = (
    b">RBloxx Node Status\n\n"
    b"Agent is not reachable right now (rbloxx-agent not running, or its "
    b"socket is missing).\n"
)


def main() -> None:
    fields = {k: v for k, v in os.environ.items() if k.startswith("field_") or k.startswith("var_")}
    request = {"remote_identity": os.environ.get("remote_identity"), "fields": fields}

    try:
        sock = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
        sock.settimeout(10)
        sock.connect(SOCKET_PATH)
        sock.sendall((json.dumps(request) + "\n").encode("utf-8"))
        sock.shutdown(socket.SHUT_WR)
        chunks = []
        while True:
            chunk = sock.recv(65536)
            if not chunk:
                break
            chunks.append(chunk)
        sock.close()
        sys.stdout.buffer.write(b"".join(chunks))
    except Exception:
        sys.stdout.buffer.write(FALLBACK)


if __name__ == "__main__":
    main()
