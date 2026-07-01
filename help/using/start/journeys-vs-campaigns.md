---
solution: Journey Optimizer
product: journey optimizer
title: Journeys vs Campaigns - Choose the right approach
description: Compare Journeys, Action campaigns, and API-triggered campaigns to choose the right approach for your marketing needs in Adobe Journey Optimizer.
feature: Journeys, Campaigns, Get Started, Overview
topic: Content Management
role: User
level: Beginner
keywords: journey, campaign, comparison, choose, decision, workflow, real-time, batch, orchestration, multi-step, scheduled, API-triggered, event-driven
exl-id: 8b4d010e-4278-49fd-a7d3-dcc706829577
TQID: https://experienceleague.adobe.com/RWLVSULVO0idnCs5OVQR1yVvNv1G0JwP3y-3sNXQg50
product_v2:
  - id: cb954087-f4fc-4456-afb9-e939cabcdc79
    internal-label: Journey Optimizer
feature_v2:
  - id: d998adac-2f81-400b-a669-d07bb196e4eb
    internal-label: Journeys
  - id: baecb07f-ce89-4ebb-9cd9-0f7c053f944f
    internal-label: Journey management
subfeature_v2:
  - id: fdac7813-bd56-47ae-9f6d-fa94ad1c5dee
    internal-label: Overview
role_v2:
  - id: b69b2659-1057-424e-8fc5-ed9e016dc554
    internal-label: User
level_v2:
  - id: e8ccd51f-da0d-4e3b-939b-e30d5ebb1ea5
    internal-label: Beginner
topic_v2:
  - id: addf009e-030a-4310-8534-776a3e62ed48
    internal-label: Customer lifecycle
  - id: bce87dde-a4ab-44c9-8a18-ad66e4ddb377
    internal-label: Customer experience
  - id: cdd65e7e-8839-44a2-bc21-0e03623b5dd1
    internal-label: Optimization
  - id: e0eb8757-182f-49f3-94a4-1587d16f5094
    internal-label: Personalization
---
# Journeys vs campaigns: choose the right approach {#journeys-vs-campaigns}

>[!BEGINSHADEBOX]

**On this page:** Compare journeys with action and API-triggered campaigns so you can choose the right approach for each marketing use case in Adobe Journey Optimizer. For Orchestrated campaigns, see [Get started with Orchestrated campaigns](../orchestrated/gs-orchestrated-campaigns.md).

>[!ENDSHADEBOX]

[!DNL Adobe Journey Optimizer] offers two main ways to reach and engage your customers: **Journeys** and **Campaigns**. Journeys are designed for real-time, multi-step orchestration driven by customer behavior, while campaigns are better suited for one-time or scheduled broadcasts to a defined audience — or for inbound channel activations to the edge for low-latency personalization. Once you have decided on a campaign, you can then choose the campaign type that best fits your use case.

This guide helps you choose between Journeys, Action campaigns, and API-triggered campaigns based on execution style, data needs, and use case — with a quick comparison, decision tree, and concrete examples.

>[!NOTE]
>
>**Orchestrated campaigns** have distinct architectural characteristics (Hub-side batch execution, multi-entity relational data) that require dedicated guidance. They are not included in the comparison tables below to avoid oversimplification. [Learn more about Orchestrated campaigns](../orchestrated/gs-orchestrated-campaigns.md)

## Quick comparison overview {#quick-overview}

| Approach | Best for | Execution style |
|----------|----------|-----------------|
| **Journeys** | Multi-step, real-time customer experiences with conditional logic | 1:1 orchestration - each profile at their own pace |
| **Action campaigns** | Scheduled or recurring activations to audiences | Batch execution - audience processed together at send time |
| **API-triggered campaigns** | Event-driven or transactional messages from external systems | On-demand execution - triggered by API call with payload |

>[!TIP]
>
>**Quick rule of thumb:** Need each customer to move at their own pace with real-time logic? Use **Journeys**. Sending one message to an audience on a schedule? Use **Action campaigns**. Triggering a single message from an external system via API? Use **API-triggered campaigns** — or a **Unitary event journey** if you need multi-step orchestration after the API-sent event. Need inbound, edge-based personalization? Use **Action campaigns**.

## Detailed comparison {#detailed-comparison}

Use this comprehensive table to understand the key differences:

