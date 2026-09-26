#!/usr/bin/env node

/**
 * Coinbase Connector Adapter
 *
 * Repository-side adapter boundary only.
 * This does NOT connect ChatGPT to Coinbase and does NOT hold credentials.
 *
 * Accepted input example:
 * {"action":"balance","asset":"BTC","public_address":null,"account_connected":false}
 */

function hold(reason, extra = {}) {
  return { status: "HOLD", reason, ...extra };
}

function run(req) {
  if (!req || !req.action) {
    return hold("MISSING_ACTION");
  }

  if (
    req.private_key ||
    req.seed_phrase ||
    req.recovery_phrase ||
    req.password ||
    req.pin ||
    req.api_secret ||
    req.access_token
  ) {
    return hold("SECRET_INPUT_REJECTED");
  }

  if (!req.account_connected) {
    return hold("COINBASE_ACCOUNT_NOT_CONNECTED", {
      next: "CONNECT_SUPPORTED_COINBASE_ACCOUNT_CONNECTOR"
    });
  }

  if (req.action === "balance") {
    return {
      status: "VERIFY",
      source: "COINBASE_ACCOUNT_CONNECTOR",
      asset: req.asset || "BTC",
      next: "READ_AUTHENTICATED_ACCOUNT_BALANCE_AND_CROSS_CHECK_PUBLIC_CHAIN_WHEN_APPLICABLE"
    };
  }

  if (req.action === "transactions") {
    return {
      status: "VERIFY",
      source: "COINBASE_ACCOUNT_CONNECTOR",
      next: "READ_AUTHENTICATED_ACCOUNT_TRANSACTIONS_AND_CROSS_CHECK_PUBLIC_TXIDS_WHEN_APPLICABLE"
    };
  }

  return hold("UNSUPPORTED_ACTION");
}

let req = {};
try {
  req = JSON.parse(process.argv[2] || "{}");
} catch {
  console.error(JSON.stringify(hold("INVALID_JSON")));
  process.exit(2);
}

console.log(JSON.stringify(run(req), null, 2));
