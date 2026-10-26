(function(root){
 'use strict';
 const $=s=>document.querySelector(s);
 const esc=s=>String(s??'').replace(/[&<>"']/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]));
 function init({days,getDate}){
  const P=root.FeedProposals,dialog=$('#feedback-dialog'),form=$('#feedback-form');
  const labelsReady=fetch(new URL('data/taxonomy-labels.json',document.baseURI),{cache:'no-store'}).then(r=>{if(!r.ok)throw new Error();return r.json();}).catch(()=>null);
  let paper=null,opener=null,labels=null,draft=null,opening=0;
  const correction=()=>!!paper&&$('#feedback-type').value==='correction';
  const show=v=>Array.isArray(v)?v.join(' · '):P.scopes[v]||v;
  const clearReview=()=>{$('#feedback-review').hidden=true;$('#feedback-error').textContent='';draft=null;$('#feedback-draft').removeAttribute('href');};
  function value(){const field=P.descriptor($('#correction-field').value);if(field.type==='text')return $('#correction-text').value.trim();if(field.type==='single')return $('#correction-select').value;return [...document.querySelectorAll('[name="correction-label"]:checked')].map(e=>e.value);}
  function renderField(){
   if(!paper||!labels)return;
   const key=$('#correction-field').value,field=P.descriptor(key),current=P.read(paper,key);
   $('#correction-current-value').textContent=show(current);
   let control;
   if(field.type==='text')control=`<label>Suggested value<textarea id="correction-text" rows="3" maxlength="${field.max}">${esc(current)}</textarea></label>`;
   else if(field.type==='single')control=`<label>Suggested value<select id="correction-select">${P.options(key,labels).map(v=>`<option value="${esc(v)}" ${v===current?'selected':''}>${esc(show(v))}</option>`).join('')}</select></label>`;
   else control=`<fieldset class="correction-options"><legend>Suggested value</legend><p>Select one or more labels. Deselect any that should be removed.</p><div>${P.options(key,labels).map(v=>`<label><input type="checkbox" name="correction-label" value="${esc(v)}" ${current.includes(v)?'checked':''}><span>${esc(v)}</span></label>`).join('')}</div></fieldset>`;
   $('#correction-value').innerHTML=control;clearReview();
  }
  function renderMode(){
   const active=correction();
   $('#correction-fields').hidden=!active;
   $('#feedback-title').textContent=active?'Suggest a correction.':'Share feedback.';
   $('.correction-steps').hidden=!active;
   $('#feedback-description').textContent=active?'Choose the correction and cite the paper. Submit it on GitHub to request an automatic PR for human review.':'Share a missing paper, website issue, or other suggestion with the team.';
   $('#feedback-message-label').textContent=active?'Why is this change needed?':'Your feedback';
   $('#feedback-message').placeholder=active?'Explain the correction and what the paper says.':'Tell us what could be improved.';
   $('#feedback-evidence').required=active;$('#feedback-locator').required=active;
   $('#feedback-locator-label').hidden=!active;$('#feedback-evidence-optional').hidden=active;
   if(active)renderField();clearReview();
  }
  async function open(p,button){
   const token=++opening;paper=p;opener=button;form.reset();clearReview();
   $('#feedback-copy-status').textContent='';$('#feedback-copy-fallback').hidden=true;
   $('#feedback-context').textContent=p?`${p.title} · ${p.id}`:'General feedback about the daily paper feed';
   $('#feedback-type').value=p?'correction':'feedback';$('#feedback-type').querySelector('[value="correction"]').disabled=!p;
   labels=await labelsReady;if(token!==opening)return;
   if(!labels){$('#feedback-type').value='feedback';$('#feedback-type').querySelector('[value="correction"]').disabled=true;}
   if(p&&labels){
    const groups=[...new Set(P.fields.map(f=>f.group))];
    $('#correction-field').innerHTML=groups.map(g=>`<optgroup label="${g}">${P.fields.filter(f=>f.group===g).map(f=>`<option value="${f.key}">${f.label}</option>`).join('')}</optgroup>`).join('');
    $('#correction-field').value='taxonomy.model_type';
    const count=days.filter(d=>d.papers.some(record=>record.id===p.id)).length;
    $('#correction-all-wrap').hidden=count<2;
    $('#correction-all-label').textContent=`Also update other search dates (${count} saved entries)`;
    $('#feedback-evidence').value=p.url;
   }
   renderMode();if(!labels)$('#feedback-error').textContent='Correction options could not load. You can still share feedback, or reload the page to try again.';
   dialog.showModal();dialog.scrollTop=0;
  }
  function close(){dialog.close();opener?.focus({preventScroll:true});}
  document.addEventListener('click',e=>{
   const button=e.target.closest('[data-feedback-id],[data-feedback]');if(!button)return;
   const p=button.dataset.feedbackId?root.FeedModel.collect(days,getDate()).find(p=>p.id===button.dataset.feedbackId):null;
   open(p,button);
  });
  $('.feedback-close').addEventListener('click',close);$('.feedback-cancel').addEventListener('click',close);
  dialog.addEventListener('click',e=>{if(e.target===dialog){const r=dialog.getBoundingClientRect();if(e.clientX<r.left||e.clientX>r.right||e.clientY<r.top||e.clientY>r.bottom)close();}});
  $('#feedback-type').addEventListener('change',renderMode);$('#correction-field').addEventListener('change',renderField);
  form.addEventListener('input',clearReview);
  form.addEventListener('change',e=>{
   if(e.target.name==='correction-label'&&e.target.checked){
    const unknown=labels.sentinels.includes(e.target.value);
    document.querySelectorAll('[name="correction-label"]:checked').forEach(other=>{if(other!==e.target&&(unknown||labels.sentinels.includes(other.value)))other.checked=false;});
   }
   clearReview();
  });
  form.addEventListener('submit',e=>{
   e.preventDefault();clearReview();
   try{
    const message=$('#feedback-message').value.trim(),evidence=$('#feedback-evidence').value.trim();
    if(!message)throw new Error('Please describe your suggestion.');
    const key=$('#correction-field').value;
    const proposal=correction()?P.create({days,paperId:paper.id,date:paper.reportDate,field:key,value:value(),evidence:{primary_url:evidence,locator:$('#feedback-locator').value.trim(),evidence:message},allDates:$('#correction-all').checked},labels):null;
    draft=root.FeedFeedback.issueDraft({paper,type:proposal?P.descriptor(key).label:'General feedback',message,evidence,date:paper?.reportDate||getDate(),proposal});
    $('#feedback-review-summary').innerHTML=proposal?`<strong>${esc(P.descriptor(key).label)}</strong>${proposal.entries.map(entry=>`<div class="correction-diff"><small>${esc(entry.date)}</small><span>${esc(show(entry.before))}</span><span aria-hidden="true">→</span><strong>${esc(show(entry.after))}</strong></div>`).join('')}`:`<p>${esc(message)}</p>`;
    $('#feedback-draft').href=draft.url;$('#feedback-copy').hidden=!draft.requiresPaste;$('#feedback-copy-status').textContent='';$('#feedback-copy-fallback').hidden=true;
    $('#feedback-draft').textContent=proposal?'Submit on GitHub →':'Send feedback on GitHub →';
    $('#feedback-next-step').textContent=draft.requiresPaste?'Copy this suggestion, open the GitHub draft, and paste it into the description before submitting.':proposal?'Submit the prefilled issue on GitHub. When automation is enabled, the bot validates the correction and replies with a pull request. Our team reviews and merges it manually.':'Submit the feedback on GitHub for our team to review. General feedback does not create a pull request.';
    $('#feedback-review').hidden=false;$('#feedback-review').focus({preventScroll:true});$('#feedback-review').scrollIntoView({block:'nearest',behavior:'smooth'});
   }catch(error){$('#feedback-error').textContent=error.message;}
  });
  $('#feedback-copy').addEventListener('click',async()=>{
   if(!draft)return;
   try{await navigator.clipboard.writeText(draft.body);$('#feedback-copy-status').textContent='Copied. Paste it into the GitHub issue description.';}
   catch{const area=$('#feedback-copy-fallback');area.value=draft.body;area.hidden=false;area.focus();area.select();$('#feedback-copy-status').textContent='Copy the selected text, then paste it into the GitHub issue description.';}
  });
 }
 root.FeedContribute={init};
})(window);
