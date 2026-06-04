---
id: platform.high-availability
title: High Availability by Failure Domain Design
type: architecture-pattern
status: seed
summary: Design the service so expected component, node, zone, or deploy failures
  do not interrupt the user-visible capability.
tags:
- platform-engineering
- cloud-architecture
- high-availability
- reliability
- failure-domains
- redundancy
- runtime-operations
- design-review
- cloud-agnostic
- testing
aliases:
- ha
- resilient service
- active active
- multi zone availability
applies_when:
- The user asks how to keep a service available during ordinary failures.
- The system has an uptime objective or customer-facing dependency.
- A single node, instance, zone, deployment, or maintenance event can currently cause
  outage.
avoid_when:
- The workload is explicitly offline, batch-only, or disposable.
- The business impact of downtime is lower than the complexity and cost of redundancy.
- State replication, dependency limits, or licensing make active redundancy unsafe.
related:
- platform.disaster-recovery
- platform.safe-infrastructure-change
- platform.observability-feedback
sources:
- 'iac2: Kief Morris, Infrastructure as Code, 2nd Edition, O''Reilly Media'
- synthesis: general platform engineering and reliability practice
source_confidence: medium
last_reviewed: 2026-06-04
subject_area: reliability
---

# High Availability by Failure Domain Design

## Intent

Keep a capability running when predictable infrastructure parts fail. Treat failure as normal and design the runtime shape, deployment process, and dependencies so no single expected fault takes down the service.

## Use when

- A service has an availability target, customer promise, or critical internal dependency role.
- Outages are caused by single-instance, single-zone, single-load-balancer, single-database, or single-deploy failures.
- The user asks for active-active, redundancy, failover, quorum, health checks, load balancing, or graceful degradation.

## Avoid when

- The service is not worth the operational cost of redundancy.
- The failure mode is disaster-scale rather than local-scale. Use disaster recovery as a separate pattern.
- The design cannot safely run more than one active instance because of shared mutable state, locking, or licensing limits.

## Context and problem

Infrastructure platforms make it easy to create resources, but availability comes from the system shape, not from resource creation alone. Agents should look for hidden single points of failure across compute, network, storage, identity, secrets, queues, external services, and deployment automation.

## Forces

- Availability versus cost: more redundancy usually means more running resources.
- Availability versus data consistency: synchronous replication may reduce data loss but increase latency or coupling.
- Availability versus operability: failover must be observable, tested, and reversible.
- Redundancy versus blast radius: shared dependencies can erase the benefit of multiple instances.

## Guidance

Design around failure domains. Identify the smallest failure that must not cause user-visible outage, then ensure at least one healthy path remains outside that domain. Redundancy is incomplete unless routing, state, dependencies, and deployment procedures also avoid the same single failure domain.

## Implementation moves

- Define the service's availability objective and the failure domains it must survive.
- Run multiple service instances across independent compute hosts or zones.
- Put traffic through health-aware routing or load balancing.
- Remove shared single points of failure in dependencies, secrets, network paths, and control-plane automation.
- Make health checks reflect real user capability, not just process liveness.
- Design graceful degradation for optional dependencies.
- Test failover with game days, chaos experiments, or controlled dependency isolation.

## Checks

- What single component failure still takes the service down?
- Can a deployment fail on one instance while traffic continues through another?
- Are health checks tied to the capability users need?
- Are dependencies as redundant as the service tier?
- Has failover been tested recently, and is the recovery path automated?

## Failure modes

- Creating multiple instances that all depend on one database, NAT gateway, secret store path, or identity provider configuration.
- Health checks that pass even when the service cannot satisfy real requests.
- Manual failover runbooks that are not tested under pressure.
- Active-active designs that corrupt state because write ownership is unclear.

## Agent trigger hints

Use this pattern when the user says or implies:

- how do we make this highly available
- avoid single points of failure
- active active or active passive
- survive a zone outage
- health checks and failover
- uptime target or availability objective

## Source notes

This is an original synthesis pattern. The source lineage includes general reliability practice and the public O'Reilly overview/table-of-contents framing around unreliable systems, reproducibility, stacks, safe change, and continuity. Do not treat this file as a recap of any chapter.
