---
id: data.eventual-consistency-boundaries
title: Eventual Consistency Boundaries
type: architecture-pattern
status: draft
summary: Use eventual consistency only where product semantics, repair mechanisms, and user expectations can tolerate temporary divergence.
tags:
  - data-systems
  - eventual-consistency
  - consistency
  - distributed-systems
  - design-review
  - cloud-agnostic
aliases:
  - eventual consistency
  - weak consistency boundary
  - stale data acceptable
applies_when:
  - Replicas, caches, indexes, or derived views update asynchronously.
  - The design trades immediate consistency for availability or performance.
avoid_when:
  - Temporary divergence violates money, access control, inventory, uniqueness, or safety invariants.
  - Users cannot understand or tolerate stale results.
related:
  - data.replication-lag-aware-reads
  - data.trust-but-verify-dataflows
  - data.conflict-free-domain-design
sources:
  - "book: Martin Kleppmann, Designing Data-Intensive Applications, first edition, data.pdf; Chapters 5, 9, and 12"
source_confidence: high
last_reviewed: 2026-06-05
---

# Eventual Consistency Boundaries

## Intent

Make weak consistency a conscious boundary with compensating behavior.

## Use when

- Replicas, caches, indexes, or derived views update asynchronously.
- The design trades immediate consistency for availability or performance.

## Avoid when

- Temporary divergence violates money, access control, inventory, uniqueness, or safety invariants.
- Users cannot understand or tolerate stale results.

## Context and problem

Eventually consistent systems can be robust and scalable, but hidden divergence creates confusing bugs and broken invariants.

## Forces

- Availability versus freshness
- Low latency versus user predictability
- Asynchronous repair versus immediate correctness

## Guidance

Define where stale data is acceptable, how convergence happens, and how violations are detected or repaired. Communicate freshness where it matters.

## Implementation moves

- Classify each read model by freshness requirement.
- Design reconciliation or rebuild paths for derived data.
- Use monotonic views or session guarantees where user experience needs them.
- Alert on lag or divergence beyond accepted limits.

## Checks

- What is the maximum acceptable staleness?
- How does the system converge after missed updates?
- Can users make harmful decisions from stale data?

## Failure modes

- Using eventual consistency for authorization decisions.
- Providing no way to detect stuck divergence.
- Letting stale derived data appear authoritative.

## Agent trigger hints

Use this pattern when the user says or implies:

- eventual consistency
- stale index
- async replication
- derived data lag

## Source notes

Synthesized from Chapters 5, 9, and 12 in the locally extracted `data-chapters/` text. This file stores original guidance and source pointers only, not source excerpts.
