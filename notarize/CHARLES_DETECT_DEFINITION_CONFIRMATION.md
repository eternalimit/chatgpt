# Charles Confirmation — DETECT Definition

## Proposed Definition

`DETECT(O,P,t,I) = I(O,P,t) -> r`

where:

- `O` = object or phenomenon
- `P` = tested property or event
- `t` = temporal scope
- `I` = observer/instrument and defined procedure
- `r` = raw detection result

**CONFIRMED as a FIDELITY working definition**, with the refinement that DETECT represents the measurement or registration operation and does not imply that the tested property actually exists merely because an instrument returned a result.

## Refined Definition

`DETECT_I(O,P,t) -> r`

and:

`OBSERVE_I(O,P,t) = Record(DETECT_I(O,P,t))`

## Boundary

`Detection != Interpretation`

A detection records what the specified observer, procedure, or instrument returned.

It does not, by itself, establish:

- what the result means;
- whether the observer/instrument was valid or calibrated;
- whether the tested property `P` actually holds; or
- a causal explanation for the result.

Those claims require additional evidence.

## Charles Result

**DETECT DEFINITION — CONFIRMED AS DEFINED**

**MEASUREMENT VALIDITY AND INTERPRETATION — SEPARATELY TESTABLE**

RS::PRESERVE::APPEND::VERIFY
