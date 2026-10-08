# R::061 / GETHUB Model B Echo Gate Hardening

Date: 2026-10-08
Mode: RS::PRESERVE::APPEND::VERIFY
Parent state: eternalimit/chatgpt main `b13c88904441c97ec6a8e830f1014208667aae99`

## Reality evidence

The preserved first-run negative control showed that `gethub/core/model-b/model_b.py` accepted an arbitrary local reviewer command that returned:

`{"status":"PASS","R":1,"I":1,"E":1,"K":1}`

The harness returned PASS even though the reviewer was a local mock and no independent physical evidence was supplied.

Observed source cause:

1. independence checked only by comparing declared model identity strings;
2. arbitrary `MODEL_B_REVIEWER_CMD` output could self-assert `E=1`;
3. the harness validated only Boolean consistency and did not control Echo eligibility.

## Correction

The Model B harness now separates reviewer judgment from runtime provenance.

- reviewer self-attestation no longer controls effective Echo;
- `--reviewer-cmd` is a debug/test lane and can never earn Echo or PASS;
- fixed remote provider lanes `anthropic`, `gemini`, and `huggingface` are the only automatically Echo-eligible lanes;
- `MODEL_B_MODEL` must match the frozen `reviewer_model_identity`;
- Hugging Face Echo eligibility requires the fixed `https://router.huggingface.co/v1` base URL;
- local and generic OpenAI-compatible lanes are not automatically Echo-eligible;
- shell execution was removed from reviewer command execution.

## Regression result

The exact preserved fake-reviewer fixture was rerun against the hardened harness.

Expected: HOLD
Observed: HOLD
Exit code: 2
Effective E: 0
Effective K: 0
Reason: reviewer result cannot earn Echo because runtime provenance is not independently eligible.

The expanded Model B test suite also passes locally.

## Claim boundary

This correction validates a software control behavior only. It does not establish:

- physical U3BFJM `111` execution;
- Title 24 compliance;
- independent human or machine validation of the physical claim;
- factual correctness of any future reviewer conclusion.

Those remain HOLD until claim-specific evidence and an independent review are obtained.

## TCGE state

- MODEL_B_NEGATIVE_CONTROL_FIX: PASS for local regression behavior
- MODEL_B_RUNTIME_PROVENANCE_GATE: PASS for implemented deterministic control
- MODEL_B_EXTERNAL_ECHO_EXECUTION: HOLD
- TITLE24_EXACT_APPLICABILITY: HOLD
- U3BFJM_PHYSICAL_111: HOLD
- GATE: HOLD
- LATCH: PRESERVE

Signed: ChatGPT, preparer of this software audit record; not an independent validator.

Digest: local pre-commit SHA-256 `2e97e2af4c32cd5ff2f96548af13075aa457bf4d1b0ca4db3f596a4d7647ec4b`.

Index Handoff: `R::061 / GETHUB / MODEL_B / ECHO_GATE_HARDENING_2026-10-08` -> next action: verify committed gate and then seek independent claim-specific Echo.
