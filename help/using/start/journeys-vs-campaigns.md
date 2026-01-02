---
solution: Journey Optimizer
product: journey optimizer
title: Journeys vs Campaigns - Choose the right approach
description: Compare journeys, campaigns, and orchestrated campaigns to choose the right approach for your marketing needs in Adobe Journey Optimizer
feature: Journeys, Campaigns, Get Started, Overview
role: User
level: Beginner
keywords: journey, campaign, orchestrated, comparison, choose, decision, workflow, real-time, batch, orchestration, multi-step, scheduled, API-triggered, event-driven
hide: yes
hidefromtoc: yes
---

# Journeys vs Campaigns: Choose the right approach {#journeys-vs-campaigns}

Adobe Journey Optimizer offers three powerful approaches to reach and engage your customers. Understanding when to use each is key to building effective marketing experiences.

This guide helps you choose between **Journeys**, **Campaigns** (Action & API-triggered), and **Orchestrated Campaigns** based on your specific marketing needs.

## Quick comparison overview {#quick-overview}

| Approach | Best for | Execution style |
|----------|----------|-----------------|
| **Journeys** | Multi-step, real-time customer experiences with conditional logic | 1:1 orchestration - each profile at their own pace |
| **Campaigns (Action & API)** | Simple, scheduled or triggered message delivery | Batch or API-triggered - all profiles simultaneously |
| **Orchestrated Campaigns** | Complex batch workflows with multi-entity segmentation | Batch canvas - all profiles processed together |

## Detailed comparison {#detailed-comparison}

Use this comprehensive table to understand the key differences:

| Feature | Journeys | Campaigns (Action & API-triggered) | Orchestrated Campaigns |
|---------|----------|-----------------------------------|----------------------|
| **Primary purpose** | Multi-step 1:1 orchestration with real-time customer context | One-time or recurring message delivery to audiences | Multi-step batch campaigns with complex segmentation workflows |
| **Canvas type** | 1:1 canvas - each profile travels at their own pace | No canvas - single action execution | Batch canvas - all profiles processed together |
| **Execution flow** | Sequential actions, profile maintains state throughout journey | Simultaneous execution to entire audience | Multi-step batch workflow with activities and transitions |
| **Entry mechanism** | Events, audiences, qualifications, business events | Manual activation, scheduled, or API trigger | Scheduled execution of batch workflow |
| **Data model** | Real-time profile + event data | Profile data + API payload | Multi-entity relational data (profiles, products, stores, bookings) |
| **Segmentation** | Pre-built audiences + real-time conditions | Pre-built audiences from Experience Platform | On-demand audiences built within canvas with exact counts |
| **Profile processing** | Individual, real-time (as events occur) | Batch, all at once | Batch, all together with multi-entity support |
| **Personalization** | Real-time contextual data + profile attributes | Profile attributes + API payload data | Multi-entity data for precision targeting |
| **Complexity** | Multi-step with branching, wait times, conditions | Single action or simple workflow | Multi-step batch workflows with segmentation, enrichment, splits |
| **Best for** | Customer lifecycle journeys, onboarding, cart abandonment | Promotional campaigns, newsletters, announcements, transactional messages | Complex seasonal campaigns, multi-step promotions, product launches |
| **Timing** | Continuous, always active once published | Scheduled start/end dates or API-triggered | Batch execution on schedule |
| **State management** | Maintains customer state for real-time actions | Stateless execution | Batch processing with worktables |
| **Use when** | Multiple touchpoints needed with real-time decision logic | Simple message to audience at specific time | Need complex segmentation, multi-entity data, or exact pre-send counts |
| **Unique capabilities** | Real-time reactions, wait activities, profile-based pacing | Simple scheduling, API triggering, rate control | Relational datasets, multi-entity segmentation, exact counts, multi-level sending |

## Decision guide {#decision-guide}

Follow this decision tree to choose the right approach:

### Step 1: What's your execution requirement?

**Real-time, individual responses to customer behavior?**
→ **Use Journeys**
- Profiles need to move at their own pace
- Conditional logic based on behavior
- Real-time context is critical

