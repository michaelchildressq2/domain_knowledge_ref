---
id: ddd.knowledge-crunching-loop
title: Knowledge Crunching Loop
type: practice
status: draft
summary: Iterate with domain experts until terminology, scenarios, code, and model structure expose useful domain knowledge.
tags:
  - domain-driven-design
  - domain-modeling
  - requirements-discovery
  - collaboration
  - iterative-design
  - feedback
  - testing
  - design-review
aliases:
  - knowledge crunching
  - model exploration loop
  - domain learning loop
applies_when:
  - A team is building software for a complex business or technical domain it does not yet understand deeply.
  - Requirements describe functions but not the domain concepts, policies, constraints, and language behind them.
avoid_when:
  - The problem is a simple CRUD workflow with stable terminology and little domain behavior.
  - Domain experts are unavailable and the team can only implement a tactical integration or throwaway prototype.
related:
  - ddd.ubiquitous-language
  - ddd.model-driven-design
  - ddd.specification-business-rules
sources:
  - "book: Eric Evans, Domain-Driven Design, 2003 final manuscript; Preface and Chapter 1: Crunching Knowledge"
source_confidence: high
last_reviewed: 2026-06-05
---

# Knowledge Crunching Loop

## Intent

Turn domain learning into a model that changes how the software is named, structured, tested, and discussed.

## Use when

- Developers and domain experts are still translating between separate vocabularies.
- New requirements keep revealing hidden rules, exceptions, policies, or terms.
- The design solves individual features but does not yet make the domain easier to reason about.

## Avoid when

- The team is only automating a small, well-understood procedure with no meaningful domain variation.
- The deadline only permits a disposable spike and there is no intent to evolve the code.
- The domain knowledge is already codified in a stable protocol or purchased package.

## Context and problem

Complex business software fails when developers collect feature requests without learning the model behind them. A shallow design may pass the first release, but later changes expose hidden concepts, contradictory terms, and rules scattered through scripts, UI code, and reports.

## Forces

- Fast feature delivery versus time spent learning the domain
- Expert terminology versus developer implementation vocabulary
- Scenario examples versus general concepts
- Early model simplicity versus later conceptual depth

## Guidance

Use conversations, scenarios, sketches, code, and tests as a single learning loop. Ask domain experts to walk through real cases, challenge ambiguous words, and test whether the model can explain new behavior. When the team discovers a better concept, change the model and then refactor names, responsibilities, and tests to match.

Treat awkwardness as evidence. If a procedure is hard to explain, a method name has no domain meaning, or every change adds special cases, look for a missing concept rather than only adding conditionals.

## Implementation moves

- Run scenario walkthroughs with domain experts and capture the terms they correct or refine.
- Sketch candidate objects, policies, events, and rules while the discussion is live.
- Move hidden policies and calculations out of reports, scripts, and controllers into named domain concepts.
- Rewrite tests using the proposed domain language before refactoring the code.
- Retire terms that are only technical translations of domain ideas.
- Keep a short list of unresolved ambiguities and revisit them after implementation exposes new constraints.

## Checks

- Can a domain expert explain important behavior using the same nouns and verbs that appear in the code?
- Does a new requirement lead to model refinement rather than only procedural branching?
- Are awkward names, duplicated rules, and contradictory interpretations being surfaced quickly?
- Can developers point to the model concept that justifies a major responsibility assignment?

## Failure modes

- Treating interviews as one-way requirements capture rather than joint model discovery.
- Freezing an early model after it becomes visible in diagrams.
- Letting a bilingual analyst become the permanent translation bottleneck.
- Recording domain insights in documents while code keeps a different language.

## Agent trigger hints

Use this pattern when the user says or implies:

- learn the domain
- extract domain concepts
- requirements are vague
- business rules keep changing
- model is shallow

## Source notes

Synthesized from the preface and Chapter 1 in `work/book-domain-driven-design/chapter-out/`, especially the PCB and shipping examples of iterative model discovery. This file stores original guidance and source pointers only.
