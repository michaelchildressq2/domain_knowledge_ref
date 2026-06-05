---
id: data.schema-registry-contracts
title: Schema Registry Contracts
type: governance-pattern
status: draft
summary: Use a registry or equivalent governance point to validate shared data schemas and compatibility before producers publish changes.
tags:
  - data-systems
  - schema-evolution
  - governance
  - data-contracts
  - delivery-pipeline
  - cloud-agnostic
aliases:
  - schema registry
  - data contract registry
  - compatibility gate
applies_when:
  - Many producers and consumers exchange encoded events or records.
  - Breaking schema changes have caused runtime failures.
avoid_when:
  - The data format is local to one deployable unit.
  - A registry would be unavailable on critical write paths and no caching strategy exists.
related:
  - data.compatible-schema-evolution
  - data.message-passing-contracts
  - data.event-log-as-source
sources:
  - "book: Martin Kleppmann, Designing Data-Intensive Applications, first edition, data.pdf; Chapter 4: Encoding and Evolution"
source_confidence: high
last_reviewed: 2026-06-05
---

# Schema Registry Contracts

## Intent

Make data contract changes visible, validated, and reviewable.

## Use when

- Many producers and consumers exchange encoded events or records.
- Breaking schema changes have caused runtime failures.

## Avoid when

- The data format is local to one deployable unit.
- A registry would be unavailable on critical write paths and no caching strategy exists.

## Context and problem

When shared schemas evolve informally, producers can break consumers without noticing until runtime.

## Forces

- Producer autonomy versus consumer safety
- Central validation versus delivery friction
- Strict compatibility versus domain evolution

## Guidance

Register schemas and enforce compatibility checks in CI/CD or publish paths. Treat schema changes as contract changes with ownership and migration policy.

## Implementation moves

- Define compatibility mode per topic or dataset.
- Require producers to register schemas before deployment.
- Validate candidate schemas against existing consumers or compatibility rules.
- Publish schema documentation and ownership.

## Checks

- Can a producer publish an incompatible schema accidentally?
- Do consumers know which schema versions they support?
- Are schema changes reviewed by contract owners?

## Failure modes

- Using a registry only as documentation.
- Allowing force-publish without migration tracking.
- Making compatibility rules too strict for legitimate evolution.

## Agent trigger hints

Use this pattern when the user says or implies:

- schema registry
- data contracts
- event schema compatibility
- producer consumer schema

## Source notes

Synthesized from Chapter 4: Encoding and Evolution in the locally extracted `data-chapters/` text. This file stores original guidance and source pointers only, not source excerpts.
