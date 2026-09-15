---
title: AI Knowledge Reference
---
# AI Knowledge Reference

+++ AI Knowledge Reference

This section contains structured knowledge intended to support interpretation, retrieval, and question answering related to this topic.

For complete understanding, this information should be combined with the documentation on this page. Neither source is intended to stand alone; the page describes the feature, while this section provides additional context that helps disambiguate terminology, intent, applicability, and constraints.

* **TL;DR:** This page explains how to manage recipient opt-out from communications and opt-out from personalization in Journey Optimizer so you can honor consent choices and meet your legal and brand-reputation obligations.

**Intents:**

* Manage unsubscriptions in journeys and campaigns
* Check a profile's push opt-out status in Adobe Experience Platform
* Understand how consent is handled through the Experience Platform Consent schema
* Implement personalization consent in decision management and campaigns
* Use the segment rule builder or a split activity to filter out profiles that have not consented to personalization

**Glossary:**

* **Opt-out**: recipient action to unsubscribe from communications; once unsubscribed, profiles are automatically removed from the audience of future marketing messages *(product-specific)*
* **Suppression REST API**: API used to control outgoing messages using suppression and allow lists *(product-specific)*
* **Push token**: token whose presence on a profile indicates implicit push consent, and which is removed when a user disables notifications at the device level *(product-specific)*
* **`consents.marketing.push.val`**: attribute used for explicit push consent tracking, where `y` indicates explicit opt-in and `n` indicates explicit opt-out *(product-specific)*
* **Consent schema**: Experience Platform schema that handles consent; by default the value is empty and treated as consent to receive communications *(product-specific)*
* **Consent policies**: used to override the default consent logic *(product-specific)*
* **`profile.consents.personalize.content.val`**: personalization consent attribute used in a split activity, where `n` signifies that users do not consent to the use of their data for personalization *(product-specific)*

**Guardrails:**

* Providing recipients the capability to unsubscribe from communications is a legal requirement, as is ensuring this choice is honored
* Journey Optimizer provides ways of managing opt-out in email and SMS messages; push notifications do not require any action on your side, as recipients can unsubscribe through their devices
* By default, the value for the consent field is empty and treated as consent to receive communications; you can modify this default value while onboarding, or use consent policies to override the default logic
* In decision management, personalization preferences are not automatically implemented in decision scopes used from a decisioning API or edge decisioning API request; you must manually enforce personalization consent
* Decision scopes used in Journey Optimizer authored channels satisfy the personalization consent requirement from the journey or campaign they belong to
* Consent for having profile data used in data modeling is not supported yet in Journey Optimizer
* The personalization editor does not perform any consent checks or enforcement, as it is not involved in the delivery of messages
* The Journey Optimizer campaign object itself does not perform any additional consent policy enforcement checks at this time
* The message preview and email rendering service mask the fields identified with sensitive information

**Terminology:**

* Canonical name: Opt-out
* Do not confuse: "opt-out from communications" (unsubscribe from receiving messages) ≠ "opt-out from personalization" (excluding a profile's data from being used for personalized content)
* Do not confuse: "`consents.marketing.push.val`" (explicit push consent attribute) ≠ "presence of a push token" (indicator of implicit push consent)
* Do not confuse: "[!UICONTROL Personalize Content = Yes (opt-in)]" ≠ "[!UICONTROL Personalize Content = No (opt-out)]"

**FAQ:**

* **Q: What happens once a recipient unsubscribes?** — The profile is automatically removed from the audience of future marketing messages.
* **Q: Do push notifications require opt-out action in Journey Optimizer?** — No, recipients can unsubscribe through their devices, and push opt-out is handled at the device level.
* **Q: How do you check whether a profile has opted out of push?** — In Adobe Experience Platform, open the profile, go to the [!UICONTROL Attributes] tab, and look at the [!UICONTROL Push Notification Details] field group; the presence of a push token indicates implicit consent, and no token indicates opt-out at the device level.
* **Q: How is consent handled by default?** — Through the Experience Platform Consent schema, where the default empty value is treated as consent; this can be changed at onboarding or overridden with consent policies.
* **Q: Is consent for data modeling supported?** — No, consent for having profile data used in data modeling is not supported yet in Journey Optimizer.
* **Q: How do you enforce personalization consent for a campaign?** — Include consent policy definitions as part of audience creation, or build an audience with the segment rule builder or a split activity to filter out profiles that have not consented to personalization.

+++

<!-- ai-section-version: 1 | source-hash: 444221fd -->
