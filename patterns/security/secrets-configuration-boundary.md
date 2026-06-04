---
id: platform.secrets-configuration-boundary
title: Secrets and Configuration Boundary
type: architecture-pattern
status: seed
summary: Separate non-sensitive configuration, sensitive secrets, and runtime identity
  so infrastructure code stays reusable and safe.
tags:
- platform-engineering
- infrastructure-as-code
- configuration-management
- secrets-management
- security
- parameterization
- runtime-operations
- implementation-planning
- cloud-agnostic
aliases:
- secret handling
- runtime secrets
- configuration registry
- secretless authorization
applies_when:
- The user asks how to pass parameters, config, credentials, tokens, certificates,
  or keys to infrastructure or workloads.
- Secrets risk appearing in code, state, plans, logs, images, or artifacts.
- A system needs different configuration per environment, region, or tenant.
avoid_when:
- The value is public, static, and safe to store in code.
- The value is not configuration but a runtime fact that should be discovered dynamically.
- The platform already provides a safer managed identity mechanism and no secret material
  needs to be distributed.
related:
- platform.environment-parity
- platform.iac-delivery
- platform.pipeline-governance
sources:
- 'iac2: Kief Morris, Infrastructure as Code, 2nd Edition, O''Reilly Media'
- synthesis: general platform security and infrastructure-as-code practice
source_confidence: medium
last_reviewed: 2026-06-04
subject_area: security
---

# Secrets and Configuration Boundary

## Intent

Keep infrastructure code reusable while preventing sensitive values from leaking through repositories, state, build artifacts, logs, or runtime environments.

## Use when

- A user asks where to store stack parameters, credentials, certificates, API keys, database passwords, or environment variables.
- A pipeline needs to inject values into infrastructure or workload deployment.
- Configuration differs by environment, tenant, region, or account.

## Avoid when

- The value is safe, public, and stable enough to live in version control.
- Workloads can use workload identity, instance identity, service account binding, or another secretless authorization path.
- The value belongs in service discovery or a runtime API instead of static configuration.

## Context and problem

Infrastructure code needs parameters, but not all parameters are equal. Mixing secrets, environment configuration, and generated runtime facts creates leakage risk and makes reproducibility harder. Agents should recommend different storage and injection paths by sensitivity and lifecycle.

## Forces

- Reproducibility versus secrecy: plans need enough information to be deterministic without exposing secrets.
- Convenience versus least privilege: environment variables are easy but often leak.
- Centralization versus blast radius: one secret store can simplify management but increase impact if misused.
- Runtime flexibility versus deployment certainty: dynamic lookup can fail at runtime.

## Guidance

Classify values before choosing where they live. Store non-sensitive intended configuration in versioned configuration files or registries. Store secrets in a secrets manager or key-management system. Prefer identity-based access over distributing static secrets. Inject sensitive values at the latest safe point and avoid writing them to state or logs.

## Implementation moves

- Classify each value as public config, sensitive secret, generated output, runtime discovery, or identity binding.
- Keep public config in reviewed files or parameter registries.
- Keep secrets out of source control, plan output, state files, images, and logs.
- Use managed identity or short-lived credentials when possible.
- Scope access by environment, workload, and pipeline stage.
- Rotate secrets and test rotation paths.
- Redact sensitive output and protect state storage.

## Checks

- Can a new environment be rebuilt without copying secrets into code?
- Are secrets visible in state, plan, logs, artifacts, or container images?
- Are values scoped to the smallest useful blast radius?
- Is there a rotation process and has it been tested?
- Can the workload use identity instead of a distributed secret?

## Failure modes

- Committing secrets or encrypted blobs without a clear key-management process.
- Passing secrets through pipeline logs or plan artifacts.
- Treating generated runtime values as static configuration.
- Sharing one credential across environments or services.
- Failing to rotate because consumers are unknown.

## Agent trigger hints

Use this pattern when the user says or implies:

- where should secrets live
- stack parameters
- environment variables
- configuration registry
- inject secrets at runtime
- keep secrets out of terraform state
- service account or workload identity

## Source notes

This is an original synthesis. Public book contents identify stack parameters, configuration registries, secrets as parameters, encrypted secrets, and runtime injection as areas of concern; this file turns those topics into reusable guidance.
