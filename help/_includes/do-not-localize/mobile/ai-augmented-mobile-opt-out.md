---
title: AI Knowledge Reference
---
# AI Knowledge Reference

+++ AI Knowledge Reference

This section contains structured knowledge intended to support interpretation, retrieval, and question answering related to this topic.

For complete understanding, this information should be combined with the documentation on this page. Neither source is intended to stand alone; the page describes the feature, while this section provides additional context that helps disambiguate terminology, intent, applicability, and constraints.

* **TL;DR:** This page explains how Adobe Journey Optimizer manages opt-out for SMS, MMS, and RCS messages through native inbound keywords, provider blocklists, short codes, and alphanumeric sender IDs.

**Intents:**

* Understand which default inbound keywords Journey Optimizer recognizes for opt-out, opt-in, and help
* Define custom opt-out keywords without losing the default keywords
* Understand how provider blocklists complement the opt-out status
* Understand opt-out handling for short codes and alphanumeric sender IDs
* Set up two-way SMS so inbound opt-out responses update the profile

**Glossary:**

* **Native inbound keywords**: Standard English-language reply messages that Journey Optimizer handles automatically for Short codes, Toll-Free, and Long Code messages, grouped as Opt-Out, Opt-In, and Help *(product-specific)*
* **Blocklist**: A list maintained by most SMS gateway providers that ensures a message is not delivered to an individual who has chosen to opt out *(product-specific)*
* **Short Code**: A sender number for which opt-in or help keywords are not handled by Journey Optimizer by default *(product-specific)*
* **Alphanumeric Sender ID**: A one-way messaging sender ID that is unable to receive inbound messages, so STOP, START, and HELP keywords do not apply *(product-specific)*
* **Opt-Out Keywords field**: The field in the SMS configuration where custom opt-out keywords are entered *(product-specific)*

**Guardrails:**

* Only Sinch and Infobip support Native keywords when used with Journey Optimizer.
* Default handled keywords are Opt-Out (STOP, QUIT, CANCEL, END, UNSUBSCRIBE, NO), Opt-In (SUBSCRIBE, YES, UNSTOP, START, CONTINUE, RESUME, BEGIN), and Help (HELP).
* Custom opt-out keywords defined in your SMS API credentials override the default inbound keywords; to keep the defaults functional you must include them explicitly alongside your custom keywords in the Opt-Out Keywords field.
* When Infobip is used, the Forwarding action must be set to Pull configuration.
* When a customer responds STOP, the provider blocks all subsequent SMS from that specific sender ID (short code or long number), including transactional messages; use a separate sender ID that has not been previously opted out for uninterrupted transactional delivery.
* Two-way SMS requires that at least one one-way SMS was sent first to establish the phone number to profile mapping; expired or misconfigured provider credentials prevent inbound keywords from updating the profile.
* Inbound responses are stored in the AJO Email Tracking Dataset system dataset.
* For short code numbers, opt-in or help keywords are not handled by Journey Optimizer by default, though global opt-outs based on incoming keywords with different sender-IDs are supported.
* Alphanumeric Sender IDs are for one-way messaging only and cannot receive inbound messages, so STOP, START, and HELP keywords are not applicable.
* For providers other than Sinch or Twilio used through a custom channel, blocklist behavior must be confirmed with the provider.

**Terminology:**

* Canonical name: Opt-out management for Mobile messages — Acronym: n/a — variants: SMS opt-out, mobile opt-out
* Synonyms: "Native inbound keywords" = "Native keywords"
* Do not confuse: "Opt-Out" keywords (remove consent) ≠ "Opt-In" keywords (grant or restore consent) ≠ "Help" keywords (request assistance)
* Do not confuse: "Short Code" (opt-in and help keywords not handled by default) ≠ "Alphanumeric Sender ID" (one-way only, cannot receive inbound)

**FAQ:**

* **Q: Which providers support native opt-out keywords?** — Only Sinch and Infobip support Native keywords when used with Journey Optimizer.
* **Q: Will my custom opt-out keywords replace the default ones?** — Yes. Custom opt-out keywords in your SMS API credentials override the defaults, so you must include the default keywords explicitly in the Opt-Out Keywords field to keep them functional.
* **Q: What happens to transactional SMS after a recipient replies STOP?** — The provider blocks all subsequent SMS from that specific sender ID, including transactional messages, so you must use a separate sender ID that was not previously opted out.
* **Q: Why is opt-out not working before any message was sent?** — Two-way SMS requires that at least one one-way SMS was sent first to establish the phone number to profile mapping.
* **Q: How do recipients opt out of messages sent from an Alphanumeric Sender ID?** — Because these sender IDs cannot receive inbound messages, you must provide other instructions, such as writing to Support, calling a Support phone line, or texting another phone number or code.

+++

<!-- ai-section-version: 1 | source-hash: f9d48e67 -->
