---
id: data.partial-failure-design
title: Partial Failure Design
type: architecture-pattern
status: draft
summary: Design distributed systems assuming some components can be slow, unreachable, or mistaken while others continue running.
tags:
  - data-systems
  - distributed-systems
  - reliability
  - failure-modes
  - design-review
  - cloud-agnostic
aliases:
  - partial failure
  - distributed systems faults
  - network failure design
applies_when:
  - A system spans multiple processes, machines, zones, or networks.
  - The design assumes failures are obvious or all-or-nothing.
avoid_when:
  - The component is truly single-process and local, with no network or distributed state.
  - A managed platform hides the distribution and provides the required guarantees.
related:
  - data.timeout-retry-backoff
  - data.fencing-tokens
  - data.consensus-for-coordination
sources:
  - "book: Martin Kleppmann, Designing Data-Intensive Applications, first edition, data.pdf; Chapter 8: The Trouble with Distributed Systems"
source_confidence: high
last_reviewed: 2026-06-05
---

# Partial Failure Design

## Intent

Prevent distributed designs from relying on impossible certainty about remote components.

## Use when

- A system spans multiple processes, machines, zones, or networks.
- The design assumes failures are obvious or all-or-nothing.

## Avoid when

- The component is truly single-process and local, with no network or distributed state.
- A managed platform hides the distribution and provides the required guarantees.

## Context and problem

In distributed systems, messages can be delayed, lost, duplicated, reordered, or processed by nodes whose status is uncertain.

## Forces

- Availability versus certainty
- Timeout speed versus false suspicion
- Automation versus ambiguity

## Guidance

Treat remote state as uncertain. Use timeouts, retries, idempotency, leases, fencing, quorum, and explicit failure semantics rather than assuming a node is simply alive or dead.

## Implementation moves

- Identify every network boundary and remote dependency.
- Define timeout, retry, and idempotency behavior.
- Avoid correctness that depends on detecting failure perfectly.
- Use consensus or fencing for decisions requiring exclusive ownership.

## Checks

- What happens if the request succeeded but the response was lost?
- Can two nodes believe they own the same role?
- Are retries safe under duplicate execution?

## Failure modes

- Using timeout as proof of failure.
- Assuming clocks are perfectly synchronized.
- Ignoring slow or paused processes.

## Agent trigger hints

Use this pattern when the user says or implies:

- partial failure
- distributed system failure
- network timeout
- node failed or slow

## Source notes

Synthesized from Chapter 8: The Trouble with Distributed Systems in the locally extracted `data-chapters/` text. This file stores original guidance and source pointers only, not source excerpts.
