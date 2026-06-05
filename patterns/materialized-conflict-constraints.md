---
id: data.materialized-conflict-constraints
title: Materialized Conflict Constraints
type: architecture-pattern
status: draft
summary: Materialize conflicts so the database can enforce invariants that would otherwise span predicate reads or missing rows.
tags:
  - data-systems
  - transactions
  - constraints
  - consistency
  - database
  - cloud-agnostic
aliases:
  - materialize conflicts
  - write skew prevention
  - constraint row
applies_when:
  - An invariant depends on absence, counts, ranges, or predicates rather than one updated row.
  - Snapshot isolation permits write skew for the workflow.
avoid_when:
  - Serializable isolation or native exclusion constraints already protect the invariant.
  - The invariant is advisory and can be repaired asynchronously.
related:
  - data.isolation-level-explicitness
  - data.transaction-boundary-fit
sources:
  - "book: Martin Kleppmann, Designing Data-Intensive Applications, first edition, data.pdf; Chapter 7: Transactions"
source_confidence: high
last_reviewed: 2026-06-05
---

# Materialized Conflict Constraints

## Intent

Turn abstract predicate conflicts into concrete records or constraints that transaction mechanisms can protect.

## Use when

- An invariant depends on absence, counts, ranges, or predicates rather than one updated row.
- Snapshot isolation permits write skew for the workflow.

## Avoid when

- Serializable isolation or native exclusion constraints already protect the invariant.
- The invariant is advisory and can be repaired asynchronously.

## Context and problem

Some anomalies occur because concurrent transactions read overlapping predicates but write different rows. The database may not see a direct write conflict.

## Forces

- Invariant correctness versus model complexity
- Serializable isolation versus targeted constraints
- Write contention versus safety

## Guidance

Represent the shared invariant as a concrete row, lock, unique key, or constraint so conflicting transactions contend on the same database object.

## Implementation moves

- Identify the predicate or absence condition that must be preserved.
- Create a constraint row, uniqueness key, exclusion constraint, or lock target.
- Update or lock it inside the same transaction as the business change.
- Monitor contention and split constraints if needed.

## Checks

- Do conflicting transactions touch the same protected object?
- Does the database reject the invalid interleaving?
- Is contention acceptable for the invariant value?

## Failure modes

- Checking a predicate then inserting without a lock or constraint.
- Using application mutexes that do not cover every writer.
- Overusing one global lock for unrelated invariants.

## Agent trigger hints

Use this pattern when the user says or implies:

- write skew
- materialize conflicts
- database constraint
- prevent phantom

## Source notes

Synthesized from Chapter 7: Transactions in the locally extracted `data-chapters/` text. This file stores original guidance and source pointers only, not source excerpts.