**Simple message delivery to an audience?**
→ **Use Action or API-triggered Campaigns**
- All profiles receive message simultaneously
- Scheduled or triggered via API
- No complex multi-step logic needed

**Complex batch workflow with advanced segmentation?**
→ **Use Orchestrated Campaigns**
- Need multi-entity data (products, stores, bookings)
- Require exact pre-send counts
- Multi-step batch processing with splits and enrichment

### Step 2: Validate your choice

| Your need | Recommended approach | Why |
|-----------|---------------------|-----|
| Welcome new customers with multi-step onboarding | Journeys | Real-time entry, multiple touchpoints, conditional paths |
| Send monthly newsletter to subscribers | Action Campaign | Simple scheduled message to audience |
| Cart abandonment with reminder sequence | Journeys | Real-time trigger, wait times, conditional follow-up |
| Promotional announcement to all customers | Action Campaign | One-time message, immediate delivery |
| Re-engage inactive users based on behavior | Journeys | Triggered by audience qualification, personalized path |
| Flash sale triggered by business event | Journeys (Business Event) | Real-time trigger affecting multiple customers |
| Seasonal promotion with product catalog integration | Orchestrated Campaign | Multi-entity data, complex segmentation, exact counts |
| API-triggered transactional message | API-triggered Campaign | External system trigger, immediate delivery |
| Multi-level sending per booking | Orchestrated Campaign | Multi-entity relationships, one message per booking |

## Key distinctions explained {#key-distinctions}

### Journeys: 1:1 Real-time orchestration

**What makes it unique:**
- Each profile maintains individual state and context
- Profiles enter and progress at their own pace
- Real-time decision-making based on behavior and events
- Wait activities create personalized timing
- Conditional branching creates unique paths per profile

**Example flow:**

```
Customer A: Abandoned cart → Wait 2 hours → No purchase? → Send reminder → Purchased? → End
Customer B: Abandoned cart → Wait 2 hours → Already purchased → End immediately
```

Each customer experiences their own journey timeline based on their actions.

[Learn more about Journeys](../building-journeys/journey.md)

### Campaigns: Simple batch or triggered delivery

**What makes it unique:**
- All profiles processed identically and simultaneously
- Stateless execution - no context maintained
- Simple scheduling or API triggering
- Ideal for broadcast communications

**Example flow:**

```
Monday 9 AM → Send newsletter to 100,000 subscribers → All receive simultaneously
```

Everyone gets the same message at the same time.

**Types:**
- **Action Campaigns**: Scheduled delivery (one-time or recurring)
- **API-triggered Campaigns**: Triggered via API call from external systems

[Learn more about Campaigns](../campaigns/get-started-with-campaigns.md)

### Orchestrated Campaigns: Batch canvas workflows

**What makes it unique:**
- Batch canvas with activities and transitions (similar to journey canvas but batch-oriented)
- Multi-entity relational data support (profiles + products + stores + bookings)
- On-demand audience building within the canvas
- Exact counts before sending (pre-send visibility)
- Multi-level sending (one message per entity, e.g., per booking)
- All profiles processed together in batch

**Example flow:**

```
Query customers → Filter by purchase history → Split by region → 
Enrich with product data → Build segments → Send personalized offers → All in one batch execution
```

Combines workflow complexity with batch campaign execution.

[Learn more about Orchestrated Campaigns](../orchestrated/gs-orchestrated-campaigns.md)

## Use case examples {#use-cases}

### Journey use cases

- **Cart abandonment recovery**: Triggered by cart add event, wait for checkout, send reminders if no purchase
- **Customer onboarding**: Multi-step welcome series with personalized content based on profile data
- **Loyalty tier upgrade**: Triggered when customer reaches new tier, send congratulations and benefits
- **Birthday campaigns**: Entry based on birthdate, personalized offers
- **Re-engagement**: Triggered by audience qualification (inactivity), progressive outreach

### Campaign use cases (Action & API-triggered)

