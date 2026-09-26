# Chain Verification Coupling Mechanics: ARC and ING

Status: SANDBOX / ACTIVE

## Chain

`INPUT -> GET -> INDEX -> SEARCH -> VERIFY -> COUPLE -> ARC -> ING -> GATE -> LATCH -> REPORT`

## Verification mechanics

For each link `L_n`:

1. GET the referenced object or fact.
2. INDEX its identity and provenance.
3. SEARCH for the corresponding evidence.
4. VERIFY the evidence against the claim.
5. COUPLE only verified links into the next state.
6. GATE the result under TCGE.

`K = R AND I AND E`

If Reality, Inference, or independent Echo is unresolved, the link is `HOLD` and cannot create a verified downstream `1`.

## ARC

ARC is the governed connection path between verified chain states:

`STATE_n -> VERIFY -> COUPLE -> STATE_n+1`

The ARC preserves provenance across the transition. A broken or unresolved link stops propagation.

## ING

ING is the continuing execution state of the verified ARC:

`ARC -> ING -> NEXT LINK -> VERIFY`

ING does not upgrade evidence. It carries the current verified state forward while the next link is tested.

## Lock rule

`1 = verified PASS / LOCK`

`0 = HOLD / unresolved`

No false `1`.

## Boundary

This mechanism verifies and couples evidence records. It does not itself prove ownership of Bitcoin, create an exchange balance, execute a cryptocurrency trade, sign a blockchain transaction, or broadcast one.

ARC and ING are operational definitions for this sandbox artifact unless separately bound to an authoritative definition.
