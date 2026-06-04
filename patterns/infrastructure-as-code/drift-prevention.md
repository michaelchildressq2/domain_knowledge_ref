---
id: platform.drift-prevention
title: Drift Prevention Through Reconciliation
type: governance-pattern
status: seed
summary: Prevent unmanaged infrastructure changes by making intended state visible,
  continuously checked, and reconciled through the normal delivery path.
tags:
- platform-engineering
- infrastructure-as-code
- drift-prevention
- governance
- reproducibility
- version-control
- policy-as-code
- runtime-operations
- cloud-agnostic
aliases:
- configuration drift
- unmanaged change
- drift detection
- reconcile infrastructure
applies_when:
- Actual infrastructure differs from code or approved configuration.
- Teams make console changes that are not captured in version control.
- The user asks how to detect, prevent, or reconcile drift.
avoid_when:
- The resource is intentionally unmanaged or externally controlled.
- Drift is caused by expected runtime autoscaling or provider-managed mutation.
- The immediate need is emergency mitigation; reconcile after stabilization.
related:
- platform.iac-delivery
- platform.environment-parity
- platform.pipeline-governance
sources:
- 'iac2: Kief Morris, Infrastructure as Code, 2nd Edition, O''Reilly Media'
- synthesis: general infrastructure-as-code and operations practice
source_confidence: medium
last_reviewed: 2026-06-04
subject_area: infrastructure-as-code
---

# Drift Prevention Through Reconciliation

## Intent

Keep the real platform aligned with intended state so infrastructure remains reproducible, reviewable, and safe to change.

## Use when

- The user mentions configuration drift, snowflakes, manual fixes, console changes, or unknown production state.
- Infrastructure code no longer matches deployed resources.
- Rebuilds fail because undocumented changes exist in live environments.

## Avoid when

- The resource is intentionally outside management and clearly documented.
- Provider-managed fields change normally and should be ignored or modeled correctly.
- The system is in active incident response and needs stabilization first.

## Context and problem

Infrastructure code loses value when real systems drift from intended state. Drift hides risk until the next apply, rebuild, or disaster recovery exercise. Agents should distinguish harmful drift from expected runtime change and recommend a reconciliation loop.

## Forces

- Control versus flexibility: teams need emergency action without making unmanaged change normal.
- Accuracy versus noise: drift detection must ignore expected provider-managed differences.
- Prevention versus recovery: preventing manual changes is not enough; existing drift must be reconciled.
- Governance versus flow: controls should not force teams to bypass the system.

## Guidance

Make the pipeline the normal path for infrastructure change and add a drift loop: detect, classify, reconcile, and improve controls. Emergency changes should be captured back into code or reverted quickly.

## Implementation moves

- Define which resources are managed by infrastructure code and which are external.
- Restrict direct mutation access for managed resources where possible.
- Run periodic plan, preview, or drift-detection jobs.
- Classify drift as expected provider mutation, emergency change, unauthorized change, or code mismatch.
- Reconcile by updating code, importing state, reverting the resource, or documenting an unmanaged exception.
- Track drift as operational debt and review repeated causes.

## Checks

- Can the team identify all unmanaged production changes from the last month?
- Would the next apply destroy or replace unexpected resources?
- Are emergency changes captured back into the delivery path?
- Are ignored fields documented and limited?
- Does access control make bypassing the pipeline exceptional?

## Failure modes

- Running drift detection but never reconciling findings.
- Ignoring broad sets of fields to make plans quiet.
- Blocking all manual change without providing an emergency path.
- Importing resources without understanding ownership or lifecycle.
- Treating autoscaling or provider-managed updates as harmful drift.

## Agent trigger hints

Use this pattern when the user says or implies:

- configuration drift
- someone changed it in the console
- snowflake server
- terraform plan has unexpected changes
- reconcile state
- prevent manual infrastructure changes

## Source notes

This is an original synthesis. Public book metadata and contents identify reproducibility, variation minimization, configuration drift, version control, and continuous delivery as core infrastructure-as-code concerns.
