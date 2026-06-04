# Pattern Files

Pattern files are reusable agent guidance. They are not summaries. Each file should help a future agent decide whether a concept applies, how to apply it, what tradeoffs to consider, and what related patterns to inspect.

## Folder rule

Store each pattern under the subject folder where a future agent is most likely to look first:

```text
patterns/reliability/high-availability.md
patterns/data/data-consistency.md
patterns/infrastructure-as-code/modular-stack-boundaries.md
patterns/governance/pipeline-governance.md
patterns/security/secrets-configuration-boundary.md
patterns/operations/runbook-feedback.md
```

If a pattern spans subjects, choose the primary folder and add tags plus `related` links for the secondary subjects.

## Required pattern template

```markdown
---
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
---

# Example Pattern Title

## Intent

State the durable design intention in one short paragraph.

## Use when

- List practical triggers.

## Avoid when

- List contexts where the pattern is wrong or risky.

## Context and problem

Describe the recurring situation this pattern solves.

## Forces

- Explain tradeoffs and tensions.

## Guidance

Give the core advice in original language.

## Implementation moves

- Provide concrete moves an agent can recommend or execute.

## Checks

- Provide review questions.

## Failure modes

- Describe ways this pattern is commonly misapplied.

## Agent trigger hints

Use this pattern when the user says or implies:

- example trigger phrase

## Source notes

Explain source lineage and confidence. Do not include long quotes or chapter recaps.
```
