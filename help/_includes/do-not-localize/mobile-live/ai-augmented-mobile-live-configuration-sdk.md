---
title: AI Knowledge Reference
---
# AI Knowledge Reference

+++ AI Knowledge Reference

This section contains structured knowledge intended to support interpretation, retrieval, and question answering related to this topic.

For complete understanding, this information should be combined with the documentation on this page. Neither source is intended to stand alone; the page describes the feature, while this section provides additional context that helps disambiguate terminology, intent, applicability, and constraints.

* **TL;DR:** This page explains how to integrate the Adobe Experience Platform Mobile SDK into an iOS app so it can register, display, and receive real-time Live activity updates on the Lock Screen and Dynamic Island.

**Intents:**

* Import the required modules **[!DNL AEPMessaging]**, **[!DNL AEPMessagingLiveActivity]**, and **[!DNL ActivityKit]**
* Define Live activity attributes conforming to `LiveActivityAttributes`, including `LiveActivityData` and a `ContentState`
* Register Live activity types with `Messaging.registerLiveActivity()` after SDK initialization
* Create a widget configuration (`ActivityConfiguration`) for both the Lock Screen and Dynamic Island
* Optionally start a Live activity locally and add Assurance debug support

**Glossary:**

* **`LiveActivityAttributes`**: The protocol a struct conforms to, defining both the static data and the dynamic content state for a Live activity *(product-specific)*
* **`LiveActivityData`**: A required property containing Adobe Experience Platform-specific data; `liveActivityID` for individual users, `channelID` for broadcast *(product-specific)*
* **`ContentState`**: Dynamic data that can be updated during the Live activity lifecycle; must conform to `Codable` and `Hashable`
* **`LiveActivityOrigin`**: An enumeration specifying whether an activity was initiated locally or remotely via a push-to-start notification, supported in iOS 17.2 and later *(product-specific)*
* **`Messaging.registerLiveActivity()`**: The call used after SDK initialization to register Live activity types *(product-specific)*
* **`ActivityConfiguration`**: The widget configuration implemented for the Lock Screen and Dynamic Island interface
* **`LiveActivityAssuranceDebuggable`**: The protocol implemented to debug Live activity schemas in Adobe Assurance *(product-specific)*

**Guardrails:**

* iOS: 16.1 or later for basic Live activity functionality; 17.2 or later for push-to-start; 18 or later for broadcast channel support (minimum versions).
* Xcode 14.0 or later (minimum version).
* Swift 5.7 or later (minimum version).
* AEP Mobile SDK: iOS Messaging 5.11.0 or later (minimum version).
* Required dependencies: AEPCore, AEPMessaging, AEPMessagingLiveActivity, ActivityKit.
* `liveActivityData` is required and contains Adobe Experience Platform-specific data; `ContentState` must conform to `Codable` and `Hashable`.

**Terminology:**

* Canonical name: Adobe Experience Platform Mobile SDK — Acronym: AEP Mobile SDK — variants: Mobile SDK, messaging SDK
* Synonyms: "push-to-start" = "remotely triggered start, supported in iOS 17.2 and later"
* Do not confuse: "`liveActivityID`" (individual users) ≠ "`channelID`" (broadcast)
* Do not confuse: "start a Live activity locally" (initiated within the application code) ≠ "start remotely via push-to-start" (triggered remotely through Journey Optimizer)

**FAQ:**

* **Q: Which modules must I import?** — **[!DNL AEPMessaging]**, **[!DNL AEPMessagingLiveActivity]**, and **[!DNL ActivityKit]**.
* **Q: What is the minimum iOS version?** — iOS 16.1 or later for basic functionality; iOS 17.2 or later for push-to-start; iOS 18 or later for broadcast channel support.
* **Q: Which AEP Mobile SDK version is required?** — iOS Messaging 5.11.0 or later.
* **Q: How do I register Live activity types?** — Use `Messaging.registerLiveActivity()` in your `AppDelegate` after SDK initialization; you can register multiple Live activity types.
* **Q: Can I start a Live activity without Journey Optimizer?** — Yes, a Live activity can be initiated locally within the application code (optional), in addition to being started remotely through Journey Optimizer.

+++

<!-- ai-section-version: 1 | source-hash: fca7b04d -->
