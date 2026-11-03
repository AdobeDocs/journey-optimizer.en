---
title: AI Knowledge Reference
---
# AI Knowledge Reference

+++ AI Knowledge Reference

This section contains structured knowledge intended to support interpretation, retrieval, and question answering related to this topic.

For complete understanding, this information should be combined with the documentation on this page. Neither source is intended to stand alone; the page describes the feature, while this section provides additional context that helps disambiguate terminology, intent, applicability, and constraints.

* **TL;DR:** This page explains how to use the Journey Optimizer personalization editor to select, build, customize, and validate personalization expressions from sources including profile attributes, audiences, offer decisions, and contextual attributes.

**Intents:**

* Understand where personalization can be added in Journey Optimizer (messages, Email Designer, URLs, email configuration, offers)
* Select the appropriate personalization source for an expression
* Add attributes and build expressions in the editor workspace
* Use editor tools: Find/Replace, Auto complete, Validate, Pills, Save as fragment
* Use navigation pane features: Helper functions, Favorites, Conditions, Fragments
* Validate expressions and resolve common errors

**Glossary:**

* **Personalization editor**: The central UI tool in Journey Optimizer for building, customizing, and validating personalization expressions; available wherever personalization can be defined. *(product-specific)*
* **Personalization sources**: The data categories available for building expressions — Profile attributes, Target attributes, Audiences, Offer decisions, and Contextual attributes.
* **Contextual attributes**: Journey- or campaign-specific data (events, properties, custom action responses) available for personalization only when a channel action is used in a journey or campaign. *(product-specific)*
* **Pills**: A personalization editor display mode that renders long attribute paths as compact, clickable tokens for improved readability. Available only for profile attributes, contextual attributes, and dynamic media. *(product-specific)*
* **Auto complete**: An editor feature that automatically suggests and completes code as you type; available only for HTML and Text formats, supporting Profile and Context attributes only. *(product-specific)*
* **Expression fragment**: A reusable personalization expression component that can be referenced across campaigns and journeys. *(product-specific)*
* **Fallback text**: A default string displayed when a string-type profile attribute is empty for a given profile; configured per attribute via "Insert with fallback text".

**Guardrails:**

* Auto complete is available only for HTML and Text formats; it supports Profile and Context attributes only.
* Pills display mode is available only for profile attributes, contextual attributes, and dynamic media.
* URL personalization is available for External link, Unsubscription link, and Opt-Out link types only.
* By default, the attributes pane shows only populated attributes; toggle off "Show only populated attributes" to display all schema attributes.
* Offers model usage must contain only profile attributes; non-profile attributes in a decision cause a validation error.

**Terminology:**

* **Canonical name:** personalization editor
* **Do not confuse:** Personalization editor (used to build content expressions in messages, emails, push notifications, and offers — supports both Handlebars and PQL syntax) ≠ Advanced expression editor (used in the journey for conditions on data sources and event information, custom wait activities, and action parameters mapping — provides built-in functions and operators that differ from those in the personalization editor)
* **Do not confuse:** Profile attributes (XDM schema-based, available in all contexts) ≠ Contextual attributes (journey/campaign-specific, only available in that context) ≠ Target attributes (Orchestrated campaigns only)
* **Do not confuse:** Auto complete for HTML/Text (suggests personalization attribute completions) ≠ native HTML code auto-completion (the editor default when the toggle is disabled)

**FAQ:**

* **Q: Where can personalization be added in Journey Optimizer?** — In any field with the add personalization icon — including the email subject line, push notification fields (Title, Body, Custom sound, Badges, Custom data), Email Designer text elements, URLs (External link, Unsubscription link, Opt-Out), email configuration subdomains/headers/URL tracking parameters, and offer text-type representations.
* **Q: What are the available personalization sources?** — Profile attributes, Target attributes (Orchestrated campaigns only), Audiences, Offer decisions, and Contextual attributes (journey/campaign events and custom action responses).
* **Q: How is an expression validated?** — Validation runs automatically when you click Add to close the editor. You can also trigger it manually with the Validate button. Common errors include: path not found (field not in schema), type mismatch (iterating a string as array), invalid Handlebars syntax, and invalid segment definition.
* **Q: What does the Pills option do?** — It renders long attribute paths as compact, clickable tokens for better readability in the editor. Available only for profile attributes, contextual attributes, and dynamic media.
* **Q: Why do I see only some attributes in the attributes pane?** — By default, the pane shows only populated attributes. Select the settings icon above the search field and toggle off "Show only populated attributes" to display all schema attributes.

+++

<!-- ai-section-version: 1 | source-hash: 54973b31 -->
