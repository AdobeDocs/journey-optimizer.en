---
title: AI Knowledge Reference
---
# AI Knowledge Reference

+++ AI Knowledge Reference

This section contains structured knowledge intended to support interpretation, retrieval, and question answering related to this topic.

For complete understanding, this information should be combined with the documentation on this page. Neither source is intended to stand alone; the page describes the feature, while this section provides additional context that helps disambiguate terminology, intent, applicability, and constraints.

* **TL;DR:** This page explains how to create an email in Journey Optimizer by adding an Email action to a journey or campaign, defining its subject and content in the Email Designer, resolving alerts, optimizing HTML size, and previewing before sending.

**Intents:**

* Add an Email action to a journey or a campaign
* Define the email subject line and body with the Email Designer
* Enable decisioning to add decision policies to an email
* Resolve warning and error alerts before testing or activating
* Enable and test HTML size optimization to avoid email clipping
* Preview and validate the email before sending

**Glossary:**

* **Email action**: The channel action added to a journey or campaign that sends an email when profiles reach that step *(product-specific)*
* **Email Designer**: The Journey Optimizer editor used to build and personalize the email body *(product-specific)*
* **Optimize HTML size**: An option that compresses the email HTML at publication time (removing unnecessary whitespace and indentation) to reduce size and avoid clipping *(product-specific)*
* **Alerts**: In-interface messages raised when key settings are missing — Warnings (recommendations/best practices) and Errors (blocking issues) *(product-specific)*
* **Decision policy**: A container for offers that uses the Decisioning engine to return the best content for each audience member (in Limited Availability for emails) *(product-specific)*

**Guardrails:**

* The subject line is mandatory and must not include line breaks.
* Legacy native channel activities (Email, Push, SMS, In-app, Web, Code-based experience, and Content Card) are deprecated as of the March 2026 release; existing journeys using them continue to work without changes and no migration is required.
* Decision policy creation in emails is in Limited Availability — contact your Adobe representative to gain access.
* All error alerts (for example a missing subject line, an empty email version, or a deleted configuration) must be resolved before you can test or activate the journey/campaign; warnings do not block.
* HTML size optimization is not applied automatically — you must enable it manually — and is applied only at publication time.
* In multilingual emails, Optimize HTML size is tracked at the email level, not per locale: enabling it on any one locale applies it to all locales at publish time; to disable it, uncheck it on every locale.
* Removal of non-essential HTML comments during optimization is temporarily disabled as of July 10, 2026.
* The sizes shown in View proofs reflect the HTML template with Handlebars expressions evaluated at their minimum value, not the size of the final delivered email.

**Terminology:**

* Canonical name: Email action — Acronym: n/a — variants: email activity, email channel action
* Do not confuse: "Warnings" (recommendations/best practices; do not block testing or activation) ≠ "Errors" (must be resolved before testing or activating)
* Do not confuse: "Simulate content" (test variations with sample input data or AI auto-generation) ≠ "Simulate content (AEP profiles)" (preview with test profiles, send proofs, and check email rendering)

**FAQ:**

* **Q: How do I create an email?** — Add an Email action to a journey or a campaign, select or create an email configuration, then define the subject and body in the Email Designer.
* **Q: Are the legacy native email/push/SMS journey activities still usable?** — They are deprecated as of the March 2026 release, but existing journeys using them continue to work without changes and no migration is required.
* **Q: Why can't I test or activate my journey or campaign?** — All error alerts (such as a missing subject line, an empty email version, or a deleted configuration) must be resolved first; warnings do not block testing or activation.
* **Q: What does the Optimize HTML size option do, and is it automatic?** — It compresses the email HTML at publication time by removing unnecessary whitespace and indentation, which helps avoid email clipping (some clients such as Gmail truncate messages over ~100 KB). It is not automatic — you must enable it manually.
* **Q: How does Optimize HTML size behave for multilingual emails?** — It is tracked at the email level, not per locale: enabling it on one locale applies it to all locales at publish time, and to disable it you must uncheck it on every locale.
* **Q: How can I preview or test my email before sending?** — Use Simulate content (sample input data or AI auto-generation), or Simulate content (AEP profiles) to preview with test profiles, send proofs, and check rendering; you can also validate content quality.

+++

<!-- ai-section-version: 1 | source-hash: 2b6a4f1b -->
