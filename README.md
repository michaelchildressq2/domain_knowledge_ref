# Knowledge Base Skill Repository

This repository is a git-native knowledge base for reusable agent guidance. It is designed for platform engineering, architecture, SRE, infrastructure-as-code, governance, security, data, and operations patterns derived from readings, project experience, and internal standards.

The goal is **not** to summarize books chapter by chapter. The goal is to convert learning into concise, attributable, reusable pattern files that agents can discover and apply when solving future engineering problems.

## Core principles

1. **Subject-first organization**: pattern files live under `patterns/<subject-area>/`, not under source or chapter folders.
2. **Attribution without copying**: each pattern records source lineage, but pattern bodies must be original synthesis, not reproduced source expression.
3. **Agent-discoverable tags**: every pattern includes tags, aliases, applicable contexts, avoid contexts, related pattern IDs, and trigger hints.
4. **Cross-linking by scan**: agents must inspect existing patterns before adding new ones, then update tags and `related` links when concepts overlap.
5. **Validation before commit**: scripts enforce required metadata, subject-folder placement, link integrity, and basic anti-copying hygiene.
6. **Local raw-source handling**: PDFs, EPUBs, notes, and raw extracts stay in `intake/` or `work/` and are ignored by git unless explicitly approved.

## Repository layout

```text
.
├── AGENTS.md                         # rules every agent must follow in this repo
├── Makefile                          # common validation/index commands
├── config/
│   ├── repo_policy.yml               # repository rules and review gates
│   ├── subjects.yml                  # subject-area folders and default tags
│   └── taxonomy.yml                  # canonical tag families
├── docker/
│   ├── Dockerfile                    # sandbox image for parsing and validation
│   └── compose.yaml                  # bind-mount repo into the sandbox
├── intake/
│   └── raw/                          # local-only source documents; gitignored
├── loops/
│   ├── extract-patterns/RALPH.md     # loop for turning source material into patterns
│   ├── tag-enrichment/RALPH.md       # loop for cross-linking and tag cleanup
│   └── curator-review/RALPH.md       # loop for review, attribution, and quality gates
├── patterns/
│   ├── reliability/
│   ├── data/
│   ├── infrastructure-as-code/
│   ├── governance/
│   ├── security/
│   └── operations/
├── scripts/
│   ├── build_index.py
│   ├── enrich_related_tags.py
│   ├── extract_source_text.py
│   ├── new_pattern.py
│   └── validate_patterns.py
├── skills/
│   └── knowledge-base-curator/        # optional ChatGPT skill for using this repo
├── sources/
│   └── manifest.yml                  # source bibliography and rights notes
└── work/                              # generated extracts, suggestions, indexes; gitignored
```

## Basic workflow

### 1. Register the source

Add a record in `sources/manifest.yml` before extracting patterns from a book, paper, talk, internal memo, or production incident.

Each source should include:

- stable `id`
- title, authors, publisher or venue
- source type
- acquisition or access note
- rights note
- allowed use for this repository
- citation label to use in pattern metadata

### 2. Extract source text locally

Put lawful local copies in `intake/raw/`. Do not commit raw documents.

```bash
python scripts/extract_source_text.py \
  --source-id iac2 \
  --input intake/raw/infrastructure-as-code-2e.pdf \
  --out work/extracts/iac2
```

This writes local working chunks under `work/extracts/`. These chunks are for agent analysis only and should not be committed.

### 3. Create or update subject-area patterns

Create a new pattern stub:

```bash
python scripts/new_pattern.py \
  --subject reliability \
  --id platform.high-availability \
  --title "High Availability by Failure Domain Design" \
  --source iac2
```

Then fill in the pattern using `patterns/README.md` and `config/taxonomy.yml`.

### 4. Enrich tags and related links

Run a scan before committing:

```bash
python scripts/enrich_related_tags.py --suggest
```

To let the script add high-confidence missing tags and reciprocal `related` links:

```bash
python scripts/enrich_related_tags.py --write
```

Agents should still inspect the diff before committing.

### 5. Validate and index

```bash
make validate
make index
```

The generated index goes into `work/index/` by default and can be published separately if desired.

## Docker sandbox

Build and enter the sandbox:

```bash
docker compose -f docker/compose.yaml build
docker compose -f docker/compose.yaml run --rm kb-agent
```

Inside the container:

```bash
make validate
python scripts/enrich_related_tags.py --suggest
```

## Ralph loop usage

This repo includes `RALPH.md` packages under `loops/`. A compatible Ralph runtime can use them directly. The loop packages are deliberately plain markdown plus validation commands, so they also work as agent instructions if copied into another orchestrator.

Use GitHub Issues as the Ralph task queue. Before starting a Ralph loop, break broad requests into individual issues following `docs/agents/issue-tracker.md`; each issue should describe one bounded pattern, tag-enrichment, review, validation, or repo-hygiene task.

Suggested loop sequence:

1. `loops/extract-patterns/` creates or updates pattern files from registered sources.
2. `loops/tag-enrichment/` scans the full pattern set and improves tags and `related` links.
3. `loops/curator-review/` performs source, quality, and duplication review before PR/merge.

## Source-use guardrails

This repo is for concept extraction, synthesis, and attribution. It is not a substitute distribution channel for source material.

Allowed outputs:

- Original pattern guidance in the repository's own language.
- Short labels, source IDs, citations, and public bibliographic facts.
- Brief quotations only when necessary and within your organization's policy.
- Generalized checklists, decision criteria, and implementation moves.

Disallowed outputs:

- Chapter-by-chapter recaps that reconstruct the source.
- Long quotations or close paraphrases of source expression.
- Bulk extracted text committed to git.
- Pattern files that present source-specific examples as if they were original internal designs.

Consult counsel for your organization-specific copyright, license, and fair-use posture.
