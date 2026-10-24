---
title: AI Knowledge Reference
---

# AI Knowledge Reference

+++ AI Knowledge Reference

This section contains structured knowledge intended to support interpretation, retrieval, and question answering related to this topic.

For complete understanding, this information should be combined with the documentation on this page. Neither source is intended to stand alone; the page describes the feature, while this section provides additional context that helps disambiguate terminology, intent, applicability, and constraints.

* **TL;DR:** This page documents two Adobe CX Enterprise Coworker skills for Adobe Journey Optimizer channels — Channel Operation, a read-only skill to view, list, search, and inspect channel configurations and credentials for standard channels, and Channel Builder, which lets administrators create, test, update, list, fetch, and delete custom outbound channels — with their use cases and limitations.

**Intents**

* List, search, and inspect channel configurations (presets) and credentials for standard Journey Optimizer channels using Channel Operation.
* Check sender domains, unsubscribe settings, IP pools, and other supporting resources of a channel configuration.
* Create, test, update, list, fetch, and delete custom outbound channels through a conversation with Coworker using Channel Builder, from a manual setup, a curl command, or an API document link (OpenAPI/Swagger spec or API reference page).
* Get guided through the channel configuration, authentication, throttling, and payload definition steps of a custom channel.

**Glossary**

* **Channel Operation** *(product-specific)*: CX Coworker skill that views, lists, searches, and inspects Adobe Journey Optimizer channel configurations (presets) and credentials for standard channels, including related resources such as push credentials, email subdomains, SMS credentials, WhatsApp credentials, file routings, LINE channel settings, and the Live Activity registry. It is read-only.
* **Channel Builder** *(product-specific)*: CX Coworker skill that helps administrators create, test, update, list, fetch, and delete custom outbound channels in Adobe Journey Optimizer, through manual setup, a curl command, or an API document link.
* **Custom channel**: A channel that brings any outbound messaging service into Adobe Journey Optimizer so that it can be used in campaigns and journeys.
* **Channel configuration (preset)**: The set of settings, such as sender and reply-to addresses, subdomains, IP pools, and unsubscribe settings, that a channel uses to send messages.

**Guardrails**

* Channel Builder is intended for the administrator persona.
* Channel Operation is read-only. It does not create, update, or delete channel configurations.
* Channel Operation is for standard channel configurations; Channel Builder is for custom outbound channels only.
* When testing a custom channel connection, Channel Builder asks which payload scenario to run before executing the test.
* Channel Operation is available to all customers who have access to Coworker.

**Terminology**

* Do not confuse: "Channel Builder" (creates and tests custom channels) is not the same skill as "Channel Operation" (reads existing channel configurations); each is a distinct Coworker skill on this page.
* Do not confuse: the Coworker skills "Explore Channel Configuration" and "Explore Campaigns", tagged Operational Insights in the Coworker skills catalog, are not documented on this page.

**FAQ**

* **What does Channel Builder do?** It lets administrators create, test, update, list, fetch, and delete custom outbound channels in Coworker chat, through a manual setup, a curl command, or an API document link, covering channel configuration, authentication, throttling, and payload definition.
* **Can Channel Operation change my channel configurations?** No. Channel Operation is read-only.
* **Which channels does Channel Operation cover?** Standard Journey Optimizer channel configurations (presets) and credentials, such as email, SMS, push, direct mail, in-app, and web, plus related resources like push credentials, email subdomains, SMS and WhatsApp credentials, file routings, LINE channel settings, and the Live Activity registry. For custom outbound channels, use Channel Builder.
* **Where can I learn about custom channels?** See Get started with custom channels.

+++

<!-- ai-section-version: 1 | source-hash: 00000000 -->
