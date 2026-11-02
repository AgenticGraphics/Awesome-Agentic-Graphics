/* Runs only from trusted repository code. Issue content is data, never executable code. */
const fs=require('node:fs');
const crypto=require('node:crypto');
const {apply,parse}=require('../assets/feed-proposals.js');
const {validate}=require('../assets/feed-validation.js');
const FILE='data/daily-results.json';
function client(token,repository){
 if(!/^[A-Za-z0-9_.-]+\/[A-Za-z0-9_.-]+$/.test(repository))throw new Error('Invalid repository.');
 return async(method,path,body)=>{
  const response=await fetch(`https://api.github.com/repos/${repository}/${path}`,{
   method,headers:{Authorization:`Bearer ${token}`,Accept:method==='GET'&&path.startsWith('contents/')?'application/vnd.github.object+json':'application/vnd.github+json','X-GitHub-Api-Version':'2022-11-28','Content-Type':'application/json','User-Agent':'agentic-graphics-correction-bot'},
   body:body===undefined?undefined:JSON.stringify(body),signal:AbortSignal.timeout(30000)
  });
  if(!response.ok){const error=new Error(`GitHub ${method} ${path.split('?')[0]} returned ${response.status}.`);error.status=response.status;throw error;}
  return response.status===204?null:response.json();
 };
}
function content(file){
 if(file.type!=='file'||file.encoding!=='base64'||typeof file.content!=='string'||!Number.isSafeInteger(file.size)||file.size<0||file.size>8000000)throw new Error('Expected a bounded repository data file.');
 const bytes=Buffer.from(file.content,'base64');
 if(bytes.length!==file.size)throw new Error('Repository data size does not match its metadata.');
 return bytes.toString('utf8');
}
async function repositoryFile(api,path,ref){
 const file=await api('GET',`contents/${path}?ref=${ref}`);
 if(file.type!=='file'||!Number.isSafeInteger(file.size)||file.size<0||file.size>8000000)throw new Error('Expected a bounded repository data file.');
 // GitHub omits content for files over 1 MB. Read the immutable Git blob,
 // using only the SHA from this trusted repository's contents response.
 if(file.encoding==='none'){
  if(!/^[a-f0-9]{40}$/.test(file.sha))throw new Error('Invalid repository blob identity.');
  const blob=await api('GET',`git/blobs/${file.sha}`);
  if(blob.sha!==file.sha||blob.size!==file.size)throw new Error('Repository blob metadata changed.');
  return {sha:file.sha,text:content({...blob,type:'file'})};
 }
 return {sha:file.sha,text:content(file)};
}
async function comment(api,number,text){
 const marker=`<!-- feed-correction-bot:${number} -->`,body=`${text}\n\n${marker}`;
 const comments=await api('GET',`issues/${number}/comments?per_page=100`);
 const prior=comments.find(c=>c.user?.login==='github-actions[bot]'&&c.body?.includes(marker));
 if(prior){if(prior.body!==body)await api('PATCH',`issues/comments/${prior.id}`,{body});}
 else await api('POST',`issues/${number}/comments`,{body});
}
async function run({api,number,repository,runURL}){
 if(!Number.isSafeInteger(number)||number<=0)throw new Error('Invalid issue number.');
 const issue=await api('GET',`issues/${number}`);
 if(issue.pull_request||issue.state!=='open'||!issue.title?.startsWith('[Feed correction]')||!issue.body?.includes('<!-- agentic-feed-proposal:v1 -->'))return {status:'ignored'};
 if(issue.body.length>65536)throw new Error('The suggestion is too large.');
 const proposal=parse(issue.body),hash=crypto.createHash('sha256').update(JSON.stringify(proposal)).digest('hex').slice(0,12);
 const owner=repository.split('/')[0],branch=`feed-correction/issue-${number}`,commitMessage=`Feed correction #${number} (${hash})`;
 // Once a PR exists, issue edits never overwrite code already under review.
 const existing=await api('GET',`pulls?state=all&head=${encodeURIComponent(owner+':'+branch)}&base=page&per_page=100`);
 if(existing.length){
  const pr=existing[0];
  await comment(api,number,`The correction has a pull request: ${pr.html_url}\n\nIssue edits do not change that PR. Continue the discussion there; if it has been closed, submit a new correction. A maintainer must review and merge the change.`);
  return {status:'existing',url:pr.html_url};
 }
 const base=await api('GET','git/ref/heads/page'),baseSHA=base.object.sha;
 const source=await repositoryFile(api,FILE,baseSHA);
 const labels=JSON.parse((await repositoryFile(api,'data/taxonomy-labels.json',baseSHA)).text);
 const data=JSON.parse(source.text),next=apply(data,proposal,labels);validate(next,labels);
 const nextText=JSON.stringify(next,null,2)+'\n';
 if(nextText===source.text)throw new Error('There is no data change to propose.');
 // Recheck the live issue before writing so closed or edited submissions are not processed silently.
 const fresh=await api('GET',`issues/${number}`);
 if(fresh.state!=='open'||fresh.body!==issue.body)throw new Error('The issue changed during processing. Edit or reopen it to retry.');
 let head;
 try{head=await api('GET',`git/ref/heads/${branch}`);}catch(error){if(error.status!==404)throw error;}
 let commitSHA;
 if(head&&head.object.sha!==baseSHA){
  // Recover only an exact bot-generated commit after a partial previous attempt.
  const commit=await api('GET',`commits/${head.object.sha}`);
  const proposed=(await repositoryFile(api,FILE,head.object.sha)).text;
  if(commit.commit.message!==commitMessage||commit.parents.length!==1||commit.parents[0].sha!==baseSHA||commit.files.length!==1||commit.files[0].filename!==FILE||proposed!==nextText)throw new Error('The correction branch already contains different changes. A maintainer must inspect it; nothing was overwritten.');
  commitSHA=head.object.sha;
 }else{
  if(!head)await api('POST','git/refs',{ref:`refs/heads/${branch}`,sha:baseSHA});
  const saved=await api('PUT',`contents/${FILE}`,{branch,message:commitMessage,sha:source.sha,content:Buffer.from(nextText).toString('base64')});
  commitSHA=saved.commit.sha;
 }
 const safeID=String(proposal.paperId).replace(/[\r\n]/g,' ').slice(0,120);
 const body=[`Generated from #${number}.`,`Paper: **${safeID}**  \nField: **${proposal.field}**  \nSearch dates: ${proposal.entries.map(e=>e.date).join(', ')}`,
  'The structured suggestion passed data validation. Scientific correctness still needs human review.',
  '**Reviewer:** inspect the JSON diff and cited evidence. Merge manually only if the correction is valid. No automatic approval or merge is configured.',
  'If GitHub shows “Approve workflows to run”, approve the validation workflow and wait for it to pass before merging.',
  `Source suggestion: #${number}. The issue remains a feedback record; close it after resolution.`,runURL?`Automation run: ${runURL}`:''].filter(Boolean).join('\n\n');
 const pr=await api('POST','pulls',{title:`[Feed correction] ${safeID}: ${proposal.field}`,head:branch,base:'page',body,maintainer_can_modify:true});
 await comment(api,number,`Your correction is ready for review: ${pr.html_url}\n\nThe bot created the data change automatically. A maintainer will check the evidence and decide whether to merge. The website has not changed yet.`);
 return {status:'created',url:pr.html_url,sha:commitSHA};
}
async function main(){
 const event=JSON.parse(fs.readFileSync(process.env.GITHUB_EVENT_PATH,'utf8'));
 const repository=process.env.GITHUB_REPOSITORY,token=process.env.GITHUB_TOKEN;
 if(!token)throw new Error('A workflow token is required.');
 const api=client(token,repository),number=event.issue?.number;
 if(!number)return;
 try{const result=await run({api,number,repository,runURL:`https://github.com/${repository}/actions/runs/${process.env.GITHUB_RUN_ID}`});console.log(JSON.stringify(result));}
 catch(error){
  const reason=error.message.slice(0,600);
  try{await comment(api,number,`The bot could not create this correction PR.\n\n${reason}\n\nNo change was merged. For an outdated suggestion, open the latest website record and submit it again. A maintainer can inspect the workflow run for configuration errors.`);}catch{console.error('Could not post the failure notice. Check workflow permissions.');}
  throw error;
 }
}
module.exports={run,client,content,repositoryFile};
if(require.main===module)main().catch(error=>{console.error(error.message);process.exitCode=1;});
