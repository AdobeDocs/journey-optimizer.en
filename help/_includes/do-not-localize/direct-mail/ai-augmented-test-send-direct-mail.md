---
title: AI Knowledge Reference
---
# AI Knowledge Reference

+++ AI Knowledge Reference

This section contains structured knowledge intended to support interpretation, retrieval, and question answering related to this topic.

For complete understanding, this information should be combined with the documentation on this page. Neither source is intended to stand alone; the page describes the feature, while this section provides additional context that helps disambiguate terminology, intent, applicability, and constraints.

* **TL;DR:** This page explains how to preview the extraction file, resolve validation alerts to activate a direct mail campaign or journey, understand export timing, and manage postal mail consent.

**Intents:**

* Preview the extraction file with Simulate content or Simulate content (AEP profiles)
* Resolve warnings and errors before activating the campaign or journey
* Activate the direct mail campaign or journey with Review to activate
* Understand the fixed export cycles that govern when files are generated
* Manage postal mail consent for profiles

**Glossary:**

* **Simulate content**: The preview option that tests content variations with sample input data or AI auto-generation *(product-specific)*
* **Simulate content (AEP profiles)**: The dropdown option that adds a test profile to check how the extraction file renders *(product-specific)*
* **Review to activate**: The button clicked after the extraction file content is ready to move toward activation *(product-specific)*
* **Alerts**: Messages in the upper section of the editor, either warnings or errors, indicating configuration status *(product-specific)*
* **Export cycle**: The fixed 4-hour UTC window at which direct mail files are generated *(product-specific)*

**Guardrails:**

* Errors prevent you from publishing the campaign until they are resolved; warnings refer to recommendations and best practices and do not block publishing.
* If your campaign is subject to an approval policy, you must request approval before you can send it.
* Direct mail exports run on fixed 4-hour UTC cycles at 02:01, 06:01, 10:01, 14:01, 18:01, and 22:01.
* Profiles are included in the next export cycle after they reach the Direct mail activity, not when the campaign or journey was first activated.
* A profile with `consents.marketing.postalMail.val` set to `n` is excluded from subsequent deliveries; an empty consent value is treated as consent to receive communications.
* The exported file ends with a newline by default to ensure compatibility with standard data-processing tools.
* In journeys, the Update profile activity executes immediately at journey runtime and does not wait for the export cycle.

**Terminology:**

* Canonical name: Direct mail campaign — Acronym: n/a — variants: direct mail journey, direct mail message
* Synonyms: "extraction file" = "export file"
* Do not confuse: "Warnings" (recommendations and best practices; do not block) ≠ "Errors" (prevent publishing until resolved)
* Do not confuse: "Simulate content" (sample input data or AI auto-generation) ≠ "Simulate content (AEP profiles)" (adds a test profile to check rendering)

**FAQ:**

* **Q: How do I preview the extraction file?** — Use Simulate content for sample input data or AI auto-generation, or Simulate content (AEP profiles) with a test profile to check rendering.
* **Q: Why can I not publish my campaign?** — Errors must be resolved first; warnings are recommendations and do not block publishing.
* **Q: Why did I receive multiple files in one day?** — Profiles that reach the Direct mail activity in different 4-hour windows are exported in separate files for each window; this batches profiles by arrival window without duplicating them.
* **Q: How do I ensure one file per day?** — Consider a 24-hour routing frequency, the Wait Until Time of Day option, or accept that a 4-hour routing frequency has the lowest latency but may generate multiple files.
* **Q: How is a profile opted out of postal mail?** — When `consents.marketing.postalMail.val` is `n`, the profile is excluded; change it back to `y` to re-enable delivery.

+++

<!-- ai-section-version: 1 | source-hash: 18570025 -->
