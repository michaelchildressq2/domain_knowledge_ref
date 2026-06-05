---
id: ddd.model-driven-design
title: Model Driven Design
type: architecture-pattern
status: draft
summary: Keep the core design and implementation closely mapped to the domain model so analysis and code evolve together.
tags:
  - domain-driven-design
  - domain-modeling
  - software-design
  - implementation-planning
  - module-boundaries
  - maintainability
  - refactoring
  - design-review
aliases:
  - model-driven design
  - analysis design alignment
  - model code alignment
applies_when:
  - The team has a domain model but implementation decisions are drifting into an unrelated procedural or data-centric design.
  - Important domain insights arise during coding and need to feed back into the model.
avoid_when:
  - The implementation technology cannot express the model directly enough to make the mapping maintainable.
  - The system is dominated by technical transformation logic with little domain behavior.
related:
  - ddd.ubiquitous-language
  - ddd.layered-domain-architecture
  - ddd.supple-domain-design
sources:
  - "book: Eric Evans, Domain-Driven Design, 2003 final manuscript; Chapter 3: Binding Model and Implementation"
source_confidence: high
last_reviewed: 2026-06-05
---

# Model Driven Design

## Intent

Make the domain model the working foundation of the software, not a separate analysis document.

## Use when

- A conceptual model exists but code only uses similar names over unrelated structures.
- Developers rediscover domain concepts during implementation because the analysis model is impractical.
- The design is hard to explain in domain terms even though the problem is domain-heavy.

## Avoid when

- A purchased package or external protocol dictates the model and local code should remain an adapter.
- Performance or platform constraints require a technical model that cannot be hidden behind a domain-facing API.
- The model is speculative and has not been exercised through implementation.

## Context and problem

Analysis models often organize business concepts without considering construction. Implementations then grow separately, losing the insights captured by analysts and domain experts. Once the mapping becomes loose or complex, both the model and the software become suspect.

## Forces

- Conceptual fidelity versus implementation practicality
- Domain expressiveness versus technical constraints
- Upfront analysis versus discoveries during coding
- Direct mapping versus accidental framework complexity

## Guidance

Use one model inside a bounded context for analysis, conversation, and core implementation. Design the domain portion of the software so classes, operations, modules, rules, and tests correspond visibly to model concepts. When the model is awkward to implement, search for a better model rather than preserving a paper abstraction. When implementation introduces new language, integrate that discovery back into the model.

Keep the mapping literal where the model carries business meaning, but isolate technical concerns so they do not pollute the model.

## Implementation moves

- Identify the bounded context where one model is expected to hold.
- Map public domain code elements to model concepts and remove accidental synonyms.
- Refactor procedural feature code into model responsibilities when repeated behavior exposes a concept.
- Put infrastructure mapping behind repositories, adapters, or persistence mechanisms.
- Use tests as executable examples of model behavior.
- Review code and diagrams together so changes in one drive changes in the other.

## Checks

- Can a reviewer infer the domain model by reading core domain code?
- Does every important model concept have a visible implementation role?
- Are implementation discoveries reflected in model language and diagrams?
- Is technical mapping complexity isolated from domain decisions?

## Failure modes

- Maintaining a polished analysis model that no longer describes the code.
- Letting framework, database, or UI concerns assign domain responsibilities.
- Forcing an impractical model into code instead of revising the abstraction.
- Allowing multiple implicit models inside one context.

## Agent trigger hints

Use this pattern when the user says or implies:

- model-driven design
- domain model does not match code
- analysis model versus implementation
- code should express the business
- design drift from model

## Source notes

Synthesized from Chapter 3 in `work/book-domain-driven-design/chapter-out/`. This file stores original guidance and source pointers only.
