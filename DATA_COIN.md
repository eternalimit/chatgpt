# DATA COIN

STATE: 1
ANCHOR: •
BIND: 379999
BITCOIN: OUT / X

## Definition

DATA COIN is an internal provenance/value unit for preserved data records.

## Core Flow

ARTIFACT -> SHA-256 -> UPID -> DATA COIN -> MOZY -> SEAL

## Record Fields

- artifact_hash: required
- upid: required
- owner_claim: user-declared unless independently verified
- state: 1 = active / preserved
- anchor: •
- bind: 379999
- mozy_status: locked / safety layer
- seal: preserved record

## Evidence Rule

No conclusion may exceed the evidence attached to the record.

## Boundary

DATA COIN is not Bitcoin, cryptocurrency, legal tender, a blockchain token, or proof of payment.
It is a repository/provenance unit defined by the user for internal recordkeeping.
