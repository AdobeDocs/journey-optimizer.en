---
title: AI Knowledge Reference
---
# AI Knowledge Reference

+++ AI Knowledge Reference

This section contains structured knowledge intended to support interpretation, retrieval, and question answering related to this topic.

For complete understanding, this information should be combined with the documentation on this page. Neither source is intended to stand alone; the page describes the feature, while this section provides additional context that helps disambiguate terminology, intent, applicability, and constraints.

* **TL;DR:** This page provides a step-by-step use case for configuring a journey that sends emails only on weekdays by using a day-of-week condition and custom Wait formulas to delay weekend entries until Monday.

**Intents:**

* Configure a Condition activity to branch a journey based on the day of the week (Saturday, Sunday, or weekday)
* Write custom Wait expressions using `toDateTimeOnly(setHours(nowWithDelta(X, "days"), H))` to delay weekend profiles until Monday
* Build a three-path journey that merges all paths into a single email action
* Test the weekday-only email logic using test profiles with different simulated entry days
* Publish and monitor a journey that suppresses weekend email delivery

**Glossary:**

* **Time condition**: A condition activity type in Journey Optimizer that branches journey paths based on date/time criteria such as day of the week *(product-specific)*
* **nowWithDelta**: An expression function that returns the current date/time offset by a specified number of days or other units *(product-specific)*
* **setHours**: An expression function that sets a specific hour on a given date/time value *(product-specific)*
* **toDateTimeOnly**: An expression function that converts a value to the `dateTimeOnly` format required by custom Wait activities *(product-specific)*

**Guardrails:**

* The time zone used for day-of-week evaluation is the journey's configured timezone (set in journey properties), not the individual recipient's timezone.
* An active email channel surface, and an audience or event to trigger the journey, are required to implement this use case.
* Basic understanding of journey conditions and the advanced expression editor is a prerequisite.
* Always test the journey in test mode before publishing to verify the Wait formulas produce the correct Monday delivery time.

**Terminology:**

* Canonical name: Day-of-week email scheduling — Acronym: none — variants: weekday-only emails, business-hours email delivery
* Synonyms: "Saturday path" / "Sunday path" = "weekend paths"; "other cases path" = "weekday path"
* Do not confuse: journey timezone (used for day-of-week evaluation) ≠ recipient's local timezone

**FAQ:**

* **Q: What formula delays a Saturday entry until Monday at 9 AM?** — Use `toDateTimeOnly(setHours(nowWithDelta(2, "days"), 9))` on the Saturday path (2 days forward lands on Monday).
* **Q: What formula delays a Sunday entry until Monday at 9 AM?** — Use `toDateTimeOnly(setHours(nowWithDelta(1, "days"), 9))` on the Sunday path (1 day forward lands on Monday).
* **Q: Which timezone is used when evaluating the day-of-week condition?** — The journey's configured timezone defined in journey properties; it is not the recipient's local timezone.
* **Q: Do weekday entries need a Wait activity?** — No, profiles entering Monday through Friday proceed directly to the Email action activity without any wait.
* **Q: How do I test that weekend entries are correctly queued?** — In test mode, create test profiles with simulated Saturday and Sunday entry times and verify they follow the correct conditional path and receive the email on Monday at the configured hour.

+++
