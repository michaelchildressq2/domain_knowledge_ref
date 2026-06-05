---
id: data.storage-engine-fit
title: Storage Engine Fit
type: decision-guide
status: draft
summary: Choose storage engines by write/read mix, update pattern, range-query needs, and compaction behavior.
tags:
  - data-systems
  - storage-engine
  - database
  - performance
  - design-review
  - cloud-agnostic
aliases:
  - b-tree vs lsm
  - storage engine choice
  - database internals fit
applies_when:
  - A workload is sensitive to write amplification, read amplification, range scans, or update latency.
  - A database choice depends on whether B-tree, LSM, or log-structured storage fits.
avoid_when:
  - The database is mandated and only application-level tuning is possible.
  - The workload is too small for storage-engine trade-offs to matter.
related:
  - data.index-cost-tradeoff
  - data.log-structured-storage
  - data.analytical-column-storage
sources:
  - "book: Martin Kleppmann, Designing Data-Intensive Applications, first edition, data.pdf; Chapter 3: Storage and Retrieval"
source_confidence: high
last_reviewed: 2026-06-05
---

# Storage Engine Fit

## Intent

Avoid treating all databases as equivalent once their API looks similar.

## Use when

- A workload is sensitive to write amplification, read amplification, range scans, or update latency.
- A database choice depends on whether B-tree, LSM, or log-structured storage fits.

## Avoid when

- The database is mandated and only application-level tuning is possible.
- The workload is too small for storage-engine trade-offs to matter.

## Context and problem

Storage-engine internals strongly affect latency, throughput, disk use, and operational behavior under real workloads.

## Forces

- Write throughput versus read amplification
- Range query efficiency versus compaction cost
- Predictable latency versus background maintenance

## Guidance

Match engine design to workload. Consider B-trees for update-heavy indexed lookup and range queries, LSM/log-structured engines for high write throughput with compaction trade-offs, and column stores for analytical scans.

## Implementation moves

- Measure read/write ratio, key locality, value size, and range-query needs.
- Check compaction, cache, and index behavior under expected data volume.
- Benchmark with production-like key distributions.
- Plan operational headroom for background maintenance.

## Checks

- Which operation becomes slower as data grows?
- Are tail latencies affected by compaction or page splits?
- Does the engine support required query patterns without extra indexes?

## Failure modes

- Choosing by benchmark headline throughput only.
- Ignoring write amplification and disk growth.
- Using OLTP row storage for analytical scans at scale.

## Agent trigger hints

Use this pattern when the user says or implies:

- b-tree vs lsm
- storage engine
- write amplification
- database performance

## Source notes

Synthesized from Chapter 3: Storage and Retrieval in the locally extracted `data-chapters/` text. This file stores original guidance and source pointers only, not source excerpts.
