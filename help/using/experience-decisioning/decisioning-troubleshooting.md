---
solution: Journey Optimizer
product: journey optimizer
title: Troubleshoot Decisioning
description: Learn how eligibility, capping, ranking, and fallback items decide which decision items a profile receives, and find out why an item was or was not shown.
feature: Decisioning
topic: Personalization
role: User
level: Intermediate
keywords: decisioning, eligibility, audience, decision rule, capping, ranking, fallback, troubleshooting, decision policy
---
# Troubleshoot Decisioning {#decisioning-troubleshooting}

>[!BEGINSHADEBOX]

**On this page:** Understand how eligibility, capping, ranking, and fallback items decide which decision items a profile receives, and use a checklist to find out why an item was or was not shown.

>[!ENDSHADEBOX]

An item did not show up, or a different one did? This page explains the rules that Decisioning applies and ends with a checklist to help you find out why. In a hurry? Go straight to the [troubleshooting checklist](#troubleshooting).

If you are new to Decisioning, start with [How Decisioning works](how-decisioning-works.md) to see how decision items, collections, rules, ranking methods, selection strategies, and decision policies fit together.

## Control who qualifies {#eligibility}

By default, all profiles are eligible for a decision item and for a selection strategy. You can restrict eligibility with audiences or decision rules, and you can limit how often an item is presented with capping rules.

### Audiences and decision rules {#audiences-rules}

Audiences and decision rules both restrict who can receive an item, or who a selection strategy applies to. They are evaluated differently:

| Aspect | Audience | Decision rule |
| --- | --- | --- |
| **What it is** | A list of profiles that Adobe Experience Platform computes from profile attributes and experience events. | A condition that runs against the individual profile. |
| **When it is evaluated** | The audience is not recomputed when a decision is made, so it might not be up to date. | Every time a decision is made, so each profile gets the latest result. |
| **What it can use** | Profile attributes and experience events. | Profile attributes, audiences, and context data. A rule created for the **[!UICONTROL Decision item]** entity can also use decision item attributes. |

[Learn more about eligibility](items.md#eligibility) and [decision rules](rules.md)

### Capping {#capping}

Capping limits how many times a decision item can be presented.

* You can create several capping rules for an item. The item is capped as soon as any single rule reaches its threshold.

* A capping rule counts decision events (default), impressions (inbound channels only), clicks, or custom events.

    * Decision events are collected automatically. For the other events, the schema that collects your experience events must include the field group for that event. Otherwise, the counter might not be incremented correctly.
    * Push notifications do not support standard impression and click capping. Use custom events instead.
    * Custom events must be experience events that you ingest. Delivery events, such as an email send, are not supported.

* A capping rule applies in total, across all profiles, or per profile. Its scope is the offer level (default), each placement, or specific placements. Placement scopes do not apply to capping rules based on Adobe Experience Platform data.

* For the delays that apply to capping counters, see [When do changes take effect?](#timing)

[Learn more about capping rules](items.md#capping)

## Rank the qualifying items {#ranking}

When several items qualify for a selection strategy, the ranking method of the strategy decides which one comes first:

| Ranking method | How it ranks the items | Learn more |
| --- | --- | --- |
| **Offer priority** (default) | The items with the highest priority are delivered first. You set the priority on each decision item. | [Create decision items](items.md) |
| **Ranking formula** | Calculates a score from your own logic instead of the item priority. For example, you can boost the offers whose end date is less than 24 hours from now. | [Ranking formulas](ranking/ranking-formulas.md) |
| **AI model** | Uses a trained model system to rank the items for each profile. | [AI models](ranking/ai-models.md) |

Auto-optimization models optimize on the overall performance of the offers. Personalized optimization models use customer data to personalize the ranking. AI models learn from the impression and conversion events that you collect in a dataset. Each model type has its own requirements and limitations: see [Auto-optimization](ranking/auto-optimization-model.md#requirements-limitations) and [Personalized optimization](ranking/personalized-optimization-model.md#key).

## Fallback items {#fallback}

Fallback items are optional. You select them when you configure the decision policy.

* Fallback items are displayed when none of the selection strategies of the policy qualify.

* A fallback item is displayed regardless of the dates and the eligibility constraints set on the item.

* You can select up to the number of items that the policy requests.

* If no item qualifies and no fallback is defined, nothing is displayed. In an email, when two decision policies select the same item, the second policy displays a blank space unless a fallback is configured.

* To see how often fallback items are displayed, check the **[!UICONTROL Fallback rate]** in the Decisioning KPIs: the percentage of instances where no selection strategy qualified. [Learn more about Decisioning KPIs](../reports/campaign-global-report-cja-code.md#decisioning-kpis)

[Learn more about fallback items](create-decision-policy.md#fallback)

## When do changes take effect? {#timing}

* Changes to a decision policy and to the objects it uses can take up to 15 minutes to propagate across all data regions, and up to 30 minutes for Canada. This includes adding an item to a collection, changing a rule or the content of an item, and updating a formula.

* A capping counter can take up to 3 seconds to update. After you approve an item or create a capping rule, it can take up to 15 minutes before events are counted toward the cap.

## Troubleshooting checklist {#troubleshooting}

If a profile did not receive the item you expected, go through these checks:

1. **Dates and status.** Is the current date within the start and end dates of the decision item? Also check its status: you approve an item when it is ready to be presented to profiles. [Manage decision items](items.md#manage)

1. **Collection.** Does the collection used by the selection strategy contain the item? Select **[!UICONTROL Preview collection]** to list the items that match the collection rules. [Manage item collections](collections.md)

1. **Eligibility.** Does the profile meet the eligibility constraints of both the item and the selection strategy? Remember that audience membership might not be up to date. To test a decision rule, use **[!UICONTROL Simulate rule]**. [Learn how to simulate a rule](rules.md#simulate-rules)

1. **Capping.** Has a capping rule of the item reached its threshold? [Capping rules](items.md#capping)

1. **Order and number of items.** Do the strategies earlier in the sequence already provide all the items that the policy requests? Items of a group with a higher priority come before the items of later groups, whatever their score.

1. **Fallback.** Does the policy define fallback items? Without them, nothing is displayed when no item qualifies.

1. **Recent changes.** Did you change the policy or one of its objects in the last 15 minutes (30 minutes for Canada)? See [When do changes take effect?](#timing)

1. **Coworker.** Ask the [Decisioning Explainer](experience-decisioning-coworker-skills.md#decisioning-explainer) why an offer was or was not shown to a profile or segment. It is available to customers who have access to Coworker and Decisioning.

To measure how your items perform, see [Report on Decisioning](cja-reporting.md).

## Learn more {#learn-more}

* [How Decisioning works](how-decisioning-works.md)
* [Get started with Decisioning](gs-experience-decisioning.md)
* [Decisioning FAQ](decisioning-faq.md)
* [Decisioning guardrails & limitations](decisioning-guardrails.md)
* [Coworker for Decisioning](experience-decisioning-coworker-skills.md)
* [Report on Decisioning](cja-reporting.md)
