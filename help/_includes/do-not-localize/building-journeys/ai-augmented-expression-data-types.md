---
title: AI Knowledge Reference
---
# AI Knowledge Reference

+++ AI Knowledge Reference

This section contains structured knowledge intended to support interpretation, retrieval, and question answering related to this topic.

For complete understanding, this information should be combined with the documentation on this page. Neither source is intended to stand alone; the page describes the feature, while this section provides additional context that helps disambiguate terminology, intent, applicability, and constraints.

* **TL;DR:** This page describes every data type supported in the Journey advanced expression editor — string, integer, decimal, boolean, dateOnly, dateTimeOnly, dateTime, duration, and list — with their JSON formats, serialization rules, and literal representation syntax.

**Intents:**

* Identify the correct literal syntax for each data type when writing journey expressions
* Understand the difference between `dateOnly`, `dateTimeOnly`, and `dateTime` types and when to use each
* Represent a duration value using ISO-8601 format or milliseconds with the `toDuration()` function
* Construct a list expression with square bracket syntax for use in collection operations
* Use conversion functions (`toDateTime`, `toDateTimeOnly`, `toDuration`, `toDateOnly`) to create typed constants

**Glossary:**

* **dateOnly**: A date without time or time zone, formatted as YYYY-MM-DD; suitable for birthdays or calendar dates *(product-specific)*
* **dateTimeOnly**: A date and time without time zone information; cannot represent a specific instant without an offset *(product-specific)*
* **dateTime**: A date-time constant that includes a UTC offset, representing a specific instant; can also be created from an epoch integer *(product-specific)*
* **duration**: A time-based amount modelled in milliseconds; uses ISO-8601 `PnDTnHnMn.nS` format; years and months are not supported *(product-specific)*
* **list**: A comma-separated collection of expressions of the same type, delimited by square brackets *(product-specific)*

**Guardrails:**

* Duration supports milliseconds, seconds, minutes, hours, and days only — years and months are not supported as they are not fixed amounts of time
* A `duration` value must be wrapped in `toDuration()` — it cannot be expressed as a bare literal
* All expressions in a `list` must have the same type — polymorphism is not supported
* `dateTimeOnly` cannot represent an instant in time without an additional offset or time zone

**Terminology:**

* Canonical name: Data Types — Acronym: none — variants: expression data types, journey data types
* Synonyms: "dateTime" = "date-time with timezone"; "dateTimeOnly" = "local date-time"
* Do not confuse: `dateOnly` (no time) ≠ `dateTimeOnly` (date + time, no timezone) ≠ `dateTime` (date + time + timezone/offset)

**FAQ:**

* **Q: What is the difference between `dateTimeOnly` and `dateTime`?** — `dateTimeOnly` has no time zone or offset and cannot represent a precise instant; `dateTime` includes a UTC offset and represents a specific moment in time.
* **Q: How do I express a duration of 2 days and 3 hours?** — Use `toDuration("P2DT3H")`.
* **Q: Can I mix integers and strings in a list expression?** — No; all expressions in a list must be the same type.
* **Q: How do I create a `dateTime` from an epoch timestamp in milliseconds?** — Use `toDateTime(<epoch in milliseconds>)`, for example `toDateTime(1560762190189)`.
* **Q: Is `true` or `True` the correct boolean literal?** — Use lowercase `true` or `false`; uppercase variants are not valid.

+++
