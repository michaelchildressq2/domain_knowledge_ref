---
id: platform.lease-based-ownership-election
title: Lease Based Ownership Election
type: architecture-pattern
status: draft
summary: Elect one active owner among replicas with consensus-backed compare-and-swap, renewable leases, and fencing checks before protected actions.
tags:
  - platform-engineering
  - cloud-architecture
  - high-availability
  - data-consistency
  - operability
  - design-review
  - runtime-operations
  - idempotency
  - testing
  - kubernetes
  - leader-election
aliases:
  - ownership election
  - master election
  - leader lease
  - distributed lock
  - fencing token
applies_when:
  - Multiple replicas may run, but only one should own a shard, scheduler role, controller loop, or exclusive task at a time.
  - A singleton deployment cannot meet the required availability or rollout SLA.
  - A consensus-backed store such as etcd, ZooKeeper, or Consul is available.
avoid_when:
  - A single orchestrated replica has acceptable downtime and simpler operation.
  - The work can be partitioned so each replica owns independent keys without global election.
  - Correctness cannot tolerate lease ambiguity and requires stronger transaction or consensus semantics at the protected resource.
related:
  - data.leader-election-safety
  - data.consensus-for-coordination
  - data.fencing-tokens
  - platform.sharded-service-routing
sources:
  - 'book: Brendan Burns, Designing Distributed Systems, Chapter 9: Ownership Election'
source_confidence: high
last_reviewed: 2026-06-05
---

# Lease Based Ownership Election

## Intent

Allow replicated services to fail over ownership while preventing stale owners from performing protected work.

## Use when

- Only one replica should make scheduling, reconciliation, shard ownership, or mutation decisions for a resource.
- You need faster recovery or safer rollout than a single active instance can provide.
- The platform already depends on a reliable consensus-backed key-value store.
- Ownership may be long-lived and must be renewed while the process remains healthy.
- Protected downstream resources can validate owner identity and a monotonically changing lease version.

## Avoid when

- A singleton under an orchestrator meets the SLA and is much simpler.
- Duplicate owners would be harmless because all operations are idempotent and commutative.
- The lease service is less available or less trusted than the workload itself.
- The downstream system cannot reject stale owners or old lease versions.
- The team is tempted to implement Paxos or Raft directly instead of using a proven store.

## Context and problem

Some distributed services need exactly one active owner for a role or resource. A single replica is simple, but it creates downtime during failures and upgrades. Running many replicas without coordination can create split ownership and duplicate mutations.

Lease-based ownership uses a consensus-backed store to acquire ownership with compare-and-swap and a time-bounded lease. The owner renews the lease while active. If it fails, the lease expires and another replica can take over. Because processes can pause, clocks can drift, and networks can delay messages, protected actions also need fencing checks so stale owners are rejected.

## Forces

- Availability versus singleton simplicity.
- Failover speed versus false lease expiration.
- Lease duration versus pause tolerance.
- Owner autonomy versus downstream fencing.
- Reusing consensus stores versus building custom coordination.
- Fast rollout versus split-owner risk.

## Guidance

First decide whether you need election at all. If a singleton can meet the SLA, use it and avoid distributed coordination. If you do need election, use a proven consensus-backed key-value store rather than implementing consensus yourself.

Use renewable leases, not permanent locks. Renew well before expiration and stop protected work immediately when renewal fails. Send an owner identity and lease version with every protected request, and require downstream systems to verify both before accepting mutations. This fencing is what protects against paused old owners and delayed requests.

## Implementation moves

- Define the owned resource or role precisely, such as scheduler, shard range, partition, tenant, or controller loop.
- Store owner identity and a lease version or resource revision in a consensus-backed key.
- Acquire ownership with compare-and-swap from empty or expired state.
- Set a TTL on the ownership record and renew periodically, commonly before half the TTL has elapsed.
- Implement `handleLockLost` behavior that stops work, exits, or transitions to standby immediately.
- Check local lease freshness before every protected operation.
- Include owner identity and lease version in requests to workers or downstream systems.
- Make downstream systems reject requests whose owner or version does not match current ownership.
- Use watchdogs or process termination when work risks exceeding the lease.
- Monitor lease acquisition, renewal failures, owner changes, and rejected stale requests.

## Checks

- Is election truly required, or is a singleton acceptable?
- Is the coordination store already operated with the required availability?
- What TTL tolerates normal pauses while still failing over quickly?
- What happens if the owner pauses longer than the TTL and resumes?
- Can a delayed request from an old lease be rejected?
- Do protected operations include a fencing token or resource version?
- Is lease loss tested under process pause, network delay, and node failure?
- Are owner changes auditable?

## Failure modes

- Using a permanent lock that remains stuck after owner failure.
- Unlocking a lock after the TTL expired and accidentally releasing someone else's lock.
- Renewing leases but continuing work after renewal fails.
- Believing a local lease check eliminates all stale-owner races.
- Sending protected requests without owner version or fencing token.
- Building a custom consensus algorithm instead of using a proven coordination store.
- Setting TTL so short that normal pauses cause churn or so long that failover is too slow.

## Agent trigger hints

Use this pattern when the user says or implies:

- leader election
- master election
- only one replica should run this
- distributed lock
- lease
- etcd lock
- split brain
- fencing token

## Source notes

Synthesized from Chapter 9's discussion of singleton trade-offs, compare-and-swap locks, TTL leases, renewal, and stale-owner validation. This file contains original guidance and source pointers only.
