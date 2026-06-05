---
id: iac.version-controlled-infrastructure
title: Version Controlled Infrastructure
type: delivery-pattern
status: draft
summary: Store infrastructure code in version control to make changes traceable, reviewable, recoverable, and deliverable through pipelines.
tags:
  - infrastructure-as-code
  - version-control
  - delivery-pipeline
  - governance
  - safe-change
  - cloud-agnostic
aliases:
  - infrastructure repo
  - source control for infrastructure
  - gitops source
applies_when:
  - Infrastructure changes need review, audit, rollback, or promotion.
  - Multiple people or teams change the same infrastructure code.
avoid_when:
  - Generated artifacts are the only representation available and source intent is elsewhere.
  - The repository would include plaintext secrets.
related:
  - iac.define-everything-as-code
  - iac.pipeline-delivered-infrastructure
  - iac.secrets-out-of-source
sources:
  - "book: Kief Morris, Infrastructure as Code, second edition, iac2.pdf; Chapters 4, 18, and 19."
source_confidence: high
last_reviewed: 2026-06-04
---

# Version Controlled Infrastructure

## Intent

Use version control as the system of record for infrastructure intent and change history.

## Use when

- Infrastructure changes need review, audit, rollback, or promotion.
- Multiple people or teams change the same infrastructure code.

## Avoid when

- Generated artifacts are the only representation available and source intent is elsewhere.
- The repository would include plaintext secrets.

## Context and problem

Without version control, infrastructure changes are hard to audit, compare, review, or recover from.

## Forces

- Traceability versus speed of local edits
- Shared ownership versus coordination overhead
- Rollback intent versus external mutable state

## Guidance

Treat infrastructure code like production software. Require commits, reviews, history, branch or trunk policies, and automated pipeline execution from versioned sources.

## Implementation moves

- Create repositories around coherent infrastructure projects.
- Require pull requests or equivalent review for meaningful changes.
- Tag or package released versions used by pipelines.
- Connect commits to deployment evidence and operational events.

## Checks

- Can the team identify which commit changed a resource?
- Can a previous known-good version be reapplied or promoted?
- Are emergency changes reconciled into source quickly?

## Failure modes

- Changing live infrastructure and forgetting to update code.
- Committing generated noise that obscures intent.
- Assuming source rollback will reverse all external data or state changes.

## Agent trigger hints

Use this pattern when the user says or implies:

- put terraform in git
- audit infrastructure changes
- rollback infra code

## Source notes

Synthesized from Chapters 4, 18, and 19. Source confidence is high because the chapter text was extracted locally from the user-provided PDF. No source excerpts are stored here.
