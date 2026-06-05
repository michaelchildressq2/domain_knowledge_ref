---
id: data.backpressure-for-streams
title: Backpressure For Streams
type: architecture-pattern
status: draft
summary: Propagate overload signals through streaming systems so slow consumers do not cause unbounded queues or cascading failure.
tags:
  - data-systems
  - stream-processing
  - backpressure
  - reliability
  - runtime-operations
  - cloud-agnostic
aliases:
  - stream backpressure
  - consumer lag
  - overload control
applies_when:
  - Producers can outpace consumers or sinks.
  - Consumer lag, queues, or memory use can grow without bound.
avoid_when:
  - The stream is low-volume and bounded with ample capacity.
  - Lossy sampling is explicitly acceptable and simpler.
related:
  - data.stream-derived-views
  - data.timeout-retry-backoff
  - data.load-and-performance-characterization
sources:
  - "book: Martin Kleppmann, Designing Data-Intensive Applications, first edition, data.pdf; Chapter 11: Stream Processing"
source_confidence: high
last_reviewed: 2026-06-05
---

# Backpressure For Streams

## Intent

Keep streaming systems stable under bursts and downstream slowdown.

## Use when

- Producers can outpace consumers or sinks.
- Consumer lag, queues, or memory use can grow without bound.

## Avoid when

- The stream is low-volume and bounded with ample capacity.
- Lossy sampling is explicitly acceptable and simpler.

## Context and problem

Unbounded buffering hides overload until memory, disk, or latency fails catastrophically.

## Forces

- Throughput versus latency
- Durability versus resource limits
- Producer autonomy versus downstream capacity

## Guidance

Make queues bounded or observable, throttle producers or consumers, shed or compact where semantics allow, and alert on lag before data becomes unusable.

## Implementation moves

- Set retention, queue, and memory limits deliberately.
- Measure consumer lag and processing throughput.
- Apply rate limits or flow control at producer boundaries.
- Define loss, compaction, or degradation policy for overload.

## Checks

- What happens when a sink is down for an hour?
- Can lag catch up before retention expires?
- Are producers slowed before queues exhaust resources?

## Failure modes

- Treating infinite queues as reliability.
- Ignoring slow consumer lag until data expires.
- Retrying failed sink writes faster than the sink can recover.

## Agent trigger hints

Use this pattern when the user says or implies:

- stream lag
- backpressure
- consumer falling behind
- queue overload

## Source notes

Synthesized from Chapter 11: Stream Processing in the locally extracted `data-chapters/` text. This file stores original guidance and source pointers only, not source excerpts.
