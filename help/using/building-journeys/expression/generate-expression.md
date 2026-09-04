---
solution: Journey Optimizer
product: journey optimizer
title: Generate expressions with AI
description: Learn how to use AI in Adobe Journey Optimizer to generate expressions directly in the Journey advanced expression editor using natural language prompts.
feature: Journeys
topic: Content Management
role: User
level: Intermediate
mini-toc-levels: 2
feature_v2: []
subfeature_v2: []
---

# Generate expressions with AI {#generate-expression}

>[!CONTEXTUALHELP]
>id="journeyExpAI"
>title="Generate expressions with AI"
>abstract="Use AI to build and generate expressions directly in the Journey advanced expression editor. For example in conditions, **Optimize** activities, or **Wait** activities that use a custom date. When you describe what you need in plain language, AI generates the corresponding expression for you."

>[!IMPORTANT]
>
>Before using this capability, read the related [Guardrails and Limitations](../../content-management/gs-generative.md#generative-guardrails) that apply to generative AI features in Journey Optimizer.

This AI-powered capability, built into the Journey advanced expression editor, helps you generate valid expressions from plain language prompts.

It is available wherever the Journey **[!UICONTROL Advanced expression editor]** opens. For example, when you configure conditions and routing inside an **[Optimize activity](../optimize.md)**, or when you configure a [**[!UICONTROL Wait]** activity](../wait-activity.md) that uses a custom date and you need a `dateTimeOnly` expression.

## Generate an expression {#generate}

To generate an expression with AI:

1. Open the **[!UICONTROL Advanced expression editor]** in your journey, for example from a branching condition, an **[!UICONTROL Optimize]** activity, or a **[!UICONTROL Wait]** activity with a custom date.

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

### Audience membership prompts {#example-prompts-audience}

Describe the audience membership check you want to make in plain language. For example:

* *"check to see if profile is in the Gold Loyalty audience"*

## Related resources {#related}

* [Work with the advanced expression editor](expressionadvanced.md) — Overview of the expression editor interface and supported syntax.
* [Get started with Generate Content in Journey Optimizer](../../content-management/gs-generative.md) — General guardrails, access, and setup for generative AI features.

{{$include /help/_includes/do-not-localize/building-journeys/ai-knowledge-reference-expression-generate-expression.md}}
