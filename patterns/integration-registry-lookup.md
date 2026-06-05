---
id: iac.integration-registry-lookup
title: Integration Registry Lookup
type: architecture-pattern
status: draft
summary: Use a general-purpose registry for cross-stack or cross-team integration values when stack-tool-specific coupling is too narrow.
tags:
  - infrastructure-as-code
  - configuration-management
  - registry
  - module-boundaries
  - platform-engineering
  - cloud-agnostic
aliases:
  - integration registry lookup
  - integration registry lookup
applies_when:
  - The user asks about integration registry lookup in an Infrastructure as Code or platform engineering context.
  - A design or workflow shows the risks, trade-offs, or symptoms described by this pattern.
avoid_when:
  - The situation is a small temporary experiment with no production, compliance, or shared-team impact.
  - A simpler local convention addresses the risk without adding process or abstraction.
related:
  - iac.externalized-configuration
sources:
  - "book: Kief Morris, Infrastructure as Code, second edition, iac2.pdf; Chapter 17."
source_confidence: high
last_reviewed: 2026-06-04
---

# Integration Registry Lookup

## Intent

Use a general-purpose registry for cross-stack or cross-team integration values when stack-tool-specific coupling is too narrow.

## Use when

- The user asks about integration registry lookup in an Infrastructure as Code or platform engineering context.
- A design or workflow shows the risks, trade-offs, or symptoms described by this pattern.

## Avoid when

- The situation is a small temporary experiment with no production, compliance, or shared-team impact.
- A simpler local convention addresses the risk without adding process or abstraction.

## Context and problem

Teams applying Infrastructure as Code encounter this concern when automation, ownership, lifecycle, and risk boundaries are not explicit enough for safe repeated change.

## Forces

- Change speed versus operational confidence
- Reuse and consistency versus local autonomy
- Automation simplicity versus hidden coupling

## Guidance

Use integration registry lookup as a deliberate design choice. Make the boundary, ownership, inputs, outputs, and failure behavior visible in code and delivery workflow. Prefer small, testable, reviewable changes over broad implicit behavior.

## Implementation moves

- Name the concrete risk or decision the pattern addresses.
- Represent the chosen behavior in source-controlled code or pipeline configuration.
- Document inputs, outputs, owners, and expected variation.
- Add checks that catch the most likely failure mode before production impact.

## Checks

- Can reviewers see the intent and affected scope from source?
- Are avoid conditions documented so the pattern is not applied universally?
- Does the delivery workflow produce evidence that the pattern is working?

## Failure modes

- Applying the pattern as a universal rule without checking context.
- Hiding important dependencies behind convenience abstractions.
- Leaving manual exceptions unreconciled with source-controlled intent.

## Agent trigger hints

Use this pattern when the user says or implies:

- integration registry lookup
- integration registry lookup
- integration-registry-lookup

## Source notes

Synthesized from Chapter 17. Source confidence is high because the chapter text was extracted locally from the user-provided PDF. No source excerpts are stored here.
