---
solution: Journey Optimizer
product: journey optimizer
title: Choose the right capability for your goal | Adobe Journey Optimizer
description: Discover the core use cases Adobe Journey Optimizer is designed for, with guidance on which AJO capabilities best fit each scenario.
feature: Get Started
topic: Content Management
role: User
level: Beginner
keywords: journey optimizer, use case, decision guide, which capability, get started, practitioner goals, tutorials
---
# Choose the right capability for your goal {#ajo-use-case-guide}

>[!BEGINSHADEBOX]

**On this page:** Start from what you want to accomplish, then jump to the Adobe Journey Optimizer capability that solves it — without needing to know the feature name first.

>[!ENDSHADEBOX]

[!DNL Adobe Journey Optimizer] offers many capabilities, and the right one depends on what you are trying to achieve. This guide is organized around business goals rather than product features: find the goal that matches your need, then follow the link to start with the recommended capability.

Use this page as a quick router — scan for your goal and jump straight to the right capability. If you are just getting started, begin with [Get started with Journey Optimizer](../../rp_landing_pages/get-started-landing-page.md) to find the right entry point for your role.

>[!NOTE]
>
>For step-by-step implementation samples, see the [Journey use cases library](../building-journeys/jo-use-cases.md).

Where an end-to-end tutorial isn't available for a specific scenario, the link takes you to the best current starting point to learn the capability and begin.

