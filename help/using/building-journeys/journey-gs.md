---
solution: Journey Optimizer
product: journey optimizer
title: Create your first journey
description: Key steps to build your first journey with [!DNL Adobe Journey Optimizer]
feature: Journeys, Get Started
topic: Content Management
role: User
level: Intermediate
keywords: journey, first, start, quick-start, audience, event, action
exl-id: d940191e-8f37-4956-8482-d2df0c4274aa
version: Journey Orchestration
TQID: https://experienceleague.adobe.com/7zNDOi2SUTyttgR6I1iOYQb61ejxpqLYznweU8alnPw
product_v2:
  - id: cb954087-f4fc-4456-afb9-e939cabcdc79
    internal-label: Journey Optimizer
feature_v2:
  - id: ad78185d-8f79-40ad-9bad-cbde74af74ee
    internal-label: Guardrails and limitations
  - id: b3538224-471e-4c63-a444-9b19d89ae29c
    internal-label: Activities
  - id: d998adac-2f81-400b-a669-d07bb196e4eb
    internal-label: Journeys
subfeature_v2:
  - id: b15c7c2e-788c-4eb7-86a8-390565b0d2c9
    internal-label: Journey design
  - id: a6c67b0d-bd3e-4d5d-95a8-882e3709d632
    internal-label: Journey guardrails
role_v2:
  - id: b69b2659-1057-424e-8fc5-ed9e016dc554
    internal-label: User
level_v2:
  - id: b5a62a22-46f7-4f0d-b151-3fc640bef588
    internal-label: Intermediate
topic_v2:
  - id: aa2f3246-cb95-4b30-8899-fdf7d73550cc
    internal-label: Reporting
  - id: b5520579-b31f-4df7-9281-f0d9f91e2edc
    internal-label: Customer engagement
  - id: c1579802-ddd4-4214-8a91-97b2066abe11
    internal-label: Troubleshooting
  - id: d00e9f03-e50b-4162-b143-0c0817c937c2
    internal-label: Customer journeys
  - id: e1e0219c-f879-479f-8427-888ed2a6e9c2
    internal-label: Insights
---
# Create your first journey {#jo-quick-start}

>[!BEGINSHADEBOX]

**On this page:** Learn the key steps to build your first journey in Adobe Journey Optimizer, from defining the entry audience or event to adding actions and publishing it live.

>[!ENDSHADEBOX]

>[!CONTEXTUALHELP]
>id="ajo_homepage_card2"
>title="Create journeys"
>abstract="**[!DNL Adobe Journey Optimizer]** builds real-time orchestration use cases using contextual data stored in events or data sources."

>[!CONTEXTUALHELP]
>id="ajo_journey_create"
>title="Journeys"
>abstract="Customer journeys deliver personalized, contextual experiences. Journey Optimizer allows you to build real-time orchestration use cases with contextual data stored in events or data sources. The **Overview** tab displays a dashboard with key metrics related to your journeys. The **Browse** tab displays the list of existing journeys."

[!DNL Adobe Journey Optimizer] includes an omnichannel orchestration canvas which allows marketers to harmonize marketing outreach with one-to-one customer engagement. The user interface allows you to easily drag and drop activities from the palette into the canvas to build your journey. The journey user interface is detailed on [this page](journey-ui.md).

![sample of journey canvas](assets/journey38.png)

The main steps to create a journey are detailed on this page. They are streamlined as follows:

![journey creation steps: create, design, test, and publish](assets/journey-creation-process.png)

In this guide, you will:

* Define a journey entry point — an audience segment or a real-time event
* Add message actions across channels — email, push, SMS, in-app, web, code-based experience, content card, and more. [See supported channels](journey-action.md)
* Test your journey with test profiles before activation
* Publish your journey and monitor its performance

Build multi-step customer journeys to initiate a sequence of interactions, offers, and messages across channels in real time. This approach ensures customers are engaged at the optimal moments based on their actions and relevant business signals.

<!--
>[!TIP]
>
>Not sure whether to use a journey or a campaign? [Learn how to choose the right approach](../start/journeys-vs-campaigns.md).
-->

