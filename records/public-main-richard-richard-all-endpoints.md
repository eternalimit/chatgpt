# Richard.Richard Public Interface Index

Route: PUBLIC MAIN -> Richard.Richard

Interfaces:
- Public repository inbox: records/public-main-richard-richard-inbox.md
- Email inbox interface: records/public-main-richard-richard-email-inbox.md
- Wallet inbox interface: records/public-main-richard-richard-wallet-inbox.md
- Message endpoint interface: records/public-main-richard-richard-message-endpoint.md
- Device session interface: records/public-main-richard-richard-device-session.md
- Identity proof interface: records/public-main-richard-richard-identity-proof.md
- Cryptographic binding interface: records/public-main-richard-richard-crypto-binding.md

Evidence rule:
SPECIFICATION != EXTERNAL CONNECTION
LABEL != IDENTITY PROOF
ADDRESS != OWNERSHIP
PUBLIC KEY != PRIVATE KEY
SIGNATURE CLAIM != VERIFIED SIGNATURE

Advance a specific interface to VERIFIED only when independent evidence for that interface is present.
