---
solution: Journey Optimizer
product: journey optimizer
title: Journey types and selection guide
description: Compare journey types and choose the right one for your use case with decision guides and feature compatibility matrix
feature: Journeys, Get Started, Overview
role: User
level: Beginner
keywords: journey types, unitary, read audience, audience qualification, business event, comparison, decision guide, choose, selection, real-time, scheduled, batch, event-triggered
version: Journey Orchestration
hide: yes
hidefromtoc: yes
exl-id: 0c894dc1-76b6-4b33-baf8-eaf6686f7d38
---
# Journey types and selection guide {#journey-types-selection}

[!DNL Adobe Journey Optimizer] supports four journey types, each designed for different entry mechanisms and business scenarios. This guide helps you understand the differences and choose the right type for your use case.

## Journey types overview {#journey-types}

>[!BEGINTABS]

>[!TAB Unitary journeys]

**When to use:** Real-time, event-triggered experiences

**Unitary journeys** are triggered individually when a specific action occurs (purchase, app sign-in, form submission). Profiles enter one at a time in real-time, making this ideal for immediate, behavior-driven responses.

**Perfect for:** Order confirmations after purchase, welcome emails when someone subscribes, cart abandonment triggered by browsing, and password reset notifications.

➡️ [Learn about events](../event/about-events.md) | [Message to subscribers use case](message-to-subscribers-uc.md)

>[!TAB Read Audience journeys]

**When to use:** Scheduled campaigns to audience segments

**Read Audience journeys** start with an [!DNL Adobe Experience Platform] audience and send messages in batch to all profiles simultaneously. This journey type is ideal for scheduled, large-scale communications.

**Perfect for:** Monthly newsletters, promotional campaigns to target segments, product announcements, and seasonal marketing campaigns.

➡️ [Learn about Read Audience](read-audience.md) | [Get started with audiences](../audience/about-audiences.md)

>[!TAB Audience Qualification journeys]

**When to use:** Real-time responses to audience membership changes

**Audience Qualification journeys** trigger when profiles qualify for (or exit from) a specific audience. Profiles enter individually as they meet criteria in real-time, enabling immediate engagement when customer behavior changes.

**Perfect for:** VIP tier upgrade notifications, re-engagement when customers become inactive, first purchase celebration messages, and geographic targeting when customers move.

➡️ [Learn about Audience Qualification](audience-qualification-events.md) | [Creating audiences](../audience/creating-a-segment-definition.md)

>[!TAB Business event journeys]

**When to use:** Business conditions affecting multiple customers

**Business event journeys** are triggered by business-level events (stock updates, weather alerts, price changes) that affect multiple profiles simultaneously. These respond to broader business conditions rather than individual actions.

**Perfect for:** Low inventory alerts to interested customers, flash sale announcements, weather-based promotions, price drop notifications, and product back-in-stock alerts.

➡️ [Learn about business events](../event/about-creating-business.md) | [Entry management](entry-management.md)

>[!ENDTABS]

## Decision guide: Choosing your journey type {#decision-guide}

Follow this decision tree to select the right journey type for your use case:

### Step 1: What triggers the journey?

* **Customer performs specific action** (purchase, click, login) → Go to Step 2
* **Time/schedule** (send at specific time or recurring) → **Use Read Audience journey**
* **Customer status changes** (joins/leaves a segment) → Go to Step 3
* **Business condition** (stock level, price change, weather) → **Use Business event journey**

### Step 2: Individual customer action triggers

* **Is immediate, real-time response needed?** 
  * Yes → **Use Unitary journey**
  * No → Consider Read Audience journey with scheduled execution

### Step 3: Customer status changes

* **Need to respond when customers enter OR exit a segment?**
  * Yes → **Use Audience Qualification journey**
  * No, only when entering → Consider Unitary journey with event or Read Audience with audience filter

### Quick selection by use case

| Your goal | Recommended journey type | Why |
|-----------|------------------------|-----|
| Send order confirmation after purchase | Unitary | Immediate response to individual action |
| Send monthly newsletter to subscribers | Read Audience | Scheduled batch communication |
| Notify customers when they reach VIP status | Audience Qualification | Real-time response to status change |
| Alert customers about low stock on watched items | Business event | Business condition affects multiple customers |
| Welcome new app users | Unitary | Triggered by signup event |
| Re-engage inactive customers | Audience Qualification | Responds to inactivity segment entry |
| Seasonal promotion to target segment | Read Audience | Scheduled campaign to audience |
| Flash sale announcement | Business event | Business decision affects multiple customers |

>[!NOTE]
>
>Not sure which type to choose? Start with **Unitary journeys** for event-based experiences or **Read Audience journeys** for scheduled campaigns—these cover most common use cases.

## Journey types detailed comparison {#journey-types-comparison}

