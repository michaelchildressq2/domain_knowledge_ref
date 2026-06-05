---
id: data.log-structured-storage
title: Log Structured Storage
type: architecture-pattern
status: draft
summary: Use append-oriented storage and compaction when write throughput and sequential I/O dominate the workload.
tags:
  - data-systems
  - storage-engine
  - performance
  - database
  - implementation-planning
  - cloud-agnostic
aliases:
  - lsm tree
  - sstable
  - append only storage
applies_when:
  - The system has high write throughput and can tolerate compaction-managed reads.
  - Sequential writes are more efficient than random in-place updates for the storage medium.
avoid_when:
  - Low-latency point reads dominate and compaction/read amplification cannot be managed.
  - Operational constraints cannot tolerate compaction bursts.
related:
  - data.storage-engine-fit
  - data.index-cost-tradeoff
  - data.event-log-as-source
sources:
  - "book: Martin Kleppmann, Designing Data-Intensive Applications, first edition, data.pdf; Chapter 3: Storage and Retrieval"
source_confidence: high
last_reviewed: 2026-06-05
---

# Log Structured Storage

## Intent

Exploit append-only writes while making compaction and read amplification explicit costs.

## Use when

- The system has high write throughput and can tolerate compaction-managed reads.
- Sequential writes are more efficient than random in-place updates for the storage medium.

## Avoid when

- Low-latency point reads dominate and compaction/read amplification cannot be managed.
- Operational constraints cannot tolerate compaction bursts.

## Context and problem

Write-heavy systems need efficient ingestion, but append-only structures accumulate segments that must be merged and indexed.

## Forces

- Sequential write speed versus read amplification
- Compaction efficiency versus latency spikes
- Immutable segments versus storage overhead

## Guidance

Use log-structured designs when write path simplicity and throughput matter. Size memory tables, compaction, and caches for the observed workload.

## Implementation moves

- Use immutable sorted segments or equivalent append structures.
- Maintain sparse indexes and bloom filters where useful.
- Tune compaction strategy for latency and disk amplification.
- Observe compaction backlog and tail latency.

## Checks

- Does compaction keep up with ingestion?
- Are point reads protected from excessive segment checks?
- Does disk headroom account for compaction?

## Failure modes

- Ignoring compaction until storage fills.
- Benchmarking ingestion without read traffic.
- Using append-only storage for workloads needing frequent in-place updates without cost analysis.

## Agent trigger hints

Use this pattern when the user says or implies:

- lsm tree
- sstable
- compaction
- append only database

## Source notes

Synthesized from Chapter 3: Storage and Retrieval in the locally extracted `data-chapters/` text. This file stores original guidance and source pointers only, not source excerpts.
