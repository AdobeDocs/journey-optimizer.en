---
title: AI Knowledge Reference
---
# AI Knowledge Reference

+++ AI Knowledge Reference

This section contains structured knowledge intended to support interpretation, retrieval, and question answering related to this topic.

For complete understanding, this information should be combined with the documentation on this page. Neither source is intended to stand alone; the page describes the feature, while this section provides additional context that helps disambiguate terminology, intent, applicability, and constraints.

* **TL;DR:** This page explains how to configure and track journey success metrics in Adobe Journey Optimizer by assigning a KPI to a journey and reviewing its performance in journey reports.

**Intents:**
* Add the required AEP dataset field groups (Commerce Details, Web, Mobile) as a prerequisite for journey metrics
* Assign a journey metric (KPI) to a journey during journey creation or configuration
* Understand which metrics are available based on the configured dataset field groups
* Interpret attribution models for journey metrics under Journey Optimizer and Customer Journey Analytics licenses
* Create custom success metrics using a Customer Journey Analytics license
* Track journey performance against the assigned KPI in journey reports

**Glossary:**
* **Journey metrics**: KPIs assigned to a journey to measure its effectiveness, visible in journey reports *(product-specific)*
* **Last Touch attribution**: The default attribution model that credits the most recent interaction before a conversion
* **Commerce Details field group**: An XDM field group enabling commerce-related metrics such as Purchases, Checkouts, and Cart events
* **Lookback window**: The time range over which attribution is evaluated; set to a maximum of 7 days with Journey Optimizer license only

**Guardrails:**
* Only one journey metric is allowed per journey
* Dataset field groups (Commerce Details, Web, Mobile) must be selected from built-in options, not custom groups, and added under Configuration > Reporting in Adobe Experience Platform
* Without a configured dataset, only Clicks, Unique Clicks, Clickthrough Rate, and Open Rate are available
* The maximum lookback window is 7 days with a Journey Optimizer license only
* Custom metrics and custom attribution settings require a Customer Journey Analytics license

**Terminology:**
* Canonical name: Journey metrics — Acronym: none — variants: success metrics, journey success metrics
* Canonical name: Clickthrough Rate — Acronym: CTR — variants: none
* Canonical name: Clickthrough Open Rate — Acronym: CTOR — variants: none
* Synonyms: "journey metrics" = "success metrics" (used interchangeably in the UI and documentation)
* Do not confuse: "Journey Optimizer license attribution" ≠ "Customer Journey Analytics attribution" — CJA license enables custom attribution models and longer lookback windows

**FAQ:**
* **Q: How many journey metrics can I assign to a single journey?** — Only one journey metric is allowed per journey.
* **Q: What metrics are available if I haven't configured a dataset with field groups?** — Only Clicks, Unique Clicks, Clickthrough Rate, and Open Rate are available without additional field group configuration.
* **Q: What field groups do I need to enable purchase and commerce metrics?** — You need to add the Commerce Details field group to your reporting dataset in Adobe Experience Platform.
* **Q: What is the default attribution model for journey metrics?** — Last Touch, which credits the most recent interaction before conversion, with a maximum 7-day lookback window under a Journey Optimizer license.
* **Q: Can I create custom success metrics?** — Yes, but only with a Customer Journey Analytics license.
* **Q: Where can I see the journey metrics results after publishing?** — In the journey report's KPIs and Journey Stats table.

+++
