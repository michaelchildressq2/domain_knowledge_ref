---
id: ddd.supple-domain-design
title: Supple Domain Design
type: architecture-pattern
status: draft
summary: Shape important domain code so intention, effects, assertions, and conceptual boundaries are obvious to client developers and maintainers.
tags:
  - domain-driven-design
  - software-design
  - code-readability
  - refactoring
  - testability
  - design-review
aliases:
  - supple design
  - intention revealing interface
  - conceptual contours
applies_when:
  - Core domain code is correct but hard to combine, change, or understand without reading internals.
  - Client code must know implementation details to use domain objects safely.
avoid_when:
  - The code is peripheral infrastructure where standard technical APIs are clearer than domain-specific abstractions.
  - The team is adding speculative flexibility that is not driven by repeated domain pressure.
related:
  - ddd.model-driven-design
  - ddd.specification-business-rules
  - ddd.core-domain-distillation
sources:
  - "book: Eric Evans, Domain-Driven Design, 2003 final manuscript; Chapter 10: Supple Design"
source_confidence: high
last_reviewed: 2026-06-05
---

# Supple Domain Design

## Intent

Make the most important domain code easy to use, safe to compose, and inviting to change.

## Use when

- A domain model exists but client code is still procedural, noisy, or fragile.
- Method names describe mechanisms rather than domain intent.
- Side effects, invariants, and valid combinations are hard to predict.
- Small domain changes require broad code reading because conceptual boundaries are unclear.

## Avoid when

- The area is not core or complex enough to justify careful design work.
- Flexibility is being added for imagined future variation instead of observed domain pressure.
- The design would become more abstract but less readable to the team maintaining it.

## Context and problem

Deep models are only useful when developers can put them to work. If public interfaces hide intent, operations have surprising side effects, and assertions are implicit, every caller must inspect internals. Encapsulation then fails as a cognitive tool, and change slows down even when the model is conceptually sound.

## Forces

- Expressiveness versus over-engineering
- Encapsulation versus hidden side effects
- Simple public concepts versus complex internal mechanisms
- Current clarity versus future change tolerance

## Guidance

Refine important domain code toward intention-revealing interfaces, side-effect-free functions where possible, explicit assertions for commands, and boundaries that follow conceptual contours. Prefer simple combinations of meaningful concepts over layers of indirection. Use tests from the client developer's point of view to force names and effects into the open.

Apply this energy selectively. Supple design matters most in the core domain and in intricate model areas that block change.

## Implementation moves

- Rename public classes, methods, parameters, commands, and events to state domain intent.
- Split queries from commands where side effects make use hard to reason about.
- Make assertions and invariants visible through tests, contracts, or aggregate methods.
- Factor cohesive concepts along natural domain boundaries rather than technical convenience.
- Keep standalone value objects and functions where they make behavior easier to test and combine.
- Refactor awkward client code until it reads in the ubiquitous language.

## Checks

- Can a caller use the public API without reading implementation details?
- Are side effects obvious from the operation name, return type, or contract?
- Do tests document important assertions in domain examples?
- Does a likely model change affect a small, conceptually coherent part of the code?

## Failure modes

- Adding abstraction layers that do not reveal domain intent.
- Hiding commands behind names that sound like pure queries.
- Treating all code as equally deserving of high-design effort.
- Optimizing for generic reuse while weakening the core domain language.

## Agent trigger hints

Use this pattern when the user says or implies:

- supple design
- intention revealing interface
- side-effect-free function
- conceptual contours
- hard to use domain API

## Source notes

Synthesized from Chapter 10 in `work/book-domain-driven-design/chapter-out/`. This file stores original guidance and source pointers only.
