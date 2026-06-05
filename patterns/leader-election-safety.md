---
id: data.leader-election-safety
title: Leader Election Safety
type: architecture-pattern
status: draft
summary: Design leader election so only one effective leader can perform protected work at a time.
tags:
  - data-systems
  - coordination
  - leader-election
  - distributed-systems
  - runtime-operations
  - cloud-agnostic
aliases:
  - single leader safety
  - split brain prevention
  - leader lease
applies_when:
  - A cluster elects one node to perform writes, scheduling, partition ownership, or coordination.
  - Split-brain would create conflicting actions.
avoid_when:
  - The work is commutative and can safely run on multiple nodes.
  - The platform fully manages leadership and exposes sufficient fencing semantics.
related:
  - data.consensus-for-coordination
  - data.fencing-tokens
  - data.partial-failure-design
sources:
  - "book: Martin Kleppmann, Designing Data-Intensive Applications, first edition, data.pdf; Chapters 8 and 9"
source_confidence: high
last_reviewed: 2026-06-05
---

# Leader Election Safety

## Intent

Prevent duplicate leaders from corrupting state during pauses, partitions, or failover.

## Use when

- A cluster elects one node to perform writes, scheduling, partition ownership, or coordination.
- Split-brain would create conflicting actions.

## Avoid when

- The work is commutative and can safely run on multiple nodes.
- The platform fully manages leadership and exposes sufficient fencing semantics.

## Context and problem

Timeout-based failure detection can produce false suspicion. Without fencing, old leaders may continue acting after new leaders are elected.

## Forces

- Fast failover versus false leadership
- Availability versus exclusive ownership
- Simplicity versus fencing enforcement

## Guidance

Base leadership on a linearizable coordinator, short-lived sessions, and fencing tokens where protected resources need enforcement. Make leadership loss observable and fail closed.

## Implementation moves

- Acquire leadership through a consensus-backed primitive.
- Attach fencing tokens to protected writes.
- Stop work promptly on session loss.
- Test long pauses and network partitions.

## Checks

- Can two leaders write to the same resource?
- Does the resource reject stale leaders?
- How does the service behave during coordinator unavailability?

## Failure modes

- Assuming heartbeat timeout proves the old leader is dead.
- Failing open when leadership status is unknown.
- Using local clocks as the only lease authority.

## Agent trigger hints

Use this pattern when the user says or implies:

- leader election
- split brain
- leader lease
- stale leader

## Source notes

Synthesized from Chapters 8 and 9 in the locally extracted `data-chapters/` text. This file stores original guidance and source pointers only, not source excerpts.
