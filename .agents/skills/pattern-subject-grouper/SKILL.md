---
name: pattern-subject-grouper
description: Group reusable pattern markdown files from one or more pattern folders into common subject matter areas. Use when Codex needs to cluster pattern libraries from multiple sources, compare overlapping architecture or platform guidance, create subject-area indexes, or prepare grouped pattern files for a later agent to turn into skills or references.
---

# Pattern Subject Grouper

Use this skill to group standalone pattern markdown files by common subject matter. It expects pattern files with YAML-style frontmatter like the output from `chapter-pattern-extractor` or `pattern-library-builder`.

## Workflow

1. Identify one or more input pattern folders.
   - Example inputs in this workspace:
     - `patterns/`
     - `.agents/skills/infrastructure-as-code-patterns/references/patterns/`
   - Inputs should contain `*.md` pattern files with `id`, `title`, `summary`, `tags`, and related frontmatter.

2. Run the grouping script.

```bash
python3 .agents/skills/pattern-subject-grouper/scripts/group_patterns.py \
  patterns \
  .agents/skills/infrastructure-as-code-patterns/references/patterns
```

The default output folder is the repository-root `./work/` folder. Subject-group files are generated there as additional working output.

3. Inspect `work/`.
   - `README.md`: overview of all subject groups.
   - `manifest.json`: machine-readable group membership.
   - `<subject-slug>.md`: one subject-area index with pattern ids, titles, tags, source paths, and summaries.
   - `unclassified.md`: patterns that did not match the subject taxonomy strongly enough.

4. Refine only when needed.
   - If a group is too broad or too narrow, update `references/subject-taxonomy.md` first.
   - If pattern metadata is weak, fix the source pattern tags or summaries rather than hardcoding one-off grouping rules.

## Grouping Rules

- Group by subject matter, not by source book or folder.
- Allow one pattern to appear in multiple subject groups when it genuinely crosses concerns.
- Preserve source references by linking to the original pattern files.
- Do not rewrite pattern content.
- Keep generated group files concise enough for a later agent to load one subject at a time.

## Quality Checks

After grouping, verify:

```bash
python3 .agents/skills/pattern-subject-grouper/scripts/group_patterns.py \
  patterns \
  .agents/skills/infrastructure-as-code-patterns/references/patterns \
  --output ./work
```

Review group counts and inspect `unclassified.md`. A few unclassified patterns are acceptable; many means the taxonomy needs better keywords.

## Resources

- `scripts/group_patterns.py`: parses pattern files and writes subject-area group indexes.
- `references/subject-taxonomy.md`: default subject areas and keyword families.
