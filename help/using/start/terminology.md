---
solution: Journey Optimizer
product: journey optimizer
title: Key terminology
description: Essential terms and concepts in Adobe Journey Optimizer
feature: Get Started
role: Admin, Developer, User
level: Beginner
exl-id: 14e72376-87ad-4fae-bf8c-f347109d7903
TQID: https://experienceleague.adobe.com/-aDvt4RUXyf0EnPfFTJkG1CvWgte-1Fr6YaWvgcNNu4
product_v2:
  - id: cb954087-f4fc-4456-afb9-e939cabcdc79
    internal-label: Journey Optimizer
feature_v2:
  - id: d556b755-390a-43f0-be32-a08cf6236126
    internal-label: Configuration
  - id: d998adac-2f81-400b-a669-d07bb196e4eb
    internal-label: Journeys
  - id: fe338112-e2ce-4876-8989-fc4d497613f1
    internal-label: Email
subfeature_v2:
  - id: d2e8a157-b3b0-4143-9ff3-809bf400be56
    internal-label: Sandboxes
  - id: e23d48b5-7858-4d45-9c56-9e2b4be8500e
    internal-label: Business rules
  - id: fa683eda-48de-4558-af32-2673edcd44fe
    internal-label: Events
role_v2:
  - id: b69b2659-1057-424e-8fc5-ed9e016dc554
    internal-label: User
  - id: c66ffd68-0f65-42bb-aa23-b4020f12e0bd
    internal-label: Admin
  - id: ff6a42d2-313e-452e-93a6-792e4fad9ff8
    internal-label: Developer
level_v2:
  - id: e8ccd51f-da0d-4e3b-939b-e30d5ebb1ea5
    internal-label: Beginner
topic_v2:
  - id: bcc5edb5-84c3-4940-9f84-ed88b6c16274
    internal-label: Experimentation
  - id: d00e9f03-e50b-4162-b143-0c0817c937c2
    internal-label: Customer journeys
  - id: e0eb8757-182f-49f3-94a4-1587d16f5094
    internal-label: Personalization
  - id: fd2e3797-f2ea-4b36-a9af-52acf5e90513
    internal-label: Customer profiles
---
# Key Terminology {#key-terminology}

This reference guide defines the essential terms you'll encounter when using Adobe Journey Optimizer. Understanding these concepts helps you navigate the platform confidently and collaborate effectively with your team.

