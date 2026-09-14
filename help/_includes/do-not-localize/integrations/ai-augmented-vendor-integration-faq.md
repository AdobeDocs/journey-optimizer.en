---
title: AI Knowledge Reference
---
# AI Knowledge Reference

+++ AI Knowledge Reference

This section contains structured knowledge intended to support interpretation, retrieval, and question answering related to this topic.

For complete understanding, this information should be combined with the documentation on this page. Neither source is intended to stand alone; the page describes the feature, while this section provides additional context that helps disambiguate terminology, intent, applicability, and constraints.

* **TL;DR:** This page answers frequently asked questions about Integrations in Adobe Journey Optimizer, covering configuration, authentication, supported channels and formats, API patterns, permissions, and troubleshooting.

**Intents:**

* Understand what Integrations do and who configures versus uses them
* Learn how administrators configure and marketers add an integration to message content
* Determine which channels, response formats, and API patterns are supported
* Find the permissions required to configure Integrations
* Troubleshoot a failing test connection or an integration missing from the marketer picker

**Glossary:**

* **Integrations**: Feature that connects external data sources so you can pull content and data from third-party systems into campaigns and journeys and personalize messages *(product-specific)*
* **Add personalization**: Action on a Text or HTML component that marketers use to open Integrations, choose an active integration, and map attributes *(product-specific)*
* **Pills mode**: Personalization editor mode used to map values to variables in the configuration, such as header or query parameters or path variables in the URL *(product-specific)*
* **Retrieval APIs**: APIs that target specific content, which are supported for this integration model *(product-specific)*
* **Listing APIs**: Broad list or pagination patterns, which are not supported for this integration model *(product-specific)*

**Guardrails:**

* Outbound channels are supported (for example email, SMS, and push).
* For API call responses, JSON and HTML are supported for field mapping; raw binary image output and formats that are not JSON are not available.
* Retrieval APIs that target specific content are supported; Listing APIs (broad list or pagination patterns) are not supported.
* To configure Integrations, users need the Manage AJO integration configuration and View AJO integration configuration permissions.
* Only active integrations appear when marketers open Integrations; the integration must be activated after a successful test.
* Supported authentication types: No Authentication, API key, Basic Auth, and OAuth 2.0.
* The Integrations feature is supported in Fragments.

**Terminology:**

* Canonical name: Integrations — Acronym: n/a — variants: external integrations, third-party integrations
* Synonyms: administrators "create and activate the technical configuration" = the setup marketers later select via "Add personalization"
* Do not confuse: "Integrations" (personalization fields in message content driven from APIs) ≠ "Sources" (Experience Platform data ingestion, such as batch ingestion and profile enrichment)
* Do not confuse: "Retrieval" APIs (supported) ≠ "Listing" APIs (not supported)

**FAQ:**

* **Q: Which channels support Integrations?** — Outbound channels (for example email, SMS, and push).
* **Q: Which API response formats are supported?** — JSON and HTML; raw binary image output and non-JSON formats are not available.
* **Q: Which API patterns can I connect to?** — Retrieval APIs that target specific content; Listing (broad list or pagination) APIs are not supported.
* **Q: Can I use Integrations in reusable fragments?** — Yes, the feature is supported in Fragments.
* **Q: Do Integrations replace Experience Platform Sources?** — No; Integrations drive personalization fields from APIs, while Sources handle data ingestion such as batch ingestion and profile enrichment.
* **Q: Why do marketers not see my integration in the picker?** — Integrations must be activated after a successful test; only active integrations appear.

+++

<!-- ai-section-version: 1 | source-hash: 4494376d -->
