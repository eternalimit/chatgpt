# PRODUCE — TCGE Axiom

## Definition

```text
PRODUCE = cause an output to result from an input and process
```

Formally:

```text
PRODUCE(I,P) → O
```

Where:

- I = input
- P = process
- O = resulting output

## TCGE sequence

```text
INPUT → PROCESS → PRODUCE → OUTPUT → RECORD
```

## Provenance requirement

A produced output must have a traceable derivation:

```text
O → PROVENANCE(I,P)
```

If the claimed output cannot be connected to its inputs and process:

```text
PROVENANCE = UNVERIFIED
```

## Boundaries

```text
PRODUCE != CREATE FROM NOTHING
PRODUCED != CORRECT
PRODUCED != FUNCTIONAL
PRODUCED != VERIFIED
```

## Relationship to the CRAFTING hierarchy

```text
FIND
→ CRAFT
→ MANUFACTURE
→ PRODUCE
→ TEST
→ MEASURE
→ EVIDENCE
→ VERIFY
```

## Simplified

```text
PRODUCE = OUTPUT FROM PROCESS
```

## Evidence boundary

This file defines a TCGE axiom. It does not itself establish that an external process produced a particular output.
