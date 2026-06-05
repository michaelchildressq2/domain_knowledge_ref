---
id: platform.event-driven-function-boundaries
title: Event Driven Function Boundaries
type: decision-guide
status: draft
summary: Use FaaS for small stateless request transformations, asynchronous event handlers, and pipelines only when observability, cost, and state constraints fit.
tags:
  - platform-engineering
  - cloud-architecture
  - operability
  - scalability
  - cost-management
  - design-review
  - implementation-planning
  - module-boundaries
  - testing
  - faas
  - event-driven
aliases:
  - FaaS fit
  - serverless function boundaries
  - event-driven functions
  - function pipeline
  - request decorator function
applies_when:
  - Work is triggered by discrete requests or events and can run statelessly.
  - A small transformation, validation, defaulting, notification, or webhook handler can be deployed independently.
  - The traffic pattern is bursty or low enough that request-based pricing and autoscaling are advantageous.
avoid_when:
  - The workload needs long-running background processing, large warm in-memory state, or sustained high utilization.
  - The function graph is hard to observe or can accidentally call itself through cycles.
  - The system needs local coordination or shared mutable memory between steps.
related:
  - platform.workflow-queue-composition
  - platform.replicated-stateless-serving
  - platform.adapter-operability-normalization
  - data.message-passing-contracts
sources:
  - 'book: Brendan Burns, Designing Distributed Systems, Chapter 8: Functions and Event-Driven Processing'
source_confidence: high
last_reviewed: 2026-06-05
---

# Event Driven Function Boundaries

## Intent

Choose function boundaries that preserve FaaS benefits without creating opaque, costly, or state-heavy distributed designs.

## Use when

- A function can process one event or request without local durable state.
- The behavior is a small decorator, such as request defaulting, validation, enrichment, or response transformation.
- A user or system event should trigger asynchronous work, such as sending notifications or registering a secondary action.
- A pipeline step is independent, short-lived, and can pass context by event payload or shared storage reference.
- The team benefits from fast deployment and automatic scale-to-zero or scale-out behavior.

## Avoid when

- Work requires minutes or hours of continuous processing.
- Each invocation must load large indexes, models, or caches before it can respond.
- Traffic is steady and high enough that per-request economics are worse than running services.
- The pipeline requires transactions or shared mutable memory across functions.
- The team lacks tracing, metrics, alerts, and cost controls for function graphs.
- Human-visible latency depends on slow external systems that should be decoupled through queues.

## Context and problem

FaaS makes it easy to deploy small pieces of code and scale them automatically, but the same decoupling that speeds development can complicate operations. Function systems communicate over the network, store state elsewhere, and may hide dependency graphs. Cycles, retries, and unexpected invocation volume can create outages or runaway costs.

The best function boundaries are event-shaped. They fit discrete triggers, short transformations, and asynchronous reactions. They are a poor fit for workloads that need long-lived memory, sustained compute, or background loops.

## Forces

- Developer speed versus operational visibility.
- Fine-grained modularity versus distributed debugging complexity.
- Pay-per-request efficiency versus sustained utilization cost.
- Stateless decoupling versus need for warm in-memory data.
- Async responsiveness versus eventual consistency.
- Easy event wiring versus accidental cycles.

## Guidance

Use FaaS as one component in a broader architecture, not as a default replacement for all services. Start by classifying the workload: decorator, event handler, pipeline step, background worker, or long-running service. Functions fit the first three when they are short, stateless, observable, and bounded.

For request decorators, ensure the function is not over-scaled with the backend and has clear timeout behavior. For asynchronous event handlers, make delivery idempotent and track retries. For pipelines, maintain a visible graph of functions and events so agents and operators can understand what happens after each trigger.

## Implementation moves

- Define the trigger source, payload schema, idempotency key, timeout, retry policy, and dead-letter behavior.
- Keep function state external and pass references rather than large payloads where possible.
- Use tracing that propagates correlation ids across every function and webhook call.
- Add metrics for invocation count, duration, errors, retries, cold starts, and cost.
- Detect or prevent cycles in the function dependency graph.
- Put slow side effects behind asynchronous events rather than in user-facing request paths.
- Move sustained or memory-heavy workloads to containers, jobs, or long-running services.
- Version payload schemas and webhook contracts.
- Protect downstream services with concurrency limits and rate limits.
- Document the pipeline graph in architecture docs or generated diagrams.

## Checks

- Is each function stateless, short-lived, and event-shaped?
- Can operators see the complete call and event graph?
- What happens if a function retries after the side effect already succeeded?
- Is the cost model still favorable at expected peak and steady-state volume?
- Does cold start or data loading violate latency targets?
- Are events versioned and validated?
- Is there a dead-letter path for failed events?
- Can the workload be moved to a long-running service if traffic becomes sustained?

## Failure modes

- Treating FaaS as a universal hammer and splitting cohesive behavior into opaque fragments.
- Building cycles where functions trigger each other until timeout or budget exhaustion.
- Running sustained high-volume traffic through per-request pricing without cost review.
- Loading large state on every cold start and violating latency goals.
- Missing distributed traces across functions and webhooks.
- Assuming retries are safe without idempotency.
- Mixing request-response user paths with slow asynchronous side effects.

## Agent trigger hints

Use this pattern when the user says or implies:

- should this be serverless
- FaaS
- event handler
- function pipeline
- webhook workflow
- request decorator
- cold start
- serverless cost

## Source notes

Synthesized from Chapter 8's discussion of FaaS benefits, limitations, request decorators, event handlers, and event-based pipelines. This file contains original guidance and source pointers only.
