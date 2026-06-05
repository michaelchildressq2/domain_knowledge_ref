---
id: data.graph-relationship-modeling
title: Graph Relationship Modeling
type: architecture-pattern
status: draft
summary: Use graph modeling when relationships between entities are central, variable, and queried across multiple hops.
tags:
  - data-systems
  - data-modeling
  - graph-database
  - query-patterns
  - design-review
  - cloud-agnostic
aliases:
  - graph data model
  - relationship-heavy data
  - property graph
applies_when:
  - Queries traverse relationships of variable depth or type.
  - The domain has many-to-many relationships that are first-class facts.
avoid_when:
  - Queries are simple key lookups or fixed joins over well-structured tables.
  - The team lacks operational maturity for the graph technology and relational queries are adequate.
related:
  - data.polyglot-persistence-fit
  - data.declarative-query-boundaries
  - data.unbundled-derived-data
sources:
  - "book: Martin Kleppmann, Designing Data-Intensive Applications, first edition, data.pdf; Chapter 2: Data Models and Query Languages"
source_confidence: high
last_reviewed: 2026-06-05
---

# Graph Relationship Modeling

## Intent

Make relationship traversal explicit and efficient when relationships are the core of the problem.

## Use when

- Queries traverse relationships of variable depth or type.
- The domain has many-to-many relationships that are first-class facts.

## Avoid when

- Queries are simple key lookups or fixed joins over well-structured tables.
- The team lacks operational maturity for the graph technology and relational queries are adequate.

## Context and problem

Relational and document models can represent relationships, but complex multi-hop traversal may become verbose, slow, or application-driven.

## Forces

- Relationship expressiveness versus operational familiarity
- Traversal flexibility versus transaction scope
- Specialized query power versus ecosystem maturity

## Guidance

Model entities and relationships directly when relationship queries drive product behavior. Keep transactional boundaries and derived projections clear.

## Implementation moves

- Identify relationship traversal queries and depth requirements.
- Model relationship properties explicitly.
- Avoid duplicating graph facts across uncoordinated stores.
- Benchmark representative traversals and updates.

## Checks

- Are important queries naturally expressed as graph traversals?
- Can updates preserve relationship invariants?
- Do operators know how to monitor and back up the graph store?

## Failure modes

- Using a graph database for simple lookup data.
- Ignoring authorization and tenancy constraints during traversal.
- Treating graph projections as authoritative without a source-of-truth plan.

## Agent trigger hints

Use this pattern when the user says or implies:

- graph database
- many to many relationships
- cypher
- relationship traversal

## Source notes

Synthesized from Chapter 2: Data Models and Query Languages in the locally extracted `data-chapters/` text. This file stores original guidance and source pointers only, not source excerpts.
