const test=require('node:test'),assert=require('node:assert/strict'),fs=require('node:fs'),path=require('node:path');
const {run}=require('./correction-bot.cjs');
const P=require('../assets/feed-proposals.js');
const {issueDraft}=require('../assets/feed-feedback.js');
const data=JSON.parse(fs.readFileSync(path.join(__dirname,'../data/daily-results.json'))),labels=JSON.parse(fs.readFileSync(path.join(__dirname,'../data/taxonomy-labels.json')));
const paper=data.dates[0].papers[0],evidence={primary_url:paper.url,locator:'Section 3',evidence:'The reviewer can inspect this specific evidence.'};
const proposal=P.create({days:data.dates,paperId:paper.id,date:data.dates[0].date,field:'summary',value:'A proposed replacement summary for review.',evidence},labels);
const issue={number:12,state:'open',title:'[Feed correction] Summary',body:issueDraft({paper,type:'Summary',message:evidence.evidence,proposal}).body};
const file=text=>({type:'file',encoding:'base64',size:Buffer.byteLength(text),content:Buffer.from(text).toString('base64'),sha:'file-sha'});
function fixture(){
 const state={issue:structuredClone(issue),data:structuredClone(data),calls:[],head:null,pulls:[],comments:[],commit:null,content:null,issueReads:0};
 const api=async(method,url,body)=>{
  state.calls.push({method,url,body});
  if(method==='GET'&&url==='issues/12'){state.issueReads++;return structuredClone(state.issue);}
  if(method==='GET'&&url.startsWith('pulls?'))return state.pulls;
  if(method==='GET'&&url==='git/ref/heads/page')return {object:{sha:'base-sha'}};
  if(method==='GET'&&url==='contents/data/daily-results.json?ref=base-sha')return file(JSON.stringify(state.data,null,2)+'\n');
  if(method==='GET'&&url==='contents/data/taxonomy-labels.json?ref=base-sha')return file(JSON.stringify(labels));
  if(method==='GET'&&url==='git/ref/heads/feed-correction/issue-12'){if(!state.head){const e=new Error('not found');e.status=404;throw e;}return {object:{sha:state.head}};}
  if(method==='POST'&&url==='git/refs'){assert.equal(body.ref,'refs/heads/feed-correction/issue-12');assert.equal(body.sha,'base-sha');state.head='base-sha';return {};}
  if(method==='PUT'&&url==='contents/data/daily-results.json'){
   assert.equal(body.branch,'feed-correction/issue-12');assert.equal(body.sha,'file-sha');state.content=Buffer.from(body.content,'base64').toString('utf8');state.head='new-sha';
   state.commit={commit:{message:body.message},parents:[{sha:'base-sha'}],files:[{filename:'data/daily-results.json'}]};return {commit:{sha:'new-sha'}};
  }
  if(method==='GET'&&url==='commits/new-sha')return state.commit;
  if(method==='GET'&&url==='contents/data/daily-results.json?ref=new-sha')return file(state.content);
  if(method==='POST'&&url==='pulls'){assert.equal(body.base,'page');const pr={html_url:'https://github.com/example/repo/pull/30',number:30};state.pulls.push(pr);return pr;}
  if(method==='GET'&&url==='issues/12/comments?per_page=100')return state.comments;
  if(method==='POST'&&url==='issues/12/comments'){state.comments.push({id:1,user:{login:'github-actions[bot]'},body:body.body});return {};}
  if(method==='PATCH'&&url==='issues/comments/1'){state.comments[0].body=body.body;return {};}
  throw new Error(`Unexpected request: ${method} ${url}`);
 };
 return {state,api,run:()=>run({api,number:12,repository:'example/repo'})};
}
const mutations=s=>s.calls.filter(c=>c.method!=='GET');
test('a valid submitted correction creates one data-only branch and PR, never merges or approves',async()=>{
 const f=fixture(),result=await f.run();assert.equal(result.status,'created');
 const changed=JSON.parse(f.state.content);assert.equal(changed.dates[0].papers[0].summary,proposal.entries[0].after);
 assert.deepEqual(mutations(f.state).map(c=>c.url),['git/refs','contents/data/daily-results.json','pulls','issues/12/comments']);
 assert.ok(f.state.comments[0].body.includes('/pull/30'));
 assert.ok(!f.state.calls.some(c=>/merge|reviews/.test(c.url)));
});
test('retries and issue edits reuse the PR without overwriting reviewed changes',async()=>{
 const f=fixture();await f.run();const original=f.state.content;
 f.state.issue.body=f.state.issue.body.replace('reviewer can inspect','reviewer should inspect');f.state.calls=[];
 assert.equal((await f.run()).status,'existing');assert.equal(f.state.content,original);
 assert.ok(!mutations(f.state).some(c=>c.url==='pulls'||c.url.startsWith('contents/')||c.url==='git/refs'));
 f.state.calls=[];await f.run();assert.equal(mutations(f.state).length,0);
});
test('ordinary feedback and closed issues are ignored',async()=>{
 for(const patch of [{title:'General feedback'},{state:'closed'},{pull_request:{url:'example'}}]){const f=fixture();Object.assign(f.state.issue,patch);assert.equal((await f.run()).status,'ignored');assert.equal(mutations(f.state).length,0);}
});
test('invalid or stale suggestions cannot create a branch',async()=>{
 const f=fixture();f.state.data.dates[0].papers[0].summary='A concurrent correction';await assert.rejects(f.run(),/changed/);assert.equal(mutations(f.state).length,0);
 const g=fixture();g.state.issue.body=g.state.issue.body.replace('"field":"summary"','"field":"__proto__.polluted"');await assert.rejects(g.run(),/Unsupported/);assert.equal(mutations(g.state).length,0);
});
test('issue edits during validation abort before mutation',async()=>{
 const f=fixture(),api=async(...args)=>{const result=await f.api(...args);if(args[1]==='issues/12'&&f.state.issueReads===2)result.body+='changed';return result;};
 await assert.rejects(run({api,number:12,repository:'example/repo'}),/changed during processing/);assert.equal(mutations(f.state).length,0);
});
test('an interrupted create-PR attempt resumes its exact validated commit',async()=>{
 const f=fixture();let fail=true;
 const api=async(...args)=>{if(args[0]==='POST'&&args[1]==='pulls'&&fail){fail=false;throw new Error('temporary failure');}return f.api(...args);};
 await assert.rejects(run({api,number:12,repository:'example/repo'}),/temporary/);f.state.calls=[];
 const result=await run({api,number:12,repository:'example/repo'});assert.equal(result.status,'created');assert.ok(!mutations(f.state).some(c=>c.method==='PUT'||c.url==='git/refs'));
});
test('foreign changes on an existing correction branch are never overwritten',async()=>{
 const f=fixture();f.state.head='new-sha';f.state.commit={commit:{message:'Unrelated change'},parents:[{sha:'base-sha'}],files:[{filename:'other.txt'}]};f.state.content=JSON.stringify(data);
 await assert.rejects(f.run(),/different changes/);assert.equal(mutations(f.state).length,0);
});
test('permission errors propagate instead of claiming that a PR exists',async()=>{
 const f=fixture(),api=async(...args)=>{if(args[0]==='POST'&&args[1]==='pulls'){const e=new Error('GitHub permission denied');e.status=403;throw e;}return f.api(...args);};
 await assert.rejects(run({api,number:12,repository:'example/repo'}),/permission denied/);assert.equal(f.state.pulls.length,0);assert.equal(f.state.comments.length,0);
});
