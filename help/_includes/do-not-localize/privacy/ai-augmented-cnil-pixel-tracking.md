---
title: AI Knowledge Reference
---
# AI Knowledge Reference

+++ AI Knowledge Reference

This section contains structured knowledge intended to support interpretation, retrieval, and question answering related to this topic.

For complete understanding, this information should be combined with the documentation on this page. Neither source is intended to stand alone; the page describes the feature, while this section provides additional context that helps disambiguate terminology, intent, applicability, and constraints.

* **TL;DR:** This page explains CNIL's April 2026 recommendation on email tracking pixels and the Adobe Journey Optimizer controls — open tracking toggles, link-level tracking, consent management, opt-out mechanisms, and suppression — that can support your compliance efforts.

**Intents:**

* Understand CNIL's April 2026 recommendation on email tracking pixels and its enforcement timeline
* Control open tracking at the message level using the [!UICONTROL Email opens] option
* Manage link-level tracking modes in the Email Designer
* Understand how consent is captured and enforced for email through Adobe Experience Platform
* Provide opt-out and withdrawal mechanisms for recipients
* Understand how the suppression list excludes profiles from marketing sends

**Glossary:**

* **Email tracking pixel**: a 1x1 transparent image embedded in the HTML of an email that, when loaded by the recipient's email client, records data such as a timestamp, device type, email client, and sometimes an IP address, allowing marketers to see whether an email is opened
* **CNIL**: the *Commission Nationale de l'Informatique et des Libertés*, France's data protection authority
* **[!UICONTROL Email opens]**: message-level option that controls whether the open-tracking pixel is included in the email; enabled by default *(product-specific)*
* **[!UICONTROL Click on email]**: message-level option that controls whether link clicks are tracked; enabled by default *(product-specific)*
* **Marketing email**: promotional communication sent to opted-in subscribers, requiring user consent and respecting suppression and opt-out preferences automatically *(product-specific)*
* **Transactional email**: non-commercial communication that can be sent to profiles who have unsubscribed from marketing communications, subject to applicable law *(product-specific)*
* **`consents.marketing.email.val`**: the primary email marketing consent field, where `y` indicates opt-in, `n` indicates opt-out, and an empty value is treated as consent by default *(product-specific)*
* **[!UICONTROL Enable List-Unsubscribe]**: email channel configuration option that automatically adds a one-click unsubscribe URL and mailto address to the email header; enabled by default for new channel configurations *(product-specific)*
* **Link tracking modes**: per-link settings in the Email Designer [!UICONTROL Links] panel — Tracked, Opt out, Mirror page, and Never *(product-specific)*
* **Suppression list**: automatically managed list of email addresses resulting in hard bounces, soft bounces, or spam complaints, which are excluded from future marketing sends *(product-specific)*

**Guardrails:**

* This page is for informational purposes only and is not legal advice
* CNIL published the recommendation on April 14, 2026, and is expected to begin enforcement activities after July 14, 2026 (dates as stated on the page)
* CNIL provided a three-month period from the date of the recommendation for companies to inform email recipients about pixel tracking and provide an opt-out if necessary
* The [!UICONTROL Email opens] and [!UICONTROL Click on email] options are enabled by default
* Email type (Marketing or Transactional) is set at the channel configuration level and determines whether subscriber consent is required before sending
* An empty value for `consents.marketing.email.val` is treated as consent by default; this default can be changed at onboarding
* The [!UICONTROL Enable List-Unsubscribe] option is enabled by default for new channel configurations
* A one-click opt-out link can be scoped at either the channel level (all future email communications across the channel) or the identity level (the specific email address used in the current message only)
* Setting a link to Never prevents tracking for that URL even when message-level tracking is enabled
* Journey Optimizer performs a consent check at the channel level before each send

**Terminology:**

* Canonical name: Email tracking pixel — variants: open-tracking pixel, 1x1 pixel
* Do not confuse: "Marketing email" (requires consent) ≠ "Transactional email" (can be sent to profiles who have unsubscribed from marketing, subject to applicable law)
* Do not confuse: "Channel level" opt-out (all future email across the channel) ≠ "Identity level" opt-out (the specific email address used in the current message only)
* Do not confuse: "Opt out" (a link tracking mode designating an opt-out or unsubscription URL) ≠ "Never" (a link tracking mode that never activates tracking for that URL)

**FAQ:**

* **Q: When is CNIL expected to begin enforcement?** — After July 14, 2026, per the page.
* **Q: How do you disable open tracking for a specific email?** — Uncheck the [!UICONTROL Email opens] option when creating the message.
* **Q: What does an empty `consents.marketing.email.val` value mean?** — It is treated as consent by default, and this default can be changed at onboarding.
* **Q: Can transactional emails be sent to profiles who unsubscribed from marketing?** — Yes, subject to applicable law.
* **Q: What causes a profile to be added to the suppression list?** — Hard bounces, soft bounces, or spam complaints.
* **Q: What happens when a recipient opts out?** — The consent attribute (`consents.marketing.email.val`) is updated to `n`, the profile is immediately excluded from future marketing email sends, and the opt-out information is stored in the AEP Consent Service Dataset.

+++

<!-- ai-section-version: 1 | source-hash: 6e314974 -->
