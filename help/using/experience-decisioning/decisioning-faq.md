---
title: Decisioning Frequently Asked Questions
description: Get answers to common questions about Decisioning capabilities
feature: Decisioning
topic: Integrations
role: User
level: Intermediate
version: Journey Orchestration
exl-id: 7bb72527-d4e1-49f8-b2c3-c943d65903f2
TQID: 'https://experienceleague.adobe.com/rqXcnwygtE6Q8Fi1Lg3EgCqIG9wPwmrzgDvtaiZPavA'
product_v2:
  - id: cb954087-f4fc-4456-afb9-e939cabcdc79
    internal-label: Journey Optimizer
feature_v2:
  - id: a4cb03e1-327e-499d-9de8-e0c0db8a63a2
    internal-label: Decision capabilities
  - id: a984631b-2bae-4860-9b15-69c41a799dcb
    internal-label: APIs and SDKs
subfeature_v2:
  - id: a7a194a0-75e2-4913-8a83-14714fbf68e6
    internal-label: Decisioning API
  - id: eb547372-2a95-4d13-b0fd-f720c9895880
    internal-label: Edge Decisioning
role_v2:
  - id: b69b2659-1057-424e-8fc5-ed9e016dc554
    internal-label: User
level_v2:
  - id: b5a62a22-46f7-4f0d-b151-3fc640bef588
    internal-label: Intermediate
topic_v2:
  - id: cdd65e7e-8839-44a2-bc21-0e03623b5dd1
    internal-label: Optimization
  - id: d3cdead0-685a-4489-9250-4bb709942f66
    internal-label: Data collection
  - id: e0eb8757-182f-49f3-94a4-1587d16f5094
    internal-label: Personalization
---
# Decisioning frequently asked questions {#decisioning-faq}

>[!BEGINSHADEBOX]

**On this page:** Find answers to common questions about Decisioning capabilities, from getting started and the differences with Decision management to eligibility, capping rules, ranking formulas, and AI model behavior, so you can configure and troubleshoot decisioning with confidence.

>[!ENDSHADEBOX]

This page provides answers to frequently asked questions about Decisioning capabilities in Adobe Journey Optimizer.

## Getting started {#getting-started}

+++**What is Decisioning?**

Decisioning is the next-generation decisioning framework in Adobe Journey Optimizer. It simplifies personalization by offering a centralized catalog of marketing offers known as decision items, and a decision engine that leverages rules and ranking criteria to select and present the most relevant decision items to each individual.

Decision items are integrated into messages and experiences across Journey Optimizer channels: code-based experience, web, email, mobile messages, push notifications, custom channels, and direct mail.

