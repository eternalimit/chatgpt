#!/usr/bin/env python3
"""Buzz Verify: evidence-first Bitcoin address/transaction verifier.

Public-data verifier only. It does not hold keys, sign transactions, spend funds,
or prove legal ownership of an address.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import sys
import urllib.error
import urllib.request
from datetime import datetime, timezone

BASE = "https://mempool.space/api"
USER_AGENT = "eternalimit-buzz-verify/1.0"


def fetch_json(url: str) -> tuple[dict, bytes]:
    req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
    with urllib.request.urlopen(req, timeout=15) as resp:
        raw = resp.read()
    return json.loads(raw.decode("utf-8")), raw


def sha256_hex(raw: bytes) -> str:
    return hashlib.sha256(raw).hexdigest()


def verify_tx(txid: str) -> dict:
    txid = txid.strip().lower()
    if len(txid) != 64 or any(c not in "0123456789abcdef" for c in txid):
        return {"state": "UNVERIFIED", "reason": "Invalid transaction-id format", "input": txid}

    url = f"{BASE}/tx/{txid}/status"
    try:
        data, raw = fetch_json(url)
    except urllib.error.HTTPError as e:
        if e.code == 404:
            return {"state": "UNVERIFIED", "reason": "Transaction not found by public source", "input": txid}
        return {"state": "NEEDS_REVIEW", "reason": f"HTTP error {e.code}", "input": txid}
    except Exception as e:
        return {"state": "NEEDS_REVIEW", "reason": str(e), "input": txid}

    confirmed = bool(data.get("confirmed"))
    return {
        "state": "VERIFIED" if confirmed else "UNVERIFIED",
        "kind": "transaction",
        "input": txid,
        "confirmed": confirmed,
        "block_height": data.get("block_height"),
        "block_hash": data.get("block_hash"),
        "block_time": data.get("block_time"),
        "source": url,
        "evidence_sha256": sha256_hex(raw),
        "checked_at_utc": datetime.now(timezone.utc).isoformat(),
    }


def verify_address(address: str) -> dict:
    address = address.strip()
    url = f"{BASE}/address/{address}"
    try:
        data, raw = fetch_json(url)
    except urllib.error.HTTPError as e:
        if e.code in (400, 404):
            return {"state": "UNVERIFIED", "reason": "Address invalid or not found by public source", "input": address}
        return {"state": "NEEDS_REVIEW", "reason": f"HTTP error {e.code}", "input": address}
    except Exception as e:
        return {"state": "NEEDS_REVIEW", "reason": str(e), "input": address}

    chain = data.get("chain_stats", {})
    mempool = data.get("mempool_stats", {})
    funded = int(chain.get("funded_txo_sum", 0))
    spent = int(chain.get("spent_txo_sum", 0))
    mempool_funded = int(mempool.get("funded_txo_sum", 0))
    mempool_spent = int(mempool.get("spent_txo_sum", 0))
    confirmed_balance = funded - spent
    pending_delta = mempool_funded - mempool_spent

    return {
        "state": "VERIFIED",
        "kind": "address",
        "input": address,
        "confirmed_balance_sats": confirmed_balance,
        "mempool_delta_sats": pending_delta,
        "transaction_count": int(chain.get("tx_count", 0)),
        "source": url,
        "evidence_sha256": sha256_hex(raw),
        "checked_at_utc": datetime.now(timezone.utc).isoformat(),
        "ownership_proven": False,
        "ownership_note": "Public chain data can verify activity/balance, not who controls the private key.",
    }


def main() -> int:
    p = argparse.ArgumentParser(description="Buzz Verify for public Bitcoin evidence")
    sub = p.add_subparsers(dest="command", required=True)

    tx = sub.add_parser("tx", help="Verify a transaction id")
    tx.add_argument("txid")

    addr = sub.add_parser("address", help="Verify an address and public balance")
    addr.add_argument("address")

    args = p.parse_args()
    result = verify_tx(args.txid) if args.command == "tx" else verify_address(args.address)
    print(json.dumps(result, indent=2, sort_keys=True))
    return 0 if result.get("state") == "VERIFIED" else 2


if __name__ == "__main__":
    sys.exit(main())
