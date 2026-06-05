---
id: platform.container-contracts-for-reuse
title: Container Contracts for Reuse
type: architecture-pattern
status: draft
summary: Treat reusable containers as callable components with explicit parameters, stable APIs, documented behavior, and compatibility checks.
tags:
  - platform-engineering
  - cloud-architecture
  - modular-architecture
  - operability
  - design-review
  - implementation-planning
  - module-boundaries
  - parameterization
  - version-control
  - kubernetes
  - container-contracts
aliases:
  - reusable container interface
  - container API surface
  - parameterized containers
  - container image contract
applies_when:
  - A sidecar, ambassador, adapter, worker, or utility container is intended for reuse across teams or services.
  - A container's behavior is configured by environment variables, command arguments, mounted files, ports, labels, or network calls.
  - Teams are treating a container image as an internal platform component.
avoid_when:
  - The container is a one-off private implementation and reuse would add process without value.
  - The component behavior is still experimental and not yet stable enough to promise compatibility.
  - A language library or managed platform feature provides the same reuse with less operational surface.
related:
  - platform.sidecar-application-augmentation
  - platform.ambassador-local-service-broker
  - platform.adapter-operability-normalization
  - platform.reusable-work-queue-interface
sources:
  - 'book: Brendan Burns, Designing Distributed Systems, Chapter 1: Introduction'
  - 'book: Brendan Burns, Designing Distributed Systems, Chapter 2: Designing Sidecars for Modularity and Reusability'
source_confidence: high
last_reviewed: 2026-06-05
---

# Container Contracts for Reuse

## Intent

Make reusable container images predictable enough for agents and teams to compose them safely without reading their internals or rebuilding them for every use.

## Use when

- The design depends on reusable sidecars, adapters, ambassadors, workers, proxies, exporters, or operators.
- A container consumes configuration through environment variables, command-line arguments, mounted files, labels, ports, sockets, or HTTP APIs.
- Several services need the same operational helper, such as TLS termination, metrics export, log normalization, configuration sync, or file processing.
- The team wants platform components that behave more like standard libraries than bespoke deployment fragments.
- A proposed change to a shared image may alter parameter names, units, defaults, exposed ports, output formats, or callback behavior.

## Avoid when

- Reuse is speculative and the container is not yet used outside one service.
- The image needs deep application-specific coupling that cannot be expressed as a narrow contract.
- A managed service, service mesh, or orchestration feature supplies the behavior with clearer support boundaries.
- The contract would conceal unsafe assumptions, such as access to host namespaces, broad credentials, or shared mutable directories.

## Context and problem

Container composition only becomes a reusable platform technique when the containers have stable boundaries. A helper image may look self-contained, but its real API includes all of its parameters, ports, mounted paths, network calls, labels, health behavior, files it reads or writes, and operational expectations. If those boundaries are implicit, small changes become breaking changes for downstream services.

Reusable containers also need enough documentation and metadata for humans and tools to use them correctly. Without this, every consumer must rediscover ports, variables, resources, privileges, and compatibility rules. The result is image forking, hidden drift, and unsafe upgrades.

## Forces

- Reuse versus application-specific tuning.
- Fast image evolution versus compatibility for many consumers.
- Small operational helpers versus large implicit API surfaces.
- Easy defaults versus explicit configuration.
- Documentation discipline versus low-friction publishing.
- Platform consistency versus local team autonomy.

## Guidance

Design reusable containers as productized components. Name every externally visible behavior as part of the contract, even if it is not a traditional HTTP API. Prefer explicit parameters, stable defaults, versioned interfaces, documented units, narrow permissions, and metadata that automation can inspect.

Treat changes to parameter names, accepted values, default units, port behavior, file paths, output schemas, readiness semantics, and labels as compatibility changes. If a change would surprise an existing consumer, version it, provide a transition path, or keep backward-compatible parsing.

Favor narrow reusable containers that do one platform job well. A helper image should be useful across workloads because it exposes a simple contract, not because consumers know how it is implemented.

## Implementation moves

- List the image's full API surface: env vars, command arguments, exposed ports, mounted volumes, expected files, emitted files, labels, probes, network calls, signals, and required privileges.
- Version externally consumed HTTP APIs and file formats from the first release, even if `v2` is not planned.
- Define parameter units explicitly, such as seconds versus milliseconds, bytes versus MiB, or percentage versus ratio.
- Set safe defaults with `ENV`, config templates, or equivalent deployment parameters, and document when defaults are unsuitable for production.
- Use image labels for maintainer, source, version, license, documentation, and support ownership.
- Provide readiness and health semantics that say when the helper is ready to accept traffic or perform its support role.
- Add compatibility tests that start the image with representative downstream configurations.
- Publish examples for common compositions, such as a pod with a main app plus the helper container.
- Keep the helper's credentials and mounts narrower than the main application whenever possible.
- Deprecate parameters before removing them, and keep release notes focused on contract changes.

## Checks

- Can a consumer configure the image without reading its source?
- Are parameter names, types, units, defaults, and allowed values documented?
- Is every exposed port, mounted path, and generated file intentional?
- Would changing a default alter behavior for existing consumers?
- Are image labels and version metadata sufficient for inventory and support?
- Are there contract tests for the most common composition scenarios?
- Does the image fail clearly when required parameters are missing or invalid?
- Can the image be upgraded independently from the main application?

## Failure modes

- Treating environment variables and file paths as implementation details until a change breaks consumers.
- Reusing a helper that depends on undocumented privileges, host paths, or namespace sharing.
- Changing units or parsing behavior while keeping the same parameter name.
- Publishing images with no owner, version, or usage metadata.
- Overloading one helper with many unrelated responsibilities.
- Documenting only Docker commands while omitting orchestration constraints such as probes, resource requests, and secrets.
- Forking a third-party image instead of wrapping it with a clear adapter or sidecar contract.

## Agent trigger hints

Use this pattern when the user says or implies:

- make this sidecar reusable
- standard container interface
- document image parameters
- can we change this env var
- shared platform container
- container contract
- image API surface

## Source notes

Synthesized from the book's discussion of reusable distributed-system components and Chapter 2's treatment of parameterization, API surface, and container documentation. This file contains original guidance and source pointers only.
