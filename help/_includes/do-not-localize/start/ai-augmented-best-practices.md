---
title: AI Knowledge Reference
---
# AI Knowledge Reference

+++ AI Knowledge Reference

This section contains structured knowledge intended to support interpretation, retrieval, and question answering related to this topic.

For complete understanding, this information should be combined with the documentation on this page. Neither source is intended to stand alone; the page describes the feature, while this section provides additional context that helps disambiguate terminology, intent, applicability, and constraints.

* **TL;DR:** This page shares Journey Optimizer best practices for real-time identity stitching and omnichannel personalization, and for scaling within journey guardrails such as the activity limit and the live journey limit.

**Intents:**

* Understand how the Identity Service stitches CRMID and ECID identities into a merged profile for real-time personalization
* Choose the right identity and timing when building re-engagement and omnichannel use cases
* Stay within the journey activity guardrail and the live journey guardrail
* Reduce the number of activities in a journey by moving logic into segment definition or audience composition
* Decide when to move single-step engagement from journeys to campaigns

**Glossary:**

* **Identity stitching**: The process by which the Identity Service associates a login identifier (CRMID) with a web or mobile app session identifier (ECID) when a person logs in *(product-specific)*
* **Identity graph**: The set of identities linked to a person across channels, which can contain a person identifier (CRMID) and a web browser identifier (ECID) *(product-specific)*
* **Merged profile**: The '360-degree view' of a person created when the Identity Service stitches identity information together *(product-specific)*
* **CRMID**: An identifier that represents a person *(product-specific)*
* **ECID**: An identifier that represents a web browser *(product-specific)*

**Guardrails:**

* Initial stitching of identities can take 30 minutes to 4 hours to complete after a person logs in.
* After initial stitching, updating the profile with the latest behavioral data can take up to 1 minute to complete.
* For omnichannel engagement, addresses for communication must be available on the profile at the time of engagement; Adobe encourages waiting at least 30 minutes after identity stitching to get the highest volume of profiles.
* Journey Optimizer has a guardrail of 50 activities in a journey canvas, designed to help with readability, QA, and troubleshooting; the activity count appears in the upper left section of the canvas when you come within 10 activities of the limit.
* As you near 100 live journeys at one time in a sandbox, an orange overlay and warning sign appear in the interface as a soft advisory (not a hard cap); to extend beyond 100 live journeys at a time, create a ticket for customer care.

**Terminology:**

* Canonical name: Identity stitching — variants: real-time identity stitching, initial stitching of identities
* Do not confuse: "CRMID" (identifier representing a person) ≠ "ECID" (identifier representing a web browser)
* Do not confuse: "Journeys" (suited when actively listening to user engagement to determine the next step) ≠ "Campaigns" (better suited for single step engagement)

**FAQ:**

* **Q: How long does initial identity stitching take?** — It can take 30 minutes to 4 hours to complete, after which data sent with either identity is associated to the merged profile and available in real time.
* **Q: Which identity should I use to re-engage a visitor 30 minutes after cart abandonment?** — Use the cookie-based identity (ECID), assuming the email address, push token, or other address is associated to the ECID.
* **Q: How do I know when I am close to the activity limit?** — When you come within 10 activities of the 50-activity guardrail, the activity count is displayed in the upper left section of the journey canvas.
* **Q: What happens as I approach 100 live journeys in a sandbox, and how do I go beyond it?** — An orange overlay and warning sign appear in the interface as a soft advisory (not a hard cap); if you need more, create a ticket for customer care.
* **Q: How can I lower the number of activities in a journey?** — Move repeated conditions (such as consent checks and suppressions) into segment definition or audience composition, and consider moving single-action Read audience journeys to campaigns.

+++

<!-- ai-section-version: 1 | source-hash: 3136399d -->
