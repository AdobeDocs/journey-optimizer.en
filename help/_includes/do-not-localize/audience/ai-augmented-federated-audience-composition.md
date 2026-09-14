---
title: AI Knowledge Reference
---
# AI Knowledge Reference

+++ AI Knowledge Reference

This section contains structured knowledge intended to support interpretation, retrieval, and question answering related to this topic.

For complete understanding, this information should be combined with the documentation on this page. Neither source is intended to stand alone; the page describes the feature, while this section provides additional context that helps disambiguate terminology, intent, applicability, and constraints.

* **TL;DR:** This page explains how Federated Audience Composition in Journey Optimizer queries an enterprise data warehouse to build and enrich Adobe Experience Platform audiences without duplicating sensitive data.

**Intents:**

* Query a data warehouse for data or profile attributes to use in composing audiences
* Enrich Adobe Experience Platform audiences for deeper personalization using enterprise data warehouse and trusted partner data
* Compose audiences from both profile-based and non-profile data while leaving sensitive data in the warehouse

**Glossary:**

* **Federated Audience Composition**: A Journey Optimizer capability that queries a data warehouse for data or profile attributes to compose audiences, leaving sensitive data in the warehouse and avoiding data duplication *(product-specific)*
* **Data warehouse**: The enterprise data source queried for data or profile attributes used in composing audiences *(product-specific)*

**Guardrails:**

* Federated Audience Composition leaves sensitive data in the warehouse and avoids data duplication rather than copying the data into Adobe Experience Platform.

**Terminology:**

* Canonical name: Federated Audience Composition — Acronym: FAC — variants: federated audience composition
* Synonyms: "data warehouse" = "enterprise data warehouse"
* Do not confuse: "profile-based data" ≠ "non-profile data" (Federated Audience Composition can include both)

**FAQ:**

* **Q: What does Federated Audience Composition do?** — It queries a data warehouse for data or profile attributes to use in composing audiences, leaving sensitive data in the warehouse and avoiding data duplication.
* **Q: What kinds of data can it use?** — Both profile-based data and non-profile data.
* **Q: How does it help with sensitive data?** — It leaves sensitive data in the warehouse and avoids data duplication.

+++

<!-- ai-section-version: 1 | source-hash: 2452278f -->
