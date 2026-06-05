---
id: platform.sharded-service-routing
title: Sharded Service Routing
type: architecture-pattern
status: draft
summary: Split stateful serving across shards with deterministic routing, careful shard-key design, consistent hashing, and targeted replication for hot or critical shards.
tags:
  - platform-engineering
  - cloud-architecture
  - scalability
  - high-availability
  - data-consistency
  - design-review
  - runtime-operations
  - module-boundaries
  - testing
  - kubernetes
  - sharding
aliases:
  - sharded service
  - shard router
  - shard key design
  - consistent hashing
  - hot shard scaling
applies_when:
  - A stateful dataset or cache cannot fit efficiently on one machine.
  - Each request can be routed to a subset of data using a deterministic key.
  - Cache hit rate, data size, or state ownership requires partitioning.
avoid_when:
  - The service is stateless and can be scaled by homogeneous replication.
  - The workload requires most requests to touch most shards.
  - The team cannot define a stable key that preserves correctness and distributes load.
related:
  - platform.ambassador-local-service-broker
  - platform.replicated-stateless-serving
  - platform.scatter-gather-request-parallelism
  - data.hot-spot-aware-partitioning
sources:
  - 'book: Brendan Burns, Designing Distributed Systems, Chapter 6: Sharded Services'
  - 'book: Brendan Burns, Designing Distributed Systems, Chapter 3: Ambassadors'
source_confidence: high
last_reviewed: 2026-06-05
---

# Sharded Service Routing

## Intent

Scale stateful serving by partitioning the key space while preserving correct request-to-shard routing and manageable resharding.

## Use when

- Data size, memory footprint, or cache efficiency exceeds one machine or one replicated homogeneous tier.
- A request can be mapped to one shard or a small shard set.
- Replicated caches waste memory by storing the same hot set in every replica.
- Specific shards need independent scaling because load is uneven.
- Clients can route through an ambassador, client library, shard router service, or gateway.

## Avoid when

- Any replica can serve all requests and stateless replication is enough.
- The system frequently needs global queries across all data.
- The shard key would include unstable fields such as request time when those fields do not affect the response.
- Losing one shard would violate the SLA and no replicated-shard design is planned.
- Operational tooling cannot identify shard ownership, load, and failure status.

## Context and problem

Replication scales request throughput when every replica can serve every request. Stateful services and large caches have a different limit: the state itself may be too large or too expensive to duplicate everywhere. Sharding assigns subsets of the state to different nodes, making state size and cache memory scale with the number of shards.

Routing is the hard part. The shard key must group equivalent requests together for correctness and cache efficiency while distributing load evenly. Resharding can remap many keys if the routing function is naive. Hot shards can form when organic traffic concentrates on one key range.

## Forces

- State capacity versus routing complexity.
- Cache hit rate versus failure sensitivity.
- Uniform distribution versus semantic grouping.
- Client-side routing simplicity versus shared-router latency.
- Consistent hashing stability versus routing implementation complexity.
- Independent shard scaling versus operational visibility.

## Guidance

Shard only around a key that reflects the data needed to answer the request. Make the sharding function deterministic and as uniform as the workload allows. Do not hash the entire request object if only part of it determines the answer; do not omit fields that change the answer.

Use consistent hashing or an equivalent strategy when shard count changes would otherwise remap most keys. If shard failure or rollout would breach performance or availability, make each shard a replicated service. For hot shards, scale or split the affected shard rather than blindly adding global replicas.

## Implementation moves

- Define the shard key from domain semantics: tenant, user, object id, request URI, region, location, or other response-determining fields.
- Document which request attributes must not be part of the key because they would destroy cache reuse or load distribution.
- Implement routing in one place: ambassador, client library, shard-router service, ingress, or gateway.
- Choose per-client ambassador routing when avoiding an extra network hop matters and per-pod complexity is acceptable.
- Choose a shared shard-router service when centralized scaling, monitoring, and configuration outweigh added latency.
- Use consistent hashing or a routing table with controlled migrations for resharding.
- Replicate individual shards when cache or state availability is critical.
- Monitor per-shard traffic, hit rate, error rate, latency, capacity, and ownership.
- Add shard-aware rollout controls so one failed shard deployment does not affect all users.
- Load test cache behavior and backend load with one shard down and during resharding.

## Checks

- Does the shard key include exactly the fields needed for correctness?
- Is routing deterministic across all clients and deployments?
- What percentage of keys move when shard count changes?
- Can one hot shard be scaled without scaling the whole service?
- What happens to cache hit rate and backend load when a shard fails?
- Are shard names, owners, and routing versions observable?
- Can operators drain or replace one shard without global outage?
- Does the system avoid sending all requests through one under-scaled router?

## Failure modes

- Hashing the entire request and sending equivalent requests to different shards.
- Hashing too few fields and serving incorrect cached results.
- Using modulo shard counts without a migration plan, causing near-total remapping during scale changes.
- Treating a sharded cache as optional even though backend capacity depends on it.
- Ignoring hot shards until one partition dominates tail latency.
- Hiding sharding in every application with inconsistent client implementations.
- Resharding during peak load without measuring cache miss amplification.

## Agent trigger hints

Use this pattern when the user says or implies:

- shard this service
- shard key
- consistent hashing
- hot shard
- cache hit rate
- state too large for one node
- shard router
- client-side sharding

## Source notes

Synthesized from Chapter 6's sharded cache design, shard-key selection, consistent hashing, replicated shards, and hot sharding sections, with routing alternatives connected to the ambassador material in Chapter 3. This file contains original guidance and source pointers only.
