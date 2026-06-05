---
id: data.saga-with-compensation
title: Saga With Compensation
type: architecture-pattern
status: draft
summary: Coordinate multi-step business workflows with explicit state and compensating actions when one distributed transaction is not appropriate.
tags:
  - data-systems
  - distributed-workflow
  - transactions
  - event-driven
  - implementation-planning
  - cloud-agnostic
aliases:
  - saga pattern
  - compensating transaction
  - long running workflow
applies_when:
  - A workflow spans multiple services, stores, or external systems.
  - Atomic distributed transactions are unavailable, too expensive, or too coupling.
avoid_when:
  - A local database transaction can protect the invariant simply.
  - The business action cannot be compensated and must be coordinated synchronously.
related:
  - data.transaction-boundary-fit
  - data.derived-data-over-distributed-transactions
  - data.idempotent-event-processing
sources:
  - "book: Martin Kleppmann, Designing Data-Intensive Applications, first edition, data.pdf; Chapters 7 and 12"
source_confidence: high
last_reviewed: 2026-06-05
---

# Saga With Compensation

## Intent

Make distributed workflows reliable without pretending all participants share one atomic transaction.

## Use when

- A workflow spans multiple services, stores, or external systems.
- Atomic distributed transactions are unavailable, too expensive, or too coupling.

## Avoid when

- A local database transaction can protect the invariant simply.
- The business action cannot be compensated and must be coordinated synchronously.

## Context and problem

Real workflows often cross transactional boundaries. Without explicit workflow state, partial success and retries create inconsistent outcomes.

## Forces

- Atomicity versus service autonomy
- Compensation versus prevention
- Workflow visibility versus local simplicity

## Guidance

Model the workflow as a sequence of durable steps with explicit status, retries, timeouts, and compensations. Design each step to be idempotent.

## Implementation moves

- Define workflow states and ownership.
- Persist progress before invoking external side effects.
- Make each participant operation idempotent.
- Define compensation or manual repair for each committed step.

## Checks

- Can the workflow resume after coordinator failure?
- Are duplicate commands safe?
- What happens if compensation also fails?

## Failure modes

- Calling remote services inside a local transaction and hoping.
- Leaving partial workflows invisible.
- Using compensation for irreversible actions without business approval.

## Agent trigger hints

Use this pattern when the user says or implies:

- saga pattern
- compensating transaction
- distributed workflow
- avoid 2pc

## Source notes

Synthesized from Chapters 7 and 12 in the locally extracted `data-chapters/` text. This file stores original guidance and source pointers only, not source excerpts.
