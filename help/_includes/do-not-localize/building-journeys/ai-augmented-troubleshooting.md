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
* Use the error log ID (ERR_XXX_XXX format) to diagnose journey issues
* Copy technical journey details for troubleshooting
* Add an alternative path to prevent individual journeys from stopping on error or timeout

**Glossary:**

* **Alerts button**: Button above the canvas that displays detected errors and warnings; errors block publication or test activation, while warnings do not *(product-specific)*
* **ERR_XXX_XXX**: Issue log ID format assigned to each detected problem, used to identify and communicate errors *(product-specific)*
* **Alternative path**: A fallback branch added to an action or condition activity that continues the journey when an error or timeout occurs *(product-specific)*

**Guardrails:**
* Basic activity checks run automatically while building. **[!UICONTROL Validate]** runs configuration checks, including message checks; errors must be resolved and validation rerun after fixes or edits before testing or publishing.

* You cannot activate test mode or publish a journey if blocking errors remain unresolved.
* Warnings do not block publication or test activation but indicate potential issues.
* Alternative paths are only available for Optimize and Action activities.

**Terminology:**

* Canonical name: Alerts — Acronym: none — variants: Alerts panel, Alerts button
* Do not confuse: "errors" (block publication) ≠ "warnings" (do not block publication)

**FAQ:**

* **Q: What is the difference between an error and a warning in Journey Optimizer?** — Errors block both test mode activation and journey publication; warnings indicate potential issues but do not prevent testing or publishing.
* **Q: Where can I see all errors affecting my journey?** — Click the Alerts button above the canvas to see a consolidated list of all system-detected errors and warnings.
* **Q: What does Copy details provide?** — The **[!UICONTROL Copy details]** button at the bottom of the Alerts list copies technical information about the journey that is useful for troubleshooting.
* **Q: Can I keep a journey running for individuals even if an action encounters an error?** — Yes, enable the "Add an alternative path in case of a timeout or an error" option in the activity properties to define a fallback path.
* **Q: When should I perform these troubleshooting checks?** — Before testing or publishing, click **[!UICONTROL Validate]**, resolve errors in the Alerts panel, and validate again. After fixing an error or editing the journey, validate again before continuing.

+++

<!-- ai-section-version: 1 | source-hash: da2b62d8 -->
