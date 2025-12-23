---
solution: Journey Optimizer
product: journey optimizer
title: Get started with journeys
description: Get started with journeys
feature: Journeys, Get Started, Overview
role: User
level: Beginner, Intermediate
keywords: journey, discover, get-start
exl-id: 73cfd48b-72e6-4b72-bbdf-700a32a34bda
version: Journey Orchestration
---

# Get started with journeys{#jo-general-principle}

Journeys in Adobe Journey Optimizer empower you to create personalized, multistep customer journeys that adapt in real-time to your audience's behavior and needs. Using an intuitive drag-and-drop canvas, you can orchestrate messages and actions across multiple channels, leveraging contextual data and audience targeting for maximum impact. Whether you're exploring real-time triggers, managing journey properties, or using advanced tools like custom actions and expressions, this section provides a clear roadmap to help you design and refine journeys that deliver meaningful, timely customer experiences.

Use [!DNL Journey Optimizer] to build real-time orchestration use cases using contextual data stored in events or data sources. You can design multistep advanced scenarios with the following capabilities:

* Send real-time **unitary delivery** triggered when an [event](general-events.md) is received, or **in batch** using Adobe Experience Platform [audiences](read-audience.md).

* Leverage **contextual data** from [events](../event/about-events.md), information from Adobe Experience Platform, or data from third-party API services through [data sources](../datasource/about-data-sources.md).

* Use the **[built-in actions](journeys-message.md)** to send messages designed in [!DNL Journey Optimizer] or create **[custom actions](using-custom-actions.md)** if you are using a third-party system to send your messages.

* With the **[journey designer](using-the-journey-designer.md)**, build your multistep use cases: easily drag and drop an entry event or a [read audience activity](read-audience.md), add [conditions](condition-activity.md) and send personalized messages.

The Journey Optimizer [journey designer](using-the-journey-designer.md) provides everything marketers and journey practitioners need to orchestrate multi-step 1:1 journeys across channels. This includes an intuitive drag-and-drop canvas to orchestrate each step of the journey, define the target audience, and include the messages, offers, and content across channels that target audience members will see based on behavior, contextual data, and business events. Explore [real-world use cases](jo-use-cases.md) to see how you can apply these capabilities.

