---
title: AI Knowledge Reference
---
# AI Knowledge Reference

+++ AI Knowledge Reference

This section contains structured knowledge intended to support interpretation, retrieval, and question answering related to this topic.

For complete understanding, this information should be combined with the documentation on this page. Neither source is intended to stand alone; the page describes the feature, while this section provides additional context that helps disambiguate terminology, intent, applicability, and constraints.

* **TL;DR:** This page explains how to deliver messages through a custom channel by adding it to a journey or a campaign, authoring and personalizing the JSON payload, optionally tracking links, and then activating the experience.

**Intents:**

* Add a custom channel to a journey using an Action activity with the custom channel selected
* Use a custom channel in a Scheduled or API-triggered campaign
* Select a channel configuration for the custom channel
* Author and personalize the JSON message payload in the payload editor
* Track links included in the payload
* Activate the custom channel experience from a journey or a campaign

**Glossary:**

* **Custom channel (in a journey)**: A channel selected in the drop-down of an Action activity; custom channels are listed by the name and icon assigned in the Channel Builder *(product-specific)*
* **Channel configuration**: The configuration selected for the custom channel, in a journey after clicking Configure action and in a campaign in the Actions section; the page links to custom-channel-configuration for how to create one *(product-specific)*
* **Payload editor**: The content editor, opened with Edit content or Edit code, that reflects the payload structure defined for the custom channel *(product-specific)*
* **Simulate content**: The feature used to validate that the payload is well-formed JSON and that all personalization expressions resolve correctly for your test profiles *(product-specific)*
* **Action tracking**: A campaign option that automatically tracks links included in the message payload and requires a subdomain configured for custom channels *(product-specific)*
* **Expression fragments**: Shared personalization logic that can be reused across multiple channels and campaigns *(product-specific)*

**Guardrails:**

* A custom channel must be configured by your administrator before you create a custom channel experience.
* Only JSON payloads are supported; non-JSON content such as XML can be wrapped in a JSON object.
* There is currently no validation of the payload at authoring time; use Simulate content to validate that the payload is well-formed JSON and that personalization expressions resolve correctly for your test profiles.
* Action tracking and link tracking require a subdomain configured for custom channels.
* For a tracked link, leave trackedUrl empty and set type to TRACKED; Journey Optimizer populates trackedUrl at send time.
* Custom channels are available in journeys, orchestrated campaigns and Marketing (action and API-triggered) campaigns. They are not available in transactional campaign types.
* If your campaign or journey is subject to an approval policy, you must request approval before activation.

**Terminology:**

* Canonical name: custom channel experience — Acronym: n/a
* Both "Edit content" and "Edit code" are named on this page as the button that opens the payload editor
* Do not confuse: "Scheduled - Marketing" ≠ "API-triggered - Marketing" (the two campaign types listed on this page)
* Do not confuse: "Publish" (journey activation) ≠ "Review to activate" and "Activate" (campaign activation)
* Do not confuse: "Live" ≠ "Scheduled" (campaign statuses after activation)

**FAQ:**

* **Q: What payload format can I author?** — Only JSON; wrap non-JSON content such as XML in a JSON object.
* **Q: How do I check my payload before activating?** — Use Simulate content to confirm the payload is well-formed JSON and that all personalization expressions resolve correctly for your test profiles.
* **Q: How do I track links in the payload?** — Wrap the URL with the handlebar syntax, leaving trackedUrl empty and setting type to TRACKED; link tracking requires a delegated subdomain.
* **Q: How do I activate the experience?** — From a journey, click Publish; from a campaign, click Review to activate and then Activate.
* **Q: Can I run A/B tests on custom channel messages in a campaign?** — Yes, in the Optimization section of the campaign, click Create experiment.

**Personas:**

* **marketer:** Can add a custom channel action to a journey through the Action activity, or select a custom channel in a Scheduled or API-triggered campaign. Can select the channel configuration, then select Edit content to author and personalize the JSON payload in the payload editor. Can select Publish to activate the journey, or select Review to activate and then Activate for a campaign. The page states that only JSON payloads are supported, and non-JSON content can be wrapped in a JSON object. Where: "Add a custom action through a journey or a campaign".

**Onboarding:**

* **Level:** Experienced
* **First minimal step:** Create a journey, then drag an Action activity from the Actions section of the palette and select a custom channel in the Action drop-down.
* **Success check:** The journey goes live and starts calling your external endpoint for qualifying profiles, or the campaign takes the Live status, or the Scheduled status if a future start date was defined.
* **Previous:** Configure a custom channel before creating a custom channel experience: Configure a custom channel – overview (custom-channel/configure-custom-channel.md); Create a journey before adding a custom channel action: Create your first journey (building-journeys/journey-gs.md)
* **Next:** Preview and test your custom channel payload before activating: Test your custom channel (custom-channel/test-custom-channel.md); Request approval before activation if the campaign or journey is subject to an approval policy: Get started with journeys & campaigns approval (test-approve/gs-approval.md)

+++

<!-- ai-section-version: 1 | source-hash: 2867b4aa -->
