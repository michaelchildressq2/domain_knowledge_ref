---
id: iac.secrets-out-of-source
title: Secrets Out Of Source
type: governance-pattern
status: draft
summary: Keep secret values out of source control while preserving coded references, access policy, and delivery flow.
tags:
  - infrastructure-as-code
  - secrets-management
  - security
  - governance
  - delivery-pipeline
  - cloud-agnostic
aliases:
  - do not commit secrets
  - secret references
  - vaulted configuration
applies_when:
  - Infrastructure code needs credentials, keys, tokens, certificates, or private connection data.
  - Teams want reproducible deployment without exposing sensitive values.
avoid_when:
  - The value is not sensitive and belongs in ordinary configuration.
  - A regulated workflow requires a specific managed secret system not yet available.
related:
  - iac.externalized-configuration
  - iac.stack-parameter-registry
  - iac.policy-as-code-guardrails
sources:
  - "book: Kief Morris, Infrastructure as Code, second edition, iac2.pdf; Chapter 4 with supporting delivery and governance concerns."
source_confidence: high
last_reviewed: 2026-06-04
---

# Secrets Out Of Source

## Intent

Make deployments repeatable without leaking sensitive values through repositories, logs, or generated artifacts.

## Use when

- Infrastructure code needs credentials, keys, tokens, certificates, or private connection data.
- Teams want reproducible deployment without exposing sensitive values.

## Avoid when

- The value is not sensitive and belongs in ordinary configuration.
- A regulated workflow requires a specific managed secret system not yet available.

## Context and problem

Secrets are often needed by infrastructure automation, but storing them as source creates persistent compromise risk.

## Forces

- Reproducibility versus confidentiality
- Developer convenience versus blast radius
- Auditability versus secret exposure

## Guidance

Store secret values in a managed secret system. Put references, policies, and wiring in code, and ensure pipelines retrieve secrets only at the point of need with least privilege.

## Implementation moves

- Classify which parameters are sensitive.
- Reference secrets by name or identity rather than embedding values.
- Grant pipeline identities narrow read access.
- Scan repositories and pipeline logs for accidental exposure.

## Checks

- Could someone clone the repo without gaining secret values?
- Are secret reads audited and scoped?
- Can rotation happen without editing multiple source files?

## Failure modes

- Encoding secrets and treating them as safe.
- Writing secret values into plan files or logs.
- Using one broad deployment credential for all environments.

## Agent trigger hints

Use this pattern when the user says or implies:

- secrets in terraform
- commit credentials
- vault parameters
- pipeline secrets

## Source notes

Synthesized from Chapter 4 with supporting delivery and governance concerns. Source confidence is high because the chapter text was extracted locally from the user-provided PDF. No source excerpts are stored here.
