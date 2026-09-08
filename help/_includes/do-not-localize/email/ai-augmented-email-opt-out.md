---
title: AI Knowledge Reference
---
# AI Knowledge Reference

+++ AI Knowledge Reference

This section contains structured knowledge intended to support interpretation, retrieval, and question answering related to this topic.

For complete understanding, this information should be combined with the documentation on this page. Neither source is intended to stand alone; the page describes the feature, while this section provides additional context that helps disambiguate terminology, intent, applicability, and constraints.

* **TL;DR:** This page explains how to let email recipients unsubscribe in Journey Optimizer — through a one-click opt-out link in the email header or body, or a two-step opt-out via a landing page — so opted-out profiles are excluded from future marketing messages.

**Intents:**

* Add a one-click unsubscribe URL to the email header
* Add a one-click opt-out link in the email body
* Set up a two-step opt-out through an opt-out landing page
* Configure an external landing page opt-out using the Subscription API
* Choose whether an opt-out applies at the channel or the identity level
* Verify that a profile's consent choice has been updated after opt-out

**Glossary:**

* **One-click opt-out**: An unsubscribe link or URL (in the email header or body) that lets a recipient opt out with a single click *(product-specific)*
* **List-Unsubscribe**: The channel-configuration option that adds a one-click unsubscribe URL and mailto address to the email header *(product-specific)*
* **Two-step opt-out**: An opt-out mechanism where the recipient clicks the email link and then confirms by submitting a form on an opt-out landing page *(product-specific)*
* **Channel-level opt-out**: An opt-out that applies to future messages sent to the profile's target(s) for the current channel *(product-specific)*
* **Identity-level opt-out**: An opt-out that applies to future messages sent to the specific target (email address) used for the current message *(product-specific)*
* **choice**: The profile consent attribute whose value changes to "no" once a recipient opts out *(product-specific)*

**Guardrails:**

* All marketing messages must include an opt-out link; this is not required for transactional messages. The category (Marketing or Transactional) is defined at the channel configuration level and when creating the message.
* Once a recipient unsubscribes, the profile is automatically removed from the audience of future marketing messages.
* In two-step opt-out, clicking the email link only opens the landing page — the recipient must submit the form (click the opt-out button) to complete the unsubscription and update consent.
* Unsubscribe events may take longer to reflect at the profile level due to downstream data processing.
* The external landing page opt-out requires implementing a Subscription API call (a POST to the consent preferences endpoint) to update the profile's choice.

**Terminology:**

* Canonical name: opt-out — Acronym: n/a — variants: unsubscribe, opt-out link, unsubscription link
* Synonyms: "opt-out" = "unsubscribe"
* Do not confuse: "One-step opt-out" (single click via a header or body link) ≠ "Two-step opt-out" (click, then submit a form on a landing page)
* Do not confuse: "Channel" opt-out level (all targets for the channel) ≠ "Identity" opt-out level (only the specific target used for the message)

**FAQ:**

* **Q: Do all emails need an opt-out link?** — All marketing messages must include one; transactional messages do not. The Marketing or Transactional category is defined at the channel configuration level and when creating the message.
* **Q: What is the difference between the channel and identity opt-out levels?** — Channel applies the opt-out to future messages sent to the profile's target(s) for the current channel (all email addresses on the profile for that channel); Identity applies it only to the specific target (email address) used for the current message.
* **Q: Why isn't a profile's opt-out reflected immediately?** — Unsubscribe events may take longer to reflect at the profile level due to downstream data processing; allow some time for the system to update.
* **Q: In two-step opt-out, is clicking the email link enough to unsubscribe?** — No. Clicking only opens the landing page; the recipient must submit the form (click the opt-out button) to complete the unsubscription and update consent.
* **Q: How can I confirm a recipient has been opted out?** — In Experience Platform, browse to the profile and check the Attributes tab: the choice value has changed to no.
* **Q: What is the expected event sequence for a landing-page opt-out?** — In order: Click, Visit, Submit, Unsubscribe, Consent update. If any step is missing or occurs out of order, it may indicate an issue with the opt-out implementation.

+++

<!-- ai-section-version: 1 | source-hash: ada7bf93 -->
