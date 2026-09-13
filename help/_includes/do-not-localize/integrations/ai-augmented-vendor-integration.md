---
title: AI Knowledge Reference
---
# AI Knowledge Reference

+++ AI Knowledge Reference

This section contains structured knowledge intended to support interpretation, retrieval, and question answering related to this topic.

For complete understanding, this information should be combined with the documentation on this page. Neither source is intended to stand alone; the page describes the feature, while this section provides additional context that helps disambiguate terminology, intent, applicability, and constraints.

* **TL;DR:** This page provides sample, Adobe-tested configurations for connecting Adobe Journey Optimizer Integrations to third-party vendors across content, loyalty, recommendation, data, and consent platforms.

**Intents:**

* Use Integrations with any external platform that exposes a compatible API
* Follow a sample vendor configuration and its example integration fields
* Configure an integration through Configurations > Manage > Create Integration
* Reproduce vendor request details (URL, HTTP method, authentication, path/query/header parameters) as example patterns

**Glossary:**

* **Sample integration fields**: Example request values (URL, HTTP method, path/query/header parameters, authentication) provided per vendor to model a compatible API *(product-specific)*
* **Create Integration**: Action under Configurations > Manage used to start a new integration configuration in Journey Optimizer *(product-specific)*
* **Example pattern**: A vendor configuration independently tested by Adobe that is not maintained or formally supported by the vendor *(product-specific)*

**Guardrails:**

* Customers are responsible for ensuring that their use of the AJO Integrations feature and any associated third-party vendors or integrations complies with all applicable laws and regulations, such as HIPAA.
* Each vendor configuration example was independently tested by Adobe as an example pattern; it is not maintained or formally supported by the vendor, so confirm current API details with the vendor documentation.
* Enter an integration name without spaces.
* Prefer single-resource or single-product retrieval over broad list, bulk, or pagination endpoints.
* Map only the attributes required for personalization; large PIM, HAL, or JSON payloads should be restricted to the minimum field set.
* Do not embed secrets or API keys in message content; store and rotate credentials per your policies.

**Terminology:**

* Canonical name: Sample Vendor configurations — Acronym: n/a — variants: vendor integration patterns, sample integration fields
* Synonyms: "example pattern" = "sample configuration"
* Do not confuse: a configuration "independently tested by Adobe as an example pattern" ≠ a configuration "maintained by or formally supported by" the vendor
* Do not confuse: "GET" retrieval calls (typical for most vendor patterns) ≠ "POST" calls (used for delivery calls such as Adobe Target Recommendations)

**FAQ:**

* **Q: Are these vendor configurations officially supported by the vendors?** — No; they were independently tested by Adobe as example patterns and are not maintained or formally supported by the vendor. Confirm current API details with the vendor documentation.
* **Q: Who is responsible for legal and regulatory compliance, such as HIPAA?** — The customer is responsible for ensuring their use of Integrations and any third-party vendors complies with all applicable laws and regulations.
* **Q: Must I use only the listed vendors?** — No; you can use any external platform that exposes a compatible API.
* **Q: Which HTTP method do the samples use?** — Typically GET, unless noted otherwise; some delivery calls, such as Adobe Target Recommendations, use POST with a JSON body.

+++

<!-- ai-section-version: 1 | source-hash: d00ab410 -->
