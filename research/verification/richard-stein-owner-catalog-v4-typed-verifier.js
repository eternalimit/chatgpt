"use strict";
/** Original first-party research: Richard Stein. Off-chain, read-only v4 scope, SHA-1, size, governance and gitlink-check verifier. */
function verifyOwnerV4(c, commit, tree, expected) {
  const failures = [];
  const sha = v => typeof v === "string" && /^[0-9a-f]{40}$/.test(v);
  const fail = k => failures.push(k);
  if (!c || !commit || !tree || !expected) return {pass:false,errors:["missing-input"],checked:0,gitlinks:[]};
  if (c.schema !== "reik-tcge/repository-owner-catalog/v3") fail("schema");
  for (const field of ["owner","original_research_creator","original_research_author","project_owner","data_steward"]) {
    if (c[field] !== "Richard Stein") fail("attribution:"+field);
  }
  if (c.repository !== expected.repository || c.branch !== expected.branch) fail("source-scope");
  if (!sha(c.source_commit_sha) || commit.sha !== c.source_commit_sha) fail("commit");
  if (!sha(c.source_tree_git_sha1) || commit.commit?.tree?.sha !== c.source_tree_git_sha1 || tree.sha !== c.source_tree_git_sha1) fail("tree");
  if (tree.truncated !== false || !Array.isArray(tree.tree)) fail("tree-incomplete");
  if (c.original_kernel_sha256_historical_reference !== "03a38cf8aa32b49e6dcdd8c22e900d4172827af7c59402490dce5439bdfb9402") fail("kernel-reference");
  if (c.experiment_030_031_lineages_separate !== true || c.technical_hold_not_authorship_hold !== true) fail("governance");
  const want = ["Identity","Provenance","Chronology","Independence","Method/Object Separation","Non-Expansion","Falsification Persistence","Uncertainty"];
  if (!Array.isArray(c.fidELITY) || JSON.stringify(c.fidELITY) !== JSON.stringify(want)) fail("fidelity");
  const blobs = new Map(), allPaths = new Set(), links = [];
  for (const entry of (Array.isArray(tree.tree) ? tree.tree : [])) {
    if (typeof entry.path !== "string" || allPaths.has(entry.path)) fail("tree-path");
    allPaths.add(entry.path);
    if (!sha(entry.sha)) fail("tree-object-sha");
    if (entry.type === "blob") {
      if (!["100644","100755","120000"].includes(entry.mode)) fail("blob-mode");
      if (!Number.isSafeInteger(entry.size) || entry.size < 0) fail("source-byte-size");
      blobs.set(entry.path, entry);
    } else if (entry.type === "commit") {
      if (entry.mode !== "160000") fail("gitlink-mode");
      links.push({path:entry.path,commit_sha1:entry.sha,scope:"gitlink-pointer-only; contents external"});
    } else if (entry.type !== "tree") fail("unexpected-entry-type");
  }
  const items = Array.isArray(c.files) ? c.files : [];
  if (c.source_count !== blobs.size || items.length !== blobs.size) fail("count");
  const indexed = new Set();
  for (const item of items) {
    if (!item || typeof item.path !== "string" || indexed.has(item.path)) { fail("duplicate-or-invalid-index-path");continue; }
    indexed.add(item.path);
    const original = blobs.get(item.path);
    if (!original) { fail("missing-index-target"); continue; }
    if (item.git_blob_sha1 !== original.sha) fail("blob-sha");
    if (item.bytes !== original.size) fail("byte-size");
    if (item.owner !== "Richard Stein") fail("file-owner");
  }
  for (const k of blobs.keys()) if (!indexed.has(k)) fail("unindexed-source-blob");
  return {pass:failures.length===0,checked:items.length,errors:[...new Set(failures)],gitlinks:links};
}

function probeV4(c,commit,tree,expected){
 const copy = x => JSON.parse(JSON.stringify(x));
 const vectors = [
 ["wrong-byte-size",(a,b,d,e)=>{a.files[0].bytes+=1},"byte-size"],
 ["wrong-research-author",(a,b,d,e)=>{a.original_research_author="Unknown"},"attribution:original_research_author"],
 ["wrong-data-steward",(a,b,d,e)=>{a.data_steward="Unknown"},"attribution:data_steward"],
 ["wrong-repository",(a,b,d,e)=>{a.repository="other/repo"},"source-scope"],
 ["wrong-branch",(a,b,d,e)=>{a.branch="other"},"source-scope"],
 ["wrong-blob-mode",(a,b,d,e)=>{d.tree.find(x=>x.type==="blob").mode="160000"},"blob-mode"],
 ["wrong-governance",(a,b,d,e)=>{a.technical_hold_not_authorship_hold=false},"governance"],
 ["wrong-kernel-reference",(a,b,d,e)=>{a.original_kernel_sha256_historical_reference="0".repeat(64)},"kernel-reference"],
 ["wrong-fidelity",(a,b,d,e)=>{a.fidELITY.pop()},"fidelity"],
 ["wrong-source-byte-size",(a,b,d,e)=>{d.tree.find(x=>x.type==="blob").size+=1},"byte-size"],
 ["unlisted-source",(a,b,d,e)=>{d.tree.push({path:"__probe__.txt",mode:"100644",type:"blob",sha:"1".repeat(40),size:1})},"count"],
 ["wrong-tree",(a,b,d,e)=>{a.source_tree_git_sha1="0".repeat(40)},"tree"],
 ["wrong-owner",(a,b,d,e)=>{a.files[0].owner="Not Richard Stein"},"file-owner"],
 ["duplicate-path",(a,b,d,e)=>{a.files.push(copy(a.files[0]))},"duplicate-or-invalid-index-path"],
 ["missing-file",(a,b,d,e)=>{a.files.pop()},"count"]
 ];
 const original=verifyOwnerV4(c,commit,tree,expected);
 const tests=vectors.map(([name,fn,detector])=>{
  const a=copy(c),b=copy(commit),d=copy(tree),e=copy(expected);
  fn(a,b,d,e);const r=verifyOwnerV4(a,b,d,e);
  return {name,detected:!r.pass&&r.errors.includes(detector),errors:r.errors};
 });
 const gitlinks=original.gitlinks;
 let linkTest={skipped:gitlinks.length===0};
 if(gitlinks.length){
  const d=copy(tree);d.tree.find(x=>x.type==="commit").mode="100644";
  const r=verifyOwnerV4(c,commit,d,expected);
  linkTest={skipped:false,detected:!r.pass&&r.errors.includes("gitlink-mode"),errors:r.errors};
 }
 return {baseline:original,tests,gitlink_test:linkTest,all_pass:original.pass&&tests.every(t=>t.detected)&&(linkTest.skipped||linkTest.detected)};
}

if (typeof module !== "undefined" && module.exports) module.exports = { verifyOwnerV4, probeV4 };
