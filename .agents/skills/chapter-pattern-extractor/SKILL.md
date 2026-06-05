---
name: chapter-pattern-extractor
description: Extract reusable agent guidance pattern markdown files, anti-patterns, principles, practices, pitfalls, trade-offs, and decision guides from chapter text folders such as pdf-chapter-text-extractor output into a local output folder.
metadata:
  tags:
    - pattern-extraction
    - chapter-analysis
    - platform-engineering
---

# Chapter Pattern Extractor

Use this skill to convert chapter text into standalone pattern markdown files. Prefer synthesis over summary: the output should help a later agent make decisions, critique designs, and plan implementations. Do not generate a complete skill package unless the user explicitly asks for one.

## Workflow

1. Intake the chapter folder.
   - Expected inputs include `context.txt`, `full-text.txt`, and `chapter-NNN-<slug>.txt`.
   - Use `context.txt` for title, source, page count, and detected chapter boundaries.
   - Do not store raw source excerpts in the generated pattern files.

2. Build a candidate index.

```bash
python3 .agents/skills/chapter-pattern-extractor/scripts/build_candidate_index.py path/to/book-chapters --output ./pattern-work
```

3. Extract and normalize patterns.
   - Read candidates by chapter or part, not all source text at once.
   - Extract recurring problems, principles, practices, anti-patterns, trade-offs, implementation moves, checks, and failure modes.
   - Merge duplicates across chapters when the problem, forces, guidance, and trigger conditions are substantially the same.
   - Split candidates when the trigger conditions or failure modes are different.

4. Write pattern files into an output folder where the skill is run.
   - Default output folder: `./patterns/`.
   - Write one markdown file per normalized pattern, using lowercase kebab-case filenames.
   - Each file should match the `pattern-library-builder` pattern template.
   - Put key concept tags in each pattern file's frontmatter.
   - Do not create `SKILL.md`, `agents/openai.yaml`, `references/index.md`, `references/tags.md`, or `references/source-map.md` unless explicitly requested.

5. Validate.

```bash
python3 .agents/skills/pattern-library-builder/scripts/validate_patterns.py ./patterns
python3 .agents/skills/chapter-pattern-extractor/scripts/validate_pattern_output.py ./patterns
```

## Pattern Requirements

Use the `pattern-library-builder` pattern template and taxonomy. Required pattern body sections are:

- `## Intent`
- `## Use when`
- `## Avoid when`
- `## Context and problem`
- `## Forces`
- `## Guidance`
- `## Implementation moves`
- `## Checks`
- `## Failure modes`
- `## Agent trigger hints`
- `## Source notes`

## Quality Rules

- Generate original synthesis, not chapter summaries.
- Keep source references as chapter, section, or page pointers.
- Do not copy long passages from copyrighted material.
- Prefer 80-180 lines per pattern.
- Every pattern must include actionable checks and clear avoid conditions.
- Every pattern must include discovery tags that match likely user language.

## Resources

- `scripts/build_candidate_index.py`: scans chapter files for headings and signal phrases.
- `scripts/validate_pattern_output.py`: validates a folder of generated pattern markdown files.
