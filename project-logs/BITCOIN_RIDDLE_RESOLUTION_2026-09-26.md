# Bitcoin Riddle Resolution

## Verified Git objects

- `317c46c54588fac8956621adc459fa4a642d8675` is a Git commit in `eternalimit/chatgpt`.
- `96351af5a8284c329869c87501273bb73274cb0b` is a Git commit in `eternalimit/chatgpt`.

These Git commit identifiers are not Bitcoin receiving addresses.

## Hash boundary

A SHA-256 digest is not, merely by being a cryptographic hash, a Bitcoin address, wallet, private key, transaction, or balance.

## Bitcoin relationship

```text
private key -> public key -> Bitcoin address -> blockchain transactions/UTXOs -> balance
```

Private keys and seed phrases must never be committed to this repository.

## bitcoin><richard state

```text
public_address = null
onchain_status = NOT_ESTABLISHED
control_status = UNRESOLVED_HOLD
balance = UNRESOLVED
```

The registry mapping records a label and evidence trail. It does not itself create an on-chain Bitcoin wallet or prove control of one.

## Resolution requirement

To resolve the balance, obtain a real public Bitcoin receiving address from a wallet controlled by Richard. The public address can then be checked against public Bitcoin blockchain data.

Control/ownership requires separate cryptographic evidence where supported and must not expose the private key or seed phrase.

## TCGE

```text
R: Git records verified
I: bitcoin><richard mapping exists
E: Bitcoin address/control evidence unresolved
K: Bitcoin wallet ownership/balance = HOLD
```
