---
solution: Journey Optimizer
product: journey optimizer
title: Journey Optimizer packages and capabilities
description: Understand how Adobe Journey Optimizer is packaged and which capabilities are available based on your base offer, channel add-ons, and advanced capability add-ons.
feature: Get Started
topic: Content Management
role: Admin, User
level: Beginner
keywords: journey optimizer, package, license, campaigns, journeys, channels, decisioning, outbound, mobile, web, modular
hide: true
---

# Adobe Journey Optimizer packages and capabilities {#ajo-packages-v2}

>[!BEGINSHADEBOX]

**On this page:** Learn how the modular Adobe Journey Optimizer packaging works across base offers, channel add-ons, and the Decisioning add-on, so you can choose the combination that fits your engagement use cases and budget.

>[!ENDSHADEBOX]

[!DNL Adobe Journey Optimizer] uses a modular packaging model. Start with the base offer that matches your primary use case, then add the channels and advanced capabilities you need.

>[!NOTE]
>
>Package availability and included capabilities may vary based on your agreement, selected add-ons, and regional availability. Contact your Adobe representative for details specific to your organization.

## Step 1 — Choose your base offer {#base-offers}

Three base offers are available. Choose the one that matches how you primarily engage customers.

| Base offer | Best for | Core behavior |
|-----------|---------|--------------|
| **Journey Optimizer – Campaigns** | Batch, marketer-planned outreach | Audience-based, scheduled orchestration. Single or multi-step campaign workflows using the Relational Datastore. |
| **Journey Optimizer – Journeys** | Real-time customer engagement | Event-driven, 1:1 orchestration. Supports both streaming and batch journey processing. |
| **Journey Optimizer – Campaigns & Journeys** | Customers needing both | Combines audience-based campaign orchestration and real-time journey orchestration. |

### Campaigns vs Journeys — what's the difference? {#campaigns-vs-journeys}

| | Journey Optimizer – Campaigns | Journey Optimizer – Journeys | Journey Optimizer – Campaigns & Journeys |
|--|:-----------------------------:|:----------------------------:|:----------------------------------------:|
| Audience-based batch orchestration | ✓ | Limited to journey use cases | ✓ |
| Real-time event-driven orchestration | — | ✓ | ✓ |
| Transactional messaging (email, push, SMS) | ✓ | ✓ | ✓ |
| Channel add-ons available | ✓ | ✓ | ✓ |
| Decisioning add-on available | ✓ | ✓ | ✓ |

>[!NOTE]
>
>Total Data Volume entitlement differs: **Campaigns** customers receive 15 KB per addressable profile; **Journeys** and **Campaigns & Journeys** customers receive 75 KB per addressable profile.

## Step 2 — Add the channels you need {#channel-addons}

Channels are not bundled into the base offer. Select the channel add-on or add-on bundle that fits your engagement strategy.

>[!BEGINTABS]

>[!TAB Outbound Delivery]

Reach audiences through outbound messaging channels.

**Includes:** email, push notifications, direct mail

**Typical use cases:** promotional emails, transactional push alerts, physical mail campaigns

**Supported surfaces:** inbox, mobile device lock screen / notification tray, postal address

Includes Deliverability Fundamentals for IP warming support on new instances. [Learn about deliverability](../reports/deliverability.md)

>[!TAB Mobile]

Engage app users with in-session and persistent mobile experiences.

**Includes:** in-app messaging, push notifications, content cards, code-based channels for mobile surfaces

**Typical use cases:** onboarding flows, feature announcements, loyalty nudges, real-time in-app offers

**Supported surfaces:** mobile app screens, notification tray, persistent content slots, custom app surfaces via SDK

>[!TAB Web]

Personalize web experiences without deploying code.

**Includes:** web channel (visual and non-visual editor), code-based channels for web surfaces

**Typical use cases:** homepage banners, landing page personalization, A/B testing, headless web personalization via API

**Supported surfaces:** browser pages, single-page apps (SPA), headless web endpoints

>[!TAB All Channels]

The **All Channels** add-on bundles Outbound Delivery + Mobile + Web in a single purchase.

Best suited for organizations that need full omnichannel coverage across outbound, mobile app, and web surfaces.