| Feature | Journeys | Action campaigns | API-triggered campaigns |
|---------|----------|------------------|------------------------|
| **Primary purpose** | Multi-step 1:1 orchestration with real-time customer context | One-time or recurring message delivery to audiences | Transactional or event-driven messages initiated by external systems |
| **Canvas type** | 1:1 canvas - each profile travels at their own pace | No canvas - single action execution | No canvas - single action execution |
| **Execution flow** | Sequential actions, profile maintains state throughout journey | Simultaneous execution to entire audience | Immediate execution per API call |
| **Entry mechanism** | Events, audiences, qualifications, business events | Manual activation and schedule | API call from external system |
| **Data model** | Real-time profile + event data | Profile data from Experience Platform audiences | API payload data with optional profile lookup |
| **Segmentation** | Pre-built audiences + real-time conditions | Pre-built audiences from Experience Platform | Payload-driven targeting (no scheduled audience) |
| **Profile processing** | Individual, real-time (as events occur) | Batch, all at once | Per API call, payload-driven |
| **Personalization** | Real-time contextual data + profile attributes | Profile attributes | Payload data + optional profile attributes |
| **Complexity** | Multi-step with branching, wait times, conditions | Single action or simple workflow | Single action with payload mapping |
| **Best for** | Customer lifecycle journeys, onboarding, cart abandonment | Promotional campaigns, newsletters, announcements | Order confirmations, shipping alerts, password resets |
| **Timing** | Continuous, always active once published | Scheduled start/end dates | On-demand, event-driven via API |
| **State management** | Maintains customer state for real-time actions | Stateless execution | Stateless execution per call |
| **Use when** | Multiple touchpoints needed with real-time decision logic | Simple message to an audience at a specific time | External system needs to trigger a message immediately |
| **Unique capabilities** | Real-time reactions, wait activities, profile-based pacing | Scheduling, audience targeting, rate control | API payload mapping, system-to-system triggering |

## Decision guide {#decision-guide}

Follow this decision tree to choose the right approach. Many brands use more than one type; pick the best fit for each use case.

### Step 1: What's your execution requirement?

**Real-time, individual responses to customer behavior?**
→ **Use Journeys**
* Profiles need to move at their own pace
* Conditional logic based on behavior
* Real-time context is critical

**Simple message delivery to an audience at a scheduled time?**
→ **Use Action campaigns**
* All profiles receive message simultaneously
* Scheduled or recurring sends
* No complex multi-step logic needed

**Immediate message triggered by an external system?**
→ **Use API-triggered campaigns** (single message) **or a Unitary event journey** (multi-step orchestration)
* Triggered on demand via API call — campaigns deliver one message; unitary journeys ingest the event via [Experience Platform ingestion](../event/additional-steps-to-send-events-to-journey.md) and run a full journey flow
* Payload-driven personalization
* Choose campaigns when no multi-step logic is needed

**Complex batch workflow with advanced segmentation, multi-entity data, or exact pre-send counts?**
→ **Use Orchestrated campaigns** — see [Get started with Orchestrated campaigns](../orchestrated/gs-orchestrated-campaigns.md) for detailed guidance.

>[!NOTE]
>
>* **Ad-hoc audience composition** — Orchestrated campaigns let you define your target audience directly in the campaign canvas using the built-in rule builder, without needing to pre-create and evaluate an Adobe Experience Platform audience first. [Learn how to build your first rule](../orchestrated/build-query.md)
>* **Federated data** — Use Federated Audience Composition to query your enterprise data warehouse and build or enrich audiences without importing sensitive data into Adobe Experience Platform. [Learn about Federated Audience Composition](../audience/federated-audience-composition.md)

### Step 2: Validate your choice

| Your need | Recommended approach | Why |
|-----------|---------------------|-----|
| Welcome new customers with multi-step onboarding | Journeys | Real-time entry, multiple touchpoints, conditional paths |
| Send monthly newsletter to subscribers | Action campaigns | Simple scheduled message to audience |
| Cart abandonment with reminder sequence | Journeys | Real-time trigger, wait times, conditional follow-up |
| Promotional announcement to all customers | Action campaigns | One-time message, immediate delivery |
| Re-engage inactive users based on behavior | Journeys | Triggered by audience qualification, personalized path |
| Flash sale triggered by business event | Journeys (Business Event) | Real-time trigger affecting multiple customers |
| API-triggered transactional message (single send) | API-triggered campaigns | External system trigger, immediate one-shot delivery |
| API-triggered multi-step flow | Journeys (Unitary event) | External system sends unitary event via API; journey orchestrates follow-up steps |
| Complex batch workflow with multi-entity data | Orchestrated campaigns | See [Get started with Orchestrated campaigns](../orchestrated/gs-orchestrated-campaigns.md) |

