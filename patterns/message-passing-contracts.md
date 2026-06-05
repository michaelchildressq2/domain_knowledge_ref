---
id: data.message-passing-contracts
title: Message Passing Contracts
type: architecture-pattern
status: draft
summary: Design asynchronous messages as durable contracts with explicit schemas, idempotency, ordering assumptions, and compatibility rules.
tags:
  - data-systems
  - messaging
  - schema-evolution
  - event-driven
  - implementation-planning
  - cloud-agnostic
aliases:
  - event contract
  - message schema
  - async data contract
applies_when:
  - Services exchange data through queues, logs, topics, or event streams.
  - Consumers evolve independently from producers.
avoid_when:
  - The call is a synchronous command whose success must be known immediately and transactionally.
  - The message is an internal implementation detail within one deployable unit.
related:
  - data.compatible-schema-evolution
  - data.event-log-as-source
  - data.idempotent-event-processing
sources:
  - "book: Martin Kleppmann, Designing Data-Intensive Applications, first edition, data.pdf; Chapters 4 and 11"
source_confidence: high
last_reviewed: 2026-06-05
---

# Message Passing Contracts

## Intent

Prevent asynchronous integration from becoming an undocumented coupling surface.

## Use when

- Services exchange data through queues, logs, topics, or event streams.
- Consumers evolve independently from producers.

## Avoid when

- The call is a synchronous command whose success must be known immediately and transactionally.
- The message is an internal implementation detail within one deployable unit.

## Context and problem

Messages persist, replay, arrive late, or reach consumers with different deployment versions. Without contracts, event systems become brittle.

## Forces

- Loose coupling versus semantic ambiguity
- Producer evolution versus consumer compatibility
- At-least-once delivery versus duplicate side effects

## Guidance

Treat message schemas and semantics as public interfaces. Specify identity, ordering, deduplication, compatibility, and meaning of each event.

## Implementation moves

- Define event names, keys, schema, and semantic meaning.
- Include stable identifiers for idempotency and tracing.
- Document ordering and replay expectations.
- Test consumers against old and new event versions.

## Checks

- Can consumers safely ignore unknown fields?
- Can duplicate messages be processed safely?
- Is the event a fact that happened rather than a vague instruction?

## Failure modes

- Changing event meaning without changing the contract.
- Publishing events with no durable identity.
- Assuming queue order across partitions or consumers.

## Agent trigger hints

Use this pattern when the user says or implies:

- event schema
- message contract
- async integration
- queue data format

## Source notes

Synthesized from Chapters 4 and 11 in the locally extracted `data-chapters/` text. This file stores original guidance and source pointers only, not source excerpts.
