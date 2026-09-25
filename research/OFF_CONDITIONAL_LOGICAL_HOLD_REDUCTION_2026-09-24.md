# OFF | Conditional Logical Hold Reduction

Date (user local): 2026-09-24
Status: APPEND-ONLY MATHEMATICAL DEFINITION
Parent: MIRROR copy-fidelity reduction, commit `17ff244332cc5b845c4582f876d4d0eeb5a4e1b7`.

## General enabled transition

For an admitted logical state `S_t`, input `u_t`, fixed context `Gamma,N`, and enable bit `a_t in {0,1}`, **define** the transition:

```text
S_(t+1) = F_general(S_t,u_t;Gamma,N), if a_t=1 (ON)
S_(t+1) = S_t,                       if a_t=0 (OFF/HOLD)
```

This is a piecewise definition, valid for arbitrary state sets; it does not presume states can be added or multiplied numerically. If the OFF branch is selected, substitution gives the simplified logical identity `S_(t+1)=S_t`. OFF therefore means no **admitted logical transition under this rule**. It does not erase logs, historical evidence, pending candidate states, or unresolved claims. A later ON command requires its own applicable gate; OFF is not a retrospective PASS or failure.

## Physical boundary

The hold branch is a chosen model assumption, not a physical law. Real actuators, fluids, electronics, and environments may change under external forces, leakage, drift, power loss, or unmodeled dynamics while control is OFF. A physical OFF claim requires a defined device-specific criterion and actual observations. Do not infer physical position, isolation, zero flow, safety, or permanent state retention from `a_t=0` alone.

For Block 061, physical `111` remains NOT ESTABLISHED, physical GATE remains HOLD, and physical LATCH remains NOT AUTHORIZED. Future measurements must be appended with provenance and checked against frozen criteria.
