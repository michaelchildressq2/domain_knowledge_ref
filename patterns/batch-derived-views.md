---
id: data.batch-derived-views
title: Batch Derived Views
type: architecture-pattern
status: draft
summary: Use batch processing to build reliable derived datasets when freshness can lag and complete input scans are acceptable.
tags:
  - data-systems
  - batch-processing
  - derived-data
  - analytics
  - data-pipeline
  - cloud-agnostic
aliases:
  - batch view
  - offline processing
  - mapreduce derived data
applies_when:
  - A derived dataset, report, index, or warehouse can be recomputed from durable input.
  - Freshness requirements allow scheduled or delayed updates.
avoid_when:
  - The view must reflect changes with low latency.
  - The input is not durable enough to replay after failures.
related:
  - data.event-log-as-source
  - data.stream-derived-views
  - data.unbundled-derived-data
sources:
  - "book: Martin Kleppmann, Designing Data-Intensive Applications, first edition, data.pdf; Chapter 10: Batch Processing"
source_confidence: high
last_reviewed: 2026-06-05
---

# Batch Derived Views

## Intent

Make derived data reproducible and fault-tolerant by computing it from stable inputs.

## Use when

- A derived dataset, report, index, or warehouse can be recomputed from durable input.
- Freshness requirements allow scheduled or delayed updates.

## Avoid when

- The view must reflect changes with low latency.
- The input is not durable enough to replay after failures.

## Context and problem

Derived data can become inconsistent or corrupted. Batch recomputation offers a repair path when the source data is durable.

## Forces

- Freshness versus reproducibility
- Full recomputation cost versus repair confidence
- Throughput versus latency

## Guidance

Use batch jobs for deterministic transformations over bounded inputs. Treat outputs as disposable derived data that can be rebuilt.

## Implementation moves

- Keep raw input immutable or versioned.
- Make transformations deterministic and side-effect free.
- Write outputs atomically or to new locations before publishing.
- Track job inputs, code version, and output version.

## Checks

- Can the output be regenerated from source?
- Does a failed job leave the previous output intact?
- Is freshness acceptable to consumers?

## Failure modes

- Treating derived output as the only source of truth.
- Mixing side effects into batch transformations.
- Overwriting outputs before job success is known.

## Agent trigger hints

Use this pattern when the user says or implies:

- batch processing
- derived data
- mapreduce
- recompute index
- offline pipeline

## Source notes

Synthesized from Chapter 10: Batch Processing in the locally extracted `data-chapters/` text. This file stores original guidance and source pointers only, not source excerpts.
