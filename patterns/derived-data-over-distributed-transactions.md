---
id: data.derived-data-over-distributed-transactions
title: Derived Data Over Distributed Transactions
type: decision-guide
status: draft
summary: Prefer replayable derived dataflows over distributed transactions when integrating heterogeneous stores for read optimization.
tags:
  - data-systems
  - data-integration
  - distributed-workflow
  - derived-data
  - design-review
  - cloud-agnostic
aliases:
  - avoid distributed transactions
  - derived data instead of 2pc
  - dual write alternative
applies_when:
  - A system writes to an OLTP store and also updates search, cache, analytics, or graph views.
  - Distributed transactions across heterogeneous systems are proposed for synchronization.
avoid_when:
  - The business invariant truly requires atomic commit across participants and supported 2PC is acceptable.
  - The derived system cannot be rebuilt or reconciled from source changes.
related:
  - data.unbundled-derived-data
  - data.event-log-as-source
  - data.saga-with-compensation
sources:
  - "book: Martin Kleppmann, Designing Data-Intensive Applications, first edition, data.pdf; Chapter 12: The Future of Data Systems"
source_confidence: high
last_reviewed: 2026-06-05
---

# Derived Data Over Distributed Transactions

## Intent

Integrate specialized systems with recoverable dataflows rather than brittle dual writes.

## Use when

- A system writes to an OLTP store and also updates search, cache, analytics, or graph views.
- Distributed transactions across heterogeneous systems are proposed for synchronization.

## Avoid when

- The business invariant truly requires atomic commit across participants and supported 2PC is acceptable.
- The derived system cannot be rebuilt or reconciled from source changes.

## Context and problem

Distributed transactions across diverse stores are operationally hard, while dual writes can leave systems inconsistent.

## Forces

- Atomicity versus availability
- Specialized reads versus integration complexity
- Replayability versus immediate consistency

## Guidance

Use one authoritative write path, publish changes to a durable log or capture stream, and update derived systems asynchronously with monitoring and repair.

## Implementation moves

- Choose the authoritative system for each fact.
- Emit or capture changes durably after commit.
- Update derived stores from the change stream.
- Provide rebuild and reconciliation jobs.

## Checks

- Can the derived store catch up after downtime?
- Can missed updates be detected and replayed?
- Does any user action require immediate derived-store consistency?

## Failure modes

- Writing database and search index directly in one request without recovery.
- Using async derived data for hard uniqueness constraints.
- Lacking observability for lag or divergence.

## Agent trigger hints

Use this pattern when the user says or implies:

- dual writes
- distributed transaction
- derived data
- search index consistency

## Source notes

Synthesized from Chapter 12: The Future of Data Systems in the locally extracted `data-chapters/` text. This file stores original guidance and source pointers only, not source excerpts.
