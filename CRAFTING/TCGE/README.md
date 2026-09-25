# TCGE

Status: DEFINED
Scope: verification engine for the CRAFTING model.

## Hierarchy

```text
TCGE/
├── REQUIREMENT/
├── INPUT/
├── METHOD/
├── DETECT/
├── OBSERVE/
├── MEMORY/
├── EVIDENCE/
├── TEST/
├── MEASURE/
├── RESULT/
│   ├── VERIFIED/
│   ├── FALSIFIED/
│   └── UNVERIFIED/
├── PROVENANCE/
├── COMMIT/
├── REVEAL/
└── AUDIT/
```

## Core execution chain

```text
REQUIREMENT
→ INPUT
→ METHOD
→ DETECT
→ OBSERVE
→ EVIDENCE
→ TEST
→ MEASURE
→ RESULT
```

FIDELITY sequence preserved:

```text
DETECT → OBSERVE → MEMORY → EVIDENCE
```

## Governing constraint

No conclusion may exceed its evidentiary derivation.

## Result states

```text
TCGE(x) =
  VERIFIED   when the requirement is supported by the defined evidence
  FALSIFIED  when the requirement is contradicted by the defined evidence
  UNVERIFIED when the evidence is insufficient
```

## Commitment–reveal

```text
TARGET
→ BYTES
→ HASH
→ COMMIT
→ TEST
→ FREEZE
→ REVEAL
→ REHASH
→ COMPARE
```

A commitment intended to blind a test must exist before the observation being tested.

## Falsification persistence

```text
FALSIFICATION != ERASE
```

A failed test remains in MEMORY / PROVENANCE / AUDIT. Later evidence may change an interpretation or support a new test, but it does not silently delete the historical result.

## Evidence boundary

```text
DEFINED != MEASURED != VERIFIED
```

This document defines the TCGE model. It does not itself establish empirical measurements or verification of external claims.
