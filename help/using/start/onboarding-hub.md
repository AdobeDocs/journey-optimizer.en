---
solution: Journey Optimizer
product: journey optimizer
title: Onboarding hub - playbooks, use cases & videos
description: A curated onboarding hub for Adobe Journey Optimizer that brings together step-by-step playbooks, real-world use cases, and video content so new users can ramp up quickly and deliver their first customer experience.
feature: Get Started
topic: Content Management
role: User
level: Beginner
hide: true
keywords: journey optimizer, onboarding, playbooks, use cases, videos, tutorials, get started, ramp up, first journey
---
# Onboarding hub: playbooks, use cases & videos {#onboarding-hub}

>[!BEGINSHADEBOX]

**On this page:** Ramp up on Adobe Journey Optimizer fast — watch a short orientation, follow an outcome-oriented playbook to ship your first experience, browse real-world use cases, and dive into curated video content.

>[!ENDSHADEBOX]

New to [!DNL Adobe Journey Optimizer]? This hub gathers the resources that help you go from zero to your first live customer experience: **playbooks** (guided, step-by-step recipes for common goals), **use cases** (real-world scenarios that show what is possible), and **video content** (tutorials, walkthroughs, and hands-on practice).

>[!TIP]
>
>Not sure which capability fits your goal? Start with the goal-first [Find the right Journey Optimizer capability for your goal](ajo-use-case-guide.md) guide, then come back here for a step-by-step playbook.

## Start here: watch & learn {#start-here}

If you have ten minutes, begin with this orientation video. It walks through the interface and highlights the key capabilities by role.

