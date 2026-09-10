---
title: AI Knowledge Reference
---
# AI Knowledge Reference

+++ AI Knowledge Reference

This section contains structured knowledge intended to support interpretation, retrieval, and question answering related to this topic.

For complete understanding, this information should be combined with the documentation on this page. Neither source is intended to stand alone; the page describes the feature, while this section provides additional context that helps disambiguate terminology, intent, applicability, and constraints.

* **TL;DR:** This page explains how to design push notification content for iOS, Android, and Web, including the Title and Body, on-click behavior, media, buttons, silent notifications, custom data, Decisioning personalization, and advanced options.

**Intents:**

* Compose the push Title and Body with personalization, inline attributes, and AI content generation
* Configure on-click behavior (Open app, Deeplink, or Web URL)
* Add media and call-to-action buttons per platform
* Send a silent (background) notification and add custom data key-value pairs
* Personalize push content with Decisioning
* Set advanced platform-specific options (collapsible, badges, expiration, priority, etc.)

**Glossary:**

* **On click behavior**: The action that occurs when a recipient taps the body of the push notification — Open app, Deeplink, or Web URL *(product-specific)*
* **Silent Notification**: A background notification delivered directly to the application with no alert displayed on the device screen *(product-specific)*
* **Custom data**: Key-value pairs added to the payload depending on the mobile application configuration *(product-specific)*
* **Decisioning**: A capability to personalize and optimize push content using Priority Scores, Formulas, or AI Models to select the best content *(product-specific)*
* **Add mutable-content flag**: An iOS advanced option that allows push content to be modified by a notification service extension; required for media attachments to render on iOS *(product-specific)*

**Guardrails:**

* For Android, you can add up to three buttons.
* Web push notifications do not support the Silent Notification feature.
* On iOS, the Add mutable-content flag option must be enabled when including media attachments (such as `adb_media`) for them to render, and the app must implement a Notification Service Extension.
* If the device screen is locked, buttons are not displayed; only the Title and the Message are visible.
* For iOS buttons, notification categories must be preconfigured in the iOS app to define the buttons displayed and actions taken.
* On iOS, Push expiration is enforced as a hard stop: any message reaching APNS after its expiration time is not delivered.
* Android media supports only an image icon and an image for expanded notifications.

**Terminology:**

* Canonical name: On click behavior — Acronym: n/a — variants: on-click behavior
* Synonyms: "Deeplink" = "deep link"
* Do not confuse: "Open app" ≠ "Deeplink" ≠ "Web URL" (three distinct on-click behaviors)
* Do not confuse: "Notification group" (iOS only) ≠ "Notification channel" (Android only)
* Do not confuse: "Add content-availability flag" (wakes the app) ≠ "Add mutable-content flag" (allows content modification / media rendering)

**FAQ:**

* **Q: What happens when a recipient taps the push body?** — The configured on-click behavior runs: Open app, Deeplink, or Web URL.
* **Q: How many buttons can I add on Android?** — Up to three.
* **Q: Can I send a silent notification on Web?** — No, Web push notifications do not support the Silent Notification feature.
* **Q: Why aren't my iOS media attachments rendering?** — The Add mutable-content flag must be enabled and your app must implement a Notification Service Extension to download and process the media.
* **Q: How can I personalize which content is shown?** — Use Decisioning, which selects the best content using Priority Scores, Formulas, or AI Models.
* **Q: What is the difference between iOS and Android expiration?** — On iOS, Push expiration is a hard stop (undelivered after expiry); on Android, Time to live is a delivery window converted by FCM, so messages may be sent later than expected.

+++

<!-- ai-section-version: 1 | source-hash: 7f203b9e -->
