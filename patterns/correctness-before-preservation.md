---
id: data.correctness-before-preservation
title: Correctness Before Preservation
type: decision-guide
status: draft
summary: Optimize data-system design for useful, correct outcomes rather than preserving existing mechanisms or local component uptime.
tags:
  - data-systems
  - correctness
  - maintainability
  - governance
  - design-review
  - cloud-agnostic
aliases:
  - correctness first
  - beneficial systems
  - outcome oriented reliability
applies_when:
  - A team protects an existing system design even though it blocks correctness or evolution.
  - Local availability metrics conflict with user or business correctness.
avoid_when:
  - A narrow operational incident requires immediate preservation before redesign.
  - The system has regulatory preservation duties that define correctness.
related:
  - data.reliability-scalability-maintainability
  - data.trust-but-verify-dataflows
  - data.evolvable-data-systems
sources:
  - "book: Martin Kleppmann, Designing Data-Intensive Applications, first edition, data.pdf; Chapter 12: The Future of Data Systems"
source_confidence: high
last_reviewed: 2026-06-05
---

# Correctness Before Preservation

## Intent

Keep architecture decisions aligned with the purpose of the system, not with the survival of current components.

## Use when

- A team protects an existing system design even though it blocks correctness or evolution.
- Local availability metrics conflict with user or business correctness.

## Avoid when

- A narrow operational incident requires immediate preservation before redesign.
- The system has regulatory preservation duties that define correctness.

## Context and problem

Teams can over-optimize for keeping components running while ignoring whether the whole dataflow remains correct, understandable, and beneficial.

## Forces

- Local uptime versus global correctness
- Legacy preservation versus evolution
- Technical success versus user impact

## Guidance

Define correctness at the system and user outcome level. Use that definition to decide when to preserve, replace, derive, reconcile, or retire components.

## Implementation moves

- State what correct outcome means for users and downstream decisions.
- Identify components whose local success can hide global failure.
- Add verification around the outcome, not just component health.
- Retire or replace mechanisms that no longer serve the purpose.

## Checks

- Can the system be up while producing wrong decisions?
- Do metrics reflect user and data correctness?
- Is preservation of a component blocking better design?

## Failure modes

- Equating uptime with correctness.
- Keeping legacy dataflows because they are familiar.
- Ignoring ethical or user-impact consequences of data errors.

## Agent trigger hints

Use this pattern when the user says or implies:

- data correctness
- system purpose
- trust but verify
- maintainability tradeoff

## Source notes

Synthesized from Chapter 12: The Future of Data Systems in the locally extracted `data-chapters/` text. This file stores original guidance and source pointers only, not source excerpts.