>[!VIDEO](https://video.tv.adobe.com/v/3424995?quality=12)

Then build hands-on confidence with these learning resources:

* [Journey Optimizer tutorials](https://experienceleague.adobe.com/en/docs/journey-optimizer-learn/tutorials/overview){target="_blank"} — Step-by-step videos and guided walkthroughs for every role.
* [Expert-curated video playlist](https://experienceleague.adobe.com/en/playlists?solution=Journey+Optimizer){target="_blank"} — A sequenced set of short videos to watch in order.
* [Training sandbox](https://experienceleague.adobe.com/en/docs/journey-optimizer-learn/configure-a-training-sandbox/introduction-and-prerequisites){target="_blank"} — A safe environment with sample data to practice in.
* [Hands-on challenges](https://experienceleague.adobe.com/en/docs/journey-optimizer-learn/challenges/introduction-and-prerequisites){target="_blank"} — Apply what you learn with guided exercises.

## Onboarding playbooks {#playbooks}

Each playbook is a short, outcome-oriented recipe: what you will build, who it is for, and the steps to get there. Pick the one that matches your first goal and follow the links to the detailed documentation.

### Playbook 1 — Welcome new customers {#playbook-welcome}

**You will build:** An automated welcome series that greets every new subscriber and nudges inactive ones.
**Best for:** Marketers · **Capability:** Event-triggered journey

1. Confirm your [unified profiles and audiences](../audience/get-started-profiles.md) are receiving the sign-up event.
2. [Create your first journey](../building-journeys/journey-gs.md) and use the sign-up event as the entry.
3. Add a welcome [email](../email/get-started-email.md), then a wait step and a follow-up [push notification](../push/get-started-push.md) for profiles that have not engaged.
4. [Personalize the content](../personalization/personalize.md) with profile attributes such as first name and stated interests.

➡️ [Start with journeys](../building-journeys/journey-gs.md)

### Playbook 2 — Recover abandoned carts {#playbook-cart}

**You will build:** A real-time recovery flow that reminds customers of items left behind.
**Best for:** Marketers · **Capability:** Event-triggered journey

1. Make sure the cart-abandonment event reaches Journey Optimizer (work with your [data team](../data/gs-data.md) if needed).
2. [Build a journey](../building-journeys/journey-gs.md) triggered by the abandonment event.
3. Send a personalized reminder email; if there is no click within 24 hours, branch to a [push](../push/get-started-push.md) follow-up.
4. [Personalize](../personalization/personalize.md) with the abandoned items and loyalty status.

➡️ [Start with journeys](../building-journeys/journey-gs.md)

### Playbook 3 — Send transactional messages {#playbook-transactional}

**You will build:** On-demand order, shipping, or appointment confirmations triggered by an external system.
**Best for:** Marketers & Developers · **Capability:** API-triggered campaign

1. Review how [API-triggered campaigns](../campaigns/api-triggered-campaigns.md) work and what payload they expect.
2. Design the message template and [personalize](../personalization/personalize.md) it with the transaction details.
3. Have your developer call the campaign endpoint from your order or fulfillment system.

➡️ [Work with API-triggered campaigns](../campaigns/api-triggered-campaigns.md)

### Playbook 4 — Launch a campaign with A/B testing {#playbook-campaign}

**You will build:** A scheduled promotion that automatically picks the best-performing content.
**Best for:** Marketers · **Capability:** Scheduled campaign + content experimentation

1. [Get started with campaigns](../campaigns/get-started-with-campaigns.md) and define your audience.
2. Use [AI content generation](../content-management/gs-generative.md) to draft subject-line and copy variations.
3. Set up a [content experiment](../content-management/experiment-accelerator-gs.md) to test variants on a sample, then send the winner to the rest.

➡️ [Get started with campaigns](../campaigns/get-started-with-campaigns.md)

### Playbook 5 — Personalize offers per customer {#playbook-offers}

**You will build:** A decision that shows the single best offer to each customer.
**Best for:** Marketers · **Capability:** Decisioning

1. [Get started with offer decisioning](../offers/get-started/starting-offer-decisioning.md) and create your offers and eligibility rules.
2. Add the decision to a [journey](../building-journeys/journey-gs.md) or campaign message.
3. Layer in [AI features](ai-features.md) to rank and optimize offers automatically.

➡️ [Get started with offer decisioning](../offers/get-started/starting-offer-decisioning.md)

## Use cases by goal {#use-cases}

The playbooks above cover the most common starting points, but Journey Optimizer supports many more scenarios — from proactive outage notifications and customer re-engagement to real-time, location-aware messaging. Each scenario combines one or more capabilities working together.

To find the exact capability for *your* goal, use the complete, goal-organized index in [Find the right Journey Optimizer capability for your goal](ajo-use-case-guide.md). For end-to-end, worked examples, see the [Journey use cases library](../building-journeys/jo-use-cases.md).

## Video library {#videos}

Browse curated video content by topic. Each tab links to the relevant tutorials and playlists on Experience League.

>[!BEGINTABS]

>[!TAB Getting started]

* [Introduction to Journey Optimizer](https://experienceleague.adobe.com/en/docs/journey-optimizer-learn/tutorials/introduction-to-journey-optimizer/introduction){target="_blank"} — Core concepts and a product tour.
* [Journey Optimizer tutorials overview](https://experienceleague.adobe.com/en/docs/journey-optimizer-learn/tutorials/overview){target="_blank"} — The full catalog of guided videos.

>[!TAB Journeys & campaigns]

* [Introduction to building a journey](https://experienceleague.adobe.com/en/docs/journey-optimizer-learn/tutorials/journeys/introduction-to-building-a-journey){target="_blank"} — Build your first event-triggered journey.
* [Build journeys with Journey Agent](https://experienceleague.adobe.com/en/docs/journey-optimizer-learn/tutorials/journeys/journey-agent-overview){target="_blank"} — Create journeys from a natural-language prompt.

>[!TAB Personalization & AI]

* [AI Assistant for content generation](https://experienceleague.adobe.com/en/docs/journey-optimizer-learn/tutorials/content-management/ai-assistant/ai-assistant-for-content-generation-overview){target="_blank"} — Generate copy, images, and variations.
* [Use decisioning to personalize web offers](https://experienceleague.adobe.com/en/docs/journey-optimizer-learn/use-decisioning-to-personalize-web-offers/introduction){target="_blank"} — Tailor offers per customer.

>[!TAB Reporting & optimization]

* [Monitor & analyze your journey with live reports](https://experienceleague.adobe.com/en/docs/journey-optimizer-learn/tutorials/report-and-monitor/monitor-and-analyze-your-journey-with-live-reports){target="_blank"} — Track performance in real time.
* [Create content experiments for email campaigns](https://experienceleague.adobe.com/en/docs/journey-optimizer-learn/tutorials/experimentation/content-experiments-for-emails){target="_blank"} — Test and optimize content.

>[!ENDTABS]

## Onboarding checklist by role {#checklist}

Onboarding spans several roles. Pick your role to see a focused starting path:

* **Administrator** — Set up sandboxes, permissions, and channels. [Get started as an Administrator](path/administrator.md)
* **Data Engineer** — Model schemas and ingest data. [Get started as a Data Engineer](path/data-engineer.md)
* **Developer** — Integrate SDKs and trigger events. [Get started as a Developer](path/developer.md)
* **Marketer** — Build journeys, content, and audiences. [Get started as a Marketer](path/marketer.md)

For a full overview of how these roles work together, see [Roles and responsibilities](quick-start.md).

## Related resources {#related-resources}

* [Find the right Journey Optimizer capability for your goal](ajo-use-case-guide.md) — Goal-first decision guide to every capability.
* [Journey use cases library](../building-journeys/jo-use-cases.md) — Practical examples and implementation patterns.
* [Key terminology](terminology.md) — Clarify the concepts behind each capability.
* [AI & intelligent features](ai-features.md) — Explore AI Assistant, send-time optimization, and content generation.
* [Get started with data management](../data/gs-data.md) — How data is ingested, unified, and activated.
