---
title: Decision management guardrails & limitations
description: Learn more on Decision management guardrails & limitations.
feature: Decisioning
role: User
level: Intermediate
---

# Decision management guardrails & limitations {#decision-management-guardrails}

To ensure optimal use of Decision management, keep the following guardrails and limitations in mind.

The complete list of [!DNL Journey Optimizer] guardrails & limitations is available in [this section](../start/guardrails.md).

## Decision requests

The delivery throughput corresponds to the number of decision responses that can be delivered by the Decision Management app service in a specified amount of time.

| Guardrail | Limit |
| ------- | ------- |
| Decisioning API requests per second | 500 |
| Edge Decisioning API requests per second with Edge Segmentation | 1500 |
| Edge Decisioning API requests per second without Edge segmentation | 5000 |
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
| Total collection qualifiers | 1000 |

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
