#!/usr/bin/env python3
import argparse
import os
import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
RUNTIMES = {
    "openai-compatible": "openai_compatible.py",
    "anthropic": "anthropic.py",
    "gemini": "gemini.py",
    "huggingface": "huggingface.py",
    "ollama": "ollama.py",
    "lmstudio": "lmstudio.py",
    "llamacpp": "llamacpp.py",
}

ap = argparse.ArgumentParser()
ap.add_argument("runtime", choices=sorted(RUNTIMES))
args = ap.parse_args()

script = HERE / RUNTIMES[args.runtime]
proc = subprocess.run(
    [sys.executable, str(script)],
    input=sys.stdin.buffer.read(),
    stdout=sys.stdout,
    stderr=sys.stderr,
    env=os.environ.copy(),
)
raise SystemExit(proc.returncode)
