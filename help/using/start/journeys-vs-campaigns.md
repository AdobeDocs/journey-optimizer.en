---
solution: Journey Optimizer
product: journey optimizer
title: Journeys vs Campaigns - Choose the right approach
description: Compare Journeys, Action campaigns, API-triggered campaigns, and Orchestrated campaigns to choose the right approach for your marketing needs in Adobe Journey Optimizer.
feature: Journeys, Campaigns, Get Started, Overview
topic: Content Management
role: User
level: Beginner
keywords: journey, campaign, orchestrated, comparison, choose, decision, workflow, real-time, batch, orchestration, multi-step, scheduled, API-triggered, event-driven
hide: yes
exl-id: 8b4d010e-4278-49fd-a7d3-dcc706829577
---
# Journeys vs Campaigns: Choose the right approach {#journeys-vs-campaigns}

[!DNL Adobe Journey Optimizer] offers two main ways to reach and engage your customers: **Journeys** and **Campaigns**. Journeys are designed for real-time, multi-step orchestration driven by customer behavior, while campaigns are better suited for one-time or scheduled broadcasts to a defined audience. Once you have decided on a campaign, you can then choose the campaign type that best fits your use case.

This guide helps you choose based on execution style, data needs, and use case—with a quick comparison, decision tree, and concrete examples.

## Quick comparison overview {#quick-overview}

| Approach | Best for | Execution style |
|----------|----------|-----------------|
| **Journeys** | Multi-step, real-time customer experiences with conditional logic | 1:1 orchestration - each profile at their own pace |
| **Action campaigns** | Scheduled or recurring broadcasts to audiences | Batch execution - audience processed together at send time |
| **API-triggered campaigns** | Event-driven or transactional messages from external systems | On-demand execution - triggered by API call with payload |
| **Orchestrated campaigns** | Complex batch workflows with multi-entity segmentation | Batch canvas - all profiles processed together |

>[!TIP]
>
>**Quick rule of thumb:** Need each customer to move at their own pace with real-time logic? Use **Journeys**. Sending one message to an audience on a schedule? Use **Action campaigns**. Triggering from an external system via API? Use **API-triggered campaigns**. Need multi-entity data, exact counts, or a batch canvas? Use **Orchestrated campaigns**.

## Detailed comparison {#detailed-comparison}

Use this comprehensive table to understand the key differences:

| Feature | Journeys | Action campaigns | API-triggered campaigns | Orchestrated campaigns |
|---------|----------|------------------|------------------------|----------------------|
| **Primary purpose** | Multi-step 1:1 orchestration with real-time customer context | One-time or recurring message delivery to audiences | Transactional or event-driven messages initiated by external systems | Multi-step batch campaigns with complex segmentation workflows |
| **Canvas type** | 1:1 canvas - each profile travels at their own pace | No canvas - single action execution | No canvas - single action execution | Batch canvas - all profiles processed together |
| **Execution flow** | Sequential actions, profile maintains state throughout journey | Simultaneous execution to entire audience | Immediate execution per API call | Multi-step batch workflow with activities and transitions |
| **Entry mechanism** | Events, audiences, qualifications, business events | Manual activation and schedule | API call from external system | Scheduled execution of batch workflow |
| **Data model** | Real-time profile + event data | Profile data from Experience Platform audiences | API payload data with optional profile lookup | Multi-entity relational data (profiles, products, stores, bookings) |
| **Segmentation** | Pre-built audiences + real-time conditions | Pre-built audiences from Experience Platform | Payload-driven targeting (no scheduled audience) | On-demand audiences built within canvas with exact counts |
| **Profile processing** | Individual, real-time (as events occur) | Batch, all at once | Per API call, payload-driven | Batch, all together with multi-entity support |
| **Personalization** | Real-time contextual data + profile attributes | Profile attributes | Payload data + optional profile attributes | Multi-entity data for precision targeting |
| **Complexity** | Multi-step with branching, wait times, conditions | Single action or simple workflow | Single action with payload mapping | Multi-step batch workflows with segmentation, enrichment, splits |
| **Best for** | Customer lifecycle journeys, onboarding, cart abandonment | Promotional campaigns, newsletters, announcements | Order confirmations, shipping alerts, password resets | Complex seasonal campaigns, multi-step promotions, product launches |
| **Timing** | Continuous, always active once published | Scheduled start/end dates | On-demand, event-driven via API | Batch execution on schedule |
| **State management** | Maintains customer state for real-time actions | Stateless execution | Stateless execution per call | Batch processing with worktables |
| **Use when** | Multiple touchpoints needed with real-time decision logic | Simple message to an audience at a specific time | External system needs to trigger a message immediately | Need complex segmentation, multi-entity data, or exact pre-send counts |
| **Unique capabilities** | Real-time reactions, wait activities, profile-based pacing | Scheduling, audience targeting, rate control | API payload mapping, system-to-system triggering | Relational datasets, multi-entity segmentation, exact counts, multi-level sending |

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
→ **Use API-triggered campaigns**
* Triggered on demand via API call
* Payload-driven personalization
* No complex multi-step logic needed

