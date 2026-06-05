---
id: iac.terraform-provider-topology
title: Terraform Provider Topology
type: implementation-pattern
status: draft
summary: Model Terraform provider source, version, aliases, accounts, regions, and module injection explicitly so multi-provider infrastructure stays reviewable and least-privilege.
tags:
  - infrastructure-as-code
  - terraform
  - providers
  - multi-account
  - multi-region
  - aliases
  - versioning
  - module-boundaries
aliases:
  - Terraform provider aliases
  - multiple Terraform providers
  - multi account Terraform
  - multi region Terraform
  - provider injection
  - required_providers
applies_when:
  - Terraform needs more than one provider instance, account, region, cluster, namespace, or provider type.
  - Reusable modules must operate with caller-selected providers instead of hardcoded credentials or locations.
avoid_when:
  - A stack genuinely uses one provider instance and aliases would add indirection without reducing risk.
  - The module boundary is so broad that provider topology cannot be explained simply.
related:
  - iac.terraform-module-contract
  - iac.terraform-state-isolation-layout
  - iac.package-infrastructure-code
  - iac.secrets-out-of-source
sources:
  - "book: Yevgeniy Brikman, Terraform: Up & Running, third edition; Chapter 7, Working with Multiple Providers."
source_confidence: high
last_reviewed: 2026-06-05
---

# Terraform Provider Topology

## Intent

Make provider selection and credential boundaries explicit when Terraform spans multiple regions, accounts, clouds, clusters, or provider types.

## Use when

- A stack deploys to multiple AWS regions, Azure subscriptions, GCP projects, Kubernetes clusters, or SaaS accounts.
- A child module needs to create related resources in more than one provider instance.
- Provider versions or sources must be controlled for reproducibility and security.
- Cross-account or cross-region replication requires primary and replica provider roles.
- The same module must be reusable across different caller-selected providers.

## Avoid when

- One root provider configuration is enough and aliases would obscure simple code.
- Provider aliases are used to hide unrelated deployments in one oversized stack.
- The credentials required by different provider instances should be isolated into separate states instead.
- A child module can be simpler by accepting IDs or endpoints rather than managing remote resources itself.

## Context and problem

Terraform providers are plugins that translate Terraform configuration into platform API calls. Simple examples often use one provider block, but real systems commonly span multiple regions, accounts, or provider types. Without an explicit provider topology, modules hardcode regions, credentials leak across boundaries, upgrades are inconsistent, and reviewers cannot tell which platform a resource will affect.

Provider topology is part of the architecture. It determines credential scope, blast radius, module portability, and how reproducible a plan is across machines and CI runners.

## Forces

- One stack can coordinate cross-provider resources, but separate states may be safer for ownership and credentials.
- Provider aliases enable reuse, but too many aliases make plans hard to understand.
- Child modules should be portable, but they still need clear provider requirements.
- Version constraints improve reproducibility, but overly tight constraints can block necessary provider fixes.
- Multi-account and multi-region systems need explicit intent so the wrong provider does not receive a resource.

## Guidance

Declare provider requirements explicitly and use aliases for intentional multiple instances of the same provider. Configure credentials and regions in root modules, then pass provider instances into child modules that need them. Keep provider aliases named by role or location, not by temporary implementation detail.

Use separate state files when provider boundaries also represent different ownership, credentials, risk, or lifecycle. Use one state only when coordinated changes across provider instances are truly needed and the apply credential model is acceptable.

## Implementation moves

- Add `required_providers` with source and version constraints in reusable modules.
- Define provider aliases in root modules for each region, account, cluster, or role.
- Pass aliased providers explicitly to child modules through the `providers` map.
- Name aliases by durable role, such as `primary`, `replica`, `audit`, or region/account identifier.
- Keep provider credentials out of child modules and source code.
- Review plans with provider alias context visible in resource addresses.
- Pin and upgrade provider versions through a deliberate workflow.
- Split state when different provider instances require different owners or permissions.

## Checks

- Can a reviewer tell which account, region, or cluster each resource targets?
- Are provider versions constrained and committed through lock files or equivalent workflow?
- Do child modules avoid hardcoded provider configuration?
- Are aliases named consistently and passed explicitly?
- Would a compromised apply credential affect only the intended provider boundary?
- Are multi-provider dependencies necessary inside one state, or should outputs connect separate states?

## Failure modes

- Default provider configuration accidentally used where an alias was intended.
- Child modules that hardcode region or account and cannot be reused safely.
- One state managing many accounts with a credential broader than any team should have.
- Unpinned provider versions changing behavior between developer laptops and CI.
- Alias names that encode temporary structure and break when topology evolves.

## Agent trigger hints

Use this pattern when the user says or implies:

- Terraform multiple providers
- provider alias
- AWS multi account Terraform
- multi region Terraform
- required_providers
- pass provider to module
- Kubernetes and AWS providers together
- provider version pinning

## Source notes

Synthesized from Chapter 7 of Terraform: Up & Running, third edition, including provider installation, versioning, aliases, multi-region and multi-account examples, and modules that accept multiple providers. No source excerpts are stored here.
