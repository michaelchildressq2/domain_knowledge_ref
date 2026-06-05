---
id: iac.ansible-collection-dependency-manifest
title: Ansible Collection Dependency Manifest
type: delivery-pattern
status: draft
summary: Use Ansible collections and dependency manifests to package modules, roles, plugins, and playbooks as versioned content with explicit fully qualified dependencies.
tags:
  - infrastructure-as-code
  - ansible
  - collections
  - dependency-management
  - versioning
  - modules
  - packaging
aliases:
  - Ansible collections
  - fully qualified collection name
  - ansible-galaxy collection install
  - collection requirements
applies_when:
  - Playbooks depend on modules, roles, or plugins outside ansible-core.
  - Teams publish reusable Ansible content internally or externally.
  - Automation runners need to install a known set of content before execution.
avoid_when:
  - The project only uses ansible-core modules and no reusable content should be packaged.
  - A single local role is not yet stable enough to publish as a collection.
related:
  - iac.package-infrastructure-code
  - iac.ansible-role-capability-boundary
  - iac.ansible-control-node-dependency-isolation
sources:
  - "book: Bas Meijer, Lorin Hochstein, and Rene Moser, Ansible: Up and Running, third edition; Chapters 1, 14, 15, 17, 21, 22, 23, and 24."
source_confidence: high
last_reviewed: 2026-06-05
---

# Ansible Collection Dependency Manifest

## Intent

Make Ansible content dependencies explicit and distributable by packaging related roles, modules, and plugins in collections and installing versioned dependencies from manifests.

## Use when

- A playbook uses modules from cloud, network, Windows, container, or community content.
- A team needs to share multiple related roles, modules, plugins, or playbooks.
- CI, local development, and Automation Controller must resolve the same content.
- Unqualified module names create ambiguity or compatibility risk.
- A project needs to consume certified, community, or internally published content.

## Avoid when

- The content is still exploratory and package versioning would create false stability.
- A role-only repository is enough and there are no modules or plugins to distribute.
- The project should vendor dependencies for offline reasons and cannot install from a registry.

## Context and problem

Modern Ansible separates core components from certified and community content. This makes Ansible more maintainable, but it also means playbook behavior depends on installed collections. If collection dependencies are implicit, two runners can resolve different modules or versions.

Collections provide a packaging boundary for modules, roles, plugins, and playbooks. Dependency manifests and fully qualified collection names turn that packaging boundary into a reproducible contract.

## Forces

- Easier module discovery versus dependency sprawl.
- Fully qualified names versus shorter playbook syntax.
- Collection releases versus source repository changes.
- Community content reuse versus support and certification requirements.
- Local development convenience versus controller and CI reproducibility.

## Guidance

Declare collection dependencies explicitly and install them as part of the project setup, CI job, Molecule dependency phase, or execution environment build. Use fully qualified collection names where ambiguity or compatibility matters, especially for cloud, network, container, and community modules. Package related reusable content as a collection when the distribution unit is broader than one role.

Treat collection upgrades like code changes. Review release notes, pin versions when reproducibility matters, and run lint and scenario tests after upgrades.

## Implementation moves

- Keep a collection dependency manifest in source control.
- Install collections during local bootstrap, CI, and runner image builds.
- Use fully qualified collection names for non-core or ambiguous modules.
- Publish internal collections when teams need to share modules, plugins, and roles together.
- Separate project roles, shared roles, Galaxy roles, and collection content in repository layout.
- Pin or constrain collection versions for production automation.
- Include collection requirements in Molecule and Automation Platform execution environments.

## Checks

- Can a clean runner install every collection needed by the project?
- Are cloud, network, Windows, and container modules resolved from explicit collections?
- Are collection versions pinned or otherwise controlled for production jobs?
- Do playbooks avoid ambiguous unqualified module names where resolution matters?
- Is internally shared content packaged at the right boundary?
- Are upgrades tested before controller jobs or CI pipelines consume them?

## Failure modes

- Assuming every runner has the same community collections installed.
- Using short module names that resolve differently after a dependency change.
- Publishing related modules and roles as loose files with no versioned distribution.
- Letting Automation Platform depend on collections that local tests never install.
- Treating certified, community, and internal content as interchangeable without support expectations.

## Agent trigger hints

Use this pattern when the user says or implies:

- Ansible collections
- fully qualified collection name
- collection requirements.yml
- ansible-galaxy collection install
- package Ansible modules and roles
- missing Ansible collection in CI

## Source notes

Synthesized from Ansible: Up and Running, third edition, especially Chapter 15 on collections; Chapters 14, 17, and 21 on collection-backed Molecule, cloud, and network modules; Chapter 22 on CI dependencies; Chapter 23 on Automation Hub; and Chapter 24 on decoupling roles and collections. No source excerpts are stored here.
