---
title: AI Knowledge Reference
---
# AI Knowledge Reference

+++ AI Knowledge Reference

This section contains structured knowledge intended to support interpretation, retrieval, and question answering related to this topic.

For complete understanding, this information should be combined with the documentation on this page. Neither source is intended to stand alone; the page describes the feature, while this section provides additional context that helps disambiguate terminology, intent, applicability, and constraints.

* **TL;DR:** This page explains the prerequisites and configuration required to send In-app messages with Journey Optimizer, including delivery prerequisites, creating an In-app channel configuration, and reporting prerequisites.

**Intents:**

* Complete the configuration steps required before sending In-app messages
* Set up the delivery prerequisites in Adobe Experience Platform Data Collection and Profile merge policies
* Create an In-app channel configuration under Channels > General settings > Channel configurations
* Configure per-platform targeting (Web, iOS, Android) for the channel configuration
* Enable reporting for the In-app channel by aligning datasets and field groups

**Glossary:**

* **In-app channel configuration**: A channel configuration created in Journey Optimizer that you select when creating an In-app message *(product-specific)*
* **Active-On-Edge Merge Policy**: A merge policy option that must be enabled on the default merge policy so inbound channels can activate and publish inbound campaigns on the edge *(product-specific)*
* **Journey Inbound dataset**: The dataset that must be added within a custom Dataset preference merge policy *(product-specific)*
* **Edge Delivery view**: A view within Adobe Experience Platform Assurance used to troubleshoot delivery of mobile experiences by inspecting request calls, profile data, identity maps, segment memberships, consent settings, and qualified activities *(product-specific)*
* **Marketing action**: A selection that associates consent policies with messages using the configuration, so customer preferences are respected *(product-specific)*
* **Pages matching rule**: A Web app configuration option that targets multiple URLs following the same pattern using Domain and Page criteria *(product-specific)*
* **Time-To-Live (TTL)**: A setting for automatic profile deletion to manage engageable profile count and associated costs when targeting pseudonymous profiles *(product-specific)*

**Guardrails:**

* You must have the correct permissions on Journey Optimizer campaigns before starting, even if you plan to use In-app messages only in journeys; campaign permissions are still required.
* The datastream must have the Adobe Experience Platform Edge and Adobe Journey Optimizer option enabled so inbound events are handled by the Adobe Experience Platform Edge.
* The default merge policy must have the Active-On-Edge Merge Policy option enabled.
* When using a custom Dataset preference merge policy, you must add the Journey Inbound dataset within that merge policy.
* The use of `context.datastream` attributes is supported only for Web channel campaigns; using `context.datastream` in In-app messages results in validation errors such as `Invalid syntax Missing schema field: 'datastream`.
* Configuration names must begin with a letter (A-Z) and can only contain alpha-numeric characters, and may also use underscore, dot, and hyphen characters.
* For iOS and Android platforms, delivery is based solely on the app ID; if both apps share the same app ID, content is delivered to both regardless of the platform selected, and restricting delivery to a specific platform requires device-specific rules within your journey or campaign logic.
* For reporting, the dataset used in your In-app implementation datastream must be included in your reporting configuration; a dataset not present in your app datastream will not display app data in reports.
* If you are not using the `AEP Web SDK ExperienceEvent` and `Consumer Experience Event` field groups, you must add the `Experience Event - Proposition Interactions`, `Application Details`, `Commerce Details`, and `Web Details` field groups.
* When targeting pseudonymous (unauthenticated) profiles, consider setting a Time-To-Live (TTL) for automatic profile deletion to manage engageable profile count and costs (recommended).

**Terminology:**

* Canonical name: In-app channel configuration — Acronym: n/a — variants: In-app message channel configuration, In-app configuration
* Synonyms: "pseudonymous profiles" = "unauthenticated visitors"
* Do not confuse: "Delivery prerequisites" (datastream and merge policy setup) ≠ "Reporting prerequisites" (datasets and field groups for reporting)
* Do not confuse: "Page URL" (target a specific page) ≠ "Pages matching rule" (target multiple URLs following the same pattern)

**FAQ:**

* **Q: What permissions do I need before configuring In-app?** — You need the correct permissions on Journey Optimizer campaigns, even if you plan to use In-app messages only in journeys, because campaign permissions are still required.
* **Q: Can I use `context.datastream` in In-app messages?** — No; it is supported only for Web channel campaigns, and using it in In-app messages produces validation errors such as `Invalid syntax Missing schema field: 'datastream`.
* **Q: Where do I create an In-app channel configuration?** — Under Channels > General settings > Channel configurations, using Create channel configuration.
* **Q: How is delivery handled for iOS and Android?** — Delivery is based solely on the app ID; if both apps share the same app ID, content is delivered to both regardless of the platform selected, unless you add device-specific rules in your journey or campaign logic.
* **Q: Why is my In-app data not showing in reports?** — The dataset used in your In-app implementation must be included in your reporting configuration; a dataset not present in your app datastream will not display app data in reports.

+++

<!-- ai-section-version: 1 | source-hash: b9dc8b75 -->
