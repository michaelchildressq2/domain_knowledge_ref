---
id: data.event-log-as-source
title: Event Log As Source
type: architecture-pattern
status: draft
summary: Use an append-only event log as a durable integration backbone when consumers need replayable ordered facts.
tags:
  - data-systems
  - event-log
  - stream-processing
  - event-driven
  - data-pipeline
  - cloud-agnostic
aliases:
  - commit log
  - event sourcing log
  - kafka topic source
applies_when:
  - Multiple consumers need to derive different views from the same sequence of changes.
  - Reprocessing or rebuilding derived state is an important recovery capability.
avoid_when:
  - Events cannot be represented as durable facts.
  - The system needs synchronous request-response semantics for every interaction.
related:
  - data.stream-derived-views
  - data.idempotent-event-processing
  - data.unbundled-derived-data
sources:
  - "book: Martin Kleppmann, Designing Data-Intensive Applications, first edition, data.pdf; Chapters 10, 11, and 12"
source_confidence: high
last_reviewed: 2026-06-05
---

# Event Log As Source

## Intent

Give downstream systems a durable, replayable history of changes.

## Use when

- Multiple consumers need to derive different views from the same sequence of changes.
- Reprocessing or rebuilding derived state is an important recovery capability.

## Avoid when

- Events cannot be represented as durable facts.
- The system needs synchronous request-response semantics for every interaction.

## Context and problem

Point-to-point integration and direct dual writes make it hard to rebuild derived data or add consumers safely.

## Forces

- Replayability versus storage retention cost
- Loose coupling versus event contract discipline
- Ordering guarantees versus partitioned throughput

## Guidance

Publish immutable events to a durable log with explicit keys, schemas, retention, and ordering expectations. Let consumers maintain their own derived state.

## Implementation moves

- Define events as facts that happened.
- Choose partition keys matching ordering needs.
- Set retention for replay and audit requirements.
- Track consumer offsets and processing status.

## Checks

- Can a new consumer build state from history?
- Are events immutable and versioned?
- Is ordering guaranteed at the granularity consumers need?

## Failure modes

- Publishing commands or mutable snapshots as events without semantics.
- Using short retention when rebuild is required.
- Assuming total order across partitions.

## Agent trigger hints

Use this pattern when the user says or implies:

- event log
- kafka as source
- replay events
- event sourcing

## Source notes

Synthesized from Chapters 10, 11, and 12 in the locally extracted `data-chapters/` text. This file stores original guidance and source pointers only, not source excerpts.
