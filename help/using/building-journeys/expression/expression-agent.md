---
solution: Journey Optimizer
product: journey optimizer
title: Generate expressions with the Expression Assistant
description: Learn how to use the Expression Assistant in Adobe Journey Optimizer to generate expressions directly in the Journey advanced expression editor using natural language prompts.
feature: Journeys
topic: Content Management
role: User
level: Intermediate
badge: label="Public beta" type="Informative"
mini-toc-levels: 2
feature_v2: []
subfeature_v2: []
---

# Generate expressions with the Expression Assistant {#expression-agent}

>[!CONTEXTUALHELP]
>id="journeyExpAI"
>title="Generate expressions with the Expression Assistant"
>abstract="The Expression Assistant uses generative AI to help you build and generate expressions directly in the Journey advanced expression editor. For example in conditions, **Optimize** activities, or **Wait** activities that use a custom date. When you describe what you need in plain language, the assistant generates the corresponding expression for you."

>[!AVAILABILITY]
>
>This feature is currently in **public beta**. For full details about the release cycle and availability phases, see [Journey Optimizer release cycle](../../rn/releases.md).
>
>Before using the Expression Assistant, read the related [Guardrails and Limitations](../../content-management/gs-generative.md#generative-guardrails) that apply to generative AI features in Journey Optimizer.

The Expression Assistant is an AI-powered feature built into the Journey advanced expression editor. It helps you generate valid expressions from plain language prompts.

It is available wherever the Journey **[!UICONTROL Advanced expression editor]** opens. For example, when you configure conditions and routing inside an **[Optimize activity](../optimize.md)**, or when you configure a [**[!UICONTROL Wait]** activity](../wait-activity.md) that uses a custom date and you need a `dateTimeOnly` expression.

## Generate an expression {#generate}

To generate an expression using the Expression Assistant:

1. Open the **[!UICONTROL Advanced expression editor]** in your journey, nfor example from a branching condition, an **[!UICONTROL Optimize]** activity, or a **[!UICONTROL Wait]** activity with a custom date.

   ![](../assets/expression-assistant-pane.png)

1. In the text field, describe the expression you want to generate in plain language. For example:

   * *"Users from USA and age greater than 18"*
   * *"Customers who have made a purchase in the last 30 days"*

   See [Example prompts](#example-prompts) at the end of this page for ideas.

1. Click **[!UICONTROL Generate]** to submit your prompt.

   The assistant starts generating the corresponding expression and displays progress status messages while generation is in progress.

   >[!NOTE]
   >
   >If the assistant cannot generate a valid expression (for example, if your prompt references fields that do not exist in available data sources), an error message appears. When this happens, revise your prompt to use field names and data sources that are available in your journey configuration, then generate again.

1. Once the expression is ready, review the result in the panel.

   ![](../assets/expression-assistant-result.png)

   * Click the ![Preview icon](../assets/do-not-localize/generation-preview.svg) icon before applying to review the assistant's output for the scenario you requested.

   * Click **[!UICONTROL Apply]** to insert the generated expression directly into the advanced expression editor (the same placement you would paste into manually).
   * Use the copy control to grab the suggested expression text and paste it elsewhere if needed.

## Example prompts {#example-prompts}

The lists below are prompt ideas only. They do not show generated expression syntax, the exact output depends on the fields and activities defined in your journey.

### Journey event and custom action {#example-prompts-event-action}

* *"event with order price total greater than 100"*
* *"event where the order was created in the last 7 days"*
* *"event where the event type is a commerce purchase"*
* *"event with order created in the last hour"*
* *"event with order price total over 200 and action response has a status code"*

### Wait activity expressions {#example-prompts-datetime}

When a **[!UICONTROL Wait]** activity uses a custom date, you define when the profile continues by building a `dateTimeOnly` expression in the **[!UICONTROL Advanced expression editor]**. For example from a profile attribute, an event timestamp, segment qualification data, or a calculated offset from the current time. For how to configure custom waits and applicable limits, see [Custom wait](../wait-activity.md#custom).

* *"use customer's last order date as date time only"*
* *"use consent email time as date time only"*
* *"convert segment membership last qualification time to date time only"*
* *"wait node: one week after Christmas 2024 as date time only"*
* *"wait node: 30 days from now at 10 PM as date time only"*
* *"wait until 9am today in UTC timezone, return as date time only"*

## Related resources {#related}

* [Work with the advanced expression editor](expressionadvanced.md) — Overview of the expression editor interface and supported syntax.
* [Get started with AI Assistant in Journey Optimizer](../../content-management/gs-generative.md) — General guardrails, access, and setup for generative AI features.

+++ AI Knowledge Reference

This section contains structured knowledge intended to support interpretation, retrieval, and question answering related to this topic.

For complete understanding, this information should be combined with the documentation on this page. Neither source is intended to stand alone; the page describes the feature, while this section provides additional context that helps disambiguate terminology, intent, applicability, and constraints.

* **TL;DR:** This page explains the Expression Assistant, an AI-powered feature in the Journey advanced expression editor that generates valid journey expressions from plain language prompts.

**Intents:**

* Generate a journey expression from a natural language description using the Expression Assistant
* Apply a generated expression directly into the advanced expression editor with the Apply button
* Use the Expression Assistant inside Optimize activities, Condition activities, and custom-date Wait activities
* Provide example prompts for event-based conditions and `dateTimeOnly` wait expressions
* Troubleshoot failed generation by revising prompts to reference valid field names and data sources

**Glossary:**

* **Expression Assistant**: An AI-powered generative feature embedded in the Journey advanced expression editor that converts plain language prompts into valid journey expressions *(product-specific)*
* **Advanced expression editor**: The Journey Optimizer interface for writing complex expressions in conditions, Wait activities, and action parameter mapping *(product-specific)*
* **dateTimeOnly**: A date-time expression type without timezone, required for custom-date Wait activities *(product-specific)*
* **Optimize activity**: A journey activity that supports branching conditions configurable via the advanced expression editor *(product-specific)*

**Guardrails:**

* The Expression Assistant is currently in **public beta** — availability and behavior may change
* Generative AI guardrails and limitations from the main AI Assistant documentation apply to this feature
* If the assistant references fields not present in your journey's data sources, it returns an error — revise the prompt to use available field names
* The exact generated expression syntax depends on the fields and activities configured in your specific journey

**Terminology:**

* Canonical name: Expression Assistant — Acronym: none — variants: Expression AI, journey expression generator
* Synonyms: "Expression Assistant" = "AI expression generator"
* Do not confuse: Expression Assistant (AI-powered generator) ≠ Advanced expression editor (the manual code editor itself)

**FAQ:**

* **Q: Where is the Expression Assistant available?** — It is available wherever the Journey advanced expression editor opens, including Condition activities, Optimize activities, and Wait activities with a custom date.
* **Q: What happens if the assistant cannot generate a valid expression?** — An error message appears; you should revise your prompt to use field names and data sources that exist in your journey configuration.
* **Q: How do I insert a generated expression into the editor?** — Click the **Apply** button in the assistant panel to insert it directly at the current cursor position in the advanced expression editor.
* **Q: Can the Expression Assistant generate `dateTimeOnly` expressions for Wait activities?** — Yes; for example prompting "30 days from now at 10 PM as date time only" generates the appropriate `dateTimeOnly` expression.
* **Q: Is the Expression Assistant generally available?** — No; it is currently in public beta. Check the Journey Optimizer release cycle page for availability updates.

+++
