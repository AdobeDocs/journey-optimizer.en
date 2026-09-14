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
* Diagnose and resolve push/transport errors (CJMPTS) affecting message delivery
* Troubleshoot journey runtime and API errors (CJMRT) during journey execution or event processing
* Fix message authoring errors (CJMMAS) when creating, saving, or publishing messages
* Resolve campaign errors (CJMCMP) during campaign activation or approval
* Escalate persistent errors to Adobe Support with the correct information

**Glossary:**

* **Service prefix**: The alphanumeric code at the start of an AJO error code that identifies which service generated the error (e.g., CJMRT = Journey Runtime) *(product-specific)*
* **HTTP status code**: The standard status code embedded in an AJO error code (e.g., 400 = Bad Request, 403 = Forbidden, 422 = Unprocessable Entity, 500 = Internal Server Error)
* **Request ID**: A unique identifier accompanying an error that is required when escalating to Adobe Support *(product-specific)*
* **CJMRT**: Journey Runtime service prefix — errors during journey execution and API operations *(product-specific)*
* **CJMMAS**: Message Authoring Service prefix — errors during message creation and publishing *(product-specific)*
* **CJMPTS**: Push/Transport Service prefix — errors during push notification and message transport *(product-specific)*

**Guardrails:**

* Email variants must include an opt-out/unsubscribe link; omitting it triggers CJMMAS-2001-200.
* Stopping a journey requires the Manage journeys permission (relevant to CJMRT errors involving permissions).
* DNS propagation for subdomain delegation can take up to 72 hours (relevant to CJMRT-080608-400).
* Lookup keys for dataset lookup activities must be defined in advanced mode, not simple mode.

**Terminology:**

* Canonical name: Error code — Acronym: n/a — variants: error message, error identifier
* Synonyms: "service prefix" = "error prefix" = "component identifier"
* Do not confuse: "400 Bad Request" ≠ "422 Unprocessable Entity" — 400 indicates malformed input; 422 indicates valid format but invalid content per schema rules

**FAQ:**

* **Q: How do I know which AJO service caused an error?** — Read the service prefix at the start of the error code: CJMPTS (push/transport), CJMRT (journey runtime), CJMMAS (message authoring), CJMCMP (campaign), CJMTL (transport layer), CJMRPS (reporting/provisioning).
* **Q: What should I do when I get a 500-series error?** — Retry after a few minutes, check Adobe Status for outages, then escalate to Adobe Support with the full error code and request ID if the issue persists.
* **Q: Why does CJMMAS-2001-200 show an error banner even though the status is "success"?** — A required opt-out/unsubscribe link is missing from an email variant; add it to all variants and language versions.
* **Q: What information should I gather before contacting Adobe Support?** — Collect the complete error code, request ID, timestamps, steps to reproduce, and any relevant configuration details.
* **Q: What causes CJMRT-030012-422?** — Invalid input data such as referencing a non-existent audience, event, or attribute; verify all referenced objects exist and are active.

+++
