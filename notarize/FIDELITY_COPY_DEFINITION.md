# FIDELITY — COPY Definition

## Definition

Within FIDELITY:

`COPY(S,D,t) = D`

where source object `S` is reproduced as destination object `D` at time `t`, with the intended invariant:

`Bytes(D) = Bytes(S)`

## Verified exact copy

A verified exact copy requires a byte-level operation establishing equality. One applicable method is independently hashing both artifacts and comparing the resulting SHA-256 values:

`SHA256(S) = SHA256(D)`

subject to the validity of the hashing and comparison procedure.

## Evidence boundary

`Same recorded reference != Verified byte copy`

Branch-local presence or inheritance may establish that an artifact is represented at another provenance location, but this must not be silently promoted into a claim that an external source object's raw bytes were independently re-hashed.

## Brian branch application

`CLARITY_ROOT.md` was inherited when the `brian` branch was created from `main`.

Calling it "Brian's copy" describes its branch-local presence and source relationship. Verification of repository identity/reference remains distinct from independent byte verification of any external source object represented by the recorded Clarity Root.

## FIDELITY rule

**COPY means an artifact reproduced into another provenance location while preserving the source relationship; exact byte identity is VERIFIED only when the required comparison operation establishes it.**

RS::PRESERVE::APPEND::VERIFY
