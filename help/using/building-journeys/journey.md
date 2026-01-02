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

Adobe Journey Optimizer empowers you to create personalized, multistep customer journeys that adapt in real-time to your audience's behavior and needs. Using an intuitive drag-and-drop canvas, you can orchestrate messages and actions across multiple channels, leveraging contextual data and audience targeting for maximum impact.

This guide provides a clear roadmap to help you understand journey fundamentals, choose the right journey type for your use case, and confidently design journeys that deliver meaningful, timely customer experiences.

## What are journeys?

**Journeys** are automated, multistep customer experiences that orchestrate personalized interactions across channels in response to customer behavior, business events, or scheduled campaigns. 

Use [!DNL Journey Optimizer] to:

* Build **real-time orchestration** use cases using contextual data stored in events or data sources
* Design **multistep advanced scenarios** that respond dynamically to customer behavior and business events
* Deliver **1:1 personalized experiences** at scale across email, push, SMS, in-app, web, and more

![Journey designer interface with palette, canvas, and properties pane](assets/journey38.png)

➡️ **Ready to start building?** [Create your first journey](journey-gs.md) in 5 minutes.

## Choose your journey type {#journey-types}

**Before you start building**, it's important to understand which type of journey fits your use case. Adobe Journey Optimizer supports four journey types, each designed for different entry mechanisms and business scenarios:

>[!BEGINTABS]

>[!TAB Unitary journeys]

