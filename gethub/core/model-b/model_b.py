#!/usr/bin/env python3
import argparse
import json
import os
import subprocess
from pathlib import Path

REQUIRED_TOP = {
    "source_evidence",
    "candidate_artifact",
    "frozen_rules",
    "primary_model_identity",
    "reviewer_model_identity",
}


def fail(msg, code=2):
    print(json.dumps({"status": "HOLD", "reason": msg}, indent=2))
    raise SystemExit(code)


def validate_packet(packet):
    missing = sorted(REQUIRED_TOP - set(packet))
    if missing:
        fail("missing required inputs: " + ", ".join(missing))
    p = str(packet["primary_model_identity"]).strip()
    r = str(packet["reviewer_model_identity"]).strip()
    if not p or not r:
        fail("model identities must be non-empty")
    if p.casefold() == r.casefold():
        fail("reviewer is not independent from primary model")


def build_prompt(packet):
    instructions = (
        "You are Model B, an independent reviewer.\n\n"
        "Do not redesign, repair, guess, or average disagreement. "
        "Audit the candidate only against the supplied source evidence and frozen rules. "
        "Return strict JSON with keys status, findings, R, I, E, K. "
        "status must be PASS or HOLD. Every HOLD finding must include location, error_type, "
        "source_conflict, required_correction. E may be 1 only if this review runtime is "
        "meaningfully independent from the primary runtime. K = R AND I AND E.\n\n"
    )
    return instructions + json.dumps(packet, indent=2, sort_keys=True)


def run_external(command, prompt):
    proc = subprocess.run(
        command,
        input=prompt.encode("utf-8"),
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        shell=True,
        check=False,
    )
    if proc.returncode != 0:
        fail("external reviewer failed: " + proc.stderr.decode("utf-8", "replace")[:500])
    try:
        return json.loads(proc.stdout.decode("utf-8"))
    except Exception as exc:
        fail(f"reviewer returned invalid JSON: {exc}")


def validate_result(result):
    if result.get("status") not in {"PASS", "HOLD"}:
        fail("reviewer status must be PASS or HOLD")
    for key in ("R", "I", "E", "K"):
        if result.get(key) not in (0, 1, False, True):
            fail(f"reviewer {key} must be 0 or 1")
    r, i, e = map(lambda k: int(bool(result[k])), ("R", "I", "E"))
    expected_k = int(r and i and e)
    if int(bool(result["K"])) != expected_k:
        fail(f"reviewer K inconsistent; expected {expected_k}")
    if result["status"] == "PASS" and expected_k != 1:
        fail("PASS is forbidden unless TCGE K=1")
    return result


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("packet", help="JSON review packet")
    ap.add_argument("--reviewer-cmd", default=os.getenv("MODEL_B_REVIEWER_CMD"))
    ap.add_argument("--prompt-out", help="write frozen prompt and stop")
    args = ap.parse_args()

    packet = json.loads(Path(args.packet).read_text(encoding="utf-8"))
    validate_packet(packet)
    prompt = build_prompt(packet)

    if args.prompt_out:
        Path(args.prompt_out).write_text(prompt, encoding="utf-8")
        print(json.dumps({"status": "HOLD", "reason": "prompt frozen; independent reviewer not executed"}, indent=2))
        return 0

    if not args.reviewer_cmd:
        fail("no independent reviewer runtime configured; set MODEL_B_REVIEWER_CMD")

    result = validate_result(run_external(args.reviewer_cmd, prompt))
    print(json.dumps(result, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
