---
id: data.declarative-query-boundaries
title: Declarative Query Boundaries
type: architecture-pattern
status: draft
summary: Prefer declarative query interfaces when callers should state what data they need without encoding execution strategy.
tags:
  - data-systems
  - query-languages
  - maintainability
  - modular-architecture
  - implementation-planning
  - cloud-agnostic
aliases:
  - declarative queries
  - query optimizer boundary
  - sql style interface
applies_when:
  - A system exposes data access to multiple consumers.
  - Callers are embedding procedural retrieval paths that make optimization difficult.
avoid_when:
  - The operation is inherently procedural or side-effecting.
  - A simple API endpoint is clearer than exposing a general query language.
related:
  - data.polyglot-persistence-fit
  - data.graph-relationship-modeling
sources:
  - "book: Martin Kleppmann, Designing Data-Intensive Applications, first edition, data.pdf; Chapter 2: Data Models and Query Languages"
source_confidence: high
last_reviewed: 2026-06-05
---

# Declarative Query Boundaries

## Intent

Separate data intent from execution details so systems can optimize and evolve storage independently.

## Use when

- A system exposes data access to multiple consumers.
- Callers are embedding procedural retrieval paths that make optimization difficult.

## Avoid when

- The operation is inherently procedural or side-effecting.
- A simple API endpoint is clearer than exposing a general query language.

## Context and problem

Procedural data access couples callers to paths, indexes, and storage layout, making optimization and refactoring harder.

## Forces

- Caller flexibility versus provider control
- Optimization freedom versus predictable behavior
- Expressiveness versus safety

## Guidance

Expose declarative query surfaces when consumers need flexible retrieval and the provider can safely optimize execution. Bound query power with authorization, quotas, and supported patterns.

## Implementation moves

- Identify where callers encode retrieval algorithms.
- Offer a query or filtering interface around stable concepts.
- Hide physical indexes and partitions behind the provider boundary.
- Monitor expensive or unsafe query shapes.

## Checks

- Can storage layout change without client rewrites?
- Are unsupported or dangerous queries rejected?
- Does the provider retain room to optimize execution?

## Failure modes

- Exposing unrestricted queries to untrusted users.
- Leaking physical schema as public contract.
- Replacing every simple command API with a query language.

## Agent trigger hints

Use this pattern when the user says or implies:

- declarative query
- sql vs imperative
- query API
- data access abstraction

## Source notes

Synthesized from Chapter 2: Data Models and Query Languages in the locally extracted `data-chapters/` text. This file stores original guidance and source pointers only, not source excerpts.
