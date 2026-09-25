# FIDELITY signing authorization checkpoint

Date: 2026-09-24 (America/Los_Angeles)
State: COMMITTED / APPEND-ONLY

## Conversation evidence

In the active conversation, the user supplied the instruction `Authorize` after the FIDELITY declaration and Charles scoped attestation were prepared and committed. The user then supplied `Verify` and requested this commit. This record treats the authorization as permission to proceed with the identity-bound signing and verification workflow for the existing declaration. It does not expand that permission to a transfer of rights, a physical test, or an assertion that signing occurred.

## Frozen object

- Declaration: `notarize/FIDELITY_RICHARD_STEIN_OWNERSHIP_INTENT_UNSIGNED_2026-09-24.txt`
- Source commit: `cd5f7a5819a4b43d2192201b9aa609d644d8de32`
- Git blob SHA-1: `a7a980ccf6573815c39d3eef4b6fb75178d06602`
- Prepared declaration: 754 UTF-8 bytes; SHA-256 `25f922c17dda5a25d73e03fab3e6874b730c293931b63f2fbb100681ecbdd551`
- Existing Charles role checkpoint: `080b2ca7cafd5bbcbfaef4a1088b8b24a829b10b`; `CONTENT_MATCH_PASS::IDENTITY_HOLD::TITLE_HOLD::NO_CRYPTOGRAPHIC_SIGNATURE`.

## Verification and boundary

The prepared declaration's size and SHA-256 were recomputed locally in the verification turn; the named GitHub source file and Charles role checkpoint were fetched at their commits. No detached digital signature, signed document, certificate, or identity verification result was present in the current conversation/workspace during that check. The user instruction is a conversation-level authorization event; it is not independently verified real-world identity or a legal ownership determination.

`AUTHORIZATION_TO_PROCEED_WITH_SIGNING_WORKFLOW = RECORDED`
`SIGNATURE = NOT PROVIDED`
`IDENTITY = HOLD`
`LEGAL_TITLE = HOLD`

Exact next operation: the claimant signs the unchanged declaration using an identity-bound credential or identity-verified signing service and supplies the signed artifact and verification material; then verify its signature against the frozen bytes and separately examine chain of title. Append new evidence without rewriting this checkpoint.
