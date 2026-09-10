---
title: AI Knowledge Reference
---
# AI Knowledge Reference

+++ AI Knowledge Reference

This section contains structured knowledge intended to support interpretation, retrieval, and question answering related to this topic.

For complete understanding, this information should be combined with the documentation on this page. Neither source is intended to stand alone; the page describes the feature, while this section provides additional context that helps disambiguate terminology, intent, applicability, and constraints.

* **TL;DR:** This page explains how to enable and configure the List-Unsubscribe header so recipients can opt out from their inbox using a Mailto (unsubscribe) address or a one-click unsubscribe URL, including the Adobe managed and Customer managed options and the decrypt API for external consent systems.

**Intents:**

* Enable the List-Unsubscribe header in an email channel configuration
* Configure the Mailto (unsubscribe) address and the One-click unsubscribe URL options
* Set the Consent level to channel or profile identity
* Manage unsubscribe data externally with the Customer managed option
* Configure the decrypt API to retrieve encrypted consent parameters for custom endpoints
* Append custom attributes to unsubscribe endpoints using URL tracking parameters

**Glossary:**

* **List-Unsubscribe header**: An email header that lets recipients opt out directly from their inbox; enabled via the Enable List-Unsubscribe option, on by default *(product-specific)*
* **Mailto (unsubscribe)**: The destination address where unsubscribe requests are routed for auto-processing, based on the selected subdomain *(product-specific)*
* **One-click unsubscribe URL**: The one-click opt-out URL generated for the List unsubscribe header, based on the selected subdomain *(product-specific)*
* **Consent level**: A setting, specific to the channel or to the profile identity, that determines whether consent updates at channel level or ID level *(product-specific)*
* **Adobe managed / Customer managed**: Options defining whether consent data is managed within the Adobe system, or in an external system with no automatic synchronization to Adobe *(product-specific)*
* **decrypt API**: An API on Adobe Developer used by an external consent system to decrypt the encrypted parameters sent by Adobe to custom endpoints *(product-specific)*

**Guardrails:**

* The Enable List-Unsubscribe option is enabled by default; its two options (Mailto and One-click unsubscribe URL) are enabled by default unless one or both are unchecked.
* To display the one-click unsubscribe URL in the email header, the recipients' email client must support this feature.
* The One-click Unsubscribe URL must use the POST request method.
* With the Customer managed option, Adobe does not store any unsubscribe or consent data; there is no auto synchronization, and the organization must initiate any data transfer to push consent data back into [!DNL Journey Optimizer].
* Appending custom attributes to endpoints is available in Limited Availability (contact your Adobe representative to gain access).
* Starting October 2025, Customer managed Mailto (unsubscribe) with custom attributes requires the new emailParamsSub and emailParamsBody query parameters instead of emailParams.
* [!DNL Journey Optimizer] does not append a specific tag to unsubscribe events triggered by the List unsubscribe feature; differentiating these clicks requires custom external tagging or an external landing page.
* The order of UTM parameters appended to the URL is random and cannot be controlled; systems requiring a specific order must parse and reorder them.
* By default the consent field value is empty and treated as consent to receive communications.

**Terminology:**

* Canonical name: List-Unsubscribe header — Acronym: n/a — variants: List unsubscribe, one-click list unsubscribe URL
* Synonyms: "One-click unsubscribe URL" = "One-click opt-out URL" (when a one-click opt-out link inserted in the email body is picked up as the header value)
* Do not confuse: "Mailto (unsubscribe)" (routes an unsubscribe request to an address for auto-processing) ≠ "One-click unsubscribe URL" (directly opts the recipient out on click)
* Do not confuse: "Adobe managed" (consent data managed within the Adobe system) ≠ "Customer managed" (consent data managed in an external system, no auto synchronization)

**FAQ:**

* **Q: Is the List-Unsubscribe header on by default?** — Yes; the Enable List-Unsubscribe option is enabled by default, and both the Mailto and One-click unsubscribe URL methods are enabled by default unless unchecked.
* **Q: Which methods should I enable?** — Adobe recommends enabling both Mailto (unsubscribe) and One-click unsubscribe URL, since not all email clients support the HTTP method; also add a one-click opt-out or unsubscribe link in the email body.
* **Q: What request method must a custom one-click unsubscribe URL use?** — It must be a POST URL.
* **Q: What happens to consent data with the Customer managed option?** — Adobe stores no unsubscribe or consent data; there is no automatic synchronization, and you must initiate any transfer of consent data back into [!DNL Journey Optimizer].
* **Q: Can I tell List unsubscribe clicks apart from other unsubscribe actions?** — Not by a built-in tag; [!DNL Journey Optimizer] does not append a specific tag, so you must implement custom tagging externally or use an external landing page for tracking.

+++

<!-- ai-section-version: 1 | source-hash: 8baef234 -->
