#!/usr/bin/env node

/**
 * Executive Buzz Exchange Clone
 *
 * Safe coordinator only. This program DOES NOT hold private keys,
 * sign Bitcoin transactions, or broadcast transactions.
 *
 * Input JSON on argv[2], e.g.:
 * {"action":"exchange","asset_from":"BTC","asset_to":"ELC","amount":1,"public_txid":null}
 */

function hold(reason, extra = {}) {
  return {
    status: "HOLD",
    reason,
    btc_moved: 0,
    elc_moved: 0,
    ...extra
  };
}

function run(req) {
  if (!req || req.action !== "exchange") {
    return hold("INVALID_OR_MISSING_EXCHANGE_REQUEST");
  }

  if (req.private_key || req.seed_phrase || req.recovery_words || req.password || req.pin) {
    return hold("SECRET_INPUT_REJECTED");
  }

  if (!req.authorized_executor) {
    return hold("AUTHORIZED_EXECUTOR_NOT_CONNECTED", {
      next: "CONNECT_AUTHORIZED_WALLET_OR_EXCHANGE"
    });
  }

  if (!req.public_txid) {
    return hold("REAL_TXID_NOT_PRESENT", {
      next: "AUTHORIZED_EXECUTOR_SIGN_AND_BROADCAST"
    });
  }

  return {
    status: "VERIFY",
    public_txid: req.public_txid,
    next: "VERIFY_PUBLIC_BLOCKCHAIN",
    note: "Presence of a TXID is not proof of settlement until independently verified."
  };
}

let req = {};
try {
  req = JSON.parse(process.argv[2] || "{}");
} catch {
  console.error(JSON.stringify(hold("INVALID_JSON")));
  process.exit(2);
}

console.log(JSON.stringify(run(req), null, 2));
