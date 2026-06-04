---
agent: codex
commands:
  - name: validate
    run: python scripts/validate_patterns.py
  - name: status
    run: git status --short
  - name: diff
    run: git diff -- patterns config sources scripts loops AGENTS.md README.md
args:
  - review_scope
---

# Curator Review Loop

Review pattern-library changes before they are pushed or merged.

## Required context

Read:

1. `AGENTS.md`
2. `config/repo_policy.yml`
3. `sources/manifest.yml`
4. Changed files from `{{ commands.diff }}`.

## Review task

Before starting a review loop, split broad review goals into individual GitHub Issues using `docs/agents/issue-tracker.md`. Each issue should cover one review scope, such as one pattern, one source lineage concern, one validation failure class, or one changed-file cluster.

For each iteration:

1. Confirm no raw source material or extracted source text is staged.
2. Confirm changed patterns are subject-organized.
3. Confirm source lineage is present and honest.
4. Check that pattern text is original synthesis, not close paraphrase.
5. Check that tags and related links are useful for future retrieval.
6. Check that the pattern includes tradeoffs, failure modes, and review questions.
7. Run validation and propose minimal fixes.
8. If there are issues, fix them and re-run validation.
9. If this work came from a GitHub issue, comment with the files changed and checks run, then close the issue after committing.
10. Stop when the diff is ready for human review.

## Acceptance criteria

- `{{ commands.validate }}` passes.
- `{{ commands.status }}` shows no raw intake or work extracts staged.
- Changed files comply with `AGENTS.md` and `config/repo_policy.yml`.
- The final message summarizes the review decisions and any remaining uncertainty.
- Any completed GitHub issue has a result comment and is closed after commit.
