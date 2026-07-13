---
solution: Journey Optimizer
product: journey optimizer
title: "Journey types: choose the right one"
description: Compare journey types and choose the right one for your use case with decision guides and feature compatibility matrix
feature: Journeys, Get Started, Overview
role: User
level: Beginner
keywords: journey types, unitary, read audience, audience qualification, business event, comparison, decision guide, choose, selection, real-time, scheduled, batch, event-triggered
version: Journey Orchestration
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
# Journey types: choose the right one {#journey-types-selection}

>[!BEGINSHADEBOX]

**On this page:** Learn how to compare the four journey types — unitary event, read audience, audience qualification, and business event — and use the decision guide and feature compatibility matrix to choose the right one for your use case.

>[!ENDSHADEBOX]

[!DNL Adobe Journey Optimizer] supports four journey types, each designed for different entry mechanisms and business scenarios. This guide helps you understand the differences and choose the right type for your use case.

>[!NOTE]
>
>Not sure which type to choose? Start with **Unitary event journeys** for event-based experiences or **Read Audience journeys** for scheduled campaigns — these cover most common use cases.

## Journey types overview {#journey-types}

>[!BEGINTABS]

>[!TAB Unitary event journeys]

**When to use:** Real-time, event-triggered experiences

**Unitary event journeys** are triggered individually when a specific action occurs (purchase, app sign-in, form submission). Profiles enter one at a time in real time, making this ideal for immediate, behavior-driven responses.

**Perfect for:** Cart abandonment recovery, new member onboarding, welcome emails when someone subscribes, and post-login personalization.

➡️ [Learn about events](../event/about-events.md) | [Message to subscribers use case](message-to-subscribers-uc.md) | [Create your first journey](journey-gs.md)

>[!TAB Read Audience journeys]

**When to use:** Scheduled campaigns to audience segments

**Read Audience journeys** start with an [!DNL Adobe Experience Platform] audience and send messages in batch to all profiles simultaneously. This journey type is ideal for scheduled, large-scale communications. Use the **incremental read** option on recurring journeys to process only profiles who joined the audience since the last execution, rather than re-processing the full audience each time.

**Perfect for:** Monthly newsletters, promotional campaigns to target segments, product announcements, recurring re-engagement series, and seasonal marketing campaigns.

➡️ [Learn about Read Audience](read-audience.md) | [Get started with audiences](../audience/about-audiences.md) | [Create your first journey](journey-gs.md)

>[!TAB Audience Qualification journeys]

**When to use:** Real-time responses to audience membership changes

**Audience Qualification journeys** trigger when profiles qualify for (or exit from) a specific audience. Profiles enter individually as they meet criteria, enabling immediate engagement when customer behavior changes. Use **streaming-evaluated** audiences — these are the only supported audience type for this activity.

>[!CAUTION]
>
>Starting **August 2026**, journeys using a batch audience in an Audience Qualification node cannot be published. [Learn how to migrate your journeys](aq-batch-audiences-migration.md)

**Perfect for:** VIP tier upgrade notifications, first purchase celebration messages, churn risk alerts, and loyalty lifecycle stage transitions.

➡️ [Learn about Audience Qualification](audience-qualification-events.md) | [Creating audiences](../audience/creating-a-segment-definition.md) | [Create your first journey](journey-gs.md)

>[!TAB Business event journeys]

**When to use:** Business conditions affecting multiple customers

**Business event journeys** are triggered by a business-level event (stock updates, price changes) that affects multiple profiles simultaneously. Internally, the business event trigger is always followed by a Read Audience step that ingests the relevant profiles — so profile entry follows Read Audience throughput rules, not unitary event throughput.

**Perfect for:** Low inventory alerts to interested customers, flash sale announcements, price drop notifications, and product back-in-stock alerts.

➡️ [Learn about business events](../event/about-creating-business.md) | [Entry management](entry-management.md) | [Create your first journey](journey-gs.md)

>[!ENDTABS]

## Decision guide: choosing your journey type {#decision-guide}

