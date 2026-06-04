---
id: platform.modular-stack-boundaries
title: Modular Stack Boundaries by Change Cohesion
type: architecture-pattern
status: seed
summary: Split infrastructure into stacks or modules around resources that change,
  deploy, and fail together.
tags:
- platform-engineering
- infrastructure-as-code
- modular-architecture
- stack-design
- module-boundaries
- blast-radius
- implementation-planning
- cloud-agnostic
aliases:
- stack boundaries
- module boundaries
- infrastructure modules
- blast radius control
applies_when:
- The user asks how to organize infrastructure code into stacks, modules, projects,
  or repositories.
- A single infrastructure project is too large, slow, risky, or coupled.
- Changes to unrelated resources are frequently planned or applied together.
avoid_when:
- The system is small enough that splitting adds more coordination cost than value.
- Hard provider or runtime dependencies require resources to be created together.
- The team cannot yet manage cross-stack outputs, contracts, and versioning.
related:
- platform.environment-parity
- platform.iac-delivery
- platform.safe-infrastructure-change
sources:
- 'iac2: Kief Morris, Infrastructure as Code, 2nd Edition, O''Reilly Media'
- synthesis: general infrastructure-as-code practice
source_confidence: medium
last_reviewed: 2026-06-04
subject_area: infrastructure-as-code
---

# Modular Stack Boundaries by Change Cohesion

## Intent

Reduce infrastructure change risk by grouping resources according to how they change, deploy, and fail together.

## Use when

- A monolithic infrastructure stack creates large plans, slow feedback, or risky replacements.
- Teams cannot change one service without touching unrelated infrastructure.
- The user asks about modules, stacks, repositories, ownership, blast radius, or reusable infrastructure components.

## Avoid when

- The added dependency management is larger than the benefit.
- Cross-stack contracts are not stable enough to manage separately.
- Splitting is used only to mirror an org chart rather than a technical boundary.

## Context and problem

Large infrastructure definitions tend to accumulate unrelated resources. This increases plan noise, apply duration, lock contention, and blast radius. Too many small stacks create their own problem: dependency sprawl and unclear ownership.

## Forces

- Small blast radius versus dependency overhead.
- Reuse versus customization.
- Team autonomy versus platform consistency.
- Independent delivery versus shared contract management.

## Guidance

Choose stack boundaries around change cohesion. Resources that change together, are owned together, and share a lifecycle often belong together. Resources with different lifecycles, risk profiles, or ownership boundaries usually deserve a separate stack with explicit outputs and inputs.

## Implementation moves

- Inventory resources by owner, lifecycle, change frequency, dependency direction, and failure impact.
- Separate foundational shared resources from application-specific resources.
- Define stable outputs and inputs between stacks.
- Version reusable modules and avoid implicit remote-state coupling when possible.
- Keep each stack small enough for understandable plans and safe review.
- Use naming, tagging, and ownership metadata consistently.

## Checks

- Can a common service change be planned without unrelated resource churn?
- Does each stack have a clear owner and lifecycle?
- Are cross-stack dependencies explicit and stable?
- Is the plan small enough for meaningful human review?
- What is the blast radius of an accidental replacement in this stack?

## Failure modes

- One giant stack for an entire account, platform, or product line.
- Splitting every resource into its own stack and creating dependency chaos.
- Hidden coupling through remote state, naming conventions, or undocumented parameters.
- Shared modules that are changed without versioning or consumer tests.

## Agent trigger hints

Use this pattern when the user says or implies:

- how should we split terraform stacks
- monolithic stack
- module boundaries
- infrastructure repository structure
- reduce blast radius
- reusable stack

## Source notes

This is an original synthesis. Public book metadata and contents identify stack structure, reusable stacks, and infrastructure project organization as major themes; this pattern turns those themes into a reusable design rule.
