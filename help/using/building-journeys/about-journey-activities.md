---
solution: Journey Optimizer
product: journey optimizer
title: Get started with journey activities
description: Get started with journey activities
feature: Journeys, Activities, Overview
topic: Content Management
role: User
level: Beginner, Intermediate
keywords: journey, activities, get started, events, action
exl-id: 239b3d72-3be0-4a82-84e6-f219e33ddca4
version: Journey Orchestration
TQID: https://experienceleague.adobe.com/8M5qgoXuziyVXMHPOwiM3xztCSNmglc2fBu-BaXn9mc
product_v2:
  - id: cb954087-f4fc-4456-afb9-e939cabcdc79
    internal-label: Journey Optimizer
feature_v2:
  - id: b3538224-471e-4c63-a444-9b19d89ae29c
    internal-label: Activities
  - id: d998adac-2f81-400b-a669-d07bb196e4eb
    internal-label: Journeys
subfeature_v2:
  - id: b3a93754-a8b8-46eb-9421-7eccaeeb3dff
    internal-label: Best practices
  - id: b5e335a9-0e5f-4dda-8845-c4ac5dca2be4
    internal-label: Orchestration activities
  - id: cfba2953-2ce9-4b00-a00c-71cd338ae63f
    internal-label: Custom actions
  - id: d8353d85-5da7-453d-bd68-40ad33fa0ab7
    internal-label: Action activities
  - id: e57d1da4-32c2-4cc6-945c-9feb219156ff
    internal-label: Event activities
  - id: fa683eda-48de-4558-af32-2673edcd44fe
    internal-label: Events
  - id: e30b0a1a-b594-47b8-af94-1e3a2be6df11
    internal-label: Get started
role_v2:
  - id: b69b2659-1057-424e-8fc5-ed9e016dc554
    internal-label: User
level_v2:
  - id: b5a62a22-46f7-4f0d-b151-3fc640bef588
    internal-label: Intermediate
  - id: e8ccd51f-da0d-4e3b-939b-e30d5ebb1ea5
    internal-label: Beginner
topic_v2:
  - id: aa2f3246-cb95-4b30-8899-fdf7d73550cc
    internal-label: Reporting
  - id: bce87dde-a4ab-44c9-8a18-ad66e4ddb377
    internal-label: Customer experience
  - id: c1579802-ddd4-4214-8a91-97b2066abe11
    internal-label: Troubleshooting
---
# Get started with journey activities {#about-journey-activities}

>[!BEGINSHADEBOX]

**On this page:** Learn how to combine event, orchestration, and action activities to build multi-step, cross-channel journeys, with best practices for labeling activities, managing parameters, and troubleshooting.

>[!ENDSHADEBOX]

Combine event, orchestration, and action activities to build multi-step, cross-channel scenarios.

## Event activities {#event-activities}

Personalized journeys start with events such as an online purchase. Once a profile enters a journey, it moves through it on its own. Each profile can take a different path and pace. When you start with an event, the journey triggers when the event arrives. Each profile then follows the steps defined in your journey.

Events configured by the technical user (see [this page](../event/about-events.md)) appear in the first category of the palette. This category is on the left side of the screen. The following event activities are available:

* [General events](../building-journeys/general-events.md)
* [Reaction](../building-journeys/reaction-events.md)
* [Audience Qualification](../building-journeys/audience-qualification-events.md)

![Event activities palette in the journey designer](assets/journey43.png)

To start your journey, drag and drop an event activity. You can also double-click on it.

![Drag and drop event activity in the journey designer](assets/journey44.png)

## Orchestration activities {#orchestration-activities}

Orchestration activities are conditions that help determine the next step in the journey. These conditions can include whether the person has an open support case or completed a purchase. They can also include the local weather forecast or whether the person reached 10,000 loyalty points.

From the palette, on the left-hand side of the screen, the following orchestration activities are available:

* [Optimize](optimize.md)
* [Read Audience](read-audience.md)
* [Wait](wait-activity.md)
* [Journey Fragments](journey-fragments.md)
* [Content decision](content-decision.md)
* [Dataset lookup](dataset-lookup.md)

![Orchestration activities palette in the journey designer](assets/journey-orchestration-activities.png)

## Action activities {#action-activities}

Actions are what you want to happen as a result of some kind of trigger, like sending a message. It is the piece of the journey that the customer experiences.

From the palette on the left side of the screen, below **[!UICONTROL Events]** and **[!UICONTROL Orchestration]**, you can find the **[!UICONTROL Actions]** category. The following action activities are available:

* [Built-in channel actions](../building-journeys/journey-action.md) available from the **Action** activity
* [Custom actions](../building-journeys/using-custom-actions.md)
* [Jump](../building-journeys/jump.md)

![Action activities palette in the journey designer](assets/journey58.png)

These activities represent the different available communication channels. You can combine them to create a cross-channel scenario.

You can also set up specific actions to send messages:

* If you are using a third-party system to send messages, you can create a specific custom action. [Learn more](../action/action.md)

* If you are working with [!DNL Adobe Campaign] and [!DNL Adobe Journey Optimizer], refer to these sections:

   * [[!DNL Adobe Journey Optimizer] and [!DNL Adobe Campaign] v7/v8](../action/acc-action.md)
   * [[!DNL Adobe Journey Optimizer] and [!DNL Adobe Campaign] Standard](../action/acs-action.md)
   * [[!DNL Adobe Journey Optimizer] and [!DNL Adobe Marketo Engage]](../action/marketo-engage.md)

