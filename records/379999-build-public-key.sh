#!/usr/bin/env bash
set -euo pipefail

KEY_ID="${1:-bbbbdddd}"
OUT_DIR="keys"
PUB_FILE="${OUT_DIR}/${KEY_ID}.asc"
FP_FILE="${OUT_DIR}/${KEY_ID}.fingerprint.txt"

mkdir -p "${OUT_DIR}"

echo "Resolving public key for: ${KEY_ID}"

# Require an exact local key match before export.
MATCHES="$(gpg --batch --with-colons --list-keys "${KEY_ID}" 2>/dev/null | awk -F: '$1=="pub"{c++} END{print c+0}')"
if [ "${MATCHES}" -ne 1 ]; then
  echo "ERROR: expected exactly one public key match for ${KEY_ID}, found ${MATCHES}."
  echo "Use a full fingerprint if the short key ID is ambiguous."
  exit 1
fi

FINGERPRINT="$(gpg --batch --with-colons --fingerprint "${KEY_ID}" | awk -F: '$1=="fpr"{print $10; exit}')"
if [ -z "${FINGERPRINT}" ]; then
  echo "ERROR: could not resolve full fingerprint."
  exit 1
fi

echo "Fingerprint: ${FINGERPRINT}"

# Export PUBLIC key only. This command does not export secret/private key material.
gpg --batch --armor --export "${FINGERPRINT}" > "${PUB_FILE}"

if ! grep -q "BEGIN PGP PUBLIC KEY BLOCK" "${PUB_FILE}"; then
  echo "ERROR: public key export failed."
  exit 1
fi

printf '%s\n' "${FINGERPRINT}" > "${FP_FILE}"

echo
echo "Built public-key artifacts:"
echo "  ${PUB_FILE}"
echo "  ${FP_FILE}"
echo
echo "Next:"
echo "  git add ${PUB_FILE} ${FP_FILE}"
echo "  git commit -m \"Publish public key ${FINGERPRINT}\""
echo "  git push"
echo
echo "Never publish a private key, secret key, seed phrase, recovery phrase, password, or 2FA code."
