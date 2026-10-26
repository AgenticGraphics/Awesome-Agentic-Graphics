/* Opens a draft only. User submission and maintainer approval happen on GitHub. */
(function(root){
 'use strict';
 function issueDraft({paper=null,type,message,evidence='',date='all',proposal=null}){
  const title=`[Feed ${proposal?'correction':'feedback'}] ${type}: ${paper?paper.shortTitle||paper.title:'Daily paper feed'}`.slice(0,220);
  const parts=['## Paper',paper?`${paper.title}\n\nPaper ID: ${paper.id}\n\n${paper.url}`:'General feedback / missing paper','## Search report',date,'## Feedback',message];
  if(proposal){
   const show=v=>Array.isArray(v)?v.join(', '):v;
   parts.push('## Proposed correction',`Field: ${proposal.field}\n\n`+proposal.entries.map(e=>`${e.date}: ${show(e.before)} → ${show(e.after)}`).join('\n\n'));
   parts.push('## Evidence',`${proposal.evidence.primary_url}\n\n${proposal.evidence.locator}`);
   parts.push('<details>\n<summary>Structured correction for maintainer review</summary>\n\n<!-- agentic-feed-proposal:v1 -->\n```json\n'+JSON.stringify(proposal)+'\n```\n<!-- /agentic-feed-proposal -->\n\n</details>');
  }else parts.push('## Supporting evidence',evidence||'Not provided');
  parts.push('---','Submitting a valid structured correction triggers an automatic pull request when repository automation is enabled. Maintainers review the evidence and merge manually; this submission does not change the website immediately.');
  const body=parts.join('\n\n'),link=new URL('https://github.com/AgenticGraphics/Awesome-Agentic-Graphics/issues/new');
  link.searchParams.set('title',title);link.searchParams.set('body',body);
  // Long multilingual suggestions can exceed GitHub's query-string limit.
  const requiresPaste=link.href.length>7500;
  if(requiresPaste)link.searchParams.delete('body');
  return {url:link.href,body,requiresPaste};
 }
 const issueURL=input=>issueDraft(input).url;
 root.FeedFeedback={issueDraft,issueURL};
 if(typeof module!=='undefined')module.exports=root.FeedFeedback;
})(typeof window==='undefined'?globalThis:window);
