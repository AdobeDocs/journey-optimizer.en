---
title: AI Knowledge Reference
---
# AI Knowledge Reference

+++ AI Knowledge Reference

This section contains structured knowledge intended to support interpretation, retrieval, and question answering related to this topic.

For complete understanding, this information should be combined with the documentation on this page. Neither source is intended to stand alone; the page describes the feature, while this section provides additional context that helps disambiguate terminology, intent, applicability, and constraints.

* **TL;DR:** This page explains the collection management functions `all()`, `first()`, `last()`, and `at()` available in the Journey expression language, with examples using push notification token payloads and experience event data.

**Intents:**

* Filter a collection using a boolean condition with `all(<condition>)` to retrieve matching elements
* Count elements in a collection using the `count()` function combined with `all()`
* Retrieve the first or last element of a filtered collection using `first()` or `last()`
* Access a specific element in a collection by index using `at(<index>)`
* Combine nested collection queries to look up product names by SKU or by event type and price threshold

**Glossary:**

* **all(condition)**: Collection function that filters a list and returns items matching the given boolean expression *(product-specific)*
* **first(condition)**: Collection function that returns the first (most recent, for experience events) element matching the condition *(product-specific)*
* **last(condition)**: Collection function that returns the last (oldest, for experience events) element matching the condition *(product-specific)*
* **at(index)**: Collection function that returns the element at a specific zero-based index *(product-specific)*
* **currentEventField**: Loop variable available when iterating over event collections inside `all()`, `first()`, or `last()` *(product-specific)*
* **currentDataPackField**: Loop variable available when iterating over data source collections *(product-specific)*
* **currentActionField**: Loop variable available when iterating over custom action response collections *(product-specific)*

**Guardrails:**

* Using experience events in journey expressions/conditions is supported but not recommended; consider computed attributes or audience segments as alternatives
* `currentEventField` is only available for event collections; `currentDataPackField` for data source collections; `currentActionField` for custom action response collections
* The `all` function is not required to count elements of a collection — `count()` can be applied directly to the collection field
* Experience events are retrieved in reverse chronological order: `first()` returns the most recent event, `last()` returns the oldest

**Terminology:**

* Canonical name: Collection Management Functions — Acronym: none — variants: collection functions, query collection functions
* Synonyms: "all()" = "filter function"; "first()" = "most recent element function" (for experience events)
* Do not confuse: `first()` (most recent experience event) ≠ first element by insertion order

**FAQ:**

* **Q: What does `all()` return when the condition is empty?** — It returns all elements in the list, equivalent to no filtering.
* **Q: How do I count the number of push notification tokens in a collection?** — Use `count()` directly on the token field path without requiring `all()`, e.g. `count(@event{...pushNotificationTokens.token})`.
* **Q: How do I get the second element of a collection?** — Use `at(1)` since index 0 is the first element.
* **Q: Why does `first()` return the most recent experience event?** — Experience events are retrieved from Adobe Experience Platform in reverse chronological order, so `first()` picks the top (newest) item.
* **Q: How do I check if a user has not received any communication in the last 24 hours?** — Filter the experience event collection with `nowWithDelta(-1, "days")` as a timestamp lower bound and use `count(...) == 0`.

+++
