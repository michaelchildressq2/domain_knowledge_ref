---
name: knowledge-base-curator
description: Build and maintain subject-organized markdown knowledge-base pattern repositories for platform engineering, architecture, SRE, infrastructure-as-code, reliability, disaster recovery, data consistency, security, governance, and operations. Use when asked to extract reusable patterns from source material, organize pattern files by subject area rather than chapter, enrich tags and related concepts across existing items, run repository validation scripts, or prepare Ralph-loop or Docker-sandbox tasks while preserving attribution and avoiding verbatim copyrighted text.
---

# Knowledge Base Curator

Use this skill to help maintain a git-native pattern library for agents.

## Operating model

Treat the repository as the source of truth. Before creating or editing a pattern, read:

1. `AGENTS.md`
2. `config/subjects.yml`
3. `config/taxonomy.yml`
4. `sources/manifest.yml`
5. Existing files under `patterns/<subject-area>/`

If the repository includes scripts, prefer running them instead of manually checking structure.

## Source-use rules

Follow `references/source-use-policy.md`.

In short:

- Extract concepts, tradeoffs, decision criteria, and implementation moves.
- Do not produce chapter recaps.
- Do not copy long passages, tables, figures, examples, or distinctive phrasing.
- Attribute source lineage in frontmatter and `Source notes`.
- Keep raw source documents and extracted text out of git unless the user explicitly confirms a rights-reviewed exception.

## Pattern workflow

1. Identify the source ID in `sources/manifest.yml`.
2. Select the primary subject folder from `config/subjects.yml`.
3. Search existing patterns for duplicates and related concepts.
4. Decide whether to update an existing pattern or create a new one.
5. Use the pattern contract in `references/pattern-file-contract.md`.
6. Add tags, aliases, applicability triggers, avoid conditions, and related pattern IDs.
7. Run validation and tag-enrichment scripts when available:
   - `python scripts/validate_patterns.py`
   - `python scripts/enrich_related_tags.py --suggest`
   - `python scripts/build_index.py`
8. Inspect the resulting diff for accidental source copying and duplicate patterns.

## Subject organization

Do not mirror a source's chapter structure. Organize by future use:

- `reliability`: high availability, disaster recovery, observability, resilience, incident response.
- `data`: consistency, continuity, migration, replication, backup, restore, state ownership.
- `infrastructure-as-code`: modules, stacks, drift, environment parity, delivery, idempotency.
- `governance`: standards, guardrails, policy, compliance, auditability, approval flows.
- `security`: identity, secrets, least privilege, isolation, secure configuration.
- `operations`: runbooks, maintenance, supportability, decommissioning, operational feedback.

When a pattern spans subjects, choose the most useful primary folder and add tags plus `related` links for secondary concerns.

## Tag enrichment

When adding or reviewing patterns:

- Use canonical tags from `config/taxonomy.yml` where possible.
- Add aliases for user phrases that may trigger retrieval.
- Link related patterns when using one pattern would affect the other.
- Prefer high-signal tags over broad tag stuffing.
- Add reciprocal `related` links when the relationship is useful in both directions.

## Ralph-loop task design

For autonomous loops, keep each iteration small and reviewable:

- Use GitHub Issues as the Ralph task queue; read `docs/agents/issue-tracker.md` before creating, reading, updating, or closing issues.
- Break broad requests into one issue per bounded task before starting Ralph.
- Extract or update one coherent pattern at a time.
- Keep each issue scoped to one pattern, one validation failure class, one tag/related-link cleanup cluster, one review scope, or one repo-hygiene change.
- Include source IDs, subject area, relevant files, constraints, and acceptance criteria in each issue body.
- Run validation at the end of each loop.
- Stop after a meaningful git diff.
- Use git as memory; do not rely on agent context to remember previous decisions.
- Keep raw extracts local and gitignored.
- After completing an issue, comment with the result, commit hash, and checks run, then close the issue.

## Output expectations

When reporting back to the user, include:

- What patterns were created or changed.
- What source IDs were used.
- What validation commands passed or failed.
- Any source-use or confidence caveats.
- The file paths that changed.
