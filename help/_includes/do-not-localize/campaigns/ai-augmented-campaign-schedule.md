---
title: AI Knowledge Reference
---
# AI Knowledge Reference

+++ AI Knowledge Reference

This section contains structured knowledge intended to support interpretation, retrieval, and question answering related to this topic.

For complete understanding, this information should be combined with the documentation on this page. Neither source is intended to stand alone; the page describes the feature, while this section provides additional context that helps disambiguate terminology, intent, applicability, and constraints.

* **TL;DR:** This page explains how to schedule an Action campaign in the **Schedule** tab: start and end dates, recipient local time delivery, execution frequency, rate control, and wave sending.

**Intents:**

* Set a start date and time with **Campaign start**
* Send messages at each recipient's local time with **Use profile timezone**
* Set a daily, weekly, or monthly execution frequency
* Set an end date with **Campaign end**
* Set rate control with **Throttle delivery**
* Deliver the message in batches over time using waves

**Glossary:**

* **Profile timezone**: The `profile.timeZone` field of each recipient's Adobe Experience Platform profile, used to determine their local timezone. *(product-specific)*
* **Rate control**: Limits the delivery rate for outbound actions to prevent overload on downstream systems. *(product-specific)*
* **Delivery rate**: The rate per second set when **Throttle delivery** is enabled in **Delivery settings**. *(product-specific)*
* **Waves**: Batches in which the campaign message is delivered over time; you define the number of waves, their size (by percentage or absolute number), and the schedule for each wave. *(product-specific)*
* **IP warmup plan activation campaign**: A campaign for email actions whose schedule is driven by the IP warmup plan it is associated with. *(product-specific)*

**Guardrails:**

* By default, Action campaigns start once they are activated manually, and end as soon as the message has been sent once.
* Outside of the dates specified in **Campaign start** and **Campaign end**, the campaign is not executed.
* For recurring campaigns, if the initial scheduled time has already passed, the campaigns roll over to the next available time slot according to their recurrence rules.
* **Use profile timezone** is available for these outbound channels only: Email, Push, Mobile message, WhatsApp, and LINE.
* If a profile does not have a timezone value, the timezone in which the campaign was created is used as the fallback.
* Time zone identifiers: `profile.timeZone` can be IANA naming or UTC offsets. IANA naming is the preferred format, as it automatically adjusts for daylight-saving rules. IANA identifiers are case-sensitive and must match the official IANA naming.
* Execution frequency (daily, weekly, or monthly) is available for Email, Mobile message, and Push notification actions.
* Delivery rate: minimum 1 per second (hard limit); maximum 2000 per second (hard limit) when the **Throttle delivery** option is enabled. Rate control is available for outbound actions (Email, Mobile messages, Push notifications).
* When a delivery rate is set, the maximum timeframe for which the campaign audience can execute is 12 hours (hard limit). If the delivery rate does not allow all the audience to be sent the message in the 12 hour timeframe, the remaining profiles are excluded from the campaign. The count of excluded profiles is visible in the campaign report.

**Terminology:**

* Canonical name: Action campaign schedule — variants: campaign schedule
* Synonyms: "Send at recipient's local time" = "Use profile timezone" (section title and option name)
* Do not confuse: "Live" (status while messages are being delivered across all timezones) ≠ "Completed" (status once all timezones have been processed)

**FAQ:**

* **Q: When does an Action campaign start and end by default?** — It starts once it is activated manually, and ends as soon as the message has been sent once.
* **Q: How do I send at the same local time for every recipient?** — Specify the date and time in **Campaign start**, then enable **Use profile timezone**. This is available for Email, Push, Mobile message, WhatsApp, and LINE only.
* **Q: What happens if a profile has no timezone value?** — The timezone in which the campaign was created is used as the fallback.
* **Q: What are the campaign statuses during profile timezone delivery?** — The campaign remains in **Live** status while messages are being delivered across all timezones; when all timezones have been processed, the status changes to **Completed**.
* **Q: Which delivery rates can I set?** — From 1 to 2000 per second when **Throttle delivery** is enabled.
* **Q: Why were some profiles excluded from my campaign?** — When a delivery rate is set, the maximum timeframe is 12 hours; the remaining profiles are excluded from the campaign if the rate does not allow sending to the whole audience in that timeframe. Their count is in the campaign report.

**Examples:**

* Profile timezone: a campaign scheduled to send at 9 AM using profile timezone reaches recipients in New York (ET) at 9 AM ET and recipients in Los Angeles (PT) at 9 AM PT.
* Rate control: set a rate limit of 165 messages per second to ensure steady delivery without overwhelming downstream systems.

**Related pages:**

* IP warmup campaigns: Learn how to create IP warmup campaigns (configuration/ip-warmup-campaign.md)
* IANA identifiers: IANA Time Zone Database (external, https://www.iana.org/time-zones)
* Waves: Learn how to send using waves (delivery/send-using-waves.md)
* Next step, activation: Review and activate an Action campaign (campaigns/review-activate-campaign.md)

+++

<!-- ai-section-version: 1 | source-hash: c2d3e159 -->
