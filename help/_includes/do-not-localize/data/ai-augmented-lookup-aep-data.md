---
title: AI Knowledge Reference
---
# AI Knowledge Reference

+++ AI Knowledge Reference

This section contains structured knowledge intended to support interpretation, retrieval, and question answering related to this topic.

For complete understanding, this information should be combined with the documentation on this page. Neither source is intended to stand alone; the page describes the feature, while this section provides additional context that helps disambiguate terminology, intent, applicability, and constraints.

* **TL;DR:** This page explains how to enable record-based Adobe Experience Platform datasets for the lookup service so their data can enrich personalization, Decisioning, and journey orchestration at runtime, including the entitlement guardrails.

**Intents:**

* Enable a record-based dataset for lookup using the dataset management toggle or the API.
* Meet the prerequisites (record-type schema, primary identity, non-person namespace).
* Review the lookup entitlement limits before designing a lookup strategy.
* Monitor lookup ingestion status.
* Use enabled data with personalization, Decisioning, and journey orchestration.

**Glossary:**

* **Lookup service**: the service that retrieves record-based dataset data at runtime for personalization, Decisioning, and journey orchestration *(product-specific)*
* **Lookup dataset**: a record-based dataset enabled for lookup *(product-specific)*
* **Primary identity (lookup key)**: the identity, required on the schema, that acts as the lookup key *(product-specific)*
* **Record-type schema**: the required schema type for lookup — a schema that is NOT of Profile or Event class
* **Edge activation region**: the region (for example, NLD2 or VA7) where the dataset's sandbox resides, for inbound edge-based activation *(product-specific)*

**Guardrails:**

* Enabled Lookup Datasets: maximum 10 per organization, combined across production and development sandboxes (default; if additional volumes are needed, contact your Adobe representative).
* Dataset Record Count: up to 2 million records per dataset, counted as the total across all batches (default; raisable by contacting your Adobe representative).
* Record Size: up to 2 KB per record (default maximum record size supported).
* Dataset Size: up to 4 GB per individual dataset; the record count and dataset size limits are independent guardrails and both must be satisfied (default; raisable by contacting your Adobe representative).
* Dataset Frequency Updates: up to 5 updates per day per dataset (default; raisable by contacting your Adobe representative).
* Datasets enabled for lookup should not contain any Personally Identifiable Information (PII).
* Datasets used in personalization are not protected from deletion; keep track of which datasets are in use.
* The schema must be record-type (NOT of Profile or Event class) and must have a primary identity defined; if a custom namespace is not defined, the identity must be a non-person identifier.
* Keep the lookup toggle on; repeatedly turning datasets on and off can lead to unexpected indexing behavior.
* Datasets enabled for lookup are available for inbound edge-based activation only in the region where the dataset's sandbox resides.
* Removing a batch of data completely removes all matching keys from the lookup service.
* The data lookup capability is in Limited Availability.

**Terminology:**

* Canonical name: lookup service — variants: data lookup, enable for lookup
* API ACTION values: `enable` OR `disable`
* Do not confuse: a "lookup dataset" (record-type, NOT Profile or Event, not stored on the profile) ≠ a profile or event dataset (Profile or Event class)
* Do not confuse: enabling a dataset for "lookup" ≠ enabling a dataset for "Profile"

**FAQ:**

* **Q: What schema type is required for a lookup dataset?** — A record-type schema that is NOT of Profile or Event class, with a primary identity defined that can act as the lookup key.
* **Q: How many datasets can I enable for lookup?** — Up to 10 per organization, combined across production and development sandboxes; contact your Adobe representative for more.
* **Q: What are the record and size limits?** — Up to 2 million records and 4 GB per dataset, up to 2 KB per record, and up to 5 updates per day per dataset; the record count and dataset size are independent guardrails that must both be satisfied.
* **Q: Can lookup datasets contain PII?** — No; datasets enabled for lookup should not contain any Personally Identifiable Information.
* **Q: What happens if I delete a batch of data?** — All matching keys in that batch are completely removed from the lookup service.
* **Q: Should I toggle lookup on and off frequently?** — No; repeatedly turning datasets on and off can lead to unexpected indexing behavior, so keep the toggle on while the dataset is in use.

+++

<!-- ai-section-version: 1 | source-hash: e76c9c89 -->
