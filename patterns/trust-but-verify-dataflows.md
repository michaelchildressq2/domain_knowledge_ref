---
id: data.trust-but-verify-dataflows
title: Trust But Verify Dataflows
type: governance-pattern
status: draft
summary: Continuously verify derived data against source facts to detect corruption, missed events, and broken assumptions.
tags:
  - data-systems
  - data-quality
  - derived-data
  - observability
  - runtime-operations
  - cloud-agnostic
aliases:
  - data reconciliation
  - verify derived data
  - pipeline correctness checks
applies_when:
  - Business decisions depend on derived datasets, indexes, or materialized views.
  - Pipelines are asynchronous and may miss, duplicate, or corrupt updates.
avoid_when:
  - The derived data is disposable and manually inspected only.
  - A fully transactional boundary guarantees source and view consistency.
related:
  - data.unbundled-derived-data
  - data.eventual-consistency-boundaries
  - data.batch-derived-views
sources:
  - "book: Martin Kleppmann, Designing Data-Intensive Applications, first edition, data.pdf; Chapter 12: The Future of Data Systems"
source_confidence: high
last_reviewed: 2026-06-05
---

# Trust But Verify Dataflows

## Intent

Catch silent data corruption and drift before users or decisions rely on wrong derived state.

## Use when

- Business decisions depend on derived datasets, indexes, or materialized views.
- Pipelines are asynchronous and may miss, duplicate, or corrupt updates.

## Avoid when

- The derived data is disposable and manually inspected only.
- A fully transactional boundary guarantees source and view consistency.

## Context and problem

Asynchronous dataflows can fail partially. Without independent checks, derived systems may appear healthy while being wrong.

## Forces

- Trust in automation versus independent evidence
- Verification cost versus correctness risk
- Freshness versus reconciliation depth

## Guidance

Add reconciliation, invariants, sampling, checksums, and end-to-end data quality metrics. Treat derived data correctness as observable production behavior.

## Implementation moves

- Define invariants between source and derived views.
- Run periodic reconciliation or sampled comparisons.
- Track event counts, lag, duplicates, and dead letters.
- Create repair workflows for detected divergence.

## Checks

- Can the team detect a missing day of events?
- Are derived totals reconcilable with source totals?
- Is repair automated or at least rehearsed?

## Failure modes

- Monitoring only job success, not output correctness.
- Assuming no news means data is accurate.
- Finding divergence with no safe rebuild path.

## Agent trigger hints

Use this pattern when the user says or implies:

- data reconciliation
- verify pipeline
- derived data correctness
- data quality checks

## Source notes

Synthesized from Chapter 12: The Future of Data Systems in the locally extracted `data-chapters/` text. This file stores original guidance and source pointers only, not source excerpts.