## Best practices {#best-practices}

Use these recommendations to keep journeys readable, consistent, and easy to troubleshoot.

### Add a label

Most activities allow you to define a **[!UICONTROL Label]**. This adds a suffix to the name that appears under your activity in the canvas. This is useful if you use the same activity several times in your journey and want to identify them more easily. It also makes debugging easier in case of errors and makes reports easier to read. You can also add an optional **[!UICONTROL Description]**.

![Label and Description fields in the journey activity properties](assets/journey-action-label.png)

>[!NOTE]
>
>For some activities, their ID is also visible in the pane. This ID can be used in reporting as a more stable key than the label, which can change.

### Manage the advanced parameters {#advanced-parameters}

Most activities display a number of advanced and/or technical parameters that you cannot modify.

![Advanced parameters fields in the journey activity properties](assets/journey-advanced-parameters.png)

For better readability, hide these parameters using the **[!UICONTROL Hide read-only fields]** button on top of the right pane.

![Hide read-only fields icon in the journey activity properties](assets/journey-hide-read-only-fields.png)

In some particular contexts, you can override the values of these parameters for specific use. To force a value, click the **[!UICONTROL Enable parameter override]** icon to the right of the field. [Learn more](../configuration/primary-email-addresses.md#override-execution-address-journey)

![Enable parameter override option in the Email activity properties](assets/journey-enable-parameter-override.png)

>[!NOTE]
>
>If the advanced parameters are hidden, click the **[!UICONTROL Show read-only fields]** button
>
>![Show read-only fields icon in the journey activity properties](assets/journey-show-read-only-fields.png){width=60%}

### Add an alternative path

When an error occurs in an action or a condition, the journey of an individual stops. The only way to make it continue is to check the box **[!UICONTROL Add an alternative path in case of a timeout or an error]**. See [this section](../building-journeys/using-the-journey-designer.md#paths)

![Add an alternative path option in the Condition activity properties](assets/journey42.png)

## Troubleshooting {#troubleshooting}

Before testing and publishing your journey, verify that all the activities are properly configured. You cannot perform tests or publications if errors are still detected by the system.

Learn how to troubleshoot errors in activities and in the journey [on this page](troubleshooting.md).

See also [Monitoring & troubleshooting](../../rp_landing_pages/troubleshoot-journey-landing-page.md)

+++ AI Knowledge Reference

This section contains structured knowledge intended to support interpretation, retrieval, and question answering related to this topic.

For complete understanding, this information should be combined with the documentation on this page. Neither source is intended to stand alone; the page describes the feature, while this section provides additional context that helps disambiguate terminology, intent, applicability, and constraints.

* **TL;DR:** This page introduces the three categories of journey activities — events, orchestration, and actions — and explains best practices for labeling, managing parameters, and handling errors in Adobe Journey Optimizer journeys.

**Intents:**
* Identify and distinguish between event, orchestration, and action activities in a journey
* Add labels and descriptions to journey activities for easier identification and reporting
* Configure an alternative path to handle timeouts or errors in a journey activity
* Override advanced parameters on a specific journey activity
* Combine multiple activity types to build cross-channel journey scenarios
* Troubleshoot activity configuration errors before publishing a journey

**Glossary:**
* **Event activity**: A journey activity triggered by an incoming event (e.g., purchase, audience qualification) that starts or advances a profile through the journey *(product-specific)*
* **Orchestration activity**: A journey activity (e.g., Optimize, Read Audience, Wait) that controls the flow and branching logic of a journey *(product-specific)*
* **Action activity**: A journey activity that delivers a communication or calls an external system as the result of a trigger *(product-specific)*
* **Custom action**: A user-configured action that connects Journey Optimizer to a third-party system for sending messages or data *(product-specific)*
* **Alternative path**: A fallback branch added to an activity so the journey continues even when a timeout or error occurs *(product-specific)*

**Guardrails:**
* Tests and publications cannot be performed if configuration errors are still detected in any activity
* Advanced/technical parameters on most activities are read-only and cannot be modified without using the parameter override feature

**Terminology:**
* Canonical name: Journey Activity — Acronym: none — variants: activity, node, step
* Synonyms: "action activity" = "channel action" = "message action"
* Do not confuse: "Orchestration activity" ≠ "Action activity" (orchestration controls flow; actions deliver communications)

**FAQ:**
* **Q: What is the difference between event, orchestration, and action activities?** — Event activities trigger journey entry or progression; orchestration activities control branching and flow logic; action activities deliver messages or call external systems.
* **Q: How do I add a label to a journey activity?** — Open the activity properties pane and fill in the Label field; the label appears as a suffix under the activity node on the canvas.
* **Q: What happens when an error occurs in an action or condition activity?** — The profile's journey stops unless you check the "Add an alternative path in case of a timeout or an error" option on that activity.
* **Q: Can I use Adobe Campaign to send messages from a journey?** — Yes, Journey Optimizer supports integration with Adobe Campaign v7/v8, Campaign Standard, and Marketo Engage for sending messages via custom action activities.
* **Q: How do I override a read-only advanced parameter on an activity?** — Click the "Enable parameter override" icon to the right of the parameter field to force a custom value.

+++
