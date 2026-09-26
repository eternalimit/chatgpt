# Consistency Core Stability Principle

## Claim

A consistency core can be more repeatable than an LLM when the core uses deterministic rules, frozen inputs, and explicit acceptance criteria.

## Distinction

LLM = generative / probabilistic

Consistency Core = deterministic / constraint-checking

## Architecture

LLM → CONSISTENCY CORE → GATE → RESULT

The LLM generates candidate output. The consistency core checks declared invariants, provenance, format, contradictions, and acceptance criteria.

## Stability statement

For the same frozen input I, a probabilistic LLM may produce different valid outputs across runs, while a deterministic consistency core can produce the same evaluation every time.

## Boundary

Greater repeatability does not automatically imply greater truth, correctness, or system reliability. A deterministic checker can consistently make the wrong judgment if its rules are flawed.

Therefore:

CONSISTENCY CORE can be more repeatable than LLM

but

SYSTEM RELIABILITY must be established experimentally.
