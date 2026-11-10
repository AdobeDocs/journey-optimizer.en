---
title: AI Knowledge Reference
---
# AI Knowledge Reference

+++ AI Knowledge Reference

This section contains structured knowledge intended to support interpretation, retrieval, and question answering related to this topic.

For complete understanding, this information should be combined with the documentation on this page. Neither source is intended to stand alone; the page describes the feature, while this section provides additional context that helps disambiguate terminology, intent, applicability, and constraints.

* **TL;DR:** This page walks through a cart abandonment email use case using three helper functions — `upperCase`, `each`, and `if` — to display a customer's first name in capitals, list cart items, and insert a product-specific shipping note conditionally.

**Intents:**

* Create a journey event whose schema includes the `productListItems` array
* Insert a customer's first name in uppercase using `{%= upperCase(profile.person.name.firstName) %}`
* List cart items by iterating over `context.journey.events.event_ID.productListItems` with `{{#each}}`
* Display a product-specific note conditionally using ``{%#if context.journey.events.`event_ID`.productListItems.name = "product_name" %}``
* Test the journey in test mode using a test profile with event payload, then publish

**Glossary:**

* **`upperCase`**: A PQL string function that converts a string to uppercase; called with `{%= upperCase(string) %}`. *(product-specific)*
* **`each` helper**: A Handlebars block helper (`{{#each array as |alias|}} ... {{/each}}`) that iterates over an array such as `productListItems`. *(product-specific)*
* **`if` helper**: A conditional block helper (`{%#if condition%} ... {%else%} ... {%/if%}`) that renders content only when the specified condition is true.
* **`productListItems`**: A standard XDM array representing cart contents, with fields including `name`, `quantity`, and `priceTotal`. *(product-specific)*
* **Test mode**: A journey feature that enables sending test messages to test profile addresses to verify journey and message behavior before publication. *(product-specific)*

**Guardrails:**

* Contextual attributes (including journey event data) are available in the personalization editor only after the message has been placed inside a journey that includes the relevant event.
* Test mode works only with test profiles.

**Terminology:**

* **Canonical name:** cart abandonment email — variants: cart abandonment use case
* **Do not confuse:** `context.journey.events.event_ID.productListItems` (event-sourced array, accessed via Contextual attributes) ≠ `profile.*` attributes (profile-sourced, always available)

**FAQ:**

* **Q: What helper functions are used in this use case?** — Three: `upperCase` (renders first name in capitals), `each` (iterates over the cart items array), and `if` (conditionally displays a product-specific shipping note).
* **Q: Where does the cart item data come from in the personalization expression?** — From the journey event's `productListItems` array, accessed via Contextual attributes at `context.journey.events.event_ID.productListItems`.
* **Q: Can contextual attributes be used before placing the message inside a journey?** — No. Contextual attributes are available in the personalization editor only after the message is placed inside a journey that includes the relevant event.
* **Q: How do I test the email with cart data?** — Turn on the **Test** toggle in the journey, click **Trigger an event**, and enter the input values in the Event configuration window, then click **Send**. The email is sent to the test profile's address.

**Personas:**

* **developer:** Can create an event whose schema includes the productListItems array and define its fields as payload fields. Can access cart data through context.journey.events.event_ID.productListItems, using the name, quantity, and priceTotal fields. The page states that contextual attributes are available only after the journey context has been passed to the message. Where: "Step 4: Insert the list of items from the cart".

**Onboarding:**

* **Level:** Intermediate
* **First minimal step:** Create an event whose schema includes the productListItems array.
* **Success check:** The email contains the note about the Juno Jacket because this product is in the cart.
* **Previous:** Configure a unitary event before personalizing the email: Work with journey events (event/about-events.md); Create the body of an email before inserting personalization tokens: Design content from scratch in Journey Optimizer (email/content-from-scratch.md)
* **Next:** Iterate over contextual data from other sources beyond productListItems: Iterate over contextual data (personalization/iterate-contextual-data.md); See another personalization use case with profile information and context: Personalization use case&colon; order status notification (personalization/personalization-use-case.md)

+++

<!-- ai-section-version: 1 | source-hash: 801d75d6 -->
