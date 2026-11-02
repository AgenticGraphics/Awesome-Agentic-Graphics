from listing_scan import scan_listing


def page(skip,links):
    return {'text':str(skip),'links':[{'text':str(x+1)+'-'+str(x+100),'url':f'https://arxiv.org/list/cs.CV/recent?skip={x}&show=100'} for x in links]}


def test_scan_follows_observed_links_only_and_deduplicates():
    calls=[]
    pages={0:page(0,[100,200]),100:page(100,[0,200]),200:page(200,[0,100])}
    def fetch(url):
        from urllib.parse import urlparse,parse_qs
        n=int(parse_qs(urlparse(url).query)['skip'][0]);calls.append(n);return pages[n]
    result=scan_listing('cs.CV','recent',12,fetch,lambda text:[{'arxiv':'synthetic-shared','title':'duplicate'},{'arxiv':'synthetic-'+text,'title':'entry'}])
    assert calls==[0,100,200]
    assert len(result['entries'])==4
    assert result['complete_observed_pagination']


def test_page_budget_preserves_unvisited_links():
    result=scan_listing('cs.CV','recent',1,lambda url:page(0,[100]),lambda text:[])
    assert not result['complete_observed_pagination']
    assert len(result['unvisited_observed_urls'])==1


def test_fetch_error_does_not_become_empty_success():
    def fail(url):raise TimeoutError('synthetic network timeout')
    result=scan_listing('cs.CV','recent',3,fail,lambda text:[])
    assert result['errors'] and not result['complete_observed_pagination']


def test_atomic_all_page_replaces_old_navigation_entries():
    first={'text':'Total of 2 entries','links':[{'text':'all','url':'https://arxiv.org/list/cs.CV/recent?skip=0&show=2000'}]}
    full={'text':'Total of 3 entries','links':[]}
    def parse(text):return [{'arxiv':str(i),'title':str(i)} for i in range(int(text.split()[2]))]
    result=scan_listing('cs.CV','recent',2,lambda url:full if 'show=2000' in url else first,parse)
    assert len(result['entries'])==3 and result['reported_total_entries']==3
    assert result['consistent_listing_snapshot'] and result['data_source_url'].endswith('show=2000')


def test_mixed_pagination_totals_are_not_reported_as_complete():
    first=page(0,[100]);first['text']='Total of 200 entries'
    second=page(100,[]);second['text']='Total of 220 entries'
    result=scan_listing('cs.CV','recent',2,lambda url:second if 'skip=100' in url else first,lambda text:[])
    assert not result['consistent_listing_snapshot']
    assert not result['complete_observed_pagination']


def test_failed_all_page_still_consumes_request_budget():
    first=page(0,[100]);first['links'].append({'text':'all','url':'https://arxiv.org/list/cs.CV/recent?skip=0&show=2000'})
    calls=[]
    def fetch(url):calls.append(url);return first if 'show=100' in url else {'text':'incomplete','links':[]}
    result=scan_listing('cs.CV','recent',2,fetch,lambda text:[])
    assert len(calls)==2 and result['requests_attempted']==2
    assert result['unvisited_observed_urls'] and not result['complete_observed_pagination']


def test_parser_failure_cannot_look_like_an_empty_complete_listing():
    result=scan_listing('cs.GR','recent',1,lambda url:{'text':'Total of 12 entries','links':[]},lambda text:[])
    assert not result['complete_observed_pagination']
    assert result['errors'][0]['parsed_entries']==0


def test_all_link_cannot_silently_replace_new_papers_with_only_replacements():
    first={'text':'Total of 1 entries new','links':[{'text':'all','url':'https://arxiv.org/list/cs.CV/new?skip=0&show=2000'}]}
    full={'text':'Total of 1 entries replaced','links':[]}
    parse=lambda text:[{'arxiv':'new-id' if text.endswith('new') else 'old-id','title':'fixture'}]
    result=scan_listing('cs.CV','new',2,lambda url:full if '2000' in url else first,parse)
    assert [x['arxiv'] for x in result['entries']]==['new-id']
    assert result['warnings'][0]['contains_first_page'] is False
    assert 'data_source_url' not in result
