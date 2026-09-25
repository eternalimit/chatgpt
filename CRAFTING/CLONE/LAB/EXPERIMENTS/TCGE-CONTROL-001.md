# TCGE CONTROL EXPERIMENT 001

Status: COMPUTATIONAL RESULT

## Model

m*x'' + c*x' + k*x = F(t)

- Mass: 1,000 kg
- Spring stiffness: 20,000 N/m
- Impulse amplitude: 1,000 N
- Impulse duration: 0.01 s
- Time step: 0.001 s
- Simulation duration: 5 s

## Conditions

CONTROL:
c = 0 Ns/m

DAMPED:
c = 3,000 Ns/m

Only damping was changed between conditions.

## Measured results

Control peak displacement: 0.1535 m
Damped peak displacement: 0.0992 m
Peak reduction: 35.4%

The independently regenerated run produced:

Control RMS displacement: 0.0984 m
Damped RMS displacement: 0.0256 m
RMS reduction: 74.0%

## TCGE result

Within this computational model, the damping condition reduced modeled displacement under the identical simulated disturbance.

Result:

VERIFIED — WITHIN THE SPECIFIED COMPUTATIONAL MODEL

## Evidence boundary

MODEL RESULT != PHYSICAL VEHICLE VALIDATION

The experiment does not establish that a physical vehicle will exhibit the same response. Physical validation would require a separately controlled physical test and measurement.
