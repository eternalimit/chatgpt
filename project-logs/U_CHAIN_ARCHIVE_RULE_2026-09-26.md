# U-Chain Archive Rule

Date: 2026-09-26

## Core rule

Every point `•` creates one data record on the archive.

```text
U0 -> •0 -> Data0 -> Archive0
U1 -> •1 -> Data1 -> Archive1
U2 -> •2 -> Data2 -> Archive2
...
```

Invariant:

```text
forall •n: CREATE(Datan) AND APPEND(Archive, Datan)
```

Archive flow:

```text
POINT -> DATA -> HASH -> INDEX -> ARCHIVE
```

## Governance boundary

- This commit establishes the architecture definition.
- It does not by itself prove that a live archive service is running.
- It does not establish that any point, data record, or archive entry has monetary value.
- External or monetary claims remain subject to TCGE verification.
