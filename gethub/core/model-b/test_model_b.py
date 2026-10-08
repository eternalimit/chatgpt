import json
import os
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).parent
SCRIPT = ROOT / "model_b.py"


def run(packet, *args, env=None):
    with tempfile.TemporaryDirectory() as td:
        p = Path(td) / "packet.json"
        p.write_text(json.dumps(packet), encoding="utf-8")
        return subprocess.run(
            [sys.executable, str(SCRIPT), str(p), *args],
            capture_output=True,
            text=True,
            env=env,
        )


def base_packet():
    return {
        "source_evidence": ["source"],
        "candidate_artifact": "candidate",
        "frozen_rules": ["rule"],
        "primary_model_identity": "Primary-A",
        "reviewer_model_identity": "Reviewer-B",
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
        assert "independently decides" in out.read_text(encoding="utf-8")


def test_arbitrary_fake_pass_cannot_earn_echo():
    with tempfile.TemporaryDirectory() as td:
        mock = Path(td) / "mock.py"
        mock.write_text(
            "import json\n"
            "print(json.dumps({'status':'PASS','findings':[],'R':1,'I':1,'E':1,'K':1}))\n",
            encoding="utf-8",
        )
        cmd = f"{sys.executable} {mock}"
        r = run(base_packet(), "--reviewer-cmd", cmd)
        assert r.returncode != 0
        data = json.loads(r.stdout)
        assert data["status"] == "HOLD"
        assert data["effective_E"] == 0
        assert data["effective_K"] == 0
        assert "cannot earn Echo" in data["reason"]


def test_runtime_model_identity_must_match():
    env = os.environ.copy()
    env["MODEL_B_MODEL"] = "Different-Model"
    r = run(base_packet(), "--runtime", "huggingface", env=env)
    assert r.returncode != 0
    data = json.loads(r.stdout)
    assert data["status"] == "HOLD"
    assert "does not match" in data["reason"]


def test_custom_huggingface_base_cannot_earn_echo():
    env = os.environ.copy()
    env["MODEL_B_MODEL"] = "Reviewer-B"
    env["HF_OPENAI_BASE_URL"] = "http://127.0.0.1:9999/v1"
    r = run(base_packet(), "--runtime", "huggingface", env=env)
    assert r.returncode != 0
    data = json.loads(r.stdout)
    assert data["status"] == "HOLD"
    assert "custom Hugging Face base URL" in data["reason"]


if __name__ == "__main__":
    test_same_model_holds()
    test_no_runtime_holds()
    test_prompt_freeze()
    test_arbitrary_fake_pass_cannot_earn_echo()
    test_runtime_model_identity_must_match()
    test_custom_huggingface_base_cannot_earn_echo()
    print("PASS")
