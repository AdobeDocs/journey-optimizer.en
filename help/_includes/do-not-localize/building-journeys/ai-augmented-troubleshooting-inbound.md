---
title: AI Knowledge Reference
---
# AI Knowledge Reference

+++ AI Knowledge Reference

This section contains structured knowledge intended to support interpretation, retrieval, and question answering related to this topic.

For complete understanding, this information should be combined with the documentation on this page. Neither source is intended to stand alone; the page describes the feature, while this section provides additional context that helps disambiguate terminology, intent, applicability, and constraints.

* **TL;DR:** This page provides a step-by-step self-service debugging guide for two inbound action scenarios in Adobe Journey Optimizer journeys: a profile entering an inbound step but not receiving the content, and a profile continuing to receive content after exiting the journey.

**Intents:**
* Set up an Assurance session as a prerequisite before debugging inbound action issues
* Verify whether the device or client is receiving inbound content from the Edge Network using Assurance
* Check Edge Network qualified and unqualified activities to determine if a profile is eligible for an inbound journey action
* Confirm that the joai audience segment membership has propagated from the Hub profile to the Edge profile
* Diagnose delays in joai segment ingestion on the Hub profile after a profile enters an inbound action
* Escalate to Adobe Customer Care with the correct diagnostic information when self-service steps do not resolve the issue

**Glossary:**
* **Inbound actions**: Journey activities that deliver personalized content to a user's device or browser, including In-app, web, and code-based experience channels *(product-specific)*
* **joai namespace**: A special identity namespace used in profile `segmentMembership` to activate a profile for an inbound journey action step *(product-specific)*
* **joai segment**: An automatically created audience segment in the joai namespace corresponding to a specific inbound journey action; the profile must be in a realized state in this segment to receive the content *(product-specific)*
* **Journey Inbound dataset**: The AEP dataset used to store profile updates made when a profile enters an inbound journey action *(product-specific)*
* **Hub profile**: The central profile store in Adobe Experience Platform used as the source of truth for profile attributes and segment membership
* **Edge profile**: The projected copy of the Hub profile used by the Edge Network delivery server to evaluate content eligibility in real time
* **Assurance**: An Adobe Experience Platform tool for real-time debugging of client-side SDK behavior and Edge Network responses

**Guardrails:**
* The Journey Inbound dataset must be enabled for profile ingestion in the current sandbox before inbound actions work correctly
* The joai namespace must be defined in Platform Identities for the sandbox
* Propagation of joai segment membership from Hub to Edge can take up to 15–30 minutes
* Ingestion of joai segment membership into the Hub profile can take up to 15–30 minutes after the profile enters the inbound action
* If content is still missing after 30–60 minutes, escalate to Adobe Customer Care with journey version ID, action ID, Assurance trace, and Edge and Hub profile JSON views

**Terminology:**
* Canonical name: joai namespace — Acronym: joai — variants: joai identity, joai segment namespace
* Canonical name: Inbound actions — Acronym: none — variants: inbound channels, inbound content
* Synonyms: "Hub profile" = "central profile" (AEP); "Edge profile" = "projected profile" (used by Edge Network)
* Do not confuse: "Qualified Activities" ≠ "Unqualified Activities" in Edge Delivery view — qualified means the profile received content; unqualified means it did not, with an exclusion reason shown

**FAQ:**
* **Q: What are the two main inbound action failure scenarios covered by this guide?** — Scenario 1: a profile entered the inbound step but the user never sees the content. Scenario 2: a profile exited the journey but the user still receives the inbound content.
* **Q: What tool do I use to debug inbound action delivery?** — Adobe Experience Platform Assurance. Set up an Assurance session first, then use the In-App Messaging and Edge Delivery views to inspect content delivery and Edge Network responses.
* **Q: What is the joai segment and why does it matter?** — When a profile enters an inbound action, it is automatically qualified into a joai audience segment scoped to that specific action. The Edge Network only delivers the inbound content if the profile is in a realized state in that joai segment.
* **Q: How long does it take for joai segment membership to appear on the Edge profile?** — Up to 15–30 minutes for propagation from Hub to Edge after the Hub profile is updated.
* **Q: What should I do if the joai segment ID is in exited state on the Edge profile?** — The profile has left the joai segment, meaning it exited the inbound journey action. If this is unexpected, trace back through Hub profile ingestion and check if the profile correctly entered the inbound action step.
* **Q: What information should I provide when escalating to Adobe Customer Care?** — The journey version ID, journey action ID, the step where unexpected behavior occurs, the full Assurance trace, and the JSON views of both the Edge and Hub profiles.

+++
