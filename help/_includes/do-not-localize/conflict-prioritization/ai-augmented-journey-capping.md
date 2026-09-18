---
title: AI Knowledge Reference
---
# AI Knowledge Reference

+++ AI Knowledge Reference

This section contains structured knowledge intended to support interpretation, retrieval, and question answering related to this topic.

For complete understanding, this information should be combined with the documentation on this page. Neither source is intended to stand alone; the page describes the feature, while this section provides additional context that helps disambiguate terminology, intent, applicability, and constraints.

* **TL;DR:** This page explains how to create journey capping rules—entry capping and concurrency capping—inside a journey-domain rule set, and how they use priority scores to arbitrate which journeys a profile enters.

**Intents:**

* Create a [!UICONTROL Journey Entry Cap] to limit journey entries over a period
* Create a [!UICONTROL Journey Concurrency Cap] to limit simultaneous journey enrollments
* Use [!UICONTROL Prioritization look ahead] to arbitrate entries based on priority scores over a chosen period
* Apply a journey rule set to a journey through the [!UICONTROL Capping rules] drop-down
* Monitor exclusions in the [!UICONTROL Journey Exclusions] table and with Query Service

**Glossary:**

* **Entry capping**: Limits the number of journey entries over a given period for a profile *(product-specific)*
* **Concurrency capping**: Limits how many journeys a profile can be enrolled in simultaneously *(product-specific)*
* **[!UICONTROL Prioritization look ahead]**: Field that arbitrates journey entries based on priority scores over a chosen period, scanning upcoming scheduled Read-Audience journeys *(product-specific)*
* **Arbitration**: Using priority scores to decide which journeys a profile enters when caps apply *(product-specific)*
* **[!UICONTROL Capping]**: Field setting the maximum number of journeys a profile can enter or be enrolled in simultaneously *(product-specific)*
* **CAP_REACHED / LOWER_PRIORITY**: Discard sub-reasons that identify why a profile did not enter a journey *(product-specific)*

**Guardrails:**

* Journey capping rules can only be added to rule sets with the "journey" domain.
* Both entry capping and concurrency capping leverage priority scores to arbitrate entries.
* Durations are based on the UTC time zone (for example, a Daily cap resets at midnight UTC).
* For entry capping, the system takes into account the priority of upcoming scheduled journeys that have the same rule applied, and can suppress a profile from a lower-priority journey when a higher-priority one is scheduled.
* If a journey is activated immediately, it can take up to 10 minutes for the system to begin suppressing customers; a message displays if you try to publish with a start time less than 10 minutes away.
* Providing a priority score of 100 to a journey ensures that it is entered into.

**Terminology:**

* Canonical name: journey capping — Acronym: n/a — variants: journey capping & arbitration, journey rule set
* Synonyms: none
* Do not confuse: "[!UICONTROL Journey Entry Cap]" (entries over a period) ≠ "[!UICONTROL Journey Concurrency Cap]" (simultaneous enrollments)
* Do not confuse: "journey capping" (limits journey entries or concurrency) ≠ "channel capping" (limits messages per channel and communication type)
* Do not confuse: "CAP_REACHED" (a cap was reached) ≠ "LOWER_PRIORITY" (excluded due to a lower priority)

**FAQ:**

* **Q: What is the difference between entry and concurrency capping?** — Entry capping limits journey entries over a period; concurrency capping limits how many journeys a profile is enrolled in simultaneously.
* **Q: How are entries arbitrated when a cap is reached?** — By priority scores; the [!UICONTROL Prioritization look ahead] scans upcoming scheduled Read-Audience journeys to suppress entry when a higher-priority journey is coming up.
* **Q: How can I guarantee a journey is entered?** — Give it a priority score of 100.
* **Q: Why can suppression be delayed after activation?** — If a journey is activated immediately, it can take up to 10 minutes for the system to begin suppressing customers.
* **Q: How do I find why a profile did not enter a journey?** — Check the [!UICONTROL Journey Exclusions] table in the journey report, or query the discard sub-reason (CAP_REACHED or LOWER_PRIORITY).

+++

<!-- ai-section-version: 1 | source-hash: 42708cf1 -->
