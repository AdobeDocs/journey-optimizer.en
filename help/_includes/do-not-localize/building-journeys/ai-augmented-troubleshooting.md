---
title: AI Knowledge Reference
---
# AI Knowledge Reference

+++ AI Knowledge Reference

This section contains structured knowledge intended to support interpretation, retrieval, and question answering related to this topic.

For complete understanding, this information should be combined with the documentation on this page. Neither source is intended to stand alone; the page describes the feature, while this section provides additional context that helps disambiguate terminology, intent, applicability, and constraints.

* **TL;DR:** This page explains how to identify and resolve configuration errors and warnings in a journey before entering test mode or publishing.

**Intents:**

* Identify activity-level configuration errors before testing or publishing a journey
* Distinguish between blocking errors and non-blocking warnings in the Alerts panel
* Use the issue log ID (ERR_XXX_XXX type) to diagnose journey issues
* Copy technical journey details for troubleshooting
* Add an alternative path to avoid interrupting the journey of an individual in case of a timeout or an error

**Glossary:**

* **Alerts button**: Button above the canvas that displays detected errors and warnings; errors block publication or test activation, while warnings do not *(product-specific)*
* **ERR_XXX_XXX**: Type of issue log ID shown with the description of each issue, which can help identify the issue *(product-specific)*
* **Alternative path**: A fallback action that can be defined for the Optimize and Action activities, through the option "Add an alternative path in case of a timeout or an error" in the activity's properties *(product-specific)*

**Guardrails:**

* Basic activity checks run automatically while building. **[!UICONTROL Validate]** runs configuration checks, including message checks; errors must be resolved and validation rerun after fixes or edits before testing or publishing.

* You cannot activate test mode or publish a journey if blocking errors remain unresolved.
* Warnings do not block publication or test activation but indicate potential issues.
* A fallback action can be defined for the Optimize and Action activities.
* When an error occurs in an action or a condition, the journey of an individual stops; the only way to make it continue is to solve the issue, or to use the alternative path option.

**Terminology:**

* Canonical name: Alerts — variants: Alerts panel, Alerts button
* Do not confuse: "errors" (block publication) ≠ "warnings" (do not block publication)

**FAQ:**

* **Q: What is the difference between an error and a warning in Journey Optimizer?** — Errors block both test mode activation and journey publication; warnings indicate potential issues but do not prevent testing or publishing.
* **Q: Where can I see all errors affecting my journey?** — Errors appear with a warning symbol on the activities on the canvas, and are also visible from the Alerts button above the canvas, which lets you see the errors detected by the system.
* **Q: What does Copy details provide?** — The **[!UICONTROL Copy details]** button at the bottom of the Alerts list copies technical information about the journey that is useful for troubleshooting.
* **Q: Can I keep a journey running for individuals even if an action encounters an error?** — Yes, for the Optimize and Action activities: check the "Add an alternative path in case of a timeout or an error" option in the activity's properties.
* **Q: When should I perform these troubleshooting checks?** — Before testing or publishing, click **[!UICONTROL Validate]**, resolve errors in the Alerts panel, and validate again. After fixing an error or editing the journey, validate again before continuing.

**Examples:**

* If a mandatory field is empty, an error is displayed on the activity.
* When two activities are disconnected on the canvas, a warning is displayed.

**Related pages:**

* Troubleshooting journey events, profile entry, navigation, and message sending: Troubleshoot your live journey execution (building-journeys/troubleshooting-execution.md)
* Troubleshooting inbound actions: Troubleshoot inbound actions in journeys (building-journeys/troubleshooting-inbound.md)
* Journey validation: Validate your journey (building-journeys/publish-journey.md#validate)
* Error codes: Error codes reference (building-journeys/error-codes-reference.md)
* Fields copied by Copy details: Copy technical details, in Define your journey's properties (building-journeys/journey-properties.md)

+++

<!-- ai-section-version: 2 | source-hash: 8533dde4 -->
