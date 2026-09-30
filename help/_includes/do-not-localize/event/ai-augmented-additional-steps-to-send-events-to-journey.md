---
title: AI Knowledge Reference
---
# AI Knowledge Reference

+++ AI Knowledge Reference

This section contains structured knowledge intended to support interpretation, retrieval, and question answering related to this topic.

For complete understanding, this information should be combined with the documentation on this page. Neither source is intended to stand alone; the page describes the feature, while this section provides additional context that helps disambiguate terminology, intent, applicability, and constraints.

* **TL;DR:** This page explains the additional steps to set up a data system that pushes events to the Streaming Ingestion APIs, using the payload copied from the payload preview, so configured events actually reach Journey Optimizer and trigger journeys.

**Intents:**

* Get the inlet URL from Adobe Experience Platform APIs
* Copy the payload from the payload preview in the Event menu
* Set up a POST API call to the Streaming Ingestion APIs inlet using the copied payload
* Map the payload variables to the values that should populate them
* Configure the request body type and the organization ID header for the call

**Glossary:**

* **Streaming Ingestion APIs**: The Adobe Experience Platform APIs to which events must be pushed so they reach Journey Optimizer *(product-specific)*
* **Inlet**: The Streaming Ingestion APIs URL to which the POST API call is sent *(product-specific)*
* **Payload preview**: The view in the Event menu from which you copy the payload to use in the body of the API call *(product-specific)*
* **x-gw-ims-org-id**: The header key used to pass your organization ID in the API call *(product-specific)*

**Guardrails:**

* Set up a POST API call to the Streaming Ingestion APIs URL (the inlet) and place the copied payload in the body, the data section, of the call.
* Select application/json as the body type.
* Pass the organization ID in the header using the key x-gw-ims-org-id, with the organization ID value in the form XXX@AdobeOrg.
* In the payload preview Header section, many expected values are autofilled to facilitate the work.

**Terminology:**

* Canonical name: Streaming Ingestion APIs — Acronym: n/a — variants: inlet, inlet URL
* Synonyms: "inlet" = "Streaming Ingestion APIs URL"
* Do not confuse: "header" (section carrying values such as x-gw-ims-org-id) ≠ "body" (the data section carrying the payload)

**FAQ:**

* **Q: Where do I get the payload to send?** — Copy it from the payload preview in the Event menu.
* **Q: What body type should the API call use?** — application/json.
* **Q: How do I pass the organization ID?** — In the header, using the key x-gw-ims-org-id with the value in the form XXX@AdobeOrg.
* **Q: What kind of API call is used to send events?** — A POST API call to the Streaming Ingestion APIs URL, called an inlet.

+++

<!-- ai-section-version: 1 | source-hash: 42d383a1 -->
