---
solution: Journey Optimizer
product: journey optimizer
title: Journeys vs Campaigns - Choose the right approach
description: Compare Journeys, Action campaigns, and API-triggered campaigns to choose the right approach for your marketing needs in Adobe Journey Optimizer.
feature: Journeys, Campaigns, Get Started, Overview
topic: Content Management
role: User
level: Beginner
hide: true
keywords: journey, campaign, comparison, choose, decision, workflow, real-time, batch, orchestration, multi-step, scheduled, API-triggered, event-driven
---

# Journeys vs campaigns: choose the right approach {#journeys-vs-campaigns}

>[!BEGINSHADEBOX]

**On this page:** Compare journeys with action and API-triggered campaigns so you can choose the right approach for each marketing use case in Adobe Journey Optimizer. For Orchestrated campaigns, see [Get started with Orchestrated campaigns](../orchestrated/gs-orchestrated-campaigns.md).

>[!ENDSHADEBOX]

[!DNL Adobe Journey Optimizer] offers two main ways to reach and engage your customers: **Journeys** and **Campaigns**. Journeys are designed for real-time, multi-step orchestration driven by customer behavior, while campaigns are better suited for one-time or scheduled broadcasts to a defined audience — or for inbound channel activations to the edge for low-latency personalization.

>[!NOTE]
>
>**Orchestrated campaigns** have distinct architectural characteristics (Hub-side batch execution, multi-entity relational data) that require dedicated guidance. They are not included in the comparison below to avoid oversimplification. [Learn more about Orchestrated campaigns](../orchestrated/gs-orchestrated-campaigns.md)

## Which approach should you use? {#decision-guide}

The answer usually comes down to one question: *what needs to happen, and for whom?*

If you need **each customer to move at their own pace** — receiving messages based on what they do, waiting, then reacting to their next action — use a **Journey**. Journeys keep track of where each profile is and what they've done, making them ideal for multi-step experiences like onboarding sequences, cart abandonment flows, or loyalty programs.

If you want to **send a message to a group of people on a schedule** — a newsletter, a product announcement, a seasonal promotion — use an **Action campaign**. Everyone in the audience receives the message at the same time, with no need for per-profile logic. Action campaigns also support inbound channel activations (in-app, web, content cards, code-based) for low-latency edge personalization.

If an **external system needs to trigger a message immediately** — an order confirmation from your e-commerce platform, a shipping alert from your logistics system, a password reset from your app — use an **API-triggered campaign** for a single on-demand message, or a **Unitary event journey** if that trigger needs to kick off a multi-step flow.

If you need a **complex batch workflow with advanced segmentation, multi-entity data, or exact pre-send counts**, see [Get started with Orchestrated campaigns](../orchestrated/gs-orchestrated-campaigns.md).

>[!TIP]
>
>**Not sure where to start?** Most teams use Journeys for behavioral, event-driven experiences and Action campaigns for scheduled communications. These two cover the majority of use cases.

## How they compare {#quick-overview}

| Approach | Best for | Execution style |
|----------|----------|-----------------|
| **Journeys** | Multi-step, real-time customer experiences with conditional logic | 1:1 orchestration — each profile at their own pace |
| **Action campaigns** | Scheduled or recurring activations to audiences | Batch execution — audience processed together at send time |
| **API-triggered campaigns** | Event-driven or transactional messages from external systems | On-demand execution — triggered by API call with payload |

## How each approach works {#key-distinctions}

### Journeys: 1:1 real-time orchestration

A Journey is a canvas where each profile travels their own path at their own pace. AJO tracks where each person is in the flow and reacts in real time to their behavior — whether that's an action they take, a period of inactivity, or a change in their profile.

Key capabilities include wait activities that create personalized timing between steps, conditional branching that routes profiles to different paths, frequency capping to control how often a customer receives messages, and test mode to validate logic before going live. Journeys can also split profiles into percentage-based groups for A/B experiments across paths.

A cart abandonment journey illustrates the difference clearly:

```
Customer A: Abandoned cart → Wait 2 hours → No purchase? → Send reminder → Purchased? → End
Customer B: Abandoned cart → Wait 2 hours → Already purchased → End immediately
```

Each customer experiences a different timeline based on what they actually do. [Learn more about Journeys](../building-journeys/journey.md)

