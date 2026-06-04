# Issue tracker: GitHub

Issues for this repo live in GitHub Issues. Use the `gh` CLI for issue operations.

## Commands

- Create: `gh issue create --title "..." --body "..."`
- Read: `gh issue view <number> --comments`
- List: `gh issue list --state open --json number,title,body,labels,comments`
- List Ralph queue: `gh issue list --state open --json number,title,body,labels --limit 50`
- Comment: `gh issue comment <number> --body "..."`
- Add label: `gh issue edit <number> --add-label "..."`
- Remove label: `gh issue edit <number> --remove-label "..."`
- Close: `gh issue close <number> --comment "..."`

Use a temporary file or heredoc for multi-line issue bodies.

## Publishing Rules

When an agent is asked to publish work to the issue tracker, create a GitHub issue. Infer the repository from the current git remote unless the user supplies an explicit repo.

Do not create issues until the user has approved the issue title and body, unless the user explicitly asks for direct creation.

## Ralph Task Queue

Use GitHub Issues as Ralph's task queue. Break broad curation requests into separate issues before starting the loop.

Each Ralph issue should describe exactly one bounded, reviewable task:

- one pattern to create or update
- one tag or related-link cleanup cluster
- one validation failure class
- one review scope
- one repo-hygiene change

Avoid issues that require multiple unrelated patterns, multiple source areas, or open-ended exploration. If a request has several independent outcomes, create several issues instead of one umbrella issue.

Recommended issue body:

```markdown
## Task
Describe the single bounded task Ralph should complete.

## Context
- Source IDs:
- Subject area:
- Relevant files:
- Constraints:

## Acceptance criteria
- [ ] Expected file or metadata change
- [ ] Validation command to run
- [ ] Index or suggestion command to run, if applicable
```

Recommended labels:

- `ralph`
- `status:ready`
- one type label such as `type:pattern`, `type:tag-enrichment`, `type:review`, or `type:repo-hygiene`

When Ralph completes an issue, comment with the selected task, files changed, checks run, and commit hash. Close the issue only after the task is complete and committed.
