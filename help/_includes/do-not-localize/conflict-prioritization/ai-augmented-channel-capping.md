---
title: AI Knowledge Reference
---
# AI Knowledge Reference

+++ AI Knowledge Reference

This section contains structured knowledge intended to support interpretation, retrieval, and question answering related to this topic.

For complete understanding, this information should be combined with the documentation on this page. Neither source is intended to stand alone; the page describes the feature, while this section provides additional context that helps disambiguate terminology, intent, applicability, and constraints.

* **TL;DR:** This page explains how to create channel rule sets that apply frequency capping rules by channel and communication type, limiting how many messages a profile receives per hour, day, week, or month, and how to apply them to journey and campaign messages.

**Intents:**

* Create a channel capping rule inside a channel-domain rule set
* Set a [!UICONTROL Capping count] and a [!UICONTROL Reset capping frequency] (hourly, daily, weekly, or monthly)
* Apply capping across several channels as a single total count
* Apply an activated rule set to a journey or campaign message with [!UICONTROL Add Business Rule]
* Understand how and when frequency counters reset and update
* Test frequency rules and view profiles excluded from delivery in reporting

**Glossary:**

* **Channel rule set**: A rule set whose [!UICONTROL Domain] is "channel"; it applies capping rules to communication channels *(product-specific)*
* **Capping rule**: A rule defining the maximum number of messages sent to a profile for the selected period *(product-specific)*
* **[!UICONTROL Capping count]**: Field setting the maximum number of messages that can be sent to an individual user profile each month, week, day, or hour *(product-specific)*
* **[!UICONTROL Reset capping frequency]**: Drop-down that selects whether the capping is applied hourly, daily, weekly, or monthly, reset at the beginning of the corresponding time frame *(product-specific)*
* **[!UICONTROL Every]**: Field that repeats the frequency capping rule over multiple hours, days, weeks, or months *(product-specific)*
* **Communication type**: A category of message (for example promotional communications, newsletters) that a rule set can be built to limit *(product-specific)*
* **[!UICONTROL Category]**: Field specifying the message category the rule applies to; read-only, with only [!UICONTROL Marketing] available *(product-specific)*

**Guardrails:**

* You can create up to 10 active local rule sets for each channel domain and for the journey domain (hard limit).
* The [!UICONTROL Every] field value must match the selected duration type: 1-23 for Hourly, 1-30 for Daily, 1-4 for Weekly, and 1-3 for Monthly.
* The [!UICONTROL Category] field is read-only, as only the [!UICONTROL Marketing] category is available.
* Selecting several channels applies capping across all selected channels as a total count.
* Frequency caps reset on calendar periods in UTC: hourly resets at the end of each UTC hour, daily until 23:59:59 UTC, weekly until Saturday 23:59:59 UTC, and monthly until the last day of the month 23:59:59 UTC.
* Before activating, schedule the journey or campaign execution at least 10 minutes into the future so counter values populate; activating immediately can prevent capping from working correctly for journeys, campaigns, and API-triggered campaigns.
* The profile counter value updates once the communication is delivered; spacing communications at least two hours apart is recommended so the counter can update.
* Frequency capping rules also apply when sending proofs; if a test profile has reached the cap, proofs show as finished but no email is delivered.
* Once a profile's frequency cap is reached, there is no way to reset the counter until the next period; deactivating a rule lets capped profiles receive messages but does not remove or delete counter increments.
* To ensure channel-level capping works correctly, choose the highest priority namespace while authoring a campaign or journey.

**Terminology:**

* Canonical name: channel capping — Acronym: n/a — variants: frequency capping by channel and communication type, channel rule set, frequency capping rules
* Synonyms: "channel rule set" = a rule set with the "channel" value in the [!UICONTROL Domain] column
* Do not confuse: "channel capping" (limits messages per channel and communication type) ≠ "journey capping" (limits journey entries or concurrency)
* Do not confuse: "rule set" (a group of rules) ≠ "capping rule" (a single rule inside a rule set)
* Do not confuse: "[!UICONTROL Reset capping frequency]" (the period unit: hourly, daily, weekly, or monthly) ≠ "[!UICONTROL Every]" (how many of those periods the rule spans)

**FAQ:**

* **Q: How many channel messages can a profile receive?** — Whatever you set in the [!UICONTROL Capping count] for the selected [!UICONTROL Reset capping frequency]; if several channels are selected, the count is shared as a total across those channels.
* **Q: When do frequency counters reset?** — At the start of the next calendar period in UTC (hourly, daily until 23:59:59 UTC, weekly until Saturday 23:59:59 UTC, or monthly until the last day of the month 23:59:59 UTC).
* **Q: Can I reset a profile's counter once its cap is reached?** — No, there is no way to reset the counter until the next period; deactivating a rule lets capped profiles receive messages but does not remove counter increments.
* **Q: Why did my immediately activated campaign not respect capping?** — Counter values need time to populate; schedule execution at least 10 minutes into the future.
* **Q: Do frequency caps apply to proofs?** — Yes; if a test profile has reached the cap, the proof shows as finished but no email is delivered.
* **Q: Where can I see profiles excluded by frequency rules?** — In the Customer Journey Analytics report and the Live report, where frequency rules are listed as a reason for exclusion.

+++

<!-- ai-section-version: 1 | source-hash: d2f03534 -->
