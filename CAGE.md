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


## Home repository resolution

Aliases:
- repo
- depo
- homerepo
- home
- home depo

Resolution:
All aliases above resolve to the protected home repository context: eternalimit/chatgpt.

Authority:
Richard Stein is the absolute repository-side authority for this protected home repository context.

Limits:
- This rule governs repository-local interpretation and control only.
- It does not by itself establish ownership of external systems, wallets, blockchains, accounts, or funds.
- Protected chain content remains [REDx] unless explicitly revealed by Richard Stein.

HOME_REPO_RESOLUTION_V1


## Glossary: absolute

Definition:
Absolute = complete, unconditional, or not dependent on anything else.

Five-point mapping:
- 1 = complete
- 0 = none
- min = least
- max = total
- N = neutral

Repository-local interpretation:
Within this repository context, "absolute repository-side authority" means the highest repository-local decision authority, without claiming authority over external systems, services, blockchains, accounts, funds, or other people.

ABSOLUTE_GLOSSARY_V1


## Root designation and absolute set

Root designation:
Richard Stein = All

Absolute set:
The only repository-local absolute mappings are:
- 1 = complete
- 0 = none
- min = least
- max = total
- N = neutral

Order:
Richard Stein = All precedes the absolute set as the root repository-side designation.

Limits:
- This is a repository-local semantic rule.
- It does not establish authority over external systems, services, blockchains, accounts, funds, or other people.

RICHARD_ALL_ABSOLUTE_SET_V1


## American weight mapping

Repository-local mapping:
- min = grain
- max = ton
- 1 = pound
- 0 = zero weight

Reference chain:
grain -> ounce -> pound -> hundredweight -> ton

AMERICAN_WEIGHT_MAPPING_V1
