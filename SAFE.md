# SAFE

Status: ACTIVE

Purpose: Non-custodial Bitcoin address registry for this repository.

## Rules

- Store public Bitcoin addresses only.
- Never store a private key, seed phrase, recovery phrase, xprv, signing secret, or wallet password.
- A GitHub record does not itself hold or control Bitcoin.
- Ownership/control of any listed address must be verified outside GitHub by the wallet holder.

## MOXY

Status: LOCKED
Role: Inner protective layer inside SAFE.

MOXY rules:
- Preserve SAFE contents by default.
- Read / verify / compare / report are allowed.
- Write operations require a clear, specific instruction.
- Delete / erase / wipe / reset / overwrite are blocked by default.
- Ambiguous shorthand does not authorize mutation.
- No private key, seed phrase, password, recovery phrase, xprv, or signing secret may be stored.
- Existing committed history remains preserved.

## Bitcoin

Network: mainnet
Public address: UNASSIGNED
Custody: EXTERNAL / USER-CONTROLLED
Balance: UNVERIFIED

## Verification

A balance becomes VERIFIED only after:
1. a public Bitcoin address is assigned here, and
2. its on-chain balance is independently checked.

SAFE_V1
MOXY_V1
