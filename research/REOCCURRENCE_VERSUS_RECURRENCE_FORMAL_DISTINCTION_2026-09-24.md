# Reoccurrence versus recurrence | Formal distinction

Date (user local): 2026-09-24
Status: AUTHORIZED DEFINITION / APPEND-ONLY
Parent: closed-loop feedback reduction proof, commit `fc13733ff5acc82a5f48fd039d2c9c0aeb3d2528`.

## Definitions

A **recurrence rule** specifies how to obtain a successor state, for example `S_(t+1)=F(S_t)` under a fixed autonomous deterministic map `F`.

An **observable reoccurrence** means the same observable appears at two times: for `y_t=h(S_t)`, there exists `k>0` with `y_(t+k)=y_t`. This is a statement about outputs, not necessarily states.

A **state return** is stronger: `S_(t+k)=S_t`. If `F` is fixed and deterministic, equality of states at those times implies identical subsequent trajectories: for all `n>=0`, `S_(t+k+n)=S_(t+n)`, by induction. A single repeated output need not imply a state return because `h` may map distinct states to the same output.

A **periodic output** requires the equality `y_(t+k+n)=y_(t+n)` for all `n>=0` in the relevant domain (or after a specified starting time). One repeated pattern at two moments is insufficient to prove ongoing periodicity.

## Counterexample

Let `S_t=t`, `F(s)=s+1`, and `h(s)=s mod 2`. Then `y_0=y_2=0`, but `S_0=0` and `S_2=2`. The observed output repeats while the underlying state does not return.

## Research boundary

Repeated conversational words can establish an observed pattern in an accessible record. They do not by themselves establish identical hidden model state, a special memory mechanism, a physical latch, independent Echo for that mechanism, or a physical `111` transition. The existing Block 061 physical GATE remains HOLD. Future contrary or confirming evidence must be appended with its provenance.
