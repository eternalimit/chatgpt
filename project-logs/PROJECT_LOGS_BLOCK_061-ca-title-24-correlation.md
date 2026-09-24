# PROJECT LOGS BLOCK 061 — California Title 24 Correlation

Date: 2026-09-24
State: COMMITTED / APPEND-ONLY
Parent block record: `project-logs/PROJECT_LOGS_BLOCK_061-california-code-workbench-commit.md`

## Correlation object

Engineering branch:
`UNIVERSAL_3_BIT_FLUID_JUNCTION`

Regulatory branch:
`CA_TITLE_24_2025`

### Candidate correlation

- P03 Electrical -> controller, motor/actuator, wiring, sensors where applicable.
- P04 Mechanical -> primary candidate branch for refrigeration, mechanical equipment, piping, valves, materials, pressure/safety, and installation.
- P06 Energy -> HVAC controls, efficiency, performance, CBECC, and verification where applicable.
- P09 Fire -> applicable fire/life-safety requirements.
- P11 CALGreen -> applicable green-building requirements.
- P12 Referenced Standards -> external standards incorporated or referenced by the governing Title 24 part.

## Component correlation

| Engineering object | Candidate regulatory branch |
| --- | --- |
| 3-bit logic | P03 / P06 when used for electrical or energy control |
| Stepper/controller | P03 |
| EEV | P04 |
| Refrigerant manifold | P04 |
| Refrigerant piping | P04 |
| Pressure containment | P04 plus referenced standards as applicable |
| Sensors | P03 / P04 / P06 depending on function |
| HVAC control algorithm | P06 |
| Energy performance | P06 / CBECC |
| Fire/life safety | P09 when applicable |
| External referenced standards | P12 plus standards referenced by governing part |

## Frozen workbench index pattern

`CA24-2025 / P04 / <CHAPTER> / <SECTION> / <REQUIREMENT> / U3BFJM / <COMPONENT> / <TEST> / <EVIDENCE>`

Illustrative unresolved path:

`CA24-2025 / P04 / <REFRIGERATION-SECTION> / <VALVE-REQUIREMENT> / U3BFJM / EEV / TEST-001 / EVIDENCE-001`

Placeholders MUST remain unresolved until authoritative section-level source text is retrieved and applicability is established.

## TCGE boundary

R: California Title 24 identifies distinct Building Standards Code parts, including Mechanical and Energy code domains.
I: Mapping individual U3BFJM components to those regulatory domains is a candidate applicability correlation.
E: No independent code review, AHJ determination, inspection, or physical compliance test is established by this record.
K: No machine-level California code compliance claim is established.

A GitHub commit freezes this correlation record only. It does not establish code compliance, product approval, listing, certification, or physical validation.

## Signature

This is Richard Stein.

## Continuation

Resolve authoritative 2025 Part 4 section-level requirements before replacing any chapter, section, or requirement placeholder. Append future evidence rather than rewriting this historical correlation.
