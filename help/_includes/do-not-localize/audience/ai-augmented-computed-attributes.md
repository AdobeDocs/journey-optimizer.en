---
title: AI Knowledge Reference
---
# AI Knowledge Reference

+++ AI Knowledge Reference

This section contains structured knowledge intended to support interpretation, retrieval, and question answering related to this topic.

For complete understanding, this information should be combined with the documentation on this page. Neither source is intended to stand alone; the page describes the feature, while this section provides additional context that helps disambiguate terminology, intent, applicability, and constraints.

- **TL;DR:** Learn how to create computed attributes on Adobe Experience Platform and use them in Journey Optimizer for segmentation, personalization, and journey logic.

**Intents:**
- Understand what computed attributes are
- Create computed attributes by combining event attributes, aggregate functions, and a lookback period
- Add the SystemComputedAttributes field group to the Experience Platform data source in Journey Optimizer
- Use computed attributes in journey conditions, audience building, and message personalization

**Glossary:**
- **Computed attribute**: A profile attribute derived from aggregated behavioral event data, stored in customer profiles *(product-specific)*
- **Lookback period**: The time window applied when calculating a computed attribute's aggregation rule (e.g. "last 3 months") *(product-specific)*
- **SystemComputedAttributes field group**: The field group added to the Journey Optimizer Experience Platform data source that contains all the created computed attributes *(product-specific)*
- **Profile union schema**: The schema on which computed attributes are created as profile attribute fields

**Guardrails:**
- Requires **View Computed attributes** and **Manage Computed attributes** permissions to access the feature
- Computed attributes must be **published** before they become available in other downstream services, including Journey Optimizer
- Computed attributes must be explicitly added to the **Experience Platform data source** in Journey Optimizer before they can be used in journeys or personalization
- Computed attributes are based on Profile-enabled Experience Event datasets ingested into Adobe Experience Platform

**Terminology:**
- Canonical name: Adobe Journey Optimizer — Acronym: AJO — variants: Journey Optimizer
- Canonical name: Adobe Experience Platform — Acronym: AEP
- Synonyms: "computed attributes" = "computed profile attributes"

**FAQ:**
- **Q: What are computed attributes?** — Aggregated behavioral event data (e.g. total purchases, last viewed item) stored as profile attributes on Adobe Experience Platform and usable in Journey Optimizer.
- **Q: Do I need special permissions?** — Yes: "View Computed attributes" and "Manage Computed attributes" are both required.
- **Q: How do I make computed attributes available in Journey Optimizer?** — Add the `SystemComputedAttributes` field group to the Experience Platform data source under Configurations > Data sources.
- **Q: Where can I use computed attributes in Journey Optimizer?** — In Condition activities (journey splitting), audience creation, and the personalization editor.
- **Q: What is a lookback period?** — The time window used to scope the aggregation rule, e.g. "sum of purchases in the last 3 weeks."

+++

<!-- ai-section-version: 1 | source-hash: 5c9a5633 -->
