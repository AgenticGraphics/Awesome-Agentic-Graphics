/* A correction is a bounded data proposal, never an instruction to write arbitrary paths. */
(function(root){
 'use strict';
 const fields=[
  {key:'title',label:'Paper title',type:'text',max:400,group:'Paper'},
  {key:'summary',label:'Short summary',type:'text',max:1600,group:'Paper'},
  {key:'applications',label:'Application area',type:'multi',group:'Paper'},
  {key:'operations',label:'Operation',type:'multi',group:'Paper'},
  {key:'scope',label:'Survey scope',type:'single',group:'Paper'},
  ...Object.entries({task:['Task','Specification'],input_form:['Input','Specification'],output:['Output','Specification'],model_type:['Model type','Base model'],model_training:['Model training','Base model'],planning:['Planning','Harness'],workflow:['Workflow','Harness'],update_strategy:['Update strategy','Harness'],verifier:['Verifier','Harness'],feedback_assessment:['Feedback assessment','Harness'],feedback_observation:['Feedback observation','Harness'],memory_time:['Memory duration','Harness'],memory_reach:['Memory reach','Harness'],action_type:['Action type','Graphics interface'],graphics_software:['Graphics software','Graphics interface'],tools:['Tools','Graphics interface'],resources:['Resources','Graphics interface'],representation:['Representation','Graphics interface']}).map(([key,[label,group]])=>({key:'taxonomy.'+key,label,type:'multi',group}))
 ];
 const scopes={core:'Core',scope_dependent:'Scope-dependent',enabling_or_adjacent:'Adjacent / enabling',excluded:'Excluded',unresolved:'Needs review'};
 const clone=x=>JSON.parse(JSON.stringify(x));
 const equal=(a,b)=>JSON.stringify(a)===JSON.stringify(b);
 const descriptor=key=>fields.find(f=>f.key===key);
 const options=(key,labels)=>key==='applications'?labels.application_families:key==='operations'?labels.operations:key==='scope'?Object.keys(scopes):key.startsWith('taxonomy.')?[...labels.fields[key.slice(9)],...labels.sentinels]:[];
 function read(p,key){if(!descriptor(key))throw new Error('Unsupported correction field.');return clone(key.startsWith('taxonomy.')?p.taxonomy[key.slice(9)]:key==='applications'?(p.applications||[p.application]):key==='operations'?(p.operations||[]):p[key]);}
 function checkValue(key,value,labels){
  const field=descriptor(key);if(!field)throw new Error('Unsupported correction field.');
  if(field.type==='text'){if(typeof value!=='string'||!value.trim()||value.length>field.max)throw new Error('Enter a proposed value within the length limit.');return;}
  const list=field.type==='single'?[value]:value;
  if(!Array.isArray(list)||!list.length||list.some(v=>!options(key,labels).includes(v))||new Set(list).size!==list.length)throw new Error('Choose valid values from the available options.');
  if(key.startsWith('taxonomy.')&&list.length>1&&list.some(v=>labels.sentinels.includes(v)))throw new Error('Choose an unknown value on its own, or select concrete labels.');
 }
 function checkEvidence(e){
  let u;try{u=new URL(e?.primary_url);}catch{throw new Error('Add a supporting paper URL.');}
  if(!['https:','http:'].includes(u.protocol)||u.username||u.password)throw new Error('Use a public HTTP or HTTPS evidence URL.');
  if(typeof e.locator!=='string'||!e.locator.trim()||e.locator.length>200)throw new Error('Add a section, page, or figure for the evidence.');
  if(typeof e.evidence!=='string'||!e.evidence.trim()||e.evidence.length>1200)throw new Error('Explain the correction and its evidence (up to 1,200 characters).');
 }
 function create({days,paperId,date,field,value,evidence,allDates=false},labels){
  checkValue(field,value,labels);checkEvidence(evidence);
  const entries=[];
  for(const day of days){
   if(!allDates&&day.date!==date)continue;
   const paper=day.papers.find(p=>p.id===paperId);if(!paper)continue;
   const before=read(paper,field);
   if(equal(before,value))continue;
   entries.push({date:day.date,before,after:clone(value),...(field.startsWith('taxonomy.')?{beforeEvidence:clone(paper.taxonomyEvidence?.[field.slice(9)]||null)}:{})});
  }
  if(!entries.length)throw new Error('The proposed value matches the saved value. Choose a different value.');
  return {schemaVersion:1,kind:'paper-correction',paperId,field,entries,evidence:clone(evidence)};
 }
 function apply(data,proposal,labels){
  if(!proposal||proposal.schemaVersion!==1||proposal.kind!=='paper-correction'||!descriptor(proposal.field)||typeof proposal.paperId!=='string')throw new Error('Unsupported correction proposal.');
  if(!Array.isArray(proposal.entries)||!proposal.entries.length||proposal.entries.length>data.dates.length)throw new Error('Invalid correction targets.');
  checkEvidence(proposal.evidence);
  const next=clone(data),seen=new Set();
  for(const entry of proposal.entries){
   if(seen.has(entry.date))throw new Error('Duplicate correction target.');seen.add(entry.date);
   const day=next.dates.find(d=>d.date===entry.date),paper=day?.papers.find(p=>p.id===proposal.paperId);
   if(!paper)throw new Error('The target paper or search date no longer exists.');
   const key=proposal.field;checkValue(key,entry.after,labels);
   if(!equal(read(paper,key),entry.before))throw new Error('Saved data has changed since this suggestion. Review it against the latest record.');
   if(key.startsWith('taxonomy.')){
    const name=key.slice(9),oldEvidence=paper.taxonomyEvidence?.[name]||null;
    if(!equal(oldEvidence,entry.beforeEvidence))throw new Error('Saved evidence has changed since this suggestion. Review it against the latest record.');
    paper.taxonomy[name]=clone(entry.after);if(paper.taxonomyGrades)paper.taxonomyGrades[name]='reviewed';paper.taxonomyEvidence=paper.taxonomyEvidence||{};
    paper.taxonomyEvidence[name]={primary_url:proposal.evidence.primary_url,locator:proposal.evidence.locator,evidence:proposal.evidence.evidence,level:'derived',reasoning:'Community correction with cited evidence; requires review before publication.'};
   }else{
    paper[key]=clone(entry.after);
    // These display aliases must agree with the corrected canonical field.
    if(key==='applications')paper.application=entry.after[0];
    if(key==='scope')paper.scopeLabel=scopes[entry.after];
    if(key==='title'&&paper.shortTitle)delete paper.shortTitle;
   }
  }
  const latest=new Map();
  next.dates.slice().sort((a,b)=>a.date.localeCompare(b.date)).forEach(d=>d.papers.forEach(p=>latest.set(p.id,p)));
  next.uniquePapers=[...latest.values()].filter(p=>!['excluded','unresolved'].includes(p.scope)).length;
  return next;
 }
 function parse(text){
  try{return JSON.parse(text);}catch{}
  const matches=[...text.matchAll(/<!-- agentic-feed-proposal:v1 -->\s*```json\s*\n([\s\S]*?)\n```\s*<!-- \/agentic-feed-proposal -->/g)];
  if(matches.length!==1)throw new Error('Expected exactly one structured correction block.');
  return JSON.parse(matches[0][1]);
 }
 root.FeedProposals={fields,scopes,descriptor,options,read,checkValue,create,apply,parse};
 if(typeof module!=='undefined')module.exports=root.FeedProposals;
})(typeof window==='undefined'?globalThis:window);