**Complex batch workflow with advanced segmentation?**
→ **Use Orchestrated campaigns**
* Need multi-entity data (products, stores, bookings)
* Require exact pre-send counts
* Multi-step batch processing with splits and enrichment

### Step 2: Validate your choice

| Your need | Recommended approach | Why |
|-----------|---------------------|-----|
| Welcome new customers with multi-step onboarding | Journeys | Real-time entry, multiple touchpoints, conditional paths |
| Send monthly newsletter to subscribers | Action campaigns | Simple scheduled message to audience |
| Cart abandonment with reminder sequence | Journeys | Real-time trigger, wait times, conditional follow-up |
| Promotional announcement to all customers | Action campaigns | One-time message, immediate delivery |
| Re-engage inactive users based on behavior | Journeys | Triggered by audience qualification, personalized path |
| Flash sale triggered by business event | Journeys (Business Event) | Real-time trigger affecting multiple customers |
| Seasonal promotion with product catalog integration | Orchestrated campaigns | Multi-entity data, complex segmentation, exact counts |
| API-triggered transactional message | API-triggered campaigns | External system trigger, immediate delivery |
| Multi-level sending per booking | Orchestrated campaigns | Multi-entity relationships, one message per booking |

## Key distinctions explained {#key-distinctions}

### Journeys: 1:1 Real-time orchestration

**What makes it unique:**
* Each profile maintains individual state and context
* Profiles enter and progress at their own pace
* Real-time decision-making based on behavior and events
* Wait activities create personalized timing
* Conditional branching creates unique paths per profile

**Example flow:**

```
Customer A: Abandoned cart → Wait 2 hours → No purchase? → Send reminder → Purchased? → End
Customer B: Abandoned cart → Wait 2 hours → Already purchased → End immediately
```

Each customer experiences their own journey timeline based on their actions.

[Learn more about Journeys](../building-journeys/journey.md)

### Campaigns: Simple batch or triggered delivery

**What makes it unique:**
* All profiles processed identically and simultaneously
* Stateless execution - no context maintained
* Simple scheduling or API triggering
* Ideal for broadcast communications

**Example flow:**

```
Monday 9 AM → Send newsletter to 100,000 subscribers → All receive simultaneously
```

Everyone gets the same message at the same time.

**Types:**
* **Action campaigns**: Scheduled delivery to audiences (one-time or recurring)
* **API-triggered campaigns**: On-demand delivery triggered by an API call with payload data

[Learn more about Campaigns](../campaigns/get-started-with-campaigns.md)

### Orchestrated campaigns: Batch canvas workflows

**What makes it unique:**
* Batch canvas with activities and transitions (similar to journey canvas but batch-oriented)
* Multi-entity relational data support (profiles + products + stores + bookings)
* On-demand audience building within the canvas
* Exact counts before sending (pre-send visibility)
* Multi-level sending (one message per entity, e.g., per booking)
* All profiles processed together in batch

**Example flow:**

```
Query customers → Filter by purchase history → Split by region → 
Enrich with product data → Build segments → Send personalized offers → All in one batch execution
```

Combines workflow complexity with batch campaign execution.

[Learn more about Orchestrated campaigns](../orchestrated/gs-orchestrated-campaigns.md)

## Use case examples {#use-cases}

### Journey use cases

* **Cart abandonment recovery**: Triggered by cart add event, wait for checkout, send reminders if no purchase
* **Customer onboarding**: Multi-step welcome series with personalized content based on profile data
* **Loyalty tier upgrade**: Triggered when customer reaches new tier, send congratulations and benefits
* **Birthday campaigns**: Entry based on birthdate, personalized offers
* **Re-engagement**: Triggered by audience qualification (inactivity), progressive outreach

### Campaign use cases (Action & API-triggered)

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

### Orchestrated campaign use cases

