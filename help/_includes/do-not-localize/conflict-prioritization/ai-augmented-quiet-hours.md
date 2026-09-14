---
title: AI Knowledge Reference
---
# AI Knowledge Reference

+++ AI Knowledge Reference

This section contains structured knowledge intended to support interpretation, retrieval, and question answering related to this topic.

For complete understanding, this information should be combined with the documentation on this page. Neither source is intended to stand alone; the page describes the feature, while this section provides additional context that helps disambiguate terminology, intent, applicability, and constraints.

* **TL;DR:** This page explains how to create quiet hours rules—time-based exclusions for Email, SMS, Push, and WhatsApp—inside custom channel-domain rule sets, and how to apply them to journey and campaign actions.

**Intents:**

* Create a quiet hours rule in a custom channel-domain rule set
* Define the exclusion period using [!UICONTROL Weekly] or [!UICONTROL Custom date] with a time zone
* Choose how messages are handled during quiet hours ([!UICONTROL Queue message] or [!UICONTROL Discard message])
* Apply an activated quiet hours rule set to journey and campaign actions
* View profiles excluded by quiet hours in reporting

**Glossary:**

* **Quiet hours**: Time-based exclusions for Email, SMS, Push, and WhatsApp that ensure no messages are sent during specific periods *(product-specific)*
* **[!UICONTROL Queue message]**: Handling option where messages are sent at the completion of the quiet hours period unless in Paused state *(product-specific)*
* **[!UICONTROL Discard message]**: Handling option where messages are never sent *(product-specific)*
* **[!UICONTROL Use recipients local time zone]**: Option that applies each profile's own time zone field instead of one standard time zone *(product-specific)*
* **Custom rule set**: A non-global rule set; quiet hours can only be defined in custom rule sets *(product-specific)*

**Guardrails:**

* Supported channels: Email, SMS, Push, and WhatsApp.
* Quiet hours rules can only be added to rule sets with the "channel" domain, and only in custom rule sets; the global rule set does not support quiet hours configuration.
* The [!UICONTROL Category] field is read-only and defaults to [!UICONTROL Marketing].
* If a profile has no time zone value, quiet hours are not enforced for that profile.
* You can add up to 5 separate periods with the [!UICONTROL Add more dates] button (hard limit).
* Updates to a quiet hours rule may take up to 12 hours to be applied to channel actions that already use that rule.
* In cases of high-volume communications, the system may take additional time to begin enforcing quiet hour suppressions.
* If a message remains in a queued state for a profile for more than 7 days, the message is discarded.
* If you select [!UICONTROL Discard message] and apply this rule to a journey action, the profile is removed from message delivery and exited from the journey.

**Terminology:**

* Canonical name: quiet hours — Acronym: n/a — variants: Quiet hours rule, quiet hours rule set
* Synonyms: none
* Do not confuse: "[!UICONTROL Queue message]" (sent after the quiet period unless Paused) ≠ "[!UICONTROL Discard message]" (never sent)
* Do not confuse: "quiet hours" (time-based exclusions) ≠ "frequency capping" (count-based message limits)
* Do not confuse: standard "[!UICONTROL Time zone]" (one time zone for all recipients) ≠ "[!UICONTROL Use recipients local time zone]" (each profile's own time zone)

**FAQ:**

* **Q: Which channels support quiet hours?** — Email, SMS, Push, and WhatsApp.
* **Q: Can I set quiet hours in the global rule set?** — No, quiet hours can only be defined in custom rule sets with the "channel" domain.
* **Q: What happens to a message that hits quiet hours?** — With [!UICONTROL Queue message] it is sent when the quiet period ends unless it is Paused; with [!UICONTROL Discard message] it is never sent.
* **Q: What if a profile has no time zone value?** — Quiet hours are not enforced for that profile.
* **Q: How long can a message stay queued?** — If it remains queued for a profile for more than 7 days, it is discarded.
* **Q: How long do rule updates take to apply?** — Up to 12 hours for channel actions that already use that rule.

+++

<!-- ai-section-version: 1 | source-hash: 5947ec37 -->
