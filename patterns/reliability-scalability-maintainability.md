---
id: data.reliability-scalability-maintainability
title: Reliability Scalability Maintainability
type: decision-guide
status: draft
summary: Evaluate data-system designs through reliability, scalability, and maintainability rather than a single technology preference.
tags:
  - data-systems
  - reliability
  - scalability
  - maintainability
  - design-review
  - cloud-agnostic
aliases:
  - rsm
  - system quality tradeoffs
  - data system fundamentals
applies_when:
  - A user asks how to choose or review a data-system architecture.
  - The discussion is focused on a product or database choice without clear quality goals.
avoid_when:
  - The problem is a narrow implementation bug with no architectural decision.
  - A mandatory platform choice has already fixed the relevant trade-offs.
related:
  - data.operability-first-systems
  - data.load-and-performance-characterization
  - data.evolvable-data-systems
sources:
  - "book: Martin Kleppmann, Designing Data-Intensive Applications, first edition, data.pdf; Chapter 1: Reliable, Scalable, and Maintainable Applications"
source_confidence: high
last_reviewed: 2026-06-05
---

# Reliability Scalability Maintainability

## Intent

Keep data-system design grounded in the qualities that determine long-term usefulness under faults, growth, and change.

## Use when

- A user asks how to choose or review a data-system architecture.
- The discussion is focused on a product or database choice without clear quality goals.

## Avoid when

- The problem is a narrow implementation bug with no architectural decision.
- A mandatory platform choice has already fixed the relevant trade-offs.

## Context and problem

Teams often choose storage and processing technologies by feature lists or popularity, then discover too late that operations, growth, or evolution are the real constraint.

## Forces

- Correctness under faults versus implementation simplicity
- Growth headroom versus unnecessary complexity
- Short-term delivery versus long-term change cost

## Guidance

Frame the decision around what can fail, how load may grow, and how the system will change. Compare designs by the risks they handle and the operational burden they create.

## Implementation moves

- Write explicit reliability, scalability, and maintainability goals.
- Identify likely faults, growth dimensions, and change vectors.
- Choose data models, storage engines, and processing patterns that fit those goals.
- Revisit the goals when observed load or team ownership changes.

## Checks

- Can the design name the faults it tolerates?
- Does it describe load using concrete measures rather than vague scale claims?
- Can future developers understand, operate, and evolve it?

## Failure modes

- Optimizing only for peak throughput.
- Choosing a database because it is fashionable.
- Ignoring operational and schema-evolution costs.

## Agent trigger hints

Use this pattern when the user says or implies:

- reliable scalable maintainable
- data system review
- which database architecture
- system qualities

## Source notes

Synthesized from Chapter 1: Reliable, Scalable, and Maintainable Applications in the locally extracted `data-chapters/` text. This file stores original guidance and source pointers only, not source excerpts.
