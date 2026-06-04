---
agent: codex
commands:
  - name: suggest
    run: python scripts/enrich_related_tags.py --suggest
  - name: validate
    run: python scripts/validate_patterns.py
  - name: index
    run: python scripts/build_index.py
args:
  - focus
---

# Tag Enrichment Loop

Improve cross-references, tags, aliases, and related concept discovery across the pattern library.

## Required context

Read:

1. `AGENTS.md`
2. `config/taxonomy.yml`
3. `config/subjects.yml`
4. `work/suggestions/related-tags.md` if it exists after running the suggestion command.
5. Pattern files related to `{{ args.focus }}`.

## Loop task

Before starting a loop, split broad enrichment goals into individual GitHub Issues using `docs/agents/issue-tracker.md`. Each issue should cover one focused tag, alias, trigger-hint, or related-link cleanup cluster.

For each iteration:

1. Run the suggestion command.
2. Inspect suggestions for false positives.
3. Update tags only when they make future retrieval more accurate.
4. Add `related` links when another pattern would materially change the design advice.
5. Add reciprocal `related` links when appropriate.
6. Improve aliases and agent trigger hints for common user phrasing.
7. Avoid tag stuffing. Prefer a small set of high-signal tags.
8. Run validation and rebuild the index.
9. If this work came from a GitHub issue, comment with the files changed and checks run, then close the issue after committing.

## Acceptance criteria

- `{{ commands.validate }}` passes.
- `{{ commands.index }}` runs successfully.
- Related links point to existing pattern IDs.
- Cross-subject relationships are intentionally preserved when useful.
- The diff contains metadata and retrieval improvements, not broad rewrites.
- Any completed GitHub issue has a result comment and is closed after commit.
