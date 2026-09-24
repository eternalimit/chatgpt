# PROJECT LOGS BLOCK 061 — EEV Physical Reference Correlation

Date: 2026-09-24
State: COMMITTED / APPEND-ONLY

## Parent context

Engineering branch:
`UNIVERSAL_3_BIT_FLUID_JUNCTION`

Regulatory branch:
`CA_TITLE_24_2025`

Related records:
- `project-logs/2026-09-24-universal-3-bit-fluid-junction-machine.md`
- `project-logs/PROJECT_LOGS_BLOCK_061-ca-title-24-correlation.md`
- `project-logs/PROJECT_LOGS_BLOCK_061-dpof-ca-title24-v1.md`

## Evidence received

Current-session user supplied two expansion-valve reference images and the external reference URL:

`https://theengineeringmindset.com/how-electronic-expansion-valves-work/`

The first supplied diagram labels:
- Stepper motor
- Needle valve
- Valve seat
- Liquid refrigerant inlet
- Gas refrigerant outlet

The second supplied diagram depicts a mechanically actuated expansion-valve cross-section with labeled inlet, outlet, port, and undercut pin.

These references are preserved as source/reference evidence. The two valve mechanisms are not declared identical.

## Engineering correlation

The EEV reference supports the following candidate physical decomposition:

```text
CONTROL SIGNAL
  -> STEPPER MOTOR
  -> ROTATIONAL MOTION
  -> LINEAR NEEDLE DISPLACEMENT
  -> NEEDLE / SEAT OPENING
  -> FLOW RESTRICTION
  -> REFRIGERANT FLOW RESPONSE
```

Candidate U3BFJM integration:

```text
3-BIT STATE
  -> CONTROL DECISION
  -> ACTUATOR COMMAND(S)
  -> VALVE POSITION(S)
  -> CONNECTED FLOW GEOMETRY
  -> MEASURED FLUID RESPONSE
```

The EEV is treated as a candidate electromechanical actuation primitive within the larger U3BFJM architecture. This record does NOT establish that an EEV implements the frozen 000-111 / 1-8 connected-path architecture.

## Frozen 3-bit contract

```text
N = 4b2 + 2b1 + b0
b2,b1,b0 in {0,1}
N in {0,1,2,3,4,5,6,7}
P = N + 1

000 -> N=0 -> P=1 connected path
001 -> N=1 -> P=2 connected paths
010 -> N=2 -> P=3 connected paths
011 -> N=3 -> P=4 connected paths
100 -> N=4 -> P=5 connected paths
101 -> N=5 -> P=6 connected paths
110 -> N=6 -> P=7 connected paths
111 -> N=7 -> P=8 connected paths
```

No physical transition or physical 111 is established by this commit.

## Title 24 candidate mapping

| Engineering object | Candidate regulatory branch |
| --- | --- |
| Stepper/controller | P03 / P04 as applicable |
| EEV / needle / seat | P04 |
| Refrigerant piping | P04 |
| Sensors | P03 / P04 / P06 depending on function |
| HVAC control algorithm | P06 |
| Energy performance | P06 / CBECC |

These remain candidate applicability correlations. Section-level applicability and compliance remain unresolved.

## TCGE boundary

Reality (R):
- Current-session supplied diagrams are direct visual reference evidence.
- The external Engineering Mindset URL was supplied as a reference.
- Existing Block 061 U3BFJM and Title 24 records establish the project correlation framework.

Inference (I):
- Mapping the EEV mechanism into the U3BFJM actuation layer is an engineering correlation.
- Mapping individual components to Title 24 Parts remains candidate applicability reasoning.

Echo (E):
- No independent validation of the specific U3BFJM 3-bit multi-path implementation is established by this commit.
- No AHJ determination, inspection, physical compliance test, or machine-level code determination is established.

Knowledge boundary:
- Basic reference evidence does not establish the proposed U3BFJM implementation.
- Git commit identity does not establish physical validation or code compliance.

## Governance state

`GROUNDED INFERENCE / PHYSICAL IMPLEMENTATION UNVALIDATED`

This commit freezes the correlation and evidence boundary only.

## Continuation

Next admissible work:
1. Resolve authoritative Title 24 section-level provisions applicable to the EEV/control/piping architecture.
2. Freeze physical EEV/actuator requirements and interface dimensions.
3. Define the mapping from each 3-bit state to specific actuator/valve commands.
4. Define measurable flow/pressure observables and pass/fail criteria.
5. Execute physical testing only when actual hardware and acquisition evidence are available.
6. Append resulting evidence without rewriting this record.

## Signature

This is Richard Stein.
