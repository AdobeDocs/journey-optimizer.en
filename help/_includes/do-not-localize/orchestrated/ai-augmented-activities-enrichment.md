---
title: AI Knowledge Reference
---
# AI Knowledge Reference

+++ AI Knowledge Reference

This section contains structured knowledge intended to support interpretation, retrieval, and question answering related to this topic.

For complete understanding, this information should be combined with the documentation on this page. Neither source is intended to stand alone; the page describes the feature, while this section provides additional context that helps disambiguate terminology, intent, applicability, and constraints.

* **TL;DR:** This page explains how to configure the Enrichment targeting activity in an Orchestrated campaign to enhance audience data with additional attributes using a single enrichment attribute or a collection link, including links between tables and the use of collection data in message personalization.

**Intents:**

* Add an Enrichment activity to an Orchestrated campaign and select enrichment data.
* Create a link between the working table data and Adobe Journey Optimizer, choosing a relation type, a target, and join conditions.
* Enrich an audience with a single enrichment attribute from the current targeting dimension.
* Enrich an audience with data from a collection link, including collecting multiple records, aggregating data, and filtering records.
* Use enrichment collection data in message personalization.

**Glossary:**

* **Enrichment activity**: a Targeting activity that lets you enhance your audience data with additional attributes *(product-specific)*
* **Single enrichment attribute**: a single attribute, such as date of birth, selected from the current targeting dimension to enrich the audience *(product-specific)*
* **Collection link**: a link used to enrich an audience with data from a linked table, with 1-N cardinality *(product-specific)*
* **Link definition**: the section used to define a relationship between the working table and another data source *(product-specific)*
* **1 cardinality simple link**: a relation type where each record in the primary set maps to exactly one record in the linked data *(product-specific)*
* **0 or 1 cardinality simple link**: a relation type where each record in the primary set maps to zero or one record in the linked data *(product-specific)*
* **N cardinality collection link**: a relation type where each record in the primary set can map to multiple records in the linked data *(product-specific)*
* **Simple join**: a join condition that matches records on a specific attribute pair *(product-specific)*
* **Advanced join**: a join condition that builds custom matching logic using the rule builder *(product-specific)*

**Terminology:**

* Canonical name: Enrichment activity — variants: Enrichment
* Do not confuse: "1 cardinality simple link" (each record maps to exactly one record) ≠ "0 or 1 cardinality simple link" (each record maps to zero or one record) ≠ "N cardinality collection link" (each record can map to multiple records)
* Do not confuse: "Simple join" (matches records on a specific attribute pair) ≠ "Advanced join" (custom matching logic using the rule builder)

**FAQ:**

* **Q: What two types of enrichment data can be selected in the Enrichment activity?** — A single enrichment attribute from the target dimension, or a collection link.
* **Q: What are the three relation types available when creating a link?** — 1 cardinality simple link, 0 or 1 cardinality simple link, and N cardinality collection link.
* **Q: What are the two ways to define join conditions between the primary set and the linked schema?** — Simple join (matching on a specific attribute pair) or Advanced join (using the rule builder).
* **Q: Where can I use enrichment attributes collected through a collection link in a message?** — Under Target attributes > Enrichment in the message editor.

**Related pages:**

* For using enrichment collection data in message personalization: Learn how to use enrichment collection data in personalization (orchestrated/add-personalization.md)

**Personas:**

* **marketer:** Can add an Enrichment activity to enhance audience data with additional attributes. Can select a single enrichment attribute from the target dimension, or a collection link. Can add a link to connect working table data with Adobe Journey Optimizer for personalization or targeting. Where: "Add an Enrichment activity".

**Onboarding:**

* **Level:** Intermediate
* **First minimal step:** Add an Enrichment activity.
* **Success check:** The enrichment data can be used in activities added after the Enrichment activity.
* **Next:** Use enrichment collection data in message personalization: Add personalization in Orchestrated campaigns (orchestrated/add-personalization.md)

+++

<!-- ai-section-version: 1 | source-hash: 5db87521 -->
