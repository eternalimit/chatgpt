#!/usr/bin/env bash
set -euo pipefail

CMD="${1:-}"
NAME="${2:-}"
PRIVATE_DIR="${PRIVATE_DIR:-.private}"

mkdir -p "${PRIVATE_DIR}"
chmod 700 "${PRIVATE_DIR}"

usage() {
  echo "Usage:"
  echo "  $0 put <name>    # read plaintext from stdin, encrypt locally with GPG"
  echo "  $0 get <name>    # decrypt locally to stdout"
  echo "  $0 list          # list encrypted object names only"
  exit 2
}

safe_name() {
  [[ "$1" =~ ^[A-Za-z0-9._-]+$ ]] || {
    echo "ERROR: invalid name" >&2
    exit 2
  }
}

case "$CMD" in
  put)
    [[ -n "$NAME" ]] || usage
    safe_name "$NAME"
    OUT="$PRIVATE_DIR/$NAME.gpg"
    umask 077
    # GPG prompts locally for the passphrase; no secret is accepted as an argument.
    gpg --batch=false --symmetric --cipher-algo AES256 --output "$OUT"
    chmod 600 "$OUT"
    echo "STORED:$NAME"
    ;;
  get)
    [[ -n "$NAME" ]] || usage
    safe_name "$NAME"
    IN="$PRIVATE_DIR/$NAME.gpg"
    [[ -f "$IN" ]] || { echo "ERROR: not found" >&2; exit 1; }
    gpg --decrypt "$IN"
    ;;
  list)
    find "$PRIVATE_DIR" -maxdepth 1 -type f -name '*.gpg' -printf '%f\n' 2>/dev/null | sed 's/\.gpg$//' | sort
    ;;
  *)
    usage
    ;;
esac
