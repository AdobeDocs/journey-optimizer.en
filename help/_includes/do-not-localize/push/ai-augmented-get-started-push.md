---
title: AI Knowledge Reference
---
# AI Knowledge Reference

+++ AI Knowledge Reference

This section contains structured knowledge intended to support interpretation, retrieval, and question answering related to this topic.

For complete understanding, this information should be combined with the documentation on this page. Neither source is intended to stand alone; the page describes the feature, while this section provides additional context that helps disambiguate terminology, intent, applicability, and constraints.

* **TL;DR:** This page introduces push notifications in Journey Optimizer for reaching mobile app users and web visitors through journeys and campaigns, and covers when to use or not use the channel.

**Intents:**

* Understand what push notifications enable in Journey Optimizer
* Decide whether to create a push in a journey or a campaign
* Define push settings for iOS, Android, and Web platforms
* Evaluate use cases where push is the right channel and where it is not
* Understand how push opt-in and opt-out are handled

**Glossary:**

* **Push notification**: A message that reaches mobile app users and web visitors at any time, including when they are not actively using the app or website *(product-specific)*
* **Opt-in**: The consent device platforms require before end-users can receive or view notifications, obtainable as early as first app launch post-install *(product-specific)*

**Guardrails:**

* Before creating a push notification for the first time, the Push channel must be configured.
* Device platforms require opt-in before end-users may receive or view notifications.
* Push notifications do not require opt-out management on your side: recipients unsubscribe through their devices, and their notification settings via the mobile OS or web browser.

**Terminology:**

* Canonical name: Push notification — Acronym: n/a — variants: push, notification
* Synonyms: "mobile app users and web visitors" = target recipients of push
* Do not confuse: creating a push "In a Journey" ≠ creating a push "In a Campaign"

**FAQ:**

* **Q: Where can push notifications be created?** — In a Journey (via a Push activity) or in a Campaign (by selecting Push notification as the action).
* **Q: Which platforms are supported?** — iOS, Android, and Web, configured via dedicated tabs.
* **Q: Do I need to manage push opt-out?** — No, recipients can unsubscribe through their devices or via mobile OS / browser notification settings.
* **Q: When should I not use push?** — When opt-in rates are low, the message needs long-form content, the content is sensitive and shouldn't appear on a lock screen, or most users are on desktop.
* **Q: How do I check a profile's push consent status?** — In the AEP profile viewer, via Check push opt-out status.

+++

<!-- ai-section-version: 1 | source-hash: dbe9001f -->
