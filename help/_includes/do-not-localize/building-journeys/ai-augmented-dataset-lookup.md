---
title: AI Knowledge Reference
---
# AI Knowledge Reference

+++ AI Knowledge Reference

This section contains structured knowledge intended to support interpretation, retrieval, and question answering related to this topic.

For complete understanding, this information should be combined with the documentation on this page. Neither source is intended to stand alone; the page describes the feature, while this section provides additional context that helps disambiguate terminology, intent, applicability, and constraints.

* **TL;DR:** This page explains how to configure the Dataset lookup activity to dynamically retrieve data from Adobe Experience Platform record datasets at journey runtime for real-time personalization and conditional logic.

**Intents:**

* Add a Dataset lookup activity to a journey to fetch external Adobe Experience Platform record data at runtime
* Select specific dataset fields (leaf nodes / primitive values) to retrieve during lookup
* Define a lookup key in advanced mode to join journey context with dataset records
* Use enriched dataset data in the journey expression editor or personalization editor
* Troubleshoot "Dataset lookup not found" errors caused by using simple mode for the lookup key

**Glossary:**

* **Dataset lookup activity**: A journey orchestration activity that retrieves selected data from Adobe Experience Platform record datasets at runtime by matching a lookup key from the journey context to dataset records *(product-specific)*
* **Leaf node**: A field at the lowest level of a schema hierarchy that holds a primitive value (string, number, boolean, date) *(product-specific)*
* **Lookup key**: The joining expression (string or list of strings) used to match journey context data against records in the selected dataset *(product-specific)*
* **Enriched data**: Data retrieved by a Dataset lookup activity and stored transiently in the journey context for use in downstream activities *(product-specific)*

**Guardrails:**

* Maximum of 10 Dataset lookup activities per journey (hard limit).
* Maximum of 20 selected fields (hard limit).
* Maximum of 50 keys in the lookup keys array (hard limit).
* Enriched data size is limited to 10KB (hard limit).
* The dataset must be enabled for lookup in Adobe Experience Platform before it appears in the activity configuration.
* Only leaf nodes (primitive values) can be selected; arrays and maps cannot be selected.
* Only strings or lists of strings are supported as lookup keys.
* The lookup key must be defined in advanced mode; using simple mode causes the activity output to be unavailable as a context attribute downstream.
* Enriched data is transient and available only during journey runtime and in outbound activity personalization.
* To avoid delays in deliverability, up to 5 lookup activities per journey are recommended. Up to 20 attributes per lookup are also recommended.

**Terminology:**

* Canonical name: Dataset lookup activity
* Synonyms: "lookup key" = "joining key"

**FAQ:**

* **Q: Why does my dataset not appear in the Dataset field dropdown?** — The dataset must be enabled for lookup in Adobe Experience Platform. See the linked "Use Adobe Experience Platform data" section for details.
* **Q: What should I check if lookup output is unavailable in a condition?** — Confirm that the lookup key was defined in advanced mode and that the Dataset lookup activity was saved. In the condition's separate expression editor, switch to advanced mode and reference the lookup output. If the key was defined using simple mode, redefine it in advanced mode and republish the journey.
* **Q: Can I retrieve arrays or map fields from the dataset?** — No, only primitive leaf node fields (string, number, boolean, date) can be selected.
* **Q: How do I access enriched data in an email?** — Use the personalization editor with the syntax `{{context.journey.datasetLookup.1482319411.entities}}`.
* **Q: Is enriched data available after the journey runtime?** — No, enriched data is transient and available only during journey runtime and in the personalization of outbound activities.

+++

<!-- ai-section-version: 1 | source-hash: 2bf5feee -->
