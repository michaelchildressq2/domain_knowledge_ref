---
id: ddd.anti-corruption-layer
title: Anti-Corruption Layer
type: architecture-pattern
status: draft
summary: Protect a clean domain model from external or legacy models by translating at an explicit boundary.
tags:
  - domain-driven-design
  - anti-corruption-layer
  - integration
  - legacy-modernization
  - bounded-context
  - modular-architecture
aliases:
  - anticorruption layer
  - translation layer
  - legacy model adapter
applies_when:
  - A bounded context must integrate with an external, legacy, vendor, or upstream model that would distort local concepts.
  - Teams need functional integration but should not become conformists to the other model.
avoid_when:
  - The external model is acceptable as the local model and conforming to it is cheaper.
  - Integration is temporary, low-risk, and translation would cost more than the protected model is worth.
related:
  - ddd.bounded-context-integrity
  - ddd.core-domain-distillation
  - data.schema-registry-contracts
sources:
  - "book: Eric Evans, Domain-Driven Design, 2003 final manuscript; Chapter 14: Maintaining Model Integrity"
source_confidence: high
last_reviewed: 2026-06-05
---

# Anti-Corruption Layer

## Intent

Preserve the integrity of a bounded context while still integrating with another model.

## Use when

- Legacy terminology, data structures, or workflows would pollute the new model if used directly.
- An upstream or vendor model is unstable, awkward, or mismatched to local domain decisions.
- The local context is strategically important enough to justify translation cost.
- A migration needs old and new systems to coexist for several iterations or releases.

## Avoid when

- The other model is the published language everyone intentionally shares.
- The local context has no meaningful model to protect.
- A simple adapter for transport or authentication is enough and semantic translation is not needed.
- Performance constraints make translation unacceptable and the model trade-off is explicit.

## Context and problem

Systems often need to collaborate across bounded contexts. Direct reuse can import another model's assumptions into the local design, especially when integrating with a legacy system. Over time, local names, invariants, and object boundaries bend around foreign concepts until the model loses coherence.

## Forces

- Model protection versus integration cost
- Semantic translation versus data pass-through
- Migration pace versus coexistence complexity
- Local autonomy versus upstream dependency

## Guidance

Put an explicit translation layer between the protected context and the foreign model. Its public interface should speak the local ubiquitous language. Internally, it can call external APIs, parse foreign messages, map identifiers, translate values, and compensate for semantic differences. Keep translation code visible, tested, and owned as an integration boundary, not scattered through domain objects.

Use the layer to support incremental migration, but shrink or remove parts of it when legacy dependencies disappear.

## Implementation moves

- Identify the local concepts that must not be shaped by the external model.
- Define a local-facing service, repository, adapter, or gateway interface in local language.
- Map foreign identifiers, data structures, states, and error semantics explicitly.
- Add contract tests and example mappings for edge cases.
- Keep translation outside aggregate and value object internals.
- Track which parts are temporary migration scaffolding and which are permanent integration policy.

## Checks

- Can domain code remain ignorant of foreign names and data shapes?
- Are all semantic translations located at named boundary components?
- Do tests cover lossy mappings, defaults, errors, and unsupported states?
- Is the translation layer shrinking as legacy responsibilities move?

## Failure modes

- Calling the external API directly from many domain services.
- Translating only field names while importing foreign lifecycle assumptions.
- Hiding complex semantic decisions in generic mappers.
- Letting a temporary layer become an undocumented permanent subsystem.

## Agent trigger hints

Use this pattern when the user says or implies:

- anti-corruption layer
- protect domain model from legacy
- translate between bounded contexts
- legacy modernization
- external model pollution

## Source notes

Synthesized from Chapter 14 in `work/book-domain-driven-design/chapter-out/`, including anti-corruption layer and legacy phasing guidance. This file stores original guidance and source pointers only.
