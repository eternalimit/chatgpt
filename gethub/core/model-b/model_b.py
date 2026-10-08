#!/usr/bin/env python3
import argparse
import json
import os
import shlex
import subprocess
import sys
from pathlib import Path

REQUIRED_TOP = {
    "source_evidence",
    "candidate_artifact",
    "frozen_rules",
    "primary_model_identity",
    "reviewer_model_identity",
}

REMOTE_ECHO_RUNTIMES = {"anthropic", "gemini", "huggingface"}
KNOWN_RUNTIMES = REMOTE_ECHO_RUNTIMES | {
    "openai-compatible",
    "ollama",
    "lmstudio",
    "llamacpp",
}


def fail(msg, code=2, **extra):
    out = {"status": "HOLD", "reason": msg}
    out.update(extra)
    print(json.dumps(out, indent=2, sort_keys=True))
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
        "source_conflict, required_correction. E is your review judgment only; the GETHUB "
        "harness independently decides whether the runtime is eligible to count as Echo. "
        "K = R AND I AND E.\n\n"
    )
    return instructions + json.dumps(packet, indent=2, sort_keys=True)


def run_external(argv, prompt):
    proc = subprocess.run(
        argv,
        input=prompt.encode("utf-8"),
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        shell=False,
        check=False,
    )
    if proc.returncode != 0:
        fail("external reviewer failed: " + proc.stderr.decode("utf-8", "replace")[:500])
    try:
        return json.loads(proc.stdout.decode("utf-8"))
    except Exception as exc:
        fail(f"reviewer returned invalid JSON: {exc}")


def runtime_command(runtime):
    selector = Path(__file__).resolve().parent / "runtimes" / "runtime_selector.py"
    return [sys.executable, str(selector), runtime]


def validate_runtime_binding(packet, runtime):
    if runtime not in KNOWN_RUNTIMES:
        fail(f"unknown reviewer runtime: {runtime}")

    configured_model = os.getenv("MODEL_B_MODEL", "").strip()
    declared_model = str(packet["reviewer_model_identity"]).strip()
    if not configured_model:
        fail("MODEL_B_MODEL is required for a selected reviewer runtime")
    if configured_model.casefold() != declared_model.casefold():
        fail(
            "configured reviewer model does not match frozen reviewer identity",
            configured_model=configured_model,
            declared_reviewer_model=declared_model,
        )

    if runtime == "huggingface":
        base = os.getenv("HF_OPENAI_BASE_URL", "https://router.huggingface.co/v1").rstrip("/")
        if base != "https://router.huggingface.co/v1":
            fail("custom Hugging Face base URL cannot earn independent Echo")


def validate_result(result, echo_eligible=False, runtime=None):
    if result.get("status") not in {"PASS", "HOLD"}:
        fail("reviewer status must be PASS or HOLD")
    for key in ("R", "I", "E", "K"):
        if result.get(key) not in (0, 1, False, True):
            fail(f"reviewer {key} must be 0 or 1")

    r = int(bool(result["R"]))
    i = int(bool(result["I"]))
    reviewer_e = int(bool(result["E"]))

    # Independence is a harness decision, never a reviewer self-attestation.
    effective_e = int(bool(reviewer_e and echo_eligible))
    expected_k = int(r and i and effective_e)

    if not echo_eligible and (result["status"] == "PASS" or reviewer_e == 1):
        fail(
            "reviewer result cannot earn Echo: runtime provenance is not independently eligible",
            reviewer_claimed_E=reviewer_e,
            effective_E=0,
            effective_K=0,
            runtime=runtime or "arbitrary-command",
        )

    if int(bool(result["K"])) != int(r and i and reviewer_e):
        fail("reviewer K is internally inconsistent with reviewer R/I/E")

    if result["status"] == "PASS" and expected_k != 1:
        fail("PASS is forbidden unless effective TCGE K=1")

    governed = dict(result)
    governed["E"] = effective_e
    governed["K"] = expected_k
    governed["runtime_provenance"] = {
        "runtime": runtime,
        "echo_eligible": bool(echo_eligible),
        "reviewer_self_attestation_controls_E": False,
    }
    return governed


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("packet", help="JSON review packet")
    ap.add_argument(
        "--runtime",
        choices=sorted(KNOWN_RUNTIMES),
        help="harness-selected reviewer runtime; only fixed remote provider lanes may be Echo-eligible",
    )
    ap.add_argument(
        "--reviewer-cmd",
        default=os.getenv("MODEL_B_REVIEWER_CMD"),
        help="debug/test command; never eligible to establish Echo",
    )
    ap.add_argument("--prompt-out", help="write frozen prompt and stop")
    args = ap.parse_args()

    packet = json.loads(Path(args.packet).read_text(encoding="utf-8"))
    validate_packet(packet)
    prompt = build_prompt(packet)

    if args.prompt_out:
        Path(args.prompt_out).write_text(prompt, encoding="utf-8")
        print(json.dumps({"status": "HOLD", "reason": "prompt frozen; independent reviewer not executed"}, indent=2))
        return 0

    if args.runtime and args.reviewer_cmd:
        fail("choose either --runtime or --reviewer-cmd, not both")

    if args.runtime:
        validate_runtime_binding(packet, args.runtime)
        result = run_external(runtime_command(args.runtime), prompt)
        governed = validate_result(
            result,
            echo_eligible=args.runtime in REMOTE_ECHO_RUNTIMES,
            runtime=args.runtime,
        )
    elif args.reviewer_cmd:
        argv = shlex.split(args.reviewer_cmd)
        if not argv:
            fail("empty reviewer command")
        result = run_external(argv, prompt)
        governed = validate_result(result, echo_eligible=False, runtime=None)
    else:
        fail("no independent reviewer runtime configured; use --runtime for an Echo-eligible lane")

    print(json.dumps(governed, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
