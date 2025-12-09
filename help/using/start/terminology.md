---
solution: Journey Optimizer
product: journey optimizer
title: Key terminology
description: Essential terms and concepts in Adobe Journey Optimizer
feature: Get Started
role: Admin, Developer, User
level: Beginner
exl-id: d4c968d2-5eae-4fff-9b67-427ac9d9d74c
---
# Key Terminology {#key-terminology}

This reference guide defines the essential terms you'll encounter when using Adobe Journey Optimizer. Understanding these concepts helps you navigate the platform confidently and collaborate effectively with your team.

>[!TIP]
>
>For detailed explanations of features and workflows, refer to the specific documentation sections linked throughout this guide.

## Core Platform Terms {#core-terms}

| Term | Definition |
|------|------------|
| **Adobe Journey Optimizer (AJO)** | An application for creating and delivering personalized messages to customers across channels (email, SMS, push notifications, web). It enables you to design customer journeys that respond to real-time customer actions. |
| **Adobe Experience Platform (AEP)** | The foundation of Adobe Journey Optimizer that collects and organizes all customer data in one place. It creates unified customer profiles that Journey Optimizer uses for personalization. [Learn more](https://experienceleague.adobe.com/docs/experience-platform/landing/home.html){target="_blank"} |
| **Real-time Customer Profile** | A unified, real-time view of each customer that combines data from multiple channels including online, offline, CRM, and third-party data. Each profile updates dynamically as customers interact with your brand. [Learn more](../audience/get-started-profiles.md) |
| **Sandbox** | A separate workspace for testing and experimentation without affecting live customer communications. Adobe Journey Optimizer provides multiple sandboxes for development, testing, and production environments. [Learn more](../administration/sandboxes.md) |

## Journey & Campaign Terms {#journey-campaign-terms}

| Term | Definition |
|------|------------|
| **Journey** | A series of connected steps that guide customers through experiences with your brand over time. Each step occurs based on customer actions or time triggers, enabling sequential, personalized interactions. [Learn more](../building-journeys/journey.md) |
| **Campaign** | A single communication or set of communications sent to a specific audience. Unlike journeys that unfold over time, campaigns deliver messages on a schedule or trigger, either immediately or at a specific time. [Learn more](../campaigns/get-started-with-campaigns.md) |
| **Event** | An action or occurrence that triggers or advances a journey. Events can be customer actions (making a purchase, abandoning a cart) or system events (date/time, data change). [Learn more](../event/about-events.md) |
| **Channel** | The method used to communicate with customers: email, SMS, push notifications, in-app messages, web, or direct mail. Each channel requires specific configuration. [Learn more](../configuration/get-started-configuration.md) |

## Customer & Audience Terms {#customer-audience-terms}

| Term | Definition |
|------|------------|
| **Audience** | A group of customers who share common characteristics or behaviors, such as "customers who purchased in the last 30 days" or "loyalty program members." Audiences are used to target specific customer segments. [Learn more](../audience/about-audiences.md) |
| **Audience Qualification** | The automatic process that occurs when a customer joins or leaves an audience. Journey Optimizer can trigger actions when someone enters or exits an audience, ensuring timely and relevant communications. [Learn more](../building-journeys/audience-qualification-events.md) |
| **Engageable Audience** | The number of customer profiles you can actively contact through Adobe Journey Optimizer based on your license agreement. This typically refers to profiles engaged within the last 12 months. |
| **Test Profile** | Fictitious profiles used for testing and previewing messages before sending to real customers. Test profiles help verify personalization, content, and journey logic. [Learn more](../audience/creating-test-profiles.md) |

## Content & Personalization Terms {#content-terms}

| Term | Definition |
|------|------------|
| **Personalization** | The process of tailoring content to individual customers using their profile data, preferences, and behaviors. For example, inserting a customer's name or showing product recommendations based on browsing history. [Learn more](../personalization/personalize.md) |
| **Content Template** | A reusable message design that can be used across multiple campaigns and journeys to maintain brand consistency and accelerate content creation. [Learn more](../content-management/content-templates.md) |
| **Fragment** | A reusable content block (such as a header, footer, or promotional banner) that can be used across multiple messages to ensure consistency and enable centralized updates. [Learn more](../content-management/fragments.md) |
| **Landing Page** | A standalone web page where customers can opt-in or opt-out from communications, subscribe to services, or provide information through online forms. [Learn more](../landing-pages/get-started-lp.md) |

## Decision & Offer Terms {#decision-terms}

| Term | Definition |
|------|------------|
| **Decision Management** | A feature that automatically selects the best content or offer for each customer based on real-time profile data, context, and business rules. [Learn more](../offers/get-started/starting-offer-decisioning.md) |
| **Offer** | A marketing message, discount, or promotion that can be presented to customers. Offers include eligibility rules that determine which customers can receive them. [Learn more](../offers/offer-library/creating-personalized-offers.md) |
| **Decision Policy** | A set of rules and strategies that determine which offer to show to which customer at what time, based on constraints like eligibility, priority, and capping rules. [Learn more](../experience-decisioning/create-decision.md) |

## Data & Configuration Terms {#data-config-terms}

| Term | Definition |
|------|------------|
| **Schema** | The structure that defines how data is organized in Adobe Experience Platform, including field names, data types, and relationships. Schemas ensure data consistency across systems. [Learn more](../data/get-started-schemas.md) |
| **Dataset** | A collection of data (typically a table) that follows a specific schema. Datasets store customer data, interaction events, and other information used for personalization. [Learn more](../data/get-started-datasets.md) |

>[!NOTE]
>
>For a comprehensive glossary of Adobe Experience Platform terms, refer to the [Adobe Experience Platform glossary](https://experienceleague.adobe.com/docs/experience-platform/landing/glossary.html){target="_blank"}.

## Related Topics {#related-topics}

* [Understanding how Journey Optimizer works](understanding-ajo.md)
* [Get started with the user interface](user-interface.md)
* [Choose your role and learning path](quick-start.md)

