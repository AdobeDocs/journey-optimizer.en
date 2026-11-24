---
title: AI Knowledge Reference
---
# AI Knowledge Reference

+++ AI Knowledge Reference

This section contains structured knowledge intended to support interpretation, retrieval, and question answering related to this topic.

For complete understanding, this information should be combined with the documentation on this page. Neither source is intended to stand alone; the page describes the feature, while this section provides additional context that helps disambiguate terminology, intent, applicability, and constraints.

* **TL;DR:** A consolidated reference of which Adobe Journey Optimizer features are available, grouped by capability area, with each feature's lifecycle status (General Availability, Limited Availability, or Beta), the base offer it applies to, and the date it became available.

**Intents:**

* Confirm what you can use during pre-implementation scoping.
* Check the lifecycle status of a feature (General Availability, Limited Availability, or Beta).
* Find which base offer a feature applies to.
* Find the date a feature became available.
* Find out why a capability you read about does not appear in your environment.

**Glossary:**

* **General Availability (GA):** lifecycle status. Released to all environments. Available to any organization whose license includes the capability. Listed as GA: Journey Fragments (June 9, 2026).
* **Limited Availability (LA):** lifecycle status. Released to a restricted set of organizations. Listed as LA: Journey arbitration (February 24, 2026).
* **Beta:** lifecycle status. Early-access release for evaluation. May change before General Availability. May require opting in. Listed as Beta: Generate content for journey expressions (June 3, 2026).
* **Base offer** *(product-specific)*: the page names three Adobe Journey Optimizer base offers. Journey Optimizer – Campaigns is batch, audience-based orchestration. Journey Optimizer – Journeys is real-time, event-driven orchestration. Journey Optimizer – Campaigns & Journeys is both.
* **Applies to** (column): refers to the three base offers.
* **All base offers** (value of Applies to): channel, content, and platform features marked this way are available regardless of base offer.
* **Available since** (column): the date the feature became available. Values appear as a full date (for example May 20, 2026), as a month and year (for example April 2026), as a year (2025), or as Core capability.
* **Core capability** (value of Available since): long-standing, foundational features that have been generally available since before 2026.
* **Notes** (column): any notes about configuration or regional restrictions.
* **Capability area:** features are grouped by capability area. The section Features by capability area has seven tabs: Channels, Journeys, Campaigns, Content & AI, Decisioning, AI agents, and Administration & data. Each tab holds a table with the columns Feature, Status, Applies to, Available since, and Notes.

**Guardrails:**

* A feature being listed on the page does not mean it is enabled in your environment.
* The list is compiled from the 2026 release notes and the current release notes, reflects the latest known status of each feature, and is not exhaustive.
* Sandboxes (GA, All base offers, Core capability): up to 5 sandboxes; additional available.

**Prerequisites and permissions:**

* All Decisioning features require the Decisioning add-on (Decisioning tab).
* Most channel, content, and platform features marked All base offers still require the relevant channel or advanced-capability add-on. The Notes column names the add-on for some features: Email requires the Outbound Delivery add-on and In-app messaging requires the Mobile add-on.

**Applicability:**

* Wave sending of outbound messages (campaigns) applies to Campaigns; Campaigns & Journeys. Status GA, available since February 19, 2026.
* Wave sending of outbound messages (journeys) applies to Journeys; Campaigns & Journeys. Status LA, available since March 16, 2026.
* Direct mail channel in journeys applies to Journeys; Campaigns & Journeys (GA, January 29, 2026). Direct mail channel in orchestrated campaigns applies to Campaigns; Campaigns & Journeys (GA, January 28, 2026).
* Orchestrated campaigns (multi-step workflows) apply to Campaigns; Campaigns & Journeys (GA, Core capability). The Notes column reads "email, SMS, push, direct mail only".

**Terminology:**

* Canonical name: Adobe Journey Optimizer — Acronym: AJO
* Canonical name: General Availability — Acronym: GA
* Canonical name: Limited Availability — Acronym: LA
* Canonical name: Mobile message. The Channels tab lists it as "New Mobile Message channel (SMS, MMS, RCS)" with the note "Unifies SMS/MMS/RCS; native RCS authoring (images, carousels)". SMS, MMS, and RCS are the names given in parentheses next to it.
* Do not confuse:
    * "General Availability (GA)" ≠ "Limited Availability (LA)": two different lifecycle statuses.
    * "Availability" ≠ "entitlement": the page tracks feature lifecycle and availability (whether a capability has shipped and at what maturity), while whether a feature is included in your license depends on your base offer and add-ons.

**FAQ:**

* **Why does a feature that is listed not appear in my environment?** Features in Limited Availability or Beta are not visible to everyone; they roll out to a restricted set of organizations first. If the status is LA or Beta, contact your Adobe representative to request access. A feature being listed on the page does not mean it is enabled in your environment.
* **Is availability the same as being included in my license?** No. The page tracks feature lifecycle and availability (whether a capability has shipped and at what maturity). Whether a feature is included in your license depends on your base offer and add-ons.
* **What does Core capability mean in the Available since column?** Long-standing, foundational features that have been generally available since before 2026.
* **What does All base offers mean in the Applies to column?** Channel, content, and platform features marked All base offers are available regardless of base offer, but most still require the relevant channel or advanced-capability add-on.
* **Where can I find the full history and the newest additions?** The list is not exhaustive. For the full history and the newest additions, always check the release notes.

**Troubleshooting:**

* A capability you read about does not appear in your environment. Cause given: features in Limited Availability or Beta are not visible to everyone, because they roll out to a restricted set of organizations first. What to do: check the status of the feature in the tables; if it is LA or Beta, contact your Adobe representative to request access.

**Related pages:**

* Understand what is in your package, and entitlement details: Packages and capabilities (start/ajo-packages.md)
* See everything that shipped, and the full history and newest additions: Release notes (rn/release-notes.md)
* See everything that shipped: 2026 release notes (rn/release-notes-2026.md)
* Get started: Get started with Journey Optimizer (start/get-started.md)

**Personas:**

* **admin:** Can look up the lifecycle status (GA, LA, or Beta), the base offer, and the add-on named in the Notes column for some features. For example, Email requires the Outbound Delivery add-on, In-app messaging requires the Mobile add-on, and Web channel requires the Web add-on. All Decisioning features require the Decisioning add-on. Sandboxes are listed as GA for All base offers, Core capability, with the note "Up to 5 sandboxes; additional available". The page states that a feature being listed here does not mean it is enabled in your environment. Where: "Features by capability area".
* **marketer:** Can look up the status, the base offer, and the Available since date of each feature. The features are grouped in the tabs Channels, Journeys, Campaigns, Content & AI, Decisioning, AI agents, and Administration & data. For example, Journey Fragments and Journey Simulation are listed as GA, available since June 9, 2026. Generate content for journey expressions is listed as Beta, available since June 3, 2026. The page states that features in Limited Availability or Beta are not visible to everyone. Where: "Features by capability area".

**Onboarding:**

* **Level:** Beginner, Intermediate
* **First minimal step:** Find the feature in the tab of its capability area and read its status, base offer, and Available since date.
* **Success check:** The row of the feature lists its current lifecycle status, the base offer it applies to, the date it became available, and any notes.
* **Next:** To check whether a feature is included in your license, which depends on your base offer and add-ons: Packages and capabilities (start/ajo-packages.md); To see the full history and the newest additions: Release notes (rn/release-notes.md)

+++

<!-- ai-section-version: 1 | source-hash: 495bb2d8 -->
