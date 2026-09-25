# CLONE GitHub Hierarchy Commit

Date: 2026-09-25
Status: AUTHORIZED WORKING MODEL / APPEND-ONLY

## GitHub hierarchy

```text
GitHub
└── Organization / Owner
    └── Repository
        ├── Branch
        │   └── Directory
        │       └── File / Artifact
        └── Commit History
            └── Commit
                └── Change
```

## CLONE mapping

```text
KEEPER
└── Repository
    ├── HOLD = committed authoritative history
    ├── ADDER = contributor
    ├── ADD = proposed change
    ├── CRAFT = develop solution
    ├── BUILD = create artifact
    ├── PRODUCE = execute/output
    └── TCGE = evidence gate before promotion
```

Working relationship:

`Adder changes -> Keeper governs -> Git records -> Commit holds`

Extended conceptual hierarchy:

`ROOT -> KEEPER -> MODEL -> ADDER -> CRAFT -> BUILD -> PRODUCE -> TCGE -> HOLD -> COMMIT`

## Governance boundary

Git/GitHub provides durable versioned history and byte-addressable artifacts, but a commit does not independently prove that an engineering, construction, code, or physical claim is true. TCGE evidence status remains separate from repository state.

This checkpoint extends, and does not rewrite, the prior CLONE Craft / Keeper / TCGE working architecture.
