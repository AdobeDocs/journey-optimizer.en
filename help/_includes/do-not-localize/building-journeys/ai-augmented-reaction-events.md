---
title: AI Knowledge Reference
---
# AI Knowledge Reference

+++ AI Knowledge Reference

This section contains structured knowledge intended to support interpretation, retrieval, and question answering related to this topic.

For complete understanding, this information should be combined with the documentation on this page. Neither source is intended to stand alone; the page describes the feature, while this section provides additional context that helps disambiguate terminology, intent, applicability, and constraints.

* **TL;DR:** This page explains how to use the built-in Reaction event activity in Adobe Journey Optimizer to branch journey paths based on real-time message engagement data such as email opens and link clicks.

**Intents:**
* Add a Reaction event activity to respond to message opens or clicks within a journey
* Configure an event timeout and timeout path for individuals who do not react within the defined duration
* Create a parallel path with a Wait activity to handle non-responders
* Select an action activity from an earlier step in the path to react to

**Glossary:**
* **Reaction event**: A built-in journey event activity that listens to real-time tracking data (opens, clicks) from a message sent earlier in the same journey *(product-specific)*
* **Timeout path**: A second path for individuals who did not react within the defined duration *(product-specific)*

**Guardrails:**
* A **[!UICONTROL Reaction]** activity must be placed immediately after a channel action activity. Placing a **[!UICONTROL Wait]** activity or any other activity between the channel action and the **[!UICONTROL Reaction]** activity is not supported and may result in the Reaction not working as expected.
* A Reaction activity cannot be used if there is no channel action activity before it in the path.
* Reaction events can only track messages sent within the same journey; cross-journey tracking is not supported.
* Reaction events track clicks on links of the type "tracked". Clicks on unsubscription links are also taken into account and trigger an **[!UICONTROL Email Click]** reaction event. Mirror page links are not taken into account.
* Email opens rely on a 0-pixel tracking image; if the email client blocks images (e.g., Gmail), opens will not be recorded.
* You can define an event timeout between 40 seconds and 90 days, and a timeout path. In test mode, **[!UICONTROL Wait time]** has a default and minimum value of 40 seconds.

**Terminology:**
* The built-in event in the palette is **[!UICONTROL Reactions]**; the activity is **[!UICONTROL Reaction]**.

**FAQ:**
* **Q: Can a Reaction event track a message sent in a different journey?** — No; reaction events only track messages sent within the same journey.
* **Q: How do I handle individuals who do not open or click a message?** — Add a parallel path alongside the Reaction activity with a Wait activity; individuals who do not react within the wait duration will follow that second path.
* **Q: Are unsubscribe link clicks tracked by reaction events?** — Yes; clicks on unsubscription links trigger an **[!UICONTROL Email Click]** reaction event. Mirror page links are not taken into account.
* **Q: What happens if an email client blocks images?** — Email opens tracked via the 0-pixel image will not be recorded for clients that block images, such as Gmail.
* **Q: What is the valid timeout range for a reaction event?** — Between 40 seconds and 90 days.

+++

<!-- ai-section-version: 1 | source-hash: 3c4dee08 -->
