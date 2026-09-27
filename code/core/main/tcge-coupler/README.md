# TCGE Inclusion + Transformer Coupler

Governed path:

`INCLUSION -> IDENTIFY -> TRANSFORM -> VERIFY -> ECHO -> GATE -> PRESERVE`

Rules:
- Every inclusion keeps its path and SHA-256 identity.
- Every transformer records input and output SHA-256.
- An output cannot PASS without an explicitly independent Echo matching its output hash.
- `K = R AND I AND E`
- `H = I AND NOT K`
- `THROUGH(HOLD) != PASS`

Run:

`python3 coupler.py manifest.example.json --out coupling-receipt.json`

The example intentionally returns HOLD because no independent Echo has been supplied. That is a successful governance test, not a failed build.
