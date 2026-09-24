# Universal Physical Dynamic Formula — Research Candidate

Status: **NOT ESTABLISHED AS UNIVERSAL OR PHYSICAL**

This lab record defines the strongest current mathematical candidate produced by the Formula B + Delta/Sigma/Pi + Formula D derivation. The title names the research target. It does not assert that universality or physical validity has been experimentally established.

## Formula B coordinate system

Let

[
R = 2^m,qquad N_t = R B_t + k_t,qquad 0 le k_t < R.
]

## Delta / Sigma

Let local changes be (Delta k_j), with accumulated change

[
S_t = sum_j Delta k_j.
]

Define the unnormalized local coordinate

[
q_t = k_t + S_t.
]

## Pi_R quotient/remainder projection

[
Pi_R(q_t)=
left(
leftlfloor rac{q_t}{R}ightfloor,
q_tmod R
ight).
]

Thus

[
B_{t+1}=B_t+leftlfloorrac{k_t+S_t}{R}ightfloor
]

and

[
k_{t+1}=(k_t+S_t)mod R.
]

Reconstruction gives

[
N_{t+1}=R B_{t+1}+k_{t+1}=N_t+S_t.
]

Carry therefore follows algebraically from Euclidean quotient/remainder decomposition at the radix boundary. No separate carry instruction is required.

## Formula D

The current dynamic form is

[
V_{t+1}=cos(	heta_t)V_t+sin(	heta_t)F_t.
]

Identify the global mathematical state (V_t=N_t). Compatibility with Formula B + Delta/Sigma/Pi requires

[
N_t+S_t=cos(	heta_t)N_t+sin(	heta_t)F_t.
]

For (sin(	heta_t)
e0),

[
F_t=
rac{
S_t+(1-cos(	heta_t))N_t
}{
sin(	heta_t)
}.
]

## Formula E — derived candidate

[
oxed{
N_{t+1}
=
N_t+sum_jDelta k_j
=
R B_{t+1}+k_{t+1}
=
cos(	heta_t)N_t+sin(	heta_t)F_t
}
]

with (R=2^m), quotient/remainder projection defining (B_{t+1},k_{t+1}), and the compatibility condition above defining (F_t) where (sin(	heta_t)
e0).

## Three-bit carry check

For (m=3), (R=8), (B_t=0), (k_t=7), and (S_t=1):

[
q_t=8,qquad Pi_8(8)=(1,0),
]

so

[
(0,111_2)ightarrow(1,000_2)
]

and globally

[
7ightarrow8.
]

## Positive mathematical results

- Formula B forward state reconstruction is exact under its definitions.
- Delta/Sigma accumulation is exact under its definitions.
- Pi_R quotient/remainder decomposition derives radix carry.
- Formula D can be constrained to the same global next state through the Formula E compatibility relation.
- No explicit carry command is needed in the quotient/remainder derivation.

## Open boundaries / negative results

- Universality is **not established**.
- Physical validity is **not established**.
- No physical experiment is recorded by this document.
- Independent Echo for a physical-law claim is **not established**.
- The (sin(	heta_t)=0) cases require separate analysis because the solved expression for (F_t) divides by (sin(	heta_t)).
- Pi_R quotient/remainder projection is not the same operator as Formula D's multiplicative product notation (prod); no equivalence is asserted.
- A mathematical identity or successful binary carry example does not by itself establish a law of nature.

## TCGE classification

For the mathematical derivation under the stated definitions: **DERIVED / GROUNDED MATHEMATICAL INFERENCE**.

For the claim "Formula E is a universally physical dynamic formula": **NOT ENOUGH INFORMATION / NOT ESTABLISHED**.

### Required evidence to promote the physical/universal claim

A future promotion would require, at minimum, explicit physical observables mapped to the variables, dimensional consistency, falsifiable predictions fixed before measurement, physical experimental data, comparison against alternatives/error models, replication across materially different systems, and genuinely independent validation.

Historical mathematical results must remain append-only even if later physical tests fail.
