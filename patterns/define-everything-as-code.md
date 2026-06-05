---
id: iac.define-everything-as-code
title: Define Everything As Code
type: delivery-pattern
status: draft
summary: Define infrastructure, configuration, policies, and operational workflows as versioned code where they affect repeatability or change safety.
tags:
  - infrastructure-as-code
  - version-control
  - reproducibility
  - governance
  - implementation-planning
  - cloud-agnostic
aliases:
  - everything as code
  - infrastructure definitions
  - coded operations
applies_when:
  - A system cannot be reliably rebuilt from known inputs.
  - Operational changes depend on undocumented manual steps.
avoid_when:
  - A one-time exploratory action has not yet revealed stable intent.
  - The item is a secret value that should be referenced, not stored in source.
related:
  - iac.version-controlled-infrastructure
  - iac.secrets-out-of-source
  - iac.repeatable-processes
sources:
  - "book: Kief Morris, Infrastructure as Code, second edition, iac2.pdf; Chapters 1 and 4."
source_confidence: high
last_reviewed: 2026-06-04
---

# Define Everything As Code

## Intent

Make important system state reviewable, testable, repeatable, and recoverable by expressing it as code.

## Use when

- A system cannot be reliably rebuilt from known inputs.
- Operational changes depend on undocumented manual steps.

## Avoid when

- A one-time exploratory action has not yet revealed stable intent.
- The item is a secret value that should be referenced, not stored in source.

## Context and problem

Manual infrastructure state hides intent and makes recovery, audit, and safe change difficult.

## Forces

- Explicit intent versus up-front effort
- Auditability versus local convenience
- Repeatability versus ad hoc operations

## Guidance

Capture desired state and operational workflows in source-controlled code. Include enough of the system to rebuild, review, test, and understand it, while externalizing secrets and runtime-specific values.

## Implementation moves

- Identify infrastructure, runtime, policy, and delivery activities that affect production behavior.
- Move repeatable definitions into code projects with review and history.
- Represent environment differences as simple parameters or registries.
- Automate application of the code through pipelines.

## Checks

- Could a new environment be rebuilt from source and approved inputs?
- Can reviewers see what infrastructure behavior changed?
- Are manual steps either removed or tracked as technical debt?

## Failure modes

- Only coding resource creation while leaving delivery and operations manual.
- Putting secret values directly in repositories.
- Using generated code that humans cannot review.

## Agent trigger hints

Use this pattern when the user says or implies:

- define as code
- manual infrastructure
- version infrastructure
- rebuild environment

## Source notes

Synthesized from Chapters 1 and 4. Source confidence is high because the chapter text was extracted locally from the user-provided PDF. No source excerpts are stored here.
