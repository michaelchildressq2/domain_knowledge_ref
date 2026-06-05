---
id: iac.ansible-vault-secret-boundary
title: Ansible Vault Secret Boundary
type: security-pattern
status: draft
summary: Keep Ansible secrets separate from ordinary inventory and encrypt or externally source them so credentials stay reviewable, scoped, and usable in automation.
tags:
  - infrastructure-as-code
  - ansible
  - secrets-management
  - ansible-vault
  - least-privilege
  - configuration-management
  - security
aliases:
  - ansible-vault
  - vault IDs
  - encrypt Ansible secrets
  - Ansible secret files
applies_when:
  - Playbooks need passwords, tokens, certificates, private keys, or other sensitive variables.
  - Secrets must be stored with Ansible content for local or CI execution.
  - Different environments or teams need different secret access levels.
avoid_when:
  - A managed secret store can supply short-lived credentials directly to the runner.
  - The data is not sensitive and encrypting it would only reduce reviewability.
related:
  - iac.secrets-out-of-source
  - iac.externalized-configuration
  - iac.ansible-variable-precedence-contract
sources:
  - "book: Bas Meijer, Lorin Hochstein, and Rene Moser, Ansible: Up and Running, third edition; Chapters 7, 10, 22, 23, and 24."
source_confidence: high
last_reviewed: 2026-06-05
---

# Ansible Vault Secret Boundary

## Intent

Prevent credentials from leaking through inventory, logs, repositories, and job definitions by giving Ansible secrets an explicit storage, encryption, access, and runtime injection boundary.

## Use when

- Ansible needs database credentials, administrator passwords, API tokens, vault variables, SSH keys, or cloud credentials.
- Secrets differ by environment or access tier.
- CI or Automation Controller must run playbooks without an operator typing passwords interactively.
- Sensitive variables need to remain close enough to playbooks for templates and tasks to consume them.

## Avoid when

- A cloud secret manager, enterprise vault, or controller credential type can provide the value without storing encrypted blobs in Git.
- The team cannot protect vault passwords or vault ID files.
- The encrypted file would be so large that reviewers cannot understand the nonsecret configuration around it.

## Context and problem

Ansible makes it easy to put variables next to inventory, but plain inventory is a poor place for passwords and tokens. Once a secret is committed unencrypted, it tends to spread through forks, logs, job templates, and backups. Encrypting everything is also harmful because it makes normal configuration impossible to review.

The Ansible source shows a middle path: keep ordinary variables and sensitive variables separate, encrypt sensitive files with Ansible Vault when Git storage is needed, use vault IDs to separate environments or access levels, and use automation-friendly vault password mechanisms carefully.

## Forces

- Reviewable configuration versus confidential values.
- Local playbook execution versus centralized secret management.
- One shared vault password versus environment-specific vault IDs.
- Automation convenience versus exposure of vault password files.
- Debug output versus accidental secret disclosure.

## Guidance

Separate secrets from ordinary variables before encrypting. Put nonsecret defaults and environment values in reviewable files, and put only sensitive values in vault files or external secret lookups. Use vault IDs when access should differ by environment, team, or sensitivity level. In automation, inject vault passwords through controlled CI secrets, controller credential types, or executable helpers with least privilege.

Design tasks and logs so secrets do not appear in output. Use `no_log` for sensitive operations, but do not rely on output masking as the only boundary.

## Implementation moves

- Split `vars.yml` and encrypted vault files under the same inventory scope when both are needed.
- Use Ansible Vault for secrets that must live in the repository.
- Use vault IDs for dev, staging, production, or access-tier separation.
- Store vault password material outside the repository and inject it into CI or controller jobs securely.
- Prefer external secret lookups for high-rotation or centrally governed credentials.
- Mark tasks that handle secret values with `no_log` where output could expose them.
- Rotate leaked secrets and vault passwords as incident response, not as a normal workflow.

## Checks

- Are passwords, tokens, and private keys absent from plain inventory and logs?
- Can reviewers inspect nonsecret configuration without decrypting secret files?
- Are vault IDs aligned with actual access boundaries?
- Is vault password material protected outside Git?
- Does CI or Automation Controller obtain secrets through a scoped mechanism?
- Are sensitive task outputs suppressed without hiding unrelated troubleshooting information?

## Failure modes

- Committing credentials in inventory because encryption feels inconvenient.
- Encrypting entire configuration files and making ordinary changes unreviewable.
- Sharing one vault password across all environments and teams.
- Storing vault password files beside the encrypted content.
- Masking logs but still passing secrets through broad environment variables or command arguments.

## Agent trigger hints

Use this pattern when the user says or implies:

- ansible-vault
- encrypt Ansible secrets
- vault IDs
- passwords in inventory
- Ansible secret management
- no_log for secrets

## Source notes

Synthesized from Ansible: Up and Running, third edition, especially Chapter 7 on deployment credentials, Chapter 10 on `ansible-vault`, Chapter 22 on CI secret handling, Chapter 23 on controller credentials, and Chapter 24 on security best practices. No source excerpts are stored here.