* **Seasonal promotion with catalog integration**: Query product catalog, identify eligible customers, segment by preferences, send personalized product recommendations
* **Store-specific campaigns**: Target customers near specific store locations with store inventory data
* **Multi-booking communications**: Send one message per booking (hotel reservations, flight bookings)
* **Complex segment orchestration**: Build audiences step-by-step with enrichment from multiple data sources
* **Pre-send validation**: Get exact counts of recipients before launching major campaigns

## Feature availability {#feature-availability}

### Channels

| Channel | Journeys | Action campaigns | API-triggered campaigns | Orchestrated campaigns |
|---------|:--------:|:----------------:|:-----------------------:|:---------------------:|
| Email | ✅ | ✅ | ✅ | ✅ |
| Push | ✅ | ✅ | ✅ | ✅ |
| SMS | ✅ | ✅ | ✅ | ✅ |
| In-app | ✅ | ✅ | ✅ | ❌ |
| Web | ✅ | ✅ | ❌ | ❌ |
| Code-based | ✅ | ✅ | ❌ | ❌ |
| Content cards | ✅ | ✅ | ❌ | ❌ |
| Direct mail | ✅ | ✅ | ❌ | ✅ |

### Advanced capabilities

| Capability | Journeys | Action campaigns | API-triggered campaigns | Orchestrated campaigns |
|-----------|:--------:|:----------------:|:-----------------------:|:---------------------:|
| Multi-step workflows | ✅ | ❌ | ❌ | ✅ |
| Real-time triggers | ✅ | ❌ | ✅ | ❌ |
| Wait activities | ✅ | ❌ | ❌ | ✅ |
| Conditional branching | ✅ | ❌ | ❌ | ✅ |
| Scheduled execution | ✅ | ✅ | ✅ | ✅ |
| API triggering | ❌ | ❌ | ✅ | ❌ |
| Multi-entity data | ❌ | ❌ | ❌ | ✅ |
| Exact pre-send counts | ❌ | ❌ | ❌ | ✅ |
| On-demand segmentation | ❌ | ❌ | ❌ | ✅ |
| Send-time optimization | ✅ | ✅ | ✅ | ✅ |
| A/B testing | ✅ | ✅ | ❌ | ❌ |
| Approval workflows | ✅ | ✅ | ✅ | ❌ |

## Common questions {#common-questions}

+++ Can I combine journeys and campaigns in my marketing strategy?

Yes. Many organizations use all four approaches for different scenarios:

* **Journeys** for behavioral, real-time engagement
* **Action campaigns** for scheduled broadcast communications
* **API-triggered campaigns** for transactional messages
* **Orchestrated campaigns** for complex, data-intensive batch campaigns

Use the right tool for each use case rather than forcing one approach for everything.

+++

+++ Can I convert a campaign to a journey or vice versa?

No, you must rebuild the experience in the appropriate format. However, you can reuse content, audiences, and logic concepts.

+++

+++ Which approach is easier to build?

Action campaigns are typically the simplest (single message to audience), followed by API-triggered campaigns, Journeys (more complex with multi-step logic), and Orchestrated campaigns (most complex due to canvas workflow and multi-entity capabilities).

+++

+++ Which scales better for large audiences?

All four can scale well; the right choice depends on your pattern:

* **Read Audience Journeys** and **Action campaigns** are optimized for large batch audiences (one message or flow to many profiles at once).
* **Orchestrated campaigns** excel at complex segmentation with large datasets and multi-entity data.
* **Unitary (event-based) Journeys** process profiles individually as events occur, so scale depends on event volume and throughput.

+++

+++ Can I use the same audience across journeys and campaigns?

Yes. Audiences created in [!DNL Adobe Experience Platform] can be used in Journeys, Action campaigns, and Orchestrated campaigns (where audience logic can also be built on-demand in the canvas). API-triggered campaigns are payload-driven and do not use pre-built audiences the same way.

+++

## Next steps {#next-steps}

Ready to start building? Explore the detailed documentation for your chosen approach:

* **[Get started with Journeys](../building-journeys/journey.md)** – Journey types, designer, and workflow
* **[Get started with Campaigns](../campaigns/get-started-with-campaigns.md)** – Action and API-triggered campaigns
* **[Get started with Orchestrated campaigns](../orchestrated/gs-orchestrated-campaigns.md)** – Batch canvas workflows

>[!MORELIKETHIS]
>
>* [Journey types comparison](../building-journeys/journey.md#journey-types-comparison)
>* [Campaign types comparison](../campaigns/get-started-with-campaigns.md#campaign-types)
>* [Journey FAQ](../building-journeys/journey-faq.md)
>* [Orchestrated campaigns FAQ](../orchestrated/orchestrated-campaigns-faq.md)
