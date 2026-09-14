---
title: AI Knowledge Reference
---
# AI Knowledge Reference

+++ AI Knowledge Reference

This section contains structured knowledge intended to support interpretation, retrieval, and question answering related to this topic.

For complete understanding, this information should be combined with the documentation on this page. Neither source is intended to stand alone; the page describes the feature, while this section provides additional context that helps disambiguate terminology, intent, applicability, and constraints.

* **TL;DR:** This page explains how Journey Optimizer detects potential conflicts between overlapping live or scheduled journeys and campaigns, how to view them, and how to resolve them.

**Intents:**

* Identify overlapping journeys and campaigns before they go live
* Open the [!UICONTROL Potential conflicts] window with the [!UICONTROL View Potential Conflicts] button
* Monitor overlap across timeline, audience, channel, capping rule set, and channel configuration
* Filter the conflict list to refine the search for overlaps
* Apply resolution tactics such as adjusting dates, refining audiences, adding frequency caps, reducing active journeys, or setting priorities

**Glossary:**

* **Conflict detection tool**: Tool that identifies potential overlaps in journeys and campaigns, such as timelines, audience overlap, and channel configurations *(product-specific)*
* **[!UICONTROL View Potential Conflicts]**: Button in the journey or campaign properties that opens the potential conflicts window *(product-specific)*
* **Unitary journey**: A journey type for which other journeys that start with the same event are displayed as potential conflicts *(product-specific)*
* **Capping Rule Set**: An overlap area that identifies which journey types are capped and whether there is overlap within those *(product-specific)*
* **Channel Configuration**: An overlap area that identifies other journeys or campaigns using the same channel configuration *(product-specific)*

**Guardrails:**

* Conflicts are shown only for live or scheduled campaigns and journeys.
* The [!UICONTROL View Potential Conflicts] button becomes available only after you assign at least one of [!UICONTROL Start / end date], [!UICONTROL Audience], [!UICONTROL Channel], [!UICONTROL Channel configuration], or [!UICONTROL Rule set], and it stays unselectable until changes are saved.
* Newly published journeys and campaigns may take up to 3-7 minutes to appear in the conflict viewer, due to caching.
* For a unitary journey, other journeys that start with the same event are displayed, as that event triggers all such journeys.
* For an Audience qualification or a Read Audience/Business Event journey, all other journeys of the same type with a valid audience are displayed.
* All campaigns potentially conflict with segment-triggered journeys (those starting with a Read audience activity), and live or scheduled campaigns may conflict with one another due to audience overlap.

**Terminology:**

* Canonical name: conflict detection — Acronym: n/a — variants: conflict detection tool, potential conflicts, View Potential Conflicts
* Synonyms: none
* Do not confuse: "conflict detection" (spots overlapping journeys and campaigns) ≠ "priority scores" (decides which communication takes precedence) ≠ "rule sets" (limit how often and how many messages are sent)

**FAQ:**

* **Q: Which journeys and campaigns appear in the conflict viewer?** — Only live or scheduled journeys and campaigns.
* **Q: Why is the [!UICONTROL View Potential Conflicts] button unavailable?** — It becomes available only after you assign at least one of start/end date, audience, channel, channel configuration, or rule set, and after you save.
* **Q: Why does a newly published item not show as a conflict yet?** — Newly published journeys and campaigns can take up to 3-7 minutes to appear, due to caching.
* **Q: How can I reduce identified conflicts?** — Adjust start/end dates, refine audience targeting, implement frequency caps, reduce the number of active journeys, or set priorities on inbound actions.
* **Q: Do campaigns conflict with journeys?** — Campaigns can conflict with segment-triggered journeys that start with a Read audience activity, and live or scheduled campaigns can conflict with one another due to audience overlap.

+++

<!-- ai-section-version: 1 | source-hash: be63a7cf -->
