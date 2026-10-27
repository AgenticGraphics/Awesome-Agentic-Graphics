const test=require('node:test');
const assert=require('node:assert/strict');
const fs=require('node:fs');
const path=require('node:path');
const os=require('node:os');
const {execFileSync}=require('node:child_process');
const P=require('../assets/feed-proposals.js');
const {issueDraft}=require('../assets/feed-feedback.js');
const {validate}=require('../assets/feed-validation.js');
const data=JSON.parse(fs.readFileSync(path.join(__dirname,'../data/daily-results.json')));
const labels=JSON.parse(fs.readFileSync(path.join(__dirname,'../data/taxonomy-labels.json')));
const paper=data.dates[0].papers[0];
const nextDate=new Date(Date.parse(data.dates.map(d=>d.date).sort().at(-1)+'T00:00:00Z')+86400000).toISOString().slice(0,10);
const evidence={primary_url:paper.url,locator:'Section 3.2, page 5',evidence:'The model reads rendered images.'};
const create=(extra={})=>P.create({days:data.dates,paperId:paper.id,date:data.dates[0].date,field:'taxonomy.model_type',value:['VLM'],evidence,...extra},labels);
test('form values map to one exact taxonomy field, with evidence and a saved before-value',()=>{
 const proposal=create(),before=JSON.stringify(data),next=P.apply(data,proposal,labels);
 assert.equal(JSON.stringify(data),before);
 assert.deepEqual(next.dates[0].papers[0].taxonomy.model_type,['VLM']);
 assert.equal(next.dates[0].papers[0].taxonomyEvidence.model_type.locator,evidence.locator);
 assert.equal(validate(next,labels),true);
 assert.equal(next.dates[0].papers[0].summary,paper.summary);
 assert.equal(next.dates[0].papers[0].eventDate,paper.eventDate);
});
test('date-specific correction leaves other search reports unchanged',()=>{
 const proposal=create();assert.deepEqual(proposal.entries.map(e=>e.date),[data.dates[0].date]);
 const next=P.apply(data,proposal,labels);assert.deepEqual(next.dates.slice(1),data.dates.slice(1));
});
test('all-date correction records and checks each affected before-value',()=>{
 const days=structuredClone(data.dates);days.push({...structuredClone(days[0]),date:nextDate});
 const proposal=P.create({days,paperId:paper.id,date:days[0].date,field:'taxonomy.model_type',value:['VLM'],evidence,allDates:true},labels);
 assert.ok(proposal.entries.some(e=>e.date===nextDate));
 const next=P.apply({...data,dates:days},proposal,labels);assert.deepEqual(next.dates.at(-1).papers[0].taxonomy.model_type,['VLM']);
});
test('edited summaries require no generated JavaScript file; application aliases stay consistent',()=>{
 const proposal=create({field:'summary',value:'A reviewed replacement summary.'});
 assert.equal(P.apply(data,proposal,labels).dates[0].papers[0].summary,'A reviewed replacement summary.');
 const next=P.apply(data,create({field:'applications',value:['2D Graphics']}),labels);
 assert.equal(next.dates[0].papers[0].application,'2D Graphics');assert.deepEqual(next.dates[0].papers[0].applications,['2D Graphics']);
});
test('rejects stale values and stale evidence rather than overwriting concurrent edits',()=>{
 const proposal=create(),edited=structuredClone(data);edited.dates[0].papers[0].taxonomy.model_type=['LLM'];assert.throws(()=>P.apply(edited,proposal,labels),/changed/);
 const changed=structuredClone(data);changed.dates[0].papers[0].taxonomyEvidence.model_type={primary_url:paper.url,locator:'New section',evidence:'Another review'};assert.throws(()=>P.apply(changed,proposal,labels),/evidence has changed/);
});
test('rejects unsupported fields, bad labels, missing evidence, and no-op suggestions',()=>{
 assert.throws(()=>create({field:'__proto__.polluted',value:true}),/Unsupported/);
 assert.throws(()=>create({value:['Made-up model']}),/valid values/);
 assert.throws(()=>create({value:['VLM','Not Reported']}),/unknown value/);
 assert.throws(()=>create({evidence:{...evidence,primary_url:'javascript:alert(1)'}}),/HTTP/);
 assert.throws(()=>create({evidence:{...evidence,locator:''}}),/section/);
 assert.throws(()=>create({value:paper.taxonomy.model_type}),/matches/);
});
test('whole proposal fails without partial mutation if any target is invalid',()=>{
 const proposal=create(),original=JSON.stringify(data);proposal.entries.push({...proposal.entries[0],date:'2099-01-01'});
 assert.throws(()=>P.apply(data,proposal,labels),/no longer exists/);assert.equal(JSON.stringify(data),original);
 const duplicate=create();duplicate.entries.push(duplicate.entries[0]);assert.throws(()=>P.apply(data,duplicate,labels),/Duplicate/);
});
test('GitHub draft round-trips the structured proposal without exposing it in the form',()=>{
 const proposal=create(),draft=issueDraft({paper,type:'Model type',message:evidence.evidence,date:data.dates[0].date,proposal});
 assert.deepEqual(P.parse(draft.body),proposal);assert.deepEqual(P.parse(JSON.stringify(proposal)),proposal);
 assert.throws(()=>P.parse(draft.body+'\n'+draft.body),/exactly one/);
 assert.ok(draft.body.includes('<details>'));assert.ok(draft.body.includes('Not Reported → VLM'));
});
test('long multilingual drafts use a short URL and preserve complete copyable content',()=>{
 const proposal=create({evidence:{...evidence,evidence:'分类依据'.repeat(250)}}),draft=issueDraft({paper,type:'Model type',message:proposal.evidence.evidence,proposal});
 assert.equal(draft.requiresPaste,true);assert.ok(draft.url.length<7500);assert.deepEqual(P.parse(draft.body),proposal);
});
test('review tool is dry-run by default and writes only with explicit --write',()=>{
 const dir=fs.mkdtempSync(path.join(os.tmpdir(),'feed-correction-test-'));
 try{
  for(const sub of ['scripts','assets','data'])fs.mkdirSync(path.join(dir,sub));
  for(const file of ['scripts/apply-correction.cjs','assets/feed-proposals.js','assets/feed-validation.js','data/taxonomy-labels.json','data/daily-results.json'])fs.copyFileSync(path.join(__dirname,'..',file),path.join(dir,file));
  const feed=path.join(dir,'data/daily-results.json'),original=fs.readFileSync(feed,'utf8'),proposal=path.join(dir,'reviewed.json');
  fs.writeFileSync(proposal,JSON.stringify(create()));
  const run=flags=>execFileSync(process.execPath,[path.join(dir,'scripts/apply-correction.cjs'),proposal,...flags],{encoding:'utf8'});
  assert.match(run([]),/No data was changed/);assert.equal(fs.readFileSync(feed,'utf8'),original);
  assert.match(run(['--write']),/Applied locally/);assert.deepEqual(JSON.parse(fs.readFileSync(feed,'utf8')).dates[0].papers[0].taxonomy.model_type,['VLM']);
  const applied=fs.readFileSync(feed,'utf8');assert.throws(()=>run(['--write']));assert.equal(fs.readFileSync(feed,'utf8'),applied);
 }finally{fs.rmSync(dir,{recursive:true,force:true});}
});
test('latest exclusion is respected across all dates and updates the derived unique count',()=>{
 const days=structuredClone(data.dates);days.push({...structuredClone(days[0]),date:nextDate});
 const proposal=P.create({days,paperId:paper.id,date:nextDate,field:'scope',value:'excluded',evidence},labels);
 const next=P.apply({...data,dates:days},proposal,labels);
 require('../assets/feed-model.js');
 const all=globalThis.FeedModel.collect(next.dates,'all');
 assert.ok(!all.some(p=>p.id===paper.id));assert.equal(next.uniquePapers,all.length);
 assert.ok(globalThis.FeedModel.collect(next.dates,data.dates[0].date).some(p=>p.id===paper.id));
});
