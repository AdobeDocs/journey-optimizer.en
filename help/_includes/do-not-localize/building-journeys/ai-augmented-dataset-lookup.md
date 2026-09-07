---
title: AI Knowledge Reference
---
# AI Knowledge Reference

+++ AI Knowledge Reference

This section contains structured knowledge intended to support interpretation, retrieval, and question answering related to this topic.

For complete understanding, this information should be combined with the documentation on this page. Neither source is intended to stand alone; the page describes the feature, while this section provides additional context that helps disambiguate terminology, intent, applicability, and constraints.

* **TL;DR:** This page explains how to configure the Dataset lookup activity to dynamically retrieve AEP record dataset data at journey runtime for real-time personalization and conditional logic.

**Intents:**

* Add a Dataset lookup activity to a journey to fetch external AEP record data at runtime
* Select specific dataset fields (leaf nodes / primitive values) to retrieve during lookup
* Define a lookup key in advanced mode to join journey context with dataset records
* Use enriched dataset data in the journey expression editor or personalization editor
* Troubleshoot "Dataset lookup not found" errors caused by using simple mode for the lookup key

**Glossary:**

* **Dataset lookup activity**: A journey orchestration activity that retrieves data from AEP record datasets at runtime using a joining key *(product-specific)*
* **Leaf node**: A field at the lowest level of a schema hierarchy that holds a primitive value (string, number, boolean, date) *(product-specific)*
* **Lookup key**: The joining expression (string or list of strings) used to match journey context data against records in the selected dataset *(product-specific)*
* **Enriched data**: Data retrieved by a Dataset lookup activity and stored transiently in the journey context for use in downstream activities *(product-specific)*

**Guardrails:**

* Maximum of 10 Dataset lookup activities per journey.
* Maximum of 20 selected fields per lookup activity.
* Maximum of 50 keys in the lookup keys array.
* Enriched data size is limited to 10KB.
* The dataset must be enabled for lookup in Adobe Experience Platform before it appears in the activity configuration.
* Only leaf nodes (primitive values) can be selected; arrays and maps cannot be selected.
* Only strings or lists of strings are supported as lookup keys.
* The lookup key must be defined in advanced mode; using simple mode causes the activity output to be unavailable as a context attribute downstream.
* Enriched data is transient and available only during journey runtime and in outbound activity personalization.
* For best performance, limit to 5 lookup activities per journey (recommended); the hard limit enforced by the system is 10 activities per journey. Up to 20 attributes per lookup are also recommended.

**Terminology:**

* Canonical name: Dataset lookup activity — Acronym: n/a — variants: AEP data lookup, data enrichment activity
* Synonyms: "lookup key" = "joining key"
* Do not confuse: "Dataset lookup activity" ≠ "Experience event lookup" — dataset lookup retrieves record dataset data, not time-series experience events

**FAQ:**

* **Q: Why doesn't my dataset appear in the Dataset field dropdown?** — The dataset must be enabled for lookup in Adobe Experience Platform. Follow the instructions in the Must-read section to enable it.
* **Q: Why does `@datasetLookup{}` return a "Dataset lookup not found" error in a condition?** — The lookup key was defined using simple mode instead of advanced mode. Redefine it in advanced mode and republish the journey.
* **Q: Can I retrieve arrays or map fields from the dataset?** — No, only primitive leaf node fields (string, number, boolean, date) can be selected.
* **Q: How do I access enriched data in an email?** — Use the personalization editor with the syntax `{{context.journey.datasetLookup.<activityId>.entities}}`.
* **Q: Is enriched data persisted after the journey ends?** — No, enriched data is transient and only available during the journey runtime session.

+++
