---
title: Decisioning guardrails & limitations
description: Learn more about Decisioning guardrails & limitations.
feature: Decisioning
role: User
level: Intermediate
exl-id: 73548973-ff8d-4d6c-b383-dd3679fa159a
version: Journey Orchestration
TQID: https://experienceleague.adobe.com/oTljriepwffzR-LIAc2kWjTQx9Oj0QMgJpbghkSEsmY
product_v2:
  - id: cb954087-f4fc-4456-afb9-e939cabcdc79
    internal-label: Journey Optimizer
feature_v2:
  - id: ad78185d-8f79-40ad-9bad-cbde74af74ee
    internal-label: Guardrails and limitations
  - id: a4cb03e1-327e-499d-9de8-e0c0db8a63a2
    internal-label: Decision capabilities
role_v2:
  - id: b69b2659-1057-424e-8fc5-ed9e016dc554
    internal-label: User
level_v2:
  - id: b5a62a22-46f7-4f0d-b151-3fc640bef588
    internal-label: Intermediate
subfeature_v2:
  - id: a7a194a0-75e2-4913-8a83-14714fbf68e6
    internal-label: Decisioning API
  - id: eb547372-2a95-4d13-b0fd-f720c9895880
    internal-label: Edge Decisioning
---
# Decisioning guardrails & limitations {#decisioning-guardrails}

>[!BEGINSHADEBOX]

**On this page:** Review the guardrails and limits that apply to Decisioning across decision requests, items, policies, eligibility rules, and ranking formulas, so you can design decisioning configurations that stay within supported thresholds.

>[!ENDSHADEBOX]

To ensure optimal use of Decisioning, keep the following guardrails and limitations in mind.

The complete list of [!DNL Journey Optimizer] guardrails & limitations is available in [this section](../start/guardrails.md).

## Decision requests {#decision-requests}

| Guardrail | Limit |
| ------- | ------- |
| Code-based experience API request with decision policy using Edge segmentation | 1500 |
| Code-based experience API request with decision policy not using Edge segmentation | 5000 |
| Max number of Surface URIs per Edge decisioning request | 30 |

## Decision items {#decision-items}

| Guardrail | Limit |
| ------- | ------- |
| Total decision items | 10K |
| Max size of items including attributes (1KB), max of 30 attributes | 1KB |
| Frequency rules - Max number of capping rules per decision item | 10 |
| Max number of AEM Content Fragments per decision item | 5 |

## Item collections {#item-collections}

| Guardrail | Limit |
| ------- | ------- |
| Items collections | 10K |
| Total decision items per collection | 500 |

## Decision policy {#decision-policy}

| Guardrail | Limit |
| ------- | ------- |
| Number of selection strategies and manual items per decision policy | 10 |
| Max decision items returned per decision policy | 30 |
| Max decision policies per email | 10 |

## Eligibility rules {#eligibility-rules}

| Guardrail | Limit |
| ------- | ------- |
| Total Decision Rules and Ranking Formulas | 10K combined |
| Max number of profile attributes per rule | 25 |
| Max number of context data attributes per rule | 30 |
| Max size of pql rule | 15K (UTF-8) |
| Max number of nesting levels | 30 |

## Ranking formulas {#ranking-formulas}

| Guardrail | Limit |
| ------- | ------- |
| Max size of ranking formula PQL | 8K (UTF-8) |
| Max number of profile attributes |25 |
| Max number of context data attributes | 30 |
| Max number of nesting levels | 30 |

## Others {#others}

| Guardrail | Limit |
| ------- | ------- |
| Number of custom attributes per items catalog schema | 100 |
| Total Placements | 1K |
| AI Ranking Model | 5 |

## Configurations {#configurations}

The total number of configurations that Decisioning supports cannot exceed 20,000.

The total configuration count is the total number of [capping rules](items.md#capping) that exist in your sandbox.
