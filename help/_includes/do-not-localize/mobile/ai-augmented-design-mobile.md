---
title: AI Knowledge Reference
---
# AI Knowledge Reference

+++ AI Knowledge Reference

This section contains structured knowledge intended to support interpretation, retrieval, and question answering related to this topic.

For complete understanding, this information should be combined with the documentation on this page. Neither source is intended to stand alone; the page describes the feature, while this section provides additional context that helps disambiguate terminology, intent, applicability, and constraints.

* **TL;DR:** This page explains how to design and personalize SMS, RCS, and MMS message content in Journey Optimizer, including RCS content types and fallback text, suggested actions, tracked and shortened URLs, deep links, Decisioning, and added MMS media.

**Intents:**

* Define RCS content by choosing a content type (Text, Media, Card, Carousel, or Location)
* Set the Default fallback text delivered when a device or carrier does not support RCS
* Add suggested actions with an action type (Reply, Open URL, Dial phone number, or View location)
* Define and personalize Mobile message content with the personalization editor and Generate text with AI
* Add tracked and shortened URLs and deep links using the Url helper function
* Personalize and optimize content with Decisioning using Priority Scores, Formulas, or AI Models
* Enable MMS to add media to the Mobile message content

**Glossary:**

* **Default fallback text**: The plain-text SMS version of an RCS message, delivered to profiles whose device or carrier does not support RCS *(product-specific)*
* **Suggested actions**: Interactive buttons that let profiles act with a single tap *(product-specific)*
* **Rich Media (Single)**: An RCS message type supporting up to 3,072 characters *(product-specific)*
* **Basic RCS**: An RCS message type limited to 160 characters *(product-specific)*
* **Personalization editor**: The editor used to define content, add personalization and dynamic content, and define conditional rules *(product-specific)*
* **Url helper function**: A helper used to add tracked URLs, shorten URLs through the originalUrl field, and create deep links with the DEEPLINK type *(product-specific)*
* **Decisioning**: A capability that dynamically selects and displays the best content using Priority Scores, Formulas, or AI Models *(product-specific)*

**Guardrails:**

* Every RCS message requires a Default fallback text; a campaign cannot be activated without it.
* SMS messages are limited to 160 characters per segment; longer messages are split into multiple parts and may incur additional charges.
* A Carousel requires a minimum of 2 cards.
* Character limits vary by message type: 3,072 characters for Rich Media (Single) and 160 for Basic RCS.
* MMS allows for up to 1600 characters of text.
* Short URLs have a lifespan of 30 days; after that period they display the message 404 short-code not found.
* To use the URL shortening function, you must first configure a subdomain linked to your configuration.
* Deep links require completing the deep link configuration steps in Journey Optimizer and implementing deep link handling in the mobile app, and link tracking must be enabled in the Actions section so the URL is rewritten through Adobe systems.

**Terminology:**

* Canonical name: Mobile message content — variants: SMS content
* Do not confuse: "Rich Media (Single)" (up to 3,072 characters) ≠ "Basic RCS" (160 characters)
* Do not confuse: "Reply" (sends a predefined text reply to the RCS agent) ≠ "Open URL" (redirects to a web page, deep link, or In-App destination) ≠ "Dial phone number" (opens the device dialer) ≠ "View location" (opens the device maps application)

**FAQ:**

* **Q: What happens when a recipient's device does not support RCS?** — Journey Optimizer automatically falls back to a standard SMS using the Default fallback text, which is required.
* **Q: How many cards does a Carousel need?** — A Carousel requires a minimum of 2 cards.
* **Q: What are the RCS character limits?** — 3,072 characters for Rich Media (Single) and 160 for Basic RCS.
* **Q: How long do shortened URLs stay active?** — The lifespan of short URLs is 30 days, after which they display 404 short-code not found.
* **Q: What is required before I can shorten URLs?** — You must first configure a subdomain that is then linked to your configuration.
* **Q: How much text can an MMS contain?** — MMS allows for up to 1600 characters of text.

**Personas:**

* **marketer:** Can define SMS content with the personalization editor, add tracked URLs and deep links with the Url helper function, and enable MMS to add media. Can define RCS content by choosing a content type such as Text, Media, Card, Carousel, or Location, add Suggested actions, and set Default fallback text. The page states that a campaign cannot be activated without a Default fallback text. Where: "Design a Mobile message".

**Onboarding:**

* **Level:** Beginner
* **First minimal step:** Add a Mobile message action in a journey or a campaign.
* **Success check:** After selecting Save, you can check your message content and rendering in the preview.
* **Previous:** Before shortening URLs in your message, you need a configured subdomain: Configure subdomains for Mobile message (mobile/mobile-subdomains.md); Before adding deep links to your message, you need to complete deep link configuration: Use and configure deep links in email and SMS messages (email/deeplinks.md)
* **Next:** After saving your message content, you can test and check it before sending: Check and test your Mobile messages (mobile/send-mobile-message.md); If your SMS, MMS, or RCS content returns an error code: Content authoring errors (content-management/content-authoring-errors.md)

+++

<!-- ai-section-version: 1 | source-hash: 827953bf -->
