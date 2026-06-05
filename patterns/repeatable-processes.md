---
id: iac.repeatable-processes
title: Repeatable Processes
type: delivery-pattern
status: draft
summary: Automate any infrastructure process that must be run reliably more than once.
tags:
  - infrastructure-as-code
  - pipeline-automation
  - reproducibility
  - operability
  - delivery-pipeline
  - cloud-agnostic
aliases:
  - repeatable processes
  - repeatable processes
applies_when:
  - The user asks about repeatable processes in an Infrastructure as Code or platform engineering context.
  - A design or workflow shows the risks, trade-offs, or symptoms described by this pattern.
avoid_when:
  - The situation is a small temporary experiment with no production, compliance, or shared-team impact.
  - A simpler local convention addresses the risk without adding process or abstraction.
related:
  - iac.define-everything-as-code
sources:
  - "book: Kief Morris, Infrastructure as Code, second edition, iac2.pdf; Chapters 2, 8, 19, and 20."
source_confidence: high
last_reviewed: 2026-06-04
---

# Repeatable Processes

## Intent

Automate any infrastructure process that must be run reliably more than once.

## Use when

- The user asks about repeatable processes in an Infrastructure as Code or platform engineering context.
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

Use repeatable processes as a deliberate design choice. Make the boundary, ownership, inputs, outputs, and failure behavior visible in code and delivery workflow. Prefer small, testable, reviewable changes over broad implicit behavior.

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

- repeatable processes
- repeatable processes
- repeatable-processes

## Source notes

Synthesized from Chapters 2, 8, 19, and 20. Source confidence is high because the chapter text was extracted locally from the user-provided PDF. No source excerpts are stored here.
