---
title: AI Knowledge Reference
---
# AI Knowledge Reference

+++ AI Knowledge Reference

This section contains structured knowledge intended to support interpretation, retrieval, and question answering related to this topic.

For complete understanding, this information should be combined with the documentation on this page. Neither source is intended to stand alone; the page describes the feature, while this section provides additional context that helps disambiguate terminology, intent, applicability, and constraints.

* **TL;DR:** This page explains how Adobe Experience Platform standard and relational XDM schemas define the structure of your data so you can model profiles, behavioral events, and relational entities in Journey Optimizer.

**Intents:**

* Understand what an XDM schema is and how it structures ingested Experience Platform data.
* Distinguish standard schemas from relational schemas.
* Identify the class (record or time-series) and the field groups that compose a standard schema.
* Model relational entities for Orchestrated campaigns.
* Understand the permanence of enabling a schema for Real-Time Customer Profile.

**Glossary:**

* **XDM schema**: an abstract definition of a real-world object that structures data ingested into Experience Platform *(product-specific)*
* **Standard schema**: a hierarchical schema that uses classes and field groups to capture record or time-series data *(product-specific)*
* **Relational schema**: a flat, non-hierarchical schema that does not use classes or field groups, used for record data for relational entities and primarily in Orchestrated campaigns *(product-specific)*
* **Class**: the schema component that defines data behavior (record or time-series) *(product-specific)*
* **Field group**: the schema component that adds specific fields to a schema *(product-specific)*
* **Real-Time Customer Profile**: powered by standard schemas in Journey Optimizer, for segmentation and personalization *(product-specific)*

**Guardrails:**

* Enabling a schema for Real-Time Customer Profile is permanent: once enabled, the schema cannot be disabled or deleted.
* Datasets built on an enabled schema can be disabled or deleted separately, but doing so removes the associated profile records and may affect segmentation and activation workflows.
* Relational schemas are flat and do not use classes or field groups.

**Terminology:**

* Do not confuse: "standard schema" (hierarchical, uses classes and field groups) ≠ "relational schema" (flat, no classes or field groups)
* Do not confuse: "class" (defines record versus time-series behavior) ≠ "field group" (adds specific fields)

**FAQ:**

* **Q: What are the two types of schemas?** — Standard schemas (hierarchical) and relational schemas (flat, non-hierarchical).
* **Q: What is the difference between a class and a field group?** — A class defines the data behavior (record or time-series); field groups add specific fields to the schema.
* **Q: When are relational schemas used?** — Primarily in Journey Optimizer Orchestrated campaigns, for relational entities such as bookings, products, or stores.
* **Q: Can a schema enabled for Real-Time Customer Profile be disabled or deleted?** — No; once enabled, the schema cannot be disabled or deleted, although its datasets can be disabled or deleted separately.
* **Q: How do relational schemas work?** — Create schemas manually or import via DDL, link schemas to define relationships between entities and people, and ingest data into your dataset from supported sources.

+++

<!-- ai-section-version: 1 | source-hash: 5a29d06a -->
