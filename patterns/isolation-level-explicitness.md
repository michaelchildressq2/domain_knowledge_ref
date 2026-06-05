---
id: data.isolation-level-explicitness
title: Isolation Level Explicitness
type: decision-guide
status: draft
summary: Choose isolation levels by the anomalies the application can tolerate, not by database defaults or ACID labels.
tags:
  - data-systems
  - transactions
  - isolation-levels
  - consistency
  - implementation-planning
  - cloud-agnostic
aliases:
  - read committed
  - snapshot isolation
  - serializable
  - transaction anomalies
applies_when:
  - Concurrent transactions can read or write overlapping data.
  - A team relies on default isolation without knowing its anomalies.
avoid_when:
  - The data is append-only and conflicts cannot occur.
  - A single-threaded serial executor enforces the required ordering.
related:
  - data.transaction-boundary-fit
  - data.materialized-conflict-constraints
sources:
  - "book: Martin Kleppmann, Designing Data-Intensive Applications, first edition, data.pdf; Chapter 7: Transactions"
source_confidence: high
last_reviewed: 2026-06-05
---

# Isolation Level Explicitness

## Intent

Make concurrency semantics visible enough that application invariants are intentionally protected.

## Use when

- Concurrent transactions can read or write overlapping data.
- A team relies on default isolation without knowing its anomalies.

## Avoid when

- The data is append-only and conflicts cannot occur.
- A single-threaded serial executor enforces the required ordering.

## Context and problem

Different isolation levels allow different anomalies. Defaults such as read committed or snapshot isolation may not prevent lost updates, write skew, or phantoms.

## Forces

- Correctness versus concurrency
- Database defaults versus application invariants
- Performance versus anomaly prevention

## Guidance

Map each invariant to the anomaly that could violate it. Use constraints, explicit locks, compare-and-set, materialized conflicts, or serializable isolation where needed.

## Implementation moves

- List concurrent workflows that touch related data.
- Identify dirty reads, lost updates, write skew, and phantom risks.
- Select isolation level or explicit concurrency control.
- Test anomalies with concurrent execution, not only sequential cases.

## Checks

- Can two valid transactions combine into an invalid result?
- Does snapshot isolation permit write skew here?
- Are uniqueness and foreign-key constraints doing needed work?

## Failure modes

- Equating ACID with serializable isolation.
- Relying on tests that never run concurrently.
- Using weak isolation for financial or quota invariants without safeguards.

## Agent trigger hints

Use this pattern when the user says or implies:

- isolation level
- write skew
- serializable
- snapshot isolation
- lost update

## Source notes

Synthesized from Chapter 7: Transactions in the locally extracted `data-chapters/` text. This file stores original guidance and source pointers only, not source excerpts.