Use the table below to match your goal to the right journey type. For most new users, **Unitary event** or **Read Audience** journeys cover the majority of use cases.

| Your goal | Recommended journey type | Why |
|-----------|--------------------------|-----|
| Recover an abandoned cart | Unitary event | Immediate response to individual behavior |
| Send monthly newsletter to subscribers | Read Audience | Scheduled batch communication |
| Notify customers when they reach VIP status | Audience Qualification | Real-time response to streaming audience entry |
| Alert customers about low stock on watched items | Business event | Business condition affects multiple customers |
| Welcome new app users | Unitary event or Audience Qualification | Signup event (unitary event) or entry into a new-user streaming audience (Audience Qualification) |
| Re-engage inactive customers (recurring, scheduled) | Read Audience | Recurring batch run against inactivity audience |
| Seasonal promotion to target segment | Read Audience | Scheduled campaign to audience |
| Flash sale announcement | Business event | Business decision affects multiple customers |
| React as soon as a customer hits Gold loyalty tier | Audience Qualification | Streaming audience, real-time individual entry |

## Journey types detailed comparison {#journey-types-comparison}

| Aspect | Unitary event journeys | Read Audience journeys | Audience Qualification journeys | Business event journeys |
|--------|------------------------|------------------------|--------------------------------|------------------------|
| **Entry mechanism** | Individual event trigger | Scheduled batch | Real-time streaming audience membership change | Business-level event + Read Audience step |
| **Entry timing** | Real-time, as events occur | Scheduled (one-time or recurring) | Real-time, as qualification occurs (streaming audiences); delayed for batch-evaluated audiences | Real-time trigger; profile ingestion follows Read Audience throughput |
| **Profile entry** | One at a time | All at once (batch) | One at a time | Multiple profiles via internal Read Audience step |
| **Trigger source** | Customer action (purchase, click, login) | Time-based schedule | Audience membership entry or exit | Business condition (stock, price) |
| **Best for** | Transactional messages, behavioral responses | Marketing campaigns, newsletters, recurring programs | Loyalty programs, lifecycle stage transitions | Inventory alerts, promotions, business conditions |
| **Use when** | Immediate response to individual actions needed | Reaching large audience segments on schedule | Responding to customer status changes in real time | Business events affect multiple customers simultaneously |
| **Examples** | Cart abandonment recovery, new member onboarding | Monthly newsletter, seasonal campaign | VIP upgrade, churn risk alert | Low stock alert, flash sale, price drop |
| **Re-entrance** | Configurable | Once per execution by default; [Force reentrance on recurrence](read-audience.md#schedule) available on scheduled runs | Configurable per qualification event; a profile already in the journey cannot re-enter the same version | Multiple profiles can be affected by same event |
| **Max throughput** | 5,000 TPS (shared org-level with Audience Qualification) | 20,000 TPS per sandbox | 5,000 TPS (shared org-level with Unitary event) | Business event: 5,000 TPS; Read Audience step: 20,000 TPS |
| **Data requirements** | Event schema with trigger data | [!DNL Adobe Experience Platform] audience | Streaming audience required. Batch audiences deprecated from August 2026 — [migrate now](aq-batch-audiences-migration.md) | Business event schema |

## Feature compatibility by journey type {#feature-compatibility}

Not all features are available for all journey types. Use this matrix to understand which capabilities work with which journey types:

| Feature / Capability | Unitary event | Read Audience | Audience Qualification | Business event |
|---------------------|:-------:|:-------------:|:----------------------:|:--------------:|
| **Entry mechanisms** | | | | |
| Event-triggered entry | ✅ | ❌ | ❌ | ✅ (business event triggers the journey; profiles enter via an internal Read Audience step) |
| Scheduled entry | ❌ | ✅ | ❌ | ❌ |
| Audience-based entry | ❌ | ✅ (batch) | ✅ (streaming) | ❌ |
| **Orchestration features** | | | | |
| Wait activities | ✅ | ✅ | ✅ | ✅ |
| Condition activities | ✅ | ✅ | ✅ | ✅ |
| Custom actions | ✅ | ✅ | ✅ | ✅ |
| Read Audience activity (journey entry) | ❌ | ✅ | ❌ | ✅ (automatic step after business event) |
| Audience Qualification activity (inside journey) | ✅ | ✅ | ✅ | ✅ |
| Jump activity | ✅ | ❌ | ❌ | ✅ |
| **Profile management** | | | | |
| Profile re-entrance | ✅ Configurable | ❌ Once per execution by default ([Force reentrance on recurrence](read-audience.md#schedule) on scheduled runs) | ✅ Configurable (profile already in journey cannot re-enter same version) | ✅ Per event |
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
| Time zone management | ✅ | ✅ | ✅ | ✅ |
| Reaction events | ✅ | ✅ | ✅ | ✅ |
| External data sources | ✅ | ✅ | ✅ | ✅ |
| Throttling / Capping | ✅ | ✅ | ✅ | ✅ |

**Legend:** ✅ = Supported | ❌ = Not supported

>[!NOTE]
>
>Jump activity limitations: a journey starting with a Read Audience or Audience Qualification activity cannot contain a Jump activity, and cannot be the target of a Jump activity from another journey.
>
>Read Audience activity as journey entry is only available in **Read Audience** and **Business event** journeys — it cannot be added to Unitary event or Audience Qualification entry journeys.

## Next steps {#next-steps}

Now that you have chosen a journey type:

* **[Journeys vs Campaigns](../start/journeys-vs-campaigns.md)** — Not sure whether Journeys or Campaigns is the right tool? Step back up to the higher-level decision first
* **[Create your first journey](journey-gs.md)** — Step-by-step guide from entry to publish
* **[Learn about the journey designer](using-the-journey-designer.md)** — Design your journey canvas
* **[Profile entrance in journeys](entry-management.md)** — Entry rules, re-entrance, and throughput by type
* **[Get started with journeys](journey.md)** — Fundamentals and capabilities overview
* **[Journey Orchestration FAQ](journey-faq.md)** — Common questions answered

+++ AI Knowledge Reference

This section contains structured knowledge intended to support interpretation, retrieval, and question answering related to this topic.

For complete understanding, this information should be combined with the documentation on this page. Neither source is intended to stand alone; the page describes the feature, while this section provides additional context that helps disambiguate terminology, intent, applicability, and constraints.

* **TL;DR:** This page provides a comprehensive comparison of the four AJO journey types — Unitary event, Read Audience, Audience Qualification, and Business event — along with a decision guide and feature compatibility matrix to help users choose the right type for their use case.

**Intents:**

* Choose the correct journey type for a given business use case using the decision table
* Compare journey types side by side using the detailed feature compatibility matrix
* Understand when to use Read Audience journeys for scheduled batch communications
* Understand when to use Unitary event journeys for real-time, event-triggered experiences
* Understand when to use Audience Qualification journeys for real-time status-change responses
* Understand when to use Business event journeys for business-condition-driven communications
* Understand throughput limits per journey type when planning high-volume deployments

**Glossary:**

* **Unitary event journey**: A journey triggered by a specific individual customer action (e.g., purchase, login) where profiles enter one at a time in real time. *(product-specific)*
* **Read Audience journey**: A journey that starts with an Adobe Experience Platform audience and sends messages in batch to all profiles simultaneously on a schedule. *(product-specific)*
* **Audience Qualification journey**: A journey that triggers when profiles qualify for or exit a specific audience segment. Requires a streaming-evaluated audience for real-time entry behavior. *(product-specific)*
* **Business event journey**: A journey triggered by a business-level event (e.g., stock update, price change) that affects multiple profiles simultaneously; always paired with an internal Read Audience step for profile ingestion. *(product-specific)*
* **Incremental read**: A Read Audience capability that processes only profiles who joined the audience since the last execution, not the full audience each time. Available for Read Audience journeys only. *(product-specific)*
* **Streaming audience**: An Adobe Experience Platform audience evaluated continuously in real time, as opposed to a batch audience evaluated on a schedule (e.g., daily). Required for Audience Qualification journeys to achieve real-time entry behavior. *(product-specific)*

**Guardrails:**

* Incremental read is only available for Read Audience journeys, not for Unitary event, Audience Qualification, or Business event journeys
* Path experiments (A/B testing) are not supported for Business event journeys
* Profile re-entrance in Read Audience journeys is limited to once per execution by default; use Force reentrance on recurrence on scheduled runs to allow profiles to re-enter on the next execution
* The Read Audience activity is only available as a journey entry in Read Audience and Business event journeys — not in Unitary event or Audience Qualification entry journeys
* Audience Qualification and Read Audience journeys cannot contain a Jump activity, and cannot be the target of a Jump activity from another journey
* Audience Qualification journeys require a streaming-evaluated audience. Starting August 2026, batch-evaluated audiences cannot be used in an Audience Qualification node — see the [migration guide](aq-batch-audiences-migration.md)
* Unitary event and Audience Qualification journeys share a 5,000 TPS throughput limit at the organization level; Read Audience journeys support up to 20,000 TPS per sandbox
* A profile already present in a journey cannot re-enter the same version of that journey, regardless of re-entrance configuration

**Terminology:**

* Canonical name: Unitary event journey — variants: event-triggered journey, unitary journey
* Canonical name: Read Audience journey — variants: batch journey
* Canonical name: Audience Qualification journey — variants: audience qualification event journey
* Canonical name: Business event journey — variants: business event-triggered journey
* Do not confuse: "Read Audience journey" ≠ "Audience Qualification journey" — Read Audience processes all audience members in batch on schedule; Audience Qualification responds to individual membership changes in real time (streaming audiences only for immediate entry)
* Do not confuse: "Unitary event journey" ≠ "Business event journey" — Unitary is triggered by a customer action affecting one profile; Business event is triggered by a business condition and ingests multiple profiles via an internal Read Audience step

**FAQ:**

* **Q: Which journey type should I use for a monthly newsletter?** — Use a Read Audience journey; it is designed for scheduled batch communication to all profiles in an audience segment simultaneously.
* **Q: Which journey type should I use to recover an abandoned cart?** — Use a Unitary event journey; it triggers immediately when the abandonment event occurs and responds to the individual's behavior in real time.
* **Q: Can I run A/B path experiments in a Business event journey?** — No; path experiments are not supported for Business event journeys.
* **Q: What is the difference between a Unitary event journey and an Audience Qualification journey?** — A Unitary event journey is triggered by a specific customer action (e.g., purchase); an Audience Qualification journey triggers when a profile enters or exits an audience segment based on streaming criteria evaluation.
* **Q: Which journey types support incremental read?** — Only Read Audience journeys support incremental read; the other three journey types do not.
* **Q: Can I add a Read Audience activity to a Unitary event journey?** — No; the Read Audience activity is only available as journey entry in Read Audience and Business event journeys.
* **Q: Can I use a Jump activity in a Read Audience journey?** — No; journeys starting with a Read Audience or Audience Qualification activity cannot contain a Jump activity and cannot be the target of a Jump from another journey.
* **Q: Can I welcome new app users with an Audience Qualification journey?** — Yes, if entry is driven by a streaming audience (for example, when a profile joins a new-user segment); a signup unitary event journey is also a common pattern.
* **Q: My Audience Qualification journey is not triggering in real time. Why?** — Audience Qualification journeys require a streaming-evaluated audience. Using a batch-evaluated audience is deprecated and will be blocked from August 2026. [See the migration guide](aq-batch-audiences-migration.md)
* **Q: What is the throughput difference between Unitary event and Read Audience journeys?** — Unitary event journeys share a 5,000 TPS limit with Audience Qualification journeys at the organization level. Read Audience journeys support up to 20,000 TPS per sandbox, making them better suited for large-scale batch campaigns.

+++
