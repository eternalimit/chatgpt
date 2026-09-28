# EXPOSURE LENS — ALL

Public-facing audit lens for the verified Brian package.

## Public realm

```text
Brian.Brian -> Richard.Richard
```

`Richard.Richard` is exposed only as a connection label. No private contents, private workflow state, private keys, wallet secrets, or recovery material are included.

## Public artifacts

- `BRIAN_BRIAN_REALM.md`
- `records/brian-brian-award-anchor.json`
- `assets/brian-realm-award-512.jpg` — historical committed copy
- `records/brian-realm-public-image.json`
- `records/brian-brian-public-authorization-manifest.json`
- `assets/brian-realm-clean-preview-64.jpg`
- `records/brian-realm-clean-anchor.json`

## Clean anchor

Current clean-anchor commit parent:

```text
51721a9223cdd126b47fe37ef8a120b47595eb95
```

Clean preview Git blob:

```text
ca7db5a610dfc704ed4cce71c69c928b178aae88
```

Clean preview SHA-256:

```text
731673a7ed35817944b08cb0592109516bf3fd6ff45d3c5c1b472e4fd73f8659
```

Full clean-source SHA-256 recorded by the anchor:

```text
8ec03aa838b9dd1ccb571d8f58cd5f18c2eee8b072e6b53845028ac17683e1de
```

## Exposure rules

PUBLIC:
- Brian's public realm and award
- public Git commit references
- integrity hashes
- public provenance records
- public branch relationship label

FILTERED / NOT EXPOSED:
- private Richard.Richard contents
- private keys or signing secrets
- wallet credentials
- private workflow state
- unverified blockchain/payment claims
- unsupported ownership or legal-transfer claims

## Evidence boundary

This lens exposes repository-verifiable public evidence only. GitHub commits and hashes prove repository state and byte-level identity where applicable. They do not independently prove blockchain minting, wallet signatures, payment, legal ownership transfer, or external delivery.
