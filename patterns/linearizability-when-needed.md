---
id: data.linearizability-when-needed
title: Linearizability When Needed
type: decision-guide
status: draft
summary: Use linearizability for operations that require a single up-to-date view, and avoid paying its cost for data that can be stale or mergeable.
tags:
  - data-systems
  - consistency
  - linearizability
  - distributed-systems
  - design-review
  - cloud-agnostic
aliases:
  - strong consistency
  - linearizable reads
  - fresh reads
applies_when:
  - Correctness depends on observing the latest write or enforcing uniqueness.
  - A user asks whether eventual consistency is acceptable.
avoid_when:
  - The data is cached, approximate, append-only, or explicitly allowed to be stale.
  - Latency and availability requirements exceed the need for a globally fresh view.
related:
  - data.eventual-consistency-boundaries
  - data.consensus-for-coordination
  - data.replication-lag-aware-reads
sources:
  - "book: Martin Kleppmann, Designing Data-Intensive Applications, first edition, data.pdf; Chapter 9: Consistency and Consensus"
source_confidence: high
last_reviewed: 2026-06-05
---

# Linearizability When Needed

## Intent

Reserve strong consistency for places where stale reads break correctness.

## Use when

- Correctness depends on observing the latest write or enforcing uniqueness.
- A user asks whether eventual consistency is acceptable.

## Avoid when

- The data is cached, approximate, append-only, or explicitly allowed to be stale.
- Latency and availability requirements exceed the need for a globally fresh view.

## Context and problem

Linearizability is easier for application reasoning but often costs latency, availability, and coordination.

## Forces

- Freshness versus latency
- Simplicity versus availability
- Global ordering versus partition tolerance

## Guidance

Identify operations that require real-time ordering, uniqueness, or compare-and-set semantics. Use linearizable systems there, and weaker models elsewhere with explicit user semantics.

## Implementation moves

- List decisions that must see the latest committed state.
- Separate critical coordination data from bulk or derived data.
- Use conditional writes or consensus-backed stores for critical keys.
- Document which reads may be stale.

## Checks

- Would a stale read allow duplicate ownership, overspend, or invariant violation?
- Can the operation tolerate retry after conditional-write failure?
- Is the coordination dataset small enough for strong consistency?

## Failure modes

- Making all data linearizable by default.
- Using eventually consistent reads for lock acquisition.
- Assuming read-after-write from any replica is fresh.

## Agent trigger hints

Use this pattern when the user says or implies:

- linearizability
- strong consistency
- stale read
- compare and set

## Source notes

Synthesized from Chapter 9: Consistency and Consensus in the locally extracted `data-chapters/` text. This file stores original guidance and source pointers only, not source excerpts.
