#!/usr/bin/env python3
"""
One-off migration: append AutoInterface + TCP server blocks to the RNS config
on all known nodes via the RBloxx server API.

Usage:
  python scripts/add_interfaces.py [SERVER_URL]

SERVER_URL defaults to http://localhost
"""

import sys
import urllib.request
import urllib.error
import json

SERVER = sys.argv[1].rstrip("/") if len(sys.argv) > 1 else "http://localhost"

NEW_BLOCKS = """
[AutoInterface]
  type = AutoInterface
  interface_enabled = True
  group_id = rbloxx

[[rns.beleth.net]]
  type = TCPClientInterface
  interface_enabled = True
  target_host = rns.beleth.net
  target_port = 4242

[[London]]
  type = TCPClientInterface
  interface_enabled = True
  target_host = 132.145.75.143
  target_port = 4242
"""

MARKERS = ["AutoInterface", "rns.beleth.net", "London"]


def api(path, method="GET", body=None):
    url = SERVER + path
    data = json.dumps(body).encode() if body is not None else None
    req = urllib.request.Request(url, data=data, method=method,
                                 headers={"Content-Type": "application/json"})
    with urllib.request.urlopen(req, timeout=30) as r:
        return json.loads(r.read())


def needs_update(config_text):
    return not any(m in config_text for m in MARKERS)


def update_node(dest_hash, hostname):
    label = hostname or dest_hash[:12]
    try:
        snap = api(f"/api/v1/nodes/{dest_hash}/config/rns/snapshot")
        content = snap["content"]
        source = "snapshot"
    except urllib.error.HTTPError as e:
        if e.code == 404:
            try:
                pulled = api(f"/api/v1/nodes/{dest_hash}/config/rns")
                content = pulled["content"]
                source = "node"
            except Exception as ex:
                print(f"  SKIP {label}: could not get config — {ex}")
                return
        else:
            print(f"  SKIP {label}: HTTP {e.code}")
            return

    if not needs_update(content):
        print(f"  OK   {label}: already up to date (via {source})")
        return

    updated = content.rstrip() + "\n" + NEW_BLOCKS
    try:
        api(f"/api/v1/nodes/{dest_hash}/config/rns", method="PUT", body={"content": updated})
        print(f"  DONE {label}: pushed updated config (via {source})")
    except Exception as ex:
        print(f"  FAIL {label}: push failed — {ex}")


def main():
    print(f"Connecting to {SERVER} …")
    nodes = api("/api/v1/nodes")
    print(f"Found {len(nodes)} node(s)\n")
    for node in nodes:
        update_node(node["dest_hash"], node.get("hostname") or node.get("label"))
    print("\nDone.")


if __name__ == "__main__":
    main()
