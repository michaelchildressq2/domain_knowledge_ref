---
id: platform.iac-delivery
title: Infrastructure Delivery Through Versioned Pipelines
type: delivery-pattern
status: seed
summary: Treat infrastructure changes as versioned work that is reviewed, tested,
  planned, applied, and observed through a controlled delivery path.
tags:
- platform-engineering
- infrastructure-as-code
- delivery-pipeline
- version-control
- testing
- reproducibility
- drift-prevention
- governance
- implementation-planning
- cloud-agnostic
aliases:
- iac pipeline
- infrastructure ci cd
- pipeline based infrastructure delivery
- continuous delivery for infrastructure
applies_when:
- Infrastructure is being changed by code, scripts, modules, or provider templates.
- The user asks how to review, test, plan, apply, or govern infrastructure changes.
- Manual console changes or workstation applies cause drift and inconsistent environments.
avoid_when:
- The infrastructure is temporary experimentation with no shared or production impact.
- Provider control-plane limits make automation unsafe without additional guardrails.
- Emergency response requires break-glass action before the pipeline can be fixed.
related:
- platform.pipeline-governance
- platform.drift-prevention
- platform.safe-infrastructure-change
sources:
- 'iac2: Kief Morris, Infrastructure as Code, 2nd Edition, O''Reilly Media'
- synthesis: general devops and infrastructure-as-code practice
source_confidence: medium
last_reviewed: 2026-06-04
subject_area: infrastructure-as-code
---

# Infrastructure Delivery Through Versioned Pipelines

## Intent

Make infrastructure change safe and repeatable by moving it through a versioned, reviewed, tested, automated delivery path.

## Use when

- Teams apply infrastructure from local machines, consoles, or undocumented scripts.
- Environments drift because changes are not captured in version control.
- The user asks how to structure infrastructure repositories, CI/CD, plans, approvals, tests, or promotion across environments.

## Avoid when

- The change is an emergency break-glass fix. Capture and reconcile it afterward.
- The platform cannot safely automate the change without missing permissions, state, or dependency discovery.
- A one-off sandbox is intentionally outside the managed estate.

## Context and problem

Infrastructure code does not produce consistent systems by itself. Consistency comes from how code is reviewed, tested, parameterized, applied, and reconciled with real infrastructure. A pipeline also creates an audit trail and a place to attach governance checks.

## Forces

- Speed versus control: too many gates slow change; too few gates allow unsafe changes.
- Local autonomy versus shared reliability: teams need self-service without bypassing standards.
- Plan accuracy versus runtime uncertainty: provider state can change between plan and apply.
- Reuse versus coupling: shared modules reduce duplication but can spread breaking changes.

## Guidance

Use version control as the source for intended infrastructure state and use pipelines as the normal path to apply changes. Make the pipeline responsible for validation, planning, policy checks, approval where needed, apply, and post-apply verification.

## Implementation moves

- Put infrastructure code, module versions, configuration values, and pipeline definitions under version control.
- Require review for production-affecting changes.
- Run linting, formatting, static checks, security checks, and policy-as-code before apply.
- Generate a plan or preview and make risky changes visible.
- Apply from a controlled identity with scoped permissions.
- Store state and artifacts in durable, access-controlled locations.
- Run post-apply checks and drift detection.

## Checks

- Can any production infrastructure be changed outside the pipeline without detection?
- Are module versions pinned and reviewed before promotion?
- Does the plan show deletions, replacements, and permission changes clearly?
- Are secrets excluded from logs and artifacts?
- Is the applied result observed after the pipeline finishes?

## Failure modes

- Treating the pipeline as a wrapper around unreviewed local scripts.
- Applying plans long after they were generated.
- Sharing one overprivileged pipeline identity across unrelated blast radii.
- Storing secrets in state, logs, or artifacts.
- Assuming a successful apply means the service is healthy.

## Agent trigger hints

Use this pattern when the user says or implies:

- infrastructure ci cd
- terraform pipeline
- apply from local machine
- plan and apply governance
- review infrastructure changes
- automate infrastructure delivery

## Source notes

This is an original synthesis from public infrastructure-as-code themes and general platform delivery practice. It aligns with public metadata about defining infrastructure as code and continuously testing and delivering infrastructure work.
