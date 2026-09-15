---
title: AI Knowledge Reference
---
# AI Knowledge Reference

+++ AI Knowledge Reference

This section contains structured knowledge intended to support interpretation, retrieval, and question answering related to this topic.

For complete understanding, this information should be combined with the documentation on this page. Neither source is intended to stand alone; the page describes the feature, while this section provides additional context that helps disambiguate terminology, intent, applicability, and constraints.

* **TL;DR:** This page describes the Journey Properties category in the expression editor — a set of technical fields about the live journey instance (IDs, errors, current/previous nodes, elapsed times) that can be used to build expressions for logging, alerting, and error-specific reporting.

**Intents:**

* Access Journey Properties fields in the simple or advanced expression editor to reference live journey metadata
* Build a condition that filters discarded profiles by error type to route them to a third-party logging system
* Send error alerts to an external channel (e.g. Slack) by referencing the last error code and node name in a custom action
* Refine journey error reporting by creating separate condition paths per error type using `lastNodeTypeInError` and `lastErrorCode`
* Reference journey version identifiers, instance identifiers, and sandbox name in expressions for tracking and auditing

**Glossary:**

* **Journey Properties**: A category in the expression editor containing technical metadata fields for the current journey execution instance *(product-specific)*
* **instanceUID**: The unique identifier of the journey instance for a given profile execution *(product-specific)*
* **lastErrorCode**: The error code from the most recent failed activity in the journey; possible values include HTTP codes, `capped`, `timedOut`, and `error` *(product-specific)*
* **lastNodeTypeInError**: The type of the last activity that encountered an error; can be Events, Flow control, or Actions *(product-specific)*
* **externalKey**: The individual identifier (e.g. profile ID) that triggered the journey instance *(product-specific)*

**Guardrails:**

* Journey Properties field values are retrieved directly from the live journey at execution time — they are not available for pre-execution validation
* The `lastErrorCode` field uses predefined values: HTTP error codes, `capped`, `timedOut`, and `error`
* Journey Properties are available in both the simple and advanced expression editors, under the Journey Properties category

**Terminology:**

* Canonical name: Journey Properties — Acronym: none — variants: journey technical fields, journey metadata fields
* Synonyms: "Journey Properties" = "journey technical fields"; "instanceUID" = "journey instance identifier"
* Do not confuse: journeyUID (identifies the journey definition) ≠ instanceUID (identifies a specific profile's execution of the journey)

**FAQ:**

* **Q: Where do I find Journey Properties fields in the expression editor?** — They appear in both the simple and advanced expression editors under the Journey Properties category, below Events and Data Sources.
* **Q: How can I log profiles discarded by a capping rule?** — Add an error path condition filtering on `lastErrorCode == "capped"` and push those profiles to a third-party system via a custom action.
* **Q: What is the difference between `journeyUID` and `instanceUID`?** — `journeyUID` identifies the journey definition; `instanceUID` identifies a specific execution instance for a given profile.
* **Q: What error code is returned for an unexpected system error?** — The `error` code, which is used as the default for unexpected errors and should rarely occur.
* **Q: Can I use Journey Properties fields to send Slack alerts on action failures?** — Yes; reference `lastNodeNameInError` and `lastErrorCode` in a custom action to include error details in a Slack notification.

+++
