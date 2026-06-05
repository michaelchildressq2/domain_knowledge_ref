---
id: data.replication-lag-aware-reads
title: Replication Lag Aware Reads
type: architecture-pattern
status: draft
summary: Design read paths around the user-visible anomalies created by asynchronous replication lag.
tags:
  - data-systems
  - replication
  - consistency
  - read-models
  - runtime-operations
  - cloud-agnostic
aliases:
  - stale reads
  - read your writes
  - replica lag
applies_when:
  - Applications read from followers or asynchronously updated replicas.
  - Users may observe stale or non-monotonic data after writes.
avoid_when:
  - All reads go to a linearizable leader or strongly consistent quorum.
  - The data is explicitly best-effort and stale reads have no user impact.
related:
  - data.leader-follower-replication
  - data.eventual-consistency-boundaries
sources:
  - "book: Martin Kleppmann, Designing Data-Intensive Applications, first edition, data.pdf; Chapter 5: Replication"
source_confidence: high
last_reviewed: 2026-06-05
---

# Replication Lag Aware Reads

## Intent

Prevent replica lag from surprising users or violating application expectations.

## Use when

- Applications read from followers or asynchronously updated replicas.
- Users may observe stale or non-monotonic data after writes.

## Avoid when

- All reads go to a linearizable leader or strongly consistent quorum.
- The data is explicitly best-effort and stale reads have no user impact.

## Context and problem

Asynchronous replicas may lag behind writes, so users can see data disappear, move backward, or differ across devices.

## Forces

- Read scalability versus freshness
- Low latency versus consistency
- Availability versus user expectations

## Guidance

Classify reads by freshness requirement. Route critical reads to fresh sources, use session guarantees where needed, and make stale data acceptable only where the product semantics allow it.

## Implementation moves

- Identify read-your-writes and monotonic-read requirements.
- Route post-write reads to leader or sufficiently caught-up replicas.
- Track session versions or timestamps where useful.
- Expose lag metrics and degrade stale views deliberately.

## Checks

- Can users see their own update immediately where expected?
- Can a later read return older data than an earlier read?
- Are stale views labeled or harmless?

## Failure modes

- Using read replicas transparently for every query.
- Ignoring cross-device user sessions.
- Assuming replication lag is always small.

## Agent trigger hints

Use this pattern when the user says or implies:

- replication lag
- read your writes
- stale replica read
- eventual consistency user experience

## Source notes

Synthesized from Chapter 5: Replication in the locally extracted `data-chapters/` text. This file stores original guidance and source pointers only, not source excerpts.
