"""Parse official Atom metadata; preserve dates without inventing version history."""
from datetime import datetime
import re
import xml.etree.ElementTree as ET

NS={'a':'http://www.w3.org/2005/Atom','o':'http://a9.com/-/spec/opensearch/1.1/'}


def normalize_id(value):
    if not re.fullmatch(r'\d{4}\.\d{4,5}(?:v[1-9]\d*)?',value):raise ValueError('Expected a modern arXiv ID, optionally versioned')
    return value


def parse_atom(content,requested):
    feed=ET.fromstring(content)
    if feed.tag!='{'+NS['a']+'}feed':raise ValueError('Expected an Atom feed from arXiv')
    records=[]
    for entry in feed.findall('a:entry',NS):
        value=lambda key:' '.join((entry.findtext('a:'+key,default='',namespaces=NS)).split())
        url=value('id');match=re.search(r'arxiv\.org/abs/(\d{4}\.\d{4,5})(v[1-9]\d*)?$',url)
        if not match:raise ValueError('arXiv returned a non-paper/error entry: '+value('title'))
        published,updated=value('published'),value('updated')
        for timestamp in (published,updated):
            parsed=datetime.fromisoformat(timestamp.replace('Z','+00:00'))
            if parsed.tzinfo is None:raise ValueError('Source timestamp lacks timezone')
        links=[dict(link.attrib) for link in entry.findall('a:link',NS)]
        records.append({'arxiv':match.group(1),'version':match.group(2),'canonical_url':'https://arxiv.org/abs/'+match.group(1),
                        'source_entry_url':url,'title':value('title'),'abstract':value('summary'),
                        'authors':[author.findtext('a:name',default='',namespaces=NS) for author in entry.findall('a:author',NS)],
                        'published':published,'updated':updated,
                        'categories':[category.attrib.get('term') for category in entry.findall('a:category',NS)],'links':links})
    found={record['arxiv'] for record in records}
    missing=[value for value in requested if re.sub(r'v\d+$','',value) not in found]
    requested_base={re.sub(r'v\d+$','',value) for value in requested}
    unexpected=sorted(found-requested_base)
    mismatches=[]
    for value in requested:
        match=re.search(r'v\d+$',value)
        if match:
            versions={record['version'] for record in records if record['arxiv']==value[:match.start()]}
            if versions and match.group(0) not in versions:mismatches.append({'requested':value,'returned_versions':sorted(v or '' for v in versions)})
    return {'records':records,'missing_ids':missing,'unexpected_ids':unexpected,'version_mismatches':mismatches,
            'requested_identities_complete':not missing and not unexpected and not mismatches,
            'warning':'published describes initial submission; updated describes the returned latest/requested version. Intermediate revisions are not supplied. Verify canonical version history when a target-day update or cutoff-sensitive PDF version depends on it.'}
