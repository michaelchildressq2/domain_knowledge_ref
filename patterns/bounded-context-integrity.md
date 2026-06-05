---
id: ddd.bounded-context-integrity
title: Bounded Context Integrity
type: architecture-pattern
status: draft
summary: Define where each model applies and keep that context internally consistent through language, ownership, integration, and tests.
tags:
  - domain-driven-design
  - bounded-context
  - model-integrity
  - modular-architecture
  - module-boundaries
  - data-contracts
  - team-boundaries
  - integration
aliases:
  - bounded context
  - context map
  - model integrity
applies_when:
  - Different teams or subsystems use the same terms with different meanings.
  - A single enterprise model is becoming too costly, political, or inconsistent to maintain.
avoid_when:
  - The area is small enough and coordinated enough to keep one unified model cheaply.
  - The proposed boundary is only an org chart artifact and does not reflect model differences.
related:
  - ddd.ubiquitous-language
  - ddd.anti-corruption-layer
  - ddd.core-domain-distillation
sources:
  - "book: Eric Evans, Domain-Driven Design, 2003 final manuscript; Chapter 14: Maintaining Model Integrity"
source_confidence: high
last_reviewed: 2026-06-05
---

# Bounded Context Integrity

## Intent

Prevent model meanings from splintering silently by naming the boundary where each model is valid.

## Use when

- Teams reuse a concept name but attach different rules, attributes, or lifecycle assumptions.
- Integrating code from different subsystems produces mysterious data or behavior defects.
- A shared model is too large for the team to keep unified through ordinary communication.
- The system needs a context map before integration decisions can be made responsibly.

## Avoid when

- A smaller team can keep one model unified with continuous integration and shared language.
- A boundary would mostly protect team autonomy while increasing translation cost.
- The difference is only technical packaging, not a difference in model meaning.

## Context and problem

Large systems rarely sustain one fully unified model. Different teams, legacy systems, packages, and applications develop different assumptions. If those differences are not explicit, code may be combined as if the same terms mean the same things, creating contradictions and unreliable behavior.

## Forces

- Model unity versus coordination cost
- Team autonomy versus integration friction
- Local conceptual fit versus enterprise-wide consistency
- Boundary clarity versus translation overhead

## Guidance

Name each bounded context and state where its model applies. Keep the model internally consistent within that boundary through shared language, code ownership, tests, and integration discipline. Draw a context map that records relationships between contexts, including shared kernels, customer-supplier dependencies, conformist dependencies, separate ways, open host services, published languages, and anti-corruption layers.

Choose boundary size deliberately. Larger contexts reduce translation but require stronger coordination. Smaller contexts protect local clarity but increase integration work.

## Implementation moves

- Inventory terms whose meaning differs by team, subsystem, package, or workflow.
- Name bounded contexts and assign ownership for model consistency inside each one.
- Draw a context map with relationship types and integration responsibilities.
- Add tests around contact points where meanings cross boundaries.
- Use continuous integration and shared review inside contexts that must stay unified.
- Revisit boundaries when team coordination, model complexity, or integration cost changes.

## Checks

- Does every important model term have a known context?
- Can teams explain which model owns a rule or lifecycle assumption?
- Are context relationships explicit enough to guide API and data translation?
- Are integration tests focused on semantic contact points, not only transport mechanics?

## Failure modes

- Pretending one enterprise model exists while teams maintain different assumptions.
- Creating context boundaries that mirror teams but ignore domain meaning.
- Sharing database tables or objects across contexts without a relationship strategy.
- Letting context maps become stale architecture posters.

## Agent trigger hints

Use this pattern when the user says or implies:

- bounded context
- context map
- model integrity
- same term different meaning
- team boundaries and domain model

## Source notes

Synthesized from Chapter 14 in `work/book-domain-driven-design/chapter-out/`, especially bounded context, continuous integration, and context map guidance. This file stores original guidance and source pointers only.
