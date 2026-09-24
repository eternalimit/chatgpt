# PROJECT LOGS BLOCK 061 — Residential Water Distribution Correlation

Date: 2026-09-24
State: COMMITTED / APPEND-ONLY

## Parent context

Engineering branch:
`UNIVERSAL_3_BIT_FLUID_JUNCTION`

Related Block 061 record:
`project-logs/PROJECT_LOGS_BLOCK_061-eev-physical-reference-correlation.md`

## Direct evidence received

Current-session user supplied:
- two residential water-service / fixture-distribution diagrams;
- `water supply sizing copy.docx`, three pages.

The supplied document states that residential water-supply sizing uses fixture units / probable demand rather than simply summing every fixture's full GPM because fixtures are not assumed to operate simultaneously.

It gives an example totaling approximately 21 fixture units, then directs conversion through the applicable water-supply fixture-unit table to probable demand in GPM.

The document identifies these service-sizing dependencies:
- available pressure at the meter;
- elevation difference;
- service length;
- number of fittings;
- required pressure at the most remote fixture;
- meter size;
- pipe material;
- maximum allowable pressure loss.

Its simplified pressure relation is:

```text
Available pressure - elevation loss - pipe/friction loss
>= required residual pressure
```

The document gives elevation pressure loss as approximately:

```text
0.433 psi x elevation in feet
```

The example distribution arrangement is:

```text
Water meter -> 1-inch service -> 3/4-inch main -> 1/2-inch individual fixture branches
```

The source explicitly warns that this example is not automatically correct and that actual sizing must be verified from demand and pressure-loss calculations.

The source also treats hot-water piping separately from the cold-water service.

## Engineering correlation

Source architecture:

```text
SOURCE / METER
  -> SERVICE
  -> MAIN TRUNK
  -> DISTRIBUTION JUNCTIONS
  -> BRANCHES
  -> FIXTURE PATHS
  -> DEMAND
```

Candidate U3BFJM architecture:

```text
SOURCE
  -> 3-BIT SELECTOR
  -> ACTUATED VALVE ARRAY
  -> MANIFOLD
  -> TRUNK / BRANCH NETWORK
  -> END POINTS
```

Candidate dynamic chain:

```text
3-BIT STATE
  -> SELECTED PATH COUNT P
  -> VALVE / GATE CONFIGURATION
  -> ACTIVE BRANCH TOPOLOGY
  -> PROBABLE DEMAND
  -> PRESSURE / FLOW CALCULATION
  -> END-POINT PERFORMANCE
```

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

The binary state defines the candidate connectivity rule. It does not by itself establish adequate hydraulic performance.

## EEV + distribution correlation

Previous EEV reference branch:

```text
CONTROL
  -> ACTUATOR
  -> VALVE POSITION
  -> FLOW THROUGH A PATH
```

Current water-distribution branch:

```text
SOURCE
  -> MAIN
  -> BRANCH NETWORK
  -> DOWNSTREAM LOADS
```

Combined candidate architecture:

```text
SOURCE
  -> 3-BIT CONTROL
  -> ACTUATED VALVE ARRAY
  -> MANIFOLD
  -> BRANCHED DISTRIBUTION
  -> LOADS
  -> PRESSURE / FLOW FEEDBACK
```

This is an engineering correlation. The supplied residential sizing material does not demonstrate the U3BFJM 000-111 / 1-8 connected-path machine.

## Physical variables that remain required

For each selected topology, physical performance depends on variables including:
- probable/simultaneous demand;
- pipe diameter;
- pipe length;
- fittings;
- elevation;
- source pressure;
- required residual pressure;
- pipe material;
- allowable pressure loss;
- downstream load.

Therefore:

```text
CONNECTIVITY STATE != HYDRAULIC PERFORMANCE
```

## TCGE

Reality (R):
- Two current-session water-distribution diagrams were directly supplied.
- The three-page water-supply sizing document was directly supplied and inspected.
- Its fixture-unit, probable-demand, pressure, elevation, sizing, branch, and hot-water statements are source evidence within this record.

Inference (I):
- Mapping residential branched distribution onto U3BFJM is an engineering correlation.
- Combining that branch with the earlier EEV actuation branch is a candidate architecture.

Echo (E):
- No independent validation of the specific U3BFJM 3-bit multi-path implementation is established by these materials.
- No physical 000-111 test sequence, measured hydraulic response, or independent engineering validation is established.

Knowledge boundary:
- The supplied sources support real water-distribution sizing concepts.
- They do not establish that the proposed U3BFJM implementation works physically.

## Governance state

`GROUNDED INFERENCE / PHYSICAL IMPLEMENTATION UNVALIDATED`

No physical 111 is established.
No experimental success is established.
No code-compliance determination is established.

## Continuation

Next admissible engineering operation:
1. Freeze the actual branch topology for each of the eight binary states.
2. Assign physical pipe/port geometry to every path.
3. Freeze source pressure, elevation, fluid, pipe material, lengths, fittings, and downstream loads.
4. Calculate the pressure/flow envelope for each state.
5. Define measurable observables and pass/fail criteria.
6. Execute physical testing only when actual hardware/acquisition evidence exists.
7. Append results without rewriting this record.

## Signature

This is Richard Stein.
