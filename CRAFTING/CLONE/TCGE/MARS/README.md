# TCGE — MARS

Status: CRAFTED / COMMITTED

## Environment architecture

```text
EARTH
→ TRANSMIT
→ MARS
→ EXECUTE
→ OBSERVE
→ RETURN
```

## Information-integrity path

```text
SOURCE
→ CANONICAL BYTES
→ {SHA1, SHA256}
→ TRANSMIT
→ MARS
→ REHASH
→ COMPARE
```

## Invariant

If the exact canonical bytes are unchanged between locations, the deterministic hash is unchanged.

```text
B_EARTH = B_MARS
=> H(B_EARTH) = H(B_MARS)
```

## Boundaries

```text
LOCATION CHANGE != BYTE CHANGE
SAME INFORMATION != SAME PHYSICAL ENVIRONMENT
SAME HASH != SAME PHYSICAL OUTCOME
HASH MATCH != PROOF OF TRUTH
```

## Current TCGE result reference

For the previously produced canonical TCGE_REDUCTION_V2 payload:

```text
H_256(TCGE result)
= 28a407ba55ab5867ad475e17e669e80e6c22e7b0a7aa4566289f26c5f64f6e40
```

This digest identifies the exact TCGE_REDUCTION_V2 canonical bytes. It is not a digest of this MARS document.
