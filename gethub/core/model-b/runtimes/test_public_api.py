#!/usr/bin/env python3
import json
import os
import subprocess
import sys
import tempfile
import threading
from http.server import BaseHTTPRequestHandler, HTTPServer
from pathlib import Path

HERE = Path(__file__).resolve().parent
ADAPTER = HERE / "public_api.py"

class Handler(BaseHTTPRequestHandler):
    response = {
        "status": "PASS",
        "findings": [],
        "R": 1,
        "I": 1,
        "E": 1,
        "K": 1,
    }

    def do_POST(self):
        length = int(self.headers.get("Content-Length", "0"))
        body = self.rfile.read(length)
        req = json.loads(body.decode("utf-8"))
        assert "prompt" in req
        encoded = json.dumps(self.response).encode("utf-8")
        self.send_response(200)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(encoded)))
        self.end_headers()
        self.wfile.write(encoded)

    def log_message(self, *_):
        pass

def run_adapter(url, prompt="ASH TEST"):
    env = os.environ.copy()
    env["MODEL_B_PUBLIC_URL"] = url
    env["MODEL_B_MODEL"] = "public-test-model"
    return subprocess.run(
        [sys.executable, str(ADAPTER)],
        input=prompt,
        text=True,
        capture_output=True,
        env=env,
    )

def main():
    server = HTTPServer(("127.0.0.1", 0), Handler)
    thread = threading.Thread(target=server.serve_forever, daemon=True)
    thread.start()
    try:
        url = f"http://127.0.0.1:{server.server_port}/review"
        result = run_adapter(url)
        assert result.returncode == 0, result.stdout + result.stderr
        data = json.loads(result.stdout)
        assert data["status"] == "PASS"
        assert data["K"] == 1
        assert data["ash"]["POINT"] == url
        assert data["ash"]["STATE"] == "RESULT"
        assert data["ash"]["SKILL"] == "HTTP_JSON_POST"
        assert data["ash"]["ACTION"] == "POST_FROZEN_REVIEW_PROMPT"
        assert data["ash"]["RESULT"] == "PASS"
        assert data["ash"]["VERIFY"] == "PASS"

        Handler.response = {
            "status": "PASS",
            "findings": [],
            "R": 1,
            "I": 1,
            "E": 0,
            "K": 0,
        }
        result2 = run_adapter(url)
        assert result2.returncode != 0
        data2 = json.loads(result2.stdout)
        assert data2["status"] == "HOLD"
        assert "PASS forbidden" in data2["reason"]

        print("PASS: public API adapter transport, ASH state chain, and TCGE fail-closed checks")
    finally:
        server.shutdown()

if __name__ == "__main__":
    main()
