#!/usr/bin/env python3
"""
Unauthenticated/public HTTP runtime adapter for Model B.

ASH basis:
POINT  -> configured endpoint
STATE  -> endpoint/config readiness
SKILL  -> HTTP JSON transport
ACTION -> POST frozen reviewer prompt
RESULT -> returned reviewer JSON
VERIFY -> parse + required reviewer fields
"""

import json
import os
import sys
import urllib.error
import urllib.request


def hold(reason, ash=None, code=2):
    out = {"status": "HOLD", "reason": reason}
    if ash is not None:
        out["ash"] = ash
    print(json.dumps(out, indent=2, sort_keys=True))
    raise SystemExit(code)


def main():
    endpoint = os.getenv("MODEL_B_PUBLIC_URL", "").strip()
    model = os.getenv("MODEL_B_MODEL", "").strip()

    ash = {
        "POINT": endpoint or None,
        "STATE": "INIT",
        "SKILL": "HTTP_JSON_POST",
        "ACTION": "POST_FROZEN_REVIEW_PROMPT",
        "RESULT": None,
        "VERIFY": "PENDING",
    }

    if not endpoint:
        ash["STATE"] = "BLOCKED"
        hold("missing environment variable: MODEL_B_PUBLIC_URL", ash)
    if not endpoint.startswith(("http://", "https://")):
        ash["STATE"] = "BLOCKED"
        hold("MODEL_B_PUBLIC_URL must be http:// or https://", ash)

    prompt = sys.stdin.read()
    if not prompt.strip():
        ash["STATE"] = "BLOCKED"
        hold("empty reviewer prompt", ash)

    ash["STATE"] = "READY"

    payload = {
        "prompt": prompt,
        "response_format": "json",
    }
    if model:
        payload["model"] = model

    req = urllib.request.Request(
        endpoint,
        data=json.dumps(payload).encode("utf-8"),
        headers={"Content-Type": "application/json"},
        method="POST",
    )

    ash["STATE"] = "ACTION"
    try:
        with urllib.request.urlopen(req, timeout=120) as resp:
            body = resp.read().decode("utf-8")
    except urllib.error.HTTPError as exc:
        ash["STATE"] = "RESULT"
        ash["RESULT"] = f"HTTP_{exc.code}"
        hold(f"public reviewer HTTP {exc.code}", ash)
    except Exception as exc:
        ash["STATE"] = "RESULT"
        ash["RESULT"] = "TRANSPORT_ERROR"
        hold(f"public reviewer request failed: {exc}", ash)

    ash["STATE"] = "RESULT"
    try:
        data = json.loads(body)
    except Exception as exc:
        ash["RESULT"] = "INVALID_JSON"
        hold(f"public reviewer returned invalid JSON: {exc}", ash)

    # Accept either direct reviewer JSON or a wrapper with 'result'.
    result = data.get("result") if isinstance(data, dict) and isinstance(data.get("result"), dict) else data
    if not isinstance(result, dict):
        ash["RESULT"] = "INVALID_SHAPE"
        hold("public reviewer response is not a JSON object", ash)

    required = ("status", "R", "I", "E", "K")
    missing = [k for k in required if k not in result]
    if missing:
        ash["RESULT"] = "MISSING_FIELDS"
        hold("public reviewer missing fields: " + ", ".join(missing), ash)

    if result["status"] not in ("PASS", "HOLD"):
        ash["RESULT"] = "INVALID_STATUS"
        hold("public reviewer status must be PASS or HOLD", ash)

    for key in ("R", "I", "E", "K"):
        if result[key] not in (0, 1, False, True):
            ash["RESULT"] = "INVALID_TCGE"
            hold(f"public reviewer {key} must be 0 or 1", ash)

    r = int(bool(result["R"]))
    i = int(bool(result["I"]))
    e = int(bool(result["E"]))
    expected_k = int(r and i and e)
    if int(bool(result["K"])) != expected_k:
        ash["RESULT"] = "INVALID_K"
        hold(f"public reviewer K inconsistent; expected {expected_k}", ash)

    if result["status"] == "PASS" and expected_k != 1:
        ash["RESULT"] = "PASS_WITHOUT_K"
        hold("PASS forbidden unless K=1", ash)

    ash["VERIFY"] = "PASS"
    ash["RESULT"] = result["status"]
    result["ash"] = ash
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
