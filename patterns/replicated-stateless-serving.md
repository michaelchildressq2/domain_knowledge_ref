---
id: platform.replicated-stateless-serving
title: Replicated Stateless Serving
type: architecture-pattern
status: draft
summary: Run multiple interchangeable service replicas behind a load balancer with readiness checks, rollout controls, and optional replicated edge layers.
tags:
  - platform-engineering
  - cloud-architecture
  - high-availability
  - scalability
  - zero-downtime
  - design-review
  - runtime-operations
  - rollback
  - testing
  - kubernetes
  - load-balancing
aliases:
  - replicated service
  - stateless replicas
  - load-balanced service
  - horizontal serving tier
applies_when:
  - Any replica can serve any request without depending on local durable state.
  - The service needs availability during crashes, node failure, or rolling deployments.
  - Capacity should increase by adding replicas.
avoid_when:
  - Requests require local state that cannot be externalized or consistently routed.
  - A single instance meets the availability and deployment SLA with acceptable risk.
  - The bottleneck is shared downstream state that replication will overload.
related:
  - platform.sharded-service-routing
  - platform.scatter-gather-request-parallelism
  - platform.sidecar-application-augmentation
  - data.load-and-performance-characterization
sources:
  - 'book: Brendan Burns, Designing Distributed Systems, Chapter 5: Replicated Load-Balanced Services'
source_confidence: high
last_reviewed: 2026-06-05
---

# Replicated Stateless Serving

## Intent

Provide availability and horizontal scale by making service instances interchangeable and routing traffic only to replicas that are ready.

## Use when

- A service can process a request using only request data and shared external dependencies.
- The team wants rolling deployment without user-visible downtime.
- A load balancer or service abstraction can hide individual replica addresses.
- The service has startup work, such as loading data or connecting to dependencies, before it can safely serve.
- You are adding replicated edge layers such as cache, rate limiting, or TLS termination in front of an application.

## Avoid when

- The service keeps necessary session state in local memory without sticky routing.
- The downstream database, cache, or API is the real capacity limit and cannot absorb multiplied traffic.
- The service needs exactly one active owner for correctness.
- The rollout process cannot run old and new replicas concurrently.
- A managed platform already provides the serving abstraction and probes.

## Context and problem

A single service instance is easy to understand but fragile under crashes, node failures, and deployments. It also imposes a hard capacity ceiling. Replicating stateless instances behind a load balancer lets traffic continue while individual instances start, fail, restart, or upgrade.

The pattern depends on honest readiness. Liveness means a process exists; readiness means it can serve user traffic correctly. Without readiness probes, a load balancer may route to instances that are still loading data, warming caches, establishing connections, or applying configuration.

## Forces

- Availability versus deployment simplicity.
- Horizontal capacity versus downstream amplification.
- Stateless interchangeability versus session affinity needs.
- Fast startup versus correctness of readiness.
- Edge functionality reuse versus too many serving layers.
- Round-robin fairness versus sticky user experience.

## Guidance

Default user-facing stateless services to at least two replicas when availability matters. Put a stable service or load-balancing abstraction in front of them and route traffic based on readiness, not only process existence. Add replicas to scale request throughput, but validate that downstream dependencies and edge layers scale with the added concurrency.

Use session affinity only when necessary and prefer application-layer keys, such as cookies, when external traffic passes through NAT or shared caches. If you add caching, rate limiting, or TLS termination, decide whether each layer should scale with the application or as an independent replicated tier.

## Implementation moves

- Externalize durable state to databases, object stores, queues, or caches.
- Define readiness endpoints that check required local initialization and critical dependency availability.
- Define liveness checks separately and avoid using them to express warmup.
- Deploy replicas behind a stable service name, load balancer, ingress, or gateway.
- Use rolling updates with max unavailable and max surge values aligned to the SLA.
- Size minimum replicas so one instance can fail or drain without breaching capacity.
- Add metrics for ready replicas, request distribution, error rate, tail latency, and rollout status.
- If sticky sessions are required, use stable user-level keys and document cache or affinity implications.
- Place cache, rate-limit, and TLS layers as separate replicated tiers when their ideal replica count differs from the app.
- Load test with one replica removed and during a rolling update.

## Checks

- Can any healthy replica serve any new request?
- Does readiness stay false until the service can serve correctly?
- Can one replica fail during peak traffic without overload?
- Does a rollout maintain enough ready capacity?
- Are caches or edge layers hiding source IPs in ways that break affinity?
- Are downstream dependencies protected from multiplied parallelism?
- Is the service name stable even when all pod or instance names change?
- Are rate limits and TLS certificates managed independently from application releases?

## Failure modes

- Using liveness checks as readiness checks and routing to half-initialized instances.
- Replicating a service that secretly depends on local mutable state.
- Scaling replicas while overloading a shared database or cache.
- Adding a cache sidecar that must scale one-to-one with app replicas even though cache efficiency wants fewer, larger instances.
- Depending on IP affinity for external clients behind NAT.
- Running only one replica and assuming orchestration restart equals high availability.
- Draining too many replicas during rollout for the promised SLA.

## Agent trigger hints

Use this pattern when the user says or implies:

- stateless service
- load-balanced replicas
- rolling deployment
- readiness probe
- horizontal scaling
- high availability for this API
- session affinity
- replicated cache layer

## Source notes

Synthesized from Chapter 5's replicated stateless service, readiness probes, session tracking, caching layer, rate limiting, and TLS termination examples. This file contains original guidance and source pointers only.
