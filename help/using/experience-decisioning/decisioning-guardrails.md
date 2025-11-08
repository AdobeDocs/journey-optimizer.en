---
title: Decisioning guardrails & limitations
description: Learn more about Decisioning guardrails & limitations.
feature: Decisioning
role: User
level: Intermediate
exl-id: 73548973-ff8d-4d6c-b383-dd3679fa159a
---
# Decisioning guardrails & limitations {#decisioning-guardrails}

To ensure optimal use of Decisioning, keep the following guardrails and limitations in mind.

The complete list of [!DNL Journey Optimizer] guardrails & limitations is available in [this section](../start/guardrails.md).

## Decision requests {#decision-requests}

|| Guardrail | Limit |
|| ------- | ------- |
|| Code-based experience API request with decision policy using Edge segmentation | 1500 |
|| Code-based experience API request with decision policy not using Edge segmentation | 5000 |
|| Max number of Surface URIs per Edge decisioning request | 30 |

## Item collections {#item-collections}

|| Guardrail | Limit |
|| ------- | ------- |
|| Items collections | 10K |
|| Total offer items per item collection | 500 |

## Decision policy {#decision-policy}

|| Guardrail | Limit |
|| ------- | ------- |
|| Number of selection strategies and manual items per decision policy | 10 |
|| Max offer items returned per decision policy | 30 |

## Eligibility rules {#eligibility-rules}

|| Guardrail | Limit |
|| ------- | ------- |
|| Total Decision Rules and Ranking Formulas | 10K combined |
|| Max number of profile attributes per rule | 25 |
|| Max number of context data attributes per rule | 30 |
|| Max size of pql rule | 15K (UTF-8) |
|| Max number of nesting levels | 30 |

## Ranking formulas {#ranking-formulas}

|| Guardrail | Limit |
|| ------- | ------- |
|| Max size of ranking formula PQL | 8K (UTF-8) |
|| Max number of profile attributes |25 |
|| Max number of context data attributes | 30 |
|| Max number of nesting levels | 30 |

## Others {#others}

|| Guardrail | Limit |
|| ------- | ------- |
|| Number of custom attributes per Offers catalog schema | 100 |
|| Total Offer Items | 10K |
|| Total Placements | 1K |
|| AI Ranking Model | 5 |
|| Frequency rules - Max number of capping rules per offer | 10 |

## Configurations {#configurations}

The total number of configurations that Decisioning supports cannot exceed 20,000.

The total configuration count is the total number of [capping rules](items.md#capping) that exist in your sandbox.
