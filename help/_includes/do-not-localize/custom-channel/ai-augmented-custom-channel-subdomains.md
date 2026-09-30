---
title: AI Knowledge Reference
---
# AI Knowledge Reference

+++ AI Knowledge Reference

This section contains structured knowledge intended to support interpretation, retrieval, and question answering related to this topic.

For complete understanding, this information should be combined with the documentation on this page. Neither source is intended to stand alone; the page describes the feature, while this section provides additional context that helps disambiguate terminology, intent, applicability, and constraints.

* **TL;DR:** This page explains how to configure a custom channel subdomain in Journey Optimizer to enable link tracking in custom channel messages, either by using a subdomain already delegated to Adobe or by configuring a new subdomain with a DNS record.

**Intents:**

* Set up a custom channel subdomain to enable link tracking in custom channel messages
* Use a subdomain that is already delegated to Adobe as a custom channel subdomain
* Configure a new subdomain by generating the matching DNS record on your domain-hosting solution
* Understand subdomain statuses during processing and validation
* Prepare a subdomain to select when creating a custom channel configuration

**Glossary:**

* **Custom channel subdomain**: The subdomain you set up and then select when creating a custom channel configuration, used to enable link tracking in custom channel messages *(product-specific)*
* **Prefix**: The value that displays in your custom channel URL and is combined with a delegated subdomain to create a unique subdomain; only alpha-numeric characters and hyphens are allowed *(product-specific)*
* **Use delegated subdomain**: The Configuration type option for using a subdomain already delegated to Adobe *(product-specific)*
* **Add your own domain**: The Configuration type option for configuring a new subdomain to delegate *(product-specific)*
* **CNAME method**: A subdomain delegation method; a subdomain delegated with this method requires you to create the DNS record on your hosting platform *(product-specific)*

**Guardrails:**

* Custom channel subdomain configuration is shared between all environments, so any modification to a custom channel subdomain also impacts other production sandboxes.
* Do not use `cdn` or `data` prefixes as these are reserved for internal use; other restricted or reserved prefixes such as `dmarc` or `spf` should also be avoided.
* You cannot select a subdomain that is already used as a custom channel subdomain, and you cannot use an existing custom channel subdomain when adding your own domain.
* Capital letters are not allowed in subdomains, and delegating an invalid subdomain to Adobe is not allowed; the subdomain must be valid and owned by your organization.
* Multi-level subdomains of the same parent domain are supported (for example, custom.marketing.yourcompany.com).
* After submission, Adobe performs the required checks, which can take up to 4 hours before the subdomain can be used to send messages.
* If you select a domain that was delegated to Adobe using the CNAME method, you must create the DNS record on your hosting platform.
* When you configure a new custom channel subdomain, it always points to a CNAME record.

**Terminology:**

* Canonical name: Custom channel subdomain — Acronym: n/a — variants: custom channel subdomain configuration
* Synonyms: "Use delegated subdomain" = using a subdomain already delegated to Adobe; "Add your own domain" = configuring a new subdomain
* Do not confuse: "Processing" (status shown after submission while checks run) ≠ "Success" (status once checks are successful and the subdomain is ready to use) ≠ "Failed" (status if you fail to create the validation record on your hosting solution)

**FAQ:**

* **Q: Why do I need a custom channel subdomain?** — You must set up a subdomain to enable link tracking in your custom channel messages, and you select it when creating a custom channel configuration.
* **Q: What are the two ways to set up a custom channel subdomain?** — You can use a subdomain that is already delegated to Adobe (Use delegated subdomain), or configure a new subdomain by adding your own domain and generating the matching DNS record.
* **Q: How long does subdomain validation take?** — After submission the subdomain shows the Processing status, and Adobe performs the required checks, which can take up to 4 hours before you can use it to send messages.
* **Q: Which prefixes are not allowed?** — Do not use `cdn` or `data` prefixes because they are reserved for internal use, and avoid other restricted or reserved prefixes such as `dmarc` or `spf`.
* **Q: Does a change to a custom channel subdomain affect other sandboxes?** — Yes, custom channel subdomain configuration is shared between all environments, so any modification also impacts other production sandboxes.
* **Q: What happens if the DNS validation record is not created?** — The subdomain is marked as Failed if you fail to create the validation record on your hosting solution.

+++

<!-- ai-section-version: 1 | source-hash: df29dbf8 -->