For pairs of similar-sounding terms that are often confused — such as **Decisioning vs Decision Management** or **Content Cards vs In-App messages** — see [When terms look similar](#disambiguation) at the bottom of this page.

>[!TIP]
>
>For detailed explanations of features and workflows, refer to the specific documentation sections linked throughout this guide.

## Core Platform Terms {#core-terms}

| Term | Definition |
|------|------------|
| **Adobe Journey Optimizer** | An application for creating and delivering personalized messages to customers across channels (email, SMS, push notifications, web). It enables you to design customer journeys that respond to real-time customer actions. |
| **Adobe Experience Platform** | The foundation of Adobe Journey Optimizer that collects and organizes all customer data in one place. It creates unified customer profiles that Journey Optimizer uses for personalization. [Learn more](https://experienceleague.adobe.com/docs/experience-platform/landing/home.html){target="_blank"} |
| **Real-time Customer Profile** | A unified, real-time view of each customer that combines data from multiple channels including online, offline, CRM, and third-party data. Each profile updates dynamically as customers interact with your brand. [Learn more](../audience/get-started-profiles.md) |
| **Sandbox** | A separate workspace for testing and experimentation without affecting live customer communications. Adobe Journey Optimizer provides multiple sandboxes for development, testing, and production environments. [Learn more](../administration/sandboxes.md) |

## Journey & Campaign Terms {#journey-campaign-terms}

| Term | Definition |
|------|------------|
| **Journey** | A series of connected steps that guide customers through experiences with your brand over time. Each step occurs based on customer actions or time triggers, enabling sequential, personalized interactions. [Learn more](../building-journeys/journey.md) |
| **Campaign** | A coordinated marketing action that delivers content to a specific audience across one or more channels. Unlike journeys, campaigns execute actions simultaneously. Journey Optimizer supports three campaign types: **Action campaigns** (scheduled batch sends), **API-triggered campaigns** (real-time, event-driven messaging via API), and **Orchestrated campaigns** (complex, multi-step workflows with a visual canvas). [Learn more](../campaigns/get-started-with-campaigns.md) |
| **Event** | An action or occurrence that triggers or advances a journey. Events can be customer actions (making a purchase, abandoning a cart) or system events (date/time, data change). [Learn more](../event/about-events.md) |
| **Channel** | The method used to communicate with customers: email, SMS, push notifications, in-app messages, web, or direct mail. Each channel requires specific configuration. [Learn more](../configuration/get-started-configuration.md) |

## Customer & Audience Terms {#customer-audience-terms}

| Term | Definition |
|------|------------|
| **Audience** | A group of customers who share common characteristics or behaviors, such as "customers who purchased in the last 30 days" or "loyalty program members." Audiences are used to target specific customer segments. [Learn more](../audience/about-audiences.md) |
| **Audience Qualification** | The automatic process that occurs when a customer joins or leaves an audience. Journey Optimizer can trigger actions when someone enters or exits an audience, ensuring timely and relevant communications. [Learn more](../building-journeys/audience-qualification-events.md) |
| **Engageable Audience** | The number of customer profiles you can actively contact through Adobe Journey Optimizer based on your license agreement. This typically refers to profiles engaged within the last 12 months. |
| **Test Profile** | Fictitious profiles used for testing and previewing messages before sending to real customers. Test profiles help verify personalization, content, and journey logic. [Learn more](../audience/creating-test-profiles.md) |

## Content & personalization terms {#content-terms}

| Term | Definition |
|------|------------|
| **Personalization** | The process of tailoring content to individual customers using their profile data, preferences, and behaviors. For example, inserting a customer's name or showing product recommendations based on browsing history. [Learn more](../personalization/personalize.md) |
| **Content Template** | A reusable message design that can be used across multiple campaigns and journeys to maintain brand consistency and accelerate content creation. [Learn more](../content-management/content-templates.md) |
| **Fragment** | A reusable content block (such as a header, footer, or promotional banner) that can be used across multiple messages to ensure consistency and enable centralized updates. [Learn more](../content-management/fragments.md) |
| **Landing Page** | A standalone web page where customers can opt-in or opt-out from communications, subscribe to services, or provide information through online forms. [Learn more](../landing-pages/get-started-lp.md) |

## Decision & offer terms {#decision-terms}

| Term | Definition |
|------|------------|
| **Decisioning** | The current-generation decision framework in Journey Optimizer, recommended for new implementations. Offers schema-based item catalog management, flexible collection rules, reusable decision components, and experimentation capabilities. Available for Code-based Experience, Push, SMS, and Email (Limited Availability). [Learn more](../experience-decisioning/gs-experience-decisioning.md) |
| **Decision Management** | The legacy offer decisioning feature in Journey Optimizer. Uses a central library of marketing offers and a rules-based decision engine that applies constraints to real-time customer profiles. Still supported for existing implementations, but new implementations should use Decisioning instead. Supports Email, In-App, Push, SMS, and Direct mail. [Learn more](../offers/get-started/starting-offer-decisioning.md) |
| **Offer** | A marketing message, discount, or promotion that can be presented to customers. Offers include eligibility rules that determine which customers can receive them. [Learn more](../offers/offer-library/creating-personalized-offers.md) |
| **Decision Policy** | A set of rules and strategies that determine which offer to show to which customer at what time, based on constraints like eligibility, priority, and capping rules. [Learn more](../experience-decisioning/create-decision.md) |

## Data & configuration terms {#data-config-terms}

| Term | Definition |
|------|------------|
| **Schema** | The structure that defines how data is organized in Adobe Experience Platform, including field names, data types, and relationships. Schemas ensure data consistency across systems. [Learn more](../data/get-started-schemas.md) |
| **Dataset** | A collection of data (typically a table) that follows a specific schema. Datasets store customer data, interaction events, and other information used for personalization. [Learn more](../data/get-started-datasets.md) |

>[!NOTE]
>
>For a comprehensive glossary of Adobe Experience Platform terms, refer to the [Adobe Experience Platform glossary](https://experienceleague.adobe.com/docs/experience-platform/landing/glossary.html){target="_blank"}.

## When terms look similar: disambiguation guide {#disambiguation}

Adobe Journey Optimizer has grown over several years, which means some feature areas share similar names. Use the tables below to quickly identify which capability fits your needs.

### Decisioning vs Decision Management {#decisioning-vs-dm}

Both capabilities select and deliver offers, but they serve different stages of the product lifecycle.

| | Decisioning | Decision Management |
|---|---|---|
| **Status** | Current — recommended for all new implementations | **Legacy** — still supported, but no longer recommended for new implementations |
| **Introduced** | 2024 | 2021 |
| **Item catalog** | Schema-based, flexible metadata | Centralized offer library |
| **Supported channels** | Code-based Experience, Push, SMS, Email (Limited Availability) | Email, In-App, Push, SMS, Direct mail |
| **Key differentiator** | Reusable decision components, experimentation, broader channel roadmap | Proven constraints engine; migrate to Decisioning for new projects |
| **Get started** | [Decisioning](../experience-decisioning/gs-experience-decisioning.md) | [Decision Management](../offers/get-started/starting-offer-decisioning.md) |
| **Migrating?** | [Migration guide](../experience-decisioning/migrate-to-decisioning.md) | — |

### Campaign types {#campaign-types-disambiguation}

Journey Optimizer offers three campaign types that are activated differently and serve distinct use cases.

| | Action campaigns | API-triggered campaigns | Orchestrated campaigns |
|---|---|---|---|
| **Also known as** | Scheduled campaigns | — | — |
| **Activation** | Manual or scheduled | External API call | Visual workflow canvas |
| **Best for** | One-off or recurring batch sends (newsletters, promotions) | Real-time, event-driven messaging (order confirmations, password resets) | Complex, multi-step cross-channel programs |
| **Personalization source** | Profile attributes | Profile attributes + API payload context | Profile attributes + relational data |
| **Get started** | [Action campaigns](../campaigns/create-campaign.md) | [API-triggered campaigns](../campaigns/api-triggered-campaigns.md) | [Orchestrated campaigns](../orchestrated/gs-orchestrated-campaigns.md) |

### Frequency capping vs journey arbitration {#capping-vs-arbitration}

Both are rule-set mechanisms under the Conflict & prioritization toolset, but they address different problems.

| | Frequency capping | Journey arbitration |
|---|---|---|
| **Problem it solves** | A profile receives too many messages over time | A profile qualifies for multiple journeys simultaneously |
| **Scope** | Per channel and communication type (Sales, Promotional, etc.) | Journey enrollment — number of concurrent journeys, or which journey wins |
| **Mechanism** | Caps the number of messages per period; automatically excludes over-solicited profiles | Uses priority scores and capping rules to decide which journey a profile enters |
| **Configured in** | Rule sets → Frequency capping | Rule sets → Journey capping & arbitration |
| **Learn more** | [Set frequency capping by channel](../conflict-prioritization/channel-capping.md) | [Manage journey capping & arbitration](../conflict-prioritization/journey-capping.md) |

### Content Cards vs In-App messages {#content-cards-vs-in-app}

Both channels deliver messages inside a mobile or web application, but they have different rendering models and persistence behaviors.

| | Content Cards | In-App messages |
|---|---|---|
| **Display model** | Persistent cards embedded in the app UI (feed, inbox, or custom surface) | Transient overlays, banners, or modals shown on top of the app |
| **Persistence** | Stays visible until explicitly dismissed or expired | Disappears after the user interacts or closes it |
| **Trigger** | SDK renders on load; rules control display and dismissal | A real-time event in the journey or campaign triggers delivery |
| **Best for** | Ongoing promotions, loyalty status, persistent alerts | Onboarding tips, limited-time offers, transient notifications |
| **Get started** | [Content Cards](../content-card/create-content-card.md) | [In-App messages](../in-app/get-started-in-app.md) |

>[!NOTE]
>
>**Adobe Journey Optimizer vs Journey Optimizer B2B Edition:** These are two separate products in the same brand family. Adobe Journey Optimizer (this documentation) targets B2C customer journeys. Journey Optimizer B2B Edition is purpose-built for account-based marketing, working with buying groups and account audiences. If you are looking for B2B Edition documentation, visit the [Journey Optimizer B2B Edition guide](https://experienceleague.adobe.com/en/docs/journey-optimizer-b2b/user/guide-overview){target="_blank"}.

## Related Topics {#related-topics}

* [Understanding how Journey Optimizer works](understanding-ajo.md)
* [Get started with the user interface](user-interface.md)
* [Choose your role and learning path](quick-start.md)
