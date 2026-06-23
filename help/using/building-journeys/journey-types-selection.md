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
hide: true
exl-id: 0c894dc1-76b6-4b33-baf8-eaf6686f7d38
TQID: https://experienceleague.adobe.com/rEANha6Lppyd5vog-0kZ3aL9VvZHc9kziW-d-jiWqeA
product_v2:
  - id: cb954087-f4fc-4456-afb9-e939cabcdc79
    internal-label: Journey Optimizer
feature_v2:
  - id: b3538224-471e-4c63-a444-9b19d89ae29c
    internal-label: Activities
  - id: d998adac-2f81-400b-a669-d07bb196e4eb
    internal-label: Journeys
subfeature_v2:
  - id: cce82f05-fc3c-4af7-85ff-8bba603861a7
    internal-label: Condition activities
  - id: cfba2953-2ce9-4b00-a00c-71cd338ae63f
    internal-label: Custom actions
  - id: ebd64fe4-362a-4a1c-9476-b2573ed12a95
    internal-label: Reaction events
  - id: fa683eda-48de-4558-af32-2673edcd44fe
    internal-label: Events
role_v2:
  - id: b69b2659-1057-424e-8fc5-ed9e016dc554
    internal-label: User
level_v2:
  - id: e8ccd51f-da0d-4e3b-939b-e30d5ebb1ea5
    internal-label: Beginner
topic_v2:
  - id: cdd65e7e-8839-44a2-bc21-0e03623b5dd1
    internal-label: Optimization
---
# Journey types and selection guide {#journey-types-selection}

>[!BEGINSHADEBOX]

**On this page:** Learn how to compare the four journey types — unitary, read audience, audience qualification, and business event — and use the decision guide and feature compatibility matrix to choose the right one for your use case.

>[!ENDSHADEBOX]

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

+++ AI Knowledge Reference

This section contains structured knowledge intended to support interpretation, retrieval, and question answering related to this topic.

For complete understanding, this information should be combined with the documentation on this page. Neither source is intended to stand alone; the page describes the feature, while this section provides additional context that helps disambiguate terminology, intent, applicability, and constraints.

* **TL;DR:** This page provides a comprehensive comparison of the four AJO journey types — Unitary, Read Audience, Audience Qualification, and Business Event — along with a decision guide and feature compatibility matrix to help users choose the right type for their use case.

**Intents:**

* Choose the correct journey type for a given business use case using the decision tree
* Compare journey types side by side using the detailed feature compatibility matrix
* Understand when to use Read Audience journeys for scheduled batch communications
* Understand when to use Unitary journeys for real-time, event-triggered experiences
* Understand when to use Audience Qualification journeys for real-time status-change responses
* Understand when to use Business event journeys for business-condition-driven communications

**Glossary:**

* **Unitary journey**: A journey triggered by a specific individual customer action (e.g., purchase, login) where profiles enter one at a time in real-time. *(product-specific)*
* **Read Audience journey**: A journey that starts with an Adobe Experience Platform audience and sends messages in batch to all profiles simultaneously on a schedule. *(product-specific)*
* **Audience Qualification journey**: A journey that triggers when profiles qualify for or exit a specific audience segment in real-time. *(product-specific)*
* **Business event journey**: A journey triggered by a business-level event (e.g., stock update, price change) that affects multiple profiles simultaneously. *(product-specific)*
* **Incremental read**: A Read Audience capability that processes only profiles who joined the audience since the last execution, not the full audience each time. *(product-specific)*

**Guardrails:**

* Incremental read is only available for Read Audience journeys, not for Unitary, Audience Qualification, or Business Event journeys
* Path experiments (A/B testing) are not supported for Business event journeys
* Profile re-entrance in Read Audience journeys is limited to once per execution
* Audience Qualification and Read Audience journeys cannot be used as the target of a Jump activity

**Terminology:**

* Canonical name: Unitary journey — Acronym: none — variants: event-triggered journey, unitary event journey
* Canonical name: Read Audience journey — Acronym: none — variants: batch journey, segment trigger journey, read segment journey
* Synonyms: "Audience Qualification journey" = "audience qualification event journey"
* Do not confuse: "Read Audience journey" ≠ "Audience Qualification journey" — Read Audience processes all audience members in batch on schedule; Audience Qualification responds to individual membership changes in real-time

**FAQ:**

* **Q: Which journey type should I use for a monthly newsletter?** — Use a Read Audience journey; it is designed for scheduled batch communication to all profiles in an audience segment simultaneously.
* **Q: Which journey type handles an order confirmation after a purchase?** — Use a Unitary journey; it provides an immediate real-time response to an individual customer action.
* **Q: Can I run A/B path experiments in a Business event journey?** — No; path experiments are not supported for Business event journeys.
* **Q: What is the difference between a Unitary journey and an Audience Qualification journey?** — A Unitary journey is triggered by a specific customer action (e.g., purchase); an Audience Qualification journey triggers when a profile enters or exits an audience segment based on criteria evaluation.
* **Q: Which journey types support incremental read?** — Only Read Audience journeys support incremental read; the other three journey types do not.

+++
