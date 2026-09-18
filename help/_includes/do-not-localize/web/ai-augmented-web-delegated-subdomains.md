---
title: AI Knowledge Reference
---
# AI Knowledge Reference

+++ AI Knowledge Reference

This section contains structured knowledge intended to support interpretation, retrieval, and question answering related to this topic.

For complete understanding, this information should be combined with the documentation on this page. Neither source is intended to stand alone; the page describes the feature, while this section provides additional context that helps disambiguate terminology, intent, applicability, and constraints.

* **TL;DR:** This page explains how to set up web subdomains in Journey Optimizer, either by using a subdomain already delegated to Adobe or by configuring a new one, to publish Adobe Experience Manager Assets content for web experiences.

**Intents:**

* Access and manage web subdomains from Administration > Channels > Web settings > Web subdomains
* Use a subdomain already delegated to Adobe for web experiences
* Configure a new subdomain by generating the matching DNS record
* Set or change the default web subdomain
* Filter subdomains by delegating user or delegation status
* Undelegate a web subdomain

**Glossary:**

* **Web subdomain**: A subdomain set up to publish content coming from the Adobe Experience Manager Assets library for web experiences *(product-specific)*
* **Default subdomain**: The single web subdomain currently in use, marked with the Default badge *(product-specific)*
* **Use delegated subdomain**: Configuration type option that selects a subdomain already delegated to Adobe *(product-specific)*
* **Add your own domain**: Configuration type option that delegates a new subdomain by generating a matching DNS record *(product-specific)*
* **Manage Web Subdomains**: The permission required, on the production sandbox, to access and edit web subdomains *(product-specific)*

**Guardrails:**

* To access and edit web subdomains, you must have the Manage Web Subdomains permission on the production sandbox.
* Web subdomain configuration is common to all environments, and any modification also impacts the production sandboxes.
* You can create several web subdomains, but only the default subdomain is used, and only one can be used at a time.
* Journey Optimizer allows you to delegate up to 10 subdomains in total (covering both email and web channels); depending on your license contract you may be able to delegate up to 100 subdomains.
* Capital letters are not allowed in subdomains.
* You cannot use an existing web subdomain, and you cannot select a subdomain that is already used as a web subdomain.
* When configuring a new subdomain, Adobe's required checks can take up to 4 hours before the subdomain can be used to send web messages.
* Multi-level subdomains of the same parent domain are supported (for example, web.marketing.yourcompany.com).
* A new web subdomain always points to a CNAME record.
* To undelegate a web subdomain, reach out to your Adobe representative.

**Terminology:**

* Canonical name: Web subdomain — Acronym: n/a — variants: web subdomains, delegated subdomain
* Synonyms: "Use delegated subdomain" = "use a subdomain that is already delegated to Adobe"
* Do not confuse: "Use delegated subdomain" (select an already-delegated subdomain) ≠ "Add your own domain" (configure and delegate a new subdomain)
* Do not confuse: "Draft" ≠ "Processing" ≠ "Success" ≠ "Failed" (delegation statuses)

**FAQ:**

* **Q: How many web subdomains can be active at once?** — You can create several, but only the default subdomain is used and only one can be used at a time.
* **Q: What permission do I need to manage web subdomains?** — The Manage Web Subdomains permission on the production sandbox.
* **Q: How long does configuring a new subdomain take?** — Adobe's required checks can take up to 4 hours before the subdomain can be used to send web messages.
* **Q: What are the delegation statuses?** — Draft, Processing, Success, and Failed; only a Success subdomain is ready to be used.
* **Q: How do I remove a web subdomain?** — To undelegate it, reach out to your Adobe representative; a Failed subdomain can be deleted from the More actions menu to clean up the list.
* **Q: Are subdomain modifications isolated to one environment?** — No, web subdomain configuration is common to all environments and any modification also impacts the production sandboxes.

+++

<!-- ai-section-version: 1 | source-hash: 09f9bb9a -->
