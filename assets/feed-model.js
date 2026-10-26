/* Shared feed logic; also exercised by the offline checks. */
(function (root) {
 'use strict';
 const sentinels = new Set(['Not Reported', 'Not Applicable', 'Unclear']);
 const kind = p => {
  const bucket = (p.bucket || '').toLowerCase();
  if (/late|catch/.test(bucket)) return 'catchup';
  if (/unresolved|pending/.test(bucket)) return 'pending';
  if (/update|revision/.test(bucket) || (!bucket && p.eventType === 'revision')) return 'update';
  return 'new';
 };
 const values = (p, key) => key === 'application' ? (p.applications || [p.application].filter(Boolean)) : key === 'scope' ? [p.scope] : key === 'operations' ? (p.operations || []) : (p.taxonomy?.[key] || ['Not Reported']);
 const identity = p => p.id || p.url || p.title;
 const collect = (days, date) => {
  const reports = date === 'all' ? days : days.filter(d => d.date === date);
  const unique = new Map();
  reports.slice().sort((a,b) => a.date.localeCompare(b.date)).forEach(d => (d.papers || []).forEach(p => {
   unique.set(identity(p), {...p, reportDate:d.date});
  }));
  return [...unique.values()].filter(p=>!['excluded','unresolved'].includes(p.scope)).sort((a,b) => (b.eventDate || '').localeCompare(a.eventDate || '') || a.title.localeCompare(b.title));
 };
 const matches = (p, filters, query, event) => {
  const haystack = [p.title,p.summary,p.abstract,p.application,...(p.authors || []),...(p.tags || []),...Object.values(p.taxonomy || {}).flat()].join(' ').toLowerCase();
  return (event === 'all' || kind(p) === event) && haystack.includes(query.trim().toLowerCase()) && Object.entries(filters).every(([key,value]) => !value || values(p,key).includes(value));
 };
 root.FeedModel = {sentinels,kind,values,identity,collect,matches};
})(typeof window === 'undefined' ? globalThis : window);
