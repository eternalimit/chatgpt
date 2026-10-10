# Experiment 049 — Runnable synthetic checkpoint falsification test

**Attribution:** Richard Stein — REIK/TCGE (AI-assisted bounded research).  
**State:** **0 · HOLD; DROP U**. This is a software test, not independent scientific Echo.

The complete Python source is archived in `reik_checkpoint_049.py.gz` rather than only describing a local test. The gzip stream has reproducible mtime=0 metadata. The deliberately deterministic Ed25519 test keys are **publicly predictable** and must never be used as real signing credentials.

## Reproduce offline after obtaining repository contents

```sh
python3 -m pip install 'cryptography==46.0.4'
sha256sum reik_checkpoint_049.py.gz
gzip -dc reik_checkpoint_049.py.gz > reik_checkpoint_049.py
sha256sum reik_checkpoint_049.py
python3 reik_checkpoint_049.py --json
```

Expected exact archive SHA-256: `5dbc2013678e00714bb2ed8f0a8e7f89c136544dd7b0a01edabfdda0cf124bc6`  
Expected unpacked script SHA-256: `bcfc799cca8c9993beafa41ba51cc250e9f8d1f039001c146d5e4fb6b1709444`  
Expected execution: **46/46 named synthetic checks PASS**; deterministic fixtures listed in the JSON audit. For Windows, use Python's `gzip` module to decompress instead of the `gzip` command. The local full JSON execution receipt SHA-256 was `a551a1118ce61f9b8685ef6d1414fd5ca741cff5a95497a896fecbc9850ca4fb`; it was **not** uploaded. Run the published source to generate your own.

The file is an executable synthetic test harness, not the missing 048 local verifier and not a deployed consensus application. Every 'pass' means the *predicted test outcome* (including expected rejection) occurred; it does not prove external trust, witness independence, REIK theory, P vs NP, or mathematical physics.

See `REIK_TCGE_RESEARCH_PAPER_049.md` and `REIK_TCGE_PUBLIC_AUDIT_049.json` for findings, limitations and lineage. No original kernel or prior experiment file changed.
