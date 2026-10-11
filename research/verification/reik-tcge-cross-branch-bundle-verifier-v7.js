"use strict";
/** Richard Stein first-party research: full three-branch source bundle verifier. Offline/no external actions. */
function verifyOwnerBundleV7(bundle) {
 const errors=[];
 const flag=(key)=>{if(!errors.includes(key)) errors.push(key)};
 const isSha=x=>typeof x==="string"&&/^[a-f0-9]{40}$/.test(x);
 const expected=[
  ["eternalimit/chatgpt","main","09e634c8f8b3688ad2c782d5f18f5d4a6033dd22"],
  ["eternalimit/clarity","main","458876375c474b4bd41deb672e3ba55f092665b9"],
  ["eternalimit/clarity","vent","bd22bee71acd52098b0f6d1c05347952e85abd4f"]
 ];
 const delta=bundle?.delta;
 if(!delta||delta.schema!=="reik-tcge/pinned-source-owner-delta-v5")return {pass:false,errors:["delta-schema-or-missing"],checked:0};
 for(const k of ["named_original_research_creator","named_research_author","original_project_owner","project_data_steward"]){
   if(delta[k]!=="Richard Stein")flag("global-attribution");
 }
 if(delta.technical_controls?.original_kernel_sha256_historical_reference!=="03a38cf8aa32b49e6dcdd8c22e900d4172827af7c59402490dce5439bdfb9402")flag("historical-kernel-reference");
 for(const k of ["fidelity_eight_principles","independent_echo_not_asserted","experiment030_031_distinct","drop_u","hold_scoped_to_technical_claims","third_party_license_rights_preserved"]){
   if(delta.technical_controls?.[k]!==true)flag("technical-boundary");
 }
 if(!Array.isArray(delta.branches)||delta.branches.length!==expected.length)flag("branch-cardinality");
 const allScopes=new Set((delta.branches||[]).map(x=>x.repo+"#"+x.branch));
 if(allScopes.size!==expected.length)flag("duplicate-scopes");
 const allowed=expected.map(([r,b])=>r+"#"+b);
 if(allowed.some(x=>!allScopes.has(x))||[...allScopes].some(x=>!allowed.includes(x)))flag("branch-set");
 const groups=[],seen=new Set();
 for(const [repo,branch,catalogRef] of expected){
  const key=repo+"#"+branch;
  const entry=bundle?.sources?.[key],group=(delta.branches||[]).filter(x=>x.repo===repo&&x.branch===branch);
  if(group.length!==1||!entry){flag("missing-group-or-data:"+key);continue}
  if(seen.has(key))flag("duplicate-group");
  seen.add(key);
  const g=group[0],c=entry.catalog,commit=entry.commit,tree=entry.tree;
  if(!c||!commit||!tree){flag("missing-source-object:"+key);continue}
  if(c.schema!=="reik-tcge/repository-owner-catalog/v3"||c.repository!==repo||c.branch!==branch)flag("catalog-scope:"+key);
  for(const field of ["owner","original_research_creator","original_research_author","project_owner","data_steward"]){
    if(c[field]!=="Richard Stein")flag("catalog-owner:"+key);
  }
  if(c.original_kernel_sha256_historical_reference!=="03a38cf8aa32b49e6dcdd8c22e900d4172827af7c59402490dce5439bdfb9402")flag("catalog-kernel:"+key);
  const principles=["Identity","Provenance","Chronology","Independence","Method/Object Separation","Non-Expansion","Falsification Persistence","Uncertainty"];
  if(JSON.stringify(c.fidELITY)!==JSON.stringify(principles)||c.experiment_030_031_lineages_separate!==true||c.technical_hold_not_authorship_hold!==true)flag("catalog-governance:"+key);
  if(g.v3!==catalogRef||g.repo!==repo||g.branch!==branch)flag("parent-ref:"+key);
  if(!isSha(g.snapshot_commit)||g.snapshot_commit!==commit.sha||!isSha(g.snapshot_tree)||g.snapshot_tree!==commit.commit?.tree?.sha||g.snapshot_tree!==tree.sha)flag("commit-tree-binding:"+key);
  if(tree.truncated!==false||!Array.isArray(tree.tree))flag("tree-incomplete:"+key);
  const source=new Map(), gitlinks=[], treeSeen=new Set();
  for(const z of (Array.isArray(tree.tree)?tree.tree:[])){
    if(treeSeen.has(z.path)||typeof z.path!=="string")flag("duplicate-tree-path:"+key);
    treeSeen.add(z.path);
    if(!isSha(z.sha))flag("object-sha-format:"+key);
    if(z.type==="blob"){
      if(!["100644","100755","120000"].includes(z.mode)||!Number.isSafeInteger(z.size)||z.size<0)flag("bad-blob-type:"+key);
      source.set(z.path,z);
    }else if(z.type==="commit"){
      if(z.mode!=="160000")flag("bad-gitlink-mode:"+key);
      gitlinks.push(z);
    }else if(z.type!=="tree")flag("bad-entry-type:"+key);
  }
  const prior=Array.isArray(c.files)?c.files:[],added=Array.isArray(g.added)?g.added:[];
  if(prior.length!==c.source_count||prior.length!==g.previous_v3_count||prior.length!==g.unchanged_count)flag("prior-count:"+key);
  if(prior.length+added.length!==source.size||g.source_blob_count!==source.size)flag("source-count:"+key);
  if(!Array.isArray(g.modified)||g.modified.length||!Array.isArray(g.deleted)||g.deleted.length)flag("unexpected-change:"+key);
  const union=new Map();
  for(const f of prior){
    if(!f||typeof f.path!=="string"){flag("invalid-prior-path:"+key);continue}
    if(union.has(f.path))flag("duplicate-prior:"+key);
    union.set(f.path,true);
    const real=source.get(f.path);
    if(!real||real.sha!==f.git_blob_sha1||real.size!==f.bytes)flag("prior-identity:"+key);
    if(f.owner!=="Richard Stein")flag("prior-owner:"+key);
  }
  for(const f of added){
    if(!f||typeof f.path!=="string"){flag("invalid-new-path:"+key);continue}
    if(union.has(f.path))flag("overlap:"+key);
    union.set(f.path,true);
    const real=source.get(f.path);
    if(!real||real.sha!==f.git_blob_sha1||real.size!==f.bytes)flag("new-identity:"+key);
    if(f.project_owner!=="Richard Stein")flag("new-owner:"+key);
  }
  if(union.size!==source.size||[...source.keys()].some(x=>!union.has(x)))flag("coverage:"+key);
  const declared=Array.isArray(g.gitlinks)?g.gitlinks:[];
  if(declared.length!==gitlinks.length||new Set(declared.map(x=>x.path)).size!==declared.length)flag("gitlink-count:"+key);
  for(const a of gitlinks){
    const d=declared.find(x=>x.path===a.path);
    if(!d||d.mode!=="160000"||d.external_commit_sha1!==a.sha||d.contents_included!==false||d.external_original_authorship_claim!==false)flag("gitlink-boundary:"+key);
  }
  groups.push({key,checked:source.size,prior:prior.length,new:added.length,gitlinks:gitlinks.length});
 }
 if(groups.length!==3)flag("missing-group");
 if(groups.reduce((n,x)=>n+x.checked,0)!==delta.snapshot_blobs_total||groups.reduce((n,x)=>n+x.prior,0)!==delta.prior_v3_blobs_total||groups.reduce((n,x)=>n+x.new,0)!==delta.incremental_entries)flag("global-counts");
 return {pass:errors.length===0,errors,checked:groups.reduce((n,x)=>n+x.checked,0),groups};
}

