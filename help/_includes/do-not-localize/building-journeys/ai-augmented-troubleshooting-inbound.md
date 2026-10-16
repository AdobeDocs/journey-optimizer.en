---
title: AI Knowledge Reference
---
# AI Knowledge Reference

+++ AI Knowledge Reference

This section contains structured knowledge intended to support interpretation, retrieval, and question answering related to this topic.

For complete understanding, this information should be combined with the documentation on this page. Neither source is intended to stand alone; the page describes the feature, while this section provides additional context that helps disambiguate terminology, intent, applicability, and constraints.

* **TL;DR:** This page provides a step-by-step process to debug issues related to inbound actions in a journey, covering two scenarios: a profile entering an inbound action but the user not receiving the content, and a user still receiving the content after the profile exits the journey.

**Intents:**

* Set up an Assurance session and gather the journey, action, and profile details before debugging inbound action issues
* Verify whether the device or client is receiving inbound content for the In-app, Web, and Code-based experience channels
* Check whether the Edge Network returns the content by reading the Qualified Activities and Unqualified Activities sections of the Edge Delivery view in Assurance
* Confirm that the joai audience segment membership is present in the Edge profile and the Hub profile
* Debug a user who still receives inbound content after the profile exits the journey
* Escalate to Adobe Customer Care or an Adobe representative with the right diagnostic information when the steps do not resolve the issue

**Glossary:**

* **Inbound actions**: Journey actions such as In-app, web, and code-based experiences that enable personalized engagement with users *(product-specific)*
* **joai namespace**: The namespace used in the profile `segmentMembership` for activating the profile for the inbound step; it must be defined in Platform Identities for the sandbox *(product-specific)*
* **joai segment**: A special audience segment in the joai namespace into which a profile is automatically qualified when it enters an inbound action; its segment ID is <*JourneyVersionID*>_<*JourneyActionID*> *(product-specific)*
* **Journey Inbound dataset**: The dataset the inbound action uses for the profile updates during execution *(product-specific)*
* **Hub profile**: The profile that is first updated when a profile is qualified into a joai segment; the segment membership is then projected to the Edge profile
* **Edge profile**: The profile to which the segment membership is projected from the Hub, for use by the Edge Network delivery server
* **Assurance**: The Adobe Experience Platform tool whose session is used on this page to check the messages on the device and the Edge response payload

**Guardrails:**

* The Journey Inbound dataset must be enabled for Profiles in the current sandbox (pre-check)
* The joai namespace must be defined in Platform Identities for the sandbox (pre-check)
* A client request qualifies a profile for inbound content on a surface only if the profile is a member of the corresponding joai segment at the time of the request
* Propagation of the joai segment membership from the Hub to the Edge can take up to 15-30 minutes from the moment the profile is updated on the Hub
* Ingestion of the joai segment membership into the Hub profile can take up to 15-30 minutes from the moment the profile entered the inbound journey action
* If the expected behavior is still not seen after waiting 30 to 60 minutes for the segment membership to propagate to the Edge Network, contact Adobe Customer Care or your Adobe representative

**Prerequisites and permissions:**

* An Assurance session set up
* The journey name and journey version ID, retrieved from the journey containing the inbound action
* The inbound action label and ID
* The profile namespace and ID of the profile encountering issues

**Terminology:**

* Canonical name: joai namespace — variants: joai identity
* Canonical name: Inbound actions — variants: inbound journey action
* Synonyms: "joai segment" = "joai audience segment"
* Do not confuse: "Qualified Activities" ≠ "Unqualified Activities" in the Edge Delivery view — in Qualified Activities the profile qualified for the inbound journey action and the content should be returned; in Unqualified Activities the profile did not qualify, and the exclusion reasons give more details

**FAQ:**

* **Q: What are the two scenarios covered by this guide?** — Scenario 1: a profile has entered the inbound action but, even after 30 minutes, the inbound content is not showing up in the device/client at the setup trigger step. Scenario 2: the profile has exited the journey, but the user is still receiving the inbound content.
* **Q: What tool do I use to debug inbound action delivery?** — Assurance. Set up an Assurance session first, then use the In-App Messaging section for the In-app channel and the Edge Delivery section for the Edge response payload.
* **Q: What is the joai segment and why does it matter?** — When a profile enters an inbound action, it is automatically qualified into a special audience segment (in the joai namespace) corresponding to the inbound journey action. The profile qualifies to receive content for the inbound journey actions targeting a surface only if it is a member of the corresponding joai segment at the time of the request.
* **Q: How do I find my Edge activity in Assurance?** — Look for the activity where the audienceNamespace is joai and the audienceSegmentId is <*JourneyVersionID*>_<*JourneyActionID*>.
* **Q: How long does it take for the joai segment membership to appear on the Edge profile?** — Up to 15-30 minutes from the moment the profile is updated on the Hub.
* **Q: What does it mean if the joai segment ID is not present or is in exited state on the Edge profile?** — It was not (yet) propagated to the Edge. Wait 15 to 30 minutes for the `segmentMembership` values to be propagated from the Hub to the Edge; if the segment ID is still not present, check the Hub profile.
* **Q: What does it mean if the joai segment ID is not present or is in exited state on the Hub profile?** — The profile was not (yet) correctly qualified into the joai segment upon entry into the inbound journey action. Wait 15 to 30 minutes for the values to be ingested into the Hub profile; if still not present, go to the next step, which is to contact Adobe Customer Care or your Adobe representative.
* **Q: What information should I provide when escalating?** — The step where you see the unexpected behavior, the journey version ID, the journey action ID, the full Assurance trace, and the JSON views of the Edge profile and the Hub profile.

**Related pages:**

* Troubleshooting errors before testing or publishing a journey: Troubleshoot errors before testing or publishing your journey (building-journeys/troubleshooting.md)
* Troubleshooting a live journey execution: Troubleshoot your live journey execution (building-journeys/troubleshooting-execution.md)
* Journey error codes: Error codes reference (building-journeys/error-codes-reference.md)

+++

<!-- ai-section-version: 1 | source-hash: 0d731a35 -->
