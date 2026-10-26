// Maintainers run a dry run first, inspect the diff, then explicitly opt into writing.
const fs=require('node:fs');
const path=require('node:path');
const {apply,parse}=require('../assets/feed-proposals.js');
const {validate}=require('../assets/feed-validation.js');
function main(){
 const args=process.argv.slice(2),write=args.includes('--write'),files=args.filter(a=>a!=='--write');
 if(files.length!==1||files[0].startsWith('--'))throw new Error('Usage: node scripts/apply-correction.cjs <proposal.json or issue-body.md> [--write]');
 const root=path.join(__dirname,'..'),feedPath=path.join(root,'data/daily-results.json');
 const original=fs.readFileSync(feedPath,'utf8');
 const data=JSON.parse(original),labels=JSON.parse(fs.readFileSync(path.join(root,'data/taxonomy-labels.json'),'utf8'));
 const proposal=parse(fs.readFileSync(files[0],'utf8')),next=apply(data,proposal,labels);
 validate(next,labels);
 console.log(`Paper: ${proposal.paperId}\nField: ${proposal.field}`);
 for(const e of proposal.entries)console.log(`${e.date}: ${JSON.stringify(e.before)} -> ${JSON.stringify(e.after)}`);
 if(!write){console.log('Dry run passed. No data was changed. Review the evidence, then rerun with --write to apply locally.');return;}
 // Reject concurrent changes between validation and write.
 if(fs.readFileSync(feedPath,'utf8')!==original)throw new Error('The feed changed during review; retry against the current file.');
 const backup=feedPath+'.review-backup';
 fs.writeFileSync(backup,original,{flag:'wx'});
 try{fs.writeFileSync(feedPath,JSON.stringify(next,null,2)+'\n');fs.unlinkSync(backup);}catch(error){console.error('A backup is retained at data/daily-results.json.review-backup.');throw error;}
 console.log('Applied locally. Inspect the Git diff and open a PR for review; nothing was committed, pushed, or merged.');
}
try{main();}catch(error){console.error(error.message);process.exitCode=1;}