### Campaigns: Batch or triggered delivery

A campaign executes a single action — either to everyone in an audience at once, or on demand when called by an external system. There is no canvas and no per-profile state: all profiles are processed identically.

**Action campaigns** deliver to a scheduled audience (one-time or recurring) and also support multi-surface inbound delivery — up to 10 inbound channel actions per campaign, with targeting rules to create message variants based on audience membership or profile attributes.

**API-triggered campaigns** fire immediately when an external system calls the API, with message personalization driven by the payload data sent in that call.

```
Monday 9 AM → Send newsletter to 100,000 subscribers → All receive simultaneously
```

[Learn more about Campaigns](../campaigns/get-started-with-campaigns.md)

## Use case examples {#use-cases}

| Use case | Recommended approach | Why |
|----------|---------------------|-----|
| Welcome new customers with multi-step onboarding | Journeys | Real-time entry, multiple touchpoints, conditional paths |
| Cart abandonment with reminder sequence | Journeys | Real-time trigger, wait times, conditional follow-up |
| Re-engage inactive users based on behavior | Journeys | Triggered by audience qualification, personalized path |
| Flash sale triggered by a business event | Journeys (Business Event) | Real-time trigger affecting multiple customers |
| Monthly newsletter to subscribers | Action campaigns | Scheduled message to audience |
| Promotional announcement to all customers | Action campaigns | One-time message, immediate delivery |
| Order confirmation or shipping alert | API-triggered campaigns | External system trigger, immediate one-shot delivery |
| API-triggered multi-step flow | Journeys (Unitary event) | External system sends event via API; journey orchestrates follow-up steps |
| Complex batch workflow with multi-entity data | Orchestrated campaigns | See [Get started with Orchestrated campaigns](../orchestrated/gs-orchestrated-campaigns.md) |

## Feature availability {#feature-availability}

### Channels

All three approaches support the full AJO outbound channel set: email, push, SMS, LINE, and WhatsApp. The table below shows differences for inbound and digital channels.

| Channel | Journeys | Action campaigns | API-triggered campaigns |
|---------|:--------:|:----------------:|:-----------------------:|
| In-app | ✅ | ✅ | ✅ |
| Web | ✅ | ✅ | ❌ |
| Code-based | ✅ | ✅ | ❌ |
| Content cards | ✅ | ✅ | ❌ |
| Direct mail | ✅ | ✅ | ❌ |

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
| API triggering | ✅ (unitary event only) | ❌ | ✅ |
| Send-time optimization | ✅ | ❌ | ❌ |
| A/B testing | ✅ | ✅ | ❌ |
| Approval workflows | ✅ | ✅ | ✅ |
| Multi-entity data | ❌ | ❌ | ❌ |
| Exact pre-send counts | ❌ | ❌ | ❌ |

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

+++ Which approach is easiest to build?

Action campaigns are typically the simplest (a single touchpoint delivered to an audience), followed by API-triggered campaigns, then Journeys, which require more design work due to multi-step logic.

+++

+++ Which scales better for large audiences?

All three can scale well; the right choice depends on your pattern:

* **Read Audience Journeys** and **Action campaigns** are optimized for large batch audiences.
* **Unitary (event-based) Journeys** process profiles individually as events occur, so scale depends on event volume and throughput.

For complex segmentation with large datasets and multi-entity data, see [Orchestrated campaigns](../orchestrated/gs-orchestrated-campaigns.md).

+++

+++ Can I use the same audience across journeys and campaigns?

Yes. Audiences created in [!DNL Adobe Experience Platform] can be used in Journeys, Action campaigns, and Orchestrated campaigns. API-triggered campaigns are payload-driven and do not use pre-built audiences the same way.

+++

## Next steps {#next-steps}

Ready to start building? Explore the detailed documentation for your chosen approach:

* **[Get started with Journeys](../building-journeys/journey.md)** – Journey types, designer, and workflow
* **[Get started with Campaigns](../campaigns/get-started-with-campaigns.md)** – Action and API-triggered campaigns
* **[Get started with Orchestrated campaigns](../orchestrated/gs-orchestrated-campaigns.md)** – Batch canvas workflows with multi-entity data (separate guidance)

>[!MORELIKETHIS]
>
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
