---
product: experience platform
solution: Experience Platform
title: Get started with context data
description: Learn how to leverage context data in decision management.
feature: Decision Management
role: Developer, Data Engineer
level: Experienced
exl-id: 4e736f9d-0f05-4a79-8ebf-ea22517d78a9
---
# Get started with context data {#context-data}

Data sent as part of the decisioning request is considered as context data. You can leverage context data in the decisioning engine, for example to design a decision rule that requires the current weather to be ≥80 degrees at the time the decision request is made.

Context data is defined differently between **Decisioning** and **Edge Decisioning** API requests. For both types of requests, context data can be used in eligibility rules or in ranking formulas, but only Edge Decisioning API requests can use context data to personalize content. 

Before starting, check the following guardrails & limitations:

* Because of different way of passing context between Decisioning and Edge Decisioning calls, context-based eligibility rules and ranking formulas are not interchangeable between Decisioning and Edge Decisioning calls.
* Testing with the `dryrun` parameter is possible with the Decisioning API only. It is not available with the Edge Decisioning API. Note that setting this parameter to `true` with the Decisioning API does not impact caps and the number of propositions.

Detailed information on how to use context data in each API, refer to these sections:

* [Use context data in Edge Decisioning requests](context-data-edge.md)
* [Use context data in Decisioning requests](context-data-decisioning.md)
