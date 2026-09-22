---
title: AI Knowledge Reference
---
# AI Knowledge Reference

+++ AI Knowledge Reference

This section contains structured knowledge intended to support interpretation, retrieval, and question answering related to this topic.

For complete understanding, this information should be combined with the documentation on this page. Neither source is intended to stand alone; the page describes the feature, while this section provides additional context that helps disambiguate terminology, intent, applicability, and constraints.

* **TL;DR:** This page explains how to configure and manage all global settings for a journey, including entrance rules, timezones, start/end dates, timeout behavior, exit criteria, payload size, and conflict management.

**Intents:**

* Configure journey entrance and reentrance rules for profiles
* Set start and end dates to control when profiles can enter or exit a journey
* Define exit criteria to automatically remove profiles when a business condition is met
* Manage access to a journey using object-level access control labels
* Monitor journey payload size to prevent publish failures
* Resolve conflicts and assign priority scores across journeys and campaigns

**Glossary:**

* **Journey properties**: The global settings panel (right rail) that controls name, entrance rules, timezone, dates, timeout, payload size, and conflict management for a journey. *(product-specific)*
* **Reentrance wait period**: The minimum time a profile must wait before being allowed to re-enter a unitary journey; maximum is 90 days. *(product-specific)*
* **Global journey timeout (TTL)**: The maximum duration a profile can remain active within a journey — currently 91 days, after which the profile is exited and its data deleted. *(product-specific)*
* **Exit criteria**: Rules defined at the journey level that automatically remove profiles from a journey when a specified event occurs or an audience condition is met. *(product-specific)*
* **Profile Attribute–Based Exit Criteria**: Exit rules based on profile attributes (e.g., location, status) that are evaluated at action steps and are only editable when a journey is paused. *(product-specific)*
* **Merge policy**: The rule set used by Adobe Experience Platform to combine profile data from multiple sources; applied consistently throughout the entire journey. *(product-specific)*
* **Conflict management**: Tools in journey properties for assigning priority scores, applying rule sets, and identifying overlapping journeys or campaigns. *(product-specific)*
* **Journey payload size**: The current size of the serialized journey definition (activities, expressions, conditions, data mappings, parameters, actions) compared to the configured limit; it is not determined by activity count alone, and exceeding the limit blocks publication. *(product-specific)*
* **OLAC (Object Level Access Control)**: A permission model that restricts access to individual journeys using data usage labels.
* **Holdout group (journey-level) (Limited Availability)**: Configured in the **Measure journey lift with a holdout group** section of journey properties; lets you exclude a percentage of your audience from the journey to measure its incremental effectiveness. *(product-specific)*
* **Holdout group**: A percentage of the target audience excluded from entering a journey, used as a baseline to measure the journey's incremental effectiveness. Profiles in the holdout group are tracked via exclusion events. *(product-specific)*
* **Incremental lift**: The measurable difference in outcome between profiles who entered the journey (active group) and profiles who did not (holdout group), used to quantify the journey's true impact.

**Guardrails:**

* Reentrance wait period maximum is 90 days
* Global journey timeout is 91 days; after this period, profile data is deleted and the profile is exited
* Journey payload default limit is 2 MB (2,000,000 bytes); the size reflects the saved configuration of the journey's activities and is not calculated from activity count alone; a warning appears at 90% of the limit and publication is blocked at 100% or more — contact your Adobe representative for a higher limit
* Exit criteria are only configurable in draft state (event/audience types); Profile Attribute exit criteria are only editable when the journey is paused
* Only one Profile Attribute exit criteria rule is allowed per journey
* Profile Attribute exit criteria are evaluated at action steps only, not globally
* When an audience merge policy is updated, any active journey referencing that audience must be republished
* Inconsistent merge policies in a journey block publication; inconsistencies in message personalization do not raise an alert
* For live journeys, the properties panel shows only the publication date and publisher name
* Holdout: minimum 5% of audience and 1,000 profiles recommended for statistical significance
* Holdout: open and click metrics are not meaningful — use bottom-of-funnel conversion metrics instead
* Holdout: only one success metric per journey; cross-journey holdout is not supported here
* Holdout percentage changes in a new journey version apply to new entrants only

**Terminology:**

* **Canonical name:** Journey properties — Acronym: none — variants: journey settings, journey configuration panel
* **Synonyms:** "global journey timeout" = "TTL" = "Time-to-Live"
* **Do not confuse:** "global journey timeout (91 days)" ≠ "reporting window (~91 days)" — the timeout limits individual profile duration in a journey; the reporting window is a UI display limit for analytics data

**FAQ:**

* **Q: How long can a profile stay in a journey?** — A maximum of 91 days (the global journey timeout); after this period, the profile is automatically exited and its data deleted.
* **Q: Can I edit journey properties while the journey is live?** — For live journeys, the properties panel shows only the publication date and publisher name; structural changes require a new version.
* **Q: What happens when multiple exit criteria are configured?** — They are evaluated from top to bottom with OR logic at every step of the journey; a profile exits when any one criterion is met.
* **Q: How do I prevent a profile from re-entering a journey?** — Uncheck the "Allow reentrance" option in journey properties; this is suitable for one-time experiences such as a gift offer.
* **Q: What is the difference between journey timeout and end date?** — The end date stops all new entries and automatically exits active profiles on that specific date; the 91-day global timeout applies per profile from the moment they enter, regardless of the journey's end date.
* **Q: How is the merge policy determined for a journey?** — It depends on the journey type: Read Audience and Audience Qualification journeys use the audience's merge policy; Unitary event journeys use the default merge policy; Business event journeys use the merge policy from the targeted audience in the subsequent Read Audience activity.
* **Q: How does the holdout group work?** — The holdout group is a configurable percentage of your target audience excluded from entering the journey. Assignment is deterministic (the same profile always maps to holdout for the same journey) and evaluated at entry time. Holdout profiles do not receive any communication but are tracked via exclusion events in the dataset for downstream CJA lift reporting. See [Measure journey lift with a holdout group](#performance-management).

+++
