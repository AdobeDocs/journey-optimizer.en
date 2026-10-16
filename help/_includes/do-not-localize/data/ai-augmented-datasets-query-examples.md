---
title: AI Knowledge Reference
---
# AI Knowledge Reference

+++ AI Knowledge Reference

This section contains structured knowledge intended to support interpretation, retrieval, and question answering related to this topic.

For complete understanding, this information should be combined with the documentation on this page. Neither source is intended to stand alone; the page describes the feature, while this section provides additional context that helps disambiguate terminology, intent, applicability, and constraints.

* **TL;DR:** This page provides ready-to-use SQL query examples for Journey Optimizer system datasets so you can analyze email and push tracking, message feedback, journey step, decisioning, BCC, and entity data for reporting and troubleshooting.

**Intents:**

* Choose the correct system dataset for a given analysis (message feedback versus email tracking versus journey step).
* Query email interaction counts (opens, clicks) and see the push tracking query examples.
* Query message delivery feedback statuses (`sent`, `bounce`) and bounce categories.
* Distinguish test executions from non-test executions using the `isTestExecution` field.
* Join the Entity Dataset with feedback and tracking datasets using `messageID` or `correlationID`.
* Troubleshoot the "Table not provisioned for dataset" message.

**Glossary:**

* **AJO Email Tracking Experience Event Dataset**: system dataset for email tracking events; queried as `ajo_email_tracking_experience_event_dataset` *(product-specific)*
* **AJO Message Feedback Event Dataset**: message delivery feedback across channels (Email, SMS/RCS/MMS, Direct Mail); queried as `ajo_message_feedback_event_dataset`; uses batch ingestion *(product-specific)*
* **AJO Push Tracking Experience Event Dataset**: mobile tracking experience events for push; queried as `ajo_push_tracking_experience_event_dataset` *(product-specific)*
* **Journey Step Event**: journey step events; queried as `journey_step_events` *(product-specific)*
* **Decisioning Event Dataset (ODE DecisionEvents)**: dataset for ingesting offer propositions to the users *(product-specific)*
* **Secondary Recipient Feedback Event Dataset (BCC)**: email BCC events when BCC archiving is enabled; table may still be named `ajo_bcc_feedback_event_dataset` *(product-specific)*
* **Entity Dataset**: stores entity metadata for messages; queried as `ajo_entity_dataset` *(product-specific)*
* **`isTestExecution`**: field distinguishing test executions (`true`) from non-test executions (`false`), with `NULL` or missing treated as unknown *(product-specific)*

**Guardrails:**

* The AJO Message Feedback Event Dataset uses batch ingestion; data may be delayed by up to 2 hours.
* If a query returns "Table not provisioned for dataset", for batch-ingested datasets allow up to two hours for data to become available before contacting Adobe Support.
* The CJM Consent Service Dataset and CJM Push Profile Dataset are system datasets used by Journey Optimizer for consent and push profile data. They are not available as queryable tables in Query Service, so a "Table not provisioned for dataset" response is expected when querying them.
* System datasets are hidden by default; enable **Show system datasets** in the Datasets workspace to see them.
* An Entity Dataset entry for a message is created only after the journey or campaign is published, and you may see the entry 30 minutes after the publication of the campaign or journey.
* Do not automatically convert a `NULL` or missing `isTestExecution` value to `false`, and do not assume that every null value represents a production execution.
* In some journeys, `messageID` may not be unique for each individual delivery; to track events at the individual send level, combine `journeyVersionID`, `journeyActionID`, and `batchInstanceID` (for batch journeys) or `identityMap` fields.
* A successful custom action HTTP call confirms only that the call completed, not that the external system delivered a message.

**Terminology:**

* Canonical name: Journey Step Event — table: `journey_step_events`
* Do not confuse: "AJO Message Feedback Event Dataset" (delivery feedback such as `sent` or `bounce`) ≠ "AJO Email Tracking Experience Event Dataset" (interaction events such as opens and clicks) ≠ "Journey Step Event" (custom action execution status, latency, and error details)
* Do not confuse: "`isTestExecution` = `NULL`" (unknown) ≠ "`isTestExecution` = `false`" (non-test execution)

**FAQ:**

* **Q: Which dataset do I query for opens and clicks?** — The AJO Email Tracking Experience Event Dataset.
* **Q: Which dataset do I query for sent and bounce delivery status?** — The AJO Message Feedback Event Dataset.
* **Q: Why does my query return "Table not provisioned for dataset"?** — It does not necessarily mean provisioning failed; enable Show system datasets, confirm the table name matches the Datasets workspace, and for batch datasets allow up to two hours for data to become available.
* **Q: Why does a query for the CJM Consent Service Dataset or CJM Push Profile Dataset return "Table not provisioned for dataset"?** — These system datasets are not available as queryable tables in Query Service, so the response is expected.
* **Q: How do I separate test executions from non-test executions?** — Use the `isTestExecution` field; treat `NULL` or missing values as unknown rather than converting them to `false`.
* **Q: How do I get marketer-defined metadata for messages in reporting?** — Use the Entity Dataset, which uses the `messageID` attribute to stitch datasets such as the Message Feedback Dataset and Experience Event Tracking Datasets; to sort emails sent by a journey by action, join the Message Feedback dataset with the Entity dataset using `_experience.decisioning.propositions.scopeDetails.correlationID` and the `_id` field in the Entity dataset.

+++

<!-- ai-section-version: 1 | source-hash: 746bd4a0 -->