## Before you start {#prerequisites}

What you need to configure before building depends on how your journey is triggered. Most journeys start from one of these two entry points:

* **Audience-based entry** — The journey runs for a defined set of profiles at a scheduled time. [Create an audience](../audience/about-audiences.md) in Adobe Experience Platform before building your journey. This is the recommended starting point if you are new to Journey Optimizer.

* **Event-based entry** — The journey is triggered in real time when an individual performs an action, such as a purchase or a sign-up. [Configure an event](../event/about-events.md) to define the trigger and the data it carries.

**Not sure which entry point to use?** The table below maps the most common use cases to the right starting activity.

| Entry point | Use when… | Profiles enter |
|---|---|---|
| **[Read Audience](read-audience.md)** | You want to send a scheduled or recurring message to a defined set of profiles (newsletters, promotions, onboarding series). | All profiles from a batch audience, at once or on a schedule. |
| **[Audience Qualification](audience-qualification-events.md)** | You need to react in real time when a profile enters or exits an audience (loyalty tier upgrade, churn risk flag). | One profile at a time, as soon as they qualify in a streaming audience. |
| **Unitary event** | A profile action triggers an immediate response (purchase confirmation, form submission, app login). | One profile at a time, in real time. |
| **[Business event](../event/about-creating-business.md)** | A non-profile event affects multiple people at once (flight cancellation, stock replenishment, breaking news alert). | All profiles associated with the event, via an automatic Read Audience step. |

The following elements are optional, but may be required depending on your use case:

* **Data source** — To enrich journey conditions or personalization with data from an external system, set up a [data source](../datasource/about-data-sources.md).

* **Custom action** — If you deliver messages through a third-party system rather than the built-in channels, configure a [custom action](../action/action.md).

>[!NOTE]
>
>* If you are a data engineer responsible for the technical setup (events, data sources, and actions), refer to [this section](../configuration/about-data-sources-events-actions.md).
>
>* Journey guardrails and limitations are detailed on [this page](../start/guardrails.md).

## Create a journey {#jo-build}

To create a multi-step journey, follow these steps:

1. In the JOURNEY MANAGEMENT menu section, click **[!UICONTROL Journeys]**.

1. Click the **[!UICONTROL Create Journey]** button to create a new journey.

