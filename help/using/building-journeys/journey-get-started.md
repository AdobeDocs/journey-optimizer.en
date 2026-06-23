---
solution: Journey Optimizer
product: journey optimizer
title: Journey Orchestration - Complete guide
description: Comprehensive guide to get started with journey orchestration in [!DNL Adobe Journey Optimizer]
feature: Journeys, Get Started, Overview
role: User
level: Beginner, Intermediate
hide: true
keywords: journey, orchestration, getting started, onboarding, capabilities
exl-id: 96b1d619-986d-493d-a73b-d7c63b92cca8
TQID: https://experienceleague.adobe.com/Ht6fS6uanOs-rXoT4bAnK6eGvm9kOmH-N5B-y8KU6Rc
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
  - id: b3a93754-a8b8-46eb-9421-7eccaeeb3dff
    internal-label: Best practices
role_v2:
  - id: b69b2659-1057-424e-8fc5-ed9e016dc554
    internal-label: User
level_v2:
  - id: b5a62a22-46f7-4f0d-b151-3fc640bef588
    internal-label: Intermediate
  - id: e8ccd51f-da0d-4e3b-939b-e30d5ebb1ea5
    internal-label: Beginner
topic_v2:
  - id: b5ce8718-c3af-4fdb-a1a9-fca32f83a87c
    internal-label: Implementation
  - id: bce87dde-a4ab-44c9-8a18-ad66e4ddb377
    internal-label: Customer experience
  - id: c1579802-ddd4-4214-8a91-97b2066abe11
    internal-label: Troubleshooting
  - id: cdd65e7e-8839-44a2-bc21-0e03623b5dd1
    internal-label: Optimization
  - id: d00e9f03-e50b-4162-b143-0c0817c937c2
    internal-label: Customer journeys
---
# Journey orchestration - complete guide{#journey-orchestration-guide}

>[!BEGINSHADEBOX]

**On this page:** Get a complete guide to journey orchestration in Adobe Journey Optimizer, covering how to design, manage, and refine multistep, multichannel customer journeys that adapt in real time.

>[!ENDSHADEBOX]

Journeys in [!DNL Adobe Journey Optimizer] empower you to create personalized, multistep customer journeys that adapt in real-time to your audience's behavior and needs. Using an intuitive drag-and-drop canvas, you can orchestrate messages and actions across multiple channels, leveraging contextual data and audience targeting for maximum impact.

Whether you're exploring real-time triggers, managing journey properties, or using advanced tools like custom actions and expressions, this guide provides a clear roadmap to confidently design and refine journeys that deliver meaningful, timely customer experiences.

## What are journeys?

Use [!DNL Journey Optimizer] to build real-time orchestration use cases using contextual data stored in events or data sources. Design multistep advanced scenarios that respond to customer behavior and business events in real-time.

The Journey Optimizer journey designer provides everything marketers and journey practitioners need to orchestrate multi-step 1:1 journeys across channels. This includes an intuitive drag-and-drop canvas to orchestrate each step of the journey, define the target audience, and include the messages, offers, and content across channels that target audience members will see based on behavior, contextual data, and business events.

![Journey designer interface with palette, canvas, and properties pane](assets/journey38.png)

**Ready to start building?** Learn how to create and design your first journey on [this page](journey-gs.md).


## Key capabilities {#capabilities}

:::: landing-cards-container

