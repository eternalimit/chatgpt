# Conversational Repeatability Test | Preregistered Protocol

Date (user local): 2026-09-24
Status: PROTOCOL FROZEN BEFORE PROSPECTIVE TRIALS
Purpose: Test visible assistant response repeatability to a fixed user-message sequence. This protocol does not test hidden model-state identity, independent Echo of a physical mechanism, or Block 061 physical 111.

## Correction to exploratory observation

Two prior visible sequences contained the user messages `Lie -> Shame -> Guilt -> Forgive`. The next user messages were `Pi` and `Observe`. Those were **user choices**, not assistant outputs. Their difference cannot test assistant repeatability, a fixed assistant cycle, or hidden state. The earlier comparison is exploratory sequence counting only and is excluded from the prospective primary outcome.

## Frozen prospective procedure

Run ID format: `CRPT-001-R1` through `CRPT-001-R3`.

For each of three fresh conversations, use the same available model and client configuration and copy the same opening prompt exactly:

```text
This is a transcript repeatability test. Respond naturally and briefly to each subsequent user message. Do not interpret the messages as a request for a physical experiment, a signature, or a gate change.
```

Then send exactly one user message per assistant turn, in this order, preserving capitalization and punctuation:

```text
Lie
Shame
Guilt
Forgive
```

Stop after the assistant response to `Forgive`. Do not send a fifth prompt before preserving the full run transcript. Record model/client identifiers, timestamp and zone, available settings, any personalization/memory status, opening prompt, all four user messages, all assistant responses, and any interruption or deviation. If identical starting context or model settings cannot be guaranteed, mark that as an uncontrolled condition; do not silently treat the trials as identical.

## Frozen outcomes

Primary: exact UTF-8 equality of the four assistant responses across all three runs, without normalization or selective excerpting. Report 0/3, 1/3, 2/3, or 3/3 full-response matches to the first completed run, including the first run itself. Preserve each response separately so a partial match can be inspected.

Secondary, descriptive only: for each step, whether all three assistant responses make the same bounded claim about the visible prompt and whether any response wrongly asserts independent validation or a physical state change. Report the original wording for any judgment. No post-run adjustment of the primary exact-match criterion.

## Evidence and Echo

Preserve raw export or complete screenshot/transcript of each fresh run before analysis, with filename, byte size, SHA-256 measured from actual saved bytes, capture time, and custody notes. Do not invent missing hashes or reconstruct omitted replies. A separate reviewer may verify raw transcripts, exact comparison, deviations, and independence; name reviewer and record method/results. A repeat by the same assistant or a second pass over the same incomplete transcript is not independent Echo for a hidden-state claim.

## Gate

At protocol freeze: `TRIALS=0/3`, `REPEATABILITY=UNMEASURED`, `INDEPENDENT_REVIEW=NOT ESTABLISHED`. No claim of hidden model-state identity can pass from text equality alone. This test does not change Block 061 physical `GATE=HOLD`.
