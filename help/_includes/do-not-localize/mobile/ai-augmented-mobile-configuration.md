---
title: AI Knowledge Reference
---
# AI Knowledge Reference

+++ AI Knowledge Reference

This section contains structured knowledge intended to support interpretation, retrieval, and question answering related to this topic.

For complete understanding, this information should be combined with the documentation on this page. Neither source is intended to stand alone; the page describes the feature, while this section provides additional context that helps disambiguate terminology, intent, applicability, and constraints.

* **TL;DR:** This page explains how to configure your Journey Optimizer environment to send SMS, MMS, and RCS messages by integrating a provider such as Sinch, Twilio, or Infobip, creating a webhook, and setting up a mobile configuration.

**Intents:**

* Integrate a Mobile messaging provider (Sinch, Twilio, Infobip, or custom) with Journey Optimizer
* Create a webhook
* Create a Mobile configuration
* Understand the prerequisites for Mobile channel configuration
* View SMS usage metrics when you purchase SMS through Adobe Journey Optimizer

**Glossary:**

* **Provider**: A third-party service (Sinch, Twilio, or Infobip) that offers Mobile messaging services independent of Journey Optimizer *(product-specific)*
* **Custom provider configuration**: The configuration used to set up additional messaging providers beyond Sinch, Twilio, and Infobip *(product-specific)*
* **API Token and Service ID**: Provider credentials required to configure the connection between Journey Optimizer and the applicable provider *(product-specific)*
* **Mobile configuration**: The configuration created after provider integration and webhook creation to enable Mobile messaging *(product-specific)*
* **Manage SMS Subdomains permission**: The permission required on the production sandbox to access and edit SMS subdomains *(product-specific)*

**Guardrails:**

* Supported providers for Mobile messaging and MMS are Sinch, Twilio, and Infobip; additional messaging providers can be configured using the custom provider configuration.
* Prior to Mobile channel configuration, you must create an account with one of these providers to get your API Token and Service ID.
* Your use of Mobile messaging and MMS services is subject to additional terms and conditions from the applicable provider; Adobe does not control, and is not responsible for, third-party products.
* To access and edit SMS subdomains, you must have the Manage SMS Subdomains permission on the production sandbox.
* These steps must be performed by an Adobe Journey Optimizer System Administrator.
* SMS usage metrics are available only if you purchase SMS through Adobe Journey Optimizer, to reconcile MO and MT volume with vendor billing.

**Terminology:**

* Canonical name: Mobile configuration — Acronym: n/a — variants: SMS channel configuration
* Do not confuse: "provider integration" (Sinch, Twilio, Infobip) ≠ "custom provider configuration" (additional providers)

**FAQ:**

* **Q: Which providers does Journey Optimizer support for Mobile messaging?** — Sinch, Twilio, and Infobip; additional providers can be configured using the custom provider configuration.
* **Q: What do I need before configuring the Mobile channel?** — An account with one of the providers to obtain your API Token and Service ID.
* **Q: Who is allowed to perform the Mobile configuration steps?** — An Adobe Journey Optimizer System Administrator.
* **Q: What permission is required to edit SMS subdomains?** — The Manage SMS Subdomains permission on the production sandbox.
* **Q: How can I reconcile SMS volume with vendor billing?** — If you purchase SMS through Adobe Journey Optimizer, you can view SMS usage metrics to reconcile MO and MT volume with vendor billing.

+++

<!-- ai-section-version: 1 | source-hash: c0ff29d1 -->
