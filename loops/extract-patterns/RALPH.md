---
agent: codex
commands:
  - name: validate
    run: python scripts/validate_patterns.py
  - name: suggest
    run: python scripts/enrich_related_tags.py --suggest
  - name: index
    run: python scripts/build_index.py
args:
  - source_id
  - subject
  - focus
---

# Extract Patterns Loop

Turn registered source material into original, reusable pattern files.

## Inputs

- `source_id`: source key from `sources/manifest.yml`.
- `subject`: preferred subject folder under `patterns/`.
- `focus`: concept, problem, or architecture concern to extract.

## Required context

Read these files first:

1. `AGENTS.md`
2. `config/repo_policy.yml`
3. `config/subjects.yml`
4. `config/taxonomy.yml`
5. `sources/manifest.yml`
6. Existing files under `patterns/{{ args.subject }}/`

If local extracts exist, read only the chunks needed for `{{ args.focus }}` from `work/extracts/{{ args.source_id }}/chunks.jsonl`. Do not copy source text into the pattern body.

## Loop task

Before starting a loop, split broad extraction goals into individual GitHub Issues using `docs/agents/issue-tracker.md`. Each issue should target one source-backed concept and one primary subject folder.

For each iteration:

1. Identify whether `{{ args.focus }}` belongs in an existing pattern or a new one.
2. Search existing patterns for related concepts using `rg` and the tag suggestion command.
3. Create or update a subject-area pattern file.
4. Write original synthesis, not a recap of the source.
5. Add source lineage in frontmatter and `Source notes`.
6. Add tags, aliases, applicability triggers, avoid conditions, and related pattern IDs.
7. Run validation and fix errors.
8. Build the index.
9. If this work came from a GitHub issue, comment with the files changed and checks run, then close the issue after committing.
10. Stop after one coherent pattern-level change so the git diff stays reviewable.

## Acceptance criteria

- `{{ commands.validate }}` passes.
- `{{ commands.suggest }}` has been considered.
- `{{ commands.index }}` runs successfully.
- No files under `intake/raw/` or `work/extracts/` are staged.
- The new or changed pattern is organized by subject, not by source chapter.
- The pattern can guide an agent without access to the source material.
- Any completed GitHub issue has a result comment and is closed after commit.
