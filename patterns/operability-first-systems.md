---
id: data.operability-first-systems
title: Operability First Systems
type: architecture-pattern
status: draft
summary: Design data systems so operators can observe, diagnose, repair, and safely change them.
tags:
  - data-systems
  - operability
  - observability
  - runtime-operations
  - reliability
  - cloud-agnostic
aliases:
  - operable data systems
  - operations friendly design
  - production diagnostics
applies_when:
  - A data system will be owned in production by a team that must diagnose incidents.
  - The design lacks monitoring, repair paths, or operational visibility.
avoid_when:
  - The component is a short-lived local prototype with no production path.
  - A managed service fully provides the required operational interface and evidence.
related:
  - data.reliability-scalability-maintainability
  - data.partial-failure-design
  - data.trust-but-verify-dataflows
sources:
  - "book: Martin Kleppmann, Designing Data-Intensive Applications, first edition, data.pdf; Chapter 1: Reliable, Scalable, and Maintainable Applications"
source_confidence: high
last_reviewed: 2026-06-05
---

# Operability First Systems

## Intent

Make production behavior understandable enough that humans can keep the system healthy.

## Use when

- A data system will be owned in production by a team that must diagnose incidents.
- The design lacks monitoring, repair paths, or operational visibility.

## Avoid when

- The component is a short-lived local prototype with no production path.
- A managed service fully provides the required operational interface and evidence.

## Context and problem

Data systems fail in subtle ways. Without operational hooks, teams cannot distinguish overload, data corruption, lag, failed consumers, or dependency faults.

## Forces

- Feature delivery versus production diagnosis
- Automation versus human intervention
- Abstraction versus visibility

## Guidance

Treat operability as a first-class design requirement. Build health signals, backpressure visibility, lag metrics, repair tools, and documented recovery paths into the system design.

## Implementation moves

- Expose metrics for latency, throughput, errors, queue depth, replication lag, and saturation.
- Log dataflow identifiers and causality where useful.
- Provide safe administrative actions for replay, reindexing, failover, and throttling.
- Document normal operating ranges and escalation paths.

## Checks

- Can an operator tell whether data is fresh and complete?
- Can failures be isolated to a dependency, node, partition, or processing stage?
- Are repair actions repeatable and safe?

## Failure modes

- Relying only on host CPU and memory metrics.
- Hiding managed-service limits from application teams.
- Building manual repair SQL with no review or audit trail.

## Agent trigger hints

Use this pattern when the user says or implies:

- operate database
- data pipeline observability
- production data issue
- operability

## Source notes

Synthesized from Chapter 1: Reliable, Scalable, and Maintainable Applications in the locally extracted `data-chapters/` text. This file stores original guidance and source pointers only, not source excerpts.
