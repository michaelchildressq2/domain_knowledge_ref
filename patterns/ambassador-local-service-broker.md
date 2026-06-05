---
id: platform.ambassador-local-service-broker
title: Ambassador Local Service Broker
type: architecture-pattern
status: draft
summary: Put service discovery, sharding, request splitting, or environment-specific brokering behind a local endpoint so application code can remain simple and portable.
tags:
  - platform-engineering
  - cloud-architecture
  - modular-architecture
  - scalability
  - safe-change
  - migration
  - runtime-operations
  - module-boundaries
  - parameterization
  - kubernetes
  - service-discovery
  - ambassador
aliases:
  - ambassador pattern
  - local service broker
  - client-side proxy
  - request-splitting ambassador
  - sharding proxy
applies_when:
  - Application code expects a simple local service while the real backend varies by environment, shard, experiment, or provider.
  - You need to keep backend routing logic out of application binaries.
  - A proxy can broker outbound interactions through localhost or another stable local endpoint.
avoid_when:
  - A shared gateway or service mesh already owns the routing concern consistently.
  - Every client would carry heavy proxy cost or complex configuration.
  - The routing logic is core business behavior that must be visible in application tests.
related:
  - platform.container-contracts-for-reuse
  - platform.sidecar-application-augmentation
  - platform.sharded-service-routing
  - platform.replicated-stateless-serving
sources:
  - 'book: Brendan Burns, Designing Distributed Systems, Chapter 3: Ambassadors'
  - 'book: Brendan Burns, Designing Distributed Systems, Chapter 6: Sharded Services'
source_confidence: high
last_reviewed: 2026-06-05
---

# Ambassador Local Service Broker

## Intent

Separate application behavior from outbound service-routing complexity by colocating a broker that presents a stable local interface.

## Use when

- An application should connect to a single local endpoint while the broker handles sharded storage, service discovery, SaaS versus self-hosted backends, or request splitting.
- Development and production environments have different backend topologies, but the app should use the same connection contract.
- You are adopting a sharded backend and want to avoid rewriting every client.
- You need a lightweight experiment, canary, or traffic-tee mechanism close to the client.
- A reusable proxy can encode routing behavior once and serve many workloads.

## Avoid when

- The broker must be scaled, monitored, or deployed independently from each client workload.
- Centralizing the broker as a shared service would reduce total operational complexity more than localizing it.
- Added per-client proxy latency, memory, and configuration are unacceptable.
- The routing rules are security-sensitive and require central policy enforcement.
- The application can use a mature client library with the same behavior and clearer failure semantics.

## Context and problem

Applications often want a simple dependency contract: connect to a database, cache, API, or service name. Real production environments are less simple. Backends may be sharded, discovered dynamically, implemented differently across clouds, or split between production and experiment variants. Putting all of that logic into application code spreads infrastructure concerns across every service and language.

An ambassador container brokers outbound calls. The application connects to localhost or a stable local endpoint; the ambassador performs discovery, routing, sharding, request splitting, or environment adaptation. This keeps application code simpler while still allowing sophisticated backend topology.

## Forces

- Application portability versus infrastructure-specific routing.
- Client-side simplicity versus per-pod proxy overhead.
- Localized routing control versus centralized operability.
- Team ownership boundaries versus shared platform consistency.
- Experiment speed versus long-term routing governance.
- Extra network hop avoidance versus duplicated proxy instances.

## Guidance

Use an ambassador when outbound infrastructure complexity belongs near the client and when the local endpoint meaningfully simplifies application code. Make the broker explicit in deployment, configuration, logs, and dashboards. If the broker becomes a permanent platform service with large shared demand, reassess whether it should move out of each pod and become a replicated shared routing tier.

For experiments or request teeing, prefer sticky assignment so users do not bounce between variants. For sharding, make the sharding key and failure behavior visible. For service discovery, define how the ambassador chooses providers and how it fails when no provider is available.

## Implementation moves

- Define the local interface the application will use: host, port, protocol, authentication, and failure responses.
- Keep the application unaware of shard counts, provider endpoints, and experiment weights.
- Put routing configuration in versioned config objects, templates, or secrets rather than baking it into the image.
- Decide between a per-client ambassador and a shared routing service based on latency, operational complexity, traffic volume, and team ownership.
- For request splitting, use stable user or session keys to prevent inconsistent user experience.
- For traffic teeing, ensure only the production response is returned to users unless the experiment is explicitly active.
- For sharding, use deterministic and documented routing functions with consistent hashing when shard counts change.
- Add metrics for route choice, backend latency, backend failures, retries, and dropped or shadowed requests.
- Limit ambassador credentials to the outbound services it brokers.
- Include ambassador health in workload readiness if the app cannot operate without it.

## Checks

- What routing concern is removed from application code?
- Does the ambassador have a stable local contract and documented parameters?
- Can operators see which backend, shard, or experiment each request used?
- Does the design choose local ambassador versus shared broker intentionally?
- Are experiment assignments sticky enough for user-visible behavior?
- Can the application tolerate ambassador restart or backend discovery failure?
- Are routing updates tested separately from application releases?
- Is the added latency acceptable at current and projected request rates?

## Failure modes

- Hiding business routing decisions in proxy configuration that application owners cannot test.
- Deploying one ambassador per pod when a shared service would be cheaper and easier to operate.
- Making the ambassador critical but omitting it from readiness and alerting.
- Using non-deterministic sharding or experiment assignment.
- Letting local proxy configuration drift across environments.
- Adding request teeing without isolating side effects in the shadow destination.
- Treating the ambassador as transparent while it mutates headers, authentication, or request paths.

## Agent trigger hints

Use this pattern when the user says or implies:

- ambassador container
- client-side proxy
- service broker
- connect to localhost but route to shards
- request splitting
- traffic tee
- hide service discovery from the app
- portable across clouds

## Source notes

Synthesized from Chapter 3 examples on sharded Redis, service brokering, and request splitting, with supporting sharded-routing trade-offs from Chapter 6. This file contains original guidance and source pointers only.
