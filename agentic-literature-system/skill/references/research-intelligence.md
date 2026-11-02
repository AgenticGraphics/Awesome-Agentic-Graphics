# Taxonomy-Grounded Research Intelligence

Use this capability to turn the maintained Agentic Graphics corpus into answers, comparisons, novelty judgments, gap analyses, and actionable research plans.

## Required bundled context

Before answering, read [METHOD_TAXONOMY_TABLE.md](METHOD_TAXONOMY_TABLE.md) and [PAPER_READING_LIST.md](PAPER_READING_LIST.md). The bundled taxonomy is the bundled frozen agentic-system taxonomy; do not substitute historical taxonomy fields.

- Use the taxonomy to interpret the domain, normalize terminology, select comparison axes, and identify structured coverage gaps.
- Use the paper list to retrieve the current Overleaf survey methods, their task assignments, citation keys, links, and in-survey status.
- Ground the answer in passages or entries from these documents, then verify current facts at primary sources when freshness matters.

## Retrieve before reasoning

Read the relevant definitions in the bundled taxonomy and every pertinent section of the bundled paper list before forming a conclusion. Retrieve by concepts and aliases, not only exact keywords. When current status matters, follow canonical paper, project, repository, dataset, benchmark, or venue links and verify the latest public evidence.

Build a compact evidence set for the question. For every central claim, retain the supporting method or source, its corpus status, and the taxonomy fields that make it comparable.

## Domain questions and synthesis

Answer the research question directly, then show the evidence boundary:

- what the maintained literature establishes;
- what is supported only by adjacent work;
- what is an inference from the taxonomy or comparison;
- what remains unknown or under-reported.

Do not treat an absent paper-list entry as proof that no such work exists. For existence, novelty, field-coverage, or corpus-completeness questions, run exactly one 60-second historical checkpoint per interactive response, return it immediately, and apply the bundled screening and taxonomy-curation contracts to at most five highest-priority candidates. State how many candidates remain rather than silently reading the whole queue. Resume only when requested and only with the same output directory. For questions restricted to releases on the current date, use the 6-minute bounded browser workflow and verify every result on an authoritative paper page. Synchronized companion skills may execute historical stages when available, but are not required.

## Method comparison

Select comparison axes from the bundled taxonomy rather than using generic feature lists. Compare only fields material to the question: task and contribution; model/input, availability, and adaptation; organization, orchestration, execution, and topology; feedback signal, evaluator, and update; application, environment, tools, action representation, interface, and observation space; resource content/source/use; and evaluation source/target.

Normalize different terminology before comparing it. Distinguish:

- architectural differences from implementation details;
- training-time agentic pipelines from inference-time agentic systems;
- agentic models from harnesses, toolkits, datasets, and benchmarks;
- reported evidence from inferred capability;
- missing information from a negative result.

## Novelty assessment

For an idea or claimed contribution:

1. Decompose it into task, contribution, model/adaptation, agent organization, orchestration, control loop, feedback/evaluator/update, action representation, interaction interface, observation space, resources, tools/environment, and evaluation.
2. Retrieve the closest core and adjacent precedents for each component and for the full combination.
3. State which components are known, which combination may be new, and which claim is not yet defensible.
4. Run one bounded checkpoint of the database-first historical discovery pipeline across the relevant taxonomy cells, including recent work, then screen and curate at most five prioritized candidates before making the current provisional novelty judgment. If coverage is incomplete, state what a resume could change.
5. Give a calibrated judgment such as `likely incremental`, `potentially differentiated`, or `plausibly novel but not yet established`, with the evidence and search limitations.

Never give an absolute novelty guarantee.

## Gap analysis

Look for gaps created by coverage, evidence, or system design rather than merely counting papers. Useful gap types include:

- empty or weakly populated taxonomy combinations;
- graphics tasks, environments, tools, action/interface/observation choices, feedback channels, or resource-use regimes with little coverage;
- capabilities claimed without appropriate benchmarks or ablations;
- closed-source dependencies, irreproducible pipelines, or missing artifacts;
- narrow benchmarks, weak baselines, metric misalignment, or missing human and physical evaluation;
- limited generalization across tasks, assets, tools, engines, or domains;
- missing safety, provenance, editability, controllability, collaboration, or long-horizon evaluation;
- taxonomy concepts repeatedly forced into `Other`, `Unclear`, or overloaded values.

Distinguish a true research gap from a gap in the maintained reading list or from under-reporting in papers. State what additional search or evidence would resolve the ambiguity.

## Future-direction planning

Convert a supported gap into a testable research direction. For each recommended direction, provide:

- the observed evidence and why the gap matters;
- the proposed research question or falsifiable hypothesis;
- the minimum system, model, dataset, benchmark, or taxonomy change needed;
- the closest baselines and comparisons;
- an evaluation plan with success and failure criteria;
- major technical, data, reproducibility, and scope risks;
- the smallest experiment that could invalidate the idea early;
- a calibrated novelty and impact assessment.

Rank directions by evidence strength, expected research value, feasibility, and differentiation. Prefer plans that close a demonstrated gap over speculative feature accumulation.

## Research-intelligence output

Use concise prose and tables where they clarify comparisons. Cite direct sources near claims. End with a short decision-oriented conclusion: what is known, what is uncertain, and the next highest-value research action.
