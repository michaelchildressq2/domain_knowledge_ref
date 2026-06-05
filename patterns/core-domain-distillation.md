---
id: ddd.core-domain-distillation
title: Core Domain Distillation
type: decision-guide
status: draft
summary: Concentrate design talent and model clarity on the parts of the domain that create strategic advantage.
tags:
  - domain-driven-design
  - core-domain
  - subdomains
  - prioritization
  - architecture-strategy
  - module-boundaries
  - maintainability
  - design-review
aliases:
  - core domain
  - domain distillation
  - generic subdomain
applies_when:
  - The model is too large for teams to see which parts deserve the most design attention.
  - Strategic behavior is buried under generic mechanisms, support workflows, or purchased capabilities.
avoid_when:
  - The system has no differentiating domain behavior and commodity solutions are enough.
  - The team is using core-domain language to justify custom-building commodity capabilities.
related:
  - ddd.bounded-context-integrity
  - ddd.supple-domain-design
  - iac.resource-matching
sources:
  - "book: Eric Evans, Domain-Driven Design, 2003 final manuscript; Chapter 15: Distillation"
source_confidence: high
last_reviewed: 2026-06-05
---

# Core Domain Distillation

## Intent

Make the strategically important model small enough to see, protect, and improve.

## Use when

- Teams spend most effort on generic supporting behavior while the differentiating domain stagnates.
- The domain model is broad, cluttered, and hard to explain.
- Architecture decisions need a principled way to decide where to buy, outsource, simplify, or invest.
- Refactoring targets compete and the team needs strategic priority.

## Avoid when

- The business value is mostly operational execution and no custom model creates advantage.
- A supposed core domain is actually a generic subdomain available as a mature product or service.
- Distillation becomes a document exercise without changing staffing, design effort, or code structure.

## Context and problem

Large models contain core ideas, generic subdomains, mechanisms, supporting features, and legacy compromises. Without distillation, the important parts are hidden. Teams then spread scarce design skill evenly, overbuild commodity areas, and underinvest in the model that differentiates the system.

## Forces

- Strategic differentiation versus commodity capability
- Model clarity versus total domain breadth
- Custom design investment versus package or service reuse
- Explicit priority versus political attachment to local features

## Guidance

Identify the core domain: the part of the model where superior understanding and implementation create the most value. Separate generic subdomains and cohesive mechanisms so they do not obscure the core. Make the core visible through code organization, highlighted model elements, concise domain vision, tests, and architecture review. Assign strong people and refactoring attention to the core first.

Distillation is iterative. As the team learns, the definition of the core may change, and so should investment decisions.

## Implementation moves

- Ask which domain behavior would materially differentiate the organization if it were better than alternatives.
- Mark generic subdomains that can be bought, delegated, reused, or implemented simply.
- Extract cohesive mechanisms that support the core but do not themselves express business meaning.
- Create a short domain vision statement that explains the core and its value.
- Highlight core modules, tests, and model elements in repository documentation or diagrams.
- Review refactoring and staffing priorities against core-domain impact.

## Checks

- Can the team name the core domain in a few sentences?
- Are the best design efforts aimed at the core rather than generic support code?
- Are generic subdomains prevented from dominating the model and codebase?
- Does the architecture make core concepts easy to find and change?

## Failure modes

- Calling everything core to avoid prioritization.
- Custom-building commodity subdomains because they are familiar or politically owned.
- Hiding the core behind generic frameworks or mechanisms.
- Freezing the first core-domain assessment after new learning changes the business picture.

## Agent trigger hints

Use this pattern when the user says or implies:

- core domain
- generic subdomain
- where should we invest design effort
- domain distillation
- strategic domain design

## Source notes

Synthesized from Chapter 15 in `work/book-domain-driven-design/chapter-out/`, including core domain, generic subdomains, domain vision, highlighted core, cohesive mechanisms, segregated core, and abstract core. This file stores original guidance and source pointers only.
