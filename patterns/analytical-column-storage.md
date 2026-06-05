---
id: data.analytical-column-storage
title: Analytical Column Storage
type: architecture-pattern
status: draft
summary: Use column-oriented storage for analytical workloads that scan many rows but only a subset of columns.
tags:
  - data-systems
  - analytics
  - storage-engine
  - data-warehouse
  - performance
  - cloud-agnostic
aliases:
  - columnar storage
  - olap storage
  - data warehouse columns
applies_when:
  - Queries aggregate or filter over large datasets while reading few columns.
  - The workload is analytical rather than transaction-oriented.
avoid_when:
  - Workloads frequently update individual rows or require low-latency point writes.
  - Queries usually need complete records by primary key.
related:
  - data.storage-engine-fit
  - data.batch-derived-views
sources:
  - "book: Martin Kleppmann, Designing Data-Intensive Applications, first edition, data.pdf; Chapter 3: Storage and Retrieval"
source_confidence: high
last_reviewed: 2026-06-05
---

# Analytical Column Storage

## Intent

Match storage layout to analytical access patterns.

## Use when

- Queries aggregate or filter over large datasets while reading few columns.
- The workload is analytical rather than transaction-oriented.

## Avoid when

- Workloads frequently update individual rows or require low-latency point writes.
- Queries usually need complete records by primary key.

## Context and problem

Row-oriented storage wastes I/O for analytical scans that touch only selected columns over many records.

## Forces

- Scan efficiency versus row update cost
- Compression versus write flexibility
- Analytical throughput versus transactional latency

## Guidance

Store analytical data in columnar formats or warehouses when scan and aggregation efficiency dominate. Feed it from operational systems through controlled dataflows.

## Implementation moves

- Identify query columns and aggregation patterns.
- Partition and sort data by common filters.
- Choose compression and encoding suited to column values.
- Load data through batch or streaming pipelines from source systems.

## Checks

- Do queries avoid reading unused columns?
- Is freshness good enough for business use?
- Are operational writes isolated from analytical scans?

## Failure modes

- Running heavy analytics directly on OLTP tables.
- Using column stores for high-churn row updates.
- Ignoring partition pruning and data layout.

## Agent trigger hints

Use this pattern when the user says or implies:

- columnar storage
- data warehouse
- olap
- analytics performance

## Source notes

Synthesized from Chapter 3: Storage and Retrieval in the locally extracted `data-chapters/` text. This file stores original guidance and source pointers only, not source excerpts.
