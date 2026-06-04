---
id: platform.data-consistency
title: Data Consistency by Explicit Write Ownership
type: architecture-pattern
status: seed
summary: Preserve correctness by making write ownership, conflict handling, replication
  lag, and read expectations explicit.
tags:
- platform-engineering
- data-platform
- data-consistency
- distributed-systems
- correctness
- replication
- design-review
- runtime-operations
- cloud-agnostic
- idempotency
aliases:
- consistency model
- strong consistency
- eventual consistency
- write ownership
applies_when:
- The user asks about data correctness across services, regions, queues, replicas,
  caches, or migrations.
- Multiple writers, replicas, asynchronous workflows, or caches can observe different
  values.
- A platform change may affect ordering, idempotency, or source of truth.
avoid_when:
- The data is disposable, derived, or can be recomputed without user impact.
- The workflow is local and single-writer with no replication, caching, or asynchronous
  boundary.
- The user only needs availability or recovery planning without consistency implications.
related:
- platform.data-continuity-during-change
- platform.high-availability
- platform.safe-infrastructure-change
sources:
- synthesis: general distributed systems and platform engineering practice
source_confidence: medium
last_reviewed: 2026-06-04
subject_area: data
---

# Data Consistency by Explicit Write Ownership

## Intent

Make the system's correctness rules explicit so agents can reason about data safety when infrastructure, services, or deployment topology changes.

## Use when

- More than one component can write, transform, cache, or replicate the same business fact.
- The design uses asynchronous messaging, read replicas, regional replication, dual writes, or caches.
- The user asks whether a migration, failover, active-active setup, or event pipeline could lose or corrupt data.

## Avoid when

- The data is purely telemetry, temporary cache, or easily recomputed.
- The system can accept last-write-wins without business harm and this is documented.
- The problem is only about backup retention, not runtime correctness.

## Context and problem

Platform changes often alter data paths. A design that works in one region or one database can break when replicated, cached, split into services, or deployed across failure domains. Without an explicit consistency model, teams often discover conflict, stale read, and ordering bugs during failover or migration.

## Forces

- Correctness versus availability: strong coordination can reduce availability under partition.
- Latency versus freshness: faster local reads may be stale.
- Autonomy versus single source of truth: independent services need clear ownership boundaries.
- Throughput versus ordering: parallelism can reorder events.

## Guidance

Identify the authoritative owner for each mutable fact. Define which reads must be fresh, which may be stale, how conflicts are detected or resolved, and how operations remain idempotent across retries, replays, and failovers.

## Implementation moves

- Create a data ownership map for critical entities and fields.
- Mark each boundary as single-writer, multi-writer with conflict resolution, append-only log, derived read model, or cache.
- Specify read expectations: read-your-writes, monotonic reads, bounded staleness, or eventual consistency.
- Add idempotency keys and deduplication for retried operations.
- Design conflict detection rather than relying on silent overwrite.
- Test failover, replay, retry, and delayed message scenarios.

## Checks

- Who owns writes for each business fact?
- What happens if the same operation is submitted twice?
- What happens if messages arrive late, out of order, or more than once?
- Which reads must be strongly consistent, and which can be stale?
- How are conflicts surfaced to users or operators?

## Failure modes

- Dual writes with no transaction or reconciliation strategy.
- Caches treated as authoritative state.
- Active-active writes without conflict detection.
- Migration scripts that change data while applications assume the old shape.
- Retry logic that creates duplicate side effects.

## Agent trigger hints

Use this pattern when the user says or implies:

- consistency model
- eventual consistency
- stale reads
- dual writes
- source of truth
- idempotency
- replay events
- active active database

## Source notes

This is an original synthesis from general distributed systems and platform engineering practice. It should be linked to source-specific notes when extracted from a particular reading.
