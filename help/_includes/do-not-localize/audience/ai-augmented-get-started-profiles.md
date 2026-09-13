---
title: AI Knowledge Reference
---
# AI Knowledge Reference

+++ AI Knowledge Reference

This section contains structured knowledge intended to support interpretation, retrieval, and question answering related to this topic.

For complete understanding, this information should be combined with the documentation on this page. Neither source is intended to stand alone; the page describes the feature, while this section provides additional context that helps disambiguate terminology, intent, applicability, and constraints.

* **TL;DR:** Real-time Customer Profile in Adobe Journey Optimizer unifies customer data from online, offline, CRM, and third-party sources into a single view, and Engageable Profiles is the key license metric counting unique profiles engaged over a rolling 12-month window.

**Intents:**

* Understand how Real-time Customer Profile combines data into a unified customer view
* Understand the capabilities that build profiles: Data Ingestion, Identity Graph, Customer Engagement, and Data Sharing
* Learn what an Engageable Profile is and how the license metric behaves
* Access the Profiles dashboard from the Customer / Profiles menu
* Monitor the organization's Engageable Profiles count

**Glossary:**

* **Real-time Customer Profile**: Capability that integrates customer attributes and events from online, offline, and pseudonymous sources into a single, unified profile *(product-specific)*
* **Engageable Profile**: A record of information representing an individual, stored in the Profile Service and engaged by journeys or campaigns; the key license metric for Journey Optimizer *(product-specific)*
* **Addressable Audience**: The total audience from which Engageable Profiles are calculated *(product-specific)*
* **Data Ingestion**: Connecting to data sources to ingest behavioral, transactional, financial, and operational data in real-time or through batch uploads to keep profiles updated *(product-specific)*
* **Merge policies**: The rules used to determine how data is prioritized and what data is combined to create the unified view *(product-specific)*

**Guardrails:**

* Profiles are not created directly within the Journey Optimizer interface; they are automatically created or updated in Adobe Experience Platform when data is ingested.
* When ingesting data, emails are case-sensitive, so duplicate profiles may be created (for example John.Greene@luma.com and john.greene@luma.com) and used when targeting the recipient.
* The Engageable Profiles count reflects unique profiles engaged over a rolling 12-month window and is counted once per sandbox (a profile entering multiple journeys or campaigns within a sandbox counts once).
* The Engageable Profiles count can increase when new profiles are engaged, cannot decrease unless there is no engagement with certain profiles for over 12 months, and can decrease when pseudonymous profiles are stitched to known profiles.
* If the organization does not yet have active Profile datasets or merge policies created, the Profiles dashboard is not visible and the Overview tab instead shows links to Adobe Experience Platform documentation.

**Terminology:**

* Canonical name: Real-time Customer Profile — Acronym: n/a — variants: real-time customer profile, unified profile
* Synonyms: "Engageable Profiles count" = "the key license metric for Journey Optimizer"
* Do not confuse: "Real-time Customer Profile" (the unified customer data capability) ≠ "Engageable Profile" (a profile engaged by journeys or campaigns that counts toward the license metric)

**FAQ:**

* **Q: Are profiles created inside Journey Optimizer?** — No, they are automatically created or updated in Adobe Experience Platform when data is ingested.
* **Q: What is an Engageable Profile?** — A record representing an individual, stored in the Profile Service and engaged by journeys or campaigns; it is Journey Optimizer's key license metric.
* **Q: How is the Engageable Profiles count scoped over time and per sandbox?** — It reflects unique profiles engaged over a rolling 12-month window and counts a profile once per sandbox even if it enters multiple journeys or campaigns.
* **Q: Where do I monitor the Engageable Profiles count?** — From Administration > License Usage.
* **Q: Why is my Profiles dashboard not visible?** — If your organization has no active Profile datasets or merge policies yet, the dashboard is not shown and the Overview tab displays links to Adobe Experience Platform documentation.

+++

<!-- ai-section-version: 1 | source-hash: ea880b4d -->
