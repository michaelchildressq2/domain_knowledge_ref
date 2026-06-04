---
id: platform.safe-infrastructure-change
title: Safe Infrastructure Change by Small Reversible Steps
type: delivery-pattern
status: seed
summary: Reduce outage risk by decomposing infrastructure change into small, observable,
  compatible steps with explicit recovery paths.
tags:
- platform-engineering
- infrastructure-as-code
- safe-change
- zero-downtime
- rollback
- roll-forward
- blast-radius
- delivery-pipeline
- design-review
- cloud-agnostic
aliases:
- safe change
- zero downtime change
- infrastructure refactoring
- reduce blast radius
applies_when:
- The user asks how to change live infrastructure safely.
- A planned change replaces, renames, moves, or refactors resources that serve production
  traffic.
- The change could affect availability, data continuity, identity, network paths,
  or deployment flow.
avoid_when:
- The system is disposable and a rebuild is cheaper than controlled migration.
- A full outage window is approved and simpler.
- The risk comes from an unknown incident rather than a planned change.
related:
- platform.iac-delivery
- platform.data-continuity-during-change
- platform.high-availability
sources:
- 'iac2: Kief Morris, Infrastructure as Code, 2nd Edition, O''Reilly Media'
- synthesis: general continuous delivery and reliability practice
source_confidence: medium
last_reviewed: 2026-06-04
subject_area: governance
---

# Safe Infrastructure Change by Small Reversible Steps

## Intent

Change live infrastructure without surprising users or operators. Make each step understandable, observable, and recoverable.

## Use when

- Infrastructure code refactoring could replace or delete live resources.
- A migration touches networking, identity, storage, databases, or shared platform components.
- The user asks about zero downtime, rollback, canary, blue-green, parallel run, or blast radius.

## Avoid when

- A controlled full outage is cheaper and acceptable.
- The system is ephemeral and can be recreated without user impact.
- The current emergency requires immediate mitigation before a safe-change sequence can be designed.

## Context and problem

Infrastructure tools can plan and apply large changes quickly. That speed is dangerous when a refactor changes resource identity, dependency ordering, or replacement behavior. Agents should slow down risky changes by breaking them into verified transitions.

## Forces

- Speed versus safety: smaller steps add time but reduce surprise.
- Reversibility versus progress: some changes become irreversible after data or traffic moves.
- Automation versus judgment: plans show mechanics, but humans still need to understand impact.
- Parallel operation versus cost: running old and new paths together costs more but reduces cutover risk.

## Guidance

Reduce scope before applying. Decompose the change into compatibility, parallelization, traffic shift, verification, and cleanup phases. Prefer recovery through roll-forward when rollback would corrupt data or recreate old failure modes.

## Implementation moves

- Identify resource replacements, deletions, renames, permission changes, and dependency changes in the plan.
- Split refactoring from behavior change.
- Add new infrastructure beside old infrastructure before removing old paths.
- Use feature flags, weighted routing, canaries, or blue-green strategies where appropriate.
- Define rollback and roll-forward decision points before starting.
- Watch user-level metrics, dependency health, errors, latency, and saturation during rollout.
- Clean up only after a verification window.

## Checks

- What is the smallest safe unit of change?
- What would make this change irreversible?
- Is the old path still available until the new path is proven?
- Do metrics prove user capability, not just resource creation?
- Is the cleanup step separate from the cutover step?

## Failure modes

- Combining refactor, version upgrade, policy change, and data migration in one apply.
- Trusting a successful infrastructure apply as proof of service health.
- Rolling back code after data has moved into a new incompatible shape.
- Cleaning up old resources before traffic and data behavior are verified.
- Ignoring hidden dependencies such as DNS TTLs, caches, certs, or firewall rules.

## Agent trigger hints

Use this pattern when the user says or implies:

- how do we change this safely
- zero downtime infrastructure change
- terraform wants to replace this resource
- reduce blast radius
- canary infrastructure change
- rollback plan
- refactor infrastructure code

## Source notes

This is an original synthesis. Public book metadata and contents identify safe infrastructure change, small changes, zero downtime, continuity, and recovery as concerns; this pattern turns them into general agent guidance.
