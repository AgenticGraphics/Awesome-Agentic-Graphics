"""Behavioral checks for exact-day evidence, taxonomy, identity and persisted reporting."""
import argparse,copy,contextlib,io,json,tempfile,unittest
from pathlib import Path
from datetime import datetime
from zoneinfo import ZoneInfo
import daily_report as D
class DailyTests(unittest.TestCase):
 def setUp(self):
  self.cb=D.read(D.ROOT/'references/taxonomy-codebook.json')
  self.run={'target_date':'2026-10-11','timezone':'America/Chicago','as_of':'2026-10-11T22:00:00-05:00','taxonomy_version':self.cb['version'],'source_snapshot':self.cb['source'],'source_ledger':[{'family':s,'status':'blocked','checks':[],'limitations':'Offline synthetic test'}for s in D.SOURCES],'query_coverage':[{'family':q['id'],'status':'not_reached_within_budget','checks':[]}for q in D.read(D.ROOT/'references/search-query-families.json')['families']],'coverage_limits':['Synthetic offline fixture; no live discovery claim.'],'papers':[]}
  self.paper={'canonical_title':'Synthetic test only','authors':[],'identifiers':{'arxiv':'9999.12345'},'canonical_urls':['https://example.org/synthetic-test'],'abstract':'Synthetic fixture','events':[self.event()],'source_records':[{'url':'https://example.org/synthetic-test'}],'screening_status':'core','screening_reason':'Synthetic test evidence','screening_evidence':[{'evidence':'Synthetic test'}],'application_families':['Static / Object'],'operations':['Generation'],'taxonomy_cells':{k:['Not Reported']for k in self.cb['fields']},'field_evidence':{},'contribution':'Synthetic test','limitations':'Not a real paper','taxonomy_delta':[],'confidence':'Low'}
 def event(self,**kw):
  e={'type':'first_submission','value':'2026-10-11T15:00:00Z','precision':'timestamp','timezone':'UTC','primary_url':'https://example.org/synthetic-test','authority':'primary','evidence':'Synthetic test event'};e.update(kw);return e
 def test_utc_boundary(self):
  self.assertEqual(D.event_day(self.event(value='2026-10-11T03:00:00Z'),ZoneInfo('America/Chicago'),D.aware(self.run['as_of'])),'2026-10-10')
 def test_dst_boundary(self):
  self.assertEqual(D.event_day(self.event(value='2026-11-01T06:30:00Z'),ZoneInfo('America/Chicago'),D.aware('2026-11-02T00:00:00Z')),'2026-11-01')
 def test_date_only_unknown_zone_not_qualified(self):
  self.assertIsNone(D.event_day(self.event(value='2026-10-11',precision='date',timezone=None),ZoneInfo('America/Chicago'),D.aware(self.run['as_of'])))
 def test_future_event_not_qualified(self):
  self.assertIsNone(D.event_day(self.event(value='2026-10-12T04:00:00Z'),ZoneInfo('America/Chicago'),D.aware(self.run['as_of'])))
 def test_secondary_date_not_qualified(self):
  self.assertIsNone(D.event_day(self.event(authority='secondary'),ZoneInfo('America/Chicago'),D.aware(self.run['as_of'])))
 def test_missing_offset_rejected(self):
  with self.assertRaises(ValueError):D.event_day(self.event(value='2026-10-11T12:00:00'),ZoneInfo('America/Chicago'),D.aware(self.run['as_of']))
 def test_revision_not_new(self):
  self.paper['events']=[self.event(type='revision')];self.assertEqual(D.bucket(self.paper,self.run),'same_day_updates')
 def test_artifact_not_paper(self):
  self.paper['events']=[self.event(type='artifact_release')];self.assertEqual(D.bucket(self.paper,self.run),'date_unresolved')
 def test_old_is_late_discovery(self):
  self.paper['events']=[self.event(value='2026-10-09T15:00:00Z')];self.assertEqual(D.bucket(self.paper,self.run),'late_discovery')
 def test_invalid_taxonomy_label_rejected(self):
  self.paper['taxonomy_cells']['planning']=['made-up'];self.run['papers']=[self.paper];self.assertTrue(any('invalid labels' in x for x in D.validate(self.run,self.cb)))
 def test_concrete_cell_without_evidence_rejected(self):
  self.paper['taxonomy_cells']['planning']=['PO-2'];self.run['papers']=[self.paper];self.assertTrue(any('evidence missing' in x for x in D.validate(self.run,self.cb)))
 def test_sentinel_mixture_rejected(self):
  self.paper['taxonomy_cells']['planning']=['PO-2','Unclear'];self.run['papers']=[self.paper];self.assertTrue(any('sentinel mixed' in x for x in D.validate(self.run,self.cb)))
 def test_duplicate_arxiv_versions_rejected(self):
  other=copy.deepcopy(self.paper);other['canonical_title']='Another title';other['identifiers']['arxiv']='9999.12345v2';self.run['papers']=[self.paper,other];self.assertTrue(any('duplicate identity' in x for x in D.validate(self.run,self.cb)))
 def test_missing_source_family_rejected(self):
  self.run['source_ledger'].pop();self.assertTrue(any('five source' in x for x in D.validate(self.run,self.cb)))
 def test_known_does_not_mean_accepted(self):
  r=D.read(D.ROOT/'references/paper-corpus.json')['records'][0];self.paper['canonical_title']=r['title'];self.assertEqual(D.corpus_status(self.paper,D.read(D.ROOT/'references/paper-corpus.json')),'known_discussed_paper')
 def test_invalid_ledger_timestamp_rejected(self):
  self.run['source_ledger'][0]['checks']=[{'query_or_url':'https://example.org','outcome':'Offline test','checked_at':'unknown'}]
  self.assertTrue(any('offset-aware' in x for x in D.validate(self.run,self.cb)))
 def test_recorded_only_ledger_timestamp(self):
  check={'query_or_url':'https://example.org','outcome':'Offline test','checked_at':None,'time_basis':'recorded_only','recorded_at':'2026-10-11T12:00:00-05:00'}
  self.run['source_ledger'][0]['checks']=[check]
  self.assertFalse(D.validate(self.run,self.cb))
  check['recorded_at']='2026-10-11T12:00:00'
  self.assertTrue(D.validate(self.run,self.cb))
 def test_invalid_query_timestamp_rejected(self):
  self.run['query_coverage'][0]['checks']=[{'query_or_url':'offline test','outcome':'fixture','checked_at':'tomorrow'}]
  self.assertTrue(any('offset-aware' in x for x in D.validate(self.run,self.cb)))
 def test_equivalent_event_time_identity(self):
  first=self.event(value="2026-10-11T15:00:00Z")
  second=self.event(value="2026-10-11T10:00:00-05:00")
  self.assertEqual(D.event_key(self.paper,first),D.event_key(self.paper,second))
 def test_render_and_prior_event_idempotency(self):
  self.run['papers']=[self.paper]
  with tempfile.TemporaryDirectory() as td:
   root=Path(td);inp=root/'input.json';D.write(inp,self.run)
   args=argparse.Namespace(input=inp,output_dir=root/'first',history_dir=None)
   with contextlib.redirect_stdout(io.StringIO()):self.assertEqual(D.finalize(args),0)
   first=D.read(root/'first/run.json');self.assertEqual(first['papers'][0]['report_bucket'],'same_day_new')
   text=(root/'first/report.md').read_text();self.assertIn('| Taxonomy field | Values | Evidence |\n|---|---|---|',text)
   args.output_dir=root/'second';args.history_dir=root
   with contextlib.redirect_stdout(io.StringIO()):self.assertEqual(D.finalize(args),0)
   self.assertEqual(D.read(root/'second/run.json')['papers'][0]['report_bucket'],'already_reported')
if __name__=='__main__':unittest.main()
