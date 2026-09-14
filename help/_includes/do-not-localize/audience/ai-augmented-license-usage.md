---
title: AI Knowledge Reference
---
# AI Knowledge Reference

+++ AI Knowledge Reference

This section contains structured knowledge intended to support interpretation, retrieval, and question answering related to this topic.

For complete understanding, this information should be combined with the documentation on this page. Neither source is intended to stand alone; the page describes the feature, while this section provides additional context that helps disambiguate terminology, intent, applicability, and constraints.

* **TL;DR:** The License usage dashboard in Adobe Journey Optimizer displays your organization's license usage from a daily snapshot, centered on the Engageable Profiles metric, and provides guidance to troubleshoot sudden increases in that count.

**Intents:**

* Navigate the license usage dashboard from Administration > License Usage
* Check the number of Engageable Profiles engaged over a rolling 12-month window
* Understand why the Engageable Profiles count may suddenly increase
* Follow the resolution steps to address a spike in Engageable Profiles

**Glossary:**

* **License usage dashboard**: A dashboard displaying important information about your organization's license usage, captured during a daily snapshot *(product-specific)*
* **Engageable Profiles**: Unique profiles engaged through journeys, campaigns, or decisioning over a rolling 12-month window *(product-specific)*
* **Addressable Audience**: The total audience used to calculate Engageable Profiles *(product-specific)*

**Guardrails:**

* To view the dashboard, you must have the View License Usage Dashboard permission.
* Certain metrics (for example compute hours, emails) are not displayed for development sandboxes and are shown as `N/A` in the quota column.
* Only non-null values are displayed; when metrics are zero or close to zero they are not populated.
* The Engageable Profiles metric cannot decrease unless there is no engagement with certain profiles for over 12 months, or if pseudonymous profiles are stitched to known ones.
* Pseudonymous Profile data expiration cannot be configured through the Platform UI or APIs; you must contact support to enable this feature.
* Deleting pseudonymous profiles affects both Journey Optimizer and Real-Time Customer Data Platform.

**Terminology:**

* Canonical name: License usage dashboard — Acronym: n/a — variants: license usage dashboard, License Usage
* Synonyms: "Engageable Profiles count" = "number of unique profiles engaged over the rolling 12-month window"
* Do not confuse: "Engageable Profiles" (unique profiles engaged through journeys, campaigns, or decisioning) ≠ "Addressable Audience" (the total audience the count is calculated from)

**FAQ:**

* **Q: Where do I access the license usage dashboard?** — Go to Administration > License Usage, which opens the Overview tab displaying the dashboard.
* **Q: What permission do I need to view the dashboard?** — The View License Usage Dashboard permission.
* **Q: What can cause a sudden spike in the Engageable Profiles count?** — Large audiences targeted by new journeys or campaigns, changes in datasets enabled for Profile Service, or batch processing of audiences not engaged recently.
* **Q: Can the Engageable Profiles count decrease?** — Only if certain profiles have no engagement for over 12 months, or when pseudonymous profiles are stitched to known ones.
* **Q: Why are some metrics shown as N/A?** — Certain metrics such as compute hours and emails are not displayed for development sandboxes.

+++

<!-- ai-section-version: 1 | source-hash: 2fcfdb20 -->
