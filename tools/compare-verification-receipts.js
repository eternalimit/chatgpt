#!/usr/bin/env node
"use strict";

const fs = require("fs");
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

function normalize(receipt) {
  return {
    schema: receipt.schema,
    status: receipt.status,
    checks: (receipt.checks || [])
      .map(c => ({
        name: c.name,
        claimed_sha256: c.claimed_sha256,
        computed_sha256: c.computed_sha256,
        hash_match: c.hash_match,
        schema_present: c.schema_present,
        workflow_present: c.workflow_present,
        route_present: c.route_present,
        public_only: c.public_only,
        private_material_included: c.private_material_included
      }))
      .sort((a, b) => String(a.name).localeCompare(String(b.name)))
  };
}

const [aPath, bPath] = process.argv.slice(2);
if (!aPath || !bPath) {
  console.error("Usage: node tools/compare-verification-receipts.js <receipt-a.json> <receipt-b.json>");
  process.exit(2);
}

let a, b;
try {
  a = JSON.parse(fs.readFileSync(aPath, "utf8"));
  b = JSON.parse(fs.readFileSync(bPath, "utf8"));
} catch (err) {
  console.error(JSON.stringify({status:"FAIL", reason:"read_or_parse_error", detail:String(err.message)}, null, 2));
  process.exit(1);
}

const na = normalize(a);
const nb = normalize(b);
const ca = canon(na);
const cb = canon(nb);
const match = ca === cb;

const result = {
  schema: "independent-receipt-comparison-v1",
  status: match ? "PASS" : "FAIL",
  receipt_a_normalized_sha256: sha256(ca),
  receipt_b_normalized_sha256: sha256(cb),
  normalized_match: match,
  compared_fields: [
    "schema",
    "status",
    "checks[].name",
    "checks[].claimed_sha256",
    "checks[].computed_sha256",
    "checks[].hash_match",
    "checks[].schema_present",
    "checks[].workflow_present",
    "checks[].route_present",
    "checks[].public_only",
    "checks[].private_material_included"
  ],
  ignored_nondeterministic_fields: [
    "verified_at",
    "receipt sha256"
  ]
};

result.sha256 = sha256(canon(result));
process.stdout.write(JSON.stringify(result, null, 2) + "\n");
process.exit(match ? 0 : 1);
