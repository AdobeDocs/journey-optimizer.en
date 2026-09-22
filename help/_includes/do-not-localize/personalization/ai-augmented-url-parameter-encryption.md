---
title: AI Knowledge Reference
---
# AI Knowledge Reference

+++ AI Knowledge Reference

This section contains structured knowledge intended to support interpretation, retrieval, and question answering related to this topic.

For complete understanding, this information should be combined with the documentation on this page. Neither source is intended to stand alone; the page describes the feature, while this section provides additional context that helps disambiguate terminology, intent, applicability, and constraints.

* **TL;DR:** This page explains how administrators create, rotate, and revoke encryption keys in Journey Optimizer's sandbox-level key registry, enabling marketers to encrypt sensitive URL query parameters so PII is not exposed in plain text in tracking links and landing pages.

**Intents:**

* Understand why URL parameter encryption is needed (sensitive data and PII visible in plain-text query strings)
* Create encryption keys in the sandbox key registry (admin task requiring specific permissions)
* Revoke a key to permanently disable it for new encryption
* Rotate a key to supply new cryptographic material while keeping the same identifier
* Use the `Encrypt` helper in the personalization editor to protect specific query parameter values

**Glossary:**

* **Key registry**: A sandbox-level repository in Journey Optimizer (Administration > Configurations) where administrators create and manage encryption keys used by the URL parameter encryption helper. *(product-specific)*
* **Encryption helper (`Encrypt`)**: A helper function in the personalization editor that encrypts an expression value at render time, replacing PII with ciphertext in URL query parameters. *(product-specific)*
* **Revoke (key)**: The act of permanently disabling a key for new encryption; the key entry remains visible in the registry for audit, and older payloads may still require it for decryption on the organization's systems.
* **Rotate (key)**: The act of supplying new cryptographic material for a key while keeping its identifier stable, so campaigns and journeys already referencing that key do not need to be updated.
* **PII (Personally Identifiable Information)**: Data that can identify an individual — such as profile attributes, tokens, or offer identifiers — which must be protected when included in URL query parameters.

**Guardrails:**

* URL parameter encryption is currently only available for the Email channel.
* Requires **View Key Registry** and **Manage Key Registry** permissions to access and manage keys.
* Decryption is the organization's responsibility. Journey Optimizer encrypts values at render time; the website, app, or API must decrypt parameters using the same cryptographic material and processes defined by the organization.
* Only active keys should be used to encrypt new values in the personalization editor; revoked keys must not be used for new content.
* Revoked keys remain visible in the registry for audit purposes; they may still be needed by the organization's systems to decrypt older payloads.

**Terminology:**

* **Canonical name:** URL parameter encryption — variants: URL encryption, query parameter encryption, URL parameter obfuscation
* **Synonyms:** "key registry" = "Key registry" (UI label in Administration > Configurations)
* **Do not confuse:** Revoke (permanently disables the key for new encryption; entry stays for audit) ≠ Rotate (replaces cryptographic material but keeps the same key identifier active for new encryption)

**FAQ:**

* **Q: Who is responsible for decryption?** — Decryption is the organization's responsibility. Journey Optimizer encrypts values when the message is rendered. The website, app, or API must decrypt query parameters using the same cryptographic material and processes the organization has defined.
* **Q: What is the difference between Revoke and Rotate?** — Revoke permanently disables a key for new encryption while keeping the entry visible in the registry for audit (older payloads may still need the key for decryption on the organization's systems). Rotate supplies new cryptographic material for a key while keeping the same key identifier, so campaigns and journeys referencing it continue to work without updates.
* **Q: What permissions are required to manage keys?** — **View Key Registry** and **Manage Key Registry** permissions.
* **Q: Which channels support URL parameter encryption?** — Currently only the Email channel.
* **Q: Can a revoked key be used for new encryption?** — No. Once a key is revoked, attempts to use it in the encryption helper should fail at render time. Do not use revoked keys for new content.

+++

<!-- ai-section-version: 1 | source-hash: c594ce24 -->