AI is built into many of these capabilities — look for the **(AI)** tag in the tables below. The conversational [AI Assistant](ai-features.md#ai-assistant) can also answer product questions and surface operational insights about your journeys at any time. For the full set of intelligent features, see [AI & intelligent features](ai-features.md).

>[!TIP]
>
>New to Journey Optimizer? Start with [Get started with Journey Optimizer](../../rp_landing_pages/get-started-landing-page.md) to choose the right path for your role, then read [What is Journey Optimizer](get-started.md) for the essentials. To build hands-on confidence, browse the [Journey Optimizer tutorials](https://experienceleague.adobe.com/en/docs/journey-optimizer-learn/tutorials/overview){target="_blank"}, follow an expert-curated [video playlist](https://experienceleague.adobe.com/en/playlists?solution=Journey+Optimizer){target="_blank"}, and practice in a [training sandbox](https://experienceleague.adobe.com/en/docs/journey-optimizer-learn/configure-a-training-sandbox/introduction-and-prerequisites){target="_blank"} or with the [hands-on challenges](https://experienceleague.adobe.com/en/docs/journey-optimizer-learn/challenges/introduction-and-prerequisites){target="_blank"}.

## Set up Journey Optimizer for your team {#setup-admin}

For administrators and technical users who need to configure the environment before building journeys or campaigns.

| I want to... | Recommended capability | Start here |
| --- | --- | --- |
| Configure email, SMS, or push channels before sending | Channel configuration | [Get started with channel configuration](../configuration/get-started-configuration.md) |
| Warm up a new IP address for email sending | IP warmup plan | [Get started with IP warmup](../configuration/ip-warmup-gs.md) |
| Set up roles, permissions, and access control | Access control | [Get started with access control](../administration/permissions-overview.md) |
| Work across multiple environments or regions | Sandboxes | [Work with sandboxes](../administration/sandboxes.md) |

## Engage customers as events happen {#engage-real-time}

For scenarios where you react to a customer action or event as it happens.

| I want to... | Recommended capability | Start here |
| --- | --- | --- |
| Welcome a new customer or subscriber automatically | Event-triggered journey | [Get started with journeys](../building-journeys/journey-gs.md) · [Introduction to building a journey](https://experienceleague.adobe.com/en/docs/journey-optimizer-learn/tutorials/journeys/introduction-to-building-a-journey){target="_blank"} |

>[!BEGINSHADEBOX]

**Before you build:** make sure you have (1) a [journey entry event configured](../event/about-events.md) to capture the sign-up trigger, (2) an [email or push channel surface](../configuration/channel-surfaces.md) set up for your sandbox, and (3) at least one [test profile](../audience/creating-test-profiles.md) available to validate the journey before publishing.

>[!ENDSHADEBOX]

| I want to... | Recommended capability | Start here |
| --- | --- | --- |
| Recover an abandoned cart or browse session | Event-triggered journey | [Get started with journeys](../building-journeys/journey-gs.md) · [Abandoned browse tutorial](https://experienceleague.adobe.com/en/docs/experience-platform/rtcdp/use-cases/personalization-insights-engagement/use-cases-luma){target="_blank"} |

>[!BEGINSHADEBOX]

**Before you build:** you need (1) a [behavioral event](../event/about-events.md) that captures the cart or browse action from your web or mobile SDK, (2) a [wait activity](../building-journeys/wait-activity.md) strategy decided (typically 1–4 hours before the first nudge), and (3) a channel surface ready for the follow-up message. Note: the journey must include a condition to exit profiles who complete the purchase before the wait period ends.

>[!ENDSHADEBOX]

| I want to... | Recommended capability | Start here |
| --- | --- | --- |
| Trigger a journey from a website form submission | Event-triggered journey | [Get started with journeys](../building-journeys/journey-gs.md) · [Tutorial](https://experienceleague.adobe.com/en/docs/journey-optimizer-learn/trigger-journey-on-form-submission/introduction){target="_blank"} |
| React to in-app behavior (app open, screen view) | Journeys + In-app | [Get started with In-app](../in-app/get-started-in-app.md) |
| Send order, shipping, or appointment confirmations | API-triggered campaign | [Work with API-triggered campaigns](../campaigns/api-triggered-campaigns.md) |
| Re-engage inactive or lapsing customers | Journeys + audiences | [Get started with profiles & audiences](../audience/get-started-profiles.md) · [Create audiences using the rule builder](https://experienceleague.adobe.com/en/docs/journey-optimizer-learn/tutorials/profiles-audiences-subscriptions/create-audiences-using-the-rule-builder){target="_blank"} |

>[!BEGINSHADEBOX]

**Before you build:** you need (1) an [audience defined in Adobe Experience Platform](../audience/about-audiences.md) that identifies inactive profiles (e.g. no purchase or login in 60 days), (2) a decision on re-engagement channel (email, push, or SMS), and (3) a suppression rule or [frequency cap](../conflict-prioritization/channel-capping.md) to avoid contacting recently messaged profiles. Use a **Read Audience** journey entry — not an event — for this scenario.

>[!ENDSHADEBOX]

| I want to... | Recommended capability | Start here |
| --- | --- | --- |
| Test a journey with real data before activating it | Journey dry run | [Test your journey with dry run](../building-journeys/journey-dry-run.md) |
| Pause a live journey to make edits without stopping in-flight profiles | Journey pause & resume | [Pause and resume a journey](../building-journeys/journey-pause.md) |
| Build or optimize a journey from a natural-language prompt | Journey Agent **(AI)** | [AI agents](ai-features.md#ai-agents) · [Journey Agent tutorial](https://experienceleague.adobe.com/en/docs/journey-optimizer-learn/tutorials/journeys/journey-agent-overview){target="_blank"} |

## Reach audiences at scale {#reach-at-scale}

For scheduled, one-to-many outreach to a defined audience.

| I want to... | Recommended capability | Start here |
| --- | --- | --- |
| Send a newsletter or promotion to a segment | Scheduled campaign | [Get started with campaigns](../campaigns/get-started-with-campaigns.md) |

>[!BEGINSHADEBOX]

**Before you build:** you need (1) a [published audience segment](../audience/about-audiences.md) in Adobe Experience Platform, (2) an [email channel surface](../configuration/channel-surfaces.md) with a verified sending domain, and (3) any [content fragments or templates](../content-management/fragments.md) you plan to reuse already published. Scheduled campaigns are the right choice here — not journeys — if this is a one-time or recurring send with no branching logic.

>[!ENDSHADEBOX]

| I want to... | Recommended capability | Start here |
| --- | --- | --- |
| Launch a product with an A/B test | Content experimentation **(AI)** | [Get started with content experimentation](../content-management/experiment-accelerator-gs.md) · [Create content experiments for email campaigns](https://experienceleague.adobe.com/en/docs/journey-optimizer-learn/tutorials/experimentation/content-experiments-for-emails){target="_blank"} |
| Notify customers of an outage or service update | Scheduled campaign + audiences | [About audiences](../audience/about-audiences.md) |
| Design a multi-step campaign with branching logic | Orchestrated campaigns | [Get started with orchestrated campaigns](../orchestrated/gs-orchestrated-campaigns.md) |
| Target only profiles that changed since my last campaign run | Orchestrated campaigns — incremental query | [Build queries in orchestrated campaigns](../orchestrated/build-query.md) <!-- TODO: verify target — no dedicated "incremental query" page found; build-query.md ("Build your first rule") is the closest existing page --> |
| Check how many profiles match my audience before launching | Audience preview | [About audiences](../audience/about-audiences.md) <!-- TODO: verify target — no "create-compositions.md#preview" page/anchor exists; about-audiences.md used as placeholder --> |
| Coordinate messaging across many channels at scale | Orchestration | [Get started with orchestrated campaigns](../orchestrated/gs-orchestrated-campaigns.md) · [Scaling orchestration to omnichannel engagement](https://experienceleague.adobe.com/en/docs/journey-optimizer-learn/scaling-orchestration-to-omnichannel-engagement/introduction){target="_blank"} |
| Send each message at the best time for each customer | Send-time optimization **(AI)** | [Send-time optimization](../building-journeys/send-time-optimization.md) |

## Personalize what each customer sees {#personalize}

For tailoring offers and content to each individual.

| I want to... | Recommended capability | Start here |
| --- | --- | --- |
| Show the best offer for each customer | Decisioning | [Get started with offer decisioning](../offers/get-started/starting-offer-decisioning.md) · [Web offers tutorial](https://experienceleague.adobe.com/en/docs/journey-optimizer-learn/use-decisioning-to-personalize-web-offers/introduction){target="_blank"} |

>[!BEGINSHADEBOX]

**Before you build:** decisioning requires a specific setup sequence. You need (1) [decision items (offers) created](../experience-decisioning/items.md) with eligibility rules and attributes, (2) a [selection strategy](../experience-decisioning/selection-strategies.md) or ranking formula configured, and (3) a [decision policy](../experience-decisioning/create-decision.md) attached to the surface where offers will appear. Skipping this sequence is the most common reason first-time decisioning setups fail to return results.

>[!ENDSHADEBOX]

| I want to... | Recommended capability | Start here |
| --- | --- | --- |
| Rank offers using a formula (zip code, income, weather) | Decisioning — ranking formula | [Ranking formulas](../experience-decisioning/ranking/ranking-formulas.md) · [Ranking formula tutorial](https://experienceleague.adobe.com/en/docs/journey-optimizer-learn/personalizing-offers-with-ranking-formulas-based-on-user-zip-code-and-income/introduction){target="_blank"} · [Weather data tutorial](https://experienceleague.adobe.com/en/docs/journey-optimizer-learn/personalizing-offers-with-real-time-weather-data/introduction){target="_blank"} |
| Use external product or CRM data to personalize offers | Decisioning — AEP dataset lookup | [Use dataset lookup in decisioning](../experience-decisioning/context-data.md) |
| Tailor message content with profile data | Personalization | [Personalize your content](../personalization/personalize.md) |
| Generate copy, images, and message variations | AI content generation **(AI)** | [AI content generation](../content-management/gs-generative.md) · [Tutorial](https://experienceleague.adobe.com/en/docs/journey-optimizer-learn/tutorials/content-management/ai-assistant/ai-assistant-for-content-generation-overview){target="_blank"} |
| Convert a design image into an editable email template | Image to HTML converter **(AI)** | [Convert an image to an email template](../content-management/image-to-html.md) |
| Automatically rank and personalize offers | AI ranking models **(AI)** | [AI models for decisioning](../experience-decisioning/ranking/ai-models.md) |
| Deliver always-on contextual content (no campaign) | Content cards | [Get started with content cards](../content-card/get-started-content-card.md) · [Create content cards](https://experienceleague.adobe.com/en/docs/journey-optimizer-learn/tutorials/channels/content-cards/create-content-cards){target="_blank"} |
| Deliver personalized content via API to any app or surface | Code-based experience | [Get started with code-based experience](../code-based/get-started-code-based.md) |
| Control which parts of an email template my team can edit | Content locking | [Lock content in email templates](../content-management/content-locking.md) |

## Coordinate & govern delivery {#coordinate-govern}

For controlling how, when, and how often customers are contacted across channels.

| I want to... | Recommended capability | Start here |
| --- | --- | --- |
| Prevent message fatigue across channels | Frequency capping | [Set frequency capping by channel](../conflict-prioritization/channel-capping.md) |
| Resolve conflicting or competing messages | Conflict prioritization | [Identify potential conflicts](../conflict-prioritization/conflicts.md) · [Tutorial](https://experienceleague.adobe.com/en/docs/journey-optimizer-learn/tutorials/conflict-management/identify-potential-conflicts){target="_blank"} |
| Decide which journey takes priority | Journey arbitration | [Use formulas to rank journeys](../conflict-prioritization/journey-ranking-formulas.md) |
| Respect quiet hours & consent | Quiet hours / Privacy | [Set quiet hours](../conflict-prioritization/quiet-hours.md) |
| Enforce consent policies and data usage labels across channels | Consent & data governance | [Get started with privacy](../privacy/get-started-privacy.md) |
| Get alerted when a journey has high error or discard rates | Journey alerts | [Set up journey alerts](../reports/alerts.md) |

## Choose a channel to deliver on {#choose-channel}

| I want to send on... | Channel | Start here |
| --- | --- | --- |
| Email newsletters, promotions, or transactional messages | Email | [Get started with email](../email/get-started-email.md) |
| Mobile push notifications (iOS and Android) | Push | [Get started with push notifications](../push/get-started-push.md) |
| SMS, MMS, or RCS text messages | SMS/MMS/RCS | [Get started with SMS/MMS/RCS](../mobile/get-started-mobile.md) · [Mobile Learning Hub](https://experienceleague.adobe.com/en/docs/journey-optimizer-learn/mobile-learning-hub/overview){target="_blank"} |
| WhatsApp messages via Meta Cloud API | WhatsApp | [Get started with WhatsApp](../whatsapp/get-started-whatsapp.md) |
| In-browser or in-app overlays and banners | In-app | [Get started with In-app](../in-app/get-started-in-app.md) |
| Personalized web page content | Web | [Get started with web channel](../web/get-started-web.md) |
| Any surface via API (kiosk, connected device, headless app) | Code-based experience | [Get started with code-based experience](../code-based/get-started-code-based.md) |
| Physical mail pieces triggered from a journey | Direct mail | [Get started with direct mail](../direct-mail/get-started-direct-mail.md) |

## Measure & optimize {#measure-optimize}

For tracking performance, diagnosing issues, and improving results over time.

| I want to... | Recommended capability | Start here |
| --- | --- | --- |
| See performance metrics for a live journey or campaign | Live reports | [Live reports](../reports/live-report.md) · [Monitor & analyze your journey with live reports](https://experienceleague.adobe.com/en/docs/journey-optimizer-learn/tutorials/report-and-monitor/monitor-and-analyze-your-journey-with-live-reports){target="_blank"} |
| Report on full campaign or journey performance after it ends | Global reports | [Get started with reporting](../reports/gs-reports.md) |
| Analyze an experiment and get next-step recommendations | Experimentation Agent **(AI)** | [Experimentation Agent](ai-features.md#experimentation-agent) · [Tutorial](https://experienceleague.adobe.com/en/docs/journey-optimizer-learn/tutorials/experimentation/experimentation-agent-overview){target="_blank"} |
| Monitor the health and latency of custom actions in my journeys | Custom action monitoring | [Use custom actions](../building-journeys/using-custom-actions.md) <!-- TODO: verify target — no dedicated "custom-action-monitoring.md" page found; using-custom-actions.md is the closest existing page --> |
| Get alerted when journey error or discard rates exceed thresholds | Journey alerts | [Set up journey alerts](../reports/alerts.md) |

## Starter flows {#starter-flows}

Each starter flow below is a short, outcome-oriented set of steps: what you will build, who it is for, and how to get there. Pick the goal that matches your first project and follow the links to the detailed documentation.

### Welcome new customers {#flow-welcome}

**You will build:** An automated welcome series that greets every new subscriber and nudges inactive ones.
**Best for:** Marketers · **Capability:** Event-triggered journey

1. Confirm your [unified profiles and audiences](../audience/get-started-profiles.md) are receiving the sign-up event.
1. [Create your first journey](../building-journeys/journey-gs.md) and use the sign-up event as the entry.
1. Add a welcome [email](../email/get-started-email.md), then a wait step and a follow-up [push notification](../push/get-started-push.md) for profiles that have not engaged.
1. [Personalize the content](../personalization/personalize.md) with profile attributes such as first name and stated interests.

➡️ [Start with journeys](../building-journeys/journey-gs.md)

### Recover abandoned carts {#flow-cart}

**You will build:** An automated recovery flow that reminds customers of items left behind.
**Best for:** Marketers · **Capability:** Event-triggered journey

1. Make sure the cart-abandonment event reaches Journey Optimizer (work with your [data team](../data/gs-data.md) if needed).
1. [Build a journey](../building-journeys/journey-gs.md) triggered by the abandonment event.
1. Send a personalized reminder email; if there is no click within 24 hours, branch to a [push](../push/get-started-push.md) follow-up.
1. [Personalize](../personalization/personalize.md) with the abandoned items and loyalty status.

➡️ [Start with journeys](../building-journeys/journey-gs.md)

### Send transactional messages {#flow-transactional}

**You will build:** On-demand order, shipping, or appointment confirmations triggered by an external system.
**Best for:** Marketers & Developers · **Capability:** Campaign triggered by an external system

1. Review how [campaigns triggered by an external system](../campaigns/api-triggered-campaigns.md) work and what payload they expect.
1. Design the message template and [personalize](../personalization/personalize.md) it with the transaction details.
1. Have your developer call the campaign endpoint from your order or fulfillment system.

➡️ [Work with campaigns triggered by an external system](../campaigns/api-triggered-campaigns.md)

### Launch a campaign with content testing {#flow-campaign}

**You will build:** A scheduled promotion that automatically picks the best-performing content.
**Best for:** Marketers · **Capability:** Scheduled campaign + content experimentation

1. [Get started with campaigns](../campaigns/get-started-with-campaigns.md) and define your audience.
1. Use [content generation](../content-management/gs-generative.md) to draft subject-line and copy variations.
1. Set up a [content experiment](../content-management/experiment-accelerator-gs.md) to test variants on a sample, then send the winner to the rest.

➡️ [Get started with campaigns](../campaigns/get-started-with-campaigns.md)

### Personalize offers per customer {#flow-offers}

**You will build:** A decision that shows the single best offer to each customer.
**Best for:** Marketers · **Capability:** Decisioning

1. [Get started with offer decisioning](../offers/get-started/starting-offer-decisioning.md) and create your offers and eligibility rules.
1. Add the decision to a [journey](../building-journeys/journey-gs.md) or campaign message.
1. Layer in [intelligent features](ai-features.md) to rank and optimize offers automatically.

➡️ [Get started with offer decisioning](../offers/get-started/starting-offer-decisioning.md)

## Example scenarios {#example-scenarios}

These examples illustrate how Journey Optimizer's capabilities work together across different roles, industries, and channels.

### Delayed shipment recovery {#scenario-delayed-shipment}

**Role:** Marketer | **Core capability:** [Unified profile + audience exclusion](../audience/get-started-profiles.md)

A clothing store typically sends post-purchase surveys to all customers who have purchased products in the last week. Due to inclement weather, a few shipments experienced delays. Seeing which customers have not received their shipments, the clothing store can exclude them from the scheduled customer satisfaction send and instead send a personalized email apologizing for the delay and offering a discount code with product recommendations based on the customer's past purchases.

[Get started with campaigns](../campaigns/get-started-with-campaigns.md)

### Real-time in-store engagement {#scenario-instore}

**Role:** Marketer | **Core capability:** [Geofence triggering + push](../push/get-started-push.md)

The same retailer can engage a loyal customer who pulls into the store parking lot by sending them a push notification about a sweater that is back in stock in the customer's size.

[Get started with push notifications](../push/get-started-push.md)

### Cart abandonment recovery {#scenario-cart}

**Role:** Marketer | **Core capability:** [Event-triggered multi-step journey](../building-journeys/journey-gs.md)

When a customer adds items to an online cart but leaves without completing the purchase, Journey Optimizer detects the event and starts a recovery journey automatically. The customer receives a personalized email reminding them of the items left behind. If they do not click through within 24 hours, a follow-up push notification is sent — personalized based on their browsing history and loyalty status.

[Build your first journey](../building-journeys/journey-gs.md)

### Streaming service welcome series {#scenario-welcome}

**Role:** Marketer | **Core capability:** [Event-triggered welcome journey](../building-journeys/journey-gs.md)

When a customer subscribes to a streaming service, Journey Optimizer detects the sign-up event and immediately starts a multi-step welcome journey. The customer receives a welcome email encouraging them to open the app for the first time. If no login activity is detected within 48 hours, a follow-up push notification is sent with personalized content recommendations based on their stated interests during sign-up — turning a passive subscriber into an active, engaged user from day one.

[Build your first journey](../building-journeys/journey-gs.md)

### Reservation reminder with directions {#scenario-reservation}

**Role:** Marketer | **Core capability:** [Scheduled + location-aware messaging](../campaigns/get-started-with-campaigns.md)

A hospitality brand sends each guest a timely reminder one hour before their reservation. The notification includes the guest's name, reservation time, and location-based directions to the venue — automatically assembled from the customer profile and booking data, with no manual effort from the marketing team.

[Get started with campaigns](../campaigns/get-started-with-campaigns.md)

### Proactive service outage notification {#scenario-outage}

**Role:** Operations | **Core capability:** [Automated audience selection at scale](../audience/about-audiences.md)

When a service disruption occurs, Journey Optimizer automatically identifies the affected customers based on their account data and usage patterns. Those customers receive a proactive notification acknowledging the issue and outlining next steps — turning a potentially negative experience into a moment of transparency and trust, delivered at scale.

[Build your first journey](../building-journeys/journey-gs.md)

### Intelligent promotional campaign {#scenario-ai-campaign}

**Role:** Marketer | **Core capability:** [Content generation + experimentation](ai-features.md)

A retail brand planning a product launch uses Journey Optimizer's AI Assistant to generate multiple subject line and body copy variations in minutes — guided by a natural language prompt and their uploaded brand guidelines. Built-in content experimentation automatically identifies the best-performing variant among an initial audience sample. The winning message is then deployed to the remaining recipients, maximizing engagement without additional copywriting effort.

[Explore intelligent features](ai-features.md) | [Learn about content experimentation](../content-management/experiment-accelerator-gs.md)

### Maintenance alerts via mobile app {#scenario-maintenance}

**Role:** Operations | **Core capability:** [Non-marketing journey orchestration](../building-journeys/journey-gs.md)

Non-marketers such as operations teams and customer support can use [!DNL Adobe Journey Optimizer] to manage operational notifications or monitor onboarding processes. For example, an amusement park where visitors download a mobile app as part of their experience: maintenance staff can use Journey Optimizer to notify park visitors of rides currently closed due to maintenance.

[Build your first journey](../building-journeys/journey-gs.md)

## Video library {#videos}

Browse curated video content by topic. Each tab links to the relevant tutorials and playlists on Experience League.

>[!BEGINTABS]

>[!TAB Getting started]

* [Introduction to Journey Optimizer](https://experienceleague.adobe.com/en/docs/journey-optimizer-learn/tutorials/introduction-to-journey-optimizer/introduction){target="_blank"} — Core concepts and a product tour.
* [Journey Optimizer tutorials overview](https://experienceleague.adobe.com/en/docs/journey-optimizer-learn/tutorials/overview){target="_blank"} — The full catalog of guided videos.

>[!TAB Journeys & campaigns]

* [Introduction to building a journey](https://experienceleague.adobe.com/en/docs/journey-optimizer-learn/tutorials/journeys/introduction-to-building-a-journey){target="_blank"} — Build your first event-triggered journey.
* [Build journeys with Journey Agent](https://experienceleague.adobe.com/en/docs/journey-optimizer-learn/tutorials/journeys/journey-agent-overview){target="_blank"} — Create journeys from a natural-language prompt.

>[!TAB Personalization & intelligence]

* [AI Assistant for content generation](https://experienceleague.adobe.com/en/docs/journey-optimizer-learn/tutorials/content-management/ai-assistant/ai-assistant-for-content-generation-overview){target="_blank"} — Generate copy, images, and variations.
* [Use decisioning to personalize web offers](https://experienceleague.adobe.com/en/docs/journey-optimizer-learn/use-decisioning-to-personalize-web-offers/introduction){target="_blank"} — Tailor offers per customer.

>[!TAB Reporting & optimization]

* [Monitor & analyze your journey with live reports](https://experienceleague.adobe.com/en/docs/journey-optimizer-learn/tutorials/report-and-monitor/monitor-and-analyze-your-journey-with-live-reports){target="_blank"} — Track performance as your journeys run.
* [Create content experiments for email campaigns](https://experienceleague.adobe.com/en/docs/journey-optimizer-learn/tutorials/experimentation/content-experiments-for-emails){target="_blank"} — Test and optimize content.

>[!ENDTABS]

## Choosing between journeys, campaigns, and orchestrated campaigns {#choosing}

| Scenario | Use |
|----------|-----|
| Behavior-driven, multi-step, each customer moves at their own pace | Journey |
| Simple scheduled or API-triggered message to an audience | Campaign |
| Complex batch workflow with multi-entity segmentation | Orchestrated campaign |

## Not sure? {#not-sure}

If your goal maps to a term you are unfamiliar with, or you are unsure which capability the table points to, start with the [Journey Optimizer key terminology](terminology.md) page to clarify the concepts behind each capability.

You can also build hands-on confidence with the end-to-end exercises in the [Journey Optimizer tutorials](https://experienceleague.adobe.com/en/docs/journey-optimizer-learn/tutorials/overview){target="_blank"}.
