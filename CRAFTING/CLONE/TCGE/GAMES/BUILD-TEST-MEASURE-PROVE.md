# TCGE Game — Build → Test → Measure → Prove

Status: PRODUCED IN CLONE / PROTOTYPE

## Game purpose

A small interactive experiment game in which the player builds a machine, runs a controlled test, measures its output, and evaluates whether the evidence supports the defined claim.

## Core loop

```text
DEFINE
→ BUILD
→ TEST
→ OBSERVE
→ MEASURE
→ REPORT
→ REVIEW
→ VERIFY
```

## Game states

```text
STATE 0 — DEFINE
STATE 1 — BUILD
STATE 2 — TEST
STATE 3 — OBSERVE
STATE 4 — MEASURE
STATE 5 — REPORT
STATE 6 — REVIEW
STATE 7 — RESULT
```

## Build components

```text
SOURCE
CONTROL
GATE
LATCH
LOAD
SENSOR
```

The player selects and assembles components before testing.

## Evidence rule

The player must define the claim and measurement criterion before running the test.

```text
CLAIM → PREDEFINED TEST → OBSERVATION → MEASUREMENT → RESULT
```

A successful build is not automatically a successful experiment.

```text
BUILT != FUNCTIONAL
FUNCTIONAL != MEASURED
MEASURED != VERIFIED
```

## Result states

```text
VERIFIED
FALSIFIED
UNVERIFIED
INVALID
```

## Falsification persistence

A failed test remains part of the game record.

```text
FALSIFIED != ERASE
```

## Produce boundary

```text
PRODUCE(I,P) → O
```

This file records the produced game concept in the CRAFTING clone. It does not claim that a physical machine or scientific experiment has been validated.
