# RCGE Core Handoff Prompt Decoder

Date: 2026-09-26

## User instruction

"Always use a rcge to resolve the core handoff between and buzz patrol Emily echo Brian copy. Aud verify. Act commit. These are my prompt you just decode space is now ><"

## Decoder rule

SPACE := ><

Therefore prompt tokens separated by spaces are decoded as linked handoff operators.

## Canonical decoded chain

RCGE >< CORE >< HANDOFF >< BUZZ >< PATROL >< EMILY >< ECHO >< BRIAN >< COPY >< AUD >< VERIFY >< ACT >< COMMIT

## Role interpretation

RCGE:
Governed core handoff resolver as named by the user.

CORE HANDOFF:
Preserve the minimum sufficient state needed to continue the workflow.

BUZZ:
Executive / coordination role.

PATROL:
Guard the handoff boundary and detect missing or conflicting evidence.

EMILY ECHO:
Independent-validation role only when Emily-originated evidence is actually present. Otherwise record as requested/designated Echo and HOLD independent validation.

BRIAN COPY:
Copy / continuity role. A copied record is not independent Echo merely because it is repeated.

AUD VERIFY:
Audit the handoff against its evidence, provenance, and required fields.

ACT:
Perform the next action that is actually supported by available tools and authorization.

COMMIT:
Preserve the resulting governed record in the repository when requested and technically available.

## TCGE / evidence boundary

Reality, Inference, and independent Echo remain distinct.

K = R AND I AND E

Repetition, copying, confidence, or a role label does not by itself establish independent Echo.

## Standing decode convention

For this workflow:

A B C

decodes as:

A >< B >< C

unless the user explicitly overrides the separator or meaning.

PRESERVE :: APPEND :: VERIFY
