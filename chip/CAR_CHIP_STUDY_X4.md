# TCGE Car Chip Study x4

Status: concept / RTL prototype planning only. Not automotive-qualified silicon.

## Pass 1 — Safety

Design goals:
- Dual redundant compute paths
- Lockstep result comparison
- Sticky fault latch
- Watchdog timeout
- Fail-silent output behavior
- Explicit reset/recovery path
- No direct actuator control in the prototype

## Pass 2 — Compute

Base engine:
- TCGE branching-tee core
- 7 levels
- 127 total nodes
- 64 leaves
- Deterministic split / evaluate / resolve

Automotive adaptation:
- Instantiate two identical branching engines
- Feed the same input to both
- Compare valid/data outputs
- Any mismatch => fault

## Pass 3 — Vehicle Interface

Prototype boundary:
- Generic command/data input
- Generic status/result output
- Vehicle buses are intentionally abstracted

Future interface targets:
- CAN / CAN FD / CAN XL
- Automotive Ethernet
- SPI / UART / LIN where appropriate

Software architecture target:
- Application layer separated from hardware-facing services
- Compatible in spirit with layered automotive ECU software design

## Pass 4 — Security / Silicon / Verification

Future requirements:
- Secure boot
- Hardware root of trust
- Key isolation
- Authenticated update
- ECC-protected memories
- Memory protection
- Clock / voltage supervision
- Fault injection testing
- CDC / RDC checks
- Formal equivalence
- Gate-level timing
- AEC-Q100 qualification path
- ISO 26262 safety case

## Build Target

`TCGE_CAR_CHIP_v0.1`

Core structure:

`INPUT -> DUAL BRANCHING TEE -> LOCKSTEP COMPARE -> SAFE RESULT`

Fault path:

`MISMATCH OR TIMEOUT -> FAULT_LATCH -> OUTPUT_SUPPRESS`

This prototype is intentionally non-actuating. It does not command brakes, steering, propulsion, or other safety-critical vehicle functions.
