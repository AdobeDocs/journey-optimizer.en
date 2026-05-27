---
solution: Journey Optimizer, Experience Platform
product: Journey Optimizer
title: Decision management guardrails & limitations
description: Learn more about Decision management guardrails & limitations.
badge: label="Legacy" type="Informative"
feature: Decision Management
role: User
level: Intermediate
exl-id: d2872bd3-42f8-4744-bb5b-41c49340098a
version: Journey Orchestration
TQID: https://experienceleague.adobe.com/teZQ3GKXJoj05ZD7bCCzKSzwLdUbgF8DXp8csDostOw
product_v2:
  - id: cb954087-f4fc-4456-afb9-e939cabcdc79
    internal-label: Journey Optimizer
feature_v2:
  - id: ad78185d-8f79-40ad-9bad-cbde74af74ee
    internal-label: Guardrails and limitations
  - id: a4cb03e1-327e-499d-9de8-e0c0db8a63a2
    internal-label: Decision capabilities (AJO)
subfeature_v2:
  - id: a7a194a0-75e2-4913-8a83-14714fbf68e6
    internal-label: Decisioning API
  - id: eb547372-2a95-4d13-b0fd-f720c9895880
    internal-label: Edge Decisioning (AJO)
role_v2:
  - id: b69b2659-1057-424e-8fc5-ed9e016dc554
    internal-label: User
level_v2:
  - id: b5a62a22-46f7-4f0d-b151-3fc640bef588
    internal-label: Intermediate
---
# Decision management guardrails & limitations {#decision-management-guardrails}

>[!IMPORTANT]
>
>This page covers guardrails for the legacy **Decision Management** capability. If you are using **Decisioning** — [!DNL Adobe Journey Optimizer]'s current decisioning capability available via code-based experience and email channels — refer to [Decisioning guardrails & limitations](../experience-decisioning/decisioning-guardrails.md) instead.
>
>Not sure which capability you are using? [Learn about Decisioning](../experience-decisioning/gs-experience-decisioning.md).

This page applies to users still working with the legacy Decision Management system. To ensure optimal use, keep the following guardrails and limitations in mind.

The complete list of [!DNL Journey Optimizer] guardrails & limitations is available in [this section](../start/guardrails.md).

## Decision requests

The delivery throughput corresponds to the number of decision responses that can be delivered by the Decision Management app service in a specified amount of time.

| Guardrail | Limit |
| ------- | ------- |
| Decisioning API requests per second | 500 per Organization |
| Edge Decisioning API requests per second with Edge Segmentation | 1,500 per Organization |
| Edge Decisioning API requests per second without Edge segmentation | 5,000 per Organization |
| Offers Returned per response |Up to 30 per decision scope or 100 in total |
| Max number of offer rules involved per request | 100 |

## Decisions

| Guardrail | Limit |
| ------- | ------- |
| Total decisions | 10K |
| Live decisions | 1K |
| Placements per decision | 30 |

## Collections

| Guardrail | Limit |
| ------- | ------- |
| Offers per collection | 500 |
| Collections | 10K |
| Collections per decision | 30 |

## Collection qualifiers

| Guardrail | Limit |
| ------- | ------- |
| Collection qualifier per offer or collection | 20 |
| Total collection qualifiers | 1,000 |

## Offers

| Guardrail | Limit |
| ------- | ------- |
| Total offers | 10K |
| Max number of **active** offers per sandbox | 10K |
| Max size of offers including attributes (1KB), max of 30 attributes | 1KB |
| Max offer representation size (total for all placements) | 1KB |

## Eligibility rules

| Guardrail | Limit |
| ------- | ------- |
| Total decision rules and ranking formulas | 10K combined |
| Max number of profile attributes per rule | 25 |
| Max number of context data attributes per rule | 30 |
| Max size of PQL rule | 15K (UTF-8) |
| Max number of nesting levels | 30|

## Ranking formulas

| Guardrail | Limit |
| ------- | ------- |
| Max size of ranking formula PQL | 8K (UTF-8) |
| Max number of profile attributes | 25 |
| Max number of context data attributes | 30 |
| Max number of nesting levels | 30|

## Others

| Guardrail | Limit |
| ------- | ------- |
| Placements | 1000 |
| AI ranking model | 5 |
| Frequency Capping - Max number of capping rules per offer | 10 |

## Configurations {#configurations}

The total number of configurations that Decision management supports cannot exceed 20,000.

The total configuration count is the total number of [capping rules](offer-library/add-constraints.md#capping) that exist in your sandbox. For each capping rule that is applied across all [placements](offer-library/creating-placements.md), the rule must be multiplied across all placements associated with the specified offer.
