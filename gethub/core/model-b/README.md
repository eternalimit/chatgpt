# Cross-Model Echo Reviewer (Model B)

Purpose: independent review lane for Gethub.GitHub artifacts before final output.

## Definition

Model B is not the primary builder and is not allowed to repair the candidate silently. It receives frozen source evidence, a candidate artifact, and frozen review rules. It returns only a structured PASS/HOLD audit.

## Governing chain

SOURCE -> PRIMARY BUILD -> MODEL B -> STRUCTURED AUDIT -> TCGE -> REVISED BUILD SPEC -> OUTPUT -> POST-OUTPUT CHECK

## Balance rule

Balance means reconciliation against source evidence, not averaging opinions.

- Primary PASS + Model B PASS: may advance if Reality evidence is sufficient.
- Any HOLD: HOLD.
- Material disagreement: preserve both findings, return to source, resolve the disputed claim, then review again.

## Independence

The harness refuses to mark Echo as independent unless the reviewer declares a model/runtime identity different from the primary lane. A same-model second pass is never sufficient Echo.

## AUTO MAX alignment

AUTO MAX source flow is preserved as:

INPUT -> EXE -> ATH -> REVIEW -> BUZZ WAVE -> MOXY -> BIND 379999 -> PRESERVED OUTPUT -> RECEIPT

Model B is used inside REVIEW. Its report becomes evidence input to the next build step. It does not replace source evidence.

## Current state

BUILD: complete
HARNESS: executable
INDEPENDENT MODEL RUNTIME: external adapter required
ECHO: HOLD until a meaningfully separate reviewer runtime is actually connected and used
