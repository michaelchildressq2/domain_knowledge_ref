---
id: platform.workflow-queue-composition
title: Workflow Queue Composition
type: architecture-pattern
status: draft
summary: Compose multi-stage batch workflows with explicit copier, filter, splitter, sharder, and merger queue patterns backed by reliable pub/sub infrastructure.
tags:
  - platform-engineering
  - data-platform
  - scalability
  - high-availability
  - modular-architecture
  - design-review
  - runtime-operations
  - idempotency
  - testing
  - event-driven
  - workflow
aliases:
  - event-driven batch workflow
  - queue pipeline
  - copier filter splitter sharder merger
  - pub/sub workflow
  - DAG workflow
applies_when:
  - Batch processing has multiple stages and outputs from one stage trigger later stages.
  - Work needs to be copied, filtered, split, sharded, or merged across queues.
  - A pub/sub service or queue platform can persist messages and deliver them reliably.
avoid_when:
  - A single work queue or single job is enough.
  - The workflow requires cyclic dependencies or unbounded feedback loops.
  - Strong transactional consistency is required across all stages.
related:
  - platform.reusable-work-queue-interface
  - platform.coordinated-batch-aggregation
  - platform.event-driven-function-boundaries
  - data.event-log-as-source
sources:
  - 'book: Brendan Burns, Designing Distributed Systems, Chapter 11: Event-Driven Batch Processing'
source_confidence: high
last_reviewed: 2026-06-05
---

# Workflow Queue Composition

## Intent

Make multi-stage batch workflows understandable and evolvable by naming the queue composition patterns instead of hiding them in ad hoc glue.

## Use when

- One work item needs multiple downstream actions.
- Some items should continue to one queue while others go to different queues.
- A workflow should isolate rollout or failure impact by sharding queues.
- Multiple independent sources need to feed one shared processing stage.
- Operators need a clear directed acyclic graph of batch stages and queue topics.

## Avoid when

- A single source and worker queue solves the problem.
- Later stages require all earlier work to be complete before any item proceeds; use coordinated batch aggregation or join instead.
- Events must be consumed in one strict global order.
- The queue platform cannot provide the durability, ordering, partitioning, or replay behavior the workflow needs.
- The design would create cycles that are hard to reason about or bound.

## Context and problem

Batch workflows often start as one queue feeding another. As requirements grow, the workflow needs branching, duplication, filtering, sharding, and convergence. Without named composition patterns, the system becomes a tangle of topics, scripts, and workers that is hard to change or diagnose.

Queue composition gives agents a vocabulary: a copier duplicates work to multiple queues, a filter removes items that do not match criteria, a splitter routes every item to one or more queues based on attributes, a sharder spreads work across equivalent queues, and a merger combines multiple queues into one source.

## Forces

- Workflow clarity versus ad hoc glue code.
- Parallelism versus operational complexity.
- Reliable delivery versus duplicate processing.
- Failure isolation versus more topics and workers.
- Reuse of generic components versus workload-specific routing rules.
- Pub/sub durability versus queue platform cost and tuning.

## Guidance

Represent the workflow as a directed acyclic graph of queues and stages. Name every routing stage by its pattern and make its criteria visible. Use pub/sub or queue infrastructure to persist messages between stages rather than relying on local files for distributed workflows.

Use sharding for failure isolation, staged rollout, and regional distribution, not only throughput. Use splitting and filtering when they communicate intent more clearly than a pile of duplicated predicates. Use merging when several independent sources should feed one common processing system, but do not mistake merger for a completeness barrier.

## Implementation moves

- Draw the workflow DAG with queue names, stage names, and routing rules.
- Assign each routing stage one primary role: copier, filter, splitter, sharder, or merger.
- Define message schemas, ids, idempotency keys, and versioning for each topic or queue.
- Use durable pub/sub topics for distributed workflows.
- Configure replication and partitions for topics based on reliability and throughput needs.
- Keep routing stages stateless where possible and externalize only necessary state.
- Make sharding functions deterministic and able to route around unhealthy shards.
- Add dead-letter queues and retry policies per stage.
- Track per-stage input rate, output rate, lag, failures, duplicate count, and age.
- Use staged rollout per shard or stage so a bad worker affects a bounded fraction of work.

## Checks

- Is the workflow graph acyclic and understandable from the deployment artifacts?
- Does each queue have a documented producer and consumer set?
- Are routing criteria versioned and tested?
- Can a duplicate message be processed safely?
- Does a merger require completeness, or is simple interleaving enough?
- Can one unhealthy shard drain or reroute without losing work?
- Are topic partitions and replication factors tied to throughput and durability goals?
- Are dead-letter queues monitored and owned?

## Failure modes

- Building a hidden workflow where every worker publishes to arbitrary topics.
- Using local filesystem directories for a workflow that must run across nodes.
- Treating a merger as a join and starting aggregate work before all inputs exist.
- Creating cycles that repeatedly trigger work.
- Missing idempotency keys and duplicating side effects during retries.
- Using one shared topic for unrelated stages and losing ownership clarity.
- Sharding a queue but rolling out all shards at once, eliminating the isolation benefit.

## Agent trigger hints

Use this pattern when the user says or implies:

- workflow queues
- batch pipeline
- copy this work to multiple queues
- filter queue items
- splitter
- merge queues
- Kafka topics
- pub/sub workflow

## Source notes

Synthesized from Chapter 11's event-driven batch patterns for copier, filter, splitter, sharder, merger, user-signup workflow, and pub/sub infrastructure. This file contains original guidance and source pointers only.
