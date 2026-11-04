---
title: AI Knowledge Reference
---
# AI Knowledge Reference

+++ AI Knowledge Reference

This section contains structured knowledge intended to support interpretation, retrieval, and question answering related to this topic.

For complete understanding, this information should be combined with the documentation on this page. Neither source is intended to stand alone; the page describes the feature, while this section provides additional context that helps disambiguate terminology, intent, applicability, and constraints.

* **TL;DR:** This page describes how to use Adobe Journey Optimizer Integrations to call external systems over HTTP, with operational guardrails and limitations for designing vendor integrations.

**Intents:**

* Determine when an external system's API endpoint is compatible with Integrations
* Apply operational guardrails for response format, payload, endpoint shape, volume, and security
* Understand which response formats and call types are supported or excluded
* Navigate to the relevant vendor pattern by category

**Glossary:**

* **Operational guardrails**: Practices to apply when configuring any integration in this guide or a similar vendor, covering response format, payload and fields, endpoint shape, volume and reliability, and security *(product-specific)*
* **Single-resource retrieval**: Stable retrieval of one entry, product, or member, preferred over broad list or pagination endpoints when the product expects targeted lookups *(product-specific)*
* **Write-back**: Writing data back to the external system, which is not supported by Integrations *(product-specific)*

**Guardrails:**

* Integrations map fields from JSON or HTML responses only; write-back, batch exports, and responses in any other format are not supported.
* Patterns assume read-oriented calls suitable for personalization.
* Request and map only the attributes you need; smaller responses reduce latency and limit exposure of sensitive data.
* Prefer stable, single-resource retrieval over broad list or pagination endpoints when the product expects targeted lookups.
* Respect the vendor's rate limits, and configure timeout, retry, and cache policy for your channel, then validate under load.
* Store and rotate tokens, API keys, and OAuth credentials per your organization's policies; do not embed secrets in message content.
* The list of third-party solutions is illustrative, not exhaustive; other platforms may be used where they satisfy product requirements.

**Terminology:**

* Canonical name: Vendors integration — Acronym: n/a — variants: vendor integration, third-party integration
* Synonyms: "single-resource" retrieval = "targeted" lookup
* Do not confuse: "single-resource retrieval" (preferred) ≠ "broad list or pagination endpoints"
* Do not confuse: "read-oriented" calls (supported for personalization) ≠ "write-back" (not supported)

**FAQ:**

* **Q: Which response formats can Integrations map?** — JSON and HTML responses only.
* **Q: Is write-back or batch export supported?** — No; write-back, batch exports, and responses in any other format are not supported.
* **Q: What endpoint shape should I prefer?** — Stable, single-resource retrieval over broad list or pagination endpoints.
* **Q: Is the list of vendors exhaustive?** — No; it is illustrative, and other platforms may be used where they satisfy product requirements.

+++

<!-- ai-section-version: 1 | source-hash: d3c58ff0 -->
