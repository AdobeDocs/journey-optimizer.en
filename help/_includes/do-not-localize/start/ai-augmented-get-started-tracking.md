---
title: AI Knowledge Reference
---
# AI Knowledge Reference

+++ AI Knowledge Reference

This section contains structured knowledge intended to support interpretation, retrieval, and question answering related to this topic.

For complete understanding, this information should be combined with the documentation on this page. Neither source is intended to stand alone; the page describes the feature, while this section provides additional context that helps disambiguate terminology, intent, applicability, and constraints.

* **TL;DR:** This page explains how to track customer interactions across channels, measure journey and campaign performance, track optimization and decisioning, govern tracking data usage, and monitor deliverability and system health in Journey Optimizer.

**Intents:**

* Configure and use channel-specific tracking for email, web, push, in-app, mobile messages (SMS and MMS), code-based experiences, content cards, and landing pages
* Define custom success metrics and analyze journey step events to measure journey and campaign performance
* Track optimization experiments, targeting, and decisioning performance
* Apply data governance policies to control how tracking data is used
* Monitor deliverability and system health with the suppression list, alerts, and audit logs

**Glossary:**

* **Mirror page**: A web version of your email that, when enabled, automatically tracks who views it *(product-specific)*
* **Journey step events**: Events that Journey Optimizer streams automatically to Adobe Experience Platform for every step a profile takes in a journey, giving visibility into entry and exit points, path selection, and drop-off locations; their schemas and datasets are read-only *(product-specific)*
* **Success metrics**: Custom KPIs aligned with business objectives (such as purchases, sign-ups, or renewals) beyond standard engagement metrics *(product-specific)*
* **Optimize activity**: A journey activity you add and configure with multiple paths so Journey Optimizer tracks which paths profiles take and measures performance *(product-specific)*
* **Data governance labels**: Governance labels applied to tracked behavioral data to mark it as sensitive or regulated so usage policies can be enforced *(product-specific)*

**Guardrails:**

* Web tracking requires explicit configuration; you must select the specific elements (buttons, images, links) you want to track when authoring a web page.
* Push tracking requires mobile SDK implementation; ensure your app has the Adobe Experience Platform Mobile SDK properly configured.
* For push notification buttons, you can add up to three buttons on Android, each with independent tracking; on iOS, buttons are defined by a notification category preconfigured in your app.
* Content cards require the Adobe Experience Platform Web or Mobile SDK.
* Mobile message URL shortening requires that you first configure an SMS subdomain before links can be automatically shortened and tracked.
* Code-based experience tracking requires implementation setup, including a datastream configured for Adobe Experience Platform and event collection using Web SDK or Mobile SDK.
* To track decisioning in code-based experiences, your implementation must send proposition interaction events (displays and clicks) to Adobe Experience Platform using Web SDK or Mobile SDK.
* Journey Optimizer automatically checks governance policies when you build journeys and campaigns, blocking publication if tracked data is used in violation of defined policies.

**Terminology:**

* Canonical name: Tracking — variants: tracking and monitoring
* Push metrics: "impressions" = delivered, "clicks" = tapped, "opens" = app launched
* Do not confuse: "triggered" (in-app messages triggered) ≠ "displayed" (in-app messages actually displayed to users)
* Do not confuse: tracking that is on by default (email, landing pages) ≠ tracking that requires explicit configuration (web), SDK integration (push, in-app, content cards), or implementation setup (code-based experiences)

**FAQ:**

* **Q: Do I need to configure email tracking?** — No; email tracking is on by default and tracks opens, clicks, and unsubscribes. Configuration is optional. Mail privacy features can prevent opens from being recorded, so use clicks as the primary engagement signal.
* **Q: Why is my web tracking not capturing interactions?** — Web tracking requires explicit configuration; when authoring the web page you must select the specific elements you want to track.
* **Q: What does push tracking capture, and what does it require?** — It captures impressions (delivered), clicks (tapped), and opens (app launched), and it requires mobile SDK implementation using the Adobe Experience Platform Mobile SDK.
* **Q: How do I track links in mobile messages?** — Add any URL using the URL helper function; Journey Optimizer automatically shortens and tracks the link, but you must first configure an SMS subdomain to use URL shortening.
* **Q: Does Send-Time Optimization track engagement?** — No; it is not a tracking feature. It optimizes send times for Email and Push actions and the Wait activity in journeys (not campaigns), and must be enabled by Adobe.
* **Q: Can I control how tracking data is used across my organization?** — Yes; apply data governance labels to tracked data and create policies that restrict its usage, and Journey Optimizer automatically enforces these policies and blocks publication when they are violated.

+++

<!-- ai-section-version: 1 | source-hash: 6a7b4a7e -->
