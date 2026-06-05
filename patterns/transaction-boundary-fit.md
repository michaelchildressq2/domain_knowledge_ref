---
id: data.transaction-boundary-fit
title: Transaction Boundary Fit
type: decision-guide
status: draft
summary: Use transactions where they simplify correctness, but keep boundaries aligned with invariants and operational cost.
tags:
  - data-systems
  - transactions
  - consistency
  - database
  - design-review
  - cloud-agnostic
aliases:
  - transaction scope
  - acid tradeoff
  - database transaction decision
applies_when:
  - A workflow updates multiple records or checks invariants before writing.
  - The team is deciding whether eventual consistency or transactions are acceptable.
avoid_when:
  - The operation is naturally independent and does not share invariants.
  - A distributed transaction would couple systems more than the business invariant justifies.
related:
  - data.isolation-level-explicitness
  - data.saga-with-compensation
  - data.derived-data-over-distributed-transactions
sources:
  - "book: Martin Kleppmann, Designing Data-Intensive Applications, first edition, data.pdf; Chapter 7: Transactions"
source_confidence: high
last_reviewed: 2026-06-05
---

# Transaction Boundary Fit

## Intent

Apply transactional guarantees where they buy real correctness rather than habit or avoidance of design.

## Use when

- A workflow updates multiple records or checks invariants before writing.
- The team is deciding whether eventual consistency or transactions are acceptable.

## Avoid when

- The operation is naturally independent and does not share invariants.
- A distributed transaction would couple systems more than the business invariant justifies.

## Context and problem

Transactions are powerful abstractions, but their semantics, isolation level, and distribution costs vary. Misplaced boundaries either hide anomalies or over-couple systems.

## Forces

- Correctness simplicity versus scalability cost
- Local invariants versus distributed workflow
- Isolation strength versus performance

## Guidance

Identify the invariant, then choose the narrowest transaction boundary that protects it. When boundaries cross services or stores, consider derived data, workflows, or compensation instead of defaulting to distributed transactions.

## Implementation moves

- State the invariant that must hold after the operation.
- Identify all reads and writes needed to preserve it.
- Choose isolation level and constraints that prevent relevant anomalies.
- Keep noncritical side effects outside the transaction.

## Checks

- Which anomaly would break the invariant?
- Does the chosen isolation level prevent it?
- Can the transaction remain local to one store or partition?

## Failure modes

- Assuming ACID means serializable behavior.
- Wrapping too much work in one transaction.
- Replacing needed constraints with application hope.

## Agent trigger hints

Use this pattern when the user says or implies:

- transaction boundary
- acid database
- distributed transaction
- data consistency

## Source notes

Synthesized from Chapter 7: Transactions in the locally extracted `data-chapters/` text. This file stores original guidance and source pointers only, not source excerpts.
