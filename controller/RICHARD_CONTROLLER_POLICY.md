# Richard GitHub Controller Policy

Root: Anchor 1
Controller: GitHub
Principal: Richard
Status: CONTROL SPECIFICATION

## Rule
NO VALID RICHARD AUTHORIZATION -> NO EXTERNAL EXECUTION.

The controller must distinguish:
DRAFT -> AUTHORIZED -> EXECUTED -> INDEPENDENTLY VERIFIED -> RECEIPT -> PRESERVE.

## Authorization
An execution request is valid only when the GitHub controller can attribute the approval to the configured Richard authorization principal under repository controls.

Text that merely says "Richard authorized" is not sufficient by itself.

For higher-assurance operations, require a verifiable cryptographic signature from a public key registered by Richard. Private signing material must never be committed to this repository.

## Security
PUBLIC DATA MAY FLOW.
SECRETS STAY IN THE WALLET.
UTILITY MUST NOT REDUCE FIDELITY.

Never commit seed phrases, private keys, recovery words, passwords, PINs, API secrets, or wallet signing credentials.

## Control flow
RICHARD
-> GITHUB CONTROLLER
-> AUTHENTICATE
-> AUTHORIZE
-> POLICY GATE
-> EXECUTE
-> INDEPENDENTLY VERIFY
-> RECEIPT
-> PRESERVE
-> ANCHOR 1

## Failure rule
If identity, authorization, scope, destination, amount, or required evidence is unresolved:
DENY EXECUTION / HOLD THAT ACTION.

## Scope
This specification defines repository-side authorization intent and evidence requirements. Actual enforcement requires GitHub repository permissions/rules and any external execution service to enforce this policy.
