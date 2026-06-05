---
id: data.compatible-schema-evolution
title: Compatible Schema Evolution
type: delivery-pattern
status: draft
summary: Evolve encoded data with backward and forward compatibility so old and new code can coexist.
tags:
  - data-systems
  - schema-evolution
  - compatibility
  - delivery-pipeline
  - safe-change
  - cloud-agnostic
aliases:
  - backward compatibility
  - forward compatibility
  - schema migration compatibility
applies_when:
  - Serialized data may be read by multiple application versions.
  - Deployments are rolling, asynchronous, or involve stored historical data.
avoid_when:
  - All data and code can be replaced atomically and no old encoded data remains.
  - The format is private to a single short-lived process.
related:
  - data.evolvable-data-systems
  - data.schema-registry-contracts
  - data.message-passing-contracts
sources:
  - "book: Martin Kleppmann, Designing Data-Intensive Applications, first edition, data.pdf; Chapter 4: Encoding and Evolution"
source_confidence: high
last_reviewed: 2026-06-05
---

# Compatible Schema Evolution

## Intent

Allow data formats and code to change independently without outages or unreadable data.

## Use when

- Serialized data may be read by multiple application versions.
- Deployments are rolling, asynchronous, or involve stored historical data.

## Avoid when

- All data and code can be replaced atomically and no old encoded data remains.
- The format is private to a single short-lived process.

## Context and problem

Old data, old writers, and old readers often coexist with new code. Incompatible schema changes break rolling deployment and long-lived data.

## Forces

- Evolution speed versus compatibility burden
- Strict schemas versus flexible payloads
- Producer freedom versus consumer safety

## Guidance

Use additive and tolerant evolution rules. New readers should handle old data, old readers should tolerate new data, and incompatible removals should be phased.

## Implementation moves

- Choose an encoding format with explicit schema-evolution rules.
- Add optional fields before requiring them.
- Keep old fields until all consumers have migrated.
- Test old/new reader-writer combinations.

## Checks

- Can old code read new messages where expected?
- Can new code read historical data?
- Are defaults and unknown-field behavior documented?

## Failure modes

- Renaming or changing field meaning in place.
- Deploying producer changes before consumers tolerate them.
- Assuming JSON flexibility removes compatibility obligations.

## Agent trigger hints

Use this pattern when the user says or implies:

- schema evolution
- backward compatibility
- avro protobuf thrift
- rolling deployment data

## Source notes

Synthesized from Chapter 4: Encoding and Evolution in the locally extracted `data-chapters/` text. This file stores original guidance and source pointers only, not source excerpts.
