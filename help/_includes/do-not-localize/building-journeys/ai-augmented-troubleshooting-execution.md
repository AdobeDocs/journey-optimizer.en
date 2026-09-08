---
title: AI Knowledge Reference
---
# AI Knowledge Reference

+++ AI Knowledge Reference

This section contains structured knowledge intended to support interpretation, retrieval, and question answering related to this topic.

For complete understanding, this information should be combined with the documentation on this page. Neither source is intended to stand alone; the page describes the feature, while this section provides additional context that helps disambiguate terminology, intent, applicability, and constraints.

* **TL;DR:** This page is a comprehensive troubleshooting reference for live journey execution in Adobe Journey Optimizer, covering event delivery, profile entry failures, test mode transition issues, discarded events, duplicate step event logs, message delivery checks, and dashboard metric discrepancies.

**Intents:**
* Diagnose why events are not triggering journey entry by checking payload structure, headers, and qualification conditions
* Verify whether profiles are entering and progressing through a live or test-mode journey
* Resolve test mode transition failures caused by future start dates or misconfigured identity namespaces
* Understand and handle the `maxInstanceStackEventsReached` discard reason for blocked journey instances
* Identify and correctly query duplicate Journey Step Event log entries caused by backend auto-scaling
* Investigate missing messages by checking journey reporting and custom action call results
* Fix empty tracking URL placeholders in emails from closed journeys

**Glossary:**
* **Journey Step Events**: A dataset that logs each step a profile executes within a journey, used for reporting and debugging *(product-specific)*
* **notSuitableInitialEvent**: A discard code indicating an event was received but dropped because the qualification condition was not met *(product-specific)*
* **maxInstanceStackEventsReached**: A discard code indicating the per-profile journey instance event stack limit of 10 has been exceeded *(product-specific)*
* **isValidTransition**: A UI-only property in journey technical details; a null value may indicate a future start date or corrupted node connection, but does not affect backend processing *(product-specific)*
* **Qualification condition**: A rule defined on an event that must be satisfied for the event to trigger a journey; events failing this condition are discarded
* **Rebalancing**: A backend auto-scaling operation in AJO microservices that can create duplicate Journey Step Event log entries with different `_id` values

**Guardrails:**
* Events sent outside the journey's active date/time window are silently discarded with no error message
* The per-profile journey instance event stack limit is 10 events; exceeding this causes events to be discarded with `maxInstanceStackEventsReached`
* Duplicate Journey Step Event entries with different `_id` values are expected system behavior and do not indicate message duplication
* Dashboard Overview metrics only include journeys with traffic in the last 24 hours; metrics may take up to 30 minutes to refresh
* Closed journeys that have not been republished after a product change may produce empty placeholders in tracking URLs

**Terminology:**
* Canonical name: Journey Step Events — Acronym: none — variants: step events, journey execution logs
* Canonical name: Qualification condition — Acronym: none — variants: event qualification rule, event condition
* Synonyms: "rebalancing" = "auto-scaling" (backend operation causing duplicate log entries)
* Do not confuse: "duplicate `_id`" ≠ "duplicate log entries from rebalancing" — true duplicates share the same `_id`; rebalancing duplicates have different `_id` values

**FAQ:**
* **Q: Why are my events not triggering a journey even though they are being sent successfully?** — Check that the journey is live or in test mode, the payload matches the event schema structure, the qualification condition is satisfied, and the correct headers (`X-gw-ims-org-id`, `Content-type`) are included.
* **Q: Why do test profiles enter the journey but not advance past the first step?** — The most common cause is a journey start date set in the future; events are silently discarded outside the active date window. Also verify the test profile flag and identity namespace match.
* **Q: What does `maxInstanceStackEventsReached` mean?** — The journey runtime has hit the internal 10-event stack limit for a specific profile instance, typically because a long-running step is blocking processing. Reduce long waits, deduplicate upstream events, or split the scenario into multiple journeys.
* **Q: I see duplicate rows in Journey Step Events — is something wrong?** — No. Duplicate entries with different `_id` values are expected and result from backend auto-scaling. Only one message is actually sent; verify with the `ajo_message_feedback_event_dataset`.
* **Q: Why do tracking URLs in emails show empty placeholders like `cid=em-acou-adob{}`?** — The journey was closed and not republished after a product change; context fields cannot be resolved. Republish the journey or remove the affected context field reference from the URL tracking parameters.
* **Q: Why does the Overview dashboard show different numbers than the Browse tab?** — The dashboard only counts journeys with traffic in the last 24 hours, metrics take up to 30 minutes to refresh, and access permissions may limit visibility.

+++