## Key distinctions explained {#key-distinctions}

### Journeys: 1:1 Real-time orchestration

**What makes it unique:**
* Each profile maintains individual state and context
* Profiles enter and progress at their own pace
* Real-time decision-making based on behavior and events
* Wait activities create personalized timing
* Conditional branching creates unique paths per profile
* Built-in active listening — inaction for a defined period can also trigger the next step, not just explicit events. [Learn about wait activities](../building-journeys/wait-activity.md)
* Frequency capping — control how often a customer can enter or receive messages from a journey. [Learn about journey capping](../conflict-prioritization/journey-capping.md)
* Audience splitting by percentage — divide profiles into random, percentage-based groups to run A/B experiments across journey paths. [Learn about percentage split](../building-journeys/condition-activity.md)
* Test mode — validate journey logic and message delivery with test profiles before publishing live. [Learn about test mode](../building-journeys/testing-the-journey.md)

**Example flow:**

```
Customer A: Abandoned cart → Wait 2 hours → No purchase? → Send reminder → Purchased? → End
Customer B: Abandoned cart → Wait 2 hours → Already purchased → End immediately
```

Each customer experiences their own journey timeline based on their actions.

[Learn more about Journeys](../building-journeys/journey.md) | [Journey types: choose the right one](../building-journeys/journey-types-selection.md)

### Campaigns: Simple batch or triggered delivery