➡️ [Discover Journey Optimizer in video](#video) 

## Journey types

Adobe Journey Optimizer supports four journey types, each designed for different use cases and entry mechanisms. Choose the right type based on how you want profiles to enter and progress through your customer experiences.

>[!BEGINTABS]

>[!TAB Unitary journeys]

**Unitary journeys** are triggered individually by an event when a specific action occurs, such as a purchase, app sign-in, or form submission. Profiles enter the journey one at a time in real-time when the event is received, making this ideal for personalized, behavior-driven experiences.

**Key characteristics:**

* Real-time, event-driven entry
* Individual profile processing
* Perfect for transactional messages and immediate responses
* Supports contextual data from the triggering event

**Use cases:**

* Order confirmation after purchase
* Welcome email when someone subscribes
* Cart abandonment triggered by browsing behavior
* Password reset notifications

➡️ [Learn about event configuration](../event/about-events.md) | [General events](general-events.md) | [Message to subscribers use case](message-to-subscribers-uc.md)

>[!TAB Read Audience journeys]

**Read Audience journeys** start with an audience from Adobe Experience Platform and send messages in batch to all profiles in that audience. This journey type processes the entire audience at once, making it ideal for scheduled campaigns and recurring communications.

**Key characteristics:**

* Batch processing of audience segments
* Scheduled or one-time execution
* All profiles enter simultaneously
* Supports large-scale communications

**Use cases:**

* Monthly newsletters
* Promotional campaigns to target segments
* Product announcements to all customers
* Seasonal marketing campaigns

➡️ [Learn about Read Audience activity](read-audience.md) | [Get started with audiences](../audience/about-audiences.md) | [Multi-channel messaging use case](journeys-uc.md)

>[!TAB Audience Qualification journeys]

**Audience Qualification journeys** are triggered when profiles qualify for (or exit from) a specific audience segment. Profiles enter the journey individually as they meet the audience criteria in real-time, enabling immediate engagement when customer behavior changes.

**Key characteristics:**

* Real-time qualification-based entry
* Continuous monitoring of audience membership
* Individual profile processing as they qualify
* Best with streaming audiences

**Use cases:**

* VIP tier upgrade notifications
* Re-engagement when customers become inactive
* First purchase celebration messages
* Geographic targeting when customers move

➡️ [Learn about Audience Qualification](audience-qualification-events.md) | [Condition activity](condition-activity.md) | [Creating segment definitions](../audience/creating-a-segment-definition.md)

>[!TAB Business event journeys]

**Business event journeys** are triggered by business events (such as stock updates, weather alerts, or price changes) that affect multiple profiles simultaneously. Rather than reacting to individual customer actions, these journeys respond to broader business conditions or external factors.

**Key characteristics:**

* Triggered by business-level events, not individual actions
* Affects multiple profiles at once
* Targets a specific audience when the event occurs
* Combines event-driven timing with audience targeting

**Use cases:**

* Low inventory alerts to interested customers
* Flash sale announcements
* Weather-based promotions
* Price drop notifications
* Product back-in-stock alerts

➡️ [Learn about business events](general-events.md) | [Configure business events](../event/about-creating-business.md) | [Entry management](entry-management.md)

>[!ENDTABS]

## Journeys Overview

:::: landing-cards-container
:::
![icon](https://cdn.experienceleague.adobe.com/icons/circle-play.svg)

Getting Started with Journey Creation

Step-by-step guidance on designing, testing, publishing, and tracking customer journeys to build personalized omnichannel campaigns.

[Create your first journey](journey-gs.md)
:::

:::
![icon](https://cdn.experienceleague.adobe.com/icons/list-check.svg)

Journey Orchestration - Complete Guide

Comprehensive documentation covering all aspects of journey creation, management, and optimization in Adobe Journey Optimizer.

[Explore the complete guide](journey-get-started.md)
:::

:::
![icon](https://cdn.experienceleague.adobe.com/icons/gear.svg)

Managing Your Journeys

Manage customer journeys efficiently with tools for filtering, profile management, time zones, and optimization techniques.

[Learn journey management](/help/rp_landing_pages/manage-journey-landing-page.md)
:::

:::
![icon](https://cdn.experienceleague.adobe.com/icons/puzzle-piece.svg)

Journey Activities

Discover how to configure and use activities like triggers, decision steps, audience management, and personalized messaging in journeys.

[Explore activities](/help/rp_landing_pages/about-journey-building-landing-page.md)
:::

:::
![icon](https://cdn.experienceleague.adobe.com/icons/code-branch.svg)

Building Expressions

Master expression creation for dynamic workflows, data manipulation, and advanced journey orchestration using powerful tools and syntax.

[Learn about expressions](/help/rp_landing_pages/building-advanced-conditions-journeys-landing-page.md)
:::

:::
![icon](https://cdn.experienceleague.adobe.com/icons/bullseye.svg)

Journey Use Cases

Explore real-world applications of Adobe Journey Optimizer, including multi-channel messaging and integration with external systems.

[Discover use cases](/help/rp_landing_pages/journey-use-cases-landing-page.md)
:::

::::

## Use cases{#uc-journey}

From within the journey designer, marketers can send real-time triggered 1:1 messages through any channel when an event occurs. For example, when a customer subscribes to a service, it can [trigger a welcome email](message-to-subscribers-uc.md), encouraging them to log into the app for the first time and set their preferences. Actions like completing the purchase, opening the email, and logging into the app can be used to advance new customers through their journeys.

The [journey designer](using-the-journey-designer.md) provides [built-in channel actions](journeys-message.md) that support outbound messages, such as emails, push notifications, and SMS/MMS, as well as inbound channels, including mobile apps, websites, and code-based experiences built directly within Journey Optimizer. You can also use third-party systems to send messages — whether via email, text, or other channels — Journey Optimizer includes [custom actions](using-custom-actions.md) to allow these systems to be integrated into journeys directly from the journey designer.

Learn how to build journeys [in these end-to-end use cases](jo-use-cases.md).

>[!NOTE]
>
>Journey guardrails and limitations are detailed on [this page](../start/guardrails.md)

## How-to video {#video}

Discover the components of a journey and understand the basics of building a journey in the canvas.

>[!VIDEO](https://video.tv.adobe.com/v/3424996?quality=12)

## Additional Resources {#additional-resources}

* **[Troubleshooting Customer Journeys](/help/rp_landing_pages/troubleshoot-journey-landing-page.md)** - Diagnose and resolve journey execution issues with tools, error codes, and best practices for debugging and optimization
* **[Journey FAQ](journey-faq.md)** - Frequently asked questions about journeys
* **[Journey Alerts](../reports/alerts.md)** - Set up alerts for journey monitoring and subscribe to notifications for real-time updates
* **[Error codes reference](error-codes-reference.md)** - Journey error codes and troubleshooting steps
* **[Troubleshooting](troubleshooting.md)** - Common journey issues and solutions
* **[Journey Tutorials (videos)](https://experienceleague.adobe.com/en/docs/journey-optimizer-learn/tutorials/journeys/journey-designer-overview){target="_blank"}** - Learn journey building through hands-on video tutorials covering features, capabilities, and best practices
