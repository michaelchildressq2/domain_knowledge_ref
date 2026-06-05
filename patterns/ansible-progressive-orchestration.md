---
id: iac.ansible-progressive-orchestration
title: Ansible Progressive Orchestration
type: delivery-pattern
status: draft
summary: Use host patterns, serial batches, delegation, tags, blocks, and handlers to make multi-host Ansible changes staged, inspectable, and recoverable.
tags:
  - infrastructure-as-code
  - ansible
  - orchestration
  - progressive-delivery
  - runtime-operations
  - high-availability
  - delivery-pipeline
aliases:
  - ansible rolling update
  - serial ansible deployment
  - delegate_to
  - Ansible tags and handlers
applies_when:
  - A playbook changes multiple hosts, tiers, or shared services where order matters.
  - Downtime, partial failure, or blast radius must be controlled.
  - Operators need to run or skip selected portions during deployment and testing.
avoid_when:
  - The change is a single-host configuration update with no dependency ordering.
  - A higher-level deployment system already controls rollout batches and Ansible only handles one scoped host at a time.
related:
  - iac.progressive-feedback
  - iac.safe-infrastructure-change
  - iac.production-change-monitoring
  - iac.ansible-playbook-convergence
sources:
  - "book: Bas Meijer, Lorin Hochstein, and Rene Moser, Ansible: Up and Running, third edition; Chapters 1, 10, 11, 22, and 24."
source_confidence: high
last_reviewed: 2026-06-05
---

# Ansible Progressive Orchestration

## Intent

Coordinate multi-host changes in controlled increments so Ansible can update, verify, and recover services without treating the fleet as one undifferentiated target set.

## Use when

- Web, application, database, load balancer, network, or monitoring systems must change in a specific order.
- Hosts should be drained, updated, validated, and returned to service one batch at a time.
- Operators need tags to test or run specific parts of a playbook.
- Pre-tasks, post-tasks, handlers, and delegated tasks coordinate work outside the target host.
- A playbook should stop early when a batch fails.

## Avoid when

- Batching would add complexity without reducing risk.
- A blue/green, canary, or platform-native rollout controller already handles progressive change.
- The playbook uses shared mutable state that cannot tolerate partial completion.

## Context and problem

Ansible can run a task across many hosts, but production changes often require finer control. Services may need load balancer updates, database ordering, monitoring notifications, serial batches, handler timing, or delegated control-plane actions. Without explicit orchestration, a playbook can create avoidable downtime or leave half-updated systems.

The Ansible source covers host patterns, `--limit`, `serial`, `delegate_to`, pre- and post-tasks, blocks with rescue behavior, tags, and handlers. These mechanisms form a progressive-change pattern when used to reduce blast radius and preserve operator visibility.

## Forces

- Fleet-wide speed versus small-batch confidence.
- Task readability versus orchestration scaffolding.
- Local host work versus delegated control-plane changes.
- Automated rollback or rescue versus simpler failure visibility.
- Reusable roles versus playbook-specific rollout order.

## Guidance

Make rollout scope and order explicit. Use inventory host patterns and `--limit` to select targets deliberately. Use `serial` and failure thresholds for rolling updates. Use `delegate_to` and `run_once` for tasks that belong on a controller, load balancer, monitoring host, or API endpoint rather than the target host. Use tags to support focused runs and tests, but keep tags aligned with meaningful operational phases.

Use handlers, pre-tasks, post-tasks, and blocks to express lifecycle boundaries. Do not hide high-risk orchestration inside a role when operators need to see the rollout sequence.

## Implementation moves

- Define host patterns and environment limits before running production plays.
- Add `serial` for rolling changes where updating all hosts at once is unsafe.
- Use `max_fail_percentage` or explicit assertions to stop unsafe batches.
- Delegate load balancer, DNS, monitoring, or cloud-control tasks to the correct control host or localhost.
- Use `run_once` for singleton coordination steps.
- Add tags for install, configure, test, deploy, rollback, or unit-test phases when those phases are useful.
- Use pre-tasks and post-tasks for lifecycle actions around the main role execution.
- Flush or structure handlers when restart timing matters.

## Checks

- Can an operator identify the exact host set and batch size before execution?
- Are delegated tasks clearly marked and scoped?
- Does the playbook stop before a failed batch damages the whole fleet?
- Are tags documented and aligned with useful execution phases?
- Do handlers run at a safe point for the deployment flow?
- Are pre- and post-tasks visible rather than hidden in unrelated roles?

## Failure modes

- Running a multi-tier change against `all` without limits or staging.
- Delegating control-plane tasks accidentally to every target host.
- Using tags so inconsistently that partial runs skip required prerequisites.
- Restarting every service at the end because handlers were notified by false changes.
- Hiding rolling-update sequencing inside a role that consumers cannot inspect.

## Agent trigger hints

Use this pattern when the user says or implies:

- Ansible rolling update
- serial playbook
- delegate_to localhost
- run Ansible against part of inventory
- Ansible tags
- pre_tasks post_tasks handlers

## Source notes

Synthesized from Ansible: Up and Running, third edition, especially Chapter 1 on orchestration, Chapter 10 on complex playbooks and blocks, Chapter 11 on host patterns, delegation, serial runs, and handlers, Chapter 22 on CI/CD rollout flow, and Chapter 24 on tags and rolling updates. No source excerpts are stored here.