1. Edit the journey's configuration pane to define the name of the journey and set its properties. Learn how to set your journey's properties on [this page](journey-properties.md).

   >[!TIP]
   >
   >**Which journey type should I choose?** If you are new to Journey Optimizer, start with an audience-based journey using a **[!UICONTROL Read Audience]** activity — it requires no prior event configuration and is the easiest way to get familiar with the canvas. For real-time, event-triggered experiences (for example, reacting to a purchase or a form submission), configure an event first and use an event-based entry. Ready to go deeper? [Discover all journey types and their entry rules](entry-management.md#types-of-journeys).

    ![Journey properties panel with settings and configuration options](assets/jo-properties.png)

You can then start designing your journey.

## Design the journey {#jo-design}

The journey designer lets you build multi-step journeys using an intuitive drag-and-drop interface. Activities in the left palette are organized into three categories: **Events**, **Orchestration**, and **Actions**. For a full overview of the canvas and its controls, refer to [this page](using-the-journey-designer.md).

![Journey designer interface with activities palette and canvas](assets/journey38.png)

Follow these steps to design your journey:

1. **Add an entry point** — Drag an event or a **[!UICONTROL Read Audience]** activity from the palette onto the canvas. This defines how profiles enter the journey: individually in real time (event-based) or all at once from a defined audience (audience-based).

    ![Read Audience activity configuration for selecting target audience](assets/read-segment.png)

1. **Add message actions** — From the **[!UICONTROL Actions]** section of the palette, drag a channel action onto the canvas to send messages to profiles flowing through the journey. Actions are available for email, push notifications, SMS, and more.

1. **Add orchestration activities** — Use a **[!UICONTROL Condition]** activity to branch the journey into multiple paths based on profile attributes or behavior. Use a **[!UICONTROL Wait]** activity to introduce a time delay between steps.

>[!TIP]
>
>For journeys with multiple phases or many touchpoints, consider breaking the end-to-end flow into smaller sub-journeys connected with the **[!UICONTROL Jump]** activity. This reduces complexity and makes each sub-journey easier to test independently. Learn more in [Design strategy: bite-sized sub-journeys](jump.md#jump-strategy).

## Test the journey {#jo-test}

Once you have built your journey, test it before publishing. Journey Optimizer offers a **Test mode** as a way to view test profiles as they move along the journey, detecting potential errors before activation. Running quick tests ensures that journeys operate correctly so that you can publish them with confidence. Learn how to test your journey [in this section](testing-the-journey.md)

You can also execute your journey in **Dry run**. Journey Dry run is a special journey publication mode in Adobe Journey Optimizer that allows journey practitioners to test a journey using real production data without contacting real customers or updating profile information. This feature helps journey practitioners gain confidence in their journey design and audience targeting before publishing it live. Learn how to publish a journey in Dry run mode [in this section](journey-dry-run.md).

## Publish the journey {#jo-pub}

You must publish a journey to activate it and make it available for new profiles to enter it. Before publishing your journey, verify that it is valid and that there are no errors. You cannot publish a journey with errors. Learn more about journey publication in this [section](publish-journey.md).

![Complete journey flow with audience, conditions, and actions](assets/jo-journeyuc2_32bis.png)

Once published, you can monitor your journey using the dedicated reporting tools to measure your journey's effectiveness. 

![Journey analytics report showing performance metrics and statistics](assets/jo-dynamic_report_journey_12.png)

Learn more about journey reports in this [section](../reports/live-report.md).

## Common use cases {#use-cases}

Not sure where to start? Here are three typical scenarios where journeys deliver the most value:

<table style="table-layout:fixed">
  <tr style="border: 0;">
    <td>
      <a href="https://experienceleague.adobe.com/en/docs/journey-optimizer-learn/tutorials/use-cases/customer-onboarding" target="_blank">
        <img src="../assets/do-not-localize/icon-quick-start.svg" width="35px">
      </a>
      <div><strong>Welcome series</strong><br/>Automatically onboard new users with a sequence of messages after sign-up, guiding them through your product or service.</div>
    </td>
    <td>
      <a href="https://experienceleague.adobe.com/en/docs/journey-optimizer-learn/tutorials/use-cases/abandoned-cart" target="_blank">
        <img src="../assets/do-not-localize/icon-campaign.svg" width="35px">
      </a>
      <div><strong>Cart abandonment</strong><br/>Re-engage customers who left without completing a purchase by sending a timely reminder with personalized content.</div>
    </td>
    <td>
      <a href="jo-use-cases.md">
        <img src="../assets/do-not-localize/icon-content.svg" width="35px">
      </a>
      <div><strong>Re-engagement</strong><br/>Win back inactive users with targeted offers or updates based on their last known behavior.</div>
    </td>
  </tr>
  <tr style="border: 0;">
    <td align="center"><a href="https://experienceleague.adobe.com/en/docs/journey-optimizer-learn/tutorials/use-cases/customer-onboarding" target="_blank"><img src="../assets/do-not-localize/learn-more-button.svg"></a></td>
    <td align="center"><a href="https://experienceleague.adobe.com/en/docs/journey-optimizer-learn/tutorials/use-cases/abandoned-cart" target="_blank"><img src="../assets/do-not-localize/learn-more-button.svg"></a></td>
    <td align="center"><a href="jo-use-cases.md"><img src="../assets/do-not-localize/learn-more-button.svg"></a></td>
  </tr>
</table>

## Additional resources

* **[Journey types and profile entry](entry-management.md)** - Understand all journey types (unitary event, business event, read audience, audience qualification) and how profiles enter, re-enter, and flow through journeys.
* **[Journey designer overview](using-the-journey-designer.md)** - Master the journey canvas interface to design and orchestrate customer journeys.
* **[Journey activities](about-journey-activities.md)** - Discover all available activities including events, actions, and orchestration components.
* **[Testing journeys](testing-the-journey.md)** - Learn how to test your journeys using test mode before publishing to production.
* **[Publishing journeys](publish-journey.md)** - Understand the journey publication process and how to manage live journeys.
* **[Journey reporting](report-journey.md)** - Track and analyze journey performance with detailed metrics and insights.
* **[Troubleshooting journeys](troubleshooting.md)** - Find solutions to common journey issues and best practices for debugging.
* **[Journey tutorials](https://experienceleague.adobe.com/en/docs/journey-optimizer-learn/tutorials/journeys/introduction-to-building-a-journey){target="_blank"}** - Explore step-by-step video tutorials on journey building and best practices.

+++ AI Knowledge Reference

This section contains structured knowledge intended to support interpretation, retrieval, and question answering related to this topic.

For complete understanding, this information should be combined with the documentation on this page. Neither source is intended to stand alone; the page describes the feature, while this section provides additional context that helps disambiguate terminology, intent, applicability, and constraints.

* **TL;DR:** This page walks through the four key steps to create a first journey in Adobe Journey Optimizer — defining an entry point, designing the canvas, testing with test mode or Dry run, and publishing — along with guidance on choosing the right entry type.

**Intents:**
* Create a new journey and configure its properties in the Journey Management menu
* Choose the correct entry point (Read Audience, Audience Qualification, unitary event, or business event) for a given use case
* Design a multi-step journey by dragging and dropping events, orchestration activities, and channel actions onto the canvas
* Test a journey using Test mode with synthetic test profiles before publishing
* Execute a Dry run to validate audience targeting with real production data without contacting customers
* Publish a journey to make it live and monitor its performance with reporting tools

**Glossary:**
* **Read Audience**: An entry activity that processes all profiles in a batch audience at once or on a schedule *(product-specific)*
* **Audience Qualification**: An entry activity triggered in real time when a profile enters or exits a streaming audience *(product-specific)*
* **Unitary event**: A real-time trigger that enters one profile at a time into a journey when a specific action occurs *(product-specific)*
* **Business event**: A non-profile event (e.g., flight cancellation, stock replenishment) that triggers a journey for multiple profiles simultaneously via an automatic Read Audience step *(product-specific)*
* **Test mode**: A validation mode that uses synthetic test profiles to simulate journey execution without activating live communications *(product-specific)*
* **Dry run**: A special publication mode that uses real production data to validate journey logic without contacting actual customers or updating profiles *(product-specific)*

**Guardrails:**
* A journey cannot be published if it contains errors; all errors must be resolved first
* Event configuration (for event-based entry) must be completed by a data engineer before the journey can be built
* Journey guardrails and limitations are documented separately and should be reviewed before designing at scale
* Audience creation in Adobe Experience Platform is a prerequisite for audience-based journeys

**Terminology:**
* Canonical name: Journey — Acronym: none — variants: customer journey, orchestration flow
* Synonyms: "Test mode" = "journey testing"; "Dry run" = "dry run mode"
* Do not confuse: "Test mode" ≠ "Dry run" — test mode uses synthetic profiles; dry run uses real production data without contacting customers

**FAQ:**
* **Q: What is the first thing I need to do before creating an event-triggered journey?** — Configure the event with a data engineer to define the trigger and the data it carries; then reference the event as the journey entry point.
* **Q: Which entry point is recommended for someone new to Journey Optimizer?** — Start with an audience-based journey using a Read Audience activity — it requires no prior event configuration and is the easiest way to get familiar with the canvas.
* **Q: Can I test my journey before it goes live?** — Yes; use Test mode with synthetic test profiles to step through the journey, or use Dry run to execute against real production data without sending any communications.
* **Q: What happens if my journey has errors when I try to publish?** — You cannot publish a journey with errors; all configuration errors must be resolved before publication.
* **Q: How do I break up a complex journey with many steps?** — Use the Jump activity to connect smaller sub-journeys, reducing complexity and making each sub-journey easier to test independently.

+++
