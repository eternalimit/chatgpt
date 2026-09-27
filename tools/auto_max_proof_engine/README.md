# AUTO MAX Proof Engine

A local evidence-packaging prototype.

## Flow

`Artifact → SHA-256 → UPID → Timestamp → Receipt → Sealed Package`

## Run

```bash
pip install -r requirements.txt
streamlit run app.py
```

## Output

For every uploaded artifact the app creates:
- SHA-256 hash
- deterministic UPID (`AUTO-<first 12 hex chars>`)
- UTC timestamp
- JSON receipt
- SHA256SUMS.txt
- sealed ZIP containing the original artifact and receipt

## Core state

- STATE: 1
- ANCHOR: •
- BIND: 379999

## Evidence boundary

A hash proves integrity of the exact bytes hashed.
This prototype does not create a legal ownership claim, wallet signature, blockchain transaction, or payment receipt.
