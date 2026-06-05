---
id: data.unbundled-derived-data
title: Unbundled Derived Data
type: architecture-pattern
status: draft
summary: Compose specialized storage and processing systems by deriving views from a durable source of truth instead of forcing one database to do everything.
tags:
  - data-systems
  - derived-data
  - data-integration
  - event-driven
  - modular-architecture
  - cloud-agnostic
aliases:
  - unbundling databases
  - derived views
  - specialized read models
applies_when:
  - The application needs search, analytics, cache, graph, or serving views that differ from the write model.
  - One database cannot serve all access patterns well.
avoid_when:
  - A single database meets all needs with lower operational cost.
  - The team cannot operate or reconcile multiple derived systems.
related:
  - data.event-log-as-source
  - data.batch-derived-views
  - data.stream-derived-views
sources:
  - "book: Martin Kleppmann, Designing Data-Intensive Applications, first edition, data.pdf; Chapter 12: The Future of Data Systems"
source_confidence: high
last_reviewed: 2026-06-05
---

# Unbundled Derived Data

## Intent

Use specialized tools without losing control of correctness and recovery.

## Use when

- The application needs search, analytics, cache, graph, or serving views that differ from the write model.
- One database cannot serve all access patterns well.

## Avoid when

- A single database meets all needs with lower operational cost.
- The team cannot operate or reconcile multiple derived systems.

## Context and problem

Different access patterns benefit from different storage engines, but maintaining several systems introduces synchronization and consistency risk.

## Forces

- Specialized performance versus operational complexity
- Derived view freshness versus source correctness
- Loose coupling versus dataflow governance

## Guidance

Choose an authoritative source for writes and derive specialized read models through batch or stream dataflows. Treat derived stores as rebuildable, observable projections.

## Implementation moves

- Identify the source of truth for each fact.
- Define dataflows from source to each derived view.
- Make derived views rebuildable from durable inputs.
- Monitor lag, completeness, and divergence.

## Checks

- Can a derived view be deleted and rebuilt?
- Do consumers know freshness and authority boundaries?
- Are dual writes avoided or controlled?

## Failure modes

- Writing independently to source and derived stores.
- Treating a search index as authoritative.
- Adding specialized stores without replay or repair paths.

## Agent trigger hints

Use this pattern when the user says or implies:

- unbundling databases
- derived data
- search index sync
- polyglot persistence architecture

## Source notes

Synthesized from Chapter 12: The Future of Data Systems in the locally extracted `data-chapters/` text. This file stores original guidance and source pointers only, not source excerpts.
