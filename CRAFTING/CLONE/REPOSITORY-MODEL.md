# Clone and Mirror Repository Model

## Physical clone

A physical clone is a copy of a repository stored on a computer.

```text
/machine/
└── chatgpt/
    ├── .git/
    ├── CRAFTING/
    └── ...
```

## Mirror repository

A mirror is a separate repository intended to preserve the source repository's Git state.

```text
GitHub
├── eternalimit/chatgpt        ← source
└── eternalimit/chatgpt-mirror ← mirror
```

## TCGE distinctions

```text
CLONE  = physical/local copy
MIRROR = separate repository preserving source state
HASH   = identity/checkpoint of specific bytes or state
```

A mirror is not automatically synchronized with its source. Correspondence must be established by comparing relevant Git state, commits, refs, or content hashes.

## Relationship

```text
ORIGINAL REPOSITORY
        ↓
   clone / copy
        ↓
PHYSICAL CLONE
        ↓
   mirror / push
        ↓
MIRROR REPOSITORY
```

## Evidence boundary

```text
CLONE != ORIGINAL
MIRROR != PROOF
HASH != TRUTH
```

## Lab / Sandbox Repository

A lab repository is an isolated workspace for experiments that are not part of the canonical repository.

\`LAB REPO = isolated workspace for experimental work\`

It may contain experiments, failed tests, prototypes, and disposable artifacts. Experimental or discarded work may still have evidentiary value, so "LAB" or "SANDBOX" is preferred over "waste repo".

\`CANONICAL REPO → LAB REPO → experiments / failed tests / prototypes\`
