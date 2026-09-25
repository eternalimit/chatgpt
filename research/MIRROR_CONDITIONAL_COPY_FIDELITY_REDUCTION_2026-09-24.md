# MIRROR | Conditional Copy Fidelity Reduction

Date (user local): 2026-09-24
Status: APPEND-ONLY MATHEMATICAL DEFINITION
Parent: ON conversational continuation checkpoint, commit `499eefef7ed7cece45f0de4313dd8438553a0f3e`.

## General operation

Let `S` be an actual available source byte stream, `C` a recorded copy operation, and `S' = C(S)` the destination byte stream. Preserve source/destination identifiers, actual sizes, acquisition/transfer method, timestamps, and custody before deriving a fidelity claim. Define `V(S,S')` as the result of a specified comparison over those **actual bytes**. A copy operation alone does not establish fidelity.

## Simplified conditional result

If an exact byte-by-byte comparison covers the entire scoped source and destination and returns equal, then

```text
V_exact(S,S') = PASS  =>  S' = S  byte for byte (within that scope).
```

The compact notation `M(S)=S` is admissible **only as a statement of measured byte identity for that copy under the stated comparison**. It does not claim that two storage locations, timestamps, identities, metadata objects, or physical events are the same. If no actual bytes or complete comparison are available, identity is UNVERIFIED. Hash agreement may be useful evidence of byte identity subject to its algorithm and collision assumptions, but it must not be silently described as a literal byte-by-byte comparison.

## TCGE separation

A faithful mirror can support provenance and source-content fidelity for a specific evidence object. It does not independently validate the source's truth, the correctness of an inference drawn from it, authorship or legal identity, or a physical experiment. `M(S)=S` does **not** imply `E=1` for the interpreted claim. Independent Echo must check the inference through a sufficiently separate and documented method. Same-environment copying, hashing, or repeating a statement is not automatically Echo.

For Block 061, neither a mirrored diagram nor matching bytes establish actual three-actuator positions or eight functioning physical paths. Physical `GATE=HOLD`; physical `111` and physical LATCH remain unestablished. Future measurements and contrary evidence are appended, never backdated into this definition.
