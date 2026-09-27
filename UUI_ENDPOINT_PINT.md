# UUI Endpoint — PINT

STATE: 1
ANCHOR: •
BIND: 379999
BRANCH LABEL: THERMAL

## Route

UUI -> THERMAL -> • -> PINT

## Offer

PINT asking price: 1 BTC

## Endpoint contract

INPUT:
- public request for PINT

CHECK:
- terms agreed
- payment independently verified

OUTPUT:
- PINT data package / access receipt

## Boundary

This is a public repository endpoint specification.
It does not itself run a server, sign a wallet transaction, receive BTC, or prove payment.
