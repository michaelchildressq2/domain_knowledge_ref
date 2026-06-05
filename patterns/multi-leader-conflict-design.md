---
id: data.multi-leader-conflict-design
title: Multi Leader Conflict Design
type: decision-guide
status: draft
summary: Use multi-leader replication only when write locality or offline operation justifies explicit conflict detection and resolution.
tags:
  - data-systems
  - replication
  - conflict-resolution
  - multi-region
  - design-review
  - cloud-agnostic
aliases:
  - multi master replication
  - active active database
  - write conflicts
applies_when:
  - Multiple regions or clients need to accept writes independently.
  - Offline or low-latency local writes are more important than immediate global convergence.
avoid_when:
  - The application cannot tolerate conflicting writes or has no meaningful resolution strategy.
  - A single leader with acceptable latency and failover meets requirements.
related:
  - data.leader-follower-replication
  - data.conflict-free-domain-design
  - data.eventual-consistency-boundaries
sources:
  - "book: Martin Kleppmann, Designing Data-Intensive Applications, first edition, data.pdf; Chapter 5: Replication"
source_confidence: high
last_reviewed: 2026-06-05
---

# Multi Leader Conflict Design

## Intent

Make conflict handling a domain design problem rather than an accidental database side effect.

## Use when

- Multiple regions or clients need to accept writes independently.
- Offline or low-latency local writes are more important than immediate global convergence.

## Avoid when

- The application cannot tolerate conflicting writes or has no meaningful resolution strategy.
- A single leader with acceptable latency and failover meets requirements.

## Context and problem

Multi-leader replication improves write locality but creates concurrent writes that may conflict.

## Forces

- Local write availability versus conflict complexity
- Latency versus global ordering
- Automatic resolution versus business correctness

## Guidance

Adopt multi-leader only with clear conflict semantics. Prefer domain operations that commute or merge, and expose unresolved conflicts for human or application-level resolution when necessary.

## Implementation moves

- Identify entities that can be written concurrently.
- Choose conflict detection based on versions, timestamps, or causal metadata.
- Define deterministic merge rules or workflow resolution.
- Test partitions, reconnects, and conflicting updates.

## Checks

- What happens when two leaders update the same field differently?
- Are conflict outcomes acceptable to users?
- Can conflicts be audited and repaired?

## Failure modes

- Last-write-wins on data where lost updates matter.
- Assuming conflicts are rare enough to ignore.
- Using active-active writes only for marketing availability claims.

## Agent trigger hints

Use this pattern when the user says or implies:

- multi leader replication
- active active database
- write conflict
- multi region writes

## Source notes

Synthesized from Chapter 5: Replication in the locally extracted `data-chapters/` text. This file stores original guidance and source pointers only, not source excerpts.
