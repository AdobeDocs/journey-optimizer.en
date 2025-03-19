---
title: Decisioning guardrails & limitations
description: Learn more on Decisioning guardrails & limitations.
feature: Decisioning
role: User
level: Intermediate
exl-id: 73548973-ff8d-4d6c-b383-dd3679fa159a
---
# Decisioning guardrails & limitations {#decisioning-guardrails}

To ensure optimal use of Decisioning, keep the following guardrails and limitations in mind.

The complete list of [!DNL Journey Optimizer] guardrails & limitations is available in [this section](../start/guardrails.md).

## Decision requests

| Guardrail | Limit |
| ------- | ------- |
| Code-based experience API request with decision policy utilizing Edge segmentation | 1500 |
| Code-based experience API request with decision policy not utilizing Edge segmentation | 5000 |

## Item collections

| Guardrail | Limit |
| ------- | ------- |
| Items collections | 10K |
| Total offer items per item collection | 500 |

## Decision policy

| Guardrail | Limit |
| ------- | ------- |
| Number of selection strategies and manual items per decision policy | 10 |
| Max offer items returned per decision policy | 30 |

## Eligibility rules

| Guardrail | Limit |
| ------- | ------- |
| Total Decision Rules and Ranking Formulas | 10K combined |
| Max number of profile attributes per rule | 25 |
| Max number of context data attributes per rule | 30 |
| Max size of pql rule | 15K (UTF-8) |
| Max number of nesting levels | 30 |

## Ranking formulas

| Guardrail | Limit |
| ------- | ------- |
| Max size of ranking formula PQL | 8K (UTF-8) |
| Max number of profile attributes |25 |
| Max number of context data attributes | 30 |
| Max number of nesting levels | 30 |

## Others

| Guardrail | Limit |
| ------- | ------- |
| Number of custom attributes per Offers catalog schema | 100 |
| Total Offer Items | 10K |
| Total Placements | 1K |
| AI Ranking Model | 5 |
| Frequency rules - Max number of capping rules per offer | 10 |
