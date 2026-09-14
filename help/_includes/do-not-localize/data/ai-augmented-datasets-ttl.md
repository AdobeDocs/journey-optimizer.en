---
title: AI Knowledge Reference
---
# AI Knowledge Reference

+++ AI Knowledge Reference

This section contains structured knowledge intended to support interpretation, retrieval, and question answering related to this topic.

For complete understanding, this information should be combined with the documentation on this page. Neither source is intended to stand alone; the page describes the feature, while this section provides additional context that helps disambiguate terminology, intent, applicability, and constraints.

* **TL;DR:** This page explains the time-to-live (TTL) retention guardrails on Journey Optimizer system-generated datasets in the profile store (90 days) and the data lake (13 months), including rollout timing and options for retaining data longer.

**Intents:**

* Understand how long system-generated dataset data is retained in the profile store versus the data lake.
* Identify which datasets are subject to TTL.
* Plan for the enforcement on existing customer sandboxes starting October 1, 2026.
* Retain data beyond the TTL using dataset export through Destinations or Data Distiller derived datasets.
* Understand the impact on segmentation, computed attributes, tracking, and Customer Journey Analytics.

**Glossary:**

* **Time-to-live (TTL)**: retention guardrail after which system-generated dataset data is dropped *(product-specific)*
* **Profile store**: store subject to the 90-day TTL for impacted datasets *(product-specific)*
* **Data lake**: store subject to the 13-month TTL for impacted datasets *(product-specific)*
* **Time-series dataset**: dataset type that is subject to TTL
* **Record-type dataset**: dataset type not subject to TTL (marked `n/a` in both TTL columns)
* **Data Distiller**: entitlement that allows creating derived datasets stored in the data lake without a TTL *(product-specific)*

**Guardrails:**

* Profile store TTL: 90 days for Journey Optimizer system-generated dataset data (hard limit; TTL extensions are not currently supported).
* Data lake TTL: 13 months for Journey Optimizer system-generated dataset data (hard limit; TTL extensions are not currently supported).
* AJO Message Export Dataset and AJO Message Event Metadata Dataset: 30 days data lake TTL (hard limit; both require the Message Export add-on).
* TTL is enforced on new sandboxes and new organizations as of February 2025, and on existing customer sandboxes starting October 1, 2026 (hard enforcement date).
* TTL applies only to time-series datasets; record-type datasets are `n/a` in both the Data Lake TTL and Profile Store TTL columns.
* TTL enforcement uses the event timestamp, not the ingestion date.
* Journey Optimizer system-generated datasets are protected and cannot be deleted through the standard Adobe Experience Platform UI.
* Computed attributes: initial backfill calculation is limited to the last 90 days of data; subsequent look-back is a maximum of 6 months.
* Segmentation and retargeting look-back is limited to 90 days on affected profile store data.

**Terminology:**

* Canonical name: Time-to-live — Acronym: TTL
* Do not confuse: "profile store TTL" (90 days) ≠ "data lake TTL" (13 months)
* Do not confuse: "time-series dataset" (subject to TTL) ≠ "record-type dataset" (`n/a`, not subject to TTL)
* Do not confuse: dataset TTL (drops system-generated dataset data in the profile after 90 days) ≠ deletion of the profiles themselves (the profiles are not dropped)

**FAQ:**

* **Q: Which datasets are subject to TTL?** — Only time-series datasets; record-type datasets (such as entity and classification datasets) are not subject to TTL and are marked `n/a`.
* **Q: Does the 90-day profile store TTL delete profiles?** — No; the system-generated dataset data in the profile is dropped after 90 days, not the profiles themselves.
* **Q: Can I increase the TTL?** — TTL extensions are not currently supported; you can export data through Destinations, or, with a Data Distiller entitlement, create derived datasets stored without a TTL.
* **Q: When does enforcement reach existing sandboxes?** — Starting October 1, 2026.
* **Q: Which timestamp is used for enforcement?** — The event timestamp, not the ingestion date.
* **Q: Can I delete Journey Optimizer system-generated datasets?** — No; they are protected and cannot be deleted through the standard Adobe Experience Platform UI; contact Adobe Engineering or Adobe Customer Care for permanent removal.

+++

<!-- ai-section-version: 1 | source-hash: 36918b67 -->
