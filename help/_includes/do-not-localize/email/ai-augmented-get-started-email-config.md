---
title: AI Knowledge Reference
---
# AI Knowledge Reference

+++ AI Knowledge Reference

This section contains structured knowledge intended to support interpretation, retrieval, and question answering related to this topic.

For complete understanding, this information should be combined with the documentation on this page. Neither source is intended to stand alone; the page describes the feature, while this section provides additional context that helps disambiguate terminology, intent, applicability, and constraints.

* **TL;DR:** This page outlines the essential steps to configure the email channel in Journey Optimizer, from delegating subdomains and creating IP pools to setting up channel configurations, execution fields, and retries.

**Intents:**

* Delegate to Adobe the subdomains used to send emails
* Create IP pools to group the IP addresses provisioned with your instance
* Create channel configurations and select the Email channel
* Configure the technical parameters (subdomain, IP pool, headers) in each email channel configuration
* Set up advanced parameters such as BCC, URL tracking, and one-click unsubscribe links
* Determine which execution fields to use in priority and manage retry days before suppression

**Glossary:**

* **Subdomain delegation**: Delegating to Adobe the subdomains used to send emails, which determine elements such as the web pages to be tracked and the mirror page URLs *(product-specific)*
* **IP pool**: A grouping of the IP addresses provisioned with your instance *(product-specific)*
* **Channel configuration**: The configuration where you select the Email channel and set the technical parameters required to deliver emails *(product-specific)*
* **Execution fields**: The fields that determine which recipient email address to use in priority when several addresses are available in Adobe Experience Platform *(product-specific)*

**Guardrails:**

* To send emails through journeys and campaigns, you must complete the listed configuration steps.
* Subdomains determine elements such as the web pages to be tracked and the mirror page URLs.
* The From email prefix and Error email prefix use the currently selected delegated subdomain; optionally, Sender name and Sender email can identify a different transmitting party (a full Sender address not tied to that subdomain suffix).
* Retries are performed for a configured number of days before sending email addresses to the suppression list.

**Terminology:**

* Canonical name: email configuration — Acronym: n/a — variants: email channel configuration, email channel setup
* Synonyms: n/a
* Do not confuse: "From email prefix" / "Error email prefix" (use the delegated subdomain suffix) ≠ "Sender name" / "Sender email" (a full address for a different transmitting party)

**FAQ:**

* **Q: What are the first configuration steps for the email channel?** — Delegate your sending subdomains to Adobe, then create IP pools to group the IP addresses provisioned with your instance.
* **Q: What do subdomains determine?** — Elements such as the web pages to be tracked and the mirror page URLs.
* **Q: Where do I set the technical parameters for sending emails?** — In each email channel configuration, where you select the subdomain and the IP pools and set up advanced parameters such as BCC, URL tracking, and unsubscribe links.
* **Q: What are execution fields for?** — To determine which recipient email address to use in priority when several addresses are available in Adobe Experience Platform.

+++

<!-- ai-section-version: 1 | source-hash: ab8ff377 -->
