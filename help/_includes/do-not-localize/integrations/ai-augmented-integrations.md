---
title: AI Knowledge Reference
---
# AI Knowledge Reference

+++ AI Knowledge Reference

This section contains structured knowledge intended to support interpretation, retrieval, and question answering related to this topic.

For complete understanding, this information should be combined with the documentation on this page. Neither source is intended to stand alone; the page describes the feature, while this section provides additional context that helps disambiguate terminology, intent, applicability, and constraints.

* **TL;DR:** This page explains how administrators configure, test, activate, and manage external integrations that connect Adobe Journey Optimizer to third-party APIs to pull JSON or HTML content for personalized, dynamic content in outbound channels.

**Intents:**

* Assign the Manage and View AJO integration configuration permissions
* Create an integration by defining URL, path template, HTTP method, headers, query parameters, authentication, and policy configuration
* Validate an endpoint with Send test connection before activating
* Map a sample JSON response and expose selected fields for personalization
* Understand send-time limits, throttling, cache, retry, and message validity behavior
* Update or archive an existing integration and review where it is used with Explore references

**Glossary:**

* **Integrations**: Feature that links Journey Optimizer to third-party systems to surface external data and composable content during authoring and at send time *(product-specific)*
* **Path Template**: Configuration of Name and Default value for each `{{placeholder}}` added in the URL; the Name is a marketer-facing label in the editor only and is not sent on the API request *(product-specific)*
* **Policy configuration**: Settings for API requests including Timeout, throttling, cache, and retry *(product-specific)*
* **Response payload**: Field that defines the expected response for authoring; marketers may reference only exposed fields, and tokens for other paths fail validation in the editor *(product-specific)*
* **Send test connection**: Action that validates the endpoint URL, authentication, and request structure against the target API prior to activation *(product-specific)*
* **Explore references**: Menu used to review usage of a configuration, including journeys and campaigns that depend on it *(product-specific)*
* **MessageValidityExclusion**: Event emitted when a queued message sits past its validity window (TTL) and is discarded *(product-specific)*

**Guardrails:**

* This integration feature is restricted to outbound channels (Email, SMS, and Push) and supports pulling JSON or HTML.
* Users need the **Manage AJO integration configuration** and **View AJO integration configuration** permissions.
* The **Name** field cannot contain spaces.
* With throttling enabled, supported rates are 50 to 5000 TPS; limits apply to the integration, not each API endpoint.
* With retry enabled, other failures retry three times by default, with 200 ms, 400 ms, and 800 ms between attempts.
* For mandatory Variable parameters, if no value is resolved at runtime and no default is provided, request generation fails with an error and the outbound API call is not made.
* At send time, responses may be up to 4 MB by default; anything larger is treated as an integration error, and retries are not attempted when the failure is caused by response size.
* If cache is enabled, only successful responses are stored and reused until the cache TTL expires; failed responses are never cached.
* Update applies only to Authentication details and Policy configuration, and those updates apply to live journeys and campaigns.

**Terminology:**

* Canonical name: Integrations — Acronym: n/a — variants: external integrations, AJO integration configuration
* Synonyms: "Manage" (from the Integrations card) = entry point to "Create Integration"
* Do not confuse: "Send test connection" (validates the configuration before activation) ≠ "Activate" (makes the integration usable by marketers)
* Do not confuse: "Update" (changes Authentication and Policy configuration only) ≠ "Archive" (archives an integration configuration)

**FAQ:**

* **Q: Which channels and formats does this feature support?** — It is restricted to outbound channels (Email, SMS, and Push) and supports pulling JSON or HTML.
* **Q: What permissions are required?** — The Manage AJO integration configuration and View AJO integration configuration permissions.
* **Q: What throttling rates are supported?** — With throttling enabled, 50 to 5000 TPS, applied to the integration rather than each API endpoint.
* **Q: What happens if a send-time response is too large?** — Responses over 4 MB by default are treated as an integration error, and retries are not attempted when the failure is caused by response size.
* **Q: What can I change on an active integration?** — Only Authentication details and Policy configuration; those updates apply to live journeys and campaigns.
* **Q: What is a MessageValidityExclusion event?** — It is emitted when a queued message sits past its validity window (TTL) and the system discards it.

+++

<!-- ai-section-version: 1 | source-hash: d880cd5e -->
