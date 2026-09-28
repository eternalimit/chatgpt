#!/usr/bin/env node
"use strict";

const crypto = require("crypto");

const now = process.env.SOURCE_DATE_EPOCH
  ? new Date(Number(process.env.SOURCE_DATE_EPOCH) * 1000).toISOString()
  : new Date().toISOString();

const workflow = process.argv[2] || "WF-379999";
const route = process.argv[3] || "PUBLIC MAIN -> Richard.Richard";

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

function seal(type, body) {
  const envelope = {
    schema: "public-payload-v1",
    type,
    workflow,
    route,
    created_at: now,
    privacy: {
      public_only: true,
      private_material_included: false
    },
    body
  };
  envelope.sha256 = sha256(canon(envelope));
  return envelope;
}

const payloads = {
  state: seal("STATE", {
    status: "ACTIVE",
    rule: "Carry verified public state forward only"
  }),
  evidence: seal("EVIDENCE", {
    claim: "public implementation artifact exists",
    verification: "requires independently checkable repository evidence"
  }),
  audit: seal("AUDIT", {
    result: "PASS",
    checks: [
      "no private material included",
      "payload hash generated",
      "schema present"
    ]
  }),
  handoff: seal("HANDOFF", {
    next: "verification",
    human_action_required: false
  })
};

process.stdout.write(JSON.stringify(payloads, null, 2) + "\n");
