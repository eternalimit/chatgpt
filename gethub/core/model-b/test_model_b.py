import json
import subprocess
import tempfile
from pathlib import Path

ROOT = Path(__file__).parent
SCRIPT = ROOT / "model_b.py"


def run(packet, *args):
    with tempfile.TemporaryDirectory() as td:
        p = Path(td) / "packet.json"
        p.write_text(json.dumps(packet), encoding="utf-8")
        return subprocess.run(["python3", str(SCRIPT), str(p), *args], capture_output=True, text=True)


def base_packet():
    return {
        "source_evidence": ["source"],
        "candidate_artifact": "candidate",
        "frozen_rules": ["rule"],
        "primary_model_identity": "Primary-A",
        "reviewer_model_identity": "Reviewer-B"
    }


def test_same_model_holds():
    p = base_packet()
    p["reviewer_model_identity"] = "Primary-A"
    r = run(p)
    assert r.returncode != 0
    assert json.loads(r.stdout)["status"] == "HOLD"


def test_no_runtime_holds():
    r = run(base_packet())
    assert r.returncode != 0
    assert "no independent reviewer runtime" in r.stdout


def test_prompt_freeze():
    with tempfile.TemporaryDirectory() as td:
        out = Path(td) / "prompt.txt"
        r = run(base_packet(), "--prompt-out", str(out))
        assert r.returncode == 0
        assert out.exists()
        assert "independent reviewer" in out.read_text(encoding="utf-8")


if __name__ == "__main__":
    test_same_model_holds()
    test_no_runtime_holds()
    test_prompt_freeze()
    print("PASS")
