---
id: data.evolvable-data-systems
title: Evolvable Data Systems
type: architecture-pattern
status: draft
summary: Favor data models, schemas, interfaces, and processing boundaries that can change without coordinated rewrites.
tags:
  - data-systems
  - maintainability
  - schema-evolution
  - modular-architecture
  - refactoring
  - cloud-agnostic
aliases:
  - evolvability
  - change-friendly data systems
  - maintainable data architecture
applies_when:
  - Requirements, data shape, or consumers are expected to change over time.
  - A proposed schema or interface requires many systems to change in lockstep.
avoid_when:
  - The data is a fixed archival format with stable access requirements.
  - A one-off migration can replace the old interface completely.
related:
  - data.compatible-schema-evolution
  - data.document-model-locality
  - data.unbundled-derived-data
sources:
  - "book: Martin Kleppmann, Designing Data-Intensive Applications, first edition, data.pdf; Chapters 1, 2, 4, and 12"
source_confidence: high
last_reviewed: 2026-06-05
---

# Evolvable Data Systems

## Intent

Reduce the cost and risk of inevitable change in data-intensive applications.

## Use when

- Requirements, data shape, or consumers are expected to change over time.
- A proposed schema or interface requires many systems to change in lockstep.

## Avoid when

- The data is a fixed archival format with stable access requirements.
- A one-off migration can replace the old interface completely.

## Context and problem

Data outlives code. Rigid schemas, tight coupling, and coordinated deployment assumptions make change slow and risky.

## Forces

- Expressive models versus compatibility
- Normalization versus locality
- Consumer autonomy versus provider control

## Guidance

Design for gradual evolution. Keep interfaces explicit, prefer compatible changes, isolate model-specific assumptions, and use derived views or adapters when consumers need different shapes.

## Implementation moves

- Identify data contracts and consumer dependencies.
- Choose schema evolution rules before the first breaking change.
- Add fields and new representations before removing old ones.
- Use derived data or translation layers to support divergent read models.

## Checks

- Can old and new code run at the same time?
- Can consumers migrate independently?
- Are data contracts documented and versioned?

## Failure modes

- Assuming a database migration and application deploy are atomic.
- Letting every consumer depend on internal tables.
- Breaking old serialized data when code changes.

## Agent trigger hints

Use this pattern when the user says or implies:

- schema evolution
- evolvable data model
- backward compatibility
- change data model

## Source notes

Synthesized from Chapters 1, 2, 4, and 12 in the locally extracted `data-chapters/` text. This file stores original guidance and source pointers only, not source excerpts.
