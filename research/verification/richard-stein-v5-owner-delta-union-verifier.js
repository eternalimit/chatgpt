"use strict";
/** Richard Stein original REIK/TCGE research metadata; read-only v5 catalog+delta verification. No network, wallet, or external changes. */
function verifyOwnerUnionV5(catalog, delta, commit, tree, scope) {
  const errors=[], flag=x=>{if(!errors.includes(x))errors.push(x)};
  const sha=x=>typeof x==="string"&&/^[0-9a-f]{40}$/.test(x);
  if(!catalog||!delta||!commit||!tree||!scope)return {pass:false,errors:["missing-input"],files:0,gitlinks:0};
  if(catalog.schema!=="reik-tcge/repository-owner-catalog/v3")flag("catalog-schema");
  if(delta.schema!=="reik-tcge/pinned-source-owner-delta-v5")flag("delta-schema");
  for(const k of ["owner","original_research_creator","original_research_author","project_owner","data_steward"])if(catalog[k]!=="Richard Stein")flag("catalog-attribution");
  for(const k of ["named_original_research_creator","named_research_author","original_project_owner","project_data_steward"])if(delta[k]!=="Richard Stein")flag("delta-attribution");
  if(catalog.repository!==scope.repo||catalog.branch!==scope.branch)flag("catalog-scope");
  if(!Array.isArray(delta.branches)||delta.branches.length!==3||new Set(delta.branches.map(x=>x.repo+"#"+x.branch)).size!==3)flag("branch-uniqueness");
  const group=(delta.branches||[]).filter(x=>x.repo===scope.repo&&x.branch===scope.branch);
  if(group.length!==1)return {pass:false,errors:[...errors,"branch-missing-or-duplicated"],files:0,gitlinks:0};
  const g=group[0];
  if(g.v3!==scope.v3Commit||g.v3!==scope.catalogRef||g.repo!==catalog.repository||g.branch!==catalog.branch)flag("parent-binding");
  if(!sha(g.snapshot_commit)||g.snapshot_commit!==commit.sha)flag("commit-binding");
  if(!sha(g.snapshot_tree)||g.snapshot_tree!==commit.commit?.tree?.sha||g.snapshot_tree!==tree.sha)flag("tree-binding");
  if(tree.truncated!==false||!Array.isArray(tree.tree))flag("tree-completeness");
  if(delta.technical_controls?.original_kernel_sha256_historical_reference!=="03a38cf8aa32b49e6dcdd8c22e900d4172827af7c59402490dce5439bdfb9402")flag("kernel-reference");
  if(delta.technical_controls?.experiment030_031_distinct!==true||delta.technical_controls?.third_party_license_rights_preserved!==true||delta.technical_controls?.hold_scoped_to_technical_claims!==true)flag("governance");
  if(catalog.fidELITY?.join("|")!=="Identity|Provenance|Chronology|Independence|Method/Object Separation|Non-Expansion|Falsification Persistence|Uncertainty")flag("fidelity");
  const source=new Map(),links=[],seen=new Set();
  for(const e of (Array.isArray(tree.tree)?tree.tree:[])){
    if(seen.has(e.path)||typeof e.path!=="string")flag("duplicate-tree-path");
    seen.add(e.path);
    if(!sha(e.sha))flag("source-sha-format");
    if(e.type==="blob"){
      if(!["100644","100755","120000"].includes(e.mode)||!Number.isSafeInteger(e.size)||e.size<0)flag("source-blob-typing");
      source.set(e.path,e);
    }else if(e.type==="commit"){
      if(e.mode!=="160000")flag("gitlink-mode");
      links.push(e);
    }else if(e.type!=="tree")flag("source-entry-type");
  }
  const old=Array.isArray(catalog.files)?catalog.files:[],added=Array.isArray(g.added)?g.added:[];
  if(old.length!==catalog.source_count||old.length!==g.previous_v3_count||old.length!==g.unchanged_count)flag("previous-count");
  if(source.size!==g.source_blob_count||old.length+added.length!==source.size)flag("union-count");
  if(!Array.isArray(g.modified)||g.modified.length||!Array.isArray(g.deleted)||g.deleted.length)flag("unexpected-mutation-declaration");
  const union=new Map();
  for(const e of old){
    if(union.has(e.path))flag("duplicate-entry");
    union.set(e.path,e);
    const actual=source.get(e.path);
    if(!actual)flag("old-file-missing");
    else if(actual.sha!==e.git_blob_sha1||actual.size!==e.bytes)flag("old-file-changed");
    if(e.owner!=="Richard Stein")flag("old-owner");
  }
  for(const e of added){
    if(union.has(e.path))flag("overlapping-delta-entry");
    union.set(e.path,e);
    const actual=source.get(e.path);
    if(!actual)flag("new-file-missing");
    else if(actual.sha!==e.git_blob_sha1||actual.size!==e.bytes)flag("new-file-mismatch");
    if(e.project_owner!=="Richard Stein")flag("new-owner");
  }
  if(union.size!==source.size||[...source.keys()].some(x=>!union.has(x)))flag("not-exhaustive");
  const declared=Array.isArray(g.gitlinks)?g.gitlinks:[];
  if(declared.length!==links.length||new Set(declared.map(x=>x.path)).size!==declared.length)flag("gitlink-count");
  for(const link of links){
    const d=declared.find(x=>x.path===link.path);
    if(!d||d.external_commit_sha1!==link.sha||d.mode!=="160000"||d.contents_included!==false||d.external_original_authorship_claim!==false)flag("gitlink-scope-or-sha");
  }
  if(delta.branches?.reduce((n,x)=>n+x.source_blob_count,0)!==delta.snapshot_blobs_total||delta.branches?.reduce((n,x)=>n+x.added?.length,0)!==delta.incremental_entries||delta.branches?.reduce((n,x)=>n+x.previous_v3_count,0)!==delta.prior_v3_blobs_total)flag("cross-branch-total");
  return {pass:errors.length===0,errors,files:source.size,baseline:old.length,added:added.length,gitlinks:links.length};
}