**Action Campaigns:**
- **Monthly newsletters**: Scheduled batch delivery to subscriber segment
- **Promotional announcements**: Time-sensitive offers to target audiences
- **Product launches**: Coordinated announcement to all customers
- **Seasonal greetings**: Holiday messages on specific dates

**API-triggered Campaigns:**
- **Order confirmations**: Triggered by e-commerce system after purchase
- **Shipping notifications**: Triggered by logistics system
- **Account alerts**: Triggered by fraud detection system
- **Password resets**: Triggered by user action in application

### Orchestrated Campaign use cases

- **Seasonal promotion with catalog integration**: Query product catalog, identify eligible customers, segment by preferences, send personalized product recommendations
- **Store-specific campaigns**: Target customers near specific store locations with store inventory data
- **Multi-booking communications**: Send one message per booking (hotel reservations, flight bookings)
- **Complex segment orchestration**: Build audiences step-by-step with enrichment from multiple data sources
- **Pre-send validation**: Get exact counts of recipients before launching major campaigns

## Feature availability {#feature-availability}

### Channels

| Channel | Journeys | Action Campaigns | API-triggered Campaigns | Orchestrated Campaigns |
|---------|:--------:|:----------------:|:-----------------------:|:---------------------:|
| Email | ✅ | ✅ | ✅ | ✅ |
| Push | ✅ | ✅ | ✅ | ✅ |
| SMS | ✅ | ✅ | ✅ | ✅ |
| In-app | ✅ | ✅ | ✅ | ❌ |
| Web | ✅ | ✅ | ❌ | ❌ |
| Code-based | ✅ | ✅ | ❌ | ❌ |
| Content cards | ✅ | ✅ | ❌ | ❌ |
| Direct mail | ✅ | ✅ | ❌ | ❌ |

### Advanced capabilities

| Capability | Journeys | Action Campaigns | API-triggered Campaigns | Orchestrated Campaigns |
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

**Q: Can I combine journeys and campaigns in my marketing strategy?**

A: Absolutely! Most organizations use all three approaches for different scenarios:
- Journeys for behavioral, real-time engagement
- Action Campaigns for scheduled broadcast communications
- API-triggered Campaigns for transactional messages
- Orchestrated Campaigns for complex, data-intensive batch campaigns

**Q: Can I convert a campaign to a journey or vice versa?**

A: No, you must rebuild the experience in the appropriate format. However, you can reuse content, audiences, and logic concepts.

**Q: Which approach is easier to build?**

A: Action Campaigns are typically the simplest (single message to audience), followed by API-triggered Campaigns, Journeys (more complex with multi-step logic), and Orchestrated Campaigns (most complex due to canvas workflow and multi-entity capabilities).

**Q: Which scales better for large audiences?**

A: All three can scale well, but:
- **Read Audience Journeys** and **Action Campaigns** are optimized for large batch audiences
- **Orchestrated Campaigns** excel at complex segmentation with large datasets
- **Unitary Journeys** process profiles individually, so scale depends on event volume

**Q: Can I use the same audience across journeys and campaigns?**

A: Yes, audiences created in Adobe Experience Platform can be used across all three approaches.

## Next steps {#next-steps}

Ready to start building? Explore the detailed documentation for your chosen approach:

- **[Get started with Journeys](../building-journeys/journey.md)** - Learn about journey types, designer, and workflow
- **[Get started with Campaigns](../campaigns/get-started-with-campaigns.md)** - Explore Action and API-triggered campaigns
- **[Get started with Orchestrated Campaigns](../orchestrated/gs-orchestrated-campaigns.md)** - Discover batch canvas workflows

**Need more help deciding?**
- [Journey types comparison](../building-journeys/journey.md#journey-types-comparison)
- [Campaign types comparison](../campaigns/get-started-with-campaigns.md#campaign-types)
- [Journey FAQ](../building-journeys/journey-faq.md)
- [Orchestrated Campaigns FAQ](../orchestrated/orchestrated-campaigns-faq.md)

