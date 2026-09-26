# U Authenticator Main

Status: DEPLOYED
Branch: main

## Purpose

U Authenticator is the governed authentication gate for user-authorized connector workflows.

## Flow

USER REQUEST
-> U AUTHENTICATOR
-> AUTHORIZATION CHECK
-> CONNECTOR AVAILABILITY CHECK
-> PROVIDER AUTHENTICATION
-> VERIFY
-> TCGE GATE
-> PASS / HOLD
-> REPORT

## Rules

- User intent is required but is not proof of provider authentication.
- A repository record is not proof that an external account is connected.
- Provider authentication must occur through the provider's supported authentication flow.
- Missing connector, missing provider session, or failed verification => HOLD / 0.
- Verified provider session plus authorized operation => PASS / 1 for that scoped operation only.
- Never upgrade HOLD to PASS from a declaration alone.

## Secrets boundary

U Authenticator does not request, store, commit, or transmit:
- passwords
- seed phrases
- private keys
- recovery phrases
- PINs
- API secrets
- access tokens

Authentication secrets stay within the supported provider authentication flow.

## Coinbase state

Repository Coinbase adapter: present.
Live Coinbase connector: unavailable / not connected.
Therefore Coinbase authentication remains HOLD / 0 until a supported connector and provider session exist.

## TCGE

K = R AND I AND E

Authorization != authentication.
Authentication != account ownership proof outside the authenticated provider scope.


## Connection provider role

U provides the governed connection handoff for supported connectors.

Flow:

U
-> DISCOVER SUPPORTED CONNECTOR
-> USER AUTHORIZATION
-> PROVIDER LOGIN / OAUTH
-> CONNECT
-> VERIFY SESSION
-> RETURN CONNECTION STATE

U may route and verify supported connections, but it does not create credentials, bypass provider authentication, or claim a connection exists before the provider confirms it.

Connection state:
- SUPPORTED + AUTHENTICATED -> CONNECTED / 1
- SUPPORTED + NOT AUTHENTICATED -> HOLD / 0
- CONNECTOR UNAVAILABLE -> HOLD / 0
