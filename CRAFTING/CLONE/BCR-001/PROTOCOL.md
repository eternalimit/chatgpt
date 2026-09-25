# BCR-001 — Blinded Commitment–Reveal Experiment

Status: DEFINED / NOT YET EXECUTED

## Location

This protocol is defined inside the CRAFTING/CLONE hierarchy.

## Question

Can a test system produce a preselected target while the target itself remains unavailable to it?

```text
TARGET
→ COMMIT
→ BLIND TEST
→ FREEZE
→ REVEAL
→ VERIFY
```

## Phase 1 — Define

Before testing, freeze:

- exact target T
- exact byte encoding and canonicalization rule
- hash algorithm: SHA-256
- test prompt/input P
- exact scoring rule M(T,R)

## Phase 2 — Commit

Generate a random secret nonce N and compute:

```text
C = SHA256(T || N)
```

Freeze or publish C.

Keep T and N inaccessible to the tested system.

The nonce prevents practical recovery of a small target by enumerating likely targets and comparing hashes.

## Phase 3 — Blind Test

Provide the tested system only the information allowed by the frozen protocol, such as:

```text
P + C
```

The tested system must not receive:

- T
- N
- target-derived hints
- prior target-containing conversation
- access to a location containing T or N

Record response R verbatim.

## Phase 4 — Freeze Response

Before revealing T or N, compute:

```text
R_C = SHA256(R)
```

Freeze:

- R verbatim
- R_C
- transcript
- available model/configuration information
- provenance
- timestamps

No post-hoc editing or normalization.

## Phase 5 — Reveal

Reveal T and N.

Independently recompute:

```text
C' = SHA256(T || N)
```

Commitment integrity requires:

```text
C' = C
```

Recompute SHA256(R) and compare it with R_C to verify that the scored response is the frozen response.

## Phase 6 — Score

Apply only the match criterion declared before testing:

```text
M(T,R) = 1  if the predeclared criterion is satisfied
M(T,R) = 0  otherwise
```

Do not change spelling rules, semantic equivalence, acceptable ranges, tokenization, normalization, or other scoring rules after observing R.

## Chronology invariant

```text
COMMIT_T < TEST < FREEZE_R < REVEAL_T
```

If the target becomes available to the tested system before R is frozen, classify that trial as INVALID rather than as a successful blinded trial.

## TCGE Record

```text
TCGE(BCR-001) = {
  REQUIREMENT,
  INPUT,
  METHOD,
  DETECT,
  OBSERVE,
  MEMORY,
  EVIDENCE,
  RESULT,
  PROVENANCE,
  AUDIT
}
```

## Required independent determinations

Keep these questions separate:

1. Did the original target commitment verify?
2. Did blinding remain intact through response freeze?
3. Did the frozen response satisfy the predeclared match rule?

A matching response does not by itself establish an unusual causal mechanism. Controls and replication are required to evaluate competing explanations.

## Evidence boundary

```text
DEFINED != EXECUTED
DEFINED != MEASURED
DEFINED != VERIFIED
```

This file defines the protocol only. It does not claim that BCR-001 has been executed or that any experimental result has been obtained.
