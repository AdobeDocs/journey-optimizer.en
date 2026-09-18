---
title: AI Knowledge Reference
---
# AI Knowledge Reference

+++ AI Knowledge Reference

This section contains structured knowledge intended to support interpretation, retrieval, and question answering related to this topic.

For complete understanding, this information should be combined with the documentation on this page. Neither source is intended to stand alone; the page describes the feature, while this section provides additional context that helps disambiguate terminology, intent, applicability, and constraints.

- **TL;DR:** Learn how to create computed attributes on Adobe Experience Platform and leverage them in Journey Optimizer for segmentation, personalization, and journey logic.

**Intents:**
- Understand what computed attributes are and how they differ from standard profile attributes
- Create computed attributes by combining event attributes, aggregate functions, and a lookback period
- Add the SystemComputedAttributes field group to the Experience Platform data source in AJO
- Use computed attributes in journey conditions, audience building, and message personalization

**Glossary:**
- **Computed attribute**: A profile attribute derived from aggregated behavioral event data, stored in customer profiles *(product-specific)*
- **Lookback period**: The time window applied when calculating a computed attribute's aggregation rule (e.g. "last 3 months") *(product-specific)*
- **SystemComputedAttributes field group**: The field group in AJO's Experience Platform data source that exposes all published computed attributes for use in journeys and personalization *(product-specific)*
- **Profile union schema**: The merged schema that combines all profile fragments for a given identity, where computed attributes are stored

**Guardrails:**
- Requires **View Computed attributes** and **Manage Computed attributes** permissions to access the feature
- Computed attributes must be **published** in AEP before they become available downstream in Journey Optimizer
- Computed attributes must be explicitly added to the **Experience Platform data source** in AJO before they can be used in journeys or personalization
- Computed attributes are based on Profile-enabled Experience Event datasets ingested into Adobe Experience Platform

**Terminology:**
- Canonical name: Adobe Journey Optimizer — Acronym: AJO — variants: Journey Optimizer, A-JO
- Canonical name: Adobe Experience Platform — Acronym: AEP
- Synonyms: "computed attributes" = "computed profile attributes"
- Do not confuse: "computed attributes" (AEP/AJO-specific aggregated feature) ≠ generic "profile attributes"

**FAQ:**
- **Q: What are computed attributes?** — Aggregated behavioral event data (e.g. total purchases, last viewed item) stored as profile attributes on AEP and usable in AJO.
- **Q: Do I need special permissions?** — Yes: "View Computed attributes" and "Manage Computed attributes" are both required.
- **Q: How do I make computed attributes available in Journey Optimizer?** — Add the `SystemComputedAttributes` field group to the Experience Platform data source under Configurations > Data sources.
- **Q: Where can I use computed attributes in AJO?** — In Condition activities (journey splitting), audience creation, and the personalization editor.
- **Q: What is a lookback period?** — The time window used to scope the aggregation rule, e.g. "sum of purchases in the last 3 weeks."
- **Q: Can I use computed attributes in real-time journeys?** — Yes, once published and added to the data source, they are accessible like any other profile attribute.

+++
