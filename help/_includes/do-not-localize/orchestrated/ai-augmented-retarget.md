---
title: AI Knowledge Reference
---
# AI Knowledge Reference

+++ AI Knowledge Reference

This section contains structured knowledge intended to support interpretation, retrieval, and question answering related to this topic.

For complete understanding, this information should be combined with the documentation on this page. Neither source is intended to stand alone; the page describes the feature, while this section provides additional context that helps disambiguate terminology, intent, applicability, and constraints.

* **TL;DR:** This page explains how to build feedback-based and tracking-based retargeting rules in an Orchestrated campaign so you can follow up with recipients based on how they responded to a previous Orchestrated campaign.

**Intents:**

* Create a feedback-based retargeting rule using the Message Feedback schema to target recipients by delivery status (sent, opened, bounced, marked as spam).
* Create a tracking-based retargeting rule using the Email Tracking schema to target recipients by interaction (opens, clicks).
* Use the built-in Campaign feedback filter to quickly target recipients based on message delivery events.
* Target a specific previous campaign by selecting a specific campaign, referencing a campaign from a previous activity (Campaign from transition), or filtering by Campaign ID (UUID).
* Target a specific message or activity within an Orchestrated campaign using the Orchestrated Campaign Action Name attribute.
* Target recipients by the execution metadata added to a previous message with the executionMetadata helper function, using the metadata attribute (Message Execution folder) of the Message Feedback condition (Limited Availability).
* Combine a feedback-based retargeting rule with a tracking-based retargeting rule to refine targeting.

**Glossary:**

* **Message Feedback**: a schema that captures delivery-related events, such as message sent, opened, bounced, etc. *(product-specific)*
* **Email Tracking**: a schema that captures user actions, such as clicks and opens *(product-specific)*
* **Feedback-based retargeting rule**: a rule that retargets recipients based on message delivery events captured in the Message Feedback schema *(product-specific)*
* **Tracking-based retargeting rule**: a rule that targets recipients based on their interactions with a message, using data from the Email Tracking schema *(product-specific)*
* **Campaign feedback filter**: a built-in filter, selectable in the Rule Builder, used to quickly target recipients based on message delivery events by choosing a Behavior (such as Message sent, Message opened, or Message clicked) *(product-specific)*
* **Execution metadata**: custom key-value pairs added to a message with the executionMetadata helper function and stored with the Message Feedback events of that message *(product-specific)*
* **Feedback Status**: an attribute of the Message Feedback condition used to target a specific message delivery status *(product-specific)*
* **Interaction Type**: an attribute of the Email Tracking condition used to target a specific user interaction, such as Message Opened or Message Link Clicked *(product-specific)*
* **Orchestrated Campaign Name**: an attribute used to target a specific Orchestrated campaign by name *(product-specific)*
* **Orchestrated Campaign Action Name**: an attribute used to target a specific message or activity within an Orchestrated campaign *(product-specific)*

**Guardrails:**

* Feedback-based retargeting rules build custom conditions linked to the Message Feedback attribute; tracking-based retargeting rules build custom conditions linked to the Email Tracking attribute. Both rule types can also use the same built-in Campaign feedback filter as a quick-start option to target recipients based on message delivery events.
* Within the Campaign feedback filter, the Campaign from transition option references a campaign from a previous activity in the same Orchestrated campaign, as an alternative to selecting a specific campaign from the list.
* The Orchestrated Campaign Action Name can also be found by clicking the information icon next to the Label field of the activity.
* Targeting by execution metadata is only available for a set of organizations (Limited Availability). The metadata attribute is a map (key-value pairs): the condition is based on a key entered as free text, as written in the executionMetadata helper function.
* The Email Tracking interaction condition uses the "Included in" operator, with one or more values selected depending on the use case.

**Terminology:**

* Canonical name: Orchestrated campaign retargeting — variants: feedback-based retargeting rule, tracking-based retargeting rule
* Do not confuse: "Message Feedback" (delivery-related events: sent, opened, bounced, spam) ≠ "Email Tracking" (user interaction events: opens, clicks)
* Do not confuse: "execution metadata" (key-value pairs added to messages with the executionMetadata helper function, stored in Message Feedback events) ≠ "custom metadata fields" (business fields filled in the campaign properties)
* Do not confuse: "Select a specific campaign" (choose a particular campaign from a list) ≠ "Campaign from transition" (reference a campaign from a previous activity in the Orchestrated campaign)

**FAQ:**

* **Q: What is the difference between a feedback-based and a tracking-based retargeting rule?** — A feedback-based rule targets recipients using the Message Feedback schema (delivery events such as sent, opened, bounced, or marked as spam); a tracking-based rule targets recipients using the Email Tracking schema (user interactions such as opens and clicks).
* **Q: Can I use the same filter to start both types of retargeting rules?** — Yes, both rule types can use the built-in Campaign feedback filter to target recipients based on message delivery events, selecting a Behavior such as Message sent, Message opened, or Message clicked.
* **Q: How can I target a specific previous campaign?** — Select a specific campaign from your list, reference a campaign from a previous activity using Campaign from transition, or filter by Campaign ID (UUID) found in your Campaign properties.
* **Q: How do I target a specific message or activity within an Orchestrated campaign?** — Use the Orchestrated Campaign Action Name attribute; action names can be found by clicking the information icon next to the Label field of the activity.
* **Q: Can I retarget recipients based on the execution metadata of a previous message?** — Yes, in Limited Availability. In a feedback-based retargeting rule, add a condition on the Message Feedback attribute, select the metadata attribute in the Message Execution folder, enter the metadata key used in the executionMetadata helper function, select an operator (equal to, not equal to, key exists, key does not exist, contains, or does not contain), and enter a value if needed.
* **Q: Can I combine feedback-based and tracking-based retargeting rules?** — Yes, you can combine a tracking-based retargeting rule with a feedback-based retargeting rule to include message outcomes such as sent, bounced, or marked as spam.

**Personas:**

* **marketer:** Can build a feedback-based retargeting rule using the Message Feedback attribute and choose a delivery status to track with the Feedback Status attribute. Can build a tracking-based retargeting rule using the Email Tracking attribute and the Interaction Type attribute with the Included in operator. The page states that a specific campaign can be targeted by selecting a campaign, using Campaign from transition, or filtering by Campaign ID (UUID). Where: "Create a feedback-based retargeting rule".

**Onboarding:**

* **Level:** Intermediate
* **First minimal step:** Create a new Orchestrated campaign.
* **Success check:** You have configured a feedback-based retargeting rule to identify recipients by delivery status, such as sent, opened, bounced, or marked as spam.

+++

<!-- ai-section-version: 1 | source-hash: 0f53cb19 -->
