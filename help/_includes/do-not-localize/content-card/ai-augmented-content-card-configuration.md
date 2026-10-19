---
title: AI Knowledge Reference
---
# AI Knowledge Reference

+++ AI Knowledge Reference

This section contains structured knowledge intended to support interpretation, retrieval, and question answering related to this topic.

For complete understanding, this information should be combined with the documentation on this page. Neither source is intended to stand alone; the page describes the feature, while this section provides additional context that helps disambiguate terminology, intent, applicability, and constraints.

* **TL;DR:** This page explains what a content card experience configuration and its surface URI are, and how to create a content card channel configuration in Journey Optimizer.

**Intents:**

* Understand what a content card experience configuration and a surface are
* Learn how a surface URI is composed from type, property, and container
* Reference surface URI examples for web, mobile, other device types, and wildcard surfaces
* Create a content card channel configuration from the Channel configurations menu
* Associate marketing actions and platform settings with the configuration
* Define web targeting with a page URL or a pages matching rule, or app targeting for iOS and Android

**Glossary:**

* **Content card experience configuration**: Any entity designed for user or system interaction, uniquely identified by a URI *(product-specific)*
* **Surface**: A container at any level of hierarchy with an entity (touchpoint) that exists, such as a web page, mobile app, desktop app, or a specific content location *(product-specific)*
* **Surface URI**: The unique identifier of a surface, composed of a type, a property, and a container *(product-specific)*
* **Wildcard surface**: A surface that matches a variety of client-surface definitions, for example `web://mydomain.com/*#hero_image` *(product-specific)*
* **Marketing action**: A selection that associates consent policies with the messages using the configuration, so customer preferences are respected *(product-specific)*
* **Pages matching rule**: A web targeting option that targets multiple URLs matching a specified rule *(product-specific)*

**Guardrails:**

* A content card experience configuration is uniquely identified by a URI.
* Configuration names must begin with a letter (A-Z) and can only contain alpha-numeric characters, plus the underscore, dot, and hyphen characters.
* For Web, specify a Page URL to apply changes to a single page exclusively, or create a Pages matching rule to target multiple URLs that match the rule.
* For iOS and Android, enter or select the App id, Location or path inside the app, and Preview URL.
* All consent policies associated with the selected marketing action are leveraged to respect customer preferences.

**Terminology:**

* Canonical name: Content card channel configuration — Acronym: URI (surface URI) — variants: content card experience configuration, content card configuration
* Synonyms: "surface" = "content card experience configuration"
* Do not confuse: "Page URL" (targets a single page exclusively) ≠ "Pages matching rule" (targets multiple URLs that match a rule)
* Do not confuse: "Type" (web, mobileapp, atm, kiosk, tvcd, service) ≠ "Property" (page URL or app bundle) ≠ "Container" (location on the page or app activity)

**FAQ:**

* **Q: What is a content card experience configuration?** — It is any entity designed for user or system interaction, uniquely identified by a URI, and can be seen as a container (surface) holding a touchpoint entity.
* **Q: What are the parts of a surface URI?** — A surface URI is composed of a type (web, mobileapp, atm, kiosk, tvcd, service, and so on), a property (page URL or app bundle), and a container (location on the page or app activity).
* **Q: What characters are allowed in a configuration name?** — Names must begin with a letter (A-Z) and can only contain alpha-numeric characters, plus the underscore, dot, and hyphen characters.
* **Q: How do I target web pages with the configuration?** — Specify a Page URL to apply changes to a single page exclusively, or create a Pages matching rule to target multiple URLs that match the specified rule.
* **Q: Where do I create a content card configuration?** — Access Channels > General settings > Channel configurations, click Create channel configuration, select the Content card channel, then configure and submit.

+++

<!-- ai-section-version: 1 | source-hash: 91dd5e06 -->
