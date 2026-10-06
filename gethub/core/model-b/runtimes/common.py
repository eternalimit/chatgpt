#!/usr/bin/env python3
import json
import os
import re
import sys
import urllib.error
import urllib.request


def hold(reason, code=2):
    print(json.dumps({"status": "HOLD", "reason": reason}, indent=2))
    raise SystemExit(code)


def require(name):
    value = os.getenv(name)
    if not value:
        hold(f"missing environment variable: {name}")
    return value


def read_prompt():
    data = sys.stdin.read()
    if not data.strip():
        hold("empty reviewer prompt")
    return data


def http_json(url, payload, headers=None, timeout=120):
    body = json.dumps(payload).encode("utf-8")
    h = {"Content-Type": "application/json"}
    if headers:
        h.update(headers)
    req = urllib.request.Request(url, data=body, headers=h, method="POST")
    try:
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            return json.loads(resp.read().decode("utf-8"))
    except urllib.error.HTTPError as exc:
        detail = exc.read().decode("utf-8", "replace")[:1000]
        hold(f"reviewer HTTP {exc.code}: {detail}")
    except Exception as exc:
        hold(f"reviewer request failed: {exc}")


def extract_json(text):
    if isinstance(text, dict):
        return text
    if not isinstance(text, str):
        hold("reviewer returned non-text content")
    text = text.strip()
    try:
        return json.loads(text)
    except Exception:
        pass
    m = re.search(r"\{.*\}", text, flags=re.S)
    if not m:
        hold("reviewer response contained no JSON object")
    try:
        return json.loads(m.group(0))
    except Exception as exc:
        hold(f"reviewer JSON parse failed: {exc}")


def emit(result):
    print(json.dumps(result, indent=2, sort_keys=True))
