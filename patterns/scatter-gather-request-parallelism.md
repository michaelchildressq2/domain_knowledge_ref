---
id: platform.scatter-gather-request-parallelism
title: Scatter Gather Request Parallelism
type: architecture-pattern
status: draft
summary: Parallelize one request across many workers only when partial results can be merged and tail-latency, straggler, and availability costs are explicitly controlled.
tags:
  - platform-engineering
  - cloud-architecture
  - scalability
  - high-availability
  - performance
  - design-review
  - runtime-operations
  - testing
  - kubernetes
  - scatter-gather
aliases:
  - scatter gather
  - fan out fan in
  - request parallelism
  - straggler problem
  - parallel search
applies_when:
  - A single request can be decomposed into independent subrequests whose partial results can be merged.
  - Request latency is dominated by compute or data lookup that can run in parallel.
  - A root service can coordinate fan-out, deadlines, and aggregation.
avoid_when:
  - The request needs sequential steps or strong coordination across leaves.
  - Every leaf must answer and leaf failure probability makes user-visible failure likely.
  - Per-leaf overhead or tail latency will dominate the benefit of parallelism.
related:
  - platform.sharded-service-routing
  - platform.replicated-stateless-serving
  - platform.coordinated-batch-aggregation
  - data.load-and-performance-characterization
sources:
  - 'book: Brendan Burns, Designing Distributed Systems, Chapter 7: Scatter/Gather'
source_confidence: high
last_reviewed: 2026-06-05
---

# Scatter Gather Request Parallelism

## Intent

Reduce request latency by distributing independent subwork to many leaves and combining their partial results into one response.

## Use when

- A request can be split into independent pieces, such as term lookup, shard search, ranking fragments, or parallel computation.
- The root can combine partial results with a known operation such as union, intersection, top-k merge, or aggregation.
- The dataset or computation can be partitioned across leaves without changing user-visible semantics.
- Tail latency is important enough to justify fan-out coordination.
- Leaf shards can be replicated so failures and rollouts do not fail all user requests.

## Avoid when

- A single worker already satisfies latency targets with simpler operations.
- The work cannot be split without cross-leaf coordination.
- Most requests require all leaves, and leaf availability is too low for the intended SLA.
- The aggregation logic is approximate but the user expects complete answers.
- Network overhead, serialization, or root CPU will dominate the work itself.

## Context and problem

Replication scales request throughput and sharding scales state size, but some requests are slow because they require a large amount of mostly independent processing. Scatter/gather fans a single request out to many leaves. Each leaf computes a partial answer, and the root gathers and merges those answers.

The pattern has sharp costs. The root waits on leaf responses, so slow leaves become user-visible stragglers. As fan-out grows, overhead and failure probability grow too. A design that speeds median latency can damage tail latency and availability if it requires every leaf to answer.

## Forces

- Parallel speedup versus fan-out overhead.
- Complete results versus deadline-bounded partial results.
- More leaves versus worse tail-latency amplification.
- State sharding versus request fan-out.
- Root simplicity versus aggregation CPU and memory pressure.
- Leaf replication cost versus rollout and failure safety.

## Guidance

Use scatter/gather when the merge operation is well-defined and the latency savings exceed the overhead and straggler cost. Model the request as a tree: a root handles decomposition, deadlines, retries or hedging, result validation, and merge. Leaves handle bounded subwork and return partial results in a predictable shape.

Replicate each leaf shard when the request requires that shard's answer. Without replicated leaves, one failed or upgrading shard can fail every request. Choose the number of leaves from measured latency curves, not from the assumption that more parallelism always helps.

## Implementation moves

- Define the split strategy: by query term, data shard, region, time range, or computation chunk.
- Define the merge operation and its correctness rules before building the fan-out path.
- Set request deadlines and per-leaf timeouts from end-to-end latency targets.
- Add bounded retries or hedged requests only where duplicate work is safe.
- Replicate leaf shards and load balance each leaf request across healthy replicas.
- Measure overhead per leaf and aggregate CPU/memory at the root.
- Keep partial result payloads compact and typed.
- Decide whether partial or stale results are acceptable, and label responses accordingly if they are.
- Monitor fan-out count, slowest-leaf latency, timeout rate, merge time, and partial-result size.
- Test with a slow leaf, a failed leaf, and a high fan-out query.

## Checks

- Can each subrequest run independently?
- Is the merge operation deterministic and tested?
- What is the probability that at least one leaf is slow or unavailable for a typical fan-out?
- Does adding leaves still reduce p95 and p99 end-to-end latency?
- Can the root shed, degrade, or return partial results under deadline pressure?
- Are leaf shards replicated enough for rollouts under load?
- Is root capacity sized for fan-out and merge work?
- Are duplicate subrequests safe if retries or hedging are used?

## Failure modes

- Increasing leaf count until fan-out overhead eliminates the benefit.
- Optimizing median latency while p99 latency gets worse because of stragglers.
- Running one replica per leaf shard, making every rollout a user-facing outage.
- Merging partial results incorrectly or returning incomplete results as complete.
- Letting the root become a bottleneck or single point of failure.
- Retrying slow leaves aggressively and amplifying load during incidents.
- Ignoring payload size until gather traffic overwhelms the network.

## Agent trigger hints

Use this pattern when the user says or implies:

- scatter gather
- fan out and aggregate
- parallelize this request
- straggler problem
- search across shards
- merge partial results
- reduce latency with parallelism

## Source notes

Synthesized from Chapter 7's root-distribution and leaf-sharding scatter/gather examples, plus its discussion of leaf count, stragglers, and replicated leaf shards. This file contains original guidance and source pointers only.
