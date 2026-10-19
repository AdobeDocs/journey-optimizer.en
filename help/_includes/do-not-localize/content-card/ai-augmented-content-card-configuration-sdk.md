---
title: AI Knowledge Reference
---
# AI Knowledge Reference

+++ AI Knowledge Reference

This section contains structured knowledge intended to support interpretation, retrieval, and question answering related to this topic.

For complete understanding, this information should be combined with the documentation on this page. Neither source is intended to stand alone; the page describes the feature, while this section provides additional context that helps disambiguate terminology, intent, applicability, and constraints.

* **TL;DR:** This page walks through a sample that uses the Adobe Experience Platform Web SDK to fetch and render Adobe Journey Optimizer content cards entirely on the client side of a web page.

**Intents:**

* Set up and run the Web SDK content card sample locally over HTTPS
* Configure the Web SDK (alloy) on a page and fetch personalized content with the sendEvent command
* Subscribe to content cards for a surface using the subscribeRulesetItems command
* Render content cards and send display and interact events
* Trigger additional content cards client side using evaluateRulesets and a decisionContext
* Persist qualified content cards across user sessions with personalizationStorageEnabled

**Glossary:**

* **Surface**: The identifier a content card subscription and events are scoped to, for example `web://alloy-samples.adobe.com/#content-cards-sample` *(product-specific)*
* **subscribeRulesetItems**: The Web SDK command used to subscribe to content cards for a surface; its callback returns propositions containing content card data *(product-specific)*
* **evaluateRulesets**: The Web SDK command triggered on client-side actions to evaluate rulesets using a decisionContext *(product-specific)*
* **decisionContext**: The context passed with evaluateRulesets that supplies the values needed to satisfy a campaign's client-side trigger rules *(product-specific)*
* **collectEvent**: A convenience function provided in the subscribeRulesetItems callback used to send Experience Edge events to track displays, interactions, and other user actions *(product-specific)*
* **personalizationStorageEnabled**: A configure option that, when set to true, stores previously qualified content cards so they continue to be displayed across user sessions *(product-specific)*
* **Trigger rule**: A client-side condition that, when met, causes additional content cards to be displayed *(product-specific)*

**Guardrails:**

* To use disqualification rules with content cards, Web SDK version 2.28.0 or later is required.
* You need to install node and npm to run the sample.
* The samples require locally signed SSL certificates to serve content over HTTPS.
* In this sample, four campaigns are used, one per content card, all sharing the same surface `web://alloy-samples.adobe.com/#content-cards-sample`.

**Terminology:**

* Canonical name: Configure content cards support in Web SDK — Acronym: SDK — variants: Web SDK content card sample, Content cards configuration Web SDK
* Synonyms: "Web SDK" = "alloy"
* Do not confuse: "sendEvent" (fetch personalized content) ≠ "subscribeRulesetItems" (subscribe to content cards for a surface) ≠ "evaluateRulesets" (evaluate rulesets on a client-side action)
* Do not confuse: "display" event (content card shown) ≠ "interact" event (content card clicked)

**FAQ:**

* **Q: What Web SDK version is needed for disqualification rules?** — Web SDK version 2.28.0 or later is required to use disqualification rules with content cards.
* **Q: Why do the samples require SSL certificates?** — The samples serve content over HTTPS, so they require locally signed SSL certificates; the page uses `mkcert` to create and install them.
* **Q: How are qualified content cards kept across sessions?** — Setting `personalizationStorageEnabled` to true in the configure command stores previously qualified content cards so they continue to be displayed across user sessions.
* **Q: How are additional content cards triggered?** — Content cards support custom triggers evaluated on the client side; the sample calls `evaluateRulesets` with a `decisionContext` when the Deposit Funds or Share on social media buttons are clicked.
* **Q: What happens when a content card button is clicked?** — The `collectEvent` function tracks the interaction, and if the button is an anchor, the browser is directed to the `actionUrl` specified by the campaign.

+++

<!-- ai-section-version: 1 | source-hash: cf6e51d8 -->
