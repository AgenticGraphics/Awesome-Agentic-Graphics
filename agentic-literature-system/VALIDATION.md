# Release validation — October 25, 2026

- Skill: 55 offline tests passed; portable-bundle validation and skill frontmatter validation passed.
- Harness: 180 offline tests passed, including synthetic model transport/replay, interruption recovery, paper contracts, PDF reading receipts, source/catalog coverage, history isolation, shell secret filtering, caller configuration, and process cleanup.
- Relocation: exported only staged Git files to a separate directory; repeated both suites, bundle validation, offline example preparation, and runner help successfully. No original experiment directory or private document connection was needed.
- Publication review: checked the staged source for developer usernames, absolute home paths, private host addresses, credential patterns, embedded authentication, private document identifiers, binary files, nested repository metadata, and generated run/cache files. No findings remained. README links and Python/JSON syntax were checked.
- Limitations: tested on macOS with Python 3.14. A fresh Linux/WSL installation and live provider/model compatibility were not exercised. No paid research run was performed for this release. These checks establish package behavior and publication hygiene; they do not certify every possible secret pattern, semantic paper accuracy, or exhaustive discovery.

Generated traces and test artifacts are excluded from the release. The included `harness/check_release.py` can be rerun on staged changes and deliberately reports locations/categories rather than matched secret values.
