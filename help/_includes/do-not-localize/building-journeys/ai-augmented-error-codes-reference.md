---
title: AI Knowledge Reference
---
# AI Knowledge Reference

+++ AI Knowledge Reference

This section contains structured knowledge intended to support interpretation, retrieval, and question answering related to this topic.

For complete understanding, this information should be combined with the documentation on this page. Neither source is intended to stand alone; the page describes the feature, while this section provides additional context that helps disambiguate terminology, intent, applicability, and constraints.

* **TL;DR:** This page is a reference guide to standardized Adobe Journey Optimizer error codes organized by service prefix, explaining each error's root cause and providing step-by-step resolution guidance.

**Intents:**

* Identify which AJO service generated an error using the service prefix in the error code
* Diagnose and resolve push and transport service errors (CJMPTS) that occur during push notification delivery and message transport operations
* Troubleshoot Journey Runtime and API errors (CJMRT) that occur during journey execution, event processing, and API operations
* Fix message authoring service errors (CJMMAS) that occur when creating, editing, or publishing messages, presets, and content
* Resolve campaign errors (CJMCMP) that occur during campaign creation, configuration, and activation
* Escalate persistent errors to Adobe Support with the correct information

**Glossary:**

* **Service prefix**: The part of an AJO error code that indicates which Adobe Journey Optimizer service generated the error (for example, CJMRT = Journey Runtime) *(product-specific)*
* **Error number**: The part of an AJO error code that is the unique identifier for the specific error condition *(product-specific)*
* **HTTP status code**: The standard HTTP status code that ends an AJO error code (for example, 400, 403, 422, 500)
* **Request ID**: An identifier that can accompany an error; the page says to note it with the complete error code because it is essential for troubleshooting and support escalation *(product-specific)*
* **CJMPTS**: Push/Transport Service prefix, for errors during push notification delivery and message transport operations *(product-specific)*
* **CJMRT**: Journey Runtime prefix, for errors during journey execution, event processing, and API operations *(product-specific)*
* **CJMMAS**: Message Authoring Service prefix, for errors when creating, editing, or publishing messages, presets, and content *(product-specific)*
* **CJMCMP**: Campaign prefix, for errors during campaign creation, configuration, and activation *(product-specific)*
* **CJMTL**: Transport Layer prefix, for errors during message transport and delivery operations *(product-specific)*
* **CJMRPS**: Reporting/Provisioning Service prefix, for errors during reporting configuration and dataset provisioning operations *(product-specific)*

**Guardrails:**

* Email variants must include an opt-out/unsubscribe link; a missing link produces CJMMAS-2001-200 (success status with an error banner).
* DNS propagation can take up to 72 hours; the page lists this as the time to allow for CJMRT-080608-400.

**Terminology:**

* Canonical name: Error code — variants: error number (the unique identifier part of the code)
* Do not confuse: CJMPTS (Push/Transport Service) ≠ CJMTL (Transport Layer) — they are separate service prefixes with separate error sections
* Do not confuse: "400 (Bad Request)" ≠ "422 (Unprocessable Entity)" — the page advises to review input data and configuration for 400, and to validate data against schema requirements for 422

**FAQ:**

* **Q: How do I know which AJO service caused an error?** — Read the service prefix at the start of the error code: CJMPTS (Push/Transport Service), CJMRT (Journey Runtime), CJMMAS (Message Authoring Service), CJMCMP (Campaign), CJMTL (Transport Layer), CJMRPS (Reporting/Provisioning Service).
* **Q: What should I do when I get a 500-series error?** — Retry after a short delay. If the error persists after following the resolution steps, contact Adobe Support with the complete error code, request ID (if available), steps to reproduce, and relevant configuration details.
* **Q: Why does CJMMAS-2001-200 show an error banner even though the status is "success"?** — A required unsubscribe link is missing in an email variant; add the opt-out/unsubscribe link to all email variants and ensure it is present in every language version.
* **Q: What information should I gather before contacting Adobe Support?** — Collect the error code, request ID, timestamps, and steps to reproduce.
* **Q: What causes CJMRT-030012-422?** — Invalid input data (for example, a nonexistent audience, event, or attribute); verify that referenced objects (audiences, datasets) exist and are active.

**Related pages:**

* Troubleshooting errors before testing or publishing a journey: Troubleshoot errors before testing or publishing your journey (building-journeys/troubleshooting.md)
* Troubleshooting a live journey execution: Troubleshoot your live journey execution (building-journeys/troubleshooting-execution.md)
* Troubleshooting inbound actions: Troubleshoot inbound actions in journeys (building-journeys/troubleshooting-inbound.md)
* Troubleshooting custom actions: Troubleshoot your custom actions (action/troubleshoot-custom-action.md)
* Journey questions: Journey Orchestration - Frequently Asked Questions (building-journeys/journey-faq.md)
* Limits and constraints: Journey Optimizer guardrails and limitations (start/guardrails.md)

+++

<!-- ai-section-version: 1 | source-hash: 2696b3f6 -->
