---
id: iac.terraform-module-contract
title: Terraform Module Contract
type: design-pattern
status: draft
summary: Design Terraform modules as explicit contracts with inputs, outputs, provider expectations, path-safe internals, and versioned consumption rather than copied environment code.
tags:
  - infrastructure-as-code
  - terraform
  - modules
  - reuse
  - contracts
  - inputs
  - outputs
  - versioning
aliases:
  - terraform module design
  - terraform module inputs outputs
  - reusable terraform modules
  - terraform root module
  - module contract
applies_when:
  - Multiple environments, services, or teams need the same infrastructure shape with controlled variation.
  - A Terraform module is becoming a reusable unit rather than a one-off root configuration.
avoid_when:
  - The infrastructure is unique enough that a reusable module would hide more intent than it clarifies.
  - Consumers need to vary nearly every internal resource, which signals that the boundary is wrong.
related:
  - iac.reusable-stack
  - iac.simple-stack-parameters
  - iac.component-boundaries
  - iac.terraform-production-module-design
  - iac.package-infrastructure-code
sources:
  - "book: Yevgeniy Brikman, Terraform: Up & Running, third edition; Chapter 4, Terraform Modules."
source_confidence: high
last_reviewed: 2026-06-05
---

# Terraform Module Contract

## Intent

Make reusable Terraform modules predictable by defining clear inputs, outputs, provider expectations, file-path behavior, and versioning discipline.

## Use when

- The same Terraform configuration is copied across staging, production, regions, or services.
- Teams need a reusable module for a load balancer, database, cluster, network, or service stack.
- A module exposes outputs consumed by another module, stack, or deployment system.
- Module consumers should configure behavior without editing module internals.
- A shared module will be used from Git, a registry, or another versioned source.

## Avoid when

- A one-off root module is clearer and cheaper than a premature reusable abstraction.
- The module has too many modes, flags, and optional branches to explain its behavior.
- Provider configuration, credentials, or environment-specific policy must stay in the root module.
- The desired variation is still unknown and should be learned through a few concrete implementations first.

## Context and problem

Terraform makes it easy to copy working code into another environment. That works briefly, then environment copies drift, fixes are missed, and reviewers cannot tell whether differences are intentional. Modules solve this only when their public contract is deliberate. A module that leaks internals, configures providers unexpectedly, or exposes unstable outputs becomes another form of coupling.

The contract is more than `variables.tf` and `outputs.tf`. It includes which provider aliases are expected, which files can be referenced safely, which inputs are optional or validated, which outputs are stable, and how consumers choose a version.

## Forces

- Reuse reduces drift, but over-generalized modules become hard to reason about.
- Inputs enable variation, but each input adds a support commitment.
- Outputs enable composition, but unstable outputs couple consumers to internals.
- Modules should be portable, but provider configuration often belongs to the root.
- Versioning protects consumers, but it requires release discipline.

## Guidance

Keep reusable modules focused on one coherent infrastructure capability. Put environment-specific decisions in root modules or configuration, and expose only the inputs needed to express supported variation. Use outputs as stable integration points, not as a dump of internal resource attributes.

Configure providers in the root module and pass provider aliases explicitly when a child module must work with multiple provider instances. Use `path.module` for files bundled with the module so calls from other directories remain safe. Version shared module sources and document compatibility expectations.

## Implementation moves

- Start from two or three concrete environment copies before extracting a shared module.
- Define required inputs, optional inputs with defaults, and validations for important constraints.
- Expose outputs needed by callers and downstream stacks; avoid exposing every internal ID.
- Keep provider blocks out of reusable child modules unless there is a deliberate exception.
- Use `required_providers` to state provider source and version constraints.
- Use `path.module` for templates and files shipped inside the module.
- Pin shared module versions from root modules using tags or registry versions.
- Add examples that exercise the supported contract.

## Checks

- Can a consumer use the module without reading every internal resource?
- Are environment differences expressed as inputs rather than copied source edits?
- Are outputs stable, named by intent, and documented?
- Are provider requirements explicit without hardcoding credentials or regions?
- Is the module version pinned by consumers?
- Would adding a new input simplify real variation or just expand a fragile mode matrix?

## Failure modes

- Copy-paste environments hidden behind similar-looking folders.
- A module that configures providers internally and prevents callers from choosing account or region.
- Outputs that expose internal implementation and break consumers during refactoring.
- Too many boolean flags that create untested combinations.
- Referencing files relative to the caller instead of the module, causing remote module failures.

## Agent trigger hints

Use this pattern when the user says or implies:

- Terraform modules
- reusable module design
- module inputs and outputs
- root module vs child module
- provider in module
- path.module
- module source ref
- avoid copy paste Terraform

## Source notes

Synthesized from Chapter 4 of Terraform: Up & Running, third edition, including module basics, inputs, locals, outputs, gotchas, and versioning. No source excerpts are stored here.
