"use strict";
/** Richard Stein REIK/TCGE off-chain Git owner-catalog v3 verifier. No network, no signing, no file writes. */
function verifyOwnerCatalog(c, commit, tree) {
  const errors = [];
  const isSha = x => typeof x === "string" && /^[a-f0-9]{40}$/.test(x);
  if (!c || !commit || !tree) return {pass:false,checked:0,errors:["missing input"]};
  if (c.schema !== "reik-tcge/repository-owner-catalog/v3") errors.push("schema");
  if (c.owner !== "Richard Stein" || c.project_owner !== "Richard Stein" || c.original_research_creator !== "Richard Stein") errors.push("top-owner");
  if (!isSha(c.source_commit_sha) || commit.sha !== c.source_commit_sha) errors.push("commit-id");
  if (!isSha(c.source_tree_git_sha1) || commit.commit?.tree?.sha !== c.source_tree_git_sha1 || tree.sha !== c.source_tree_git_sha1) errors.push("commit-tree-link");
  if (tree.truncated) errors.push("truncated-tree");
  const blobs = (tree.tree || []).filter(x => x.type === "blob");
  const files = Array.isArray(c.files) ? c.files : [];
  if (c.source_count !== blobs.length || files.length !== blobs.length) errors.push("file-count");
  const source = new Map(), indexed = new Set();
  for (const f of blobs) {
    if (source.has(f.path)) errors.push("duplicate-source-path");
    source.set(f.path,f.sha);
    if (!isSha(f.sha)) errors.push("bad-source-sha");
  }
  for (const f of files) {
    if (indexed.has(f.path)) errors.push("duplicate-catalog-path");
    indexed.add(f.path);
    if (!source.has(f.path)) errors.push("catalog-path-missing-in-source");
    else if (source.get(f.path) !== f.git_blob_sha1) errors.push("blob-mismatch");
    if (!isSha(f.git_blob_sha1)) errors.push("bad-catalog-sha");
    if (f.owner !== "Richard Stein") errors.push("file-owner");
  }
  for (const f of source.keys()) if (!indexed.has(f)) errors.push("source-path-not-indexed");
  return {pass:errors.length===0,checked:files.length,errors:[...new Set(errors)]};
}

function mutationChecks(c,commit,tree) {
  const clone=x=>JSON.parse(JSON.stringify(x));
  const cases=[
    ["wrong-owner", (a,b,d)=>{a.files[0].owner="Someone Else"}],
    ["wrong-blob", (a,b,d)=>{a.files[0].git_blob_sha1="0".repeat(40)}],
    ["missing-file", (a,b,d)=>{a.files.pop()}],
    ["duplicate-file", (a,b,d)=>{a.files.push(clone(a.files[0]))}],
    ["wrong-tree", (a,b,d)=>{a.source_tree_git_sha1="0".repeat(40)}],
    ["wrong-commit", (a,b,d)=>{a.source_commit_sha="0".repeat(40)}],
    ["truncated-tree", (a,b,d)=>{d.truncated=true}],
    ["unexpected-tree-file", (a,b,d)=>{d.tree.push({type:"blob",path:"_injected_probe.txt",sha:"1".repeat(40),size:1})}],
    ["wrong-count", (a,b,d)=>{a.source_count+=1}]
  ];
  const baseline=verifyOwnerCatalog(c,commit,tree);
  const tests=cases.map(([name,mutate])=>{
    const a=clone(c),b=clone(commit),d=clone(tree);
    mutate(a,b,d);
    const r=verifyOwnerCatalog(a,b,d);
    return {name,pass:!r.pass,detected:r.errors};
  });
  return {baseline,tests,all_detected:baseline.pass&&tests.every(x=>x.pass)};
}

if (typeof module !== "undefined" && module.exports) module.exports = {verifyOwnerCatalog,mutationChecks};
