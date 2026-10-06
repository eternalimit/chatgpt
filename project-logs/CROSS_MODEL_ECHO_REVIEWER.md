# Cross-Model Echo Reviewer

Status: ACTIVE DESIGN
Repository role: Gethub balance control for image and artifact review

## Purpose

Provide a separate review lane between source evidence and final output.

The reviewer does not replace the source of truth and does not average disagreements.
If the primary lane and reviewer disagree on a material claim, the result is HOLD until the conflict is resolved from source evidence.

## Governing rule

R = Reality / direct source evidence
I = Inference / interpretation
E = independent Echo / validation
K = R AND I AND E

No claim becomes validated knowledge unless R=1, I=1, and E=1.

## Pipeline

SOURCE
-> PRIMARY BUILD
-> REVIEWER MODEL B
-> STRUCTURED AUDIT
-> TCGE GATE
-> REVISED BUILD SPEC
-> OUTPUT
-> POST-OUTPUT CHECK

## Reviewer contract

ROLE: Independent Plumbing Image Auditor

INPUTS:
1. Original Week 6 source image
2. Candidate 3D isometric image
3. Frozen topology rules
4. Week 6 answer-key data

CHECK:
- fixture locations preserved
- blue cold-water path correct
- red hot-water path correct
- green sanitary/drain path correct
- purple vent path correct
- no false cross-system fittings
- no invented pipe runs
- no architectural drift
- DFU and WSFU remain separate
- no cropped content
- every claimed connection is traceable to the source

OUTPUT:
PASS or HOLD

For every HOLD, report:
- exact location
- system color
- error type
- source conflict
- required correction

RULES:
- No redesign
- No guessing
- No self-validation
- No silent repair
- No majority vote
- No averaging contradictory claims

## Balance rule

Balance means independent reconciliation, not compromise.

If Primary = PASS and Echo = PASS:
    TCGE may advance if Reality evidence is sufficient.

If Primary = PASS and Echo = HOLD:
    HOLD.

If Primary = HOLD and Echo = PASS:
    HOLD until the primary defect is resolved.

If Primary != Echo on a material claim:
    preserve both findings
    return to source evidence
    resolve the exact disputed claim
    rerun the reviewer on the corrected candidate

## Week 6 image constraints

Blue = cold water:
water service -> meter -> cold-water main -> fixture branches -> water-heater cold inlet

Red = hot water:
water-heater hot outlet -> hot-water fixture branches

Green = sanitary:
fixture trap -> branch drain -> building drain -> building sewer

Purple = vent:
fixture vent -> vent branch -> vent riser -> through roof

Hard separation:
- red/blue never connect to green/purple
- red and blue may terminate at the same fixture but do not merge
- crossings are not connections unless the source explicitly establishes a fitting
- no invented foundation drops
- no invented architecture
- unresolved topology remains HOLD

## Independence requirement

A same-model second pass is not independent Echo.
Model B must be meaningfully separate in model/runtime/evidence path.
Until such a model is actually available and used, Echo status remains HOLD.

## Continuation state

Use this reviewer as the balance control before generating or approving the next Week 6 image.
