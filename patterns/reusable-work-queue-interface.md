---
id: platform.reusable-work-queue-interface
title: Reusable Work Queue Interface
type: architecture-pattern
status: draft
summary: Build batch work queues from a generic queue manager, a versioned source interface, and worker containers launched by the orchestrator.
tags:
  - platform-engineering
  - data-platform
  - scalability
  - operability
  - modular-architecture
  - implementation-planning
  - runtime-operations
  - module-boundaries
  - idempotency
  - kubernetes
  - work-queue
aliases:
  - work queue pattern
  - batch work queue
  - reusable queue manager
  - worker container interface
  - job queue
applies_when:
  - A batch workload contains many independent items that can be processed in parallel.
  - The source of items and the item-processing logic vary, but queue management is generic.
  - An orchestrator can launch, track, retry, and record worker jobs.
avoid_when:
  - Work items depend on each other or require coordinated aggregation before completion.
  - The workload needs streaming stateful processing rather than independent batch jobs.
  - The system cannot make work processing idempotent or safely retryable.
related:
  - platform.workflow-queue-composition
  - platform.coordinated-batch-aggregation
  - platform.container-contracts-for-reuse
  - data.idempotent-event-processing
sources:
  - 'book: Brendan Burns, Designing Distributed Systems, Chapter 10: Work Queue Systems'
source_confidence: high
last_reviewed: 2026-06-05
---

# Reusable Work Queue Interface

## Intent

Separate generic queue management from workload-specific item discovery and item processing so batch systems can be assembled from reusable containers.

## Use when

- A workload has many independent items, such as files, media assets, reports, tenants, or records.
- The platform can provide common scheduling, retry, completion tracking, and scaling.
- Item discovery is application-specific but can be exposed through a narrow source API.
- Workers can receive one item through a file, environment variable, queue message, or mounted config.
- The team wants to reuse queue infrastructure across many batch tasks.

## Avoid when

- Items must be processed in a strict global order.
- Work items have cross-item dependencies that require coordination during processing.
- Completion cannot be detected reliably by the orchestrator or queue manager.
- Retrying a work item would corrupt output or duplicate side effects.
- The orchestration API is too slow or expensive for the item granularity.

## Context and problem

Many batch systems repeat the same infrastructure: list work, identify unfinished items, start workers, retry failures, record completion, and scale parallelism. The application-specific parts are usually the source of work items and the logic for processing one item.

A reusable work queue factors these concerns into contracts. A source container exposes the list and details of work items. A generic queue manager compares desired work with observed jobs. Worker containers process individual items through a simple input contract. The orchestrator supplies reliable job execution and status.

## Forces

- Reusable queue infrastructure versus workload-specific sources.
- Parallel throughput versus resource bursts.
- Simple worker interface versus security and data-passing constraints.
- Retry reliability versus idempotent side effects.
- Orchestrator state reuse versus custom queue storage.
- Fine-grained jobs versus scheduling overhead.

## Guidance

Build the queue manager as reusable infrastructure. Push only item discovery and item processing into workload-specific containers. Version the source API from the beginning, and choose a worker input contract that is simple for shell scripts and batch tools.

Use the orchestrator's job abstraction when it can reliably run work to completion and report status. Track work by item id and job annotations or labels. Make every worker safe to retry, or explicitly encode non-retryable behavior and compensation.

## Implementation moves

- Define a versioned source API that lists item ids and returns item details.
- Keep processed and in-progress state in orchestrator job metadata when practical.
- Use stable item ids as job names, labels, or annotations.
- Pass work data to workers through a file, mounted config, message, or environment variable that avoids unauthenticated remote calls.
- Make worker containers small, single-purpose, and parameterized.
- Configure job restart and retry policy based on idempotency.
- Add concurrency limits so the queue cannot burst beyond cluster capacity.
- Measure interarrival time, processing time, backlog age, and failure count.
- Scale parallelism so effective processing time stays below item interarrival time with safety margin.
- Compose multiple worker containers only when their contracts remain clear and reusable.

## Checks

- Are work items independent and safe to run in parallel?
- Is the source API versioned and documented?
- Can the queue manager distinguish new, running, succeeded, and failed items?
- Are item ids stable enough to prevent duplicate jobs?
- Is retry safe for the worker's side effects?
- Is the item granularity large enough to justify a scheduled job?
- Are backlog age and processing time monitored?
- Does concurrency have an upper bound tied to cluster capacity and cost?

## Failure modes

- Building a custom queue manager for every batch task.
- Letting the source container own too much generic queue state.
- Using remote worker APIs without authentication when a file or mounted input would be safer.
- Creating one job per tiny item and overwhelming the orchestrator.
- Retrying non-idempotent workers and duplicating output.
- Scaling workers to clear a burst and starving other workloads.
- Omitting API versioning and making source evolution expensive.

## Agent trigger hints

Use this pattern when the user says or implies:

- work queue
- batch jobs
- process each file
- worker container
- Kubernetes Job
- queue backlog
- dynamic worker scaling
- generic queue manager

## Source notes

Synthesized from Chapter 10's generic work queue, source API, worker interface, Kubernetes Job usage, dynamic scaling, and multi-worker composition. This file contains original guidance and source pointers only.
