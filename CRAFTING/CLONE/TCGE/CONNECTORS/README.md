# TCGE — CONNECTORS

A connector is a defined interface that allows two components, systems, or evidence domains to exchange data, signals, commands, or state without collapsing their identities.

```text
CONNECTOR(A,B,I) → LINK
```

Where:

- A = source component/system
- B = destination component/system
- I = defined interface/protocol
- LINK = bounded connection

## Hierarchy

```text
CRAFTING/
└── CLONE/
    └── TCGE/
        └── CONNECTORS/
            ├── REQUIREMENT/
            ├── SOURCE/
            ├── DESTINATION/
            ├── INTERFACE/
            ├── PROTOCOL/
            ├── AUTHENTICATION/
            ├── AUTHORIZATION/
            ├── TRANSFORM/
            ├── TRANSPORT/
            ├── VALIDATION/
            ├── OBSERVE/
            ├── LOG/
            ├── ERROR/
            ├── RETRY/
            ├── PROVENANCE/
            ├── TEST/
            ├── REVIEW/
            └── VERIFY/
```

## Core chain

```text
DEFINE
→ CONNECT
→ AUTHENTICATE
→ AUTHORIZE
→ TRANSFORM
→ TRANSPORT
→ VALIDATE
→ RECORD
→ VERIFY
```

## Connector axioms

```text
CONNECTOR != SOURCE
CONNECTOR != DESTINATION
CONNECTED != AUTHORIZED
AUTHORIZED != EXECUTED
TRANSFERRED != VALIDATED
VALIDATED != TRUE
RETRY != DUPLICATE PERMISSION
TRANSFORMED DATA != SOURCE DATA
```

## Provenance rule

Every connector event should preserve:

```text
SOURCE
+ DESTINATION
+ METHOD
+ TIME
+ INPUT
+ OUTPUT
+ RESULT
```

## Governing axiom

```text
A connector may transfer state; it may not manufacture authority, provenance, or truth.
```

## Simplified

```text
CONNECTOR = DEFINED BRIDGE BETWEEN SYSTEMS
```
