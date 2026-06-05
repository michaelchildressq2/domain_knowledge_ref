---
id: data.index-cost-tradeoff
title: Index Cost Tradeoff
type: decision-guide
status: draft
summary: Add indexes deliberately because they speed reads but increase write cost, storage, and maintenance complexity.
tags:
  - data-systems
  - indexing
  - performance
  - database
  - implementation-planning
  - cloud-agnostic
aliases:
  - index tradeoff
  - secondary index cost
  - read write tradeoff
applies_when:
  - Queries are slow and a new index is proposed.
  - A schema accumulates many indexes without clear ownership.
avoid_when:
  - The index is required for a primary invariant or uniqueness constraint.
  - The table is small enough that index cost is irrelevant.
related:
  - data.storage-engine-fit
  - data.hot-spot-aware-partitioning
  - data.analytical-column-storage
sources:
  - "book: Martin Kleppmann, Designing Data-Intensive Applications, first edition, data.pdf; Chapter 3: Storage and Retrieval"
source_confidence: high
last_reviewed: 2026-06-05
---

# Index Cost Tradeoff

## Intent

Treat indexes as maintained derived data, not free query acceleration.

## Use when

- Queries are slow and a new index is proposed.
- A schema accumulates many indexes without clear ownership.

## Avoid when

- The index is required for a primary invariant or uniqueness constraint.
- The table is small enough that index cost is irrelevant.

## Context and problem

Every index improves some reads by adding write work, storage, rebuild cost, and possible operational risk.

## Forces

- Read latency versus write throughput
- Query flexibility versus storage cost
- Operational rebuild time versus online availability

## Guidance

Create indexes for important access paths with measured need. Remove unused indexes and account for write amplification, backfill, and maintenance behavior.

## Implementation moves

- Identify the query shape and selectivity the index supports.
- Estimate write and storage overhead.
- Plan online creation or backfill for large datasets.
- Monitor index usage and remove stale indexes.

## Checks

- Which query gets faster and by how much?
- What write path now updates the index?
- Can the index be rebuilt after corruption or migration?

## Failure modes

- Indexing every field preemptively.
- Ignoring index backfill impact on production.
- Creating indexes that do not match real predicates or sort order.

## Agent trigger hints

Use this pattern when the user says or implies:

- add database index
- secondary index
- slow query
- index overhead

## Source notes

Synthesized from Chapter 3: Storage and Retrieval in the locally extracted `data-chapters/` text. This file stores original guidance and source pointers only, not source excerpts.
