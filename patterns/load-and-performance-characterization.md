---
id: data.load-and-performance-characterization
title: Load And Performance Characterization
type: decision-guide
status: draft
summary: Describe scalability using workload dimensions, service-level expectations, and performance distributions before choosing scaling tactics.
tags:
  - data-systems
  - scalability
  - performance
  - capacity-planning
  - design-review
  - cloud-agnostic
aliases:
  - describe load
  - performance percentiles
  - capacity model
applies_when:
  - A team says a system must scale but has not defined load.
  - Performance goals are expressed only as averages or vague latency targets.
avoid_when:
  - The system is experimental and no meaningful workload exists yet.
  - The performance concern is already narrowed to a specific known bottleneck.
related:
  - data.reliability-scalability-maintainability
  - data.hot-spot-aware-partitioning
  - data.backpressure-for-streams
sources:
  - "book: Martin Kleppmann, Designing Data-Intensive Applications, first edition, data.pdf; Chapter 1: Reliable, Scalable, and Maintainable Applications"
source_confidence: high
last_reviewed: 2026-06-05
---

# Load And Performance Characterization

## Intent

Make scalability discussions concrete enough to guide design and testing.

## Use when

- A team says a system must scale but has not defined load.
- Performance goals are expressed only as averages or vague latency targets.

## Avoid when

- The system is experimental and no meaningful workload exists yet.
- The performance concern is already narrowed to a specific known bottleneck.

## Context and problem

Scale is not one-dimensional. Data volume, request rate, write/read mix, fan-out, tail latency, and skew can each dominate the design.

## Forces

- Simple capacity estimates versus workload reality
- Average latency versus tail behavior
- Headroom versus cost

## Guidance

Define load parameters and performance expectations in measurable terms. Use distributions and percentiles, model skew, and test against representative workload changes.

## Implementation moves

- Identify primary load dimensions such as reads, writes, data size, fan-out, and concurrent users.
- Set latency and throughput targets using percentiles.
- Model hot keys, burstiness, and growth trends.
- Benchmark designs under realistic mixes, not only idealized throughput.

## Checks

- Can the team explain what growing load means for this system?
- Are tail latencies visible and bounded?
- Do tests include skew and burst behavior?

## Failure modes

- Optimizing for average latency.
- Assuming more nodes always solve bottlenecks.
- Benchmarking with uniform synthetic data only.

## Agent trigger hints

Use this pattern when the user says or implies:

- describe load
- tail latency
- p99
- capacity planning
- scale database

## Source notes

Synthesized from Chapter 1: Reliable, Scalable, and Maintainable Applications in the locally extracted `data-chapters/` text. This file stores original guidance and source pointers only, not source excerpts.
