# CAGE

Status: LOCKED

Purpose: Protective control layer for code.core.code and related repository state.

## Default policy

- READ: ALLOWED
- VERIFY: ALLOWED
- COMPARE: ALLOWED
- REPORT: ALLOWED
- WRITE: BLOCKED unless explicitly authorized
- DELETE / ERASE / WIPE / RESET: BLOCKED
- FORCE / OVERWRITE / REWRITE HISTORY: BLOCKED
- SECRET EXPOSURE: BLOCKED

## Protected terms

The following words or similar commands must NOT mutate protected code by themselves:

wipe
erase
delete
remove
reset
undo
archive
release
mutate
transform
regenerate
reconstruct
bind
couple
merge
lock
latch
gate
commit
commit all
authorize commit all

## Authorization rule

No protected write may occur unless the user gives a clear, specific instruction identifying:
1. the exact target,
2. the exact change,
3. the intent to write/commit that change.

Ambiguous shorthand is treated as NON-AUTHORIZATION.

## Preservation rule

Existing committed history must remain preserved.
Changes create a new revision.
FALSIFIED != ERASE.
UNVERIFIED != DELETE.

## Scope

Protected object: code.core.code
Repository: eternalimit/chatgpt

CAGE_V1


## REDx chain rule

Default representation for chain-related protected content: [REDx]

Rules:
- Chain-related protected terms, mappings, and internal meanings remain redacted as [REDx] by default.
- Do not infer, reconstruct, expand, or reveal redacted meanings.
- Only an explicit instruction from the user may authorize replacing [REDx] with specific content.
- Ambiguous shorthand does not count as authorization.
- Existing Git history remains preserved; this rule governs current and future repository handling, not retroactive history rewriting.

REDX_CHAIN_V1


## Resolution

Designated repository controller: Richard Stein

Scope:
- Repository-side authority for protected SAFE / CAGE / [REDx] records resolves to Richard Stein.
- Protected chain contents remain represented as [REDx] unless Richard Stein explicitly instructs otherwise.
- This declaration does not by itself prove ownership or control of any on-chain Bitcoin address, private key, or funds.

RESOLVE_TO_RICHARD_STEIN_V1
