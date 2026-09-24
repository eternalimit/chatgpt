# California Building-Code GitHub Workbench Sources

Purpose: preserve external GitHub sources relevant to California building-code, energy-code, statutory, and automated compliance research without copying or merging their contents into this repository.

## Upstream repositories

### California Energy Commission — CBECC
- Repository: https://github.com/california-energy-commission/CBECC
- Role: California Building Energy Code compliance software and machine-processable energy-compliance tooling.
- Authority boundary: useful official CEC source for its covered energy-compliance domain; not a substitute for all parts of California Title 24.

### Open Construction Stack — building-codes
- Repository: https://github.com/open-construction-stack/building-codes
- Role: machine-readable building-code adoption/edition information.
- Authority boundary: third-party dataset; verify applicability against official California and local sources.

### Building Plan Compliance Checker
- Repository: https://github.com/srinandan/building-permit
- Role: experimental software architecture for automated building-plan/code review.
- Authority boundary: example/research implementation, not an authoritative California code source.

### California statutory codes dataset
- Repository: https://github.com/johnakelly-yahoo-com/california-codes
- Role: machine-readable/plain-text California statutory-code dataset derived from legislative data.
- Authority boundary: California statutes are distinct from the California Building Standards Code (Title 24); this repository does not replace Title 24.

## Workbench integration rule

External repositories remain upstream references. Their content, licenses, histories, and provenance are not silently copied into `eternalimit/chatgpt`.

Candidate governed compliance pipeline:

`DESIGN -> APPLICABLE CODE -> REQUIREMENT -> TEST -> EVIDENCE -> COMPLIANCE STATUS`

For every material compliance claim, record the code edition, jurisdiction, authoritative source, section/rule, interpretation, test/inspection evidence, and independent validation where required.

## TCGE boundary

A repository link establishes only the referenced upstream location. It does not establish that every statement or rule in that repository is current, applicable, authoritative, or independently validated. Compliance conclusions remain unresolved until the applicable authoritative code and jurisdiction are verified.
