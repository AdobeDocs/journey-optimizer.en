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

+++**What happens when you create more than one capping rule for an offer? Will we stop showing the offer when we match any of the capping rules, or all of them?**

The offer is capped as soon as **one condition is met**. This means that any of the capping rules will stop the offer from being shown once its threshold is reached.

For example, if you have two capping rules:
* 5 times per profile per week
* 100 times total across all users

The offer will stop being displayed to a user once they've seen it 5 times in a week, even if the total cap of 100 hasn't been reached yet. Similarly, once 100 total impressions are reached, the offer stops being displayed to all users.

Learn more about [capping rules](items.md#capping).

+++

## Ranking formulas {#ranking-formulas}

+++**Why would I add an audience to an AI model? What is the benefit of adding audiences versus a full dataset? Will it restrict the model or expand the model?**

When working with AI models (specifically [personalized optimization models](ranking/personalized-optimization-model.md)):

* **Datasets** are added to collect your conversion events (clicks, orders, revenue). These are the outcomes the model tries to optimize for.
* **Audiences** are added to be used as predictor variables in the model. They help personalize predictions to try to predict clicks, orders, or revenue for different customer segments.

Both datasets and audiences are needed for the personalized optimization model to work effectively. Audiences **neither restrict nor expand** the model—instead, they provide additional context that helps the model make better personalized decisions.

Learn more about [AI models](ranking/ai-models.md).

+++

+++**Will adding or removing offers to a collection have any impact on the model if I'm using auto-optimization or personalized optimization models?**

Both models will serve traffic to the next best available offer based on traffic data from the last 30 days. 

If several offers are removed at one time and the remaining offers received very little traffic within the last 30 days, then offer distribution may behave unexpectedly. This could result in random distribution or bias towards certain offers that have a higher conversion rate based on only a few impressions.

**Best practice**: When making significant changes to offer collections, ensure that the remaining offers have sufficient historical performance data to maintain optimal model performance.

+++

+++**How long does it take for the AI models to understand that there is new content added and start to add them to the mix?**

Both AI models will identify newly available offers on the next training run:

* **Auto-optimization**: Daily training runs
* **Personalized optimization**: Weekly training runs

Once identified, both models will start serving the new offers to some visitors immediately in order to test their performance and gather data about their effectiveness.

Learn more about [auto-optimization](ranking/auto-optimization-model.md) and [personalized optimization](ranking/personalized-optimization-model.md) models.

+++

+++**If we don't have control groups in the AI models, are we learning and optimizing all traffic, all at the same time?**

Yes. Both AI models (auto-optimization and personalized optimization) use an "explore and exploit" approach:

* Initially, both models are **100% exploration**, meaning they test different offers to gather performance data.
* Over time, the models **automatically manage the explore/exploit tradeoff** as behavioral events are collected and predictions improve.
* The models gradually shift more traffic to better-performing offers while continuing to explore and test other options.

This ensures continuous learning and optimization across all traffic without requiring separate control groups.

+++

+++**How many optimization events do we need to be statistically significant? Is there a minimum traffic threshold for a surface?**

To ensure optimal model performance, Adobe recommends the following minimums:

**Recommended minimums (per week):**
* At least **1,000 impressions** per offer/item
* At least **100 conversion events** per offer/item

<!--**Absolute minimums (per 30 days):**
* At least **250 impressions** per offer/item  
* At least **25 conversion events** per offer/item-->

By default, the system will not attempt to build personalized models for offers/items with fewer than 1,000 impressions or 50 conversion events.

**Important**: In practice, some customers have many offers (~300) in a single model, and some offers may have very restrictive business rules. The absolute minimums (250 impressions / 25 conversions per 30 days) represent the lowest threshold the system can support for building models.

Learn more about [data collection requirements](data-collection/data-collection.md).

+++

+++**Do the content of the offers need to be clearly differentiated for the AI models to work well? What happens if I have multiple offers that are too similar to each other?**

Generally speaking, the AI model will be more likely to generate benefits from personalization when **offers are suited to different types of customers**. 

When offers are very similar, one of two outcomes is likely:

* **Similar performance**: The offers will perform identically and receive a relatively even share of traffic.
* **Dominance**: Small differences may cause one offer to dominate the others across all customer types, and it will receive the bulk of traffic.

>[!NOTE]
>
>Differences in offers are not a guarantee that one offer won't dominate the others. For example, a €100 off offer will almost always outperform a €50 off offer across all customer types, regardless of personalization.

**Best practice**: Ensure your offers provide meaningful differentiation that can appeal to different customer segments for optimal AI model performance.

+++

+++**What happens to the model if there is a traffic anomaly, like a huge traffic spike? Will it cause issues or lift weirdness?**

A traffic spike would be included in the modeling proportionally to other traffic in the last 30 days. 

For example, a 2x daily traffic spike will have a relatively modest effect on the overall model, because there are 29 days of normal traffic which represent significantly more of the overall behavioral data. 

**Key point**: The rolling 30-day window helps the model maintain stability during temporary traffic anomalies. Short-term spikes or dips won't significantly disrupt model performance.

+++

## Related topics {#related-topics}

<!--* [Get started with Decisioning](gs-experience-decisioning.md)-->
* [Create decision items](items.md)
* [AI models overview](ranking/ai-models.md)
* [Decisioning guardrails & limitations](decisioning-guardrails.md)

