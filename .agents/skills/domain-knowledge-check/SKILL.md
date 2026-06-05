---
name: domain-knowledge-check
description: Check architecture, platform, infrastructure, domain-modeling, cloud, delivery, operations, reliability, scaling, governance, configuration, secrets, and data-system questions against the local subject-groups and patterns corpus. Use when Codex needs cross-domain, reference-grounded critique, alignment scoring, relationship mapping, or recommendations from local patterns, anti-patterns, principles, governance patterns, and decision guides. Return "no matching context" for unrelated prompts.
---

# Domain Knowledge Check

Use this skill to answer or critique a user prompt only when the local pattern corpus contains matching context. Ground every recommendation in the reference files.

## Reference Layout

- Use `subject-groups/manifest.json` as the primary structured subject-group index when present.
- Use `subject-groups/README.md` to see the available subject groups.
- Use `subject-groups/*.md` to inspect group membership and subject relationships.
- Use `patterns/*.md` for full pattern guidance, including `Use when`, `Avoid when`, `related`, `Checks`, and `Failure modes`.

Resolve paths relative to the repository or workspace root that contains `subject-groups/` and `patterns/`.

## Matching Workflow

1. Extract the user's concrete domain terms, technologies, risks, design decisions, symptoms, and requested outcome.
2. Search the subject-group index first. Match against group names, pattern titles, ids, types, tags, summaries, and source paths.
3. Read every subject group that appears relevant or potentially relevant. Include adjacent groups when the prompt spans concerns such as change plus reliability, data plus coordination, or governance plus secrets.
4. Perform the cross-domain fan-out pass below before finalizing candidates. This is required for design reviews, alignment scoring, architecture critique, modernization, migration, and standardization prompts.
5. Collect all candidate patterns, anti-patterns, governance patterns, and decision guides that plausibly relate to the prompt. Treat decision guides and governance patterns as principle guidance when no file is explicitly typed as a principle.
6. Read the full `patterns/*.md` files for each candidate before judging. Include `related` patterns when the loaded pattern names them and the relationship is relevant to the user's question.
7. If no subject-group entry or pattern file plausibly matches the prompt, respond exactly:

```text
no matching context
```

Do not provide generic advice after returning `no matching context`.

## Cross-Domain Fan-Out

Do not stop at the first obvious technology family. After direct matches are found, explicitly consider every pattern family represented by candidate ids in the corpus, normally `iac`, `ddd`, `data`, and `platform`.

- `iac`: Terraform, infrastructure-as-code, modules, stacks, environments, state, drift, pipelines, policy, reproducibility, change safety.
- `ddd`: business units, teams, ownership, inconsistent terminology, lifecycle names, migration from local or legacy models, standardization across autonomous groups, bounded contexts, context maps, ubiquitous language.
- `data`: SQL, storage, stateful migration, data continuity, consistency, replication, recovery, schema/data contracts, analytical or operational data flows.
- `platform`: platform operating model, shared services, golden paths, reusable operational components, Kubernetes, containers, sidecars/adapters, observability normalization, service discovery.

For each family:

1. Identify whether the prompt has direct, adjacent, weak, or no trigger signals.
2. Include references from families with direct or adjacent trigger signals, even when the main technology belongs to another family.
3. Include weaker candidates only when they could reveal an important risk the primary lens would miss; mark them as potential.
4. Exclude a family only after checking group entries, tags, summaries, and relevant `related` links; record the reason in `Lens Coverage`.

The goal is broad review without pattern dumping: make the agent prove adjacent lenses were considered, not force every family into every answer.

## Relevance Rules

- Count a reference as relevant when the prompt directly matches its id, title, aliases, tags, summary, `Use when`, problem statement, checks, or failure modes.
- Count a reference as potentially relevant when it shares a meaningful subject group, risk, tag, or related-pattern link with a direct match.
- Do not count a reference as relevant only because it shares generic words such as system, service, cloud, platform, data, or architecture.
- Prefer including a weaker but plausible candidate over omitting context, but mark the relationship as potential.
- Never invent a pattern, principle, source, relationship, or score that is not grounded in the local files.

## Scoring

Rate each selected reference from 1 to 100 for alignment with the reference guidance:

- `90-100`: Strongly aligned; the design or answer satisfies the key checks and avoids known failure modes.
- `70-89`: Mostly aligned; gaps are limited or easy to close.
- `50-69`: Partially aligned; important details are missing, ambiguous, or uneven.
- `25-49`: Weakly aligned; the design shows major gaps or contradicts important guidance.
- `1-24`: Misaligned; the design strongly exhibits the failure mode or ignores the reference guidance.

For anti-patterns, the score still means alignment with the reference guidance, not alignment with the bad behavior. A high anti-pattern score means the design avoids or remediates the anti-pattern; a low score means it exhibits the anti-pattern.

## Output Contract

When matching context exists, structure the answer around the references, not around generic recommendations.

Always include:

- `Lens Coverage`: state the primary lens, adjacent lenses included, potential lenses included, and lenses considered but excluded with a brief reason.
- `Matching Context`: cite every selected reference by id, title, type, and source path.
- `Relationships`: explicitly state why each reference was selected, including subject group, matching tags or terms, and related-pattern links when relevant.
- `Alignment Review`: for each reference, state the 1-100 alignment score, where the user prompt aligns, where it misaligns or is unclear, and a small recommendation to align more closely.
- `Grounded Recommendation`: provide concise advice that cites the reference ids it depends on.

Use this compact table shape when practical:

| Reference | Relationship | Score | Aligns | Misaligns or unclear | Small recommendation |
| --- | --- | ---: | --- | --- | --- |
| `id` Title (`type`, `patterns/file.md`) | Subject group/tag/related-pattern reason | 1-100 | Concrete alignment | Concrete gap | Specific next adjustment |

If a user asks a narrow question, a short table plus a brief grounded recommendation is enough. If a user asks for a design review, include all relevant and potentially relevant references before making recommendations.

## Source Policy

Use only original synthesized guidance and source pointers from the local pattern files. Do not reproduce long passages from source chapter text.
