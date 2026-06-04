---
name: scaffold-issue-creation
description: Scaffold repository guidance for agent-created issues using only GitHub Issues or GitLab Issues. Use when a repo needs docs/agents issue tracker setup, AGENTS.md issue creation instructions, gh/glab command conventions, or a restricted GitHub/GitLab-only issue creation workflow.
---

# Scaffold Issue Creation

Set up repo-local agent guidance for creating issues in **GitHub Issues** or **GitLab Issues** only. Do not configure local markdown, Jira, Linear, Azure DevOps, or other trackers for this skill.

## Workflow

1. Inspect the repo.
   - Run `git remote -v` if available.
   - Read root `AGENTS.md` if present.
   - Check `docs/agents/issue-tracker.md`.
   - Identify whether the remote is GitHub or GitLab.

2. Choose tracker.
   - If the remote clearly points to GitHub, use GitHub.
   - If the remote clearly points to GitLab, use GitLab.
   - If ambiguous, ask the user to choose GitHub or GitLab.
   - If the user asks for another tracker, explain that this skill only scaffolds GitHub/GitLab issue creation.

3. Write `docs/agents/issue-tracker.md`.
   - Use the matching template below.
   - Keep commands concrete and copy-pastable.
   - Include creation, reading, listing, commenting, labeling, and closing conventions.

4. Update or create root `AGENTS.md`.
   - If an `## Agent skills` block exists, update its issue tracker subsection in place.
   - Otherwise append an `## Agent skills` block.
   - If `AGENTS.md` does not exist, create it.

5. Verify.
   - Re-read the changed files.
   - Do not call `gh issue create` or `glab issue create` during setup unless the user explicitly asks to create a real issue.

## AGENTS.md Block

```markdown
## Agent skills

### Issue creation

Issues for this repo are created in [GitHub/GitLab] using the [`gh`/`glab`] CLI. See `docs/agents/issue-tracker.md` before creating, reading, labeling, commenting on, or closing issues.
```

Replace the bracketed values with the chosen tracker and CLI.

## GitHub Template

```markdown
# Issue tracker: GitHub

Issues for this repo live in GitHub Issues. Use the `gh` CLI for issue operations.

## Commands

- Create: `gh issue create --title "..." --body "..."`
- Read: `gh issue view <number> --comments`
- List: `gh issue list --state open --json number,title,body,labels,comments`
- Comment: `gh issue comment <number> --body "..."`
- Add label: `gh issue edit <number> --add-label "..."`
- Remove label: `gh issue edit <number> --remove-label "..."`
- Close: `gh issue close <number> --comment "..."`

Use a temporary file or heredoc for multi-line issue bodies.

## Publishing Rules

When an agent is asked to publish work to the issue tracker, create a GitHub issue. Infer the repository from the current git remote unless the user supplies an explicit repo.

Do not create issues until the user has approved the issue title and body, unless the user explicitly asks for direct creation.
```

## GitLab Template

```markdown
# Issue tracker: GitLab

Issues for this repo live in GitLab Issues. Use the `glab` CLI for issue operations.

## Commands

- Create: `glab issue create --title "..." --description "..."`
- Read: `glab issue view <number> --comments`
- List: `glab issue list -F json`
- Comment: `glab issue note <number> --message "..."`
- Add label: `glab issue update <number> --label "..."`
- Remove label: `glab issue update <number> --unlabel "..."`
- Close: `glab issue close <number>`

Use a temporary file or heredoc for multi-line issue descriptions. GitLab calls issue comments "notes"; post a note before closing if the close needs explanation.

## Publishing Rules

When an agent is asked to publish work to the issue tracker, create a GitLab issue. Infer the repository from the current git remote unless the user supplies an explicit repo.

Do not create issues until the user has approved the issue title and description, unless the user explicitly asks for direct creation.
```

## Quality Bar

- The setup names exactly one tracker: GitHub or GitLab.
- `docs/agents/issue-tracker.md` contains no local/other tracker fallback.
- `AGENTS.md` points agents to `docs/agents/issue-tracker.md`.
- The setup is guidance-only; it does not create live issues unless requested.
