# Block 061 | Illustrative fixture image correction and PI/KEY checkpoint

Date (user local): 2026-09-24
Status: APPEND-ONLY CORRECTION / CONVERSATIONAL CHECKPOINT
Parent: Block 061 physical 111 field worksheet; Charles PI/KEY verification

## Direct image evidence and correction

The user supplied an illustrative JPEG showing a residential water fixture table. The inspected local copy was 710 × 1536 pixels with SHA-256 `ed516bf120620fc808de475b749ad6703f18db06a1be39639a242db26916d9ee`. The original underlying fixture schedule, authoritative code source, project plan, and as-built physical route map were not provided by that image. An earlier assistant description called the screenshot the "source fixture schedule"; retract that characterization. The image is the source for **what the screenshot displays**, not an authenticated source for code values or the actual installation.

| Visible fixture category | Quantity | Displayed example units each | Recomputed row total |
|---|---:|---:|---:|
| Toilet | 2 | 2.5 | 5.0 |
| Lavatory | 2 | 1.0 | 2.0 |
| Shower | 2 | 2.0 | 4.0 |
| Bathtub | 1 | 1.5 | 1.5 |
| Kitchen sink | 1 | 1.5 | 1.5 |
| Dishwasher | 1 | 1.5 | 1.5 |
| Clothes washer | 1 | 2.0 | 2.0 |
| Exterior hose bibb | 2 | 2.5 | 5.0 |

Eight visible categories contain twelve listed fixtures/outlets. Row arithmetic gives **22.5 example fixture units**; the image prints **21.0**, a discrepancy of **1.5**. The correct underlying schedule value is UNRESOLVED. The image's illustrative pressure arithmetic is 40 - 8 - 10 = 22 psi, two psi above its example 20 psi threshold; no field pressure measurement is thereby established.

## Frozen design contract versus physical evidence

`N = 4b2 + 2b1 + b0`, `P = N + 1`. For a planned command `111`, `N = 7` and target `P = 8`. A category-to-path assignment numbered 1–8 is a **candidate association only**. The image does not show the actual three actuator positions, eight physical path IDs and connectivity, fixture branch topology, pressure/flow readings, untouched acquisition files, or independent field validation. Eight categories do not prove eight functioning physical paths or Title 24 compliance.

The existing Block 061 worksheet has no completed pre-run protocol/criteria reference, actuator observations, per-path raw measurements, acquisition provenance, or named independent validator. Do not retrofit criteria after a run or infer physical state from the symbolic count.

## PI/KEY and gate

The existing Charles PI/KEY record defines `PI ≡ KEY` as a symbolic relation only; it supplies no key bytes, cryptographic signature, access authority, or physical authorization. The current conversational sequence `Pi → No → Key → Go → Correlate → Latch → Lock → Authorize → Commit` preserves this correction as a conversation-level checkpoint. It does not prove a special hidden state mechanism. The user's authorization applies to this append-only record and does not establish a physical-run authorization, field measurement, or independent Echo.

TCGE for the image arithmetic: R = visible displayed values; I = recomputation; E = arithmetic cross-check only within the same displayed input. For the physical `111` claim, E is not established; **GATE = HOLD**, **physical 111 = NOT ESTABLISHED**, **physical LATCH = NOT AUTHORIZED**. Future evidence must be appended, not backdated into this checkpoint.

Next admissible physical step: obtain and authenticate the underlying fixture schedule; resolve the 21.0/22.5 discrepancy; define and freeze the actuator/path map, protocol and criteria before execution; then acquire untouched logs/measurements with provenance and submit them to sufficiently independent validation before re-running the gate.
