---
title: AI Knowledge Reference
---
# AI Knowledge Reference

+++ AI Knowledge Reference

This section contains structured knowledge intended to support interpretation, retrieval, and question answering related to this topic.

For complete understanding, this information should be combined with the documentation on this page. Neither source is intended to stand alone; the page describes the feature, while this section provides additional context that helps disambiguate terminology, intent, applicability, and constraints.

* **TL;DR:** This page explains how to create an API triggered campaign by choosing its type (Marketing or Transactional), and how to set its name, description, tags, and access labels in the **Properties** tab.

**Intents:**

* Create an API triggered campaign from the **API triggered** tab of the **Campaigns** menu
* Choose between **API triggered - Marketing** and **API triggered - Transactional**
* Enable **High Throughput** mode for a transactional API triggered campaign
* Assign Unified Tags to the campaign
* Limit access to the campaign with access labels using **Manage access**

**Glossary:**

* **API triggered - Marketing**: Campaign type used to send personalized marketing communications to targeted audiences
* **API triggered - Transactional**: Campaign type used to send transactional messages, that is messages sent out following an action performed by an individual, such as a password reset request or a cart purchase
* **High Throughput** mode: Mode designed for large-scale, real-time messaging (up to 5000 transactions per second) that provides higher availability with lower latency *(product-specific)*
* **Tags**: Adobe Experience Platform Unified Tags assigned to a campaign to classify it and improve search from the campaigns list
* **Access labels**: Labels used to limit access to the campaign, set with **Manage access**

**Guardrails:**

* Make sure to select only access labels you have permission for.

**Prerequisites and permissions:**

* **High Throughput** mode is only available for organizations that have purchased the Adobe **High throughput transactional messaging** add-on offering.

**Applicability:**

* **High Throughput** mode: transactional API triggered campaigns only; currently available only for the email channel and in the US region

**Terminology:**

* Canonical name: API triggered campaign
* Acronym: OLAC — Object level access control
* Acronym: AEP — Adobe Experience Platform
* Short name: Platform — Adobe Experience Platform
* Do not confuse: **API triggered - Marketing** (marketing communications to targeted audiences) ≠ **API triggered - Transactional** (messages sent following an action performed by an individual)

**FAQ:**

* **Q: How do I create an API triggered campaign?** — Browse to the **Campaigns** menu, select the **API triggered** tab, click **Create campaign**, and select the campaign type.
* **Q: Which campaign types are available?** — **API triggered - Marketing** and **API triggered - Transactional**.
* **Q: What is required for High Throughput mode?** — The Adobe **High throughput transactional messaging** add-on offering; it is currently available only for the email channel and in the US region.
* **Q: How do I limit access to a campaign?** — Use the **Manage access** button to add access labels, selecting only labels you have permission for.

**Related pages:**

* High Throughput mode: Learn how to work with the Highthrouput mode (campaigns/api-triggered-high-throughput.md)
* Tags: Learn how to work with tags (start/search-filter-categorize.md#tags)
* Access labels: Learn more about Object Level Access Control (administration/object-based-access.md)
* Next step, configuring the action: Learn more (campaigns/api-triggered-campaign-action.md)

+++

<!-- ai-section-version: 1 | source-hash: 95cb2ca2 -->
