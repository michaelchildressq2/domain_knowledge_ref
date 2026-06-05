---
id: data.consensus-for-coordination
title: Consensus For Coordination
type: architecture-pattern
status: draft
summary: Use consensus-backed coordination for leader election, membership, locks, and configuration that require agreement despite failures.
tags:
  - data-systems
  - consensus
  - coordination
  - distributed-systems
  - reliability
  - cloud-agnostic
aliases:
  - raft paxos zookeeper
  - coordination service
  - distributed consensus
applies_when:
  - Several nodes must agree on ownership, ordering, membership, or configuration.
  - Split-brain or duplicate leadership would corrupt data or violate invariants.
avoid_when:
  - The decision is advisory and can be eventually consistent.
  - A single-node coordinator is acceptable for the system risk and scale.
related:
  - data.fencing-tokens
  - data.leader-election-safety
  - data.linearizability-when-needed
sources:
  - "book: Martin Kleppmann, Designing Data-Intensive Applications, first edition, data.pdf; Chapter 9: Consistency and Consensus"
source_confidence: high
last_reviewed: 2026-06-05
---

# Consensus For Coordination

## Intent

Use proven coordination abstractions for decisions that cannot be made independently.

## Use when

- Several nodes must agree on ownership, ordering, membership, or configuration.
- Split-brain or duplicate leadership would corrupt data or violate invariants.

## Avoid when

- The decision is advisory and can be eventually consistent.
- A single-node coordinator is acceptable for the system risk and scale.

## Context and problem

Distributed nodes cannot reliably infer global truth through timeouts alone. Consensus provides a way to agree on ordered decisions under failures.

## Forces

- Correctness versus availability under partition
- Coordination latency versus safety
- Generic service versus custom protocol risk

## Guidance

Use established consensus systems for small, critical coordination state. Keep high-volume data paths out of consensus unless strong ordering is truly required.

## Implementation moves

- Identify the minimal coordination state.
- Use a mature consensus-backed service or database feature.
- Design clients for session expiry, retries, and fencing.
- Monitor quorum health and write latency.

## Checks

- What happens if the coordinator loses quorum?
- Can stale clients act after session expiry?
- Is the coordinated state small and critical?

## Failure modes

- Building ad hoc consensus with heartbeats.
- Putting all application data through a coordination service.
- Ignoring quorum placement and correlated failures.

## Agent trigger hints

Use this pattern when the user says or implies:

- consensus
- zookeeper
- etcd
- raft
- leader election
- distributed lock

## Source notes

Synthesized from Chapter 9: Consistency and Consensus in the locally extracted `data-chapters/` text. This file stores original guidance and source pointers only, not source excerpts.
