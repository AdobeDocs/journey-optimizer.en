---
title: AI Knowledge Reference
---
# AI Knowledge Reference

+++ AI Knowledge Reference

This section contains structured knowledge intended to support interpretation, retrieval, and question answering related to this topic.

For complete understanding, this information should be combined with the documentation on this page. Neither source is intended to stand alone; the page describes the feature, while this section provides additional context that helps disambiguate terminology, intent, applicability, and constraints.

* **TL;DR:** This page answers common questions about Live activities across general, developer, marketer, API, and troubleshooting topics for iOS and Android apps and Journey Optimizer campaigns.

**Intents:**

* Understand how a Live activity differs from a push notification, and which iOS and Android versions support it
* Learn the concurrency, duration, and rate limits that apply to Live activities
* Understand developer requirements such as the widget extension, attribute registration, and token handling
* Understand API payload behavior for `timestamp`, `dismissal-date`, `requestId`, and `x-request-id`
* Understand how an Android Live Update relates to an iOS Live Activity, including the Android app requirements and the `event_type`, `topic_name`, `notification_id`, and `notification_channel_id` fields
* Learn marketer options for personalization, A/B testing, and update frequency, plus troubleshooting basics

**Glossary:**

* **`liveActivityID`**: The identifier used for individual (unitary) Live activity targeted at specific users; each ID represents a unique instance *(product-specific)*
* **`channelID`**: The identifier used for broadcast Live activity sent to audiences; all users on the channel receive the same updates *(product-specific)*
* **`Activity.id`**: The unique ID of each Live activity instance, used to update or end it individually
* **`x-request-id`**: A header that, when paired one-to-one with a `liveActivityID`, ensures duplicate requests start only one Live activity instance *(product-specific)*
* **`requestId`**: For an Android Live Update, a value that must be unique per new Android Live Update and that ties `update`/`end` requests back to the running Android Live Update
* **`NSSupportsLiveActivitiesFrequentUpdates`**: An `Info.plist` key set to YES when frequent updates are needed
* **priority: 5 / priority: 10**: Standard and high-priority Live activity updates (iOS)
* **Android Live Update**: The Android counterpart of an iOS Live Activity; the page describes it as the same product concept in Journey Optimizer, using the same Headless API and campaign model, implemented as a promoted ongoing notification *(product-specific)*
* **`event_type`**: The Android payload field that drives the lifecycle with the values `start`, `update`, and `end`; the Android analog of the iOS event field
* **`topic_name`**: The broadcast channel that devices subscribe to; mandatory for broadcast `update`/`end`
* **`notification_id`**: Correlates the ongoing notification on the device
* **`notification_channel_id`**: The Android notification channel your app posts on

**Guardrails:**

* iOS: Apple limits a Live activity to 8 hours of active updates (hard limit), after which the system automatically ends the activity; it may remain visible in a static state for up to 12 additional hours before removal. Android: there is no fixed 8-hour expiry; an ongoing notification stays active until your app sends an end event or the app or user dismisses it.
* iOS typically supports up to about five concurrent Live activity instances per app; iOS enforces a system-level cap on how many can be active or visible at once, and there is no developer-imposed limit. Android has no equivalent instance cap.
* Campaigns have a default rate limit of 500 transactional messages per second across all channels combined (default), including iOS Live activities; there is no separate rate limit specifically for iOS Live activities.
* Remote starts via `ActivityKit` are subject to system-enforced limits; after about 5 consecutive start attempts, subsequent requests begin failing until a brief cooldown period passes.
* Apple does not specify an exact numerical cap for high-priority (priority: 10) updates; the system maintains a dynamic internal budget and may throttle or delay subsequent updates.
* iOS version support: 16.1+ for basic Live activities, 17.2+ for push-to-start, 18+ for broadcast channel support.
* Native Android Live Updates require Android 16; on earlier Android versions the same campaign falls back to a standard ongoing notification. A Mobile SDK version that supports Android Live Update handling is needed.
* Android app requirements: the app must target API level 36; the Android manifest must declare the `POST_PROMOTED_NOTIFICATION` permission; the notification must use one of the styles Standard, BigTextStyle, CallStyle, ProgressStyle, or MetricStyle (Android 37).
* A Live Update channel configuration targets a single platform, so iOS and Android are set up as separate campaigns, each with its own channel configuration, for both unitary and broadcast.
* Broadcast Android Live Updates are supported only for marketing campaigns; unitary supports transactional use cases.
* Android Live Updates are delivered through Firebase Cloud Messaging, which caps each message at roughly 4 KB.
* Epoch timestamps must be in Unix seconds, not milliseconds.

**Terminology:**

* Canonical name: Live activity — Acronym: n/a — variants: Live activities
* Synonyms: "unitary" = "individual"
* Synonyms: "broadcast" = "audience-based"
* Do not confuse: "`liveActivityID`" (individual/unitary, per user) ≠ "`channelID`" (broadcast, per audience)
* Do not confuse: "`timestamp`" (iOS: current epoch time, required for all events) ≠ "`dismissal-date`" (iOS: future epoch time when the Live activity should auto-dismiss, required only for end events); Android does not use `timestamp` or `dismissal-date`
* Do not confuse: "priority: 5" (standard updates) ≠ "priority: 10" (high-priority updates)
* Do not confuse: "`requestId`" (ties `update`/`end` requests to the running Android Live Update) ≠ "`x-request-id`" (header paired with a `liveActivityID` to prevent duplicate starts)

**FAQ:**

* **Q: How long can a Live activity remain active?** — Apple limits it to 8 hours of active updates; afterward the system automatically ends it, though it may remain visible in a static state for up to 12 additional hours before removal. You can end it sooner by setting a `dismissalDate` or calling `activity.end()`.
* **Q: How many Live activity instances can be active at once?** — There is no hard limit imposed by developers, but iOS enforces a system-level limit and typically supports up to about five concurrent instances per app, and may stop displaying or terminate older ones beyond that.
* **Q: What are the rate limits?** — A default rate limit of 500 transactional messages per second across all channels combined, including iOS Live activities; there is no separate rate limit specifically for iOS Live activities.
* **Q: Do users need the app open to receive updates?** — No; start, update, and end are delivered remotely and work with the app in the background or closed.
* **Q: Can I test Live activities in the iOS Simulator?** — Yes, both locally-started and remotely-started Live activities can be tested in the iOS Simulator.
* **Q: Can a single campaign target both iOS and Android?** — No; a Live Update channel configuration targets a single platform, so you create one campaign for iOS and one for Android.
* **Q: What format should epoch timestamps use?** — Unix epoch time in seconds, not milliseconds.

+++

<!-- ai-section-version: 1 | source-hash: b24807ba -->
