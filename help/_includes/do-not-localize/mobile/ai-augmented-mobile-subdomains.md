---
title: AI Knowledge Reference
---
# AI Knowledge Reference

+++ AI Knowledge Reference

This section contains structured knowledge intended to support interpretation, retrieval, and question answering related to this topic.

For complete understanding, this information should be combined with the documentation on this page. Neither source is intended to stand alone; the page describes the feature, while this section provides additional context that helps disambiguate terminology, intent, applicability, and constraints.

* **TL;DR:** This page explains how to set up SMS subdomains in Adobe Journey Optimizer to shorten URLs in messages, either by using a subdomain already delegated to Adobe or by configuring a new subdomain with a DNS record.

**Intents:**

* Set up an SMS subdomain used when creating an SMS configuration
* Use a subdomain that is already delegated to Adobe
* Configure a new subdomain by generating the matching DNS record
* Understand subdomain statuses and validation timing
* Undelegate an SMS subdomain through your Adobe representative

**Glossary:**

* **SMS subdomain**: The subdomain used to shorten URLs added to SMS, RCS, and MMS messages, selected when creating an SMS configuration *(product-specific)*
* **Use delegated subdomain**: Configuration type that reuses a subdomain already delegated to Adobe *(product-specific)*
* **Add your own domain**: Configuration type used to delegate and configure a new subdomain *(product-specific)*
* **CNAME method**: Delegation approach where the subdomain points to a CNAME record and a DNS record must be created on your hosting platform *(product-specific)*
* **Manage SMS Subdomains permission**: The permission required on the production sandbox to access and edit SMS subdomains *(product-specific)*

**Guardrails:**

* SMS subdomain configuration is shared between all environments, so any modification to an SMS subdomain also impacts other production sandbox.
* The Manage SMS Subdomains permission on the production sandbox is required to access and edit SMS subdomains.
* Subdomain prefixes may use only alpha-numeric characters and hyphens; the cdn and data prefixes are reserved for internal use, and prefixes such as dmarc or spf should be avoided.
* Capital letters are not allowed in subdomains.
* A subdomain that is already used as an SMS subdomain cannot be selected or reused.
* If you select a domain delegated using the CNAME method, you must create the DNS record on your hosting platform.
* Adobe performs required checks that can take up to 4 hours before a subdomain can be used to send messages.
* A new SMS subdomain always points to a CNAME record.
* The Journey Optimizer user interface does not support deletion or undelegation of SMS subdomains once they have been set up; contact your Adobe representative for removal or undelegation.
* Multi-level subdomains of the same parent domain are supported.

**Terminology:**

* Canonical name: SMS subdomain — Acronym: n/a — variants: SMS/RCS/MMS subdomain
* Do not confuse: "Use delegated subdomain" (reuse a subdomain already delegated to Adobe) ≠ "Add your own domain" (delegate and configure a new subdomain)
* Do not confuse: "Processing" (checks in progress) ≠ "Success" (checks successful, ready to create SMS channel configurations) ≠ "Failed" (validation record was not created on your hosting solution)

**FAQ:**

* **Q: Why do I need an SMS subdomain?** — You must set up the subdomain to shorten URLs added to your SMS, RCS, and MMS messages and to select it when creating an SMS configuration.
* **Q: How long does subdomain validation take?** — Adobe performs the required checks, which can take up to 4 hours, before the subdomain can be used to send messages.
* **Q: Can I delete an SMS subdomain from the interface?** — No. The user interface does not support deletion or undelegation once a subdomain has been set up; contact your Adobe representative for assistance.
* **Q: Does a change to an SMS subdomain affect other sandboxes?** — Yes. SMS subdomain configuration is shared between all environments, so any modification also impacts other production sandbox.
* **Q: What does the Failed status mean?** — The subdomain is marked as Failed if you fail to create the validation record on your hosting solution.

+++

<!-- ai-section-version: 1 | source-hash: 08d982b2 -->
