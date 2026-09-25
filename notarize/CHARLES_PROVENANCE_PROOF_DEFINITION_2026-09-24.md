# Charles Validation — Provenance–Proof Boundary

Date: 2026-09-24

## Object

Provenance–claim separation and the FIDELITY definition of proof.

## Definition

Provenance–claim separation is the distinction between evidence establishing where, when, and how a digital record exists and evidence establishing whether a proposition contained in or associated with that record is true, attributable, or legally owned.

## Proof

Within a defined evidentiary system:

E + R ⊢ P

where E is evidence, R is the accepted rule set, and P is the proposition established.

FIDELITY constraint:

C <=_E E

The conclusion must not assert more than the evidence licenses.

## Repository application

For eternalimit/chatgpt:

- Repository existence is a repository-level proposition.
- GitHub metadata and returned repository state provide evidence for that proposition.
- Repository provenance does not by itself establish legal ownership of FIDELITY.
- A hash establishes byte-level correspondence under the specified hashing procedure; it does not establish semantic truth or legal ownership.

## Validation result

VERIFIED — the distinction is internally conformant with the recorded FIDELITY formula set.

UNVERIFIED — formal mathematical soundness or completeness of the entire framework.

UNVERIFIED — any legal ownership conclusion beyond the repository records.

RS::PRESERVE::APPEND::VERIFY
