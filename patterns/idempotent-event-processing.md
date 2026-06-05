---
id: data.idempotent-event-processing
title: Idempotent Event Processing
type: delivery-pattern
status: draft
summary: Make event consumers safe under duplicate delivery, retries, restarts, and replay.
tags:
  - data-systems
  - stream-processing
  - idempotency
  - event-driven
  - runtime-operations
  - cloud-agnostic
aliases:
  - deduplicate events
  - exactly once effect
  - idempotent consumer
applies_when:
  - A consumer processes messages from queues, topics, or logs with at-least-once delivery.
  - Restart or retry can cause the same event to be handled more than once.
avoid_when:
  - The source and sink provide a proven transactional exactly-once boundary for this operation.
  - The effect is naturally read-only and duplicates are harmless.
related:
  - data.message-passing-contracts
  - data.stream-derived-views
  - data.timeout-retry-backoff
sources:
  - "book: Martin Kleppmann, Designing Data-Intensive Applications, first edition, data.pdf; Chapter 11: Stream Processing"
source_confidence: high
last_reviewed: 2026-06-05
---

# Idempotent Event Processing

## Intent

Protect downstream state from duplicate event effects.

## Use when

- A consumer processes messages from queues, topics, or logs with at-least-once delivery.
- Restart or retry can cause the same event to be handled more than once.

## Avoid when

- The source and sink provide a proven transactional exactly-once boundary for this operation.
- The effect is naturally read-only and duplicates are harmless.

## Context and problem

Distributed messaging commonly redelivers events after failure. Without idempotency, retries cause double charges, duplicate records, or inflated aggregates.

## Forces

- Throughput versus deduplication state
- At-least-once reliability versus exactly-once effects
- Replayability versus side effects

## Guidance

Use event IDs, deterministic output keys, compare-and-set writes, or transactional offset/output commits so repeated processing has one logical effect.

## Implementation moves

- Include stable event identifiers or source offsets.
- Record processed IDs where duplicate effects matter.
- Use upserts or deterministic keys for derived records.
- Commit offsets only after durable output success.

## Checks

- What happens if the process crashes after writing output but before acknowledging input?
- Can the same event be replayed safely?
- Is deduplication state retained long enough?

## Failure modes

- Assuming the broker guarantees exactly-once end-to-end.
- Using random output IDs for retried events.
- Acknowledging input before durable side effects.

## Agent trigger hints

Use this pattern when the user says or implies:

- idempotent consumer
- duplicate event
- exactly once
- at least once processing

## Source notes

Synthesized from Chapter 11: Stream Processing in the locally extracted `data-chapters/` text. This file stores original guidance and source pointers only, not source excerpts.
