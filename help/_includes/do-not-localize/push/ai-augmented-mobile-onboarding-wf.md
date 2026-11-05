---
title: AI Knowledge Reference
---
# AI Knowledge Reference

+++ AI Knowledge Reference

This section contains structured knowledge intended to support interpretation, retrieval, and question answering related to this topic.

For complete understanding, this information should be combined with the documentation on this page. Neither source is intended to stand alone; the page describes the feature, while this section provides additional context that helps disambiguate terminology, intent, applicability, and constraints.

* **TL;DR:** This page describes the mobile onboarding quick start workflow (public Beta) that rapidly configures the Adobe Experience Platform Mobile SDK to collect and validate mobile event data and send push notifications with Journey Optimizer.

**Intents:**

* Access the mobile onboarding quick start workflow from Data Collection
* Auto-create and configure the required Data Collection and Journey Optimizer assets
* Implement the SDK code in a mobile app with step-by-step guidance
* Validate the implementation and send a test push notification
* Transition to more advanced mobile implementation afterward

**Glossary:**

* **Mobile onboarding quick start workflow**: A product feature that rapidly configures the Adobe Experience Platform Mobile SDK and automates Data Collection setup for Journey Optimizer *(product-specific)*
* **Set up**: The step that auto creates and configures Data Collection and Journey Optimizer assets (Mobile Properties, Mobile Extensions, Journey Optimizer Extension, Rules, Data Elements, etc.) *(product-specific)*
* **Validate**: The step that reviews and checks the implementation, where a test push notification can be sent *(product-specific)*

**Guardrails:**

* The capability is available as a public Beta.
* It is accessible via the Adobe Experience Platform Data Collection home page to all customers.
* Beta Terms & Conditions must be accepted before proceeding.
* The Set up step requires the mobile app name, and iOS and Android platform information including App ID and authentication keys or key file.

**Terminology:**

* Canonical name: Mobile onboarding quick start workflow — Acronym: n/a — variants: mobile onboarding workflow, quick start workflow
* Synonyms: "Set up" step = first of the four steps
* Do not confuse: "Set up" ≠ "Implement" ≠ "Validate" ≠ "Review" (the four distinct workflow steps)

**FAQ:**

* **Q: What are the steps of the workflow?** — Four steps: set up, implement, validate, and review.
* **Q: Where do I access the workflow?** — From Data Collection in the solution switcher, via the Start Collecting Mobile Data card on the home page.
* **Q: Is this generally available?** — It is available as a public Beta.
* **Q: Can I test a push during onboarding?** — Yes, during the Validate step you can send a test push notification, leveraging Adobe Experience Platform Assurance.
* **Q: What does the Set up step create?** — Data Collection and Journey Optimizer assets such as Mobile Properties, Mobile Extensions, the Journey Optimizer Extension, Rules, and Data Elements.

**Personas:**

* **admin:** Can set up the workflow by entering the mobile app name and providing iOS and Android App ID and authentication keys or key file. The page states that Beta Terms & Conditions must be accepted before proceeding. Where: "Set up".

**Onboarding:**

* **Level:** Intermediate
* **First minimal step:** Select the Start Collecting Mobile Data card on the Data Collection home page.
* **Success check:** Automated setup is done, and you can start sending push notifications with Journey Optimizer.
* **Next:** Configure the push channel: Push notification configuration (push/push-configuration.md); Create a push notification: Configure a push notification (push/create-push.md)

+++

<!-- ai-section-version: 1 | source-hash: 0ed1ded5 -->
