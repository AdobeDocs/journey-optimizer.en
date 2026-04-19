---
solution: Journey Optimizer
product: journey optimizer
title: Journey Optimizer
description: Discover Adobe Journey Optimizer key features and use cases
feature: Get Started
topic: Content Management
role: User
level: Beginner
keywords: journey optimizer, what is ajo, adobe journey optimizer, get started, omnichannel, personalization, customer journey
exl-id: 956178c0-9985-4ff8-a29e-17dd367ce4d4
---
# Get Started with Journey Optimizer {#cjm-gs}

This page introduces Adobe Journey Optimizer: what it is, who it's for, its key capabilities, and how it fits into the Adobe Experience Platform architecture. It is the recommended starting point for new users.

## What is [!DNL Adobe Journey Optimizer]?{#about-cjm}

[!DNL Adobe Journey Optimizer] is an enterprise application for creating and delivering connected, contextual, and personalized customer experiences across all channels and touchpoints. It is built natively on [!DNL Adobe Experience Platform] and leverages a unified real-time customer profile, an API-first open framework, centralized offer decisioning, and AI/ML capabilities. Journey Optimizer enables brands to orchestrate both scheduled marketing campaigns and real-time, event-triggered communications — from a single application, at scale. The result is meaningful brand experiences that boost customer loyalty and lifetime value.

This guide applies to marketing practitioners, operations teams, and administrators new to Journey Optimizer.

