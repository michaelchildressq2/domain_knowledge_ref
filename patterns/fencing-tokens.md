---
id: data.fencing-tokens
title: Fencing Tokens
type: architecture-pattern
status: draft
summary: Use monotonically increasing fencing tokens to prevent stale leaders or lock holders from corrupting shared resources.
tags:
  - data-systems
  - distributed-systems
  - coordination
  - consistency
  - runtime-operations
  - cloud-agnostic
aliases:
  - fencing token
  - stale lock holder
  - lease fencing
applies_when:
  - A process obtains a lease or lock before writing to shared storage or controlling a resource.
  - A paused or partitioned process might continue acting after its lease expired.
avoid_when:
  - The resource itself provides linearizable conditional writes that already reject stale actors.
  - The operation is read-only or harmless if duplicated.
related:
  - data.partial-failure-design
  - data.consensus-for-coordination
  - data.leader-election-safety
sources:
  - "book: Martin Kleppmann, Designing Data-Intensive Applications, first edition, data.pdf; Chapters 8 and 9"
source_confidence: high
last_reviewed: 2026-06-05
---

# Fencing Tokens

## Intent

Ensure that old owners cannot perform writes after a newer owner has taken over.

## Use when

- A process obtains a lease or lock before writing to shared storage or controlling a resource.
- A paused or partitioned process might continue acting after its lease expired.

## Avoid when

- The resource itself provides linearizable conditional writes that already reject stale actors.
- The operation is read-only or harmless if duplicated.

## Context and problem

Locks and leases can expire while a process is paused. When it resumes, it may still believe it owns the resource.

## Forces

- Availability through leases versus stale-owner risk
- Simple locking versus resource-side enforcement
- Timeouts versus correctness

## Guidance

Issue an increasing token on each successful lock or leadership grant. Require the protected resource to reject operations with tokens older than the latest seen.

## Implementation moves

- Generate tokens through a linearizable coordinator.
- Include the token in every write to the protected resource.
- Have the resource remember and reject stale tokens.
- Test pauses longer than lease expiry.

## Checks

- Can a paused old leader write after a new leader starts?
- Does the storage layer enforce token ordering?
- Are tokens persisted across resource restarts?

## Failure modes

- Using a lock service without resource-side fencing.
- Treating lease expiry as proof the old process stopped.
- Generating tokens from unsynchronized clocks.

## Agent trigger hints

Use this pattern when the user says or implies:

- fencing token
- distributed lock
- lease expired
- stale leader

## Source notes

Synthesized from Chapters 8 and 9 in the locally extracted `data-chapters/` text. This file stores original guidance and source pointers only, not source excerpts.
