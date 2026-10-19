---
title: AI Knowledge Reference
---
# AI Knowledge Reference

+++ AI Knowledge Reference

This section contains structured knowledge intended to support interpretation, retrieval, and question answering related to this topic.

For complete understanding, this information should be combined with the documentation on this page. Neither source is intended to stand alone; the page describes the feature, while this section provides additional context that helps disambiguate terminology, intent, applicability, and constraints.

* **TL;DR:** This page teaches how to use the `datasetLookup` helper function in the Journey Optimizer personalization editor to retrieve fields from Adobe Experience Platform record datasets and incorporate them into message personalization.

**Intents:**

* Enable an AEP record dataset for lookup personalization
* Add the `datasetLookup` helper function to a personalization expression
* Configure the function with a dataset ID, join key, result alias, and required flag
* Reference retrieved dataset fields in personalization expressions using the result alias
* Test personalized content using the Simulate content flow

**Glossary:**

* **datasetLookup**: A helper function in the personalization editor that retrieves field values from an AEP record dataset by joining on a specified key. *(product-specific)*
* **Record dataset**: An Adobe Experience Platform dataset type containing record-level data that can be enabled for lookup personalization. *(product-specific)*
* **Lookup personalization**: The process of fetching fields from an AEP record dataset at send time to personalize message content. *(product-specific)*
* **result parameter**: An arbitrary alias assigned in the `datasetLookup` call; used to reference all retrieved field values in subsequent expressions (e.g. `{{result.fieldId}}`).
* **required parameter**: A boolean flag in `datasetLookup` that controls whether message delivery requires a matching key to be found in the dataset.

**Guardrails:**

* Feature is in Limited Availability — not yet generally available to all customers.
* The `datasetLookup` helper function within expression fragments is available to a limited set of customers only; contact your Adobe representative to gain access.
* Datasets must be explicitly enabled for lookup personalization before they can be used with `datasetLookup`.
* Keep the number of fields retrieved per `datasetLookup` call under 50 to avoid impacting throughput (recommended limit — no hard limit is stated on the page).

**Terminology:**

* **Canonical name:** datasetLookup — variants: dataset lookup, dataset lookup helper, dataset lookup helper function
* **Synonyms:** "datasetLookup" = "dataset lookup helper function"
* **Do not confuse:** "datasetId" (identifier of the AEP dataset) ≠ "id" (the source column used to join with the dataset's primary identity) ≠ "result" (the alias for referencing retrieved field values)

**FAQ:**

* **Q: What is the `datasetLookup` helper function?** — It is a helper function in the personalization editor that retrieves field values from Adobe Experience Platform record datasets, allowing you to incorporate that data into message personalization.
* **Q: What happens if `required=false` and no matching key is found in the dataset?** — The message can still be delivered. It is recommended to account for fallback or default values in your message content when using `required=false`.
* **Q: What happens if `required=true` and no matching key is found?** — The message will only be delivered if a matching key is found in the dataset.
* **Q: Where do I find the dataset ID and field IDs needed for the syntax?** — Dataset IDs can be retrieved in the Adobe Experience Platform UI under Datasets. Field IDs are visible when previewing a dataset and browsing the record schema in the AEP UI.
* **Q: How do I test content that uses `datasetLookup`?** — Use the **Simulate content** button to test with sample input data or AI auto-generation, or select **Simulate content (AEP profiles)** from the dropdown to preview with test profiles.

+++

<!-- ai-section-version: 1 | source-hash: 89d99e47 -->
