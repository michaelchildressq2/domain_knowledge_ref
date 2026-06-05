---
id: data.document-model-locality
title: Document Model Locality
type: architecture-pattern
status: draft
summary: Use document storage when related data is usually read and written together as one aggregate.
tags:
  - data-systems
  - data-modeling
  - document-database
  - query-patterns
  - implementation-planning
  - cloud-agnostic
aliases:
  - document database fit
  - aggregate document
  - json document locality
applies_when:
  - Application access commonly needs a whole nested record or aggregate at once.
  - Relationships inside the aggregate are mostly one-to-few and owned together.
avoid_when:
  - The data has many-to-many relationships or frequent cross-document joins.
  - Independent updates to nested parts create contention or duplication.
related:
  - data.polyglot-persistence-fit
  - data.compatible-schema-evolution
sources:
  - "book: Martin Kleppmann, Designing Data-Intensive Applications, first edition, data.pdf; Chapter 2: Data Models and Query Languages"
source_confidence: high
last_reviewed: 2026-06-05
---

# Document Model Locality

## Intent

Exploit document locality without turning the application into a manual join engine.

## Use when

- Application access commonly needs a whole nested record or aggregate at once.
- Relationships inside the aggregate are mostly one-to-few and owned together.

## Avoid when

- The data has many-to-many relationships or frequent cross-document joins.
- Independent updates to nested parts create contention or duplication.

## Context and problem

Documents can make aggregate reads simple, but they become awkward when relationships cross aggregate boundaries.

## Forces

- Read locality versus relationship flexibility
- Denormalization versus update consistency
- Schema flexibility versus implicit contracts

## Guidance

Store data as documents when the aggregate boundary matches user workflows and ownership. Keep references explicit for relationships that need independent lifecycle or many-to-many traversal.

## Implementation moves

- Identify the aggregate users read or update together.
- Embed data that shares lifecycle and ownership.
- Reference entities that are shared, large, or independently updated.
- Track duplication and repair mechanisms for denormalized fields.

## Checks

- Can common reads avoid many round trips?
- Do updates usually affect one document?
- Are duplicated values either immutable or repairable?

## Failure modes

- Embedding everything to avoid joins.
- Creating huge documents with unrelated update patterns.
- Letting implicit document schemas diverge silently.

## Agent trigger hints

Use this pattern when the user says or implies:

- document database
- mongodb schema
- embed or reference
- json data model

## Source notes

Synthesized from Chapter 2: Data Models and Query Languages in the locally extracted `data-chapters/` text. This file stores original guidance and source pointers only, not source excerpts.
