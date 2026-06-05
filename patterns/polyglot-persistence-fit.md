---
id: data.polyglot-persistence-fit
title: Polyglot Persistence Fit
type: decision-guide
status: draft
summary: Choose storage and query models based on access patterns, relationships, consistency needs, and evolution costs.
tags:
  - data-systems
  - data-modeling
  - database
  - design-review
  - cloud-agnostic
aliases:
  - choose database model
  - polyglot persistence
  - database selection
applies_when:
  - A team is choosing between relational, document, graph, search, or key-value stores.
  - The design uses one database model for all use cases despite conflicting access patterns.
avoid_when:
  - Operational constraints require a single approved database and only modeling choices remain.
  - The data volume and access pattern are trivial.
related:
  - data.document-model-locality
  - data.graph-relationship-modeling
  - data.unbundled-derived-data
sources:
  - "book: Martin Kleppmann, Designing Data-Intensive Applications, first edition, data.pdf; Chapter 2: Data Models and Query Languages"
source_confidence: high
last_reviewed: 2026-06-05
---

# Polyglot Persistence Fit

## Intent

Match the persistence model to the problem rather than forcing every problem into one database shape.

## Use when

- A team is choosing between relational, document, graph, search, or key-value stores.
- The design uses one database model for all use cases despite conflicting access patterns.

## Avoid when

- Operational constraints require a single approved database and only modeling choices remain.
- The data volume and access pattern are trivial.

## Context and problem

Different data models make different relationships and queries easy or hard. Choosing poorly pushes complexity into application code and migrations.

## Forces

- Data locality versus join flexibility
- Schema discipline versus agility
- Operational simplicity versus specialized fit

## Guidance

Start from access patterns and invariants. Prefer relational models for flexible joins and many-to-many relationships, document models for contained aggregate locality, graph models for deep relationship traversal, and derived stores for specialized reads.

## Implementation moves

- List core queries, update paths, and relationship cardinalities.
- Identify which invariants must be enforced transactionally.
- Evaluate how schema changes will affect stored data and code.
- Limit specialized stores to cases where their query or operational benefit is clear.

## Checks

- Does the model make common queries simple?
- Are relationships represented without duplicating fragile facts?
- Can the team operate every chosen store?

## Failure modes

- Choosing NoSQL only to avoid schema design.
- Using documents for highly interconnected data.
- Adding a specialized database without an ownership plan.

## Agent trigger hints

Use this pattern when the user says or implies:

- relational vs document
- choose database
- data model decision
- polyglot persistence

## Source notes

Synthesized from Chapter 2: Data Models and Query Languages in the locally extracted `data-chapters/` text. This file stores original guidance and source pointers only, not source excerpts.