Learn more about [Decisioning](gs-experience-decisioning.md#about).

+++

+++**Where do I start?**

1. Read [How Decisioning works](how-decisioning-works.md) to see how decision items, collections, rules, ranking methods, selection strategies, and decision policies fit together.

1. Check the [prerequisites](gs-experience-decisioning.md#prerequisites). Decisioning is only available to users with access to a Decisioning related role, such as Decision managers.

1. Follow the [key steps](gs-experience-decisioning.md#steps) to set up your decision items, collections, rules, ranking methods, selection strategies, and decision policy.

If you prefer to learn by watching, see the [Decisioning tutorials](https://experienceleague.adobe.com/en/docs/journey-optimizer-learn/tutorials/decision-capabilities/decisioning/introduction-to-decisioning){target="_blank"}. If an item does not appear as expected, go through the [troubleshooting checklist](decisioning-troubleshooting.md#troubleshooting).

+++

## Key concepts {#key-concepts}

+++**What are the key concepts of Decisioning?**

Decisioning works with a handful of objects that you configure in advance:

* **Decision items**: Offers or pieces of content in the Offers catalog. Each item has its own start and end dates, priority, eligibility, and capping rules.
* **Collections**: Groups of items based on attribute rules, for example all the items where the `Category` attribute is `Yoga`.
* **Decision rules**: Reusable conditions that determine who qualifies.
* **Ranking methods**: Set the order of the qualifying items: the item priority (default), a ranking formula, or an AI model.
* **Selection strategies**: Reusable objects that combine a collection, an eligibility constraint, and a ranking method.
* **Decision policies**: Put selection strategies in order, set how many items to return, and define optional fallback items. A decision policy is added to the content of a campaign or journey.
* **Placements** (email only): Containers for the items displayed in an email.

Learn more about [the building blocks of Decisioning](how-decisioning-works.md#building-blocks).

+++

## Decision management and Decisioning {#decision-management}

+++**What is the difference between Decision management and Decisioning?**

Decision management is the legacy decisioning framework in Adobe Journey Optimizer. Decisioning is the next-generation framework and feature set. It offers significant capabilities and benefits over Decision management, for example:

* **Schema-based items**: You define the attributes of your decision items once, in the schema of the catalog, and every item inherits them.
* **Reusable decision logic**: A selection strategy is a reusable object, and decision logic can be reused across placements and locations. In Decision management, decision logic is tied to a specific placement.
* **Experimentation**: Decisioning introduces experimentation, so you can experiment on items, aspects of an item, and ranking methods.
* **Integrated authoring**: You can insert Decisioning components directly in your message authoring workflows.

The objects of the two frameworks do not always map one to one. For example, an offer becomes a decision item, and a decision maps to a selection strategy and a decision policy.

Learn more about [Decisioning and Decision management terms](how-decisioning-works.md#compare) and the [benefits of migrating to Decisioning](migrate-to-decisioning.md). To move your Decision management objects, use the [migration tooling](decisioning-migration-api.md).

+++

## Eligibility {#eligibility}

+++**What is the difference between an audience and a decision rule?**

Both restrict who can receive an item, or who a selection strategy applies to, but they are evaluated differently:

* **Audience**: A list of profiles that Adobe Experience Platform computes from profile attributes and experience events. The audience is not recomputed when a decision is made, so it might not be up to date.
* **Decision rule**: A condition that runs against the individual profile every time a decision is made, so each profile gets the latest result. A rule can use profile attributes, audiences, and context data.

Learn more about [audiences and decision rules](decisioning-troubleshooting.md#audiences-rules).

+++

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

## Strategy sequence {#strategy-sequence}

+++**Why is the item with the highest score not returned first?**

Selection strategies are evaluated in the order of the strategy sequence. The first selection strategy or decision item in the sequence has the highest priority. Selection strategies that you combine in a group have the same priority, so their qualifying items are ranked together according to their scores. The items of a later group are placed after the items of the earlier groups, whatever their score.

In the example on the concept page, Offer 6 has the highest score (60) but comes last, because it belongs to the group with the lower priority.

Learn more about [what happens when a decision is requested](how-decisioning-works.md#decision-process).

+++

## Ranking formulas {#ranking-formulas}

+++**What is the role of audiences versus a full dataset in AI models?**

When configuring [AI models](ranking/ai-models.md), both datasets and audiences serve distinct purposes.

* **Datasets**: Capture conversion events (clicks, orders, revenue) that serve as optimization targets for the model.
* **Audiences**: Function as predictor variables that enable the model to personalize recommendations based on customer segment membership.

Audiences do not restrict or expand the model's scope. Instead, they provide contextual attributes that improve the model's ability to make personalized predictions across different customer segments.

Both components are required for effective [personalized optimization models](ranking/personalized-optimization-model.md) model performance.

+++

+++**How do changes to offer collections impact auto-optimization or personalized optimization models?**

The auto-optimization model serves traffic to the next best available offer based on traffic data from the last 14 days, whether the personalized optimization model uses traffic data from the last 30 days.

When several offers are removed simultaneously and the remaining offers have minimal traffic data within the 14-day or 30-day window, the model may exhibit suboptimal behavior, including random distribution patterns or bias toward offers with higher conversion rates based on limited impression data.

**Best practice**: When modifying offer collections significantly, verify that remaining offers have sufficient historical performance data to maintain model effectiveness.

+++

+++**How quickly do AI models incorporate new offers?**

AI models identify and begin testing newly available offers on their next training cycle:

* **Auto-optimization** identifies and begins testing new offers on its next training cycle. Auto-optimization training occurs 3 to 4 times daily, approximately every 6 hours.
* **Personalized optimization** identifies and begins testing new offers as they are added to the offer strategy. They will be included in random exploration traffic. Then, those offers will be personalized in the model's next training cycle, occurring on a weekly basis.

Once identified, both models will start serving the new offers to some visitors immediately in order to test their performance and gather data about their effectiveness.

Learn more about [auto-optimization](ranking/auto-optimization-model.md) and [personalized optimization](ranking/personalized-optimization-model.md) models.

+++

+++**How do AI models optimize without control groups?**

Both auto-optimization and personalized optimization models employ an "explore-exploit" strategy that eliminates the need for dedicated control groups.

* **Initial phase**: Models begin with 100% exploration, testing different offers to establish baseline performance data.
* **Adaptive optimization**: As behavioral events accumulate and prediction accuracy improves, models automatically balance exploration and exploitation.
* **Ongoing learning**: The system progressively allocates more traffic to high-performing offers while continuing to test alternatives.

This ensures continuous learning and optimization across all traffic without requiring separate control groups.

+++

+++**What are the minimum traffic requirements for optimal AI model performance?**

Adobe recommends the following minimum thresholds to ensure effective model performance:
* 1,000 impressions per offer/item per week
* 100 conversion events per offer/item per week

<!--
**Absolute minimums (per 30 days):**
* At least **250 impressions** per offer/item  
* At least **25 conversion events** per offer/item
-->

By default, the system will not attempt to build personalized models for offers/items with fewer than 1,000 impressions or 50 conversion events.

>[!NOTE]
>
>In production environments with large offer catalogs (~300 offers) and restrictive business rules, some offers may approach lower absolute thresholds (250 impressions and 25 conversions per 30 days). These represent the minimum data requirements for model training but may not guarantee optimal performance.

Learn more about [data collection requirements](data-collection/data-collection.md).

+++

+++**How do similar offers affect AI model performance?**

AI models generate greater personalization benefits when offers appeal to distinct customer segments. When offers are highly similar, two outcomes are typical:

* **Equivalent performance**: Offers perform identically and receive approximately equal traffic distribution.
* **Dominant offer**: Minor differences cause one offer to outperform others across all segments, capturing the majority of traffic.

>[!NOTE]
>
>Offer differentiation does not guarantee balanced traffic distribution. Offers with objectively superior value propositions (for example, &euro;100 discount versus &euro;50 discount) will typically dominate across all customer segments regardless of personalization efforts.

**Best practice**: Design offers with meaningful differentiation that align with distinct customer segment preferences to maximize AI model effectiveness.

+++

+++**How do traffic anomalies impact AI model performance?**

Traffic anomalies are incorporated into the model proportionally within the 30-day rolling window, which provides model stability during temporary traffic fluctuations. Short-term spikes or drops do not significantly disrupt model predictions or performance.

A temporary traffic spike (for example, twice the daily traffic) has minimal effect on overall model performance because the anomalous traffic represents a small fraction of the 30-day dataset.

+++

## Troubleshooting {#troubleshooting}

+++**Why was an item not shown to a profile?**

Go through the [troubleshooting checklist](decisioning-troubleshooting.md#troubleshooting). It covers the dates and status of the item, the collection, the eligibility of the profile, capping rules, the order of the strategies and the number of items requested, fallback items, and recent changes.

You can also ask the [Decisioning Explainer](experience-decisioning-coworker-skills.md#decisioning-explainer) why an offer was or was not shown to a profile or segment. It is available to customers who have access to Coworker and Decisioning.

+++

+++**How long do changes take to apply?**

* Changes to a decision policy and to the objects it uses can take up to 15 minutes to propagate across all data regions, and up to 30 minutes for Canada. This includes adding an item to a collection, changing a rule or the content of an item, and updating a formula.
* A capping counter can take up to 3 seconds to update. After you approve an item or create a capping rule, it can take up to 15 minutes before events are counted toward the cap.

Learn more about [when changes take effect](decisioning-troubleshooting.md#timing).

+++
