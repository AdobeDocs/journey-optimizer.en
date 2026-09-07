---
title: AI Knowledge Reference
---
# AI Knowledge Reference

+++ AI Knowledge Reference

This section contains structured knowledge intended to support interpretation, retrieval, and question answering related to this topic.

For complete understanding, this information should be combined with the documentation on this page. Neither source is intended to stand alone; the page describes the feature, while this section provides additional context that helps disambiguate terminology, intent, applicability, and constraints.

* **TL;DR:** This page documents the `all()`, `first()`, `last()`, and `at()` collection management functions used in the Journey advanced expression editor, illustrated with push notification token payload examples.

**Intents:**

* Filter a collection of event or data source fields using a boolean condition with `all(<condition>)`
* Count filtered or unfiltered collection elements using `count()` combined with collection functions
* Retrieve the first or last matching element of a collection using `first()` or `last()`
* Access a collection element at a specific zero-based index using `at(<index>)`
* Understand which loop variable (`currentEventField`, `currentDataPackField`, `currentActionField`) applies to each collection context

**Glossary:**

* **all(condition)**: Filters a collection and returns all items matching the given boolean expression *(product-specific)*
* **first(condition)**: Returns the first (most recent for experience events) element in a collection matching the condition *(product-specific)*
* **last(condition)**: Returns the last (oldest for experience events) element in a collection matching the condition *(product-specific)*
* **at(index)**: Returns the element at the specified zero-based index of a collection *(product-specific)*
* **currentEventField**: Loop variable available only when iterating over event collections *(product-specific)*
* **currentDataPackField**: Loop variable available only when iterating over data source collections *(product-specific)*
* **currentActionField**: Loop variable available only when iterating over custom action response collections *(product-specific)*

**Guardrails:**

* Using experience events in journey expressions/conditions is not supported; consider alternative methods such as computed attributes
* `currentEventField`, `currentDataPackField`, and `currentActionField` are only available inside their respective collection contexts
* The `all` function is not required to count collection elements — `count()` can be applied directly to the field path
* When `all()` is called with an empty condition, all elements in the collection are returned

**Terminology:**

* Canonical name: Collection Management Functions — Acronym: none — variants: collection functions, query collection functions
* Synonyms: "all()" = "collection filter function"; "at()" = "index accessor"
* Do not confuse: `first()` (most recent experience event) ≠ first inserted element in general lists

**FAQ:**

* **Q: What is the difference between `all()` with an empty condition and `all()` with a condition?** — An empty `all()` returns every element; a condition-based `all()` returns only elements matching that boolean expression.
* **Q: How do I count push notification tokens without using `all()`?** — Call `count()` directly on the token field path, e.g. `count(@event{LobbyBeacon...pushNotificationTokens.token})`.
* **Q: Which variable do I use to reference the current element when looping over a data source collection?** — Use `currentDataPackField` inside `all()`, `first()`, or `last()` on data source collections.
* **Q: How do I get the second item in a collection?** — Use `at(1)` because index 0 is the first element.
* **Q: Why does `last()` return the oldest experience event?** — Experience events are stored in reverse chronological order, so the last position in the collection corresponds to the oldest event.

+++
