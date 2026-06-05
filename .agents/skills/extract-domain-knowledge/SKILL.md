---
name: extract-domain-knowledge
description: Ingest PDFs, books, reports, or already-extracted chapter text into the local domain_knowledge_ref knowledge base by extracting chapters, synthesizing reusable pattern markdown files, merging them into patterns/, and regenerating subject-groups/. Use when asked to add source material to the domain knowledge corpus, run the PDF-to-pattern pipeline, or update the local pattern reference from a document.
---

# Extract Domain Knowledge

Use this skill to turn source material into the repository's local pattern corpus. It coordinates the repo-local extraction skills rather than replacing them.

## Repository Target

1. Prefer the current repository when it contains `.agents/skills`, `patterns/`, or `subject-groups/`.
2. Otherwise look for `/Users/mchildress/personal-knowledge/Books/InfrastructureAsCode/domain_knowledge_ref`.
3. If the repo is not present locally, clone `https://github.com/michaelchildressq2/domain_knowledge_ref` before starting.
4. Resolve all relative paths from the repository root.

## Inputs And Defaults

- Input PDF default output: `work/book-<source-slug>/chapter-out/`.
- Existing chapter folder input: a folder containing `context.txt`, `full-text.txt`, and `chapter-*.txt`.
- Pattern output folder: `patterns/`.
- Subject-group output folder: `subject-groups/`.
- Scratch and review output: `work/`.

Keep raw extracted text and intermediate indexes under `work/`. Do not move full chapter text into tracked reference folders.

## Workflow

1. Inspect the source and current corpus.
   - Identify whether the input is a PDF or an existing chapter folder.
   - Run `git status --short` and note unrelated user changes without reverting them.
   - Inspect `patterns/` and `subject-groups/README.md` so new patterns fit the existing corpus.

2. Extract chapter text when the input is a PDF.
   - Use `$pdf-chapter-text-extractor`.
   - Prefer Docker from the repo root:

```bash
docker build -t pdf-chapter-text-extractor .agents/skills/pdf-chapter-text-extractor
docker run --rm -v "$PWD:/work" pdf-chapter-text-extractor path/to/source.pdf --output-dir work/book-source-slug/chapter-out
```

   - If Docker is unavailable, use the host Python fallback:

```bash
python3 .agents/skills/pdf-chapter-text-extractor/scripts/pdf_to_chapters.py path/to/source.pdf --output-dir work/book-source-slug/chapter-out
```

   - Inspect `context.txt` and several chapter files. Stop and report if the PDF is scanned/image-only or the chapter split is unusable.

3. Build extraction signals from the chapter folder.
   - Use `$chapter-pattern-extractor`.
   - Run the candidate index script:

```bash
python3 .agents/skills/chapter-pattern-extractor/scripts/build_candidate_index.py work/book-source-slug/chapter-out
```

   - Read candidates by chapter or part. Do not load the entire book into context unless it is small enough and necessary.

4. Synthesize or merge pattern files.
   - Write standalone pattern markdown into `patterns/` unless the user asked for a review-only output.
   - Generate original synthesis, not chapter summaries.
   - Include pattern frontmatter with `id`, `title`, `type`, `summary`, `tags`, `aliases`, `applies_when`, `avoid_when`, `related`, `sources`, `source_confidence`, and `last_reviewed`.
   - Use a stable id prefix based on the source or domain, such as `iac.`, `data.`, or another short source-specific prefix already present in the corpus.
   - Before adding a new file, search for overlapping existing patterns. Merge or extend an existing pattern when the intent, forces, guidance, and failure modes are substantially the same.
   - Preserve existing source notes when extending a pattern, and add the new source pointer instead of replacing prior provenance.
   - Avoid long quotations from source text. Store chapter, section, or page pointers in `## Source notes`.

5. Validate pattern files.

```bash
python3 .agents/skills/chapter-pattern-extractor/scripts/validate_pattern_output.py patterns
```

   - If `.agents/skills/pattern-library-builder/scripts/validate_patterns.py` exists, run it too.
   - Fix missing required headings, weak tags, duplicate ids, or source-note problems before continuing.

6. Regenerate subject groups.
   - First create a candidate grouping for review:

```bash
python3 .agents/skills/pattern-subject-grouper/scripts/group_patterns.py patterns --output work/subject-groups-candidate
```

   - Inspect `work/subject-groups-candidate/README.md`, `manifest.json`, and `unclassified.md` when present.
   - If many relevant patterns are unclassified, improve pattern tags or the grouper taxonomy before publishing the groups.
   - After review, regenerate the tracked subject groups:

```bash
python3 .agents/skills/pattern-subject-grouper/scripts/group_patterns.py patterns --output subject-groups
```

7. Final verification.
   - Re-run pattern validation after any fixes.
   - Review `git diff --stat` and the changed pattern and subject-group files.
   - Confirm raw extracted text remains under `work/`.
   - Summarize added or merged patterns, subject-group changes, validation results, and any source limitations.

## Quality Rules

- Prefer the bundled extractor and grouper scripts over ad hoc parsing or grouping.
- Do not delete or rewrite unrelated corpus files.
- Do not commit or publish full copyrighted source text unless the user explicitly approves.
- Treat extracted PDF text as evidence to synthesize from, not as final knowledge-base content.
- Favor fewer, stronger patterns over shallow one-chapter summaries, but do not ignore distinct, defensible patterns.
- Keep every pattern actionable: include use/avoid conditions, forces, implementation moves, checks, failure modes, trigger hints, and source notes.
- Make the corpus useful for `$domain-knowledge-check`: use searchable tags, likely user terms, and concrete summaries.
