---
id: data.hot-spot-aware-partitioning
title: Hot Spot Aware Partitioning
type: architecture-pattern
status: draft
summary: Partition data to distribute load while accounting for skew, range access, secondary indexes, and rebalancing.
tags:
  - data-systems
  - partitioning
  - scalability
  - database
  - implementation-planning
  - cloud-agnostic
aliases:
  - sharding strategy
  - hot key partitioning
  - data partitioning
applies_when:
  - A dataset or workload is too large for one node.
  - Some keys, ranges, or tenants receive disproportionate traffic.
avoid_when:
  - The dataset fits comfortably on one node and partitioning would only add complexity.
  - Cross-partition transactions dominate the workload and cannot be redesigned.
related:
  - data.index-cost-tradeoff
  - data.partition-rebalancing
sources:
  - "book: Martin Kleppmann, Designing Data-Intensive Applications, first edition, data.pdf; Chapter 6: Partitioning"
source_confidence: high
last_reviewed: 2026-06-05
---

# Hot Spot Aware Partitioning

## Intent

Scale data and query load without concentrating traffic on a small number of partitions.

## Use when

- A dataset or workload is too large for one node.
- Some keys, ranges, or tenants receive disproportionate traffic.

## Avoid when

- The dataset fits comfortably on one node and partitioning would only add complexity.
- Cross-partition transactions dominate the workload and cannot be redesigned.

## Context and problem

Naive partitioning can spread data while still creating hot spots, expensive fan-out queries, or difficult rebalancing.

## Forces

- Even distribution versus range locality
- Simple routing versus query flexibility
- Static partitions versus changing load

## Guidance

Choose partition keys from real access patterns. Use hashing, ranges, composite keys, or deliberate salting according to skew and query needs, and plan rebalancing from the start.

## Implementation moves

- Measure key frequency, tenant distribution, and range-query needs.
- Avoid monotonically increasing hot partition keys for high write rates.
- Design secondary-index partitioning explicitly.
- Monitor per-partition load and split or rebalance when needed.

## Checks

- Can one key or tenant overload a partition?
- Do common queries target few partitions or fan out?
- Can partitions move without downtime?

## Failure modes

- Hashing away needed range queries.
- Partitioning by tenant when one tenant can dominate load.
- Ignoring secondary index query paths.

## Agent trigger hints

Use this pattern when the user says or implies:

- partitioning
- sharding
- hot spot
- hot key
- rebalance partitions

## Source notes

Synthesized from Chapter 6: Partitioning in the locally extracted `data-chapters/` text. This file stores original guidance and source pointers only, not source excerpts.
