"""Transparent high-recall title hints. No paper IDs, dates or scope labels are encoded."""
import re

# Derived from the maintained survey's graphics applications and agent mechanisms.
# A non-match is NOT exclusion evidence: agentic contributions can be inside a paper.
MECHANISM=re.compile(r'agent\w*|assist\w*|cod(?:e|ing)|program\w*|plan\w*|reason\w*|tool\w*|workflow\w*|feedback|self[- ](?:improv\w*|refin\w*)|interact\w*|iterat\w*|synthes\w*',re.I)
GRAPHICS=re.compile(r'graphic\w*|visual\w*|imag\w*|\bsvg\b|\b3d\b|scene\w*|world\w*|spatial\w*|geometr\w*|mesh\w*|\bcad\b|render\w*|animat\w*|simulat\w*|layout\w*|poster\w*|diagram\w*|chart\w*|video\w*|design\w*|articulat\w*|shape\w*|model(?:ing|ling)|draw\w*|illustrat\w*|infographic\w*',re.I)


def title_hints(entries):
    hints=[]
    for entry in entries:
        title=entry.get('title','')
        mechanism=sorted(set(x.lower() for x in MECHANISM.findall(title)))
        graphics=sorted(set(x.lower() for x in GRAPHICS.findall(title)))
        if mechanism and graphics:
            hints.append({'arxiv':entry['arxiv'],'title':title,'mechanism_terms':mechanism,'graphics_terms':graphics,
                          'canonical_url':entry.get('canonical_url','')})
    return hints
