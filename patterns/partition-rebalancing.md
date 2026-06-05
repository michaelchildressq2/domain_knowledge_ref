---
id: data.partition-rebalancing
title: Partition Rebalancing
type: delivery-pattern
status: draft
summary: Plan partition movement as an operational workflow with bounded load, stable routing, and rollback or retry behavior.
tags:
  - data-systems
  - partitioning
  - runtime-operations
  - scalability
  - safe-change
  - cloud-agnostic
aliases:
  - rebalance shards
  - move partitions
  - resharding
applies_when:
  - Nodes are added, removed, or resized in a partitioned data system.
  - Uneven partition load requires data movement.
avoid_when:
  - The system is static and well within capacity.
  - The platform fully automates rebalancing and exposes adequate safety controls.
related:
  - data.hot-spot-aware-partitioning
  - data.operability-first-systems
  - data.partial-failure-design
sources:
  - "book: Martin Kleppmann, Designing Data-Intensive Applications, first edition, data.pdf; Chapter 6: Partitioning"
source_confidence: high
last_reviewed: 2026-06-05
---

# Partition Rebalancing

## Intent

Make partition movement routine rather than an outage-prone emergency.

## Use when

- Nodes are added, removed, or resized in a partitioned data system.
- Uneven partition load requires data movement.

## Avoid when

- The system is static and well within capacity.
- The platform fully automates rebalancing and exposes adequate safety controls.

## Context and problem

Rebalancing consumes network, disk, and CPU while changing routing and ownership. Poorly managed movement can overload the system.

## Forces

- Fast balancing versus serving stability
- Automation versus operator control
- Data movement cost versus skew reduction

## Guidance

Move partitions gradually with observable progress, backpressure, and stable routing metadata. Protect serving workloads while rebalancing.

## Implementation moves

- Define partition ownership metadata and update protocol.
- Throttle data movement based on live load.
- Verify copied data before switching ownership.
- Keep old owners available until cutover is complete.

## Checks

- Can clients route correctly during movement?
- Does rebalancing degrade user-facing latency?
- Can failed moves resume safely?

## Failure modes

- Moving too much data at once.
- Changing routing before data is fully available.
- Ignoring hotspot root causes after rebalancing.

## Agent trigger hints

Use this pattern when the user says or implies:

- rebalance shards
- resharding
- move partition
- add database node

## Source notes

Synthesized from Chapter 6: Partitioning in the locally extracted `data-chapters/` text. This file stores original guidance and source pointers only, not source excerpts.
