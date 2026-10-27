const test=require('node:test'),assert=require('node:assert/strict'),fs=require('node:fs'),path=require('node:path');
require('../assets/feed-model.js');
const M=globalThis.FeedModel,P=require('../assets/feed-proposals.js');
const data=JSON.parse(fs.readFileSync(path.join(__dirname,'../data/daily-results.json')));
const labels=JSON.parse(fs.readFileSync(path.join(__dirname,'../data/taxonomy-labels.json')));
test('survey collection is separate from daily discoveries and has no invented search run',()=>{
 const historical=M.collect(data.dates,'survey'),daily=M.collect(data.dates,'daily');
 assert.equal(historical.length,337);assert.ok(historical.every(p=>M.kind(p)==='archive'));
 assert.ok(daily.every(p=>M.kind(p)!=='archive'));
 assert.deepEqual(M.collect(data.dates,'2026-10-26').map(p=>p.id),M.collect(data.dates.filter(d=>d.collectionType!=='survey'),'2026-10-26').map(p=>p.id));
 assert.equal(M.collect(data.dates,'all').length,new Set([...historical,...daily].map(p=>p.id)).size);
});
test('latest annotation replaces an archived record without counting the paper twice',()=>{
 const p=M.collect(data.dates,'survey')[0];
 const days=[{date:'2026-10-19',collectionType:'survey',papers:[p]},{date:'2026-10-27',papers:[{...p,summary:'Reviewed daily annotation',bucket:'late_discovery'}]}];
 assert.equal(M.collect(days,'all').length,1);assert.equal(M.collect(days,'all')[0].summary,'Reviewed daily annotation');
 assert.equal(M.collect(days,'survey')[0].summary,p.summary);
});
test('historical papers support combined filters and the existing correction pipeline',()=>{
 const p=M.collect(data.dates,'survey').find(p=>p.taxonomy.model_type.includes('LLM'));
 assert.ok(M.matches(p,{model_type:'LLM',application:p.application},p.title.slice(0,10),'archive'));
 assert.ok(!M.matches(p,{model_type:'Hybrid'},'','archive'));
 const proposal=P.create({days:data.dates,paperId:p.id,date:p.reportDate,field:'summary',value:'Reviewed historical summary.',evidence:{primary_url:p.url,locator:'Section 3',evidence:'Verified against the paper.'}},labels);
 const next=P.apply(data,proposal,labels);
 assert.equal(M.collect(next.dates,'survey').find(x=>x.id===p.id).summary,'Reviewed historical summary.');
 assert.deepEqual(next.dates.filter(d=>d.collectionType!=='survey'),data.dates.filter(d=>d.collectionType!=='survey'));
});
test('export excludes private research metadata and does not promote provisional labels',()=>{
 const papers=M.collect(data.dates,'survey'),text=JSON.stringify(papers);
 assert.doesNotMatch(text,/\/Users\/|\/home\/|docs\.google\.com|slack\.com|127\.0\.0\.1|review_file|retained_source/);
 for(const p of papers){
  assert.ok(p.eventDate<='2026-09-30');
  for(const [key,grade] of Object.entries(p.taxonomyGrades)){
   if(['P','C'].includes(grade))assert.ok(p.taxonomy[key].every(v=>labels.sentinels.includes(v)));
  }
 }
});
