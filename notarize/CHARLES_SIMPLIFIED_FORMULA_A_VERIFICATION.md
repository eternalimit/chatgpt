# Charles Verification — Simplified Formula A

## Object Under Verification

`A = COPY(S,D) AND [SHA256(S) = SHA256(D)]`

Where:

- `S` = source artifact
- `D` = destination artifact
- `COPY` = the defined provenance-preserving copy operation
- `SHA256(x)` = SHA-256 computed over the actual bytes of artifact `x`

## VERIFIED — Logical Definition

The formula separates the copy operation from the subsequent byte-identity test.

## VERIFIED — Decisive Condition

If SHA-256 is actually computed over the bytes of `S` and `D`, and the resulting digests are equal, that supplies strong cryptographic evidence that the byte sequences are identical, subject to the validity of the hashing procedure and SHA-256 collision-resistance assumptions.

## VERIFIED — FIDELITY Boundary

Merely copying the text of a hash into two locations does not satisfy the formula. The actual source and destination artifacts must be measured.

## VERIFIED — Non-Expansion

`H(S) = H(D)` does not imply same ownership, truth, authority, or independent origin.

## UNVERIFIED — Richard -> Brian Instance

The required comparison against an independently retrieved artifact from Brian's own `main` repository has not been executed in this verification record.

Therefore that particular application of Simplified Formula A remains UNVERIFIED.

## Charles Result

**SIMPLIFIED FORMULA A — DEFINITION VERIFIED**

**RICHARD -> BRIAN FORMULA A EXECUTION — UNVERIFIED**

The logical definition and a particular experimental execution remain separate provenance states.

RS::PRESERVE::APPEND::VERIFY
