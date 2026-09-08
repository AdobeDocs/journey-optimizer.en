---
title: AI Knowledge Reference
---
# AI Knowledge Reference

+++ AI Knowledge Reference

This section contains structured knowledge intended to support interpretation, retrieval, and question answering related to this topic.

For complete understanding, this information should be combined with the documentation on this page. Neither source is intended to stand alone; the page describes the feature, while this section provides additional context that helps disambiguate terminology, intent, applicability, and constraints.

* **TL;DR:** This page explains how to set up and run a sample that combines a Content Card campaign and an Inbox campaign with the Adobe Experience Platform Web SDK to deliver a persistent notification inbox on a website.

**Intents:**

* Configure the Journey Optimizer datastream, channels, and campaigns that feed the inbox
* Deliver notification items with a Content Card campaign and inbox configuration with an Inbox campaign on the same surface
* Subscribe to ruleset items and fetch propositions with the Web SDK
* Report inbox interactions back to AJO with `collectEvent`
* Trigger cards that have additional delivery rules with `evaluateRulesets`
* Run the sample server locally and point it at your AJO environment

**Glossary:**

* **Message inbox**: A persistent notification inbox driven by two AJO campaigns that target the same surface *(product-specific)*
* **Content Card campaign**: The campaign that delivers individual notification items to the inbox *(product-specific)*
* **Inbox campaign**: The campaign that delivers configuration such as the title, empty-state copy, and layout for the inbox shell *(product-specific)*
* **Surface**: The Page URL and Location on page location that both channels target and that the Web SDK code queries for *(product-specific)*
* **`subscribeRulesetItems`**: Web SDK command that registers a callback that runs each time the propositions eligible for display change *(product-specific)*
* **`sendEvent`**: Web SDK command that fetches propositions *(product-specific)*
* **`collectEvent`**: Function provided by the `subscribeRulesetItems` callback used to report interactions (display, interact, dismiss, delete) back to AJO to keep campaign reporting accurate *(product-specific)*
* **`evaluateRulesets`**: Web SDK command called with a matching `decisionContext` to trigger cards that have additional delivery rules *(product-specific)*

**Guardrails:**

* The datastream must be configured with Adobe Experience Platform as a service, with Journey Optimizer enabled and an event dataset selected.
* The two channel configurations (one Content Cards channel and one Inbox channel) must share the same surface, and the Page URL and Location on page of both must be set to that surface.
* The Location on page must match the surface you query for in your Web SDK code.
* Match the audience and schedule settings of the Inbox campaign to the Content Card campaign so both are active for the same users at the same time.
* Both campaigns must be activated.
* Cards with additional delivery rules do not appear on `sendEvent` alone; you must call `evaluateRulesets` with the matching `decisionContext` to trigger them.
* Before testing, update the `datastreamId`, `orgId`, and `SURFACE` constant in `src/app/page.js` to point at your AJO environment.

**Terminology:**

* Canonical name: Message inbox — Acronym: n/a — variants: persistent notification inbox, inbox
* Synonyms: "Web SDK" = "Adobe Experience Platform Web SDK"
* Do not confuse: "Content Card campaign" (delivers individual notification items) ≠ "Inbox campaign" (delivers the inbox configuration/metadata such as title, empty-state copy, and layout)
* Do not confuse: "`sendEvent`" (fetches propositions) ≠ "`evaluateRulesets`" (triggers cards with additional delivery rules via `decisionContext`)

**FAQ:**

* **Q: Which two campaigns drive the inbox?** — A Content Card campaign that delivers individual notification items and an Inbox campaign that delivers configuration such as the title, empty-state copy, and layout, both targeting the same surface.
* **Q: Which Web SDK commands does the inbox rely on?** — `subscribeRulesetItems`, which registers a callback that runs when eligible propositions change, and `sendEvent`, which fetches those propositions.
* **Q: Why don't cards with additional delivery rules appear after `sendEvent`?** — They do not appear on `sendEvent` alone; you must call `evaluateRulesets` with the matching `decisionContext` to trigger them, after which the `subscribeRulesetItems` callback runs again with the newly qualified cards.
* **Q: How do I keep campaign reporting accurate?** — Use the `collectEvent` function provided by the `subscribeRulesetItems` callback to report interactions (display, interact, dismiss, delete) back to AJO.
* **Q: How do I run the sample?** — Run `npm install` and `npm start`, open `https://localhost`, and update `datastreamId`, `orgId`, and the `SURFACE` constant in `src/app/page.js` for your AJO environment.

+++

<!-- ai-section-version: 1 | source-hash: 87182ea0 -->
