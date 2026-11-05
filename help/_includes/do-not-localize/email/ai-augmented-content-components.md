---
title: AI Knowledge Reference
---
# AI Knowledge Reference

+++ AI Knowledge Reference

This section contains structured knowledge intended to support interpretation, retrieval, and question answering related to this topic.

For complete understanding, this information should be combined with the documentation on this page. Neither source is intended to stand alone; the page describes the feature, while this section provides additional context that helps disambiguate terminology, intent, applicability, and constraints.

* **TL;DR:** Content components are empty content placeholders you add inside structure components in the Email Designer — including Container, Button, Text, Divider, HTML, Image, Social, Offer decision, and Grid — and configure through the Settings and Style tabs.

**Intents:**

* Add and configure content components inside structure components
* Insert buttons, text, dividers, images, social links, HTML, and offer decisions into an email
* Group components inside a Container to apply a distinct style
* Organize content into rows and columns with the Grid component
* Insert personalized offers with the Offer decision component
* Adjust component attributes and styling using the Settings and Style tabs

**Glossary:**

* **Content components**: Empty content placeholders used to build and personalize email layout, added inside structure components *(product-specific)*
* **Container**: A component that groups content components so a distinct style can be applied to the group *(product-specific)*
* **Grid**: A component that organizes content into rows and columns, where each cell can contain other content components *(product-specific)*
* **Offer decision**: A component that inserts offers into a message, with the decision management engine picking the best offer to deliver *(product-specific)*
* **Alt text**: Caption defined for an image, corresponding to the alt HTML attribute *(product-specific)*

**Guardrails:**

* If changes are made to an offer decision used in a journey's message, you need to unpublish the journey and republish it so the changes are incorporated.
* Follow the European accessibility act guidelines (accessible fonts, readable formats, and alternative text for images) when designing with content components.
* For images, Adobe recommends using Adobe Assets rather than a source URL to keep links active and avoid expiration issues.
* Button Target options: None (default, same frame), Blank (new window or tab), Self (same frame), Parent (parent frame), Top (full body of the window).
* Use the Do not stack columns on mobile option to preserve a grid layout on mobile devices instead of stacking columns vertically.

**Terminology:**

* Canonical name: Content components — Acronym: n/a — variants: content component
* Synonyms: "Settings tab" and "Style tab" = the two configuration tabs in the right pane (also referred to as Styles tab)
* Do not confuse: "Content components" (empty placeholders for content) ≠ "Structure components" (define the layout, hold content components)
* Do not confuse: "Container" (styles a group of components) ≠ "Grid" (organizes components into rows and columns)

**FAQ:**

* **Q: Which content components are available?** — Container, Button, Text, Divider, HTML, Image, Social, Offer decision, and Grid.
* **Q: How many components can go into a structure component?** — You can add several components into a single structure component and into each column of a structure component.
* **Q: What happens after I change an offer decision used in a journey?** — You must unpublish and republish the journey so the message reflects the latest updates.
* **Q: How do I insert an image?** — Drag the Image component into a structure component, then Browse your assets, Import media to Adobe Experience Manager Assets, or Find Adobe Stock photos.
* **Q: Can I keep the grid layout on mobile?** — Yes, use the Do not stack columns on mobile option.

**Personas:**

* **marketer:** Can drag and drop content components into structure components using the Content components panel in the Email Designer. Can adjust each component's attributes and styling with the Settings and Style tabs, and delete or duplicate components from the advanced menu. The page states that you can add several components into a single structure component and into each column of a structure component. Where: "Add content components".

**Onboarding:**

* **Level:** Beginner, Intermediate
* **First minimal step:** Drag and drop the content components of your choice inside the relevant structure components.
* **Success check:** The newly added component is selected, and the Settings and Style tabs become available in the right pane to adjust its attributes.
* **Previous:** Define the layout of your email with structure components: Design content from scratch in Journey Optimizer (email/content-from-scratch.md)
* **Next:** Add personalized offers into an email using the Offer decision component: Add personalized offers (email/add-offers-email.md); Personalize text content with profile data fields: Personalize content in Journey Optimizer (personalization/personalize.md)

+++

<!-- ai-section-version: 1 | source-hash: e51f1972 -->