>[!ENDTABS]

**WhatsApp** is available as a separate add-on for customers who need to send messages via WhatsApp Business. [Learn how to use WhatsApp](../whatsapp/get-started-whatsapp.md)

## Step 3 — Add advanced capabilities {#advanced-addons}

### Decisioning {#decisioning-addon}

The **Decisioning** add-on enables you to define, manage, and deliver the best offer, action, or experience for each profile in real time, across any channel.

**What it unlocks:**
- Real-time offer selection using eligibility rules, ranking logic, and constraints
- AI-powered ranking models to optimize offer performance automatically
- Decisioning policies usable in journeys, campaigns, and code-based experiences

**Available on:** all three base offers, subject to your license agreement. [Learn how to use decisioning](../experience-decisioning/gs-experience-decisioning.md) | [Learn about AI models](../offers/ranking/ai-models.md)

## Compare at a glance {#comparison-matrix}

| Capability | Journey Optimizer – Campaigns | Journey Optimizer – Journeys | Journey Optimizer – Campaigns & Journeys | Add-on required |
|-----------|:-----------------------------:|:----------------------------:|:----------------------------------------:|:---------------:|
| Transactional messaging (email, push, SMS) | ✓ | ✓ | ✓ | — |
| Batch campaigns | ✓ | — | ✓ | — |
| Orchestrated campaigns _(email, SMS, push, direct mail only)_ | ✓ | — | ✓ | — |
| Automated journeys | — | ✓ | ✓ | — |
| Real-time event triggers | — | ✓ | ✓ | — |
| Email | ✓ | ✓ | ✓ | Outbound Delivery |
| Push notifications | ✓ | ✓ | ✓ | Outbound Delivery |
| Direct mail | ✓ | ✓ | ✓ | Outbound Delivery |
| SMS / MMS | ✓ | ✓ | ✓ | Outbound Delivery |
| In-app messaging | ✓ | ✓ | ✓ | Mobile |
| Content cards | ✓ | ✓ | ✓ | Mobile |
| Web channel | ✓ | ✓ | ✓ | Web |
| Code-based experiences | ✓ | ✓ | ✓ | Mobile or Web |
| WhatsApp | ✓ | ✓ | ✓ | WhatsApp |
| Decisioning | Depends on license | Depends on license | Depends on license | Decisioning |
| AI-powered ranking | Depends on license | Depends on license | Depends on license | Decisioning |

## Frequently asked questions {#faq}

+++**Does every base offer include every channel?**

No. [!DNL Adobe Journey Optimizer] uses a modular model: the base offer determines your orchestration capability (Campaigns, Journeys, or both), and channel add-ons determine which messaging surfaces you can engage. You choose the combination that fits your use case and budget.

+++

+++**What is the difference between Campaigns and Journeys?**

**Campaigns** are audience-based and marketer-planned — you define an audience, create a message, and schedule or trigger it as a batch send. They are best for promotional outreach, newsletters, and multi-step audience workflows.

**Journeys** are real-time and event-driven — they react to individual customer behavior as it happens and orchestrate 1:1 experiences across touchpoints. They are best for onboarding flows, post-purchase sequences, and real-time triggered messages.

**Campaigns & Journeys** gives you both capabilities in a single license.

+++

+++**Which channels are supported in Orchestrated campaigns?**

Orchestrated campaigns (multi-step audience workflows using the Campaign Orchestration feature) support **email, SMS, push notifications, and direct mail** only. Web, in-app, code-based, and content card channels are not supported in orchestrated campaign workflows.

+++

+++**Is Decisioning included in every configuration?**

No. Decisioning is a distinct advanced capability add-on and is not included in any base offer by default. Contact your Adobe representative to add Decisioning to your configuration.

+++

+++**I've heard of Select, Prime, or Ultimate. Are those still the current packaging model?**

[!DNL Adobe Journey Optimizer] is now offered through a modular packaging model built around base offers (Campaigns, Journeys, Campaigns & Journeys) and add-ons. If you are an existing customer using Select, Prime, or Ultimate terminology and have questions about your current entitlements, contact your Adobe representative.

+++
