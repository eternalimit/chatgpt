# Cross-Model Echo Reviewer (Model B)

Purpose: independent review lane for GETHUB artifacts before final output.

## Definition

Model B is not the primary builder and is not allowed to repair the candidate silently. It receives frozen source evidence, a candidate artifact, and frozen review rules. It returns a structured PASS/HOLD audit.

## Governing chain

SOURCE -> PRIMARY BUILD -> MODEL B -> STRUCTURED AUDIT -> TCGE -> REVISED BUILD SPEC -> OUTPUT -> POST-OUTPUT CHECK

## Balance rule

Balance means reconciliation against source evidence, not averaging opinions.

- Primary PASS + Model B PASS: may advance if Reality evidence is sufficient.
- Any HOLD: HOLD.
- Material disagreement: preserve both findings, return to source, resolve the disputed claim, then review again.

## Independence

Echo independence is decided by the GETHUB harness, not by the reviewer response.

- Different identity strings are necessary but not sufficient.
- Reviewer self-reporting `E=1` never proves independence by itself.
- `--reviewer-cmd` is a debug/test lane and can never earn Echo or PASS.
- Harness-selected fixed remote provider lanes may be Echo-eligible only when the configured runtime model exactly matches the frozen reviewer identity.
- Hugging Face may earn Echo only through the fixed `https://router.huggingface.co/v1` endpoint; a custom base URL is HOLD.
- Local runtimes and generic OpenAI-compatible endpoints are not automatically Echo-eligible.

These controls establish runtime provenance only. They do not prove that a reviewer conclusion is factually correct, and they do not substitute for claim-specific Reality evidence.

## AUTO MAX alignment

AUTO MAX source flow is preserved as:

INPUT -> EXE -> ATH -> REVIEW -> BUZZ WAVE -> MOXY -> BIND 379999 -> PRESERVED OUTPUT -> RECEIPT

Model B is used inside REVIEW. Its report becomes evidence input to the next build step. It does not replace source evidence.

## Current state

BUILD: hardened against reviewer self-attestation
HARNESS: executable
NEGATIVE CONTROL: arbitrary fake PASS cannot earn Echo
INDEPENDENT MODEL RUNTIME: external provider credentials still required for a real review
ECHO: HOLD until a genuinely independent runtime executes the frozen review and the claim-specific evidence is sufficient
