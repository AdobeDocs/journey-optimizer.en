---
title: AI Knowledge Reference
---
# AI Knowledge Reference

+++ AI Knowledge Reference

This section contains structured knowledge intended to support interpretation, retrieval, and question answering related to this topic.

For complete understanding, this information should be combined with the documentation on this page. Neither source is intended to stand alone; the page describes the feature, while this section provides additional context that helps disambiguate terminology, intent, applicability, and constraints.

- **TL;DR:** This page is a curated library of practical journey use cases — covering experience events, dataset queries, business scenarios, technical patterns, video tutorials, and community blog posts — to help practitioners get the most out of Adobe Journey Optimizer.

**Intents:**
- Find practical use case examples covering business scenarios such as multi-channel messaging, subscriber campaigns, and weekday-only email delivery
- Locate technical use case patterns for custom actions, throughput limiting, and removing profiles from a live journey
- Access video tutorials for common journey patterns including customer onboarding, cart abandonment, and re-engagement
- Query Adobe Journey Optimizer datasets (step events, tracking events, offer propositions) to build custom analytics and reporting
- Use Experience Event lookup patterns to manage opt-outs, frequency, and real-time personalization

**Glossary:**
- **Experience Event**: A time-stamped record of a customer interaction (e.g., purchase, click, page view) stored in Adobe Experience Platform and used to trigger or personalise journeys *(product-specific)*
- **Step event**: An automatically generated dataset record that captures every step a profile takes in a journey, used for custom reporting and debugging *(product-specific)*
- **Custom action**: A journey activity that calls an external API to send data to or receive data from a third-party system *(product-specific)*

**Guardrails:**
- Each use case example includes recommendations that should be tailored to specific needs; they are starting points, not prescriptive configurations
- Dataset queries require access to Adobe Experience Platform Query Service
- Video tutorials reference external learning resources on Experience League

**Terminology:**
- Canonical name: Use cases — Acronym: none — variants: journey use cases, practical examples, recipes
- Synonyms: "business use case" = "marketing use case"; "technical use case" = "developer use case"

**FAQ:**
- **Q: Where do I start if I am new to journey entry and exit criteria?** — Begin with the comprehensive guide to journey entry and exit criteria, which includes real-world use cases, best practices, and step-by-step configuration guidance.
- **Q: How do I query journey step events for custom reporting?** — Use the Adobe Experience Platform Query Service to query the journey step events dataset; example queries are available in the linked datasets query examples page.
- **Q: Where can I find a use case for sending emails only on weekdays?** — See the weekday email use case page, also available as a community blog post.
- **Q: How can I remove profiles from a live journey?** — Use the profile attribute exit criteria feature on a paused journey, as described in the technical use case for removing profiles from a live journey.

+++
