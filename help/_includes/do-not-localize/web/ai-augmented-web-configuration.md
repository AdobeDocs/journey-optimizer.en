---
title: AI Knowledge Reference
---
# AI Knowledge Reference

+++ AI Knowledge Reference

This section contains structured knowledge intended to support interpretation, retrieval, and question answering related to this topic.

For complete understanding, this information should be combined with the documentation on this page. Neither source is intended to stand alone; the page describes the feature, while this section provides additional context that helps disambiguate terminology, intent, applicability, and constraints.

* **TL;DR:** This page explains how to create a web channel configuration in Journey Optimizer, targeting either a single page URL or multiple pages through a pages matching rule built with Domain and Path operators.

**Intents:**

* Create a web channel configuration from Channels > General settings > Channel configurations
* Target a single page by entering a Page URL
* Target multiple pages by building a pages matching rule
* Assign data usage labels to a configuration through Manage access (OLAC)
* Associate consent policies to messages by selecting Marketing actions
* Choose the right Domain and Path operators to match the intended URLs

**Glossary:**

* **Web channel configuration**: A web property identified by a URL where content will be delivered; it can match a single page URL or multiple pages *(product-specific)*
* **Single page**: Web settings option that applies changes to a single page by entering a Page URL *(product-specific)*
* **Pages matching rule**: Web settings option that targets multiple URLs matching the same rule so the same content changes apply across multiple pages at once *(product-specific)*
* **Default authoring and preview URL**: A URL entered for a pages matching rule so the pages generated or matched by the rule have a designated URL for content creation and preview *(product-specific)*
* **Marketing action**: A selection that associates consent policies to messages using the configuration so customer preferences are respected *(product-specific)*
* **Wildcard matching**: An operator allowing a wildcard (asterisk) match inside the Domain or Path string *(product-specific)*

**Guardrails:**

* Configuration names must begin with a letter (A-Z) and can only contain alphanumeric characters plus underscore, dot, and hyphen.
* You can add up to 10 rules when building a pages matching rule.
* For the Domain "Wildcard matching" operator, the value must contain one and only one wildcard (asterisk).
* A pages matching rule can be built when creating a web or code-based experience configuration.
* The Or and Exclude operators can be used between the different rules.

**Terminology:**

* Canonical name: Web channel configuration — Acronym: n/a — variants: web configuration, channel configuration
* Synonyms: "Pages matching rule" = "rule that matches multiple pages"
* Do not confuse: "Single page" (targets one Page URL) ≠ "Pages matching rule" (targets multiple URLs matching a rule)
* Do not confuse: "Domain" operators ≠ "Path" operators (each section has its own available operators)

**FAQ:**

* **Q: How do I create a web channel configuration?** — Go to Channels > General settings > Channel configurations, click Create channel configuration, enter a name, select the Web channel, choose Single page or Pages matching rule, then Submit.
* **Q: What characters are allowed in a configuration name?** — It must begin with a letter (A-Z) and can only contain alphanumeric characters plus underscore, dot, and hyphen.
* **Q: How many rules can a pages matching rule contain?** — You can add up to 10 rules, and use the Or or Exclude operators between them.
* **Q: How do I target more than one page?** — Select Pages matching rule, define criteria for the Domain and Page fields, and enter a Default authoring and preview URL.
* **Q: When would I use the Exclude operator?** — When one of the pages matching the defined rule should not be targeted.

+++

<!-- ai-section-version: 1 | source-hash: 411246b0 -->
