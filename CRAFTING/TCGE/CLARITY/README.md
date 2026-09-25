# Clarity Coin, Wallet, and Exchange — TCGE Architecture

Status: DEFINED / NOT IMPLEMENTED / NOT DEPLOYED

## Hierarchy

```text
TCGE/
└── CLARITY/
    ├── COIN/
    │   ├── SPEC/
    │   ├── SUPPLY/
    │   ├── LEDGER/
    │   ├── TRANSACTION/
    │   ├── VALIDATION/
    │   └── AUDIT/
    ├── WALLET/
    │   ├── ADDRESS/
    │   ├── PUBLIC_KEY/
    │   ├── PRIVATE_KEY/
    │   ├── SIGN/
    │   ├── VERIFY/
    │   ├── BALANCE/
    │   └── HISTORY/
    └── EXCHANGE/
        ├── MARKET/
        ├── ORDER/
        ├── MATCH/
        ├── SETTLEMENT/
        ├── LEDGER/
        ├── PROVENANCE/
        └── AUDIT/
```

## Coin transaction rule

```text
TX = (FROM, TO, AMOUNT, NONCE)
SIGN_private(TX) → VERIFY_public(TX) → VALIDATE → LEDGER
```

## Wallet boundary

```text
PRIVATE KEY != ADDRESS
```

Private keys must never be stored in GitHub, public provenance records, or public audit output.

## Exchange execution chain

```text
BUY + SELL → MATCH → EXECUTE → SETTLE → LEDGER → AUDIT
```

```text
ORDERED != MATCHED != EXECUTED != SETTLED
```

## TCGE evidence chain

```text
REQUIREMENT → METHOD → DETECT → OBSERVE → EVIDENCE → RESULT
```

Allowed result states:

- VERIFIED
- FALSIFIED
- UNVERIFIED

## Evidence boundary

```text
DEFINED != IMPLEMENTED != TESTED != DEPLOYED
```

This document defines a prototype architecture only. It does not issue a token, generate wallet keys, operate a financial exchange, establish market value, or claim regulatory approval.