➡️ [Discover Journey Optimizer](https://experienceleague.adobe.com/docs/journey-optimizer-learn/tutorials/introduction-to-journey-optimizer/introduction.html){target="_blank"} (video)


<!--
 Use [!DNL Adobe Journey Optimizer] to build multi-step customer journeys that initiate a sequence of interactions, offers, and messages across channels in real time. This approach ensures customers are engaged at the optimal moments based on their actions and relevant business signals. Learn how to build journeys in [this section](../building-journeys/journey-gs.md).

You can also create audience-based campaigns to send messages.
-->


## Use cases {#use-cases}

These examples illustrate how Journey Optimizer's capabilities work together across different roles, industries, and channels.

| Use case | Role | Core capability |
|----------|------|----------------|
| Delayed shipment recovery | Marketer | [Unified profile + audience exclusion](../audience/get-started-profiles.md) |
| Real-time in-store engagement | Marketer | [Geofence triggering + push](../push/get-started-push.md) |
| Cart abandonment recovery | Marketer | [Event-triggered multi-step journey](../building-journeys/journey-gs.md) |
| Streaming service welcome series | Marketer | [Event-triggered welcome journey](../building-journeys/journey-gs.md) |
| Reservation reminder with directions | Marketer | [Scheduled + location-aware messaging](../campaigns/get-started-with-campaigns.md) |
| Proactive service outage notification | Operations | [Automated selection at scale](../audience/about-audiences.md) |
| AI-powered promotional campaign | Marketer | [AI content generation + experimentation](ai-features.md) |
| Maintenance alerts via mobile app | Operations | [Non-marketing orchestration](../building-journeys/journey-gs.md) |

+++**Delayed shipment recovery (Marketer)**

A clothing store typically sends post-purchase surveys to all customers who have purchased products in the last week. Due to inclement weather, a few shipments experienced delays. Seeing which customers have not received their shipments, the clothing store can exclude them from the scheduled customer satisfaction send and instead send a personalized email apologizing for the delay and offering a discount code with product recommendations based on the customer's past purchases.

[Get started with campaigns](../campaigns/get-started-with-campaigns.md)

+++

+++**Real-time in-store engagement (Marketer)**

The same retailer can engage a loyal customer who pulls into the store parking lot in real time by sending them a push notification about a sweater that is back in stock in the customer's size.

[Get started with push notifications](../push/get-started-push.md)

+++

+++**Cart abandonment recovery (Marketer)**

When a customer adds items to an online cart but leaves without completing the purchase, Journey Optimizer detects the event in real time and starts a recovery journey automatically. The customer receives a personalized email reminding them of the items left behind. If they do not click through within 24 hours, a follow-up push notification is sent — personalized based on their browsing history and loyalty status.

[Build your first journey](../building-journeys/journey-gs.md)

+++

+++**Streaming service welcome series (Marketer)**

When a customer subscribes to a streaming service, Journey Optimizer detects the sign-up event and immediately starts a multi-step welcome journey. The customer receives a welcome email encouraging them to open the app for the first time. If no login activity is detected within 48 hours, a follow-up push notification is sent with personalized content recommendations based on their stated interests during sign-up — turning a passive subscriber into an active, engaged user from day one.

[Build your first journey](../building-journeys/journey-gs.md)

+++

+++**Reservation reminder with directions (Marketer)**

A hospitality brand sends each guest a timely reminder one hour before their reservation. The notification includes the guest's name, reservation time, and location-based directions to the venue — automatically assembled from the customer profile and booking data, with no manual effort from the marketing team.

[Get started with campaigns](../campaigns/get-started-with-campaigns.md)

+++

+++**Proactive service outage notification (Operations team)**

When a service disruption occurs, Journey Optimizer automatically identifies the affected customers based on their account data and usage patterns. Those customers receive a proactive notification acknowledging the issue and outlining next steps — turning a potentially negative experience into a moment of transparency and trust, delivered at scale.

[Build your first journey](../building-journeys/journey-gs.md)

+++

+++**AI-powered promotional campaign (Marketer)**

A retail brand planning a product launch uses Journey Optimizer's AI Assistant to generate multiple subject line and body copy variations in minutes — guided by a natural language prompt and their uploaded brand guidelines. Built-in content experimentation automatically identifies the best-performing variant among an initial audience sample. The winning message is then deployed to the remaining recipients, maximizing engagement without additional copywriting effort.

[Explore AI & intelligent features](ai-features.md) | [Learn about content experimentation](../content-management/experiment-accelerator-gs.md)

+++

+++**Maintenance alerts via mobile app (Operations team)**

Non-marketers such as operations teams and customer support can use [!DNL Adobe Journey Optimizer] to manage operational notifications or monitor onboarding processes. For example, an amusement park where visitors download a mobile app as part of their experience: maintenance staff can use Journey Optimizer to notify park visitors of rides currently closed due to maintenance.

[Build your first journey](../building-journeys/journey-gs.md)

+++

## Key capabilities {#key-capabilities}

[!DNL Adobe Journey Optimizer] is an agile and scalable application for creating and delivering personalized, connected, and timely customer experiences across any app, device, or channel. 

![Diagram showing Journey Optimizer's three core capability areas: Real-time Customer Insights & Engagement, Modern Omnichannel Orchestration & Execution, and Intelligent Decisioning & Personalization, all built on Adobe Experience Platform.](assets/ajo-capabilities.png)

Key capabilities include:

### Real-time Customer Insights & Engagement

An integrated profile fuses live data from all sources across customer touchpoints, including behavioral, transactional, financial, and operational data to optimize personal and contextual experiences for customers in their time. [Learn about profiles and audiences](../audience/get-started-profiles.md)

### Modern Omnichannel Orchestration & Execution

A single canvas on which to harmonize and optimize the customer journey for 1:1 customer engagement and marketing outreach — to help brands deliver more value across the customer lifecycle. Customer journeys designed in [!DNL Adobe Journey Optimizer] can be dynamic and event-based to help brands react to real-time signals as well as connect those interactions with scheduled campaigns so the right decisions can be made about what communications to send a customer, when, and through what channels. Embedded content creation tools — including a drag-and-drop visual designer, reusable templates, content fragments, and a personalization editor — allow teams to author, personalize, and manage messages for every channel directly within the same workflow. [Build your first journey](../building-journeys/journey-gs.md) | [Design your content](../../rp_landing_pages/content-management-landing-page.md)

### Intelligent Decisioning & Personalization

Brands can apply centralized decisioning and incorporate artificial intelligence and machine learning to configure predictive insights throughout the customer experience, making it easier to automate decisions and optimize the experience at scale. Decisioning powers centralized offers across channels at scale through [!DNL Adobe Journey Optimizer]. [Explore offer decisioning](../offers/get-started/starting-offer-decisioning.md) | [Discover AI features](ai-features.md)


## Availability & Licensing {#availability}

This documentation covers the current release of Journey Optimizer and applies to both B2C and B2B edition users unless otherwise noted. Components and capabilities available in your environment depend on your [permissions](../administration/permissions.md) and on your [licensing package](https://helpx.adobe.com/legal/product-descriptions/adobe-journey-optimizer.html){target="_blank"}. For any question, reach out to your Adobe Customer Success Manager or your Adobe representative.

Adobe Experience Cloud general privacy guidelines and procedures apply to [!DNL Journey Optimizer]. [Learn more about Adobe Experience Cloud privacy](https://www.adobe.com/privacy/experience-cloud.html){target="_blank"}.


## Architecture {#architecture}

Understand the basic architecture of [!DNL Adobe Journey Optimizer], the points of integration, and the relationship between [!DNL Journey Optimizer] and [!DNL Experience Platform], in the diagram below.

Adobe Experience Platform is a powerful, flexible, open, and centralized data foundation that collects, standardizes, governs, applies AI insights to, and unifies data to offer thoughtful and relevant digital customer experiences.

![Diagram showing Adobe Experience Platform as the foundational data layer, with four natively built applications on top: Adobe Real-Time Customer Data Platform, Journey Optimizer, Customer Journey Analytics, and Adobe Mix Modeler. Shared services such as Real-Time Customer Profile, data governance, and identity resolution underpin all four applications.](assets/ajo-aep-architecture-diagram.png){width="70%" zoomable="yes"}

Four applications are natively built on Experience Platform: Adobe Real-Time Customer Data Platform, Journey Optimizer, Customer Journey Analytics, and Adobe Mix Modeler.

The core functionality and services of Journey Optimizer operate off the foundational components of Adobe Experience Platform, which includes the Real-Time Customer Profile. While Journey Optimizer works seamlessly and is interoperable with Real-Time CDP and Customer Journey Analytics, it can also function independently as a standalone application.

![Diagram showing Journey Optimizer's internal architecture and its integration points with Adobe Experience Platform services, including data ingestion, Real-Time Customer Profile, decisioning engine, and outbound channel delivery across email, push, SMS, and web.](assets/ajo-architecture-diagram.png){width="70%" zoomable="yes"}


### Adobe Journey Optimizer Blueprints

Digital experience blueprints provide system and data flow architecture diagrams to help better understand how Adobe Experience Platform and Applications are integrated and implemented. The blueprints provide a visual representation of inter-system and component data and content flows, sequence of operations, and dependencies to help inform use case design and architecture of Adobe Experience Platform and Applications.

See [Adobe Journey Optimizer blueprints](https://experienceleague.adobe.com/en/docs/blueprints-learn/architecture/customer-journeys/journey-optimizer/journey-optimizer-overview){target="_blank"}.


>[!MORELIKETHIS]
>
>* [Key steps to start](quick-start.md) — Role-based quickstart guides for admins, marketers, and data engineers.
>* [Get started with data management](../data/gs-data.md) — Learn how data is ingested, unified, and activated in Journey Optimizer.
>* [Design journeys and send messages](../building-journeys/journey-gs.md) — Build your first customer journey and configure channel actions.
>* [Live reports](../reports/live-report.md) — Monitor campaign and journey performance in real time.
>* [Introduction to Journey Optimizer tutorial](https://experienceleague.adobe.com/en/docs/journey-optimizer-learn/tutorials/introduction-to-journey-optimizer/introduction){target="_blank"} — A guided video walkthrough of core Journey Optimizer concepts.
>* [Journey Optimizer Security Overview](https://www.adobe.com/content/dam/cc/en/security/pdfs/AJO_SecurityOverview.pdf) (PDF) — Security architecture, data protection, and compliance details.
>* [Journey Optimizer Product Description](https://helpx.adobe.com/legal/product-descriptions/adobe-journey-optimizer.html){target="_blank"} — Official licensing terms and edition feature breakdown.
