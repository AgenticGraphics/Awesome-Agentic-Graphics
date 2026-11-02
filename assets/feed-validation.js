/* The same data checks run in the browser and on pull requests. */
(function (root) {
  'use strict';
  const fields = ['task','input_form','output','model_type','model_training','planning','workflow','update_strategy','verifier','feedback_assessment','feedback_observation','memory_time','memory_reach','action_type','graphics_software','tools','resources','representation'];
  function validate(data, labels) {
    const fail = message => {throw new Error(message);};
    const text = value => typeof value === 'string' && value.trim().length > 0;
    const strings = value => Array.isArray(value) && value.every(text);
    const https = value => {try {const u=new URL(value);return ['https:','http:'].includes(u.protocol)&&!u.username&&!u.password;}catch{return false;}};
    const dateOK = value => typeof value==='string' && /^\d{4}-\d{2}-\d{2}$/.test(value) && !Number.isNaN(Date.parse(value)) && new Date(value).toISOString().slice(0,10)===value;
    if(!data || !Array.isArray(data.dates))fail('Feed must contain a dates array.');
    const dates=new Set();
    for(const day of data.dates){
      if(!dateOK(day.date)||dates.has(day.date))fail('Invalid or duplicate report date.');
      dates.add(day.date);
      if(!Array.isArray(day.papers))fail(`${day.date}: papers must be an array.`);
      const ids=new Set();
      for(const paper of day.papers){
        const at=`${day.date} / ${paper.id || 'missing ID'}`;
        for(const key of ['id','title','summary','scope'])if(!text(paper[key]))fail(`${at}: missing ${key}.`);
        if(ids.has(paper.id))fail(`${at}: duplicate paper within one report.`);ids.add(paper.id);
        if(!https(paper.url))fail(`${at}: invalid paper URL.`);
        if(!['core','scope_dependent','enabling_or_adjacent','excluded','unresolved'].includes(paper.scope))fail(`${at}: invalid scope.`);
        if(!['first_submission','revision'].includes(paper.eventType))fail(`${at}: invalid event type.`);
        if(!text(paper.eventDate)||Number.isNaN(Date.parse(paper.eventDate)))fail(`${at}: invalid event date.`);
        if(paper.publication!==undefined){
          const p=paper.publication;
          if(!p || !['day','month'].includes(p.precision) || !https(p.source))fail(`${at}: invalid publication provenance.`);
          if(p.precision==='day'?!dateOK(p.date):!/^\d{4}-\d{2}$/.test(p.date)||!dateOK(p.date+'-01'))fail(`${at}: invalid publication date.`);
          if(!['arxiv_first_submission','publication','first_submission'].includes(p.basis))fail(`${at}: invalid publication date basis.`);
          if(p.timestamp && (Number.isNaN(Date.parse(p.timestamp)) || !/(Z|\+00:00)$/.test(p.timestamp) || p.timestamp.slice(0,10)!==p.date))fail(`${at}: inconsistent publication timestamp.`);
        }
        for(const key of ['applications','operations','authors','tags'])if(paper[key]!==undefined&&!strings(paper[key]))fail(`${at}: ${key} must be a string array.`);
        if(!paper.taxonomy || typeof paper.taxonomy!=='object')fail(`${at}: missing taxonomy.`);
        for(const key of Object.keys(paper.taxonomy))if(!fields.includes(key))fail(`${at}: unknown taxonomy field ${key}.`);
        for(const key of fields){
          const values=paper.taxonomy[key];
          if(!strings(values)||values.length===0||new Set(values).size!==values.length)fail(`${at}: invalid ${key} labels.`);
          if(labels&&values.some(v=>![...labels.fields[key],...labels.sentinels].includes(v)))fail(`${at}: unknown ${key} label.`);
          if(values.length>1&&values.some(v=>['Not Reported','Not Applicable','Unclear'].includes(v)))fail(`${at}: do not mix unknown and concrete labels.`);
        }
        if(labels){
          if((paper.applications||[paper.application]).some(v=>!labels.application_families.includes(v)))fail(`${at}: invalid application.`);
          if((paper.operations||[]).some(v=>!labels.operations.includes(v)))fail(`${at}: invalid operation.`);
        }
        for(const [field,evidence] of Object.entries(paper.taxonomyEvidence||{})){
          if(!fields.includes(field)||!evidence||!https(evidence.primary_url)||!text(evidence.evidence)||!text(evidence.locator))fail(`${at}: invalid evidence for ${field}.`);
        }
      }
    }
    return true;
  }
  root.FeedValidation={validate};
  if(typeof module!=='undefined')module.exports=root.FeedValidation;
})(typeof window==='undefined'?globalThis:window);
