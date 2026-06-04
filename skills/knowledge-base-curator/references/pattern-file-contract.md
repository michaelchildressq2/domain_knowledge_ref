# Pattern File Contract

Every pattern file must contain YAML frontmatter followed by required sections.

## Required frontmatter

```yaml
id: platform.example-pattern
title: Example Pattern Title
type: architecture-pattern
status: draft
subject_area: reliability
summary: One sentence describing what the pattern helps an agent do.
tags:
  - platform-engineering
  - reliability
  - design-review
  - cloud-agnostic
aliases:
  - alternate phrase
applies_when:
  - The user asks for a decision or design that matches this pattern.
avoid_when:
  - The pattern would create more risk, cost, or complexity than value.
related:
  - platform.related-pattern
sources:
  - iac2: Kief Morris, Infrastructure as Code, 2nd Edition, O'Reilly Media
source_confidence: medium
last_reviewed: 2026-06-04
```

## Required body headings

Use these headings exactly:

```markdown
# Pattern Title

## Intent
## Use when
## Avoid when
## Context and problem
## Forces
## Guidance
## Implementation moves
## Checks
## Failure modes
## Agent trigger hints
## Source notes
```

## Quality bar

A strong pattern gives future agents:

- applicability triggers
- avoid conditions
- tradeoffs
- implementation moves
- review questions
- failure modes
- related patterns
- source lineage

A weak pattern merely summarizes a source.
