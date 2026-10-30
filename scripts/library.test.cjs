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
test('all historical dates have public provenance and month-only papers are not assigned a day',()=>{
 const historical=M.collect(data.dates,'survey');
 assert.equal(historical.filter(p=>p.publication.basis==='arxiv_first_submission').length,322);
 assert.equal(historical.filter(p=>p.publication.precision==='month').length,5);
 for(const p of historical){
  assert.equal(p.publication.date,p.eventDate);
  assert.match(p.publication.source,/^https:\/\//);
  if(p.publication.timestamp)assert.equal(p.publication.timestamp.slice(0,10),p.publication.date);
  assert.ok(M.byPublication(data.dates,p.publication.date.slice(0,7)).some(q=>q.id===p.id));
  if(p.publication.precision==='month')assert.ok(!M.byPublication(data.dates,p.publication.date+'-01').some(q=>q.id===p.id));
 }
});
test('publication browsing keeps first submission, latest annotation, and real correction target',()=>{
 const original={...M.collect(data.dates,'survey')[0],id:'example',publication:{date:'2024-03-02',precision:'day',source:'https://arxiv.org/abs/2403.01248'}};
 const revision={...original,publication:undefined,eventType:'revision',eventDate:'2026-10-29',bucket:'revision',summary:'Updated annotation'};
 const days=[{date:'2026-10-19',collectionType:'survey',papers:[original]},{date:'2026-10-30',papers:[revision]}];
 const p=M.byPublication(days,'2024-03-02')[0];
 assert.equal(p.summary,'Updated annotation');assert.equal(p.reportDate,'2026-10-30');
 assert.equal(M.byPublication(days,'2026-10-29').length,0);
 const proposal=P.create({days,paperId:p.id,date:p.reportDate,field:'summary',value:'Corrected historical paper.',evidence:{primary_url:p.url,locator:'Abstract',evidence:'Evidence from the paper.'}},labels);
 assert.equal(proposal.entries[0].date,'2026-10-30');
});
test('publication browsing uses UTC release dates and never treats a revision as a first release',()=>{
 const p={...M.collect(data.dates,'survey')[0],publication:undefined,eventType:'first_submission',eventDate:'2026-10-28T22:52:21-05:00',sourceEventTime:'2026-10-29T03:52:21+00:00'};
 const days=[{date:'2026-10-28',papers:[p]}];
 assert.equal(M.byPublication(days,'2026-10-29').length,1);
 assert.equal(M.byPublication(days,'2026-10-28').length,0);
 assert.equal(M.publication({...p,eventType:'revision'}),null);
 assert.equal(M.collect(days,'2026-10-28').length,1);
});
