---
title: AI Knowledge Reference
---
# AI Knowledge Reference

+++ AI Knowledge Reference

This section contains structured knowledge intended to support interpretation, retrieval, and question answering related to this topic.

For complete understanding, this information should be combined with the documentation on this page. Neither source is intended to stand alone; the page describes the feature, while this section provides additional context that helps disambiguate terminology, intent, applicability, and constraints.

* **TL;DR:** This page is a troubleshooting reference for live journey execution in Adobe Journey Optimizer, covering event delivery, profile entry, test mode transition issues, discarded events, duplicate journey step event entries, message delivery checks, dashboard metric discrepancies, and empty tracking parameter placeholders.

**Intents:**

* Diagnose why events are not entering a journey by checking payload structure, headers, event condition data types, and qualification conditions
* Verify whether profiles are entering and progressing through a journey in test mode or live
* Resolve test profiles that do not progress, using the journey start date, test profile configuration, and identity namespace checks
* Understand and handle the `maxInstanceStackEventsReached` discard reason for blocked journey instances
* Identify and correctly query duplicate Journey Step Events entries that have different `_id` values
* Investigate missing messages by checking journey reporting, message feedback, and custom action call results
* Fix empty tracking URL placeholders in emails from closed journeys

**Glossary:**

* **Journey Step Events**: The dataset to which journey step events are logged; queried to find discard reasons and duplicate rows, and to confirm that Journey Optimizer executed a custom action *(product-specific)*
* **notSuitableInitialEvent**: A discard code that logs can show when an event was received but discarded because it did not meet the qualification condition *(product-specific)*
* **maxInstanceStackEventsReached**: A discard reason that appears when the journey runtime reaches its internal per-profile event stack limit for a specific journey version (see Guardrails) *(product-specific)*
* **isValidTransition**: A UI-only property in the journey's technical details; the page states it does not impact backend processing or journey performance, and a null value can indicate a journey misconfiguration (start date set in the future) or a corrupted transition *(product-specific)*
* **Qualification condition**: A condition on rule-based events; when the event payload does not satisfy it (for example, a required field is empty or missing), the event is received but discarded and the journey is not triggered
* **Rebalancing**: A backend auto-scaling operation in Adobe Journey Optimizer's microservices architecture that can cause the same event to be reprocessed by another service instance, creating a second log entry with a different `_id`

**Guardrails:**

* Events sent outside the journey's active date window are discarded silently with the log entry `DISPATCHER DISCARD #16 — unqualified on journey version enablements` and no UI error
* The journey runtime has an internal per-profile event stack limit of 10 events for a specific journey version; events beyond it are discarded with `maxInstanceStackEventsReached`. This is not a time-window or throughput limit
* The namespace in the **Profile Identifier** must match the namespace defined in the event schema exactly (case-sensitive); a mismatch causes a silent drop: the event is accepted and returns a success response, but the profile never enters the journey and no error is surfaced in the UI
* Overview dashboard metrics only include journeys that had traffic in the last 24 hours; allow up to 30 minutes for metrics to refresh after changes
* Only republished journeys correctly populate context fields in tracking URLs; a closed journey that was not republished after a relevant product change can show empty placeholders

**Terminology:**

* Canonical name: Journey Step Events — variants: journey step events, Journey Step Events dataset, step events
* Synonyms: "rebalancing" = "auto-scaling" (the backend operation that can create duplicate log entries)
* Do not confuse: entries with the same `_id` (duplicates at system level) ≠ entries with different `_id` values (separate log entries from the rebalancing scenario)
* Do not confuse: `sent` ≠ `delivered` — in Adobe Journey Optimizer Message Feedback Event datasets, `sent` is the relevant status for successful message delivery outcomes and the `delivered` value is not used

**FAQ:**

* **Q: Why are my events not entering a journey even though they are sent successfully?** — Check that the journey is in test mode or live, that the event was saved before copying the payload from the payload preview, that the payload has an event id and follows the streaming ingestion APIs payload structure, that the URL and the header key-value pairs (`X-gw-ims-org-id`, `Content-type`) are right, that the data types in the event condition match the event schema, and that the qualification condition is satisfied.
* **Q: Why does the journey fail to enable test mode with `ERR_MODEL_RULES_16`?** — Ensure the event used includes an identity namespace when using a channel action.
* **Q: Why do test profiles enter the journey but not advance past the initial step?** — The most common cause is a journey start date set in the future; events outside the active date window are discarded silently. Also check the test profile configuration and the identity namespace.
* **Q: What does `maxInstanceStackEventsReached` mean?** — The journey runtime has reached its internal per-profile event stack limit of 10 events for a specific journey version, because the profile's journey instance is blocked on a long-running step. Reduce long waits or slow steps, deduplicate or debounce upstream events, or split long-running scenarios into multiple journeys.
* **Q: I see duplicate rows in journey step events - is something wrong?** — No. Entries with the same `profileID`, `instanceID`, `nodeID`, and `requestID` but different `_id` values are expected system behavior from backend auto-scaling; the impact is limited to logging, and only one message is sent. Verify with `ajo_message_feedback_event_dataset`.
* **Q: Why do tracking URLs in emails show empty placeholders like `cid=em-acou-adob{}`?** — A context field such as `context.system.source.actionId` could not be resolved because the journey was closed and not republished after a relevant product change. Republish the journey, or remove the reference to the affected context field from the URL tracking parameters.
* **Q: Why does the Overview dashboard show different numbers than the Browse tab?** — Check that the journeys had traffic in the last 24 hours, that you have the access permissions to view all journeys in your organization, and allow up to 30 minutes for metrics to refresh.

**Related pages:**

* Troubleshooting errors before testing or publishing a journey: Troubleshoot errors before testing or publishing your journey (building-journeys/troubleshooting.md)
* Troubleshooting inbound actions: Troubleshoot inbound actions in journeys (building-journeys/troubleshooting-inbound.md)
* Understanding journey step events: Journey step events (reports/journey-step-events-overview.md)
* Journey error codes: Error codes reference (building-journeys/error-codes-reference.md)

+++

<!-- ai-section-version: 2 | source-hash: 1b156b07 -->
