---
id: platform.adapter-operability-normalization
title: Adapter Operability Normalization
type: architecture-pattern
status: draft
summary: Use an adapter container to translate heterogeneous application interfaces into standard operational contracts for metrics, logs, health, or control planes.
tags:
  - platform-engineering
  - sre
  - observability
  - operability
  - modular-architecture
  - runtime-operations
  - implementation-planning
  - module-boundaries
  - testing
  - kubernetes
  - adapter
aliases:
  - adapter pattern
  - metrics exporter sidecar
  - log normalization adapter
  - health check adapter
  - interface normalization
applies_when:
  - A service, database, or third-party image exposes metrics, logs, or health in a format the platform cannot consume directly.
  - You need a consistent operational interface across heterogeneous applications.
  - Modifying or forking the application image would create maintenance burden.
avoid_when:
  - You own the application and can implement the standard interface directly with little risk.
  - The adapter would mask a broken or unsupported application contract.
  - The adapter needs privileged access that would be unacceptable for the workload.
related:
  - platform.container-contracts-for-reuse
  - platform.sidecar-application-augmentation
  - platform.reusable-work-queue-interface
  - data.trust-but-verify-dataflows
sources:
  - 'book: Brendan Burns, Designing Distributed Systems, Chapter 4: Adapters'
source_confidence: high
last_reviewed: 2026-06-05
---

# Adapter Operability Normalization

## Intent

Make heterogeneous applications operable through common platform interfaces without modifying each application image.

## Use when

- A monitoring system expects one metrics protocol, but applications expose many formats.
- A log pipeline expects stdout or structured events, but applications write files or custom formats.
- A database or packaged service needs richer health checks than process or port checks.
- A third-party image should remain unchanged so upstream updates stay easy to apply.
- Platform teams need one reusable exporter, logger, or health adapter across many workloads.

## Avoid when

- The application already exposes the desired standard interface.
- The adapter introduces more moving parts than direct instrumentation.
- The adapter requires parsing unstable human-readable output when a structured source exists.
- The adapter consumes enough resources to affect the user-facing application.
- Compliance or security rules forbid exposing the underlying operational data to a colocated helper.

## Context and problem

Real distributed systems include custom code, vendor binaries, open source services, and legacy applications. Each may expose metrics, logs, health, and control interfaces differently. Operating such systems with one monitoring, logging, alerting, or orchestration platform requires a standard interface.

An adapter container bridges this mismatch. It sits beside the application, reads or queries the application's native interface, and emits the platform-standard interface. This keeps the application image unchanged while making the workload conform to operational expectations.

## Forces

- Standard operations versus heterogeneous application behavior.
- Direct code changes versus maintainable wrapping.
- Reusable adapters versus bespoke image forks.
- Accurate signal versus translation loss.
- Dedicated adapter resources versus extra pod footprint.
- Fast upstream upgrades versus locally patched images.

## Guidance

Prefer adapter containers when the integration concern is operational and the source application should not be modified. Keep the adapter's transformation narrow and testable. The adapter should not become a broad business facade; it should translate metrics, logs, health, or similar operational signals into a standard shape.

Use structured interfaces when available. If the adapter must parse text or logs, define error handling for parse failures and version changes. Monitor the adapter separately so that a healthy app with a broken adapter does not appear fully operable.

## Implementation moves

- Identify the source interface: file, stdout, HTTP endpoint, database query, command-line tool, socket, or native protocol.
- Define the target platform interface: metrics schema, log fields, health endpoint, readiness result, or control-plane API.
- Run the adapter with the minimum network, filesystem, and credentials needed to read the source interface.
- Configure platform discovery so the monitoring or logging stack targets the adapter endpoint, not the raw application.
- Allocate resource requests and limits for adapter CPU and memory.
- Include adapter version and source application compatibility in image labels or deployment metadata.
- Add tests using realistic raw outputs from each supported application version.
- Decide whether adapter failure should mark the workload unhealthy, degrade observability only, or trigger restart.
- Alert separately on adapter scrape failures, parse errors, and stale output.
- Document which semantics are preserved and which are approximated by the adapter.

## Checks

- Is the adapter translating an operational concern rather than hiding business behavior?
- Is the source interface stable enough for a reusable adapter?
- Can the app be updated independently of the adapter, and vice versa?
- Are parse failures, stale metrics, and missing logs visible?
- Does the adapter have bounded resource usage?
- Does the health adapter actually test representative behavior rather than only process liveness?
- Are standard labels and metric names consistent with the rest of the platform?
- Is direct instrumentation cheaper for applications the team owns?

## Failure modes

- Forking application images for every operational integration and then falling behind upstream.
- Treating adapter health as application health without understanding what the adapter checks.
- Parsing brittle log text without tests or version pinning.
- Letting adapter CPU or memory pressure degrade the main workload.
- Duplicating adapters with slightly different metric names across teams.
- Forgetting to secure adapter endpoints that expose sensitive operational data.
- Normalizing away important application-specific context.

## Agent trigger hints

Use this pattern when the user says or implies:

- Prometheus exporter
- normalize logs
- adapter container
- standard health endpoint
- make this third-party image observable
- do not fork the image
- metrics format mismatch

## Source notes

Synthesized from Chapter 4 examples covering Prometheus exporters, fluentd log normalization, and rich database health checks. This file contains original guidance and source pointers only.
