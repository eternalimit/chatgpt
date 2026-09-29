# Villatherm Low-Cost Science Prototype Control Fix

Date: 2026-09-29
Status: DESIGN / HOLD
Scope: science-side prototype. Field verification required before installation.

## Frozen architecture

- Air control: motorized damper.
- Refrigerant control: electronic expansion valve (EEV), kept on the existing refrigerant rail.
- Whole-house fan: separate ventilation/exhaust branch.
- Mini-splits: independent refrigerant systems; coordination is by data/control only unless a manufacturer-approved interface is verified.
- Custom 3D part: air-side coupler/adapter only. No 3D-printed pressure-containing refrigerant component.

## Low-cost control loop

UPSTAIRS TEMP ----\
DOWNSTAIRS TEMP ---+--> ESP32 --> DAMPER DRIVER --> MOTORIZED DAMPER --> AIR PATH
DUCT TEMP ---------+
STATIC PRESSURE ---/

No laptop or phone is required for the control loop.

The damper driver must match the selected actuator. A relay is not assumed. On/off, power-open/power-close, 0-10 V, proportional, PWM, or other actuator types require the appropriate interface.

## Procurement rule

Choose the motorized damper first, record its voltage and control specification, then select/design the driver. Do not buy the driver before the actuator interface is known.

## Cost target

Hard prototype parts ceiling: USD 350.
Preferred procurement gate: USD 300, preserving roughly USD 50 contingency.

Reuse existing Villatherm, mini-splits, whole-house fan, ductwork, tools, and power hardware where appropriate.

## Evidence boundary

CAD/control design = inference.
Bench and field measurements = Reality evidence.
Independent field verification = Echo.
No field approval, HVAC compliance, physical performance, or refrigerant-system modification is claimed by this design record.

TCGE: DESIGN / HOLD.
