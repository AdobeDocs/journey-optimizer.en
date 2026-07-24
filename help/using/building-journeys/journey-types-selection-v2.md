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
---

# Journey types: choose the right one {#journey-types-selection}

>[!BEGINSHADEBOX]

**On this page:** Learn about the four AJO journey types — unitary event, read audience, audience qualification, and business event — and find out which one fits your use case.

>[!ENDSHADEBOX]

[!DNL Adobe Journey Optimizer] supports four journey types, each designed for a different kind of trigger and business scenario. Understanding the difference helps you build the right experience from the start.

## The four journey types {#journey-types}

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

## Which type should you use? {#decision-guide}

The answer usually comes down to one question: *what starts the journey?*

If a **customer does something specific** — abandons a cart, signs up, makes a purchase — use a **Unitary event journey**. It fires immediately when the action happens, one profile at a time.

If you want to **reach an audience on a schedule** — a monthly newsletter, a seasonal campaign, a recurring re-engagement series — use a **Read Audience journey**. You define the audience and the timing; AJO processes everyone at once.

If you want to respond **the moment a customer reaches a milestone** — joining a loyalty tier, hitting a churn risk threshold, completing a first purchase — use an **Audience Qualification journey**. It triggers as soon as the streaming audience membership changes, not on a fixed schedule.

If something changes **in your business** that affects multiple customers at once — a stock level drops, a price changes, a sale starts — use a **Business event journey**.

>[!TIP]
>
>**Not sure where to start?** Most teams begin with **Unitary event** for behavior-triggered experiences and **Read Audience** for campaigns. These two cover the majority of use cases.

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

## Feature availability reference {#feature-compatibility}

All journey types support the full AJO channel set (email, push, SMS, in-app, web, content cards), core orchestration activities (wait, condition, custom actions), test mode, dry run, and send-time optimization. The table below shows only the capabilities that differ across types.

>[!NOTE]
>
>Jump activity limitations: a journey starting with a Read Audience or Audience Qualification activity cannot contain a Jump activity, and cannot be the target of a Jump activity from another journey.
>
>Read Audience activity as journey entry is only available in **Read Audience** and **Business event** journeys — it cannot be added to Unitary event or Audience Qualification entry journeys.

| Capability | Unitary event | Read Audience | Audience Qualification | Business event |
|-----------|:-------:|:-------------:|:----------------------:|:--------------:|
| **Entry** | | | | |
| Event-triggered entry | ✅ | ❌ | ❌ | ✅ (business event triggers the journey; profiles enter via an internal Read Audience step) |
| Scheduled entry | ❌ | ✅ | ❌ | ❌ |
| Audience-based entry | ❌ | ✅ (batch) | ✅ (streaming only) | ❌ |
| **Orchestration** | | | | |
| Read Audience activity (journey entry) | ❌ | ✅ | ❌ | ✅ (automatic step after business event) |
| Jump activity | ✅ | ❌ | ❌ | ✅ |
| **Profile management** | | | | |
| Profile re-entrance | ✅ Configurable | ❌ Once per execution by default ([Force reentrance on recurrence](read-audience.md#schedule) available) | ✅ Configurable (profile already in journey cannot re-enter same version) | ✅ Per event |
| **Optimization** | | | | |
| Path experiments (A/B testing) | ✅ | ✅ | ✅ | ❌ |
| **Advanced** | | | | |
| Incremental read | ❌ | ✅ | ❌ | ❌ |
| Max throughput | 5,000 TPS (shared org-level with Audience Qualification) | 20,000 TPS per sandbox | 5,000 TPS (shared org-level with Unitary event) | Business event: 5,000 TPS; Read Audience step: 20,000 TPS |

**Legend:** ✅ = Supported | ❌ = Not supported

## Next steps {#next-steps}

Now that you have chosen a journey type:

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