**What makes it unique:**
* All profiles processed identically and simultaneously
* Stateless execution - no context maintained
* Simple scheduling or API triggering
* Ideal for broadcast communications
* Multi-surface inbound delivery — Add up to 10 inbound channel actions (Code-based experience, In-app, Content Card, Web) in a single campaign, using targeting rules to create message variants based on audience membership or profile attributes. [Learn more](../campaigns/campaign-action.md#multi-action)

**Example flow:**

```
Monday 9 AM → Send newsletter to 100,000 subscribers → All receive simultaneously
```

Everyone gets the same message at the same time.

**Types:**
* **Action campaigns**: Scheduled delivery to audiences (one-time or recurring)
* **API-triggered campaigns**: On-demand delivery triggered by an API call with payload data

[Learn more about Campaigns](../campaigns/get-started-with-campaigns.md)

## Use case examples {#use-cases}

### Journey use cases

* **Cart abandonment recovery**: Triggered by cart add event, wait for checkout, send reminders if no purchase
* **Customer onboarding**: Multi-step welcome series with personalized content based on profile data
* **Loyalty tier upgrade**: Triggered when customer reaches new tier, send congratulations and benefits
* **Birthday campaigns**: Entry based on birthdate, personalized offers
* **Re-engagement**: Triggered by audience qualification (inactivity), progressive outreach

### Campaign use cases (action & API-triggered)

**Action campaigns:**
* **Monthly newsletters**: Scheduled batch delivery to subscriber segment
* **Promotional announcements**: Time-sensitive offers to target audiences
* **Product launches**: Coordinated announcement to all customers
* **Seasonal greetings**: Holiday messages on specific dates

**API-triggered campaigns:**
* **Order confirmations**: Triggered by e-commerce system after purchase
* **Shipping notifications**: Triggered by logistics system
* **Account alerts**: Triggered by fraud detection system
* **Password resets**: Triggered by user action in application

## Feature availability {#feature-availability}

### Channels

| Channel | Journeys | Action campaigns | API-triggered campaigns |
|---------|:--------:|:----------------:|:-----------------------:|
| Email | ✅ | ✅ | ✅ |
| Push | ✅ | ✅ | ✅ |
| SMS | ✅ | ✅ | ✅ |
| In-app | ✅ | ✅ | ✅ |
| Web | ✅ | ✅ | ❌ |
| Code-based | ✅ | ✅ | ❌ |
| Content cards | ✅ | ✅ | ❌ |
| Direct mail | ✅ | ✅ | ❌ |
| LINE | ✅ | ✅ | ✅ |
| WhatsApp | ✅ | ✅ | ✅ |

>[!NOTE]
>
>For Orchestrated campaigns channel availability, see [Channels in journeys & campaigns](../channels/gs-channels.md#channels).

### Advanced capabilities

| Capability | Journeys | Action campaigns | API-triggered campaigns |
|-----------|:--------:|:----------------:|:-----------------------:|
| Multi-step workflows | ✅ | ❌ | ❌ |
| Real-time triggers | ✅ | ❌ | ✅ |
| Wait activities | ✅ | ❌ | ❌ |
| Conditional branching | ✅ | ❌ | ❌ |
| Scheduled execution | ✅ | ✅ | ✅ |
| API triggering | ✅ (unitary event only — event sent via API) | ❌ | ✅ |
| Multi-entity data | ❌ | ❌ | ❌ |
| Exact pre-send counts | ❌ | ❌ | ❌ |
| On-demand segmentation | ❌ | ❌ | ❌ |
| Send-time optimization | ✅ | ❌ | ❌ |
| A/B testing | ✅ | ✅ | ❌ |
| Approval workflows | ✅ | ✅ | ✅ |

>[!NOTE]
>
>For Orchestrated campaigns capability details — including content experiments, batch API triggering, and multi-entity segmentation — see [Get started with Orchestrated campaigns](../orchestrated/gs-orchestrated-campaigns.md).

## Common questions {#common-questions}

+++ Can I combine journeys and campaigns in my marketing strategy?

Yes. Many organizations use all approaches for different scenarios:

* **Journeys** for behavioral, real-time engagement
* **Action campaigns** for scheduled communications or inbound activations
* **API-triggered campaigns** for transactional messages
* **Orchestrated campaigns** for complex, data-intensive batch campaigns — see [Get started with Orchestrated campaigns](../orchestrated/gs-orchestrated-campaigns.md)

Use the right tool for each use case rather than forcing one approach for everything.

+++

+++ Can I convert a campaign to a journey or vice versa?

No, you must rebuild the experience in the appropriate format. However, you can reuse content, audiences, and logic concepts.

+++

+++ Which approach is easier to build?

Action campaigns are typically the simplest (single touch-point or engagement delivered to an audience), followed by API-triggered campaigns, then Journeys (more complex with multi-step logic).

+++

+++ Which scales better for large audiences?

All three can scale well; the right choice depends on your pattern:

* **Read Audience Journeys** and **Action campaigns** are optimized for large batch audiences (one message or flow to many profiles at once).
* **Unitary (event-based) Journeys** process profiles individually as events occur, so scale depends on event volume and throughput.

For complex segmentation with large datasets and multi-entity data, see [Orchestrated campaigns](../orchestrated/gs-orchestrated-campaigns.md).

+++

+++ Can I use the same audience across journeys and campaigns?

Yes. Audiences created in [!DNL Adobe Experience Platform] can be used in Journeys, Action campaigns, and Orchestrated campaigns. API-triggered campaigns are payload-driven and do not use pre-built audiences the same way.

+++

## Next steps {#next-steps}

Ready to start building? Explore the detailed documentation for your chosen approach:

* **[Get started with Journeys](../building-journeys/journey.md)** – Journey types, designer, and workflow
* **[Journey types: choose the right one](../building-journeys/journey-types-selection.md)** – Unitary event, read audience, audience qualification, and business event
* **[Get started with Campaigns](../campaigns/get-started-with-campaigns.md)** – Action and API-triggered campaigns
* **[Get started with Orchestrated campaigns](../orchestrated/gs-orchestrated-campaigns.md)** – Batch canvas workflows with multi-entity data (separate guidance)

>[!MORELIKETHIS]
>
>* [Journey types: choose the right one](../building-journeys/journey-types-selection.md)
>* [Journey types comparison](../building-journeys/journey.md#journey-types-comparison)
>* [Campaign types comparison](../campaigns/get-started-with-campaigns.md#campaign-types)
>* [Journey FAQ](../building-journeys/journey-faq.md)
>* [Orchestrated campaigns FAQ](../orchestrated/orchestrated-campaigns-faq.md)

+++ AI Knowledge Reference

This section contains structured knowledge intended to support interpretation, retrieval, and question answering related to this topic.

For complete understanding, this information should be combined with the documentation on this page. Neither source is intended to stand alone; the page describes the feature, while this section provides additional context that helps disambiguate terminology, intent, applicability, and constraints.

* **TL;DR:** Choose between Journeys, Action campaigns, and API-triggered campaigns based on whether you need real-time 1:1 orchestration, scheduled or inbound batch delivery, or on-demand API-triggered execution.

**Intents:**
* Understand the key differences between Journeys, Action campaigns, and API-triggered campaigns
* Select the right approach for a given marketing use case using the decision guide and comparison tables
* Understand when Action campaigns support inbound channel activations vs. outbound broadcasts
* Know when to escalate to Orchestrated campaigns (ad-hoc composition, federated data, multi-entity)
* Combine multiple approaches effectively in a marketing strategy

**Glossary:**
* **Journey**: A multi-step, real-time orchestration flow where each profile progresses at their own pace based on behavior and events. *(product-specific)*
* **Action campaign**: A campaign delivering scheduled or recurring activations to audiences — outbound broadcast or inbound channel activations to the edge for low-latency personalization. *(product-specific)*
* **API-triggered campaign**: A campaign initiated by an external system via API call, delivering a single on-demand message with payload-driven personalization. *(product-specific)*
* **Orchestrated campaign**: A Hub-side batch campaign supporting multi-entity relational data, ad-hoc audience composition, and federated data sources; not covered by the comparison tables on this page. *(product-specific)*
* **Unitary event journey**: A journey triggered by a single profile action in real time; use when multi-step orchestration is needed after an API-sent event. *(product-specific)*
* **Inbound channel activation**: Delivering personalized experiences to the edge (Code-based experience, In-app, Content Card, Web) for low-latency rendering, supported in Action campaigns. *(product-specific)*

**Guardrails:**
* Up to 10 inbound channel actions per Action campaign (hard limit) — applies to inbound channels only: Code-based experience, In-app, Content Card, Web
* Orchestrated campaigns are excluded from the comparison tables on this page to avoid oversimplification; see dedicated Orchestrated campaigns documentation for architectural details

**Terminology:**
* Canonical name: Action campaigns — variants: "scheduled campaigns", "broadcast campaigns"
* Canonical name: API-triggered campaigns — variants: "transactional campaigns", "event-driven campaigns"
* Do not confuse: "Action campaigns" (scheduled/inbound delivery to audiences) ≠ "API-triggered campaigns" (on-demand, payload-driven, no pre-built audience) ≠ "Orchestrated campaigns" (Hub-side batch with relational data)
* Do not confuse: "Unitary event journey" (triggered by a profile's real-time action) ≠ "Business event journey" (triggered by a non-profile event affecting multiple people via an internal Read Audience step)
* Synonyms: "inbound channel activation" = "inbound channel action" (used interchangeably on this page for edge-delivered experiences in Action campaigns)

**FAQ:**
* **Q: When should I use a Journey instead of an Action campaign?** — Use Journeys when customers need to move at their own pace with real-time conditional logic across multiple touchpoints; use Action campaigns for scheduled or inbound delivery to a pre-defined audience.
* **Q: Can Action campaigns deliver to inbound channels?** — Yes. Action campaigns support inbound channel activation (Code-based experience, In-app, Content Card, Web) to the edge for low-latency personalization, with up to 10 inbound actions per campaign and targeting rules for message variants.
* **Q: What distinguishes Orchestrated campaigns from Action campaigns?** — Orchestrated campaigns run Hub-side batch execution with multi-entity relational data, exact pre-send counts, ad-hoc audience composition, and federated data support; Action campaigns are stateless single-execution deliveries to Experience Platform audiences.
* **Q: When should I use an API-triggered campaign vs. a Unitary event journey?** — Use an API-triggered campaign when an external system needs to trigger a single message immediately with payload data; use a Unitary event journey when multi-step orchestration is needed after the API-sent event.
* **Q: Can I combine Journeys and campaigns in the same marketing strategy?** — Yes. Use Journeys for behavioral real-time engagement, Action campaigns for scheduled broadcasts or inbound activations, API-triggered campaigns for transactional messages, and Orchestrated campaigns for complex batch workflows.

+++
<!-- ai-accordion-version: 1 | source-hash: 873097f5 -->
