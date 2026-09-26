#!/usr/bin/env node

/**
 * BitcoinSigner Adapter
 *
 * Non-custodial signing boundary for Executive Buzz.
 *
 * IMPORTANT:
 * - This adapter does NOT accept, store, derive, or expose private keys,
 *   seed phrases, recovery words, PINs, or wallet passwords.
 * - It does NOT implement Bitcoin private-key signing.
 * - A real signature must be produced by an external authorized wallet,
 *   hardware signer, or exchange.
 * - This adapter accepts the externally signed transaction only for handoff
 *   into the broadcast/verification workflow.
 */

function hold(reason, extra = {}) {
  return {
    status: "HOLD",
    reason,
    signed: false,
    broadcast: false,
    txid: null,
    ...extra
  };
}

function run(req) {
  if (!req || req.action !== "bitcoin_sign") {
    return hold("INVALID_OR_MISSING_SIGN_REQUEST");
  }

  if (
    req.private_key ||
    req.seed_phrase ||
    req.recovery_words ||
    req.wallet_password ||
    req.password ||
    req.pin
  ) {
    return hold("SECRET_INPUT_REJECTED");
  }

  if (!req.authorization) {
    return hold("USER_AUTHORIZATION_REQUIRED");
  }

  if (!req.psbt && !req.unsigned_tx) {
    return hold("UNSIGNED_TRANSACTION_REQUIRED");
  }

  if (!req.external_signer_id) {
    return hold("AUTHORIZED_EXTERNAL_SIGNER_REQUIRED", {
      next: "CONNECT_HARDWARE_WALLET_OR_AUTHORIZED_EXCHANGE"
    });
  }

  if (!req.signed_tx_hex) {
    return {
      status: "SIGN_EXTERNAL",
      signed: false,
      broadcast: false,
      txid: null,
      external_signer_id: req.external_signer_id,
      next: "EXTERNAL_SIGNER_RETURNS_SIGNED_TX_HEX",
      note: "This adapter never receives or stores signing secrets."
    };
  }

  return {
    status: "SIGNED_TX_RECEIVED",
    signed: true,
    broadcast: false,
    txid: null,
    external_signer_id: req.external_signer_id,
    signed_tx_hex: req.signed_tx_hex,
    next: "BROADCAST_WITH_AUTHORIZED_BITCOIN_EXECUTOR",
    note: "A signed transaction is not proof of broadcast or settlement."
  };
}

let req = {};
try {
  req = JSON.parse(process.argv[2] || "{}");
} catch {
  console.error(JSON.stringify(hold("INVALID_JSON"), null, 2));
  process.exit(2);
}

console.log(JSON.stringify(run(req), null, 2));
