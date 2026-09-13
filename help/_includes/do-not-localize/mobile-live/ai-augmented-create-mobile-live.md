---
title: AI Knowledge Reference
---
# AI Knowledge Reference

+++ AI Knowledge Reference

This section contains structured knowledge intended to support interpretation, retrieval, and question answering related to this topic.

For complete understanding, this information should be combined with the documentation on this page. Neither source is intended to stand alone; the page describes the feature, while this section provides additional context that helps disambiguate terminology, intent, applicability, and constraints.

* **TL;DR:** This page explains how to build an API-triggered campaign in Journey Optimizer to remotely start, update, and end Live activities for individual users or audiences, and how to attach custom data to a profile using the optional `executionMetadata` field.

**Intents:**

* Create an API-triggered campaign for Live activities, selecting API-triggered Marketing for audience-based campaigns or API-triggered Transactional for individual campaigns
* Choose Live activity in the Actions section and select or create a configuration
* Create a content experiment with treatments to measure performance
* Activate the campaign and use the provided cURL request to trigger start, update, or end events
* Attach custom data to a profile using the optional `executionMetadata` field for later retrieval from the Live activity feedback dataset

**Glossary:**

* **API-triggered Marketing**: The campaign type used for audience-based campaigns *(product-specific)*
* **API-triggered Transactional**: The campaign type used for individual campaigns *(product-specific)*
* **[!UICONTROL High Throughput]**: An option that should not be enabled for API-triggered Transactional Live activity campaigns *(product-specific)*
* **Live activity**: The action chosen in the Actions section, tied to a selected or newly created configuration *(product-specific)*
* **executionMetadata**: An optional field that attaches custom data to a profile, stored alongside the execution and retrievable from the Live activity feedback dataset *(product-specific)*
* **Live activity feedback dataset**: The dataset from which stored `executionMetadata` values can be retrieved to match delivery results to your own records *(product-specific)*
* **event**: The payload field whose values are `start`, `update`, or `end`

**Guardrails:**

* For API-triggered Transactional campaigns, the **[!UICONTROL High Throughput]** option should not be enabled.
* `executionMetadata` is only available for API-triggered Transactional campaigns.
* `executionMetadata` accepts only string keys and string values; convert any non-string value to a string before sending.
* `executionMetadata` does not support personalization expressions, so any `{{...}}` expression is treated as literal text rather than resolved.
* Each profile can carry up to 50 key/value pairs in `executionMetadata` (hard limit), with a combined size limit of 2 KB for all keys and values (hard limit). Metadata exceeding this limit is discarded, but the Live activity is still delivered.
* In the unitary payload example, most fields are mandatory; only `requestId`, `dismissal-date`, and `alert` are optional.

**Terminology:**

* Canonical name: Live activity — Acronym: n/a — variants: Live activities
* Synonyms: "Unitary use cases" = "individual campaigns (API-triggered Transactional)"
* Synonyms: "Broadcast use cases" = "audience-based campaigns (API-triggered Marketing)"
* Do not confuse: "API-triggered Marketing" (audience-based campaigns) ≠ "API-triggered Transactional" (individual campaigns)
* Do not confuse: "start" ≠ "update" ≠ "end" (the values of the `event` field)
* Do not confuse: "dismissal-date" (optional; auto-removes the activity when `event` is `end`) ≠ "timestamp" (current epoch time)

**FAQ:**

* **Q: Which campaign type do I use for Live activities?** — API-triggered Marketing for audience-based campaigns; API-triggered Transactional for individual campaigns.
* **Q: Should High Throughput be enabled for API-triggered Transactional?** — No; for API-triggered Transactional, the **[!UICONTROL High Throughput]** option should not be enabled.
* **Q: How do I trigger start, update, or end events after activation?** — Use the provided cURL request as a template, update the sample payload with your specific data, and copy the **[!UICONTROL Campaign ID]** into your payload.
* **Q: What is `executionMetadata` for?** — Attaching your own custom data, such as an order ID, loyalty tier, or region code, to a profile; it is stored alongside the execution and retrievable from the Live activity feedback dataset. It is only available for API-triggered Transactional campaigns.
* **Q: What are the `executionMetadata` limits?** — Up to 50 key/value pairs per profile with a combined 2 KB size limit; only string keys and values are accepted, and personalization expressions are not resolved. Metadata exceeding the limit is discarded, but the Live activity is still delivered.

+++

<!-- ai-section-version: 1 | source-hash: 9f4fc886 -->
