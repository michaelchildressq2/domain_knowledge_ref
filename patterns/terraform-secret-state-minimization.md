---
id: iac.terraform-secret-state-minimization
title: Terraform Secret State Minimization
type: security-pattern
status: draft
summary: Keep secrets out of Terraform source while also minimizing secret exposure through variables, state, plan files, logs, provider credentials, and remote-state outputs.
tags:
  - infrastructure-as-code
  - terraform
  - secrets-management
  - state-management
  - plan-files
  - oidc
  - security
aliases:
  - Terraform secrets
  - secrets in tfstate
  - terraform sensitive variables
  - terraform plan secrets
  - OIDC for Terraform
  - provider credentials
applies_when:
  - Terraform needs provider credentials, database passwords, API keys, certificates, or secret values for managed resources.
  - A team already avoids plaintext source secrets but has not assessed state, plan, log, and output leakage.
avoid_when:
  - The value is non-sensitive configuration that should be visible in code review.
  - A separate system creates and injects the secret without Terraform ever seeing its value.
related:
  - iac.secrets-out-of-source
  - iac.terraform-remote-state-backend
  - iac.policy-as-code-guardrails
  - iac.stack-parameter-registry
sources:
  - "book: Yevgeniy Brikman, Terraform: Up & Running, third edition; Chapter 6, Managing Secrets with Terraform."
source_confidence: high
last_reviewed: 2026-06-05
---

# Terraform Secret State Minimization

## Intent

Reduce the number of places Terraform can expose secrets while preserving automated, repeatable infrastructure delivery.

## Use when

- Terraform authenticates to cloud providers, Kubernetes, SaaS providers, databases, or secret stores.
- Terraform resources or data sources need secret input values.
- Plans, state files, logs, or remote-state outputs might be stored outside the immediate apply process.
- CI/CD uses long-lived access keys, service principals, or machine users.
- Teams need rotation, audit, and least-privilege access for Terraform automation.

## Avoid when

- Terraform does not need the secret value and can instead reference an existing secret by name, ARN, URI, or identity.
- Passing the secret through Terraform would copy it into state unnecessarily.
- The delivery platform already injects short-lived credentials directly into provider SDKs without exposing them to Terraform configuration.
- The team cannot protect the chosen remote backend and plan artifact storage.

## Context and problem

Keeping secrets out of `.tf` files is necessary but incomplete. Terraform can still receive secrets through variables, environment variables, data sources, provider configuration, generated plans, logs, and state. Marking a value as sensitive can reduce display in CLI output, but it does not mean the value disappears from state or every artifact.

Terraform secret management is therefore a data-flow problem. The team must know where each secret enters, where it is stored, who can read it, how long it lives, and how it rotates.

## Forces

- Automation needs credentials, but long-lived credentials create persistent blast radius.
- Secret references are safer than secret values, but some resources require the value at creation time.
- Sensitive flags improve display hygiene, but state and plan storage still need protection.
- Environment variables avoid source commits, but they can leak through process, logs, or CI settings.
- Remote state enables collaboration, but it centralizes sensitive infrastructure metadata.

## Guidance

Prefer designs where Terraform references secrets or identities rather than handling raw values. For provider authentication, favor short-lived credentials, role assumption, workload identity, or OIDC-based federation over static keys where the platform supports it. When Terraform must handle a secret value, treat state, plan files, logs, and outputs as sensitive artifacts.

Do not publish secret values through outputs or remote-state contracts unless there is no safer integration path. Protect plan files with the same care as state files, because saved plans can include values that are not visible in normal command output.

## Implementation moves

- Classify Terraform secrets by source: human credential, machine credential, customer secret, generated password, certificate, or API token.
- Use provider-native identity mechanisms and short-lived credentials for Terraform runners.
- Pass user-supplied secrets through secure CI variables or secret managers, not source files.
- Mark sensitive variables and outputs, but do not rely on that as the only control.
- Avoid outputting secret values for downstream stacks; output secret identifiers instead.
- Encrypt and access-control state backends and saved plan artifacts.
- Scan logs, plans, and state access paths during pipeline design.
- Rotate credentials and verify Terraform does not retain obsolete values in old state versions longer than policy allows.

## Checks

- Does Terraform need the secret value, or only a reference to a secret object?
- Where can the secret appear after `plan` and `apply` complete?
- Can someone with state read access retrieve sensitive values?
- Are saved plans stored, encrypted, expired, and access controlled?
- Are provider credentials short-lived and scoped to the target stack?
- Do outputs and remote-state consumers expose secret values accidentally?

## Failure modes

- Assuming `sensitive = true` removes values from state.
- Passing secrets through Terraform outputs because it is convenient for another stack.
- Saving plan files as ordinary CI artifacts.
- Using one static machine credential across all environments.
- Protecting source code while leaving state buckets, logs, or old object versions broadly readable.

## Agent trigger hints

Use this pattern when the user says or implies:

- Terraform secrets
- secrets in tfstate
- sensitive variables
- Terraform plan file security
- provider credentials in CI
- OIDC Terraform
- pass secrets to Terraform
- remote state exposes secrets

## Source notes

Synthesized from Chapter 6 of Terraform: Up & Running, third edition, including secret types, storage and access interfaces, provider authentication, resource/data-source secrets, state files, and plan files. No source excerpts are stored here.
