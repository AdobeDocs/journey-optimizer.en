---
title: AI Knowledge Reference
---
# AI Knowledge Reference

+++ AI Knowledge Reference

This section contains structured knowledge intended to support interpretation, retrieval, and question answering related to this topic.

For complete understanding, this information should be combined with the documentation on this page. Neither source is intended to stand alone; the page describes the feature, while this section provides additional context that helps disambiguate terminology, intent, applicability, and constraints.

* **TL;DR:** This page explains how to pass simple and object collections dynamically into custom action parameters in Journey Optimizer, including supported field types, the configuration procedure, and known limitations around nested arrays.

**Intents:**
* Configure a custom action to accept a collection (simple or object) as a dynamic parameter
* Define array parameters as variables in the advanced expression editor when building a journey
* Apply filter and intersect functions to manipulate array data in the expression editor
* Understand and work within the nested array limitations for custom action request payloads
* Test collection parameters using code view mode in journey test mode

**Glossary:**
* **Simple collection**: A list of basic scalar values (strings, numbers, booleans) passed as a custom action parameter *(product-specific)*
* **Object collection**: A list of structured objects, each with multiple fields, passed as a custom action parameter *(product-specific)*
* **listObject**: The field type used in custom action configuration to represent an array of objects *(product-specific)*
* **listAny**: The field type used for heterogeneous arrays or arrays of arrays where items have mixed types *(product-specific)*
* **Variable (vs. Constant)**: In action parameter configuration, a field set to "variable" is populated dynamically at runtime from the journey context, while a "constant" is a fixed value set at configuration time *(product-specific)*

**Guardrails:**
* Nested arrays in request payloads are only supported when they contain a fixed number of items (defined as constants); dynamic nested arrays are not supported
* Code view mode is required to test collections in test mode; code view is not supported for business events, so only single-element collections can be sent in that case
* At least one object must be present in the payload example used to define collection fields
* The first object of the payload example defines the fields for the entire collection

**Terminology:**
* Canonical name: Collection — Acronym: none — variants: array, list, dynamic collection
* Synonyms: "simple collection" = "list of scalar values" ; "object collection" = "array of objects"
* Do not confuse: "listAny" ≠ "listObject" (listAny handles heterogeneous or nested arrays; listObject handles uniform arrays of structured objects)

**FAQ:**
* **Q: What is the difference between a simple collection and an object collection?** — A simple collection contains basic scalar values (strings, numbers, booleans), while an object collection contains structured objects each with multiple named fields.
* **Q: How do I make a collection parameter dynamic at runtime?** — In the custom action's Action parameters section, set the array field to "variable"; all object fields within it are then automatically set to variables.
* **Q: Are nested arrays supported in custom action request payloads?** — Only partially. Nested arrays with a fixed, known number of items can be defined as constants. Nested arrays with a dynamic number of items are not supported in request payloads.
* **Q: How do I test a collection in journey test mode?** — Use code view mode in the test interface. Note that business events do not support code view, so only single-element collections can be tested in that context.
* **Q: What field types are supported for collections?** — listString, listInteger, listDecimal, listBoolean, listDateTime, listDateTimeOnly, listDateOnly, and listObject are all supported.

+++
