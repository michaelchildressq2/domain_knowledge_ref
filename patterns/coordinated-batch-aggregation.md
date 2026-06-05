---
id: platform.coordinated-batch-aggregation
title: Coordinated Batch Aggregation
type: architecture-pattern
status: draft
summary: Use join barriers and reduce stages when parallel batch outputs must be made complete or aggregated into final results.
tags:
  - platform-engineering
  - data-platform
  - data-consistency
  - scalability
  - operability
  - design-review
  - runtime-operations
  - testing
  - idempotency
  - batch-processing
  - aggregation
aliases:
  - join barrier
  - barrier synchronization
  - reduce phase
  - MapReduce reduce
  - batch aggregation
applies_when:
  - Parallel batch stages must converge before deletion, aggregation, reporting, or downstream processing.
  - A complete dataset is required before a stage can run correctly.
  - Partial outputs can be progressively combined with an associative reduce operation.
avoid_when:
  - Simple queue merging is enough and completeness is not required.
  - The reduce operation is not associative or cannot tolerate partial ordering.
  - Waiting for all inputs would create unacceptable latency and approximate results are acceptable.
related:
  - platform.reusable-work-queue-interface
  - platform.workflow-queue-composition
  - platform.scatter-gather-request-parallelism
  - data.batch-derived-views
sources:
  - 'book: Brendan Burns, Designing Distributed Systems, Chapter 12: Coordinated Batch Processing'
source_confidence: high
last_reviewed: 2026-06-05
---

# Coordinated Batch Aggregation

## Intent

Coordinate parallel batch outputs so downstream stages either see a complete input set or a correctly reduced aggregate.

## Use when

- Work has been sharded or parallelized and later stages need to know that all prior work completed.
- It is unsafe to delete original data until all transformed outputs are present.
- Many partial outputs must be aggregated into counts, sums, histograms, model features, reports, or other final results.
- The reduce logic can combine two or more partial outputs into one equivalent partial output.
- The workflow needs a clear distinction between merging streams and synchronizing completeness.

## Avoid when

- Items can flow independently to the next stage without needing the full set.
- A simple merger should interleave outputs from multiple sources.
- The aggregate operation depends on a global ordering that cannot be partitioned.
- The workflow needs continuous streaming results with bounded lateness rather than batch completion.
- Barrier waits would hold resources too long for the value of completeness.

## Context and problem

Parallel batch processing splits work across queues and workers for throughput. Eventually, many workflows need to bring results back together. Sometimes downstream work must wait until every shard is done; other times partial outputs can be combined progressively into a final aggregate.

A join is a barrier: it releases work only after all required prior work is complete. A reduce stage is different: it can start combining partial outputs while upstream work continues, as long as the combine operation preserves correctness. Confusing merge, join, and reduce leads to missing data, slow workflows, or incorrect results.

## Forces

- Completeness guarantees versus batch latency.
- Barrier simplicity versus lost parallelism.
- Progressive reduce versus more complex aggregate logic.
- Data deletion safety versus storage cost.
- Shard independence versus final consistency.
- Resource utilization versus waiting on stragglers.

## Guidance

Use join when the next stage must not begin until the full prior set is known complete. Use reduce when partial results can be safely combined in parallel and repeatedly until a final result remains. Use merger only when streams should be blended without completeness guarantees.

Before deleting originals or publishing final reports, make completeness explicit. Track expected item counts, shard completion markers, or manifest files so the join can prove all work arrived. For reduce, design output schemas so intermediate and final records have the same shape wherever possible.

## Implementation moves

- Define the batch boundary: manifest, input list, snapshot id, partition set, or time window.
- Track expected work items and shard completion independently from worker success logs.
- Use a join barrier before destructive actions, final publication, or stages requiring the complete set.
- Design reduce functions to be associative and preferably commutative.
- Keep reduce input and output schemas compatible so reduction can be repeated hierarchically.
- Store intermediate aggregate metadata such as counts, weights, and source ranges.
- Make reduce jobs idempotent and able to overwrite or version outputs safely.
- Detect stragglers and failed shards before the join waits indefinitely.
- Add timeout and remediation policies for incomplete batches.
- Validate final aggregates against input counts, shard counts, or sampling checks.

## Checks

- Does the next stage require completeness or only a stream of available outputs?
- Is this component a merge, join, or reduce?
- How does the join know the expected item set?
- Can reduce start before all map or shard work is complete?
- Is the reduce operation associative and tested with different grouping orders?
- What prevents original data deletion before transformed data is complete?
- Are stragglers, failed shards, and missing outputs visible?
- Can a batch be rerun without corrupting final aggregates?

## Failure modes

- Using a merger where a join barrier is required and processing incomplete data.
- Waiting for all work before starting a reduce that could have run progressively.
- Deleting source data before all transformed outputs are durable.
- Writing reduce functions that depend on accidental ordering.
- Losing counts or weights needed to merge histograms or averages correctly.
- Waiting forever because the expected item set is not explicit.
- Publishing final aggregate results without reconciling against the input manifest.

## Agent trigger hints

Use this pattern when the user says or implies:

- join all batch outputs
- barrier synchronization
- reduce phase
- aggregate partial results
- MapReduce
- wait until all shards finish
- delete originals after processing
- batch completeness

## Source notes

Synthesized from Chapter 12's join and reduce sections and the image tagging pipeline that combines sharding, multi-worker processing, join, copier, and reduce. This file contains original guidance and source pointers only.
