---
title: AI Knowledge Reference
---
# AI Knowledge Reference

+++ AI Knowledge Reference

This section contains structured knowledge intended to support interpretation, retrieval, and question answering related to this topic.

For complete understanding, this information should be combined with the documentation on this page. Neither source is intended to stand alone; the page describes the feature, while this section provides additional context that helps disambiguate terminology, intent, applicability, and constraints.

* **TL;DR:** This page explains how to access, create, and govern Adobe Experience Platform datasets in Journey Optimizer, including system-generated datasets and enabling a dataset for Real-Time Customer Profile.

**Intents:**

* Access and preview datasets in the Datasets workspace.
* Reveal and identify Journey Optimizer system-generated datasets.
* Create a dataset from a schema or from a CSV file.
* Enable a dataset for Real-Time Customer Profile.
* Review data governance labels at the dataset and field level.

**Glossary:**

* **Dataset**: a storage and management construct for a collection of data, typically a table, that contains a schema (columns) and fields (rows) *(product-specific)*
* **Data Lake**: where all data ingested into Adobe Experience Platform is persisted as datasets
* **System dataset (system-generated dataset)**: a dataset created automatically by Journey Optimizer for reporting, consent, message export, intelligent services, and inbound activity *(product-specific)*
* **Show system datasets**: toggle in the Datasets workspace filter that reveals system datasets, which are hidden by default *(product-specific)*
* **Enable for Profile**: enabling a dataset to contribute to Real-Time Customer Profile *(product-specific)*
* **Data Governance**: dataset and field-level labels that categorize data according to applicable usage policies

**Guardrails:**

* System datasets must not be modified; any change is automatically reverted with every product update.
* Enabling the schema underlying a dataset for Profile is permanent: once enabled, the schema cannot be disabled or deleted (hard constraint). Only the dataset itself can be disabled or deleted separately.
* Disabling or deleting a Profile-enabled dataset removes the associated profile records and may disrupt segmentation and activation workflows.
* As of November 1, 2024, streaming segmentation no longer supports send and open events from Journey Optimizer tracking and feedback datasets; use Business Rules for frequency capping or fatigue management instead.
* As of February 2025, a time-to-live (TTL) guardrail is being rolled out to Journey Optimizer system-generated datasets.
* The AJO Message Export Dataset retains records for 7 calendar days from ingestion and is available only to organizations that purchased the Message Export add-on.
* The Message Feedback Event Dataset uses batch ingestion; expect a data latency of up to 2 hours (expected latency, batch ingestion).
* When a dataset is empty, the Preview dataset link is deactivated.

**Terminology:**

* Do not confuse: "profile dataset" (Profile-enabled, contributing to Real-Time Customer Profile) ≠ "event dataset" (behavioral data for journeys and analysis) ≠ "system dataset" (auto-created for tracking, feedback, and journey step events)
* Do not confuse: disabling or deleting a "dataset" (possible independently) ≠ disabling the underlying "schema" for Profile (permanent, cannot be reversed)

**FAQ:**

* **Q: How do I see system-generated datasets?** — Enable the Show system datasets toggle in the Datasets workspace filter, on the Browse tab.
* **Q: Can I edit a system dataset?** — No; any change is automatically reverted with every product update.
* **Q: Is enabling a dataset for Profile reversible?** — The schema enablement is permanent and cannot be reversed; the dataset can be disabled or deleted separately, but doing so removes the associated profile records.
* **Q: How do I create a dataset?** — From an existing schema or by mapping a CSV file to an XDM schema.
* **Q: Why is the Preview dataset link deactivated?** — The dataset is empty; preview shows the most recent successful batch.

+++

<!-- ai-section-version: 1 | source-hash: 156bba9b -->