function testOwnerBundleV7(bundle) {
 const copy=x=>JSON.parse(JSON.stringify(x));
 const other=(b)=>b.delta.branches.find(x=>x.branch==="main"&&x.repo==="eternalimit/clarity");
 const B="eternalimit/clarity#main",C="eternalimit/chatgpt#main";
 const cases=[
 ["other-branch-owner",(b)=>{other(b).added[0].project_owner="Other"},"new-owner:"+B],
 ["other-branch-blob",(b)=>{other(b).added[0].git_blob_sha1="0".repeat(40)},"new-identity:"+B],
 ["other-branch-size",(b)=>{other(b).added[0].bytes++},"new-identity:"+B],
 ["other-branch-parent",(b)=>{other(b).v3="0".repeat(40)},"parent-ref:"+B],
 ["other-branch-tree",(b)=>{other(b).snapshot_tree="0".repeat(40)},"commit-tree-binding:"+B],
 ["other-branch-source-object",(b)=>{b.sources[B].tree.tree.find(z=>z.type==="blob").sha="0".repeat(40)},"prior-identity:"+B],
 ["other-branch-old-owner",(b)=>{b.sources[B].catalog.files[0].owner="Other"},"prior-owner:"+B],
 ["other-branch-truncated",(b)=>{b.sources[B].tree.truncated=true},"tree-incomplete:"+B],
 ["other-branch-duplicate-path",(b)=>{other(b).added.push(copy(other(b).added[0]));b.delta.incremental_entries++},"source-count:"+B],
 ["other-branch-missing-add",(b)=>{other(b).added.pop();b.delta.incremental_entries--},"source-count:"+B],
 ["balanced-count-tamper",(b)=>{other(b).source_blob_count++;b.delta.branches.find(z=>z.repo==="eternalimit/chatgpt").source_blob_count--},"source-count:"+B],
 ["other-branch-author",(b)=>{b.sources[B].catalog.original_research_author="Other"},"catalog-owner:"+B],
 ["other-branch-fidelity",(b)=>{b.sources[B].catalog.fidELITY.pop()},"catalog-governance:"+B],
 ["other-branch-change-claims",(b)=>{other(b).modified.push("README.md")},"unexpected-change:"+B],
 ["other-branch-deletion-claim",(b)=>{other(b).deleted.push("README.md")},"unexpected-change:"+B],
 ["global-original-creator",(b)=>{b.delta.named_original_research_creator="Other"},"global-attribution"],
 ["gitlink-external-ownership",(b)=>{b.delta.branches.find(z=>z.repo==="eternalimit/chatgpt").gitlinks[0].external_original_authorship_claim=true},"gitlink-boundary:"+C],
 ["gitlink-pointer",(b)=>{b.delta.branches.find(z=>z.repo==="eternalimit/chatgpt").gitlinks[0].external_commit_sha1="0".repeat(40)},"gitlink-boundary:"+C],
 ["main-owner",(b)=>{b.sources[C].catalog.project_owner="Other"},"catalog-owner:"+C],
 ["main-added-owner",(b)=>{b.delta.branches.find(z=>z.repo==="eternalimit/chatgpt").added[0].project_owner="Other"},"new-owner:"+C],
 ["wrong-root-reference",(b)=>{b.delta.technical_controls.original_kernel_sha256_historical_reference="0".repeat(64)},"historical-kernel-reference"],
 ["extra-branch",(b)=>{b.delta.branches.push(copy(b.delta.branches[0]))},"branch-cardinality"],
 ["missing-tree",(b)=>{delete b.sources[B].tree},"missing-source-object:"+B],
 ["unknown-repository",(b)=>{other(b).repo="another/repo"},"branch-set"]
 ];
 const baseline=verifyOwnerBundleV7(bundle);
 const tests=cases.map(([id,mutate,want])=>{
  const clone=copy(bundle);mutate(clone);
  const r=verifyOwnerBundleV7(clone);
  return {id,detected:!r.pass&&r.errors.includes(want),reason:r.errors};
 });
 return {baseline,tests,all_pass:baseline.pass&&tests.every(x=>x.detected)};
}

if(typeof module!=="undefined"&&module.exports)module.exports={verifyOwnerBundleV7,testOwnerBundleV7};
