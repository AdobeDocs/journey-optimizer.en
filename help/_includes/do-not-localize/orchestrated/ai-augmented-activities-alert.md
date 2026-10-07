---
title: AI Knowledge Reference
---
# AI Knowledge Reference

+++ AI Knowledge Reference

This section contains structured knowledge intended to support interpretation, retrieval, and question answering related to this topic.

For complete understanding, this information should be combined with the documentation on this page. Neither source is intended to stand alone; the page describes the feature, while this section provides additional context that helps disambiguate terminology, intent, applicability, and constraints.

* **TL;DR:** The **[!UICONTROL Alert]** flow control activity notifies subscribers when Orchestrated campaign execution reaches the activity.

## Intents

* Configure a static alert title and message.
* Define a label to identify the activity on the canvas.
* Use a Test branch to notify subscribers when a query returns fewer than 10,000 profiles.

## Glossary

* **[!UICONTROL Alert]** *(product-specific)*: A **[!UICONTROL Flow control]** activity that notifies subscribers when campaign execution reaches it.
* **[!UICONTROL Label]**: The name that identifies the activity on the canvas.
* **[!UICONTROL Title]**: The required short, static plain-text title for the alert.
* **[!UICONTROL Message]**: The required static plain-text message that describes what subscribers need to know.
* **[!UICONTROL Test]** *(product-specific)*: The activity that evaluates the population count condition in the low population example.

## Guardrails

* The Alert activity has no independent trigger or condition configuration. Its position in the flow and upstream orchestration logic determine when it fires.
* **[!UICONTROL Title]** and **[!UICONTROL Message]** are required fields.
* The title and message are static. Dynamic tokens are not supported.
* The value of 10,000 in the low population example is a threshold configured in the Test activity, not a product limit.

## Terminology

* **Do not confuse:** The **[!UICONTROL Test]** activity evaluates a condition. The **[!UICONTROL Alert]** activity fires when execution reaches it.

## FAQ

* **What triggers an Alert activity?** Campaign execution reaching the activity triggers the alert. Upstream orchestration logic determines when it is reached.
* **Can the title or message contain dynamic tokens?** No. Both fields use static plain text, and dynamic tokens are not supported.
* **How can an alert depend on an audience condition?** Place it on the relevant Test branch. The Test activity evaluates the condition, not the Alert activity.

+++

<!-- ai-section-version: 4 | source-hash: 98730c60 -->