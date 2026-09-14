---
title: AI Knowledge Reference
---
# AI Knowledge Reference

+++ AI Knowledge Reference

This section contains structured knowledge intended to support interpretation, retrieval, and question answering related to this topic.

For complete understanding, this information should be combined with the documentation on this page. Neither source is intended to stand alone; the page describes the feature, while this section provides additional context that helps disambiguate terminology, intent, applicability, and constraints.

* **TL;DR:** This page explains how a marketer delivers messages through a custom channel by adding a custom channel action to a journey or a campaign, authoring and personalizing the JSON payload, optionally tracking links, and then activating the experience.

**Intents:**

* Add a custom channel action to a journey using the Action activity
* Use a custom channel in a Scheduled or API-triggered campaign
* Select a channel configuration for the custom channel action
* Author and personalize the JSON message payload in the payload editor
* Track links included in the payload
* Activate the custom channel experience from a journey or a campaign

**Glossary:**

* **Custom channel action**: An action that delivers a message to profiles when they reach that step of the journey, referencing a custom channel configuration *(product-specific)*
* **Channel configuration**: The named preset, selected when configuring the action, that defines the endpoint, payload, and credentials used to deliver the message *(product-specific)*
* **Payload editor**: The content editor, opened with Edit content or Edit code, that reflects the payload structure defined for the custom channel *(product-specific)*
* **Simulate content**: The feature used to validate that the payload is well-formed JSON and that all personalization expressions resolve correctly for your test profiles *(product-specific)*
* **Action tracking**: A campaign option that automatically tracks links included in the message payload and requires a subdomain configured for custom channels *(product-specific)*
* **Expression fragments**: Shared personalization logic that can be reused across multiple channels and campaigns *(product-specific)*

**Guardrails:**

* This capability is available in Limited Availability; contact your Adobe representative to gain access.
* A custom channel must be configured by your administrator before you create a custom channel experience.
* Only JSON payloads are supported; non-JSON content such as XML can be wrapped in a JSON object.
* There is currently no validation of the payload at authoring time; use Simulate content to validate that the payload is well-formed JSON and that personalization expressions resolve correctly for your test profiles.
* Action tracking and link tracking require a subdomain configured for custom channels.
* For a tracked link, leave trackedUrl empty and set type to TRACKED; Journey Optimizer populates trackedUrl at send time.
* If your campaign or journey is subject to an approval policy, you must request approval before activation.

**Terminology:**

* Canonical name: custom channel experience — Acronym: n/a — variants: custom channel action
* Synonyms: "Edit content" = "Edit code" (both open the payload editor)
* Do not confuse: "Scheduled - Marketing" ≠ "API-triggered - Marketing/Transactional" (the two campaign types)
* Do not confuse: "Publish" (journey activation) ≠ "Review to activate" and "Activate" (campaign activation)
* Do not confuse: "Live" ≠ "Scheduled" (campaign statuses after activation)

**FAQ:**

* **Q: What payload format can I author?** — Only JSON; wrap non-JSON content such as XML in a JSON object.
* **Q: How do I check my payload before activating?** — Use Simulate content to confirm the payload is well-formed JSON and that all personalization expressions resolve correctly for your test profiles.
* **Q: How do I track links in the payload?** — Wrap the URL with the handlebar syntax, leaving trackedUrl empty and setting type to TRACKED; link tracking requires a delegated subdomain.
* **Q: How do I activate the experience?** — From a journey, click Publish; from a campaign, click Review to activate and then Activate.
* **Q: Can I run A/B tests on custom channel messages?** — Yes, in the Optimization section click Create experiment.

+++

<!-- ai-section-version: 1 | source-hash: 37d113c4 -->
