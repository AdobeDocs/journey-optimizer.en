---
title: AI Knowledge Reference
---
# AI Knowledge Reference

+++ AI Knowledge Reference

This section contains structured knowledge intended to support interpretation, retrieval, and question answering related to this topic.

For complete understanding, this information should be combined with the documentation on this page. Neither source is intended to stand alone; the page describes the feature, while this section provides additional context that helps disambiguate terminology, intent, applicability, and constraints.

* **TL;DR:** This page documents all conversion functions in AJO journey expressions, explaining how to transform values between types such as string, integer, decimal, boolean, date, datetime, and duration.

**Intents:**
* Convert a string or epoch integer to a timezone-aware datetime using `toDateTime`
* Convert a string or datetime to a timezone-less datetime using `toDateTimeOnly`
* Extract a date-only value (year-month-day) from a string or datetime using `toDateOnly`
* Cast a value to an integer, decimal, or boolean using `toInteger`, `toDecimal`, or `toBool`
* Serialize any value to its string representation using `toString`
* Convert a string or millisecond integer to a duration using `toDuration`

**Glossary:**
* **dateTime**: A datetime value that includes timezone offset information *(product-specific)*
* **dateTimeOnly**: A datetime value with no timezone information *(product-specific)*
* **dateOnly**: A date value representing year-month-day with no time component *(product-specific)*
* **duration**: A time period expressed in ISO-8601 format (e.g., PT10H) *(product-specific)*
* **epoch milliseconds**: Unix timestamp expressed in milliseconds since 1970-01-01T00:00:00Z

**Guardrails:**
* The timezone argument in `toDateTime` must be a string constant — field references and dynamic expressions are not allowed
* String inputs to `toDateTime` and `toDateTimeOnly` must follow ISO-8601 format; malformed strings return null without an error
* `toDateTime` with an epoch integer expects milliseconds; multiply seconds-based timestamps by 1000 before passing
* `toBool` returns `true` only for the exact string `"true"`; strings like `"1"`, `"yes"`, or `"TRUE"` return `false`

**Terminology:**
* Canonical name: Conversion functions — Acronym: none — variants: type casting functions, type conversion functions
* Synonyms: "toDateTime" = "convert to datetime with timezone"; "toDateTimeOnly" = "convert to datetime without timezone"
* Do not confuse: "toDateTime" (timezone-aware) ≠ "toDateTimeOnly" (no timezone)
* Do not confuse: "toDateOnly" (date only, no time) ≠ "toDateTime" (date and time with timezone)

**FAQ:**
* **Q: When should I use `toDateTime` versus `toDateTimeOnly`?** — Use `toDateTime` when timezone information matters (e.g., scheduling or cross-region comparisons); use `toDateTimeOnly` when only the local date-time is relevant and timezone can be ignored.
* **Q: Why does `toBool("TRUE")` return false?** — `toBool` only recognizes the exact lowercase string `"true"`; all other string values including `"TRUE"` or `"yes"` return false.
* **Q: How do I convert a Unix timestamp in seconds to a dateTime?** — Multiply the seconds value by 1000 to get milliseconds, then pass it to `toDateTime`, e.g., `toDateTime(myField * 1000)`.
* **Q: Can the timezone in `toDateTime` be read from a profile attribute?** — No, the timezone ID must be a string constant; field references and expressions are not supported.
* **Q: What format does `toDuration` accept as a string?** — ISO-8601 duration format, e.g., `"PT10H"` for 10 hours or `"P1DT2H"` for 1 day and 2 hours.

+++