:::
![icon](https://cdn.experienceleague.adobe.com/icons/circle-play.svg)

**Real-time & batch delivery**

Send real-time **unitary delivery** triggered when an event is received, or **in batch** using [!DNL Adobe Experience Platform] audiences.

[Learn about journey entry](entry-management.md)
:::

:::
![icon](https://cdn.experienceleague.adobe.com/icons/database.svg)

**Contextual data**

Leverage **contextual data** from events, information from [!DNL Adobe Experience Platform], or data from third-party API services.

[Work with data sources](../datasource/about-data-sources.md)
:::

:::
![icon](https://cdn.experienceleague.adobe.com/icons/envelope.svg)

**Built-in actions**

Use **built-in channel actions** to send messages designed in [!DNL Journey Optimizer] across email, push, SMS/RCS/MMS, and more.

[Send messages in journeys](journey-action.md)
:::

:::
![icon](https://cdn.experienceleague.adobe.com/icons/gear.svg)

**Custom actions**

Create **custom actions** if you're using a third-party system to send your messages or connect to external APIs.

[Configure custom actions](../action/about-custom-action-configuration.md)
:::

:::
![icon](https://cdn.experienceleague.adobe.com/icons/puzzle-piece.svg)

**Visual journey designer**

With the **journey designer**, build your multistep use cases: easily drag and drop an entry event or a read audience activity, add conditions and send personalized messages.

[Explore the journey designer](using-the-journey-designer.md)
:::

:::
![icon](https://cdn.experienceleague.adobe.com/icons/puzzle-piece.svg)

**Reusable Journey Fragments**

Build a set of journey nodes once — such as an eligibility check or channel routing logic — and reuse them across journeys with **Journey Fragments**.

[Learn about Journey Fragments](journey-fragments.md)
:::

:::
![icon](https://cdn.experienceleague.adobe.com/icons/shield-halved.svg)

**Test & optimize**

Test your journeys before publishing, monitor their performance, and optimize delivery with advanced features like send-time optimization.

[Test and publish journeys](testing-the-journey.md)
:::

::::

## Use cases and examples {#use-cases}

From within the journey designer, marketers can send real-time triggered 1:1 messages through any channel when an event occurs. For example, when a customer subscribes to a service, it can [trigger a welcome email](message-to-subscribers-uc.md), encouraging them to log into the app for the first time and set their preferences. Actions like completing the purchase, opening the email, and logging into the app can be used to advance new customers through their journeys.

The [journey designer](using-the-journey-designer.md) provides [built-in channel actions](journey-action.md) that support outbound messages, such as emails, push notifications, and SMS/RCS/MMS, as well as inbound channels, including mobile apps, websites, and code-based experiences built directly within Journey Optimizer. You can also use third-party systems to send messages — Journey Optimizer includes [custom actions](using-custom-actions.md) to allow these systems to be integrated into journeys directly from the journey designer.


:::: landing-cards-container

:::
![icon](https://cdn.experienceleague.adobe.com/icons/book.svg)

**Learn through use cases**

Explore comprehensive, end-to-end journey use cases that demonstrate real-world implementations and best practices.

[Discover all use cases](jo-use-cases.md)
:::

:::
![icon](https://cdn.experienceleague.adobe.com/icons/envelope.svg)

**Welcome new subscribers**

Send a personalized welcome journey when customers subscribe to your service, guiding them through onboarding steps.

[Learn more](message-to-subscribers-uc.md)
:::

:::
![icon](https://cdn.experienceleague.adobe.com/icons/calendar-alt.svg)

**Optimize email send times**

Use AI-powered send-time optimization to deliver emails when each customer is most likely to engage.

[Learn more](send-time-optimization.md)
:::

:::
![icon](https://cdn.experienceleague.adobe.com/icons/chart-line.svg)

**Ramp up deliveries**

Gradually increase message volume to warm up your sending reputation and avoid deliverability issues.

[Learn more](ramp-up-deliveries-uc.md)
:::

:::
![icon](https://cdn.experienceleague.adobe.com/icons/bullseye.svg)

**Target by weekday**

Send different content based on the day of the week customers enter your journey.

[Learn more](weekday-email-uc.md)
:::

:::
![icon](https://cdn.experienceleague.adobe.com/icons/question.svg)

**Journey FAQ**

Find answers to frequently asked questions about journey building, troubleshooting, and best practices.

[View FAQ](journey-faq.md)
:::

::::



## Learning resources {#learning-resources}

:::: landing-cards-container

:::
![icon](https://cdn.experienceleague.adobe.com/icons/list-check.svg)

**Create & manage journeys**

Step-by-step guidance on designing, testing, publishing, and tracking customer journeys to build personalized omnichannel campaigns.

[Explore journey creation](../../rp_landing_pages/create-journey-landing-page.md) | [Learn journey management](../../rp_landing_pages/manage-journey-landing-page.md) | [Journey workflow steps](journey.md#workflow)
:::

:::
![icon](https://cdn.experienceleague.adobe.com/icons/puzzle-piece.svg)

**Journey activities**

Discover how to configure and use activities like triggers, decision steps, audience management, and personalized messaging in journeys.

[Explore activities](../../rp_landing_pages/about-journey-building-landing-page.md)
:::

:::
![icon](https://cdn.experienceleague.adobe.com/icons/code-branch.svg)

**Expressions & conditions**

Master expression creation for dynamic workflows, data manipulation, and advanced journey orchestration using powerful tools and syntax.

[Learn about expressions](../../rp_landing_pages/building-advanced-conditions-journeys-landing-page.md)
:::

:::
![icon](https://cdn.experienceleague.adobe.com/icons/bell.svg)

**Troubleshoot & monitor**

Diagnose and resolve journey execution issues with tools, error codes, and best practices for debugging and optimization.

[Troubleshooting guide](../../rp_landing_pages/troubleshoot-journey-landing-page.md)
:::

:::
![icon](https://cdn.experienceleague.adobe.com/icons/book.svg)

**Journey designer overview**

Understand the journey canvas, palette, and how to design your customer journeys using the visual interface.

[Learn the designer](using-the-journey-designer.md)
:::

:::
![icon](https://cdn.experienceleague.adobe.com/icons/shield-halved.svg)

**Test & publish**

Test your journeys thoroughly before publishing them to ensure they work as expected and deliver the right experience.

[Testing guide](testing-the-journey.md)
:::

::::

### Video tutorial {#video}

Discover the components of a journey and understand the basics of building a journey in the canvas.

>[!VIDEO](https://video.tv.adobe.com/v/3424996?quality=12)

### Additional resources

* **[Error codes reference](error-codes-reference.md)** - Journey error codes and troubleshooting steps
* **[Alerts](../reports/alerts.md)** - Set up alerts for journey monitoring
* **[Troubleshooting](troubleshooting.md)** - Common journey issues and solutions
* **[Journey Tutorials](https://experienceleague.adobe.com/en/docs/journey-optimizer-learn/tutorials/journeys/journey-designer-overview){target="_blank"}** - Learn journey building through hands-on video tutorials
* **[Journey guardrails & limitations](../start/guardrails.md)** - Check guardrails and limitations when using [!DNL Adobe Journey Optimizer]

+++ AI Knowledge Reference

This section contains structured knowledge intended to support interpretation, retrieval, and question answering related to this topic.

For complete understanding, this information should be combined with the documentation on this page. Neither source is intended to stand alone; the page describes the feature, while this section provides additional context that helps disambiguate terminology, intent, applicability, and constraints.

* **TL;DR:** This is the comprehensive getting-started guide for journey orchestration in Adobe Journey Optimizer, covering key capabilities (real-time and batch delivery, contextual data, built-in and custom actions, the visual designer, Journey Fragments, and testing), common use cases, and links to all major learning resources.

**Intents:**
* Understand the key capabilities available in the Journey Optimizer journey designer before building a first journey
* Navigate to the correct resource for creating, managing, testing, or troubleshooting journeys
* Learn how to trigger 1:1 real-time messages across any channel using the journey designer
* Discover how Journey Fragments enable reuse of common node logic across journeys
* Access video tutorials and step-by-step guides for common journey use cases such as welcome series, cart abandonment, and send-time optimization

**Glossary:**
* **Journey designer**: The drag-and-drop visual canvas in Adobe Journey Optimizer used to build and orchestrate multi-step customer journeys *(product-specific)*
* **Journey Fragment**: A reusable set of journey nodes (e.g., eligibility check, channel routing logic) built once and inserted into multiple journeys *(product-specific)*
* **Unitary delivery**: A real-time message triggered for a single profile when a specific event occurs *(product-specific)*
* **Batch delivery**: Messages sent to all profiles in an Adobe Experience Platform audience at once or on a schedule *(product-specific)*
* **Send-Time Optimization (STO)**: An AI-driven feature that predicts the optimal time to send a message to each individual profile to maximise engagement *(product-specific)*
* **Custom action**: A journey activity that connects to a third-party system via API to send messages or retrieve data *(product-specific)*

**Guardrails:**
* Journey guardrails and limitations are detailed separately on the guardrails page and should be reviewed before designing at scale
* Custom actions require prior configuration by a technical user before they can be used in a journey
* Journey Fragments must be Active before they can be inserted into a journey

**Terminology:**
* Canonical name: Journey — Acronym: none — variants: customer journey, orchestration flow, multistep journey
* Synonyms: "journey designer" = "journey canvas" = "journey builder"
* Do not confuse: "built-in channel actions" ≠ "custom actions" — built-in actions use native AJO channels; custom actions call external third-party APIs

**FAQ:**
* **Q: What is the difference between real-time (unitary) delivery and batch delivery in journeys?** — Unitary delivery triggers a message for one profile at a time in real-time when an event occurs. Batch delivery processes all profiles in an audience at once or on a schedule using a Read Audience activity.
* **Q: Can I reuse common logic (like an eligibility check) across multiple journeys?** — Yes; save the nodes as a Journey Fragment and insert the Active fragment into any journey across the sandbox.
* **Q: Where do I go to create my first journey?** — Follow the step-by-step guide on the "Create your first journey" page, which walks through entry point selection, canvas design, testing, and publication.
* **Q: How do I send messages through a third-party system from a journey?** — Configure a custom action to call the external API, then add it as an action activity in the journey canvas.
* **Q: Where can I find answers to common journey questions?** — Visit the Journey FAQ page for answers covering concepts, building, testing, execution, monitoring, and best practices.

+++
