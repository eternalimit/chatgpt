#!/usr/bin/env node

/**
 * WF-379999 proof verifier
 *
 * Verifies public GitHub evidence for the workflow without claiming
 * anything beyond what GitHub's public API reports.
 */

const REPO = "eternalimit/chatgpt";

const expected = {
  dgeo: {
    sha: "3041c385818f7974e01970f653e79fa7c51f5521",
    message: "Block 061: define DGEO as Distributed Geospatial Evidence Object",
    file: "project-logs/PROJECT_LOGS_BLOCK_061-DGEO-definition.md"
  },
  workflow: {
    sha: "170d7dd01b4ec7def0e79c9dc6c52b6397f1d3a5",
    message: "ChatGPT.eternalimit.GitHub.commit.",
    file: "records/379999-2026-09-27.txt"
  }
};

async function getCommit(sha) {
  const url = `https://api.github.com/repos/${REPO}/commits/${sha}`;
  const res = await fetch(url, {
    headers: {
      "Accept": "application/vnd.github+json",
      "User-Agent": "wf-379999-proof-verifier"
    }
  });

  if (!res.ok) {
    throw new Error(`GitHub API ${res.status} for ${sha}`);
  }
  return res.json();
}

function hasFile(commit, path) {
  return Array.isArray(commit.files) &&
    commit.files.some((f) => f.filename === path);
}

function checkCommit(commit, spec) {
  return {
    sha_match: commit.sha === spec.sha,
    message_match: commit.commit?.message === spec.message,
    file_match: hasFile(commit, spec.file),
    github_signature_verified: commit.commit?.verification?.verified === true,
    github_signature_reason: commit.commit?.verification?.reason ?? null
  };
}

function allTrue(obj, keys) {
  return keys.every((k) => obj[k] === true);
}

async function main() {
  const [dgeoCommit, workflowCommit] = await Promise.all([
    getCommit(expected.dgeo.sha),
    getCommit(expected.workflow.sha)
  ]);

  const dgeo = checkCommit(dgeoCommit, expected.dgeo);
  const workflow = checkCommit(workflowCommit, expected.workflow);

  const result = {
    repo: REPO,
    test_id: "379999",
    dgeo,
    workflow,
    gates: {
      dgeo_public_evidence:
        allTrue(dgeo, ["sha_match", "message_match", "file_match"]),
      workflow_public_evidence:
        allTrue(workflow, ["sha_match", "message_match", "file_match"]),
      workflow_signature_verified:
        workflow.github_signature_verified
    }
  };

  result.overall =
    result.gates.dgeo_public_evidence &&
    result.gates.workflow_public_evidence &&
    result.gates.workflow_signature_verified
      ? "PASS"
      : "PARTIAL";

  console.log(JSON.stringify(result, null, 2));

  // Exit 0 when public evidence is present, even if signature gate is still partial.
  // This keeps evidence verification separate from signature verification.
  if (!result.gates.dgeo_public_evidence ||
      !result.gates.workflow_public_evidence) {
    process.exitCode = 1;
  }
}

main().catch((err) => {
  console.error(JSON.stringify({
    overall: "ERROR",
    error: err.message
  }, null, 2));
  process.exitCode = 1;
});
