# Discovery Source Matrix

Use sources for their actual strengths. Same-day work is browser-based and verifies releases on authoritative pages. Historical work uses the bundled collector for scalable, auditable retrieval and then follows up in the browser.

## Source roles

| Source | Same-day browser role | Historical role | Evidence caveat |
|---|---|---|---|
| arXiv | Browse `new`, `recent`, category, search, and canonical abstract pages | Category-by-submission-date enumeration with adaptive slicing and pagination | Category coverage is broad but not universal; the canonical submission history is the date authority |
| Hugging Face Papers | Browse Daily Papers, search results, and individual paper pages | Supplemental recent-paper coverage | Curation date and arXiv publication date may differ |
| OpenReview | Browse recent submissions, venue groups, search results, and forum pages | Manual follow-up after collection | Forum modification time is not automatically a paper-release date |
| Official proceedings and venue pages | Browse current programs, proceedings, and digital libraries | Manual archive follow-up | Prefer the authoritative proceedings record over search snippets |
| OpenAlex, Crossref, Semantic Scholar, and DBLP websites | Supplemental browser searches and identity/date cross-checks | Multi-index query augmentation | Index or update dates are not paper-release dates |
| Project, author, lab, and organization pages | Verify plausible releases and locate primary artifacts | Manual follow-up | Use only authoritative pages for final evidence |
| GitHub and public social posts | Lead generation or artifact verification after a plausible paper is known | Project/repository alias discovery | Repository or post activity is not paper-publication evidence |

## Same-day browser policy

Use browser or web-search tools directly. Do not run the bundled discovery script, query scholarly API endpoints, or create a scraper for the same-day workflow.

1. Use the explicit target date, otherwise the client current calendar day in `America/Chicago`.
2. Derive a compact query set from the taxonomy and paper-list aliases. Cover general Agentic Graphics, Blender/DCC, CAD and fabrication, 3D scene/world generation, rendering/material/lighting, inverse graphics, animation, simulation/physics, graphics code, tool interfaces, spatial reasoning, feedback/refinement, and benchmarks.
3. Run a breadth-first pass across arXiv category `new`/`recent` pages and targeted arXiv search results; Hugging Face Daily Papers and targeted paper searches; OpenReview; official current venue/proceedings pages; and targeted project/author/lab searches. Use ordinary web search to locate pages, not as final evidence. Do not spend the whole run deep-reading the first lead.
4. Use a default interactive budget of 6 minutes, 10 search batches, and 24 candidate/primary-page opens. Stop at the first limit reached. Retry a failed page or query once at most, record the failure, and move to the next source family. An explicitly requested extended pass must still declare a finite budget.
5. Open plausible candidates' canonical paper or official proceedings pages until the page budget is exhausted. Verify the title, identifiers, event type, and exact day before inclusion.
6. Deduplicate by arXiv ID, DOI, OpenReview forum ID, and normalized title while preserving aliases and version history.
7. Maintain a source ledger with the page/query checked, timestamp, status, candidates found, limitations, and whether a family was not reached within budget.
8. Screen and curate at most 10 verified candidates in the first response, queue any remainder, and save an English Markdown report even when coverage is partial.

Use one of these report labels:

- `browser-based same-day search; documented source coverage` when every maintained browser source family was attempted and limitations are listed;
- `partial browser-based same-day search; source coverage incomplete` when one or more material source families could not be checked;
- `blocked browser-based same-day search; no primary paper source accessible` when no authoritative paper source could be inspected.

These are evidence-boundary labels, not completeness guarantees. If no candidate qualifies, say only that no qualifying paper was verified in the browsed source set.

## Targeted follow-up sources

- OpenReview and official conference programs or proceedings;
- CVF Open Access, ACM Digital Library, IEEE Xplore, Eurographics Digital Library, AAAI, SIGGRAPH and SIGGRAPH Asia pages;
- official project, author, laboratory, university, benchmark, dataset, and demo pages;
- Hugging Face paper pages, models, datasets, Spaces, and collections;
- GitHub/GitLab repositories, releases, tags, and organization pages;
- official company research blogs, engineering blogs, newsrooms, developer changelogs, and product announcements;
- public author/lab/company posts on X, Bluesky, Mastodon, LinkedIn, YouTube, and similar channels;
- curated lists, newsletters, Hacker News, Reddit, and technology press as lead generators only.

## Historical two-lane rule

The historical runner must use both mechanisms unless the user explicitly narrows the task:

1. **Enumeration lane:** enumerate arXiv metadata by configured category and submission-date slices, recursively split dense slices, paginate until `totalResults`, retain raw records, and checkpoint every completed slice.
2. **Query-augmentation lane:** query every controlled taxonomy family across OpenAlex, Crossref, Semantic Scholar, DBLP, and Hugging Face to recover non-arXiv work, aliases, and records outside the enumerated categories.

For an interactive run, execute query augmentation first, interleave maintained sources for each taxonomy query, and then enumerate arXiv newest-first. Use a 60-second foreground budget by default, a 10-second request timeout, two attempts, short bounded backoff, and page-level progress. Return the materialized checkpoint before attempting another batch. These priority choices improve time-to-first-result but do not change eventual configured coverage. Resume only through the same output directory so pages and slices remain auditable.

Query augmentation is not enumeration. Category enumeration is not universal scholarly coverage. Neither can prove that all papers have been found.

## Coverage and claim rule

A same-day report must expose its browser source ledger and scope every result or zero-result statement to the pages and searches actually checked. A historical collection-integrity gate passes only when every configured arXiv date slice completes without truncation or gaps, recent slices pass stability checks, every configured query batch exhausts before its cap, every supplied non-injection recall check passes, and raw artifacts are retained. A usable historical run also requires the independent artifact audit. A separate comprehensive-wording gate additionally requires the maintained full date/category/source/query scope. Manual venue/archive and citation-chain follow-up remains required for strong field-coverage claims. Record failures and access limits rather than silently dropping a source.

Never equate a passing gate with a mathematical completeness guarantee. `best-effort comprehensive automated historical sweep` is permitted only when the independent artifact audit and comprehensive-wording gate pass; forbidden wording includes `all papers found`, `complete literature`, and `provably exhaustive`.

For the current executable daily output/date contract, read [daily-workflow.md](daily-workflow.md). Offline preparation and validation are allowed; the API/scraper restriction concerns retrieval.
