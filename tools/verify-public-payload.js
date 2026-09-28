#!/usr/bin/env node
"use strict";

const crypto = require("crypto");

function sha256(value) {
  return crypto.createHash("sha256").update(value).digest("hex");
}

function canon(obj) {
  if (Array.isArray(obj)) return "[" + obj.map(canon).join(",") + "]";
  if (obj && typeof obj === "object") {
    return "{" + Object.keys(obj).sort().map(k => JSON.stringify(k) + ":" + canon(obj[k])).join(",") + "}";
  }
  return JSON.stringify(obj);
}

function verifyEnvelope(name, envelope) {
  const clone = JSON.parse(JSON.stringify(envelope));
  const claimed = clone.sha256;
  delete clone.sha256;
  const computed = sha256(canon(clone));
  return {
    name,
    claimed_sha256: claimed || null,
    computed_sha256: computed,
    hash_match: claimed === computed,
    schema_present: typeof envelope.schema === "string",
    workflow_present: typeof envelope.workflow === "string",
    route_present: typeof envelope.route === "string",
    public_only: envelope?.privacy?.public_only === true,
    private_material_included: envelope?.privacy?.private_material_included === true
  };
}

let input = "";
process.stdin.setEncoding("utf8");
process.stdin.on("data", c => input += c);
process.stdin.on("end", () => {
  let parsed;
  try {
    parsed = JSON.parse(input);
  } catch {
    console.error(JSON.stringify({status:"FAIL", reason:"invalid_json"}, null, 2));
    process.exit(1);
  }

  const receipts = Object.entries(parsed).map(([name, env]) => verifyEnvelope(name, env));
  const pass = receipts.every(r =>
    r.hash_match &&
    r.schema_present &&
    r.workflow_present &&
    r.route_present &&
    r.public_only &&
    !r.private_material_included
  );

  const receipt = {
    schema: "verification-receipt-v1",
    status: pass ? "PASS" : "FAIL",
    verified_at: new Date().toISOString(),
    checks: receipts
  };

  receipt.sha256 = sha256(canon(receipt));
  process.stdout.write(JSON.stringify(receipt, null, 2) + "\n");
  process.exit(pass ? 0 : 1);
});
