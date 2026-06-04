#!/usr/bin/env bash
set -euo pipefail

repo_root="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$repo_root"

collect_github_issues() {
  if command -v gh >/dev/null 2>&1; then
    gh issue list --state open --json number,title,body,labels --limit 50 2>/dev/null || echo "Could not read GitHub issues with gh."
  else
    echo "gh CLI not found; GitHub issue queue unavailable."
  fi
}

collect_patterns() {
  find patterns -maxdepth 3 -type f -name '*.md' 2>/dev/null | sort
}

collect_validation() {
  make validate 2>&1 || true
}

commits="$(git log -n 5 --format='%H%n%ad%n%B---' --date=short 2>/dev/null || echo 'No commits found.')"
issues="$(collect_github_issues)"
patterns="$(collect_patterns)"
validation="$(collect_validation)"
prompt="$(cat ralph/prompt.md)"

codex -a on-request -s workspace-write \
  "Previous commits:
$commits

GitHub issues:
$issues

Pattern inventory:
$patterns

Current validation output:
$validation

$prompt"
