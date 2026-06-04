---
id: platform.pipeline-governance
title: Governance in the Delivery Path
type: governance-pattern
status: seed
summary: Enforce standards through automated checks, policy, review, and evidence
  inside the normal delivery workflow instead of after-the-fact inspection.
tags:
- platform-engineering
- governance
- policy-as-code
- delivery-pipeline
- security
- compliance
- auditability
- implementation-planning
- cloud-agnostic
aliases:
- pipeline governance
- policy as code
- guardrails
- shift left governance
applies_when:
- The user asks how to enforce architecture, security, compliance, cost, or reliability
  rules for infrastructure changes.
- Reviews happen too late, after systems are already deployed.
- Teams bypass governance because it is manual, slow, or unclear.
avoid_when:
- The rule requires human risk judgment that cannot be encoded safely.
- The pipeline cannot observe enough context to make the decision.
- Emergency break-glass action is needed and will be reviewed afterward.
related:
- platform.iac-delivery
- platform.drift-prevention
- platform.secrets-configuration-boundary
sources:
- 'iac2: Kief Morris, Infrastructure as Code, 2nd Edition, O''Reilly Media'
- synthesis: general platform governance and security engineering practice
source_confidence: medium
last_reviewed: 2026-06-04
subject_area: governance
---

# Governance in the Delivery Path

## Intent

Make governance fast, consistent, and auditable by embedding checks and evidence into the normal path for infrastructure delivery.

## Use when

- Teams need guardrails for infrastructure changes without a heavy manual approval process.
- Security, compliance, architecture, or cost standards are repeatedly discovered after deployment.
- The user asks about policy-as-code, review gates, platform guardrails, audit evidence, or shift-left governance.

## Avoid when

- The decision cannot be encoded with available context.
- The rule is experimental and should start as advisory before becoming blocking.
- A critical incident requires break-glass action.

## Context and problem

Governance fails when it is separate from delivery. Late review creates rework and encourages bypasses. Pipeline governance lets teams move quickly while producing evidence that standards were checked before and after apply.

## Forces

- Autonomy versus standardization: teams need self-service within safe boundaries.
- Blocking power versus false positives: strict checks can slow delivery if noisy.
- Central policy versus local context: one rule may not fit every workload.
- Evidence versus overhead: compliance proof should be generated as a side effect of delivery.

## Guidance

Move objective rules into automated checks. Use advisory mode before blocking mode. Keep human review for context-heavy decisions. Make exceptions explicit, time-bounded, and visible.

## Implementation moves

- Define standards as testable policies where possible.
- Run policy checks before plan, after plan, and after apply when appropriate.
- Separate advisory warnings from blocking failures.
- Require human approval only for high-risk changes or unresolved exceptions.
- Store evidence: code review, plan, policy results, approvals, apply logs, and post-deploy checks.
- Review exceptions and policy noise regularly.

## Checks

- Does the policy stop known bad changes before apply?
- Are exceptions visible, owned, and time-limited?
- Is policy feedback clear enough for teams to fix without a meeting?
- Are high-risk changes routed to humans with the right context?
- Does the pipeline produce audit evidence automatically?

## Failure modes

- Turning every rule into a blocking gate before teams trust it.
- Writing policies that are too generic to account for valid context.
- Manual approval theater where approvers lack useful evidence.
- Exceptions that become permanent undocumented architecture.
- Governance checks that can be bypassed by local applies.

## Agent trigger hints

Use this pattern when the user says or implies:

- policy as code
- platform guardrails
- governance pipeline
- architecture standards
- compliance evidence
- prevent insecure infrastructure
- approval gates

## Source notes

This is an original synthesis. Public book metadata and contents identify governance in pipeline-based workflows and team workflows as concerns; this file generalizes that into a reusable pattern.
