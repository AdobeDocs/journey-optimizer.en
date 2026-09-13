---
title: AI Knowledge Reference
---
# AI Knowledge Reference

+++ AI Knowledge Reference

This section contains structured knowledge intended to support interpretation, retrieval, and question answering related to this topic.

For complete understanding, this information should be combined with the documentation on this page. Neither source is intended to stand alone; the page describes the feature, while this section provides additional context that helps disambiguate terminology, intent, applicability, and constraints.

* **TL;DR:** This page answers common questions about Live activities across general, developer, marketer, API, and troubleshooting topics for iOS apps and Journey Optimizer campaigns.

**Intents:**

* Understand how a Live activity differs from a push notification and which iOS versions support it
* Learn the concurrency, duration, and rate limits that apply to Live activities
* Understand developer requirements such as the widget extension, attribute registration, and token handling
* Understand API payload behavior for `timestamp`, `dismissal-date`, `requestId`, and `x-request-id`
* Learn marketer options for personalization, A/B testing, and update frequency, plus troubleshooting basics

**Glossary:**

* **`liveActivityID`**: The identifier used for individual (unitary) Live activity targeted at specific users; each ID represents a unique instance *(product-specific)*
* **`channelID`**: The identifier used for broadcast Live activity sent to audiences; all users on the channel receive the same updates *(product-specific)*
* **`Activity.id`**: The unique ID of each Live activity instance, used to update or end it individually
* **`x-request-id`**: A header that, when paired one-to-one with a `liveActivityID`, ensures duplicate requests start only one Live activity instance *(product-specific)*
* **`requestId`**: A unique identifier per API request used for idempotency and tracking
* **`NSSupportsLiveActivitiesFrequentUpdates`**: An `Info.plist` key set to YES when frequent updates are needed
* **priority: 5 / priority: 10**: Standard and high-priority Live activity updates

**Guardrails:**

* Apple limits a Live activity to 8 hours of active updates (hard limit), after which the system automatically ends the activity; it may remain visible in a static state for up to 12 additional hours before removal.
* iOS typically supports up to about five concurrent Live activity instances per app (iOS system-level limit); there is no hard limit imposed by developers on how many instances of a given attribute type can exist.
* Campaigns have a default rate limit of 500 transactional messages per second across all channels combined (default), including iOS Live activities; there is no separate rate limit specifically for iOS Live activities.
* Remote starts via `ActivityKit` are subject to system-enforced limits; after about 5 consecutive start attempts, subsequent requests begin failing until a brief cooldown period passes.
* Apple does not specify an exact numerical cap for high-priority (priority: 10) updates; the system maintains a dynamic internal budget and may throttle or delay subsequent updates.
* iOS version support: 16.1+ for basic Live activities, 17.2+ for push-to-start, 18+ for broadcast channel support.
* Each API request should have a unique `requestId`; epoch timestamps must be in Unix seconds, not milliseconds.

**Terminology:**

* Canonical name: Live activity — Acronym: n/a — variants: Live activities
* Synonyms: "unitary" = "individual (transactional)"
* Synonyms: "broadcast" = "audience-based"
* Do not confuse: "`liveActivityID`" (individual/unitary, per user) ≠ "`channelID`" (broadcast, per audience)
* Do not confuse: "`timestamp`" (current epoch time, required for all events) ≠ "`dismissal-date`" (future epoch time, required only for end events)
* Do not confuse: "priority: 5" (standard updates) ≠ "priority: 10" (high-priority updates)
* Do not confuse: "`requestId`" (unique identifier per API request for tracking) ≠ "`x-request-id`" (header paired with a `liveActivityID` to prevent duplicate starts)

**FAQ:**

* **Q: How long can a Live activity remain active?** — Apple limits it to 8 hours of active updates; afterward the system automatically ends it, though it may remain visible in a static state for up to 12 additional hours before removal. You can end it sooner by setting a `dismissalDate` or calling `activity.end()`.
* **Q: How many Live activity instances can be active at once?** — There is no hard limit imposed by developers, but iOS enforces a system-level limit and typically supports up to about five concurrent instances per app, and may stop displaying or terminate older ones beyond that.
* **Q: What are the rate limits?** — A default rate limit of 500 transactional messages per second across all channels combined, including iOS Live activities; there is no separate rate limit specifically for iOS Live activities.
* **Q: Do users need the app open to receive updates?** — No; a Live activity can be started, updated, and ended remotely even when the app is completely closed.
* **Q: Can I test Live activities in the iOS Simulator?** — Yes, both locally-started and remotely-started Live activities can be tested in the iOS Simulator.
* **Q: What format should epoch timestamps use?** — Unix epoch time in seconds, not milliseconds.

+++

<!-- ai-section-version: 1 | source-hash: d8ec3986 -->
