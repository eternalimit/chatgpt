# SCOUT -> BUZZ -> RECO

Date: 2026-09-26

Architecture:

SCOUT -> OBSERVE -> BUZZ -> VERIFY -> RECO -> HUMAN AUTHORIZE -> ACT

Definitions:

- SCOUT: finds and observes external blockchain data.
- BUZZ: turns a new observation into a structured event.
- VERIFY: checks the event against available evidence and preserves unresolved boundaries.
- RECO: produces a recommendation or next action without treating observation alone as proof of wallet ownership or control.
- HUMAN AUTHORIZE: requires explicit human approval before action.
- ACT: performs the authorized action through the appropriate connected system.

Evidence boundary:

Observation, recommendation, and Git records do not themselves create an on-chain transaction or prove wallet ownership. On-chain actions require the appropriate network, wallet/control authority, signing, and broadcast.