![icon](https://cdn.experienceleague.adobe.com/icons/circle-play.svg) **When to use:** Real-time, event-triggered experiences

**Unitary journeys** are triggered individually when a specific action occurs (purchase, app sign-in, form submission). Profiles enter one at a time in real-time, making this ideal for immediate, behavior-driven responses.

**Perfect for:**

* Order confirmations after purchase
* Welcome emails when someone subscribes  
* Cart abandonment triggered by browsing
* Password reset notifications

➡️ [Learn about events](../event/about-events.md) | [Message to subscribers use case](message-to-subscribers-uc.md)

>[!TAB Read Audience journeys]

![icon](https://cdn.experienceleague.adobe.com/icons/database.svg) **When to use:** Scheduled campaigns to audience segments

**Read Audience journeys** start with an Adobe Experience Platform audience and send messages in batch to all profiles simultaneously. This journey type is ideal for scheduled, large-scale communications.

**Perfect for:**

* Monthly newsletters
* Promotional campaigns to target segments
* Product announcements
* Seasonal marketing campaigns

➡️ [Learn about Read Audience](read-audience.md) | [Get started with audiences](../audience/about-audiences.md)

>[!TAB Audience Qualification journeys]

![icon](https://cdn.experienceleague.adobe.com/icons/bullseye.svg) **When to use:** Real-time responses to audience membership changes

**Audience Qualification journeys** trigger when profiles qualify for (or exit from) a specific audience. Profiles enter individually as they meet criteria in real-time, enabling immediate engagement when customer behavior changes.

**Perfect for:**

* VIP tier upgrade notifications
* Re-engagement when customers become inactive
* First purchase celebration messages  
* Geographic targeting when customers move

➡️ [Learn about Audience Qualification](audience-qualification-events.md) | [Creating audiences](../audience/creating-a-segment-definition.md)

>[!TAB Business event journeys]

![icon](https://cdn.experienceleague.adobe.com/icons/calendar-alt.svg) **When to use:** Business conditions affecting multiple customers

**Business event journeys** are triggered by business-level events (stock updates, weather alerts, price changes) that affect multiple profiles simultaneously. These respond to broader business conditions rather than individual actions.

**Perfect for:**

* Low inventory alerts to interested customers
* Flash sale announcements
* Weather-based promotions
* Price drop notifications
* Product back-in-stock alerts

➡️ [Learn about business events](../event/about-creating-business.md) | [Entry management](entry-management.md)

>[!ENDTABS]

>[!NOTE]
>
>Not sure which type to choose? Start with **Unitary journeys** for event-based experiences or **Read Audience journeys** for scheduled campaigns—these cover most common use cases. 

## Build with the journey designer {#journey-designer}

The **[journey designer](using-the-journey-designer.md)** is your visual canvas for creating customer experiences. With an intuitive drag-and-drop interface, you can orchestrate every step of your journey without writing code.

![Journey designer interface with palette, canvas, and properties pane](assets/journey38.png)

### What you can do in the designer:

:::: landing-cards-container

:::
![icon](https://cdn.experienceleague.adobe.com/icons/circle-play.svg)

**Define entry points**

Choose how customers enter: through an event, audience segment, or audience qualification.

[Learn about entry management](entry-management.md)
:::

:::
![icon](https://cdn.experienceleague.adobe.com/icons/envelope.svg)

**Send messages**

Use built-in channel actions for email, push, SMS/MMS, in-app, web, and more—all designed in Journey Optimizer.

[Send messages in journeys](journeys-message.md)
:::

:::
![icon](https://cdn.experienceleague.adobe.com/icons/code-branch.svg)

**Add logic & conditions**

Branch your journey based on profile attributes, audience membership, or real-time events.

[Use conditions](condition-activity.md)
:::

:::
![icon](https://cdn.experienceleague.adobe.com/icons/database.svg)

**Leverage data**

Use contextual data from events, Adobe Experience Platform, or third-party API services.

[Work with data sources](../datasource/about-data-sources.md)
:::

:::
![icon](https://cdn.experienceleague.adobe.com/icons/gear.svg)

**Connect external systems**

Create custom actions to integrate third-party systems for sending messages or triggering workflows.

[Configure custom actions](../action/about-custom-action-configuration.md)
:::

:::
![icon](https://cdn.experienceleague.adobe.com/icons/puzzle-piece.svg)

**Add orchestration activities**

Use wait times, jumps, profile updates, and audience management to create sophisticated flows.

[Explore all activities](about-journey-activities.md)
:::

::::

➡️ **Hands-on learning:** [Watch the journey designer video](#video) or [explore end-to-end use cases](jo-use-cases.md)

## Your journey creation workflow {#workflow}

Building successful journeys follows a clear, repeatable process. Here's your step-by-step workflow:

```mermaid
graph LR
    A[1. Plan] --> B[2. Design]
    B --> C[3. Test]
    C --> D[4. Publish]
    D --> E[5. Monitor]
    E --> F[6. Optimize]
```

### 1. **Plan your journey** {#plan}

Before opening the designer, clarify your objectives:

* **What's the goal?** (e.g., onboard new customers, re-engage inactive users)
* **Who's the audience?** (specific segment, event-driven individuals)
* **Which journey type fits?** (See [journey types](#journey-types) above)
* **What channels will you use?** (email, push, SMS, etc.)

### 2. **Design in the canvas** {#design}

Use the journey designer to build your flow:

1. **Set entry conditions** - Define how profiles enter (event, audience, qualification)
2. **Add orchestration logic** - Include wait times, conditions, and decision points
3. **Configure messages** - Design your communications or leverage existing templates
4. **Set up actions** - Configure built-in or custom actions to execute
5. **Define exit criteria** - Specify when and how profiles complete the journey

[Learn to use the journey designer →](using-the-journey-designer.md)

### 3. **Test before going live** {#test}

Always test your journey to catch issues before customers experience them:

* Use **test mode** to simulate the journey with test profiles
* Use **dry run** to preview journey execution without affecting real data or sending messages
* Verify all conditions, messages, and actions work as expected
* Check timing, data flows, and personalization

[Test your journey →](testing-the-journey.md) | [Learn about dry run →](journey-dry-run.md)

### 4. **Publish your journey** {#publish}

Once testing is complete, publish to make your journey live:

* Review final settings and properties
* Publish to activate for real customers
* Note: Live journeys can be stopped but not edited (you must create a new version)

[Publish your journey →](publish-journey.md)

### 5. **Monitor performance** {#monitor}

Track how your journey performs in the real world:

* View journey reports and analytics
* Monitor entry, completion, and error rates
* Set up alerts for critical issues

[Monitor and report →](report-journey.md) | [Set up alerts →](../reports/alerts.md)

### 6. **Optimize and iterate** {#optimize}

Use insights to improve:

* Analyze engagement metrics and conversion rates
* Test send-time optimization
* Create new journey versions with improvements
* Use AI-powered recommendations

[Optimize your journeys →](optimize.md) | [Send-time optimization →](send-time-optimization.md)

➡️ **Ready to start?** [Create your first journey now →](journey-gs.md)

## Real-world use cases {#use-cases}

Learn from practical examples that demonstrate how to apply journey concepts to solve common marketing challenges:

:::: landing-cards-container

:::
![icon](https://cdn.experienceleague.adobe.com/icons/envelope.svg)

**Welcome new subscribers**

When a customer subscribes to your service, trigger a welcome journey that encourages them to complete onboarding steps.

[View use case →](message-to-subscribers-uc.md)
:::

:::
![icon](https://cdn.experienceleague.adobe.com/icons/calendar-alt.svg)

**Send-time optimization**

Use AI to deliver emails when each customer is most likely to engage, maximizing open and click rates.

[View use case →](send-time-optimization.md)
:::

:::
![icon](https://cdn.experienceleague.adobe.com/icons/chart-line.svg)

**Ramp up deliveries**

Gradually increase message volume to warm up your sending reputation and avoid deliverability issues.

[View use case →](ramp-up-deliveries-uc.md)
:::

:::
![icon](https://cdn.experienceleague.adobe.com/icons/bullseye.svg)

**Target by weekday**

Send different content based on the day of the week customers enter your journey for better relevance.

[View use case →](weekday-email-uc.md)
:::

:::
![icon](https://cdn.experienceleague.adobe.com/icons/puzzle-piece.svg)

**Multi-channel campaigns**

Orchestrate seamless experiences across email, push, SMS, and web channels in a single journey.

[View use case →](journeys-uc.md)
:::

:::
![icon](https://cdn.experienceleague.adobe.com/icons/book.svg)

**All use cases**

Explore the complete library of journey use cases with step-by-step implementations.

[Browse all →](jo-use-cases.md) | [Use case library →](/help/rp_landing_pages/journey-use-cases-landing-page.md)
:::

::::

## Explore journey capabilities {#capabilities}

As you get more comfortable with journey building, explore these powerful capabilities to create sophisticated customer experiences:

:::: landing-cards-container

:::
![icon](https://cdn.experienceleague.adobe.com/icons/chart-line.svg)

**Advanced Expressions**

Build dynamic conditions and personalization using the expression editor for data manipulation and complex logic.

[Learn about expressions](/help/rp_landing_pages/building-advanced-conditions-journeys-landing-page.md)
:::

:::
![icon](https://cdn.experienceleague.adobe.com/icons/clock.svg)

**Time zone management**

Handle global audiences with automatic time zone adjustments and optimal send times.

[Manage time zones](timezone-management.md)
:::

:::
![icon](https://cdn.experienceleague.adobe.com/icons/shield-halved.svg)

**Test mode & dry run**

Validate journeys with test profiles before going live, and preview execution without affecting real data.

[Use dry run](journey-dry-run.md)
:::

:::
![icon](https://cdn.experienceleague.adobe.com/icons/database.svg)

**Copy to sandbox**

Duplicate journeys across sandboxes to streamline testing and deployment workflows.

[Copy journeys](copy-to-sandbox.md)
:::

:::
![icon](https://cdn.experienceleague.adobe.com/icons/book.svg)

**Tags & organization**

Use tags to categorize and filter journeys for better management at scale.

[Organize with tags](tags.md)
:::

:::
![icon](https://cdn.experienceleague.adobe.com/icons/gear.svg)

**Throughput control**

Limit message throughput to manage sending reputation and avoid overwhelming systems.

[Control throughput](limit-throughput.md)
:::

::::

[View all journey capabilities →](/help/rp_landing_pages/manage-journey-landing-page.md)

## Learn by watching {#video}

Get a visual introduction to journey components and learn the basics of building journeys in the canvas:

>[!VIDEO](https://video.tv.adobe.com/v/3424996?quality=12)

➡️ **Want more videos?** [Explore journey video tutorials](https://experienceleague.adobe.com/en/docs/journey-optimizer-learn/tutorials/journeys/journey-designer-overview){target="_blank"}

## Need help? {#help}

### Quick links for common tasks

* **[Create your first journey](journey-gs.md)** - Step-by-step guide for beginners
* **[Journey FAQ](journey-faq.md)** - Common questions answered
* **[Troubleshooting](/help/rp_landing_pages/troubleshoot-journey-landing-page.md)** - Diagnose and fix issues
* **[Error codes reference](error-codes-reference.md)** - Understand error messages
* **[Guardrails & limitations](../start/guardrails.md)** - Technical boundaries and best practices

### Get notified about issues

Set up **[journey alerts](../reports/alerts.md)** to receive real-time notifications when journeys encounter errors or unusual patterns.

### Additional resources

* **[Journey management hub](/help/rp_landing_pages/manage-journey-landing-page.md)** - Tools for filtering, optimization, and profile management
* **[Journey activities reference](/help/rp_landing_pages/about-journey-building-landing-page.md)** - Complete guide to all activity types
* **[Troubleshooting execution issues](troubleshooting-execution.md)** - Debug journey execution problems
* **[Troubleshooting inbound activities](troubleshooting-inbound.md)** - Fix entry and qualification issues

**Ready to build your first journey?** [Get started now →](journey-gs.md)
