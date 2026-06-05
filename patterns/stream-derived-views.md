---
id: data.stream-derived-views
title: Stream Derived Views
type: architecture-pattern
status: draft
summary: Use stream processing to maintain derived data incrementally when low-latency updates matter.
tags:
  - data-systems
  - stream-processing
  - derived-data
  - event-driven
  - runtime-operations
  - cloud-agnostic
aliases:
  - streaming materialized view
  - near real time pipeline
  - incremental view
applies_when:
  - Derived indexes, caches, aggregates, or read models must update quickly as events arrive.
  - Batch recomputation is too stale or too expensive for routine use.
avoid_when:
  - Freshness is not important and batch recomputation is simpler and safer.
  - The input event stream lacks durable replay or ordering needed for correctness.
related:
  - data.event-log-as-source
  - data.idempotent-event-processing
  - data.backpressure-for-streams
sources:
  - "book: Martin Kleppmann, Designing Data-Intensive Applications, first edition, data.pdf; Chapter 11: Stream Processing"
source_confidence: high
last_reviewed: 2026-06-05
---

# Stream Derived Views

## Intent

Maintain useful derived state continuously while preserving the ability to recover from failures.

## Use when

- Derived indexes, caches, aggregates, or read models must update quickly as events arrive.
- Batch recomputation is too stale or too expensive for routine use.

## Avoid when

- Freshness is not important and batch recomputation is simpler and safer.
- The input event stream lacks durable replay or ordering needed for correctness.

## Context and problem

Low-latency derived data requires incremental updates, but stream processors face duplicates, ordering, late events, and state recovery.

## Forces

- Freshness versus correctness complexity
- Stateful processing versus replayability
- Throughput versus backpressure

## Guidance

Build stream processors around durable input logs, checkpointed state, idempotent outputs, and explicit time/order semantics. Keep rebuild paths available.

## Implementation moves

- Define event time, processing time, and window behavior.
- Checkpoint state and offsets consistently.
- Make output writes idempotent or transactional where needed.
- Monitor lag, dead letters, and state size.

## Checks

- Can the processor recover without losing or duplicating effects?
- How are late or out-of-order events handled?
- Can the view be rebuilt from the log?

## Failure modes

- Treating stream processing as just faster batch processing.
- Ignoring duplicate events after restart.
- Letting lag grow without backpressure or alerting.

## Agent trigger hints

Use this pattern when the user says or implies:

- stream processing
- materialized view
- real time pipeline
- derived data stream

## Source notes

Synthesized from Chapter 11: Stream Processing in the locally extracted `data-chapters/` text. This file stores original guidance and source pointers only, not source excerpts.
