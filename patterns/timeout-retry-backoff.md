---
id: data.timeout-retry-backoff
title: Timeout Retry Backoff
type: delivery-pattern
status: draft
summary: Use timeouts, retries, backoff, and idempotency together so transient faults do not become overload or duplicate side effects.
tags:
  - data-systems
  - distributed-systems
  - resilience
  - runtime-operations
  - implementation-planning
  - cloud-agnostic
aliases:
  - retry policy
  - exponential backoff
  - timeout design
applies_when:
  - A service calls remote systems or databases over a network.
  - Transient failures or latency spikes are expected.
avoid_when:
  - The operation is non-idempotent and cannot be safely retried without redesign.
  - A hard real-time deadline requires immediate failure instead of retry.
related:
  - data.partial-failure-design
  - data.idempotent-event-processing
  - data.backpressure-for-streams
sources:
  - "book: Martin Kleppmann, Designing Data-Intensive Applications, first edition, data.pdf; Chapter 8: The Trouble with Distributed Systems"
source_confidence: high
last_reviewed: 2026-06-05
---

# Timeout Retry Backoff

## Intent

Handle transient uncertainty without amplifying failure.

## Use when

- A service calls remote systems or databases over a network.
- Transient failures or latency spikes are expected.

## Avoid when

- The operation is non-idempotent and cannot be safely retried without redesign.
- A hard real-time deadline requires immediate failure instead of retry.

## Context and problem

Retries can mask temporary faults, but unbounded or synchronized retries can overload dependencies and duplicate side effects.

## Forces

- User latency versus recovery chance
- Retry success versus overload
- Duplicate safety versus implementation complexity

## Guidance

Set explicit deadlines, retry only safe operations, use backoff with jitter, and propagate overload signals. Pair retries with idempotency keys or deduplication.

## Implementation moves

- Classify operations as idempotent, safely retryable, or nonretryable.
- Set per-call timeout and overall request deadline.
- Use exponential backoff with jitter.
- Emit metrics for attempts, failures, and retry exhaustion.

## Checks

- Can the operation run twice safely?
- Does retry traffic stay bounded during dependency failure?
- Are timeouts aligned with user and upstream deadlines?

## Failure modes

- Retrying immediately in tight loops.
- Retrying non-idempotent writes without keys.
- Using very long timeouts that tie up resources.

## Agent trigger hints

Use this pattern when the user says or implies:

- retry policy
- timeout
- backoff
- idempotency key
- transient failure

## Source notes

Synthesized from Chapter 8: The Trouble with Distributed Systems in the locally extracted `data-chapters/` text. This file stores original guidance and source pointers only, not source excerpts.
