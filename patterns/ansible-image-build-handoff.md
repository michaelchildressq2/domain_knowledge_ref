---
id: iac.ansible-image-build-handoff
title: Ansible Image Build Handoff
type: delivery-pattern
status: draft
summary: Use Ansible inside image-building workflows to configure base images once, then hand runtime variation to inventory, variables, and deployment automation.
tags:
  - infrastructure-as-code
  - ansible
  - image-building
  - packer
  - immutable-infrastructure
  - delivery-pipeline
  - reproducibility
aliases:
  - Ansible with Packer
  - bake images with Ansible
  - immutable image handoff
  - golden image playbook
applies_when:
  - A team builds VM, cloud, or container images and wants to reuse Ansible configuration logic.
  - Slow or security-sensitive host setup should happen before deployment time.
  - The same baseline image supports multiple runtime environments.
avoid_when:
  - Runtime configuration changes too often to bake safely.
  - Secrets, host identity, or environment-specific data would be embedded in the image.
related:
  - iac.reproducible-infrastructure
  - iac.disposable-infrastructure
  - iac.ansible-playbook-convergence
  - iac.ansible-control-node-dependency-isolation
sources:
  - "book: Bas Meijer, Lorin Hochstein, and Rene Moser, Ansible: Up and Running, third edition; Chapters 13, 16, 21, and 24."
source_confidence: high
last_reviewed: 2026-06-05
---

# Ansible Image Build Handoff

## Intent

Use Ansible to build repeatable machine or container images while keeping environment-specific runtime configuration out of the baked artifact.

## Use when

- Package installation, OS hardening, language runtime setup, or baseline agents are slow or risky to perform on every deployment.
- Packer or another image builder can run Ansible as a provisioner.
- The image should be tested and promoted through environments.
- Runtime deployments need faster startup or reduced configuration drift.
- Security teams want hardened base images with traceable build steps.

## Avoid when

- The playbook must discover live host state that only exists at runtime.
- The image would contain secrets, credentials, node identity, or environment-specific endpoints.
- Baking images would slow feedback more than it improves deployment confidence.
- The platform already provides trusted base images and runtime configuration is minimal.

## Context and problem

Ansible can configure running hosts, and image builders can create reusable artifacts. Teams often need both: build a secure, patched, dependency-ready image once, then apply small runtime differences at deployment. If the boundary is unclear, images become stale snowflakes or playbooks repeatedly redo expensive setup.

The Ansible source covers containers, Packer, cloud images, and security baselines. The pattern is a handoff: bake stable baseline state into images, then let inventory, variables, and deployment playbooks handle runtime variation.

## Forces

- Faster deployments versus slower image build pipelines.
- Immutable baseline confidence versus flexibility at runtime.
- Security hardening versus accidentally baking credentials.
- Cross-cloud image portability versus provider-specific build steps.
- Reusing Ansible roles versus keeping image build roles separate from runtime roles.

## Guidance

Separate image-time and runtime responsibilities. Use Ansible in the image build for stable operating system, package, hardening, toolchain, and agent configuration. Exclude secrets, hostnames, environment credentials, and data that should be assigned at deploy time. Version images, capture build provenance, and test images before promotion.

Keep image playbooks idempotent even though the build is usually a fresh machine. Idempotency makes local development, rebuilds, and troubleshooting safer.

## Implementation moves

- Define which Ansible roles run at image build time and which run at runtime.
- Use Packer or a comparable builder to create VM, cloud, or container images.
- Pin Ansible roles, collections, and package repositories used during image builds.
- Remove build credentials and temporary files before finalizing the image.
- Run smoke or compliance tests against the built image.
- Tag images with source version, build time, role versions, and security baseline identifiers.
- Promote images through environments instead of rebuilding differently per environment.
- Keep runtime configuration in inventory, variables, secret stores, or deployment systems.

## Checks

- Does the image contain only stable baseline configuration?
- Are secrets and environment-specific values absent from the artifact?
- Can the image be traced to source, role, collection, and package versions?
- Does the deployment path avoid redoing image-time work unnecessarily?
- Are image tests run before promotion?
- Is there a rebuild process for base image updates and vulnerability fixes?

## Failure modes

- Baking production credentials or host-specific values into images.
- Running the same heavy setup both in the image pipeline and at deployment time.
- Treating a manually prepared image as a reusable artifact without source provenance.
- Letting image playbooks diverge from runtime playbooks without an explicit boundary.
- Rebuilding images per environment and losing artifact promotion confidence.

## Agent trigger hints

Use this pattern when the user says or implies:

- Ansible with Packer
- bake AMI or VM image
- golden image playbook
- image build pipeline
- immutable infrastructure with Ansible
- configure base image

## Source notes

Synthesized from Ansible: Up and Running, third edition, especially Chapter 13 on containers, Chapter 16 on Packer and cloud images, Chapter 21 on security automation image workflows, and Chapter 24 on deployment and reproducibility evidence. No source excerpts are stored here.
