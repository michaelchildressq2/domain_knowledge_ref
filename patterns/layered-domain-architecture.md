---
id: ddd.layered-domain-architecture
title: Layered Domain Architecture
type: architecture-pattern
status: draft
summary: Isolate domain logic from UI, application coordination, and infrastructure so the model can stay expressive and testable.
tags:
  - domain-driven-design
  - layered-architecture
  - domain-layer
  - separation-of-concerns
  - modular-architecture
  - testability
aliases:
  - domain layer
  - layered architecture
  - isolate the domain
applies_when:
  - Business rules are mixed into controllers, UI widgets, database scripts, or integration code.
  - The team wants model-driven design but technical concerns keep dominating domain objects.
avoid_when:
  - The application is so small and short-lived that layering would add more ceremony than clarity.
  - A Smart UI style is a deliberate choice for a simple data-entry tool with a non-expert team and limited behavior.
related:
  - ddd.model-driven-design
  - ddd.aggregate-lifecycle-boundary
  - iac.declarative-imperative-separation
sources:
  - "book: Eric Evans, Domain-Driven Design, 2003 final manuscript; Chapter 4: Isolating the Domain"
source_confidence: high
last_reviewed: 2026-06-05
---

# Layered Domain Architecture

## Intent

Give domain logic a protected place where it can evolve independently of presentation, orchestration, persistence, and messaging concerns.

## Use when

- Business behavior is duplicated across UI, reports, scripts, services, and persistence mappings.
- Changing a business rule requires tracing unrelated technical code.
- Domain objects know too much about storage, widgets, request formats, or transaction plumbing.

## Avoid when

- The work is a simple form-over-data application with no meaningful domain behavior.
- A framework's conventions already isolate domain behavior clearly and adding another layer would duplicate structure.
- The team cannot maintain the discipline needed to keep dependencies flowing in the intended direction.

## Context and problem

Software functions combine presentation, coordination, business rules, persistence, messaging, and other infrastructure. If these concerns are tangled, the domain model cannot become rich: rules hide in technical code, automated tests are awkward, and superficial UI or database changes can alter business behavior.

## Forces

- Short-term implementation speed versus long-term model clarity
- Thin application coordination versus domain behavior leakage
- Infrastructure convenience versus domain independence
- Layer purity versus practical framework integration

## Guidance

Separate the system into cohesive layers and concentrate domain model code in the domain layer. Keep the application layer thin: it coordinates tasks, transactions, and calls into domain objects, but does not own business rules. Put persistence, messaging, UI rendering, and generic technical services in infrastructure or presentation layers.

The goal is not abstract layering for its own sake. The key decision is whether the domain model can be understood, tested, and changed without dragging unrelated technologies into every design conversation.

## Implementation moves

- Identify business rules currently embedded in UI, controllers, jobs, reports, stored procedures, or adapters.
- Move rules into domain objects, domain services, specifications, or aggregates.
- Keep application services focused on use-case coordination and transaction boundaries.
- Hide persistence mechanics behind repositories or mappers.
- Prohibit domain objects from depending on UI and infrastructure APIs unless the dependency is explicitly inverted.
- Add domain-level tests that exercise rules without booting the whole application.

## Checks

- Can core business behavior be tested without UI, network, and database setup?
- Is the application layer mostly orchestration instead of rule evaluation?
- Do domain names and responsibilities remain visible without reading infrastructure code?
- Are dependencies pointing toward stable domain abstractions where appropriate?

## Failure modes

- Creating layers in package names while behavior remains tangled.
- Moving all behavior into application services and leaving domain objects anemic.
- Letting persistence models dictate aggregate and object boundaries.
- Adding generic architecture rules that obscure the domain instead of isolating it.

## Agent trigger hints

Use this pattern when the user says or implies:

- isolate domain logic
- domain layer
- business rules in controllers
- layered architecture
- anemic domain model

## Source notes

Synthesized from Chapter 4 in `work/book-domain-driven-design/chapter-out/`, including the layered architecture and Smart UI trade-off discussion. This file stores original guidance and source pointers only.
