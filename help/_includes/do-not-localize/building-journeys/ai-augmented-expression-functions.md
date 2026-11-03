---
title: AI Knowledge Reference
---
# AI Knowledge Reference

+++ AI Knowledge Reference

This section contains structured knowledge intended to support interpretation, retrieval, and question answering related to this topic.

For complete understanding, this information should be combined with the documentation on this page. Neither source is intended to stand alone; the page describes the feature, while this section provides additional context that helps disambiguate terminology, intent, applicability, and constraints.

* **TL;DR:** This page is a categorized reference of all 60+ built-in functions available in the Journey advanced expression editor, covering aggregation, conversion, date/time, list, math, string, and Adobe Experience Platform audience functions.

**Intents:**

* Identify the right function for a task by browsing the categorized function tables
* Transform data types between string, integer, decimal, boolean, date, and duration using conversion functions
* Perform date-based filtering with functions like `inLastDays`, `inNextHours`, `nowWithDelta`, and `dateDiff`
* Manipulate and validate string values using functions like `contain`, `replace`, `split`, and `trim`
* Perform statistical calculations on collections using aggregation functions like `count`, `avg`, `sum`, and `distinctCount`
* Check audience membership in journey conditions using the `inAudience` function

**Glossary:**

* **Aggregation functions**: Functions that compute a single value (count, sum, average, min, max) from a collection of values *(product-specific)*
* **Conversion functions**: Functions that cast a value from one data type to another (e.g. `toString`, `toDateTime`, `toDuration`) *(product-specific)*
* **Date functions**: Functions for working with date, time, and timezone values in journey expressions *(product-specific)*
* **List functions**: Functions for filtering, sorting, and analyzing array/collection data *(product-specific)*
* **inAudience**: A function that checks whether a profile belongs to a specified Adobe Experience Platform audience segment *(product-specific)*

**Guardrails:**

* Functions follow a consistent syntax: `functionName(param1, param2, ...)`
* A function may have multiple signatures (different parameter sets) to handle different use cases
* Each function has a fixed return type — ensure the return type matches what the expression context expects
* The functions available in the Journey expression editor differ from those in the personalization editor

**Terminology:**

* Canonical name: Functions — Acronym: none — variants: built-in functions, expression functions
* Synonyms: "aggregation functions" = "statistical functions"; "conversion functions" = "type casting functions"
* Do not confuse: journey expression functions ≠ personalization editor functions (different sets)

**FAQ:**

* **Q: How many functions are available in the Journey expression editor?** — Over 60 functions organized across categories including aggregation, conversion, date, list, math, string, and Adobe Experience Platform.
* **Q: How do I check if a profile belongs to an audience in a journey condition?** — Use the `inAudience` function with the audience identifier.
* **Q: What function should I use to get the current date and time offset by a number of days?** — Use `nowWithDelta(N, "days")` to get a dateTime offset from the current time.
* **Q: How can I calculate the difference between two dates?** — Use the `dateDiff` function. Both parameters must be the same type: `dateOnly` parameters return the difference in days, while `dateTimeOnly` and `dateTime` parameters return the difference in milliseconds.
* **Q: Can a function return different types depending on how it is called?** — A function has a specific return type per signature, but a single function name can have multiple signatures with different parameter sets and return types.
* **Q: What is the difference between `count` and `countWithNull`?** — `count` counts only non-null elements; `countWithNull` counts all elements including nulls.

+++
