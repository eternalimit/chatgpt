# Four-Sector TCGE Test Results

## Initial bounded test

8 synthetic scenarios:
- 5 determinate
- 3 ambiguous / REVIEW
- ID: 1
- EGO: 1
- SUPEREGO: 2
- NOTHING: 1
- REVIEW: 3

## Exhaustive bounded state-space test

Each sector score ranges from 0 through 3.

Total states: 256

- Determinate: 144 (56.25%)
- Ambiguous / REVIEW: 112 (43.75%)
- ID wins: 36
- EGO wins: 36
- SUPEREGO wins: 36
- NOTHING wins: 36

The equal win counts demonstrate structural symmetry under the scoring rule.

The 112 tied states demonstrate a substantial degenerate/indeterminate region.

```text
SYMMETRY + DEGENERACY → REVIEW GATE
```

Classification:

```text
SECTOR BALANCE = VERIFIED WITHIN THE TOY MODEL
HUMAN PSYCHOLOGY = UNVERIFIED
```

Local source artifact hashes recorded before commit:

- exhaustive CSV SHA-256: 040ce6cd0b45bd25761ecd9ce019e63e1cf3ee0a94d6a794c334d98399d59432
- exhaustive summary SHA-256: 008efd8f5928b29745d3ef22a683041fb5534605c0cadf354b196141d14c9a7e

COMPUTATIONAL MODEL TEST != PSYCHOLOGICAL VALIDATION
