---
title: AI Knowledge Reference
---
# AI Knowledge Reference

+++ AI Knowledge Reference

This section contains structured knowledge intended to support interpretation, retrieval, and question answering related to this topic.

For complete understanding, this information should be combined with the documentation on this page. Neither source is intended to stand alone; the page describes the feature, while this section provides additional context that helps disambiguate terminology, intent, applicability, and constraints.

* **TL;DR:** This page provides practical examples of using the advanced expression editor to build journey conditions that filter users by cart activity, inventory status, geofence events, string manipulations, and timestamp windows.

**Intents:**

* Build a cart abandonment condition using `in()` and `inLastDays()` to target users who added items but did not complete purchase within 7 days
* Filter experience event collections by timestamp window to avoid capturing historical data
* Apply case-sensitive and case-insensitive string comparisons to geofence event fields
* Extract and manipulate CRM IDs from mobile app launch events using `substr` and `lastIndexOf`
* Check product inventory availability by comparing a quantity field against a threshold
* Combine multiple boolean expressions using `and` / `not` logic in journey conditions

**Glossary:**

* **Advanced expression editor**: The Journey Optimizer interface for writing complex, code-level expressions using functions, operators, and field references *(product-specific)*
* **currentDataPackField**: A loop variable used when iterating over data source collections inside `all()`, `first()`, or `last()` functions *(product-specific)*
* **inLastDays(timestamp, N)**: A date function that returns true if the given timestamp falls within the last N days *(product-specific)*
* **Experience Events**: Time-series behavioral data records stored in Adobe Experience Platform, retrieved in reverse chronological order *(product-specific)*

**Guardrails:**

* Using experience events directly in journey expressions/conditions is not supported; alternative methods such as computed attributes or audience segments should be used instead
* The advanced expression editor must be used (not the simple editor) for queries on time-series data such as collections of purchases or clicks
* Double-clicking a field in the left panel inserts it into the expression quickly; avoid typing field paths manually to reduce errors
* Expressions querying experience events return a boolean; ensure downstream logic expects a boolean type

**Terminology:**

* Canonical name: Advanced Expression Editor — Acronym: none — variants: expression editor, advanced editor
* Synonyms: "addToCart" = "add to cart interaction"; "completePurchase" = "purchase completion event"
* Do not confuse: events (prefixed with `@`) ≠ data sources (prefixed with `#`)

**FAQ:**

* **Q: Why must I use the advanced editor instead of the simple editor for cart abandonment queries?** — The simple editor cannot perform queries on time-series collections; the advanced editor is required for `all()`, `first()`, and `last()` collection functions.
* **Q: How do I reference the most recent "addToCart" event in an expression?** — Use the `first()` function on the experience event collection filtered by `productInteraction == "addToCart"`, since events are returned in reverse chronological order.
* **Q: How do I make a string comparison case-insensitive in the advanced editor?** — Use the `equalIgnoreCase()` function instead of the `==` operator.
* **Q: What is the purpose of adding a timestamp window when querying cart events?** — Specifying both a start and end timestamp prevents picking up historical data that falls outside the intended activity window.
* **Q: How do I remove curly braces from a CRM ID string passed in an event?** — Use `substr()` combined with `lastIndexOf()` to extract the content between the braces.

+++
