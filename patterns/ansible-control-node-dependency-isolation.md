---
id: iac.ansible-control-node-dependency-isolation
title: Ansible Control Node Dependency Isolation
type: delivery-pattern
status: draft
summary: Isolate Ansible, Python, collection, and control-node dependencies per project so playbook behavior is reproducible across contributors and automation runners.
tags:
  - infrastructure-as-code
  - ansible
  - dependency-management
  - reproducibility
  - python
  - ci-cd
  - platform-engineering
aliases:
  - ansible virtualenv
  - pin ansible version
  - ansible control node dependencies
  - reproducible ansible runtime
applies_when:
  - Multiple people, laptops, CI workers, or automation controllers run the same Ansible project.
  - Playbooks depend on specific ansible-core, Python library, role, or collection versions.
  - A project needs predictable local and pipeline behavior.
avoid_when:
  - The playbook is a one-off experiment and dependency drift is acceptable.
  - A centrally managed execution environment already pins and publishes every runtime dependency.
related:
  - iac.reproducible-infrastructure
  - iac.pipeline-delivered-infrastructure
  - iac.ansible-collection-dependency-manifest
sources:
  - "book: Bas Meijer, Lorin Hochstein, and Rene Moser, Ansible: Up and Running, third edition; Chapters 2, 15, 22, and 23."
source_confidence: high
last_reviewed: 2026-06-05
---

# Ansible Control Node Dependency Isolation

## Intent

Make Ansible execution repeatable by treating the control-node runtime as project infrastructure: pinned, isolated, reviewable, and recreated the same way in local development, CI, and automation platforms.

## Use when

- Contributors install Ansible differently or share a system Python environment.
- Upgrading ansible-core, collections, or Python dependencies has caused unexpected playbook behavior.
- CI and developer machines need to run the same playbooks with the same module behavior.
- The project depends on cloud SDKs, Windows support libraries, network automation libraries, or custom modules.
- Automation Platform execution environments or containerized runners are being introduced.

## Avoid when

- A short-lived local lab does not need reproducibility.
- The organization already provides a locked execution image and forbids project-local runtime changes.
- Dependency isolation would hide required platform-level packages that operators must manage explicitly.

## Context and problem

Ansible runs from a control node, and the control node supplies ansible-core, Python, installed collections, cloud SDKs, SSH behavior, vault helpers, and plugin paths. If these dependencies are implicit, the same playbook can behave differently depending on who runs it or where it runs. Troubleshooting then shifts from infrastructure intent to local workstation archaeology.

The Ansible source emphasizes using isolated Python environments for project work, installed collections for content, dependency manifests for roles and collections, and execution environments for managed automation. The corpus should treat that as a delivery pattern rather than an installation detail.

## Forces

- Local convenience versus reproducible automation.
- Fast upgrades versus compatibility with existing playbooks and modules.
- Project autonomy versus centrally managed runner images.
- Small dependency files versus the need to capture Python libraries, Ansible collections, roles, and plugins.
- Developer environments versus Automation Controller execution environments.

## Guidance

Define the Ansible runtime alongside the project. Pin ansible-core and Python dependencies in a project-specific environment, express role and collection dependencies in manifests, and make the runner image or execution environment version visible. Keep the project runnable from a clean machine or clean CI worker without relying on a contributor's global Python packages.

When using Automation Platform, align local development with the execution environment that will run jobs. When using plain CI, install dependencies from checked-in manifests before linting, testing, or applying playbooks.

## Implementation moves

- Use a Python virtual environment, container image, or execution environment per project.
- Pin ansible-core and required Python libraries in `requirements.txt`, lockfiles, or image definitions.
- Put role dependencies in `requirements.yml` and collection dependencies in a collection manifest.
- Document the supported Ansible and Python versions in the project README or automation guide.
- Install dependencies in CI from the same files used locally.
- Version and publish automation execution environments when controller jobs use them.
- Make upgrade pull requests small enough to test dependency changes independently from playbook intent.

## Checks

- Can a new contributor recreate the control-node runtime from checked-in files?
- Does CI install the same Ansible, collection, role, and Python dependencies that developers use?
- Are cloud, Windows, network, and custom-module libraries explicit rather than assumed?
- Is the Automation Platform execution environment version traceable to source?
- Are dependency upgrades reviewed and tested as changes to automation behavior?

## Failure modes

- Installing Ansible globally and getting different module behavior on every machine.
- Pinning ansible-core but leaving cloud SDKs, collections, and roles floating.
- Running CI in one dependency set and production jobs in another.
- Treating Automation Platform execution environments as opaque infrastructure rather than versioned runtime artifacts.
- Upgrading collections and playbook logic in one large change that cannot be diagnosed.

## Agent trigger hints

Use this pattern when the user says or implies:

- install Ansible for this project
- Ansible works on my machine but not in CI
- pin ansible-core
- Python virtualenv for Ansible
- Ansible execution environment
- collection or Python dependency drift

## Source notes

Synthesized from Ansible: Up and Running, third edition, especially Chapter 2 on installation isolation, Chapter 15 on collections, Chapter 22 on CI/CD dependencies, and Chapter 23 on execution environments. No source excerpts are stored here.