Use this table to quickly compare journey types and choose the right one for your use case:

| Aspect | Unitary journeys | Read Audience journeys | Audience Qualification journeys | Business event journeys |
|--------|------------------|------------------------|--------------------------------|------------------------|
| **Entry mechanism** | Individual event trigger | Scheduled batch | Real-time audience membership change | Business-level event |
| **Entry timing** | Real-time, as events occur | Scheduled (one-time or recurring) | Real-time, as qualification occurs | Real-time, when business event fires |
| **Profile entry** | One at a time | All at once (batch) | One at a time | Multiple profiles simultaneously |
| **Trigger source** | Customer action (purchase, click, login) | Time-based schedule | Audience membership (entry/exit) | Business condition (stock, weather, price) |
| **Best for** | Transactional messages, behavioral responses | Marketing campaigns, newsletters | Loyalty programs, lifecycle stages | Inventory alerts, promotions, business conditions |
| **Use when** | Immediate response to individual actions needed | Reaching large audience segments on schedule | Responding to customer status changes | Business events affect multiple customers |
| **Examples** | Order confirmation, password reset | Monthly newsletter, seasonal campaign | VIP upgrade, inactivity alert | Low stock alert, flash sale, price drop |
| **Re-entrance** | Configurable (allow multiple entries per profile) | Each profile enters once per execution | Configurable per qualification event | Multiple profiles can be affected by same event |
| **Data requirements** | Event schema with trigger data | [!DNL Adobe Experience Platform] audience | Streaming or batch audience | Business event schema |

## Feature compatibility by journey type {#feature-compatibility}

Not all features are available for all journey types. Use this matrix to understand which capabilities work with which journey types:

| Feature / Capability | Unitary | Read Audience | Audience Qualification | Business event |
|---------------------|:-------:|:-------------:|:----------------------:|:--------------:|
| **Entry mechanisms** | | | | |
| Event-triggered entry | ✅ | ❌ | ❌ | ✅ |
| Scheduled entry | ❌ | ✅ | ❌ | ❌ |
| Audience-based entry | ❌ | ✅ | ✅ | ❌ |
| **Orchestration features** | | | | |
| Wait activities | ✅ | ✅ | ✅ | ✅ |
| Condition activities | ✅ | ✅ | ✅ | ✅ |
| Custom actions | ✅ | ✅ | ✅ | ✅ |
| Read audience activity (inside journey) | ✅ | ✅ | ✅ | ✅ |
| Audience qualification activity | ✅ | ✅ | ✅ | ✅ |
| Jump activity | ✅ | ✅ | ✅ | ✅ |
| **Profile management** | | | | |
| Profile re-entrance | ✅ Configurable | ❌ Once per execution | ✅ Configurable | ✅ Per event |
| Namespace configuration | ✅ Required | ✅ Optional | ✅ Required | ✅ Required |
| Profile cap | ✅ | ✅ | ✅ | ✅ |
| **Testing & optimization** | | | | |
| Test mode | ✅ | ✅ | ✅ | ✅ |
| Dry run | ✅ | ✅ | ✅ | ✅ |
| Path experiments (A/B testing) | ✅ | ✅ | ✅ | ❌ |
| Send-time optimization | ✅ | ✅ | ✅ | ✅ |
| **Channels** | | | | |
| Email | ✅ | ✅ | ✅ | ✅ |
| Push notifications | ✅ | ✅ | ✅ | ✅ |
| SMS / MMS | ✅ | ✅ | ✅ | ✅ |
| In-app messages | ✅ | ✅ | ✅ | ✅ |
| Web | ✅ | ✅ | ✅ | ✅ |
| Content cards | ✅ | ✅ | ✅ | ✅ |
| **Advanced capabilities** | | | | |
| Incremental read | ❌ | ✅ | ❌ | ❌ |
| Export audience | ✅ | ✅ | ✅ | ✅ |
| Time zone management | ✅ | ✅ | ✅ | ✅ |
| Reaction events | ✅ | ✅ | ✅ | ✅ |
| External data sources | ✅ | ✅ | ✅ | ✅ |
| Throttling / Capping | ✅ | ✅ | ✅ | ✅ |

**Legend:** ✅ = Supported | ❌ = Not supported

## Next steps {#next-steps}

Now that you understand journey types, you're ready to:

* **[Create your first journey](journey-gs.md)** - Step-by-step guide
* **[Learn about the journey designer](using-the-journey-designer.md)** - Design your journey canvas
* **[Explore journey capabilities](journey.md#capabilities)** - Discover advanced features
* **[View journey FAQ](journey-faq.md)** - Common questions answered

**Need to compare with campaigns?**

* [Journeys vs Campaigns comparison guide](../start/journeys-vs-campaigns.md) - Choose between journeys, Action/API campaigns, and Orchestrated campaigns
