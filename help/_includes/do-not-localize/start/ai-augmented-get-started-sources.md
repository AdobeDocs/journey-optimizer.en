---
title: AI Knowledge Reference
---
# AI Knowledge Reference

+++ AI Knowledge Reference

This section contains structured knowledge intended to support interpretation, retrieval, and question answering related to this topic.

For complete understanding, this information should be combined with the documentation on this page. Neither source is intended to stand alone; the page describes the feature, while this section provides additional context that helps disambiguate terminology, intent, applicability, and constraints.

* **TL;DR:** This page explains what source connectors are, why they matter, the common source types, and how sources bring external data from CRM, cloud storage, and databases into Journey Optimizer for personalized journeys.

**Intents:**

* Understand what a source is and how it brings external data into Journey Optimizer
* Identify the common source types available for Adobe applications, cloud storage, databases, CRM and marketing automation, and loyalty and rewards
* Confirm the prerequisites needed before configuring sources
* Understand the basic sources workflow from connection through monitoring
* Configure file-based Change Data Capture sources for Orchestrated campaigns correctly

**Glossary:**

* **Source**: A connector that brings external data into Adobe Journey Optimizer from systems such as CRM platforms, cloud storage, or databases *(product-specific)*
* **Sources framework**: The Adobe Experience Platform framework that Journey Optimizer uses to power sources *(product-specific)*
* **`_change_request_type`**: A field required for file-based Change Data Capture sources used with Orchestrated campaigns, indicating the change operation *(product-specific)*

**Guardrails:**

* Before configuring sources, you need appropriate permissions to manage sources in Adobe Experience Platform, source system credentials, and an understanding of which data fields you need and how they map to Journey Optimizer profiles.
* For file-based Change Data Capture sources used with Orchestrated campaigns, the `_change_request_type` field is required, and its supported values must be lowercase `u` (upsert) or `d` (delete), not uppercase `U` and `D`.
* Once configured, sources run automatically in the background to keep customer data fresh.

**Terminology:**

* Canonical name: Source — variants: source connector, sources
* Synonyms: "source" = "source connector"
* Do not confuse: "`u` (upsert)" ≠ "`d` (delete)" — both must be lowercase

**FAQ:**

* **Q: What is a source in Journey Optimizer?** — A connector that brings external data from systems such as CRM platforms, cloud storage, or databases into Journey Optimizer and makes that data available for personalized journeys.
* **Q: Do I have to import data manually?** — No; once configured, sources sync data automatically in the background so customer information stays current.
* **Q: What do I need before I configure a source?** — Appropriate permissions to manage sources in Adobe Experience Platform, source system credentials, and an understanding of your data fields and how they map to profiles.
* **Q: What values does the `_change_request_type` field accept for Orchestrated campaign Change Data Capture sources?** — Lowercase `u` for upsert or `d` for delete; uppercase `U` and `D` are not supported.

+++

<!-- ai-section-version: 1 | source-hash: 4f1d4bfa -->
