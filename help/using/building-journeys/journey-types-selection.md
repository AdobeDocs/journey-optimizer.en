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
# Journey types: choose the right one {#journey-types-selection}

>[!BEGINSHADEBOX]

**On this page:** Learn how to compare the four journey types — unitary event, read audience, audience qualification, and business event — use the decision guide and feature compatibility matrix to choose the right one, and find links to every key section you need to build and go live.

>[!ENDSHADEBOX]

[!DNL Adobe Journey Optimizer] supports four journey types, each designed for different entry mechanisms and business scenarios. This guide helps you understand the differences and choose the right type for your use case.

## Journey types overview {#journey-types}

>[!BEGINTABS]

>[!TAB Unitary journeys]

**When to use:** Real-time, event-triggered experiences

**Unitary journeys** are triggered individually when a specific action occurs (purchase, app sign-in, form submission). Profiles enter one at a time in real-time, making this ideal for immediate, behavior-driven responses.

**Perfect for:** Order confirmations after purchase, welcome emails when someone subscribes, cart abandonment triggered by browsing, and password reset notifications.

➡️ [Learn about events](../event/about-events.md) | [Message to subscribers use case](message-to-subscribers-uc.md) | [Build a Unitary event journey](#build-unitary-event)

>[!TAB Read Audience journeys]

**When to use:** Scheduled campaigns to audience segments

**Read Audience journeys** start with an [!DNL Adobe Experience Platform] audience and send messages in batch to all profiles simultaneously. This journey type is ideal for scheduled, large-scale communications.

**Perfect for:** Monthly newsletters, promotional campaigns to target segments, product announcements, and seasonal marketing campaigns.

➡️ [Learn about Read Audience](read-audience.md) | [Get started with audiences](../audience/about-audiences.md) | [Build a Read Audience journey](#build-read-audience)

>[!TAB Audience Qualification journeys]

**When to use:** Real-time responses to audience membership changes

**Audience Qualification journeys** trigger when profiles qualify for (or exit from) a specific audience. Profiles enter individually as they meet criteria in real-time, enabling immediate engagement when customer behavior changes.

**Perfect for:** VIP tier upgrade notifications, re-engagement when customers become inactive, first purchase celebration messages, and geographic targeting when customers move.

➡️ [Learn about Audience Qualification](audience-qualification-events.md) | [Creating audiences](../audience/creating-a-segment-definition.md) | [Build an Audience Qualification journey](#build-audience-qualification)

>[!TAB Business event journeys]

**When to use:** Business conditions affecting multiple customers

**Business event journeys** are triggered by business-level events (stock updates, weather alerts, price changes) that affect multiple profiles simultaneously. These respond to broader business conditions rather than individual actions.

**Perfect for:** Low inventory alerts to interested customers, flash sale announcements, weather-based promotions, price drop notifications, and product back-in-stock alerts.

➡️ [Learn about business events](../event/about-creating-business.md) | [Entry management](entry-management.md) | [Build a Business event journey](#build-business-event)

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

>[!NOTE]
>
>Jump activity limitations: a journey starting with a Read Audience or Audience Qualification activity cannot contain a Jump activity, and cannot be the target of a Jump activity from another journey.

## Build your journey {#build-your-journey}

Once you have chosen a journey type, use this documentation map to configure prerequisites, build on the canvas, validate, publish, and manage your journey. Jump to your journey type in [Build by journey type](#build-by-type), or follow the full lifecycle below.

### Documentation hubs {#documentation-hubs}

Start from these overview pages, then drill into the sections that match your use case:

* [Create a journey](../../rp_landing_pages/create-journey-landing-page.md) — create, design, test, and publish
* [Manage your journeys](../../rp_landing_pages/manage-journey-landing-page.md) — browse, entry rules, optimization, lifecycle
* [Journey activities](../../rp_landing_pages/about-journey-building-landing-page.md) — entry, orchestration, action, and data activities
* [Journey configuration](../../rp_landing_pages/configure-journeys-landing-page.md) — events, data sources, and actions prerequisites
* [Journey use cases](../../rp_landing_pages/journey-use-cases-landing-page.md) — step-by-step recipes
* [Monitor & troubleshoot journeys](../../rp_landing_pages/troubleshoot-journey-landing-page.md) — reporting, errors, and diagnostics

### Configure prerequisites {#configure-prerequisites}

What you configure before opening the canvas depends on your journey type. See [Get started with journeys configuration](../configuration/about-data-sources-events-actions.md) for the full picture.

**Events** (Unitary event and Business event journeys)

* [Work with journey events](../event/about-events.md)
* [Configure a unitary event](../event/about-creating.md)
* [About ExperienceEvent schemas](../event/experience-event-schema.md)
* [Configure a business event](../event/about-creating-business.md)
* [Send events to Journey Optimizer](../event/additional-steps-to-send-events-to-journey.md)
* [Work with Adobe Analytics data](../event/about-analytics.md)

**Audiences** (Read Audience and Audience Qualification journeys)

* [Get started with audiences](../audience/about-audiences.md)
* [Create an audience](../audience/creating-a-segment-definition.md)

**Data sources** (optional — enrich conditions and personalization)

* [Get started with data sources](../datasource/about-data-sources.md)
* [Configure a data source](../datasource/configure-data-sources.md)
* [Adobe Experience Platform data source](../datasource/adobe-experience-platform-data-source.md)
* [External data sources](../datasource/external-data-sources.md)

**Actions and channels**

* [Get started with communication channels](../channels/gs-channels.md)
* [Action activity](journey-action.md) — built-in email, push, SMS, in-app, web, and content card actions
* [Get started with custom actions](../action/action.md)
* [Configure a custom action](../action/about-custom-action-configuration.md)
* [Adobe Campaign Standard action](../action/acs-action.md) | [Campaign v7/v8 action](../action/acc-action.md) | [Marketo Engage action](../action/marketo-engage.md)

### Create and design {#create-and-design}

* [Create your first journey](journey-gs.md) — end-to-end walkthrough from entry to publish
* [Set your journey properties](journey-properties.md) — name, re-entrance, namespace, and caps
* [Design your journey](using-the-journey-designer.md) — canvas, palette, and versioning
* [Get started with journey activities](about-journey-activities.md) — how activities connect on the canvas
* [Send using waves in journeys](send-using-waves.md) — stagger large Read Audience sends
* [Configure and track journey metrics](success-metrics.md) — define success KPIs

### Journey activities {#journey-activities}

**Event activities**

* [General events](general-events.md) — unitary event entry inside a journey
* [Reaction events](reaction-events.md) — respond to profile behavior after entry
* [Audience Qualification](audience-qualification-events.md) — entry or in-journey qualification
* [Read Audience](read-audience.md) — batch entry, schedule, and incremental read

**Orchestration activities**

* [Get started with the Optimize activity](optimize.md)
* [Path experimentation](path-experimentation.md) — A/B testing (not supported on Business event entry journeys)
* [Path targeting](path-targeting.md)
* [Conditions](conditions.md)
* [Wait](wait-activity.md)
* [Jump](jump.md) — connect sub-journeys (not available on Read Audience or Audience Qualification entry journeys)
* [Journey Fragments](journey-fragments.md)

**Action activities**

* [Action](journey-action.md)
* [Content decision](content-decision.md)
* [Custom actions](using-custom-actions.md)
* [Adobe Campaign Standard actions](using-adobe-campaign-standard.md)
* [Adobe Campaign v7/v8 actions](using-adobe-campaign-v7-v8.md)

**Data activities**

* [Dataset lookup](dataset-lookup.md)
* [Update profile](update-profiles.md)

### Validate before going live {#validate-journey}

* [Test your journey](testing-the-journey.md) — test mode with test profiles
* [Journey Dry run](journey-dry-run.md) — run against production data without contacting customers
* [Get started with journey simulation](simulate-journey-gs.md) | [Simulate your journey](simulate-journey.md)

### Publish, manage, and optimize {#publish-and-manage}

* [Publish your journey](publish-journey.md)
* [Pause a journey](journey-pause.md) | [End your journey](end-journey.md)
* [Browse and filter your journeys](journey-ui.md) | [Organize with tags](tags.md)
* [Profile entrance in journeys](entry-management.md) — throughput, re-entrance, and entry rules by type
* [Journey entry and exit criteria](entry-exit-criteria-guide.md)
* [Use supplemental identifiers](supplemental-identifier.md) — Unitary event and Read Audience journeys
* [Time zone management](timezone-management.md) | [Send-Time optimization](send-time-optimization.md)
* [Live report in your journey](report-journey.md) | [Work with journey step events](../reports/journey-step-events-overview.md)

### Build by journey type {#build-by-type}

#### Unitary event journeys {#build-unitary-event}

| Step | Documentation |
|------|---------------|
| **Configure** | [Configure a unitary event](../event/about-creating.md) → [Send events](../event/additional-steps-to-send-events-to-journey.md) |
| **Entry** | [General events](general-events.md) or unitary event as the journey entry activity |
| **Orchestrate** | [Conditions](conditions.md), [Wait](wait-activity.md), [Reaction events](reaction-events.md), [Jump](jump.md) |
| **Send messages** | [Action activity](journey-action.md) or [Custom actions](using-custom-actions.md) |
| **Enrich** | [Data sources](../datasource/about-data-sources.md), [Dataset lookup](dataset-lookup.md) |
| **Use cases** | [Send a message to subscribers](message-to-subscribers-uc.md) · [Send multi-channel messages](journeys-uc.md) |
| **Manage** | [Profile entrance](entry-management.md) · [Supplemental identifiers](supplemental-identifier.md) |

#### Read Audience journeys {#build-read-audience}

| Step | Documentation |
|------|---------------|
| **Configure** | [Create an audience](../audience/creating-a-segment-definition.md) in [!DNL Adobe Experience Platform] |
| **Entry** | [Read Audience activity](read-audience.md) — schedule, recurring runs, [incremental read](read-audience.md) |
| **Orchestrate** | [Conditions](conditions.md), [Wait](wait-activity.md), [Path experimentation](path-experimentation.md) |
| **Send messages** | [Action activity](journey-action.md) · [Send using waves](send-using-waves.md) for large audiences |
| **Use cases** | [Send multi-channel messages](journeys-uc.md) · [Send emails only on weekdays](weekday-email-uc.md) · [Ramp up deliveries](ramp-up-deliveries-uc.md) |
| **Manage** | [Profile entrance](entry-management.md) — once per execution · [Time zone management](timezone-management.md) |

#### Audience Qualification journeys {#build-audience-qualification}

| Step | Documentation |
|------|---------------|
| **Configure** | [Create a streaming audience](../audience/creating-a-segment-definition.md) — batch audiences delay entry up to 24 hours |
| **Entry** | [Audience Qualification activity](audience-qualification-events.md) — entry or exit qualification |
| **Orchestrate** | [Conditions](conditions.md), [Wait](wait-activity.md), [Reaction events](reaction-events.md) |
| **Expressions** | [inAudience function](functions/functioninaudience.md) for in-journey audience checks |
| **Use cases** | [Journey entry and exit criteria](entry-exit-criteria-guide.md) · [Learn through use cases](jo-use-cases.md) |
| **Manage** | [Profile entrance](entry-management.md) — re-entrance and namespace (required) |

#### Business event journeys {#build-business-event}

| Step | Documentation |
|------|---------------|
| **Configure** | [Configure a business event](../event/about-creating-business.md) → [Send events](../event/additional-steps-to-send-events-to-journey.md) |
| **Entry** | Business event trigger + automatic [Read Audience](read-audience.md) step for profile ingestion |
| **Orchestrate** | [Conditions](conditions.md), [Wait](wait-activity.md), [Jump](jump.md) — no [path experiments](path-experimentation.md) |
| **Throughput** | Business event trigger: 5,000 TPS · Read Audience ingestion: 20,000 TPS per sandbox — see [Profile entrance](entry-management.md) |
| **Use cases** | [Limit throughput with external data sources](limit-throughput.md) · [Learn through use cases](jo-use-cases.md) |
| **Manage** | [Profile entrance](entry-management.md) · [Namespace configuration](journey-properties.md) (required) |

### Expressions and advanced logic {#expressions}

* [Work with the advanced expression editor](expression/expressionadvanced.md)
* [Generate expressions with the Expression Assistant](expression/expression-agent.md)
* [Expression syntax and functions](../../rp_landing_pages/building-advanced-conditions-journeys-landing-page.md)
* [Experience event lookup](exp-event-lookup.md)

### Use cases and tutorials {#use-cases}

* [Learn through use cases](jo-use-cases.md) — hub with videos and recipes
* [Send multi-channel messages](journeys-uc.md)
* [Send a message to subscribers](message-to-subscribers-uc.md)
* [Send a message using Campaign v7/v8](ajo-ac.md)
* [Send emails only on weekdays](weekday-email-uc.md)
* [Pass collections into custom action parameters](collections.md)
* [Limit throughput with external data sources & custom actions](limit-throughput.md)
* [Use custom actions to write journey events in Experience Platform](custom-action-aep.md)

### Report, monitor, and troubleshoot {#report-troubleshoot}

* [Tracking in Journey Optimizer](../start/get-started-tracking.md)
* [Live reporting](../reports/live-report.md) | [Journey step events](../reports/journey-step-events-overview.md)
* [Error codes reference](error-codes-reference.md) | [System alerts](../reports/alerts.md)
* [Troubleshoot journey errors](troubleshooting.md) | [Troubleshoot journey execution](troubleshooting-execution.md) | [Troubleshoot inbound actions](troubleshooting-inbound.md)
* [Troubleshoot custom actions](../action/troubleshoot-custom-action.md)
* [Guardrails & limitations](../start/guardrails.md) | [Journey Orchestration FAQ](journey-faq.md)

### Still deciding? {#still-deciding}

* **[Get started with journeys](journey.md)** — fundamentals, designer, and capabilities overview
* **[Journeys vs Campaigns](../start/journeys-vs-campaigns.md)** — when to use journeys vs Action, API-triggered, or Orchestrated campaigns
* **[Work with Journey Optimizer APIs](../configuration/ajo-apis.md)** — automate journey operations
* **[Get started with access control](../administration/permissions-overview.md)** — permissions for journey authors

+++ AI Knowledge Reference

This section contains structured knowledge intended to support interpretation, retrieval, and question answering related to this topic.

For complete understanding, this information should be combined with the documentation on this page. Neither source is intended to stand alone; the page describes the feature, while this section provides additional context that helps disambiguate terminology, intent, applicability, and constraints.

* **TL;DR:** This page compares the four AJO journey types, provides a decision guide and feature compatibility matrix, and links to the full Journeys documentation map — configuration, activities, validation, publishing, use cases, and troubleshooting — so users can choose a type and start implementing.

**Intents:**

* Understand how to start implementing each journey type using the build paths and workflow links
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
* Profile re-entrance in Read Audience journeys is limited to once per execution
* Audience Qualification and Read Audience journeys cannot contain a Jump activity, and cannot be the target of a Jump activity from another journey
* Audience Qualification journeys require a streaming-evaluated audience for real-time entry; batch-evaluated audiences cause entry delays of up to 24 hours
* Unitary event and Audience Qualification journeys share a 5,000 TPS throughput limit at the organization level; Read Audience journeys support up to 20,000 TPS per sandbox
* A profile already present in a journey cannot re-enter the same version of that journey, regardless of re-entrance configuration

**Terminology:**

* Canonical name: Unitary event journey — variants: event-triggered journey, unitary journey
* Canonical name: Read Audience journey — variants: batch journey, segment trigger journey, read segment journey
* Canonical name: Audience Qualification journey — variants: audience qualification event journey
* Canonical name: Business event journey — variants: business event-triggered journey
* Do not confuse: "Read Audience journey" ≠ "Audience Qualification journey" — Read Audience processes all audience members in batch on schedule; Audience Qualification responds to individual membership changes in real time (streaming audiences only for immediate entry)
* Do not confuse: "Unitary event journey" ≠ "Business event journey" — Unitary is triggered by a customer action affecting one profile; Business event is triggered by a business condition and ingests multiple profiles via an internal Read Audience step

**FAQ:**

* **Q: Which journey type should I use for a monthly newsletter?** — Use a Read Audience journey; it is designed for scheduled batch communication to all profiles in an audience segment simultaneously.
* **Q: Which journey type handles an order confirmation after a purchase?** — Use a Unitary event journey; it provides an immediate real-time response to an individual customer action.
* **Q: Can I run A/B path experiments in a Business event journey?** — No; path experiments are not supported for Business event journeys.
* **Q: What is the difference between a Unitary event journey and an Audience Qualification journey?** — A Unitary event journey is triggered by a specific customer action (e.g., purchase); an Audience Qualification journey triggers when a profile enters or exits an audience segment based on streaming criteria evaluation.
* **Q: Which journey types support incremental read?** — Only Read Audience journeys support incremental read; the other three journey types do not.
* **Q: Can I use a Jump activity in a Read Audience journey?** — No; journeys starting with a Read Audience or Audience Qualification activity cannot contain a Jump activity and cannot be the target of a Jump from another journey.
* **Q: My Audience Qualification journey is not triggering in real time. Why?** — Audience Qualification journeys require a streaming-evaluated audience. If the audience is batch-evaluated (e.g., a daily snapshot), entry is delayed until the next evaluation window, which can be up to 24 hours.
* **Q: What is the throughput difference between Unitary event and Read Audience journeys?** — Unitary event journeys share a 5,000 TPS limit with Audience Qualification journeys at the organization level. Read Audience journeys support up to 20,000 TPS per sandbox, making them better suited for large-scale batch campaigns.

+++