function probeUnionV5(c,d,commit,tree,scope){
 const cp=x=>JSON.parse(JSON.stringify(x));
 const branch=x=>x.branches.find(z=>z.repo===scope.repo&&z.branch===scope.branch);
 const cases=[
 ["change-added-owner",(a,b)=>{branch(b).added[0].project_owner="Somebody Else"},"new-owner"],
 ["change-added-size",(a,b)=>{branch(b).added[0].bytes++},"new-file-mismatch"],
 ["change-added-sha",(a,b)=>{branch(b).added[0].git_blob_sha1="0".repeat(40)},"new-file-mismatch"],
 ["remove-added-entry",(a,b)=>{branch(b).added.pop()},"union-count"],
 ["duplicate-added-entry",(a,b)=>{branch(b).added.push(cp(branch(b).added[0]))},"union-count"],
 ["old-added-overlap",(a,b)=>{branch(b).added[0].path=a.files[0].path},"overlapping-delta-entry"],
 ["change-old-blob",(a,b)=>{a.files[0].git_blob_sha1="0".repeat(40)},"old-file-changed"],
 ["change-old-size",(a,b)=>{a.files[0].bytes++},"old-file-changed"],
 ["change-old-owner",(a,b)=>{a.files[0].owner="Other"},"old-owner"],
 ["change-project-author",(a,b)=>{b.named_research_author="Other"},"delta-attribution"],
 ["wrong-scope",(a,b)=>{a.repository="Other/repo"},"catalog-scope"],
 ["wrong-parent",(a,b)=>{branch(b).v3="0".repeat(40)},"parent-binding"],
 ["wrong-commit",(a,b)=>{branch(b).snapshot_commit="0".repeat(40)},"commit-binding"],
 ["wrong-tree",(a,b)=>{branch(b).snapshot_tree="0".repeat(40)},"tree-binding"],
 ["wrong-unchanged",(a,b)=>{branch(b).unchanged_count--},"previous-count"],
 ["conceal-modification",(a,b)=>{branch(b).modified.push("README.md")},"unexpected-mutation-declaration"],
 ["conceal-deletion",(a,b)=>{branch(b).deleted.push("README.md")},"unexpected-mutation-declaration"],
 ["wrong-total",(a,b)=>{b.snapshot_blobs_total++},"cross-branch-total"],
 ["duplicate-branch",(a,b)=>{b.branches[1]=cp(b.branches[0])},"branch-uniqueness"],
 ["wrong-kernel-ref",(a,b)=>{b.technical_controls.original_kernel_sha256_historical_reference="0".repeat(64)},"kernel-reference"],
 ["missing-fidelity",(a,b)=>{a.fidELITY.pop()},"fidelity"],
 ["unindexed-tree-object",(a,b,c,t)=>{t.tree.push({path:"_probe_added.txt",type:"blob",mode:"100644",sha:"a".repeat(40),size:12})},"union-count"],
 ["truncated-tree",(a,b,c,t)=>{t.truncated=true},"tree-completeness"]
 ];
 const baseline=verifyOwnerUnionV5(c,d,commit,tree,scope);
 const tests=cases.map(([id,mutate,expected])=>{
   const cc=cp(c),dd=cp(d),co=cp(commit),tt=cp(tree);
   mutate(cc,dd,co,tt);
   const r=verifyOwnerUnionV5(cc,dd,co,tt,scope);
   return {id,pass:!r.pass&&r.errors.includes(expected),errors:r.errors};
 });
 let gitlink={skipped:baseline.gitlinks===0};
 if(baseline.gitlinks>0){
   const dd=cp(d);branch(dd).gitlinks[0].external_original_authorship_claim=true;
   const r=verifyOwnerUnionV5(c,dd,commit,tree,scope);
   gitlink={skipped:false,pass:!r.pass&&r.errors.includes("gitlink-scope-or-sha"),errors:r.errors};
 }
 return {baseline,tests,gitlink,all_pass:baseline.pass&&tests.every(x=>x.pass)&&(gitlink.skipped||gitlink.pass)};
}

if(typeof module!=="undefined"&&module.exports)module.exports={verifyOwnerUnionV5,probeUnionV5};
