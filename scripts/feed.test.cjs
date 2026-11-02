const test=require('node:test');
const assert=require('node:assert/strict');
const fs=require('node:fs');
const path=require('node:path');
const vm=require('node:vm');
const {validate}=require('../assets/feed-validation.js');
const {issueURL}=require('../assets/feed-feedback.js');
const root=path.join(__dirname,'..');
const data=JSON.parse(fs.readFileSync(path.join(root,'data/daily-results.json')));
const labels=JSON.parse(fs.readFileSync(path.join(root,'data/taxonomy-labels.json')));
const copy=()=>structuredClone(data);
test('saved feed validates; repeated paper across different dates is valid',()=>assert.equal(validate(data,labels),true));
for(const [name,change] of [
 ['duplicate report',d=>d.dates.push(d.dates[0])],
 ['invalid calendar date',d=>d.dates[0].date='2026-02-30'],
 ['duplicate paper in a report',d=>d.dates[0].papers.push(d.dates[0].papers[0])],
 ['executable paper URL',d=>d.dates[0].papers[0].url='javascript:alert(1)'],
 ['misspelled taxonomy label',d=>d.dates[0].papers[0].taxonomy.model_type=['VLMM']],
 ['mixed unknown and concrete labels',d=>d.dates[0].papers[0].taxonomy.model_type=['VLM','Not Reported']],
 ['unsafe evidence URL',d=>d.dates[0].papers[0].taxonomyEvidence.task.primary_url='file:///private/paper.pdf']
])test(`rejects ${name}`,()=>{const d=copy();change(d);assert.throws(()=>validate(d,labels));});
test('feedback draft preserves Unicode, newlines, evidence and paper identity',()=>{
 const paper=data.dates[0].papers[0],message='分类有误 & feedback\nPlease check Figure #2.';
 const u=new URL(issueURL({paper,type:'Incorrect taxonomy',message,evidence:'https://arxiv.org/abs/2610.28210',date:'2026-10-20'}));
 assert.equal(u.origin,'https://github.com');assert.equal(u.pathname,'/AgenticGraphics/Awesome-Agentic-Graphics/issues/new');
 const body=u.searchParams.get('body');assert.ok(body.includes(message));assert.ok(body.includes(paper.id));assert.ok(body.includes('2026-10-20'));assert.ok(!body.includes('127.0.0.1'));assert.ok(!body.includes('/Users/'));
});
test('general feedback draft works without a paper',()=>{const u=new URL(issueURL({type:'Missing paper',message:'Please consider this paper.'}));assert.ok(u.searchParams.get('body').includes('General feedback / missing paper'));});
const loader=fs.readFileSync(path.join(root,'assets/feed-loader.js'),'utf8');
async function load(fetch){const context={window:{SURVEY_DATA:{}},document:{baseURI:'https://example.org/Awesome-Agentic-Graphics/'},URL,fetch,console:{warn(){}}};context.window.FeedValidation={validate};vm.runInNewContext(loader,context);await context.window.feedReady;return context.window.SURVEY_DATA.daily;}
test('loader reads the edited JSON without rebuilding a JS payload',async()=>{
 const edited=copy();edited.dates[0].papers[0].summary='Reviewed correction, merged into JSON.';
 const result=await load(async(url,opts)=>{assert.equal(url.href,'https://example.org/Awesome-Agentic-Graphics/data/daily-results.json');assert.equal(opts.cache,'no-store');return {ok:true,json:async()=>edited};});
 assert.equal(result.dates[0].papers[0].summary,'Reviewed correction, merged into JSON.');
});
test('network failures and malformed feeds do not silently display stale data',async()=>{
 assert.equal(await load(async()=>{throw new Error('offline');}),null);
 assert.equal(await load(async()=>({ok:false})),null);
 assert.equal(await load(async()=>({ok:true,json:async()=>({dates:'bad'})})),null);
});

test('rejects invalid publication precision, dates, source links and conflicting timestamps',()=>{
 for(const patch of [{precision:'year'},{date:'2025-02-30'},{source:'javascript:alert(1)'},{timestamp:'2020-01-01T00:00:00Z'}]){
  const d=copy(),p=d.dates.find(d=>d.collectionType==='survey').papers[0];
  Object.assign(p.publication,patch);assert.throws(()=>validate(d,labels));
 }
});
