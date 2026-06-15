---
solution: Journey Optimizer
product: journey optimizer
title: Find the right Journey Optimizer capability for your goal
description: A goal-first decision guide that maps common practitioner goals to the right Adobe Journey Optimizer capability, with hands-on tutorials, so you can find the right tool for what you want to accomplish and start quickly.
feature: Get Started
topic: Content Management
role: User
level: Beginner
keywords: journey optimizer, use case, decision guide, which capability, get started, practitioner goals, tutorials
---
# Find the right Journey Optimizer capability for your goal {#ajo-use-case-guide}

>[!BEGINSHADEBOX]

**On this page:** Start from what you want to accomplish, then jump to the Adobe Journey Optimizer capability that solves it — without needing to know the feature name first.

>[!ENDSHADEBOX]

[!DNL Adobe Journey Optimizer] offers many capabilities, and the right one depends on what you are trying to achieve. This guide is organized around business goals rather than product features: find the goal that matches your need, then follow the link to start with the recommended capability.

Where an end-to-end tutorial isn't available for a specific scenario, the link takes you to the best current starting point to learn the capability and begin.

AI is built into many of these capabilities — look for the **(AI)** tag in the tables below. The conversational [AI Assistant](ai-features.md#ai-assistant) can also answer product questions and surface operational insights about your journeys at any time. For the full set of intelligent features, see [AI & intelligent features](ai-features.md).

>[!TIP]
>
>New to Journey Optimizer? Browse the full [Journey Optimizer tutorials](https://experienceleague.adobe.com/en/docs/journey-optimizer-learn/tutorials/overview){target="_blank"} (videos and guided walkthroughs), follow an expert-curated [video playlist](https://experienceleague.adobe.com/en/playlists?solution=Journey+Optimizer){target="_blank"}, and practice in a [training sandbox](https://experienceleague.adobe.com/en/docs/journey-optimizer-learn/configure-a-training-sandbox/introduction-and-prerequisites){target="_blank"} or with the [hands-on challenges](https://experienceleague.adobe.com/en/docs/journey-optimizer-learn/challenges/introduction-and-prerequisites){target="_blank"}.

## Set up Journey Optimizer for your team {#setup-admin}

For administrators and technical users who need to configure the environment before building journeys or campaigns.

| I want to... | Recommended capability | Start here |
| --- | --- | --- |
| Configure email, SMS, or push channels before sending | Channel configuration | [Get started with channel configuration](../configuration/get-started-configuration.md) |
| Warm up a new IP address for email sending | IP warmup plan | [Get started with IP warmup](../configuration/ip-warmup-gs.md) |
| Set up roles, permissions, and access control | Access control | [Get started with access control](../administration/permissions-overview.md) |
| Work across multiple environments or regions | Sandboxes | [Work with sandboxes](../administration/sandboxes.md) |

## Engage customers in real time {#engage-real-time}

For scenarios where you react to a customer action or event as it happens.

| I want to... | Recommended capability | Start here |
| --- | --- | --- |
| Welcome a new customer or subscriber automatically | Event-triggered journey | [Get started with journeys](../building-journeys/journey-gs.md) · [Introduction to building a journey](https://experienceleague.adobe.com/en/docs/journey-optimizer-learn/tutorials/journeys/introduction-to-building-a-journey){target="_blank"} |
| Recover an abandoned cart or browse session | Event-triggered journey | [Get started with journeys](../building-journeys/journey-gs.md) · [Abandoned browse tutorial](https://experienceleague.adobe.com/en/docs/experience-platform/rtcdp/use-cases/personalization-insights-engagement/use-cases-luma){target="_blank"} |
| Trigger a journey from a website form submission | Event-triggered journey | [Get started with journeys](../building-journeys/journey-gs.md) · [Tutorial](https://experienceleague.adobe.com/en/docs/journey-optimizer-learn/trigger-journey-on-form-submission/introduction){target="_blank"} |
| React to in-app behavior (app open, screen view) | Journeys + In-app | [Get started with In-app](../in-app/get-started-in-app.md) |
| Send order, shipping, or appointment confirmations | API-triggered campaign | [Work with API-triggered campaigns](../campaigns/api-triggered-campaigns.md) |
| Re-engage inactive or lapsing customers | Journeys + audiences | [Get started with profiles & audiences](../audience/get-started-profiles.md) · [Create audiences using the rule builder](https://experienceleague.adobe.com/en/docs/journey-optimizer-learn/tutorials/profiles-audiences-subscriptions/create-audiences-using-the-rule-builder){target="_blank"} |
| Test a journey with real data before activating it | Journey dry run | [Test your journey with dry run](../building-journeys/journey-dry-run.md) |
| Pause a live journey to make edits without stopping in-flight profiles | Journey pause & resume | [Pause and resume a journey](../building-journeys/journey-pause.md) |
| Build or optimize a journey from a natural-language prompt | Journey Agent **(AI)** | [AI agents](ai-features.md#ai-agents) · [Journey Agent tutorial](https://experienceleague.adobe.com/en/docs/journey-optimizer-learn/tutorials/journeys/journey-agent-overview){target="_blank"} |

## Reach audiences at scale {#reach-at-scale}

For scheduled, one-to-many outreach to a defined audience.

| I want to... | Recommended capability | Start here |
| --- | --- | --- |
| Send a newsletter or promotion to a segment | Scheduled campaign | [Get started with campaigns](../campaigns/get-started-with-campaigns.md) |
| Launch a product with an A/B test | Content experimentation **(AI)** | [Get started with content experimentation](../content-management/experiment-accelerator-gs.md) · [Create content experiments for email campaigns](https://experienceleague.adobe.com/en/docs/journey-optimizer-learn/tutorials/experimentation/content-experiments-for-emails){target="_blank"} |
| Notify customers of an outage or service update | Scheduled campaign + audiences | [About audiences](../audience/about-audiences.md) |
| Design a multi-step campaign with branching logic | Orchestrated campaigns | [Get started with orchestrated campaigns](../orchestrated/gs-orchestrated-campaigns.md) |
| Target only profiles that changed since my last campaign run | Orchestrated campaigns — incremental query | [Build queries in orchestrated campaigns](../orchestrated/build-query.md) <!-- TODO: verify target — no dedicated "incremental query" page found; build-query.md ("Build your first rule") is the closest existing page --> |
| Check how many profiles match my audience before launching | Audience preview | [About audiences](../audience/about-audiences.md) <!-- TODO: verify target — no "create-compositions.md#preview" page/anchor exists; about-audiences.md used as placeholder --> |
| Coordinate messaging across many channels at scale | Orchestration | [Scaling orchestration to omnichannel engagement](https://experienceleague.adobe.com/en/docs/journey-optimizer-learn/scaling-orchestration-to-omnichannel-engagement/introduction){target="_blank"} |
| Send each message at the best time for each customer | Send-time optimization **(AI)** | [Send-time optimization](../building-journeys/send-time-optimization.md) |

## Personalize what each customer sees {#personalize}

For tailoring offers and content to each individual.

| I want to... | Recommended capability | Start here |
| --- | --- | --- |
| Show the best offer for each customer | Decisioning | [Get started with offer decisioning](../offers/get-started/starting-offer-decisioning.md) · [Web offers tutorial](https://experienceleague.adobe.com/en/docs/journey-optimizer-learn/use-decisioning-to-personalize-web-offers/introduction){target="_blank"} |
| Rank offers using a formula (zip code, income, weather) | Decisioning — ranking formula | [Ranking formula tutorial](https://experienceleague.adobe.com/en/docs/journey-optimizer-learn/personalizing-offers-with-ranking-formulas-based-on-user-zip-code-and-income/introduction){target="_blank"} · [Weather data tutorial](https://experienceleague.adobe.com/en/docs/journey-optimizer-learn/personalizing-offers-with-real-time-weather-data/introduction){target="_blank"} |
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

## Not sure? {#not-sure}

If your goal maps to a term you are unfamiliar with, or you are unsure which capability the table points to, start with the [Journey Optimizer key terminology](terminology.md) page to clarify the concepts behind each capability.

You can also build hands-on confidence with the end-to-end exercises in the [Journey Optimizer tutorials](https://experienceleague.adobe.com/en/docs/journey-optimizer-learn/tutorials/overview){target="_blank"}.
