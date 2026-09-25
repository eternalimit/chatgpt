# Applied Formula A — Charles Validation Checkpoint

Date: 2026-09-24
State: COMMITTED / APPEND-ONLY
Scope: R::061 continuity

## Candidate definition

Applied Formula A is the execution form of Dynamic Formula A against a specified input and state.

```
A_applied(S_t, X_t) = Pi(Sigma(Delta(S_t, X_t))) -> S*_(t+1)
```

Where:
- X_t = resolved input
- S_t = current state
- Delta = determine the change/difference induced by the input
- Sigma = accumulate/integrate that change with state/context
- Pi = apply/project the accumulated result into the next candidate state
- S*_(t+1) = candidate successor state

## Governance

```
S*_(t+1) -> VERIFY -> GATE

GATE = PASS -> LATCH(S_(t+1))
GATE != PASS -> HOLD
```

Invariant:

```
APPLIED != VERIFIED != LATCHED
THROUGH(HOLD) != PASS
LATCH <=> GATE:PASS
```

## Charles validation result

Internal consistency with the stated governance: PASS.

TCGE status for the newly defined Applied Formula A:

```
R = 1
I = 1
E = 0
K = 0
```

The definition is therefore preserved as a grounded candidate definition. Independent Echo validation has not been established.

This commit does not establish independent validation, physical validation, physical 111, experimental success, or a physical law.

Next admissible operation: independent Echo validation of the definition, followed by GATE evaluation.

RS::PRESERVE::APPEND::VERIFY
