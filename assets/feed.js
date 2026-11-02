(async function () {
 'use strict';
 const $ = s => document.querySelector(s), $$ = s => [...document.querySelectorAll(s)];
 const esc = v => String(v ?? '').replace(/[&<>"']/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]));
 const url = v => /^(https?:\/\/|data\/)/.test(v || '') ? esc(v) : '#';
 await window.feedReady;
 const M = window.FeedModel, daily = window.SURVEY_DATA.daily;
 if(!daily){
  $('#feed-date-title').textContent='Papers are temporarily unavailable';
  $('#feed-date-note').textContent='We could not load the latest feed. Please reload to try again.';
  $('#feed-papers').innerHTML='<button class="button secondary" id="feed-retry">Reload feed</button>';
  $('#feed-retry').addEventListener('click',()=>location.reload());
  return;
 }
 const days = (daily.dates || []).slice().sort((a,b)=>a.date.localeCompare(b.date));
 const reports = days.filter(d=>d.collectionType !== 'survey');
 const searchDates = new Set(reports.map(d=>d.date)), latest = reports.at(-1)?.date;
 const publicationPapers = M.published(days);
 const publicationDates = new Set(publicationPapers.map(p=>p.publication?.date).filter(Boolean));
 const params = new URLSearchParams(location.search);
 // Default to the visitor’s current month; preserve explicit collection and report links.
 const today=new Date(),currentMonth=`${today.getFullYear()}-${String(today.getMonth()+1).padStart(2,'0')}`;
 const basis = params.get('by')==='publication' ? 'publication' : params.get('by')==='search' || searchDates.has(params.get('date')) ? 'search' : 'publication';
 const validDate = date => /^\d{4}-\d{2}(?:-\d{2})?$/.test(date) && ((basis==='search'?searchDates:publicationDates).has(date) || (basis==='publication' && [...publicationDates].some(d=>d.startsWith(date))));
 const requested=params.get('date');
 const state = {basis,date:requested && (['all','survey','daily'].includes(requested)||validDate(requested)) ? requested : basis==='search'?(latest||'daily'):currentMonth,filters:{},query:'',event:'all',limit:12};
 const currentPapers = () => state.basis==='publication' && /^\d{4}-/.test(state.date) ? M.byPublication(days,state.date) : state.basis==='publication' && state.date==='all' ? publicationPapers : M.collect(days,state.date);
 const groups = [
  {name:'Specification',tone:'spec',keys:['task','input_form','output']},
  {name:'Base model',tone:'model',keys:['model_type','model_training']},
  {name:'Harness',tone:'harness',keys:['planning','workflow','update_strategy','verifier','feedback_assessment','feedback_observation','memory_time','memory_reach']},
  {name:'Graphics interface',tone:'interface',keys:['action_type','graphics_software','tools','resources','representation']}
 ];
 const names = {application:'Application',scope:'Scope',operations:'Operation',task:'Task',input_form:'Input',output:'Output',model_type:'Model',model_training:'Training',planning:'Planning',workflow:'Workflow',update_strategy:'Update strategy',verifier:'Verifier',feedback_assessment:'Assessment',feedback_observation:'Observation',memory_time:'Memory duration',memory_reach:'Memory reach',action_type:'Action',graphics_software:'Software',tools:'Tools',resources:'Resources',representation:'Representation'};
 const pretty = {'core':'Core','scope_dependent':'Scope-dependent','enabling_or_adjacent':'Adjacent / enabling','2D Graphics':'2D graphics','Static / Object':'3D objects','Static / CAD':'CAD','Static / Scene':'3D scenes','Dynamic / Articulated assets':'Articulation','Dynamic / Animation and temporal scene':'Animation & temporal scenes','Dynamic / Physical simulation and effects':'Physical simulation','Datasets and Benchmarks':'Datasets & benchmarks','Cross-category':'Cross-category','PO-1':'Fixed plan (PO-1)','PO-2':'Hybrid plan (PO-2)','PO-3':'Dynamic plan (PO-3)'};
 const label = v => pretty[v] || v;
 const formatDate = (date, opts={month:'long',day:'numeric',year:'numeric'}) => new Date((date.length===7?date+'-01':date)+'T12:00:00').toLocaleDateString('en-US',date.length===7?{month:'long',year:'numeric'}:opts);
 const icon = tone => `<svg viewBox="0 0 24 24" aria-hidden="true">${({spec:'<rect x="5" y="4" width="14" height="16" rx="2"/><path d="M8 9h8M8 13h6M8 17h4"/>',model:'<circle cx="12" cy="12" r="4"/><path d="M12 2v4m0 12v4M2 12h4m12 0h4M5 5l3 3m8 8 3 3M5 19l3-3m8-8 3-3"/>',harness:'<path d="M5 7h14M5 17h14M8 4v6m8 4v6"/><circle cx="8" cy="7" r="2"/><circle cx="16" cy="17" r="2"/>',interface:'<path d="m12 3 8 5v8l-8 5-8-5V8zM4 8l8 5 8-5M12 13v8"/>'})[tone]}</svg>`;
 const all = M.collect(days,'all');
 const options = key => [...new Set(all.flatMap(p=>M.values(p,key)))].sort((a,b)=>Number(M.sentinels.has(a))-Number(M.sentinels.has(b)) || label(a).localeCompare(label(b)));
 const primaryKeys = ['application','model_type','verifier','action_type'];
 const field = key => `<label class="feed-select"><span>${names[key]}</span><select data-facet="${key}" aria-label="Filter by ${names[key].toLowerCase()}"><option value="">All ${key==='application'?'applications':key==='model_type'?'models':key==='verifier'?'verifiers':key==='action_type'?'actions':'values'}</option>${options(key).map(v=>`<option value="${esc(v)}">${esc(label(v))}</option>`).join('')}</select></label>`;
 $('#feed-filters').innerHTML=`<div class="feed-primary-filters">${primaryKeys.map(field).join('')}</div><details class="feed-more-filters"><summary>More filters <span id="feed-more-count"></span><span aria-hidden="true">＋</span></summary><div class="feed-filter-sections"><fieldset><legend>Paper</legend>${field('scope')}${field('operations')}</fieldset>${groups.map(g=>`<fieldset class="tone-${g.tone}"><legend>${icon(g.tone)}${g.name}</legend>${g.keys.filter(k=>!primaryKeys.includes(k)).map(field).join('')}</fieldset>`).join('')}</div></details>`;
 $$('[data-facet]').forEach(s=>s.addEventListener('change',()=>{if(s.value)state.filters[s.dataset.facet]=s.value;else delete state.filters[s.dataset.facet];renderResults();}));
 $('#feed-search').addEventListener('input',e=>{state.query=e.target.value;renderResults();});
 $('#feed-event').addEventListener('change',e=>{state.event=e.target.value;renderResults();});
 const availableDates=()=>state.basis==='publication'?publicationDates:searchDates;
 const availableMonths=()=>[...new Set([...availableDates()].map(d=>d.slice(0,7)).concat(state.basis==='publication'?[currentMonth]:[]))].sort();
 let month=(/^\d{4}-/.test(state.date)?state.date:latest)?.slice(0,7),calendarFocus;
 function renderCalendar(){
  const dateSet=availableDates(),months=availableMonths();
  if(!months.includes(month))month=months.at(-1);
  if(!month)return;
  $('#feed-date-basis').value=state.basis;
  $('#feed-calendar-key-text').textContent=state.basis==='publication'?'Papers published':'Search available';
  const first=new Date(month+'-01T12:00:00'),last=new Date(first.getFullYear(),first.getMonth()+1,0).getDate(),offset=(first.getDay()+6)%7;
  $('#feed-calendar').innerHTML=`<div class="feed-month-nav"><button data-month-step="-1" aria-label="Previous month" ${months.indexOf(month)<=0?'disabled':''}>←</button><select id="feed-month-select" aria-label="Choose month">${months.map(m=>`<option value="${m}" ${m===month?'selected':''}>${formatDate(m)}</option>`).join('')}</select><button data-month-step="1" aria-label="Next month" ${months.indexOf(month)===months.length-1?'disabled':''}>→</button></div><div class="feed-month" role="group" aria-label="Select a ${state.basis} date"><div class="feed-weekdays" aria-hidden="true">${['M','T','W','T','F','S','S'].map(d=>`<span>${d}</span>`).join('')}</div><div class="feed-month-days">${'<span aria-hidden="true"></span>'.repeat(offset)}${Array.from({length:last},(_,i)=>{const d=month+'-'+String(i+1).padStart(2,'0'),available=dateSet.has(d);return available?`<button data-date="${d}" aria-pressed="${state.date===d}" aria-label="${formatDate(d)}, ${(state.basis==='publication'?M.byPublication(days,d):M.collect(days,d)).length} papers"><span>${i+1}</span><i></i></button>`:`<span class="feed-no-run">${i+1}</span>`;}).join('')}</div></div>${state.basis==='publication'?`<button class="feed-month-all" data-date="${month}" aria-pressed="${state.date===month}">View whole month <span>${M.byPublication(days,month).length}</span></button>`:''}`;
  $$('[data-date]').forEach(b=>b.addEventListener('click',()=>{calendarFocus=b.dataset.date;selectDate(b.dataset.date);$(`[data-date="${calendarFocus}"]`)?.focus({preventScroll:true});}));
  $('#feed-month-select').addEventListener('change',e=>{month=e.target.value;if(state.basis==='publication')selectDate(month);else renderCalendar();$('#feed-month-select').focus({preventScroll:true});});
  $$('[data-month-step]').forEach(b=>b.addEventListener('click',()=>{const step=Number(b.dataset.monthStep);month=months[months.indexOf(month)+step];if(state.basis==='publication')selectDate(month);else renderCalendar();const next=$(`[data-month-step="${step}"]:not(:disabled)`);(next||$('#feed-month-select'))?.focus({preventScroll:true});}));
  [['#feed-library','all'],['#feed-survey','survey'],['#feed-all-dates','daily']].forEach(([id,value])=>$(id).setAttribute('aria-pressed',String(state.date===value)));
 }
 function selectDate(date){
  state.date=date;
  if(/^\d{4}-/.test(date))month=date.slice(0,7);
  state.event='all';$('#feed-event').value='all';
  const next=new URL(location.href);next.searchParams.set('date',date);next.searchParams.set('by',state.basis);history.replaceState(null,'',next);
  renderCalendar();renderResults();
 }
 $('#feed-date-basis').addEventListener('change',e=>{state.basis=e.target.value;const months=availableMonths();if(!months.includes(month))month=months.at(-1);selectDate(state.basis==='publication'?month:latest);});
 [['#feed-library','all'],['#feed-survey','survey'],['#feed-all-dates','daily']].forEach(([id,value])=>$(id).addEventListener('click',()=>{if(value==='daily')state.basis='search';if(value==='survey')state.basis='publication';selectDate(value);}));
 $('#feed-library-count').textContent=M.collect(days,'all').length;
 $('#feed-survey-count').textContent=M.collect(days,'survey').length;
 $('#feed-daily-count').textContent=M.collect(days,'daily').length;
 const chip=(key,value,tone)=>`<button class="feed-chip tone-${tone}" data-chip-key="${key}" data-chip-value="${esc(value)}" title="Filter by ${names[key]}: ${esc(label(value))}">${icon(tone)}<span>${esc(label(value))}</span></button>`;
 function annotation(p){
  const pub=M.publication(p);
  return `<div class="feed-annotation">${pub?`<p class="feed-annotation-note">${pub.basis==='arxiv_first_submission'?'arXiv first submission':'Original release'}: <a href="${url(pub.source)}" target="_blank" rel="noopener">${esc(formatDate(pub.date))}</a>${pub.timestamp?` · ${esc(pub.timestamp)} (UTC)`:''}${pub.precision==='month'?' · Exact day not available':''}. ${esc(pub.evidence||'')}</p>`:''}<p class="feed-annotation-note">Evidence-based annotations · ${p.bucket==='survey_collection'?'From the survey’s retained reading records. Provisional labels are shown as “Unclear”.':'Unassessed fields remain “Not Reported”.'}</p>${groups.map(g=>`<section class="feed-tax-group tone-${g.tone}"><h5>${icon(g.tone)}${g.name}</h5><dl>${g.keys.map(k=>{const ev=p.taxonomyEvidence?.[k],vals=M.values(p,k);return `<div><dt>${names[k]}</dt><dd>${vals.map(v=>M.sentinels.has(v)?`<span class="feed-unknown">${esc(v)}</span>`:chip(k,v,g.tone)).join('')}${ev?`<details class="feed-field-evidence"><summary>Evidence</summary><p>${esc(ev.evidence)}${ev.reasoning?` <span class="feed-evidence-basis">${esc(ev.reasoning)}</span>`:''} <a href="${url(ev.primary_url)}" target="_blank" rel="noopener">${esc(ev.locator||'Source')}</a></p></details>`:''}</dd></div>`;}).join('')}</dl></section>`).join('')}<div class="feed-scope-evidence"><strong>Why this paper?</strong><p>${esc(p.scopeReason||p.scopeLabel||'See the source report.')}</p>${p.limitations?`<p>${esc(p.limitations)}</p>`:''}${(p.evidence||[]).map(e=>`<p>${esc(typeof e==='string'?e:e.evidence||e.text||'')}${e.primary_url?` <a href="${url(e.primary_url)}" target="_blank" rel="noopener">Source</a>`:''}</p>`).join('')}</div></div>`;
 }
 function card(p,i){
  const pub=M.publication(p),displayDate=state.basis==='publication'&&pub?pub.date:p.eventDate;
  const kind=M.kind(p), eventNames={new:'New submission',update:'Revision',catchup:'Earlier paper',pending:'Pending',archive:'Survey collection'};
  const featured=[['application',M.values(p,'application')[0],'spec'],['model_type',M.values(p,'model_type').find(v=>!M.sentinels.has(v)),'model'],['verifier',M.values(p,'verifier').find(v=>!M.sentinels.has(v)),'harness'],['action_type',M.values(p,'action_type').find(v=>!M.sentinels.has(v)),'interface']].filter(x=>x[1]);
  return `<article class="feed-card" aria-labelledby="feed-paper-${i}"><div class="feed-card-meta"><span class="feed-event feed-event-${kind}">${eventNames[kind]}</span><span>${state.basis==='publication'&&pub?(pub.basis==='arxiv_first_submission'?'First submitted':'Published'):kind==='archive'?'Published':p.eventType==='revision'?'Revised':'Submitted'} ${esc(displayDate?formatDate(displayDate.slice(0,10),{month:'short',day:'numeric',year:'numeric'}):'date unverified')}</span><span class="feed-scope">${esc(label(p.scope))}</span></div><h4 id="feed-paper-${i}" tabindex="-1"><a href="${url(p.url)}" target="_blank" rel="noopener">${esc(p.title)}</a></h4><p class="feed-card-summary">${esc(p.summary)}</p><div class="feed-card-tags">${featured.map(x=>chip(...x)).join('')}</div><div class="feed-card-links"><a class="feed-read-paper" href="${url(p.url)}" target="_blank" rel="noopener">Read paper</a><button class="feed-feedback-link feed-correction-button" data-feedback-id="${esc(p.id)}"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="m15 5 4 4M4 20l4-1L20 7a2.8 2.8 0 0 0-4-4L4 15z"/></svg><span>Suggest a correction</span><span aria-hidden="true">→</span></button></div><details class="feed-paper-details"><summary>Taxonomy & evidence <span aria-hidden="true">＋</span></summary>${annotation(p)}</details></article>`;
 }
 function renderRun(d){
  if(!d){$('#feed-run-details').innerHTML='<a class="feed-collection-notes" href="data/survey-collection.md" target="_blank">About this collection</a>';return;}
  const cov=d.coverage||{},limits=Array.isArray(cov)?cov:cov.limitations||[];
  const artifacts=Array.isArray(d.artifacts)?d.artifacts:Object.entries(d.artifacts||{}).map(([label,url])=>({label,url}));
  $('#feed-run-details').innerHTML=`<details class="feed-run-details"><summary>${d.collectionType==='survey'?'Collection notes':'Search coverage & report'} <span aria-hidden="true">＋</span></summary><div><p>${esc(d.summary||'Bounded search results.')}</p>${limits.map(l=>`<p>${esc(l)}</p>`).join('')}<ul>${(cov.sources||[]).map(s=>`<li>${esc(s.family.replaceAll('_',' '))}: ${esc(s.status)}</li>`).join('')}</ul><div class="feed-report-links">${artifacts.map(a=>`<a href="${url(a.url||a.path)}" target="_blank" rel="noopener">${esc(a.label||a.name)}</a>`).join('')}</div></div></details>`;
 }
 function focusFacet(key){
  if(!primaryKeys.includes(key))$('.feed-more-filters').open=true;
  $(`[data-facet="${key}"]`)?.focus({preventScroll:true});
 }
 function renderResults(keepLimit=false){
  if(!keepLimit)state.limit=12;
  const publicationView=state.basis==='publication' && /^\d{4}-/.test(state.date),d=state.date==='survey'?days.find(d=>d.collectionType==='survey'):publicationView?null:reports.find(d=>d.date===state.date),papers=currentPapers(),filtered=papers.filter(p=>M.matches(p,state.filters,state.query,state.event));
  $('#feed-date-title').textContent=state.date==='survey'?'Survey collection':state.date==='all'?'All papers':state.date==='daily'?'Daily discoveries':formatDate(state.date);
  $('#feed-date-note').textContent=publicationView?'Papers by original release date: arXiv first submission (UTC), or publication date. Month-only records appear in the whole-month view.':d?(d.feedNote||'Papers found in this search. Submission and revision dates are shown below.'):state.date==='all'?'The survey collection and daily discoveries, with duplicate papers combined.':'Papers found in daily searches. Choose a date to view one report.';
  $('#feed-event').parentElement.hidden=state.date==='survey';
  const filterEntries=Object.entries(state.filters),active=filterEntries.length+Number(!!state.query)+Number(state.event!=='all');
  $('#feed-result-count').textContent=`${filtered.length} ${filtered.length===1?'paper':'papers'}${active?` of ${papers.length}`:''}`;
  $('#feed-more-count').textContent=filterEntries.filter(([k])=>!primaryKeys.includes(k)).length||'';
  $('#feed-active').innerHTML=filterEntries.map(([k,v])=>`<button data-remove="${k}">${names[k]}: ${esc(label(v))} <span aria-hidden="true">×</span><span class="sr-only"> Remove filter</span></button>`).join('')+(active?'<button class="feed-reset" data-reset>Clear filters</button>':'');
  $$('[data-facet]').forEach(s=>s.value=state.filters[s.dataset.facet]||'');
  $$('[data-remove]').forEach(b=>b.addEventListener('click',()=>{delete state.filters[b.dataset.remove];renderResults();focusFacet(b.dataset.remove);}));
  const reset=()=>{state.filters={};state.query='';state.event='all';$('#feed-search').value='';$('#feed-event').value='all';renderResults();$('#feed-search').focus({preventScroll:true});};
  $('[data-reset]')?.addEventListener('click',reset);
  $('#feed-papers').innerHTML=filtered.length?filtered.slice(0,state.limit).map(card).join(''):`<div class="feed-empty"><span aria-hidden="true">⌕</span><h4>${active?'No matching papers':publicationView?'No papers in this period yet':'No verified papers in this search'}</h4><p>${active?'Try a different combination or browse another date.':publicationView?'Choose an earlier month or browse all papers.':'See the search report for checked sources and pending candidates.'}</p>${active?'<button id="feed-empty-reset">Clear filters</button>':''}</div>`;
  $('#feed-empty-reset')?.addEventListener('click',reset);
  $$('[data-chip-key]').forEach(b=>b.addEventListener('click',()=>{state.filters[b.dataset.chipKey]=b.dataset.chipValue;renderResults();focusFacet(b.dataset.chipKey);}));
  const shown=Math.min(state.limit,filtered.length);
  $('#feed-pagination').innerHTML=shown<filtered.length?`<span>Showing ${shown} of ${filtered.length}</span><button id="feed-load-more">Show more papers</button>`:'';
  $('#feed-load-more')?.addEventListener('click',()=>{const next=state.limit;state.limit+=12;renderResults(true);$(`#feed-paper-${next}`)?.focus({preventScroll:true});});
  renderRun(d);
 }
 if(!days.length){$('#feed-date-title').textContent='No papers yet';return;}
 window.FeedContribute.init({days,getDate:()=>state.date,getPapers:currentPapers});
 renderCalendar();renderResults();
})();
