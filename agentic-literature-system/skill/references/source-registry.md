# Source registry

The public release uses the frozen October 15, 2026 survey research snapshot in [source-manifest.json](source-manifest.json). Private document IDs, tab IDs, and revision tokens are not distributed. The release revision identifies this sanitized bundle, not a live document revision.

Read [METHOD_TAXONOMY_TABLE.md](METHOD_TAXONOMY_TABLE.md) for source wording and [taxonomy-codebook.json](taxonomy-codebook.json) for executable labels. The source heading says Taxonomy v2 while the original tab was named v3; the mismatch and provisional Tools definitions are preserved. This 18-field experimental codebook is versioned independently of later manuscript/website terminology.

[paper-corpus.json](paper-corpus.json) holds 259 discussed-paper occurrences, including repeated placements and alternative/adjacent entries. Membership is prior context, not a new discovery or an inclusion verdict.

To refresh, supply your own authorized taxonomy and corpus snapshots. Update both text snapshots, the structured corpus, source manifest, codebook and curation schema consistently. Keep source retrieval dates and public provenance; do not publish private document identifiers. Run the portable validator and offline tests. New candidates never silently change the accepted corpus or taxonomy.
