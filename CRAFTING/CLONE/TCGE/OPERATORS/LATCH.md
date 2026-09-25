# TCGE — LATCH

## Definition

A latch is a state-preserving mechanism that holds a defined state until a valid release or transition condition occurs.

```text
LATCH(INPUT, CONDITION) → HELD_STATE
```

## Core behavior

```text
SET → HOLD → CHECK → RELEASE / PRESERVE
```

## Boundaries

```text
LATCH != LOCK
LATCH != AUTHORIZATION
LATCH != PROOF
LATCH != ERASE
HELD != VERIFIED
```

A latch preserves state; it does not establish that the preserved state is true, authorized, or externally valid.

## TCGE sequence

```text
INPUT
→ VALIDATE CONDITION
→ LATCH
→ PRESERVE STATE
→ RELEASE CONDITION
→ TRANSITION
→ RECORD
```

## Governing rule

```text
A latch may preserve a state transition boundary; it may not manufacture truth, authority, or evidence.
```
