#!/usr/bin/env bash
set -euo pipefail

if [ -z "$1" ]; then
  echo "Usage: $0 <iterations>"
  exit 1
fi

repo_root="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$repo_root"

# jq filter to extract streaming text from assistant messages
stream_text='select(.type == "assistant").message.content[]? | select(.type == "text").text // empty | gsub("\n"; "\r\n") | . + "\r\n\n"'

# jq filter to extract final result
final_result='select(.type == "result").result // empty'

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

collect_suggestions() {
  make suggest-tags 2>&1 || true
  if [ -f work/suggestions/related-tags.md ]; then
    printf '\n--- work/suggestions/related-tags.md ---\n'
    sed -n '1,220p' work/suggestions/related-tags.md
  fi
}

for ((i=1; i<=$1; i++)); do
  tmpfile=$(mktemp)
  trap "rm -f $tmpfile" EXIT

  commits="$(git log -n 5 --format='%H%n%ad%n%B---' --date=short 2>/dev/null || echo 'No commits found.')"
  issues="$(collect_github_issues)"
  patterns="$(collect_patterns)"
  validation="$(collect_validation)"
  suggestions="$(collect_suggestions)"
  prompt="$(cat ralph/prompt.md)"

  codex -a on-request -s workspace-write \
    --verbose \
    --print \
    --output-format stream-json \
    "Previous commits:
$commits

GitHub issues:
$issues

Pattern inventory:
$patterns

Current validation output:
$validation

Current tag/link suggestions:
$suggestions

$prompt" \
  | grep --line-buffered '^{' \
  | tee "$tmpfile" \
  | jq --unbuffered -rj "$stream_text"

  result=$(jq -r "$final_result" "$tmpfile")

  if [[ "$result" == *"<promise>NO MORE TASKS</promise>"* ]]; then
    echo "Ralph complete after $i iterations."
    exit 0
  fi
done
