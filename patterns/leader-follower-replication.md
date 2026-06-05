---
id: data.leader-follower-replication
title: Leader Follower Replication
type: architecture-pattern
status: draft
summary: Use leader-follower replication when one primary write path and multiple read or failover copies fit the consistency and availability needs.
tags:
  - data-systems
  - replication
  - high-availability
  - database
  - runtime-operations
  - cloud-agnostic
aliases:
  - primary replica
  - leader follower
  - master slave replication
applies_when:
  - A dataset needs copies for read scaling, failover, or geographic placement.
  - Writes can be routed through one leader for a given shard or dataset.
avoid_when:
  - The application requires multi-region writes with low latency.
  - Leader failover semantics and replication lag are unacceptable for the workload.
related:
  - data.replication-lag-aware-reads
  - data.multi-leader-conflict-design
sources:
  - "book: Martin Kleppmann, Designing Data-Intensive Applications, first edition, data.pdf; Chapter 5: Replication"
source_confidence: high
last_reviewed: 2026-06-05
---

# Leader Follower Replication

## Intent

Replicate data while keeping write ordering relatively simple.

## Use when

- A dataset needs copies for read scaling, failover, or geographic placement.
- Writes can be routed through one leader for a given shard or dataset.

## Avoid when

- The application requires multi-region writes with low latency.
- Leader failover semantics and replication lag are unacceptable for the workload.

## Context and problem

Data copies improve availability and read throughput, but writes need an ordering authority and lag must be understood.

## Forces

- Read scalability versus stale reads
- Leader simplicity versus write availability
- Failover speed versus split-brain risk

## Guidance

Use a leader to serialize writes and followers for read scaling or failover. Make replication mode, lag tolerance, and failover behavior explicit in application design.

## Implementation moves

- Route writes to the current leader.
- Expose replication lag and follower freshness.
- Choose synchronous, asynchronous, or semi-synchronous replication per durability need.
- Design failover with fencing and client retry behavior.

## Checks

- Can clients tolerate reading stale follower data?
- What data may be lost if the leader fails?
- How is a former leader prevented from accepting writes after failover?

## Failure modes

- Reading from followers after writes that require read-your-writes.
- Assuming asynchronous replicas are fully durable.
- Promoting a follower without fencing the old leader.

## Agent trigger hints

Use this pattern when the user says or implies:

- leader follower replication
- primary replica
- read replica
- database failover

## Source notes

Synthesized from Chapter 5: Replication in the locally extracted `data-chapters/` text. This file stores original guidance and source pointers only, not source excerpts.
