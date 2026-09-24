# Relevant Research Index

Scope: external literature relevant to the GIVE -> GET -> THROUGH -> GATE -> GIVE -> ECHO research line.

| ID | Research | Chain relevance | Evidence role |
|---|---|---|---|
| P01 | Wilkinson et al. (2016), "The FAIR Guiding Principles for scientific data management and stewardship", Scientific Data 3, 160018. DOI: 10.1038/sdata.2016.18 | Persistent identifiers, provenance, machine-readable/reusable research objects and workflows | Supports GET / GIVE provenance concepts |
| P02 | National Academies of Sciences, Engineering, and Medicine (2019), "Reproducibility and Replicability in Science" | Distinguishes computational reproducibility from independent replication and emphasizes records, data, code, and methods | Supports distinction between reproduction/hash checks and stronger independent ECHO |
| P03 | Torres-Arias et al. (2019), "in-toto: Providing farm-to-table guarantees for bits and bytes", USENIX Security 2019 | Cryptographically records ordered software-supply-chain operations, actors, and artifacts against a predefined layout | Analogue for evidence-bearing GIVE -> GET -> THROUGH -> GATE -> GIVE transitions |
| P04 | in-toto framework/specification | Step metadata and verification of an expected supply-chain sequence | Implementation reference for machine-verifiable provenance chains |

## Indexed relationship

P01 FAIR -> artifact identity, metadata, provenance -> GIVE0 / GET

P03 + P04 in-toto -> ordered evidence-bearing transitions -> GET / THROUGH / GATE / GIVE1

P02 reproducibility and replicability -> reproduction versus independent confirmation -> GIVE1 / ECHO

## Governance boundary

These sources provide external precedent for components of the architecture. They do not, by themselves, validate TCGE, ECHO, or the combined GIVE / GET / THROUGH / GATE / GIVE formulation.

Hash verification establishes a scoped identity/integrity result. It is not automatically independent replication or independent Echo.
