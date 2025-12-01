---
title: Decisioning Frequently Asked Questions
description: Get answers to common questions about Decisioning capabilities
feature: Decisioning
topic: Integrations
role: User
level: Intermediate
version: Journey Orchestration
hide: yes
hidefromtoc: yes
---
# Decisioning Frequently Asked Questions {#decisioning-faq}

This page provides answers to frequently asked questions about Decisioning capabilities in Adobe Journey Optimizer.

## Capping rules {#capping-rules}

+++**What happens when multiple capping rules are applied to a single offer?**

An offer is capped as soon as **any single condition is met**. When multiple capping rules exist, the offer stops being displayed once any rule reaches its threshold.

**Example:**
If you define two capping rules for an offer:
* 5 times per profile per week
* 100 times total across all users

The offer will stop being displayed to a user once they've seen it 5 times in a week, even if the total cap of 100 hasn't been reached yet. Similarly, once 100 total impressions are reached, the offer stops being displayed to all users.

Learn more about [capping rules](items.md#capping).

+++

## Ranking formulas {#ranking-formulas}

+++**What is the role of audiences in AI models?**

When configuring [personalized optimization models](ranking/personalized-optimization-model.md), both datasets and audiences serve distinct purposes:

* **Datasets**: Capture conversion events (clicks, orders, revenue) that serve as optimization targets for the model.
* **Audiences**: Function as predictor variables that enable the model to personalize recommendations based on customer segment membership.

Audiences do not restrict or expand the model's scope. Instead, they provide contextual attributes that improve the model's ability to make personalized predictions across different customer segments.

Both components are required for effective personalized optimization model performance. Learn more about [AI models](ranking/ai-models.md).

+++

+++**How do changes to offer collections impact AI models if using auto-optimization or personalized optimization models?**

Both models will serve traffic to the next best available offer based on traffic data from the last 30 days. 

When several offers are removed simultaneously and the remaining offers have minimal traffic data within the 30-day window, the model may exhibit suboptimal behavior, including:
* Random distribution patterns
* Bias toward offers with higher conversion rates based on limited impression data

**Best practice**: When modifying offer collections significantly, verify that remaining offers have sufficient historical performance data to maintain model effectiveness.

+++

+++**How quickly do AI models incorporate new offers?**

AI models identify and begin testing newly available offers on their next training cycle:

* **Auto-optimization**: Daily training runs
* **Personalized optimization**: Weekly training runs

Once identified, both models will start serving the new offers to some visitors immediately in order to test their performance and gather data about their effectiveness.

Learn more about [auto-optimization](ranking/auto-optimization-model.md) and [personalized optimization](ranking/personalized-optimization-model.md) models.

+++

+++**How do AI models optimize without control groups?**

Both auto-optimization and personalized optimization models employ an explore-exploit strategy that eliminates the need for dedicated control groups:

* **Initial phase**: Models begin with 100% exploration, testing different offers to establish baseline performance data.
* **Adaptive optimization**: As behavioral events accumulate and prediction accuracy improves, models automatically balance exploration and exploitation.
* **Ongoing learning**: The system progressively allocates more traffic to high-performing offers while continuing to test alternatives.

This ensures continuous learning and optimization across all traffic without requiring separate control groups.

+++

+++**What are the minimum traffic requirements for optimal AI model performance?**

Adobe recommends the following minimum thresholds to ensure effective model performance:

**Recommended minimums (per week):**
* 1,000 impressions per offer/item
* 100 conversion events per offer/item

<!--**Absolute minimums (per 30 days):**
* At least **250 impressions** per offer/item  
* At least **25 conversion events** per offer/item-->

By default, the system will not attempt to build personalized models for offers/items with fewer than 1,000 impressions or 50 conversion events.

>[!NOTE]
>
>In production environments with large offer catalogs (~300 offers) and restrictive business rules, some offers may approach lower absolute thresholds (250 impressions and 25 conversions per 30 days). These represent the minimum data requirements for model training but may not guarantee optimal performance.

Learn more about [data collection requirements](data-collection/data-collection.md).

+++

+++**How does offer similarity affect AI model performance?**

AI models generate greater personalization benefits when offers appeal to distinct customer segments. When offers are highly similar, two outcomes are typical:

* **Equivalent performance**: Offers perform identically and receive approximately equal traffic distribution.
* **Dominant offer**: Minor differences cause one offer to outperform others across all segments, capturing the majority of traffic.

>[!NOTE]
>
>Offer differentiation does not guarantee balanced traffic distribution. Offers with objectively superior value propositions (for example, €100 discount versus €50 discount) will typically dominate across all customer segments regardless of personalization efforts.

**Best practice**: Design offers with meaningful differentiation that align with distinct customer segment preferences to maximize AI model effectiveness.

+++

+++**How do traffic anomalies impact AI model performance?**

Traffic anomalies are incorporated into the model proportionally within the 30-day rolling window. 

**Impact assessment:**
A temporary traffic spike (for example, 2x daily traffic) has minimal effect on overall model performance because the anomalous traffic represents a small fraction of the 30-day dataset.

**Key insight**: The rolling 30-day data window provides model stability during temporary traffic fluctuations. Short-term spikes or drops do not significantly disrupt model predictions or performance.

+++

## Related topics {#related-topics}

<!--* [Get started with Decisioning](gs-experience-decisioning.md)-->
* [Create decision items](items.md)
* [AI models overview](ranking/ai-models.md)
* [Decisioning guardrails & limitations](decisioning-guardrails.md)

