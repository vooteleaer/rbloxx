import paramiko, time
from pathlib import Path

HOST = "192.168.4.1"
USER = "reticulum"
PASS = "reticulum"
REMOTE_DIR = "/home/reticulum/bloxx"
BASE = Path(__file__).parent

files = [
    (BASE / "node" / "bloxx_agent.py",     f"{REMOTE_DIR}/bloxx_agent.py"),
    (BASE / "node" / "config_handler.py",  f"{REMOTE_DIR}/config_handler.py"),
    (BASE / "node" / "system_handler.py",  f"{REMOTE_DIR}/system_handler.py"),
    (BASE / "node" / "power_handler.py",   f"{REMOTE_DIR}/power_handler.py"),
    (BASE / "shared" / "protocol.py",      f"{REMOTE_DIR}/protocol.py"),
    (BASE / "node" / "agent.json.example", f"{REMOTE_DIR}/agent.json.example"),
]

client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
client.connect(HOST, username=USER, password=PASS, timeout=10)
client.exec_command(f"mkdir -p {REMOTE_DIR}")
time.sleep(0.5)

sftp = client.open_sftp()
for local, remote in files:
    sftp.put(str(local), remote)
    print(f"  {local.name} -> {remote}")

sftp.close()
client.close()
print("Done.")
