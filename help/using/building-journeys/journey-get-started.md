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
