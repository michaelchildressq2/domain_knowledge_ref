---
id: data.conflict-free-domain-design
title: Conflict Free Domain Design
type: architecture-pattern
status: draft
summary: Shape replicated operations so concurrent updates commute or merge without losing user intent.
tags:
  - data-systems
  - replication
  - conflict-resolution
  - eventual-consistency
  - implementation-planning
  - cloud-agnostic
aliases:
  - commutative updates
  - crdt friendly design
  - mergeable data
applies_when:
  - Users or regions may update the same logical data concurrently.
  - The system needs availability during partitions or offline operation.
avoid_when:
  - The domain requires strict serial ordering or uniqueness that cannot be relaxed.
  - Conflicts are rare and better handled by explicit workflow.
related:
  - data.multi-leader-conflict-design
  - data.eventual-consistency-boundaries
  - data.idempotent-event-processing
sources:
  - "book: Martin Kleppmann, Designing Data-Intensive Applications, first edition, data.pdf; Chapter 5: Replication"
source_confidence: high
last_reviewed: 2026-06-05
---

# Conflict Free Domain Design

## Intent

Reduce conflict risk by designing operations around intent and mergeability.

## Use when

- Users or regions may update the same logical data concurrently.
- The system needs availability during partitions or offline operation.

## Avoid when

- The domain requires strict serial ordering or uniqueness that cannot be relaxed.
- Conflicts are rare and better handled by explicit workflow.

## Context and problem

If concurrent updates overwrite each other, available replicated systems lose data or violate user expectations.

## Forces

- Availability versus coordination
- User intent preservation versus simple storage updates
- Merge complexity versus correctness

## Guidance

Prefer operations that express intent, such as add item, increment counter, or set membership, over blind replacement. Use mergeable data types or explicit conflict workflows.

## Implementation moves

- Model user actions as operations rather than whole-record replacements.
- Use commutative operations where possible.
- Track causal metadata when merges need it.
- Escalate non-mergeable conflicts to domain workflows.

## Checks

- Can concurrent operations be applied in any order?
- Does merge preserve both users intent?
- Are deletes and replacements handled carefully?

## Failure modes

- Using last-write-wins for collaborative data.
- Merging syntax while losing semantic intent.
- Ignoring tombstones or causal context for deletes.

## Agent trigger hints

Use this pattern when the user says or implies:

- conflict resolution
- crdt
- commutative update
- merge concurrent writes

## Source notes

Synthesized from Chapter 5: Replication in the locally extracted `data-chapters/` text. This file stores original guidance and source pointers only, not source excerpts.
