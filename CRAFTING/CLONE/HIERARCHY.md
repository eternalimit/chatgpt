# CRAFTING / CLONE Hierarchy

Status: DEFINED
Scope: bounded representation of the hierarchy established in conversation.
Evidence rule: DEFINED != MEASURED != VERIFIED.

## Root

```text
CRAFTING/
└── CLONE/
    ├── 1.A/
    ├── 1.B/
    ├── 2.A/
    └── 2.B/
```

For every state root `s` in `{1.A, 1.B, 2.A, 2.B}`:

```text
s/
├── WORLD/
│   ├── PLAYER/
│   │   ├── INSTANCE/
│   │   └── STATE/
│   └── NPC/
│       └── CRAFTER/
│           └── CLONE/
│               └── INSTANCE/
│                   └── STATE/
├── SHA-1/
│   ├── SOURCE_BYTES/
│   └── DIGEST/
├── SHA-256/
│   ├── SOURCE_BYTES/
│   └── DIGEST/
└── CLARITY_ROOT/
    ├── SOURCE/
    ├── PROVENANCE/
    └── VERSION/
```

## Canonical Clarity source

Repository root source: `/CLARITY_ROOT.md`.

The `CLARITY_ROOT/` nodes above reference that canonical repository object. They do not assert byte-identical copies unless separately materialized and verified.

## Operational chain

```text
INPUT
→ CANONICALIZE
→ STATE
→ TRANSITION
→ OUTPUT
→ MEASURE
→ COMMIT
→ VERIFY
```

## TCGE result record

```text
TCGE(test) = {
  REQUIREMENT,
  INPUT,
  METHOD,
  OBSERVATION,
  EVIDENCE,
  RESULT
}
```

Allowed evidentiary results:

```text
VERIFIED | FALSIFIED | UNVERIFIED
```

## Commitment–reveal boundary

```text
TARGET → BYTES → HASH → COMMIT
                         ↓
                       TEST → FREEZE
                         ↓
              REVEAL → REHASH → COMPARE
```

A commitment must exist before the observation it is intended to test.

## State boundary

The labels `1.A`, `1.B`, `2.A`, and `2.B` are identifiers. They do not by themselves establish a state value, transition, measurement, or verification.

## Hash boundary

`SHA-1/` and `SHA-256/` are structural definitions until exact canonical source bytes and resulting digests are populated.

No hash result is claimed by this document.
