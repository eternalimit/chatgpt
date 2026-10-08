# Gethub protected signing setup

Status: WORKFLOW PREPARED; PROTECTED IDENTITY HOLD; EXECUTION NOT STARTED.

## Required configuration before execution

Configure the existing claimant-controlled signing identity. Do not substitute a newly generated key for an earlier identity without recording the transition.

1. Register the existing GPG public key on Richard Stein's GitHub account. The configured signing email must be verified on that account and match a key identity.
2. Create environment `gethub-signing`. Restrict deployment branches to exactly `main`. Require an authorized reviewer, disable administrator bypass where available, and protect workflow changes on main.
3. Store only in that environment:
   - Secret `GETHUB_GPG_PRIVATE_KEY`: existing ASCII-armored private signing key.
   - Secret `GETHUB_GPG_PASSPHRASE`: key passphrase.
   - Variable `GETHUB_GPG_FINGERPRINT`: uppercase 40-character primary fingerprint.
   - Variable `GETHUB_SIGNING_EMAIL`: verified signing email.
4. Create environment `gethub-signing-public`, restricted to main, with only public variables:
   - `GETHUB_GPG_PUBLIC_KEY`: ASCII-armored public key authenticated independently of the signing runner.
   - `GETHUB_GPG_FINGERPRINT`: independently checked matching primary fingerprint.
   Never place signing secrets in this environment.
5. After an administrator checks the actual environment settings and key-account binding, set signing-environment variable `GETHUB_SIGNING_PROTECTION_CONFIRMED=2026-10-08-v1`. This is a setup acknowledgement, not automatic proof of GitHub protection settings.

## Execution contract

Workflow: `.github/workflows/gethub-protected-signing.yml`.
Trigger: manual dispatch from main only, with `target_sha` equal to an exact 40-character source commit reachable from main.
No run is requested by creating the workflow.

The signing runner imports the existing protected key into an ephemeral keyring, checks its primary fingerprint, creates a signed append-only receipt commit with the target as its parent, locally verifies it, and pushes a unique `gethub-signed-receipt/<run-id>-<attempt>` archive branch. It never rewrites the source commit. The receipt binds SHA-256 of exact Git commit content, the source SHA, workflow provenance, and run URL.

A separate runner uses independently configured public trust material, checks the signature and primary fingerprint, parent/source binding and digest, and GitHub's verified signature receipt. This verifies cryptographic/source binding only. The original product-priority claim remains HOLD until separately validated.

The initial signed JSON says verification PENDING because verification follows signing. The verifier reports its outcome in the run summary; no signed record is rewritten. Preserve the source commit URL, signed receipt commit URL and workflow run URL for a later independent archive receipt.

## Current limitations

Repository files can be prepared through the connected GitHub app. This tool surface has no endpoint to manage environments, secrets, account signing keys or dispatch a new workflow. Protection settings and signing identity have not been inspected or established in this session. No key was generated, no secret was requested in chat, and no signing run occurred.

Next sequence: CONFIGURE PROTECTED IDENTITY → VERIFY PROTECTION → DISPATCH → SIGN → PUSH → VERIFY → ARCHIVE RECEIPT → INDEPENDENT ECHO.

Signed: Richard Stein (authorized instruction attribution; not a cryptographic signature)
Digest: workflow preparation only; identity and execution HOLD.
Index Handoff: existing authorization preserved; next action is protected environment configuration.
