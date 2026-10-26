'use strict';
const data = window.SURVEY_DATA;
const $ = (s, root=document) => root.querySelector(s);
const $$ = (s, root=document) => [...root.querySelectorAll(s)];
const escapeHTML = value => String(value ?? '').replace(/[&<>"']/g, char => ({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[char]));
const safeURL = url => /^(https?:\/\/|data\/|assets\/)/.test(url || '') ? url : '#';
const affiliations = [...new Set(data.authors.map(a=>a.affiliation))];
$('#hero-authors').innerHTML = data.authors.map(a=>`<a href="${escapeHTML(safeURL(a.url))}" target="_blank" rel="noopener" title="${escapeHTML(a.affiliation)}${a.equal_contribution?' · Equal contribution':''}"${a.equal_contribution?' aria-describedby="equal-contribution"':''}>${escapeHTML(a.name)}<sup>${affiliations.indexOf(a.affiliation)+1}${a.equal_contribution?',*':''}</sup></a>`).join('');
$('#affiliations').innerHTML = affiliations.map((a,i)=>`<span><sup>${i+1}</sup>${escapeHTML(a)}</span>`).join('');
$('#abstract-text').textContent = data.abstract;

let currentTax = 0, pendingTax = null;
const taxTrack = $('#taxonomy-panel');
const reducedMotion = window.matchMedia('(prefers-reduced-motion: reduce)');
$('#taxonomy-tabs').innerHTML=data.taxonomy.map((t,i)=>`<button class="tax-tab" role="tab" id="tax-${t.id}" aria-selected="${i===0}" aria-controls="panel-${t.id}" tabindex="${i===0?0:-1}" data-tax="${i}"><span>0${i+1}</span><span><strong>${escapeHTML(t.title)}</strong><small>${escapeHTML(t.kicker)}</small></span></button>`).join('');
taxTrack.innerHTML=data.taxonomy.map((item,index)=>`<div class="taxonomy-panel tax-slide" data-dimension="${item.id}" id="panel-${item.id}" role="tabpanel" aria-labelledby="tax-${item.id}"><div class="panel-title"><h3>${escapeHTML(item.title)}</h3><span class="panel-number">0${index+1}</span></div><p class="panel-description">${escapeHTML(item.description)}</p>${item.fields.map(f=>`<div class="tax-row"><div class="tax-field">${escapeHTML(f.name)}</div><div class="tax-options">${f.options.map(o=>`<span class="tax-chip">${escapeHTML(o)}</span>`).join('')}</div></div>`).join('')}<p class="tax-caption">Based on Section 3 of the survey manuscript.</p></div>`).join('');
const taxSlides=$$('.tax-slide');
function updateTax(index){
 currentTax=index;
 $$('[data-tax]').forEach((button,i)=>{button.setAttribute('aria-selected',String(i===index));button.tabIndex=i===index?0:-1;});
 taxSlides.forEach((slide,i)=>{slide.inert=i!==index;slide.setAttribute('aria-hidden',String(i!==index));});
 taxTrack.style.height=taxSlides[index].offsetHeight+'px';
 $('#tax-progress').textContent=`0${index+1} / 0${taxSlides.length}`;
 $('#tax-prev').disabled=index===0;
 $('#tax-next').disabled=index===taxSlides.length-1;
}
function renderTax(index, behavior=reducedMotion.matches?'auto':'smooth'){
 pendingTax=index;
 updateTax(index);
 taxTrack.scrollTo({left:taxSlides[index].offsetLeft,behavior});
}
$$('[data-tax]').forEach(button=>button.addEventListener('click',()=>renderTax(Number(button.dataset.tax))));
$('#tax-prev').addEventListener('click',()=>renderTax(Math.max(0,currentTax-1)));
$('#tax-next').addEventListener('click',()=>renderTax(Math.min(taxSlides.length-1,currentTax+1)));
function taxKeyboard(e){
 let index=currentTax;
 if(e.key==='ArrowRight'||e.key==='ArrowDown')index=(index+1)%taxSlides.length;
 else if(e.key==='ArrowLeft'||e.key==='ArrowUp')index=(index+taxSlides.length-1)%taxSlides.length;
 else if(e.key==='Home')index=0;
 else if(e.key==='End')index=taxSlides.length-1;
 else return;
 e.preventDefault();renderTax(index);
 if(e.currentTarget.id==='taxonomy-tabs')$(`[data-tax="${index}"]`).focus({preventScroll:true});
}
$('#taxonomy-tabs').addEventListener('keydown',taxKeyboard);
taxTrack.addEventListener('keydown',taxKeyboard);
let taxScrollTimer;
function settleTaxScroll(){
 clearTimeout(taxScrollTimer);
 if(pendingTax!==null&&Math.abs(taxSlides[pendingTax].offsetLeft-taxTrack.scrollLeft)>2)return;
 pendingTax=null;
 const nearest=taxSlides.reduce((best,slide,i)=>Math.abs(slide.offsetLeft-taxTrack.scrollLeft)<Math.abs(taxSlides[best].offsetLeft-taxTrack.scrollLeft)?i:best,0);
 if(nearest!==currentTax)updateTax(nearest);
}
taxTrack.addEventListener('scroll',()=>{
 clearTimeout(taxScrollTimer);
 taxScrollTimer=setTimeout(settleTaxScroll,140);
},{passive:true});
taxTrack.addEventListener('scrollend',settleTaxScroll);
['wheel','pointerdown','touchstart'].forEach(event=>taxTrack.addEventListener(event,()=>{pendingTax=null;},{passive:true}));
let taxWidth=0;
new ResizeObserver(()=>{
 const width=taxTrack.clientWidth;
 if(width!==taxWidth){taxWidth=width;renderTax(currentTax,'auto');}
 else taxTrack.style.height=taxSlides[currentTax].offsetHeight+'px';
}).observe(taxTrack);
const taxSizeObserver=new ResizeObserver(()=>{taxTrack.style.height=taxSlides[currentTax].offsetHeight+'px';});
taxSlides.forEach(slide=>taxSizeObserver.observe(slide));
renderTax(0,'auto');
$$('[data-tax-target]').forEach(button=>button.addEventListener('click',()=>{
 renderTax(Number(button.dataset.taxTarget));
 $('#taxonomy').scrollIntoView({behavior:window.matchMedia('(prefers-reduced-motion: reduce)').matches?'auto':'smooth',block:'start'});
 $('#taxonomy-panel').focus({preventScroll:true});
}));
const navigationSections=['overview','taxonomy','applications','discovery'];
let navigationFrame;
function updateActiveNavigation(){
 const boundary=$('header').offsetHeight+100;
 let active='overview';
 for(const id of navigationSections){if(document.getElementById(id).getBoundingClientRect().top<=boundary)active=id;}
 $$('nav a').forEach(link=>{
  const selected=link.getAttribute('href')==='#'+active;
  link.classList.toggle('active',selected);
  if(selected)link.setAttribute('aria-current','location');else link.removeAttribute('aria-current');
 });
}
function scheduleNavigation(){cancelAnimationFrame(navigationFrame);navigationFrame=requestAnimationFrame(updateActiveNavigation);}
window.addEventListener('scroll',scheduleNavigation,{passive:true});
window.addEventListener('resize',scheduleNavigation);
new ResizeObserver(scheduleNavigation).observe($('#main'));
scheduleNavigation();

// Application categories follow the current local manuscript's application sections.
const applicationGroups=[
 {id:'2d',title:'2D graphics',kicker:'Create & edit visual communication',dimension:'specification',description:'Editable visual artifacts, from individual shapes to complete documents and slide decks.',points:[
 ['SVG & vector graphics','Scalable shapes, paths, semantic groups, and code-driven motion.'],
 ['Visual design & editing','Collaborative sketching, graphic editing, and layout composition.'],
 ['Scientific figures & diagrams','Technical illustrations, relationship diagrams, and editable figure reconstruction.'],
 ['Data visualization & plots','Data-grounded charts and plots generated through executable code.'],
 ['Documents & presentations','Posters, banners, and slide decks with coherent layouts and styles.']],image:'assets/graphics-2d.png',caption:'SketchAgent: text-conditioned sketching, human–agent collaboration, and sketch editing.'},
 {id:'static',title:'Static 3D graphics',kicker:'Build objects, CAD & scenes',dimension:'base-model',description:'Construct and refine editable 3D geometry, surface appearance, and spatial arrangements.',points:[
 ['Object modeling','Geometry construction, texture and material modeling, and localized asset editing.'],
 ['CAD modeling','Specification-driven generation, reference-based reconstruction, and parametric model editing.'],
 ['Scene modeling','Scene generation, reconstruction, and editing with spatial relationships and constraints.']],image:'assets/graphics-3d.png',caption:'ViSculpt: localized 3D asset edits through sculpting operations and visual feedback.'},
 {id:'dynamic',title:'Dynamic 3D graphics',kicker:'Articulate, animate & simulate',dimension:'tooling',description:'Editable descriptions of how objects and scenes move, deform, and interact.',points:[
 ['Articulation','Part geometry, joints, motion limits, and functional mechanisms.'],
 ['Animation','Character and camera motion, joint trajectories, and evolving visual effects.'],
 ['Simulation','Physical responses, deformable assets, and interaction-based diagnosis and repair.']],image:'assets/graphics-dynamic.png',caption:'Articraft and Artisan: articulated asset programs, part structure, and physical validation.'}
];
const taskVisuals={
 '2d':[
  {image:'assets/task-vector-paper.png',type:'Paper figure · IntroSVG',caption:'IntroSVG (CVPR 2026), Figure 4: successive iterations refine generated SVG icons using rendering feedback.',source:'https://openaccess.thecvf.com/content/CVPR2026/papers/Wang_IntroSVG_Learning_from_Rendering_Feedback_for_Text-to-SVG_Generation_via_an_CVPR_2026_paper.pdf#page=8',figure:4},
  {image:'assets/graphics-2d.png',type:'Survey figure · SketchAgent',caption:'SketchAgent: sequential sketch generation, human–agent collaboration, and text-guided editing.'},
  {image:'assets/task-scientific.png',type:'Survey figure · PaperBanana',caption:'PaperBanana: methodology diagrams and scientific illustrations, with examples of statistical plots.'},
  {image:'assets/task-plots-paper.png',type:'Paper figure · MatPlotAgent',caption:'MatPlotAgent (Findings of ACL 2024), Figure 4: charts without visual feedback, with visual feedback, and their reference plots.',source:'https://aclanthology.org/2024.findings-acl.701.pdf#page=8',figure:4},
  {image:'assets/task-documents-paper.png',type:'Paper figure · AutoPresent',caption:'AutoPresent (CVPR 2025), Figure 1: natural-language instructions are translated into slide-generation code with control over text, images, and layout.',source:'https://openaccess.thecvf.com/content/CVPR2025/papers/Ge_AutoPresent_Designing_Structured_Visuals_from_Scratch_CVPR_2025_paper.pdf#page=1',figure:1}
 ],
 'static':[
  {image:'assets/task-object.png',type:'Survey figure · LL3M',caption:'LL3M: visual critique guides successive repairs of a generated hydrant until the cap is correctly attached.'},
  {image:'assets/task-cad.png',type:'Survey figure · CADCodeVerify / Seek-CAD',caption:'CADCodeVerify and Seek-CAD: design requirements and intermediate geometry guide CAD program refinement.'},
  {image:'assets/task-scene.png',type:'Survey figure · SceneSmith',caption:'SceneSmith: hierarchical construction of layouts, furniture, wall and ceiling elements, and smaller objects.'}
 ],
 'dynamic':[
  {image:'assets/graphics-dynamic.png',type:'Survey figure · Articraft / Artisan',caption:'Articraft and Artisan: articulated parts and joints, with geometric and physical validation.'},
  {image:'assets/task-animation.png',type:'Survey figure · ArtiMo',caption:'ArtiMo: text-guided motion editing for articulated objects, from basket handles to appliance doors.'},
  {image:'assets/task-simulation.png',type:'Survey figure · DiagGen',caption:'DiagGen: construct a deformable asset, diagnose its behavior, and route repairs to geometry or physical properties.'}
 ]
};
const applicationTrack=$('#application-track');
const applicationTabs=$('#application-tabs');
applicationTabs.innerHTML=applicationGroups.map((g,i)=>`<button class="tax-tab" role="tab" id="application-tab-${g.id}" aria-controls="application-${g.id}" aria-selected="${i===0}" tabindex="${i===0?0:-1}"><span>0${i+1}</span><span><strong>${g.title}</strong><small>${g.kicker}</small></span></button>`).join('');
applicationTrack.innerHTML=applicationGroups.map((g,i)=>{
 const visual=taskVisuals[g.id][0];
 return `<article class="taxonomy-panel application-slide" id="application-${g.id}" data-dimension="${g.dimension}" role="tabpanel" aria-labelledby="application-tab-${g.id}"><div class="panel-title"><h3>${g.title}</h3><span class="panel-number">0${i+1}</span></div><p class="panel-description">${g.description}</p><div class="application-body"><ul class="application-points" role="tablist" aria-label="${g.title} tasks" aria-orientation="vertical">${g.points.map(([title,description],j)=>`<li role="presentation"><button class="application-task" role="tab" id="task-${g.id}-${j}" aria-controls="visual-${g.id}" aria-selected="${j===0}" tabindex="${j===0?0:-1}" data-task-group="${g.id}" data-task-index="${j}"><span class="task-label">${escapeHTML(title)}</span><span class="task-description">${escapeHTML(description)}</span></button></li>`).join('')}</ul><figure class="application-example" id="visual-${g.id}" role="tabpanel" aria-labelledby="task-${g.id}-0" tabindex="0"><div class="task-visual-heading"><span class="task-visual-type">${escapeHTML(visual.type)}</span><span class="task-visual-count">01 / 0${g.points.length}</span></div><button data-image="${visual.image}" data-caption="${escapeHTML(visual.caption)}" aria-label="Enlarge ${escapeHTML(g.points[0][0])} visualization"><img src="${visual.image}" alt="${escapeHTML(visual.caption)}" decoding="async"><span>View full size</span></button><figcaption>${escapeHTML(visual.caption)}</figcaption><a class="task-source" href="${escapeHTML(safeURL(visual.source))}" target="_blank" rel="noopener"${visual.source?'':' hidden'}>Source paper · Figure ${visual.figure||''}</a></figure></div></article>`;
}).join('');
function selectTask(group,index,scrollToVisual=false){
 const g=applicationGroups.find(item=>item.id===group),visual=taskVisuals[group][index];
 $$(`[data-task-group="${group}"]`).forEach((button,i)=>{button.setAttribute('aria-selected',String(i===index));button.tabIndex=i===index?0:-1;});
 const figure=$(`#visual-${group}`),button=$('[data-image]',figure),img=$('img',figure);
 figure.setAttribute('aria-labelledby',`task-${group}-${index}`);
 $('.task-visual-type',figure).textContent=visual.type;
 $('.task-visual-count',figure).textContent=`0${index+1} / 0${g.points.length}`;
 button.dataset.image=visual.image;button.dataset.caption=visual.caption;
 button.setAttribute('aria-label',`Enlarge ${g.points[index][0]} visualization`);
 img.src=visual.image;img.alt=visual.caption;$('figcaption',figure).textContent=visual.caption;
 const sourceLink=$('.task-source',figure);sourceLink.hidden=!visual.source;sourceLink.href=safeURL(visual.source);sourceLink.textContent=`Source paper · Figure ${visual.figure||''}`;
 if(window.matchMedia('(max-width:760px)').matches){
  $(`#task-${group}-${index}`).scrollIntoView({behavior:reducedMotion.matches?'auto':'smooth',block:'nearest',inline:'nearest'});
  if(scrollToVisual)figure.scrollIntoView({behavior:reducedMotion.matches?'auto':'smooth',block:'nearest'});
 }
}
const compactApplications=window.matchMedia('(max-width:760px)');
function updateTaskOrientation(){
 $$('.application-points').forEach(list=>list.setAttribute('aria-orientation',compactApplications.matches?'horizontal':'vertical'));
}
compactApplications.addEventListener('change',updateTaskOrientation);
updateTaskOrientation();
$$('.application-task').forEach(button=>button.addEventListener('click',()=>selectTask(button.dataset.taskGroup,Number(button.dataset.taskIndex),true)));
$$('.application-points').forEach(list=>list.addEventListener('keydown',e=>{
 const button=e.target.closest('.application-task');if(!button)return;
 const group=button.dataset.taskGroup,length=taskVisuals[group].length;let index=Number(button.dataset.taskIndex);
 if(e.key==='ArrowDown'||e.key==='ArrowRight')index=(index+1)%length;
 else if(e.key==='ArrowUp'||e.key==='ArrowLeft')index=(index+length-1)%length;
 else if(e.key==='Home')index=0;else if(e.key==='End')index=length-1;else return;
 e.preventDefault();e.stopPropagation();selectTask(group,index);$(`#task-${group}-${index}`).focus({preventScroll:true});
}));
const applicationSlides=$$('.application-slide');
const applicationButtons=$$('button',applicationTabs);
let currentApplication=0,applicationScrollTimer,applicationWidth=0,pendingApplication=null;
function updateApplication(index){
 currentApplication=index;
 applicationButtons.forEach((button,i)=>{button.setAttribute('aria-selected',String(i===index));button.tabIndex=i===index?0:-1;});
 applicationSlides.forEach((slide,i)=>{slide.inert=i!==index;slide.setAttribute('aria-hidden',String(i!==index));});
 applicationTrack.style.height=applicationSlides[index].offsetHeight+'px';
 $('#application-progress').textContent=`0${index+1} / 03`;
 $('#application-prev').disabled=index===0;
 $('#application-next').disabled=index===2;
}
function selectApplication(index,behavior=reducedMotion.matches?'auto':'smooth'){
 pendingApplication=index;
 updateApplication(index);applicationTrack.scrollTo({left:applicationSlides[index].offsetLeft,behavior});
}
applicationButtons.forEach((button,i)=>button.addEventListener('click',()=>selectApplication(i)));
$('#application-prev').addEventListener('click',()=>selectApplication(Math.max(0,currentApplication-1)));
$('#application-next').addEventListener('click',()=>selectApplication(Math.min(2,currentApplication+1)));
function applicationKeyboard(e){
 let index=currentApplication;
 if(e.key==='ArrowRight')index=(index+1)%3;else if(e.key==='ArrowLeft')index=(index+2)%3;else if(e.key==='Home')index=0;else if(e.key==='End')index=2;else return;
 e.preventDefault();selectApplication(index);
 if(e.currentTarget===applicationTabs)applicationButtons[index].focus({preventScroll:true});
}
applicationTabs.addEventListener('keydown',applicationKeyboard);
applicationTrack.addEventListener('keydown',applicationKeyboard);
function settleApplication(){
 clearTimeout(applicationScrollTimer);
 if(pendingApplication!==null&&Math.abs(applicationSlides[pendingApplication].offsetLeft-applicationTrack.scrollLeft)>2)return;
 pendingApplication=null;
 const index=applicationSlides.reduce((best,slide,i)=>Math.abs(slide.offsetLeft-applicationTrack.scrollLeft)<Math.abs(applicationSlides[best].offsetLeft-applicationTrack.scrollLeft)?i:best,0);
 if(index!==currentApplication)updateApplication(index);
}
applicationTrack.addEventListener('scroll',()=>{clearTimeout(applicationScrollTimer);applicationScrollTimer=setTimeout(settleApplication,140);},{passive:true});
applicationTrack.addEventListener('scrollend',settleApplication);
['wheel','pointerdown','touchstart'].forEach(event=>applicationTrack.addEventListener(event,()=>{pendingApplication=null;},{passive:true}));
new ResizeObserver(()=>{
 if(applicationWidth!==applicationTrack.clientWidth){applicationWidth=applicationTrack.clientWidth;selectApplication(currentApplication,'auto');}
}).observe(applicationTrack);
const applicationSizeObserver=new ResizeObserver(()=>{applicationTrack.style.height=applicationSlides[currentApplication].offsetHeight+'px';});
applicationSlides.forEach(slide=>applicationSizeObserver.observe(slide));
selectApplication(0,'auto');

(async function renderLiveCorpus(){
 await window.feedReady;
 const days=data.daily?.dates || [];
const dialog=$('#image-dialog');
$$('[data-image]').forEach(button=>button.addEventListener('click',()=>{$('#dialog-image').src=button.dataset.image;$('#dialog-image').alt=button.dataset.caption;$('#dialog-caption').textContent=button.dataset.caption;dialog.showModal();document.documentElement.classList.add('figure-open');}));
$('.dialog-close').addEventListener('click',()=>dialog.close());
dialog.addEventListener('click',e=>{if(e.target===dialog){const rect=dialog.getBoundingClientRect();if(e.clientX<rect.left||e.clientX>rect.right||e.clientY<rect.top||e.clientY>rect.bottom)dialog.close();}});

dialog.addEventListener('close',()=>document.documentElement.classList.remove('figure-open'));

// Keep the arXiv placeholder inert until its URL is supplied.
document.querySelectorAll('[data-pending-link]').forEach(link=>link.addEventListener('click',event=>event.preventDefault()));

// Corpus growth: the survey's monthly counts, extended live by new papers from the daily feed.
const growth=data.growth;
if(growth){
 const monthName=(key,style='short')=>new Date(key+'-15T12:00:00').toLocaleDateString('en-US',{month:style,year:'numeric'});
 const firstSeen={},latestScopes={};
 days.slice().sort((a,b)=>a.date.localeCompare(b.date)).forEach(d=>(d.papers||[]).forEach(p=>latestScopes[p.id]=p.scope));
 days.forEach(d=>(d.papers||[]).forEach(p=>{
  const date=(p.eventDate||'').slice(0,10);
  if(p.eventType==='first_submission'&&growth.liveScopes.includes(latestScopes[p.id])&&date>growth.cutoff&&!(p.id in firstSeen))firstSeen[p.id]=date;
 }));
 const points=growth.monthly.map(([month,count])=>({month,count}));
 const liveByMonth={};
 Object.values(firstSeen).forEach(date=>{const m=date.slice(0,7);liveByMonth[m]=(liveByMonth[m]||0)+1;});
 let total=points[points.length-1].count;
 Object.keys(liveByMonth).sort().forEach(month=>{total+=liveByMonth[month];points.push({month,count:total,live:true});});
 const events=Object.fromEntries(growth.events.map(e=>[e.month,e.label]));
 const liveCount=Object.keys(firstSeen).length;
 $('#growth-total').textContent=total;
 if(liveCount){$('#growth-live').hidden=false;$('#growth-live>span:last-child').textContent=`+${liveCount} from the daily feed since ${monthName(growth.cutoff.slice(0,7),'long').split(' ')[0]}`;}
 const chart=$('#growth-chart');
 const table=`<table class="growth-table"><caption>Cumulative papers by month</caption><tr><th>Month</th><th>Papers</th></tr>${points.map(p=>`<tr><td>${monthName(p.month)}</td><td>${p.count}</td></tr>`).join('')}</table>`;
 let chartWidth=0;
 const renderGrowth=()=>{
  const W=chart.clientWidth, H=W<560?230:290, m={top:14,right:14,bottom:30,left:38};
  const maxY=Math.ceil(total/100)*100, step=(W-m.left-m.right)/(points.length-1);
  const x=i=>m.left+i*step, y=v=>m.top+(H-m.top-m.bottom)*(1-v/maxY);
  const path=list=>list.map((p,i)=>`${i?'L':'M'}${x(p.i).toFixed(1)},${y(p.count).toFixed(1)}`).join('');
  const indexed=points.map((p,i)=>({...p,i})), corpus=indexed.filter(p=>!p.live), split=corpus.length-1;
  const grid=[];for(let v=0;v<=maxY;v+=100)grid.push(`<line x1="${m.left}" x2="${W-m.right}" y1="${y(v)}" y2="${y(v)}"/><text class="growth-axis" x="${m.left-8}" y="${y(v)}" text-anchor="end" dominant-baseline="middle">${v}</text>`);
  const ticks=[{i:0,label:monthName(points[0].month)}];
  points.forEach((p,i)=>{if(i&&p.month.endsWith('-01')&&x(points.length-1)-x(i)>60)ticks.push({i,label:p.month.slice(0,4)});});
  ticks.push({i:points.length-1,label:monthName(points[points.length-1].month),end:true});
  const marks=indexed.filter(p=>events[p.month]).map(p=>`<line class="growth-leader" x1="${x(p.i)-6}" x2="${x(p.i)-14}" y1="${y(p.count)}" y2="${y(p.count)}"/><text class="growth-event" x="${x(p.i)-18}" y="${y(p.count)}" text-anchor="end" dominant-baseline="middle">${escapeHTML(events[p.month])}</text><circle class="growth-marker" cx="${x(p.i)}" cy="${y(p.count)}" r="4.5"/>`).join('');
  const end=indexed[indexed.length-1];
  chart.innerHTML=`<svg width="${W}" height="${H}" role="img" aria-label="Cumulative papers grew from ${points[0].count} in ${monthName(points[0].month)} to ${total} in ${monthName(end.month)}."><g class="growth-grid">${grid.join('')}</g>${ticks.map(t=>`<text class="growth-axis" x="${x(t.i)}" y="${H-8}" text-anchor="${t.i===0?'start':t.end?'end':'middle'}">${t.label}</text>`).join('')}<path class="growth-area" d="${path(indexed)}L${x(end.i)},${y(0)}L${x(0)},${y(0)}Z"/><path class="growth-line" d="${path(corpus)}"/>${end.live?`<path class="growth-line live" d="${path(indexed.slice(split))}"/>`:''}${marks}<circle class="growth-end" cx="${x(end.i)}" cy="${y(end.count)}" r="4.5"/><line class="growth-cross" y1="${m.top}" y2="${y(0)}" visibility="hidden"/><circle class="growth-hover" r="4.5" visibility="hidden"/><rect class="growth-hit" x="${m.left-step/2}" y="0" width="${W-m.left-m.right+step}" height="${H}"/></svg><div class="growth-tip" hidden></div>${table}`;
  const svg=$('svg',chart), tip=$('.growth-tip',chart), cross=$('.growth-cross',chart), dot=$('.growth-hover',chart);
  const hide=()=>{tip.hidden=true;cross.setAttribute('visibility','hidden');dot.setAttribute('visibility','hidden');};
  svg.addEventListener('pointermove',e=>{
   const i=Math.max(0,Math.min(points.length-1,Math.round((e.clientX-svg.getBoundingClientRect().left-m.left)/step))), p=points[i];
   cross.setAttribute('x1',x(i));cross.setAttribute('x2',x(i));cross.setAttribute('visibility','visible');
   dot.setAttribute('cx',x(i));dot.setAttribute('cy',y(p.count));dot.setAttribute('visibility','visible');
   tip.innerHTML=`<strong>${p.count} papers</strong><span>${monthName(p.month)}${p.live?' · daily feed':''}</span>${events[p.month]?`<span>${escapeHTML(events[p.month])}</span>`:''}`;
   tip.hidden=false;
   tip.style.left=Math.max(tip.offsetWidth/2,Math.min(W-tip.offsetWidth/2,x(i)))+'px';tip.style.top=(y(p.count)-14)+'px';
  });
  svg.addEventListener('pointerleave',hide);
 };
 new ResizeObserver(()=>{if(chart.clientWidth!==chartWidth){chartWidth=chart.clientWidth;renderGrowth();}}).observe(chart);
}

})();
