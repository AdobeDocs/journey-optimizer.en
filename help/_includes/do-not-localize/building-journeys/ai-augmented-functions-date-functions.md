---
title: AI Knowledge Reference
---
# AI Knowledge Reference

+++ AI Knowledge Reference

This section contains structured knowledge intended to support interpretation, retrieval, and question answering related to this topic.

For complete understanding, this information should be combined with the documentation on this page. Neither source is intended to stand alone; the page describes the feature, while this section provides additional context that helps disambiguate terminology, intent, applicability, and constraints.

* **TL;DR:** This page documents all date and time functions available in AJO journey expressions, covering how to get the current time, check whether a date falls within a relative time window, and modify date/time components.

**Intents:**
* Get the current datetime (with optional timezone) using `now` or `nowWithDelta`
* Retrieve the current time as an epoch integer using `currentTimeInMillis`
* Calculate the difference between two dates or date-times using `dateDiff`
* Check if a datetime falls within the last N days, hours, months, or years using `inLastDays`, `inLastHours`, `inLastMonths`, `inLastYears`
* Check if a datetime falls within the next N days, hours, months, or years using `inNextDays`, `inNextHours`, `inNextMonths`, `inNextYears`
* Force a specific hour or day of the month on a datetime value using `setHours` or `setDays`
* Convert a datetime to a different timezone while preserving the same instant using `updateTimeZone`

**Glossary:**
* **dateOnly**: A date value with no time or timezone information *(product-specific)*
* **dateTime**: A date-time value that includes timezone offset information *(product-specific)*
* **dateTimeOnly**: A date-time value with no timezone information *(product-specific)*
* **epoch milliseconds**: An integer representing the number of milliseconds elapsed since 1970-01-01T00:00:00Z
* **delta**: An integer offset (positive or negative) used with `nowWithDelta` to shift the current time by a number of years, months, days, hours, minutes, or seconds

**Guardrails:**
* `now()` is only available in journey expressions; for email personalization use `getCurrentZonedDateTime()` instead
* The timezone ID in `nowWithDelta` must be a string constant — field references and dynamic expressions are not supported
* The timezone ID in `updateTimeZone` must be a string constant
* `dateDiff` requires both parameters to be the same data type (`dateOnly`, `dateTimeOnly`, or `dateTime`); mixing types is not supported
* `dateDiff` returns `null` if either parameter is `null`
* `dateDiff` returns days for `dateOnly` parameters, but milliseconds (not days) for `dateTimeOnly` and `dateTime` parameters — convert accordingly when comparing results across types

**Terminology:**
* Canonical name: Date functions — Acronym: none — variants: date-time functions, temporal functions
* Synonyms: "now()" = "current datetime"; "currentTimeInMillis()" = "current epoch milliseconds"
* Do not confuse: "inLastDays" (looks back in time) ≠ "inNextDays" (looks forward in time)
* Do not confuse: "setHours" (replaces the hour component) ≠ "nowWithDelta" (offsets the current time)
* Do not confuse: "updateTimeZone" (same instant, different timezone representation) ≠ "setHours" (changes the time value itself)
* Do not confuse: the journey expression editor's `dateDiff` (accepts `dateOnly`, `dateTimeOnly`, or `dateTime`; returns days or milliseconds depending on type) ≠ the personalization editor's `dateDiff` (accepts only `dateTime`; always returns days)

**FAQ:**
* **Q: Can I use `now()` in email personalization content?** — No, `now()` is only available in journey expressions. Use `getCurrentZonedDateTime()` for email personalization.
* **Q: How do I check if an event happened in the last 24 hours?** — Use `inLastHours(@event{MyEvent.timestamp}, 24)`.
* **Q: How do I get the current time offset by 2 hours in the past?** — Use `nowWithDelta(-2, "hours")`.
* **Q: What does `updateTimeZone` do differently from `setHours`?** — `updateTimeZone` keeps the same instant in time but expresses it in a different timezone, while `setHours` actually changes the hour component of the datetime value.
* **Q: Can the timezone parameter in `nowWithDelta` be a profile field?** — No, the timezone ID must be a string constant; field references are not supported.
* **Q: What happens when `nowWithDelta()` is used with months and the current date is a month-end date?** — The function uses calendar-month arithmetic and normalizes the result to the last valid day of the target month. For example, adding 1 month to January 31 returns February 28 (not March 3).

+++
