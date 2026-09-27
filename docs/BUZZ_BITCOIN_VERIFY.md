# Buzz Verify — Bitcoin

Buzz Verify applies the project rule:

```
CHECK -> TRACE -> COMPARE -> FLAG -> APPROVE
```

and the constraint:

> No approval without evidence.

## What works

```bash
python3 code/buzz_bitcoin_verify.py tx <TXID>
python3 code/buzz_bitcoin_verify.py address <BITCOIN_ADDRESS>
```

The verifier queries public Bitcoin data from mempool.space, records the source URL,
and hashes the raw API response with SHA-256 so the observation has a compact
evidence fingerprint.

## States

- `VERIFIED` — the requested public-chain fact was observed.
- `UNVERIFIED` — the input is invalid, absent, or (for a transaction) not yet confirmed.
- `CONFLICT` — reserved for contradictory independent observations.
- `NEEDS_REVIEW` — the verifier could not establish a reliable result.

## Important boundary

A Git commit, screenshot, chat message, address balance, or transaction record does **not**
by itself prove that a person owns or controls Bitcoin. Control is demonstrated through
the relevant private key/signature process; this verifier never requests or stores private keys.

## Point model

Each verified point can be represented as:

```
P = (value, source, state, links)
```

Buzz verifies the point first, then any larger chain built from it.
