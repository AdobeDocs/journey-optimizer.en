---
title: AI Knowledge Reference
---
# AI Knowledge Reference

+++ AI Knowledge Reference

This section contains structured knowledge intended to support interpretation, retrieval, and question answering related to this topic.

For complete understanding, this information should be combined with the documentation on this page. Neither source is intended to stand alone; the page describes the feature, while this section provides additional context that helps disambiguate terminology, intent, applicability, and constraints.

* **TL;DR:** This page explains how to set up your app push credentials and create a Live activity channel configuration so Adobe Journey Optimizer is authorized to deliver real-time updates to your iOS app.

**Intents:**

* Add app push credentials (optional if already configured) using a .p8 Apple Push Notification Authentication Key, Key ID, and Team ID
* Reuse existing push credentials or make them available across sandboxes
* Create a Live activity channel configuration under Administration, Channels, General settings, Channel configurations
* Associate consent policies by selecting marketing action(s)
* Select iOS as Platform and the matching App id, then submit or save as draft

**Glossary:**

* **Push credential**: A registration required to authorize Adobe to send push notifications on your behalf *(product-specific)*
* **.p8 Apple Push Notification Authentication Key**: The key file dragged and dropped when manually entering push credentials
* **[!UICONTROL Key ID]**: A 10 character string assigned during creation of the .p8 auth key
* **[!UICONTROL Team ID]**: A string value found under the Membership tab
* **[!UICONTROL Apply to all sandboxes]**: An option that makes push credentials available across all sandboxes; sandbox-specific credentials for the same Platform and App ID pair take precedence *(product-specific)*
* **Channel configuration**: A configuration created under General settings to deliver messages through the Live activity channel *(product-specific)*
* **[!UICONTROL Marketing action(s)]**: A selection that associates consent policies to messages using the configuration *(product-specific)*
* **[!UICONTROL Processing]** / **[!UICONTROL Active]**: The statuses a channel configuration passes through; Active means it is ready to deliver messages *(product-specific)*

**Guardrails:**

* Step 1 (adding push credentials) is optional if push credentials are already configured, as they can be reused for the Live activity channel configuration.
* Configuration names must begin with a letter (A-Z) and can only contain alpha-numeric characters plus underscore, dot, and hyphen characters.
* If a specific sandbox has its own credentials for the same Platform and App ID pair, those sandbox-specific credentials take precedence over credentials applied to all sandboxes.
* All consent policies associated with the selected marketing action are leveraged in order to respect the preferences of your customers.
* The channel configuration is ready to deliver messages only once the checks are successful and it reaches the **[!UICONTROL Active]** status; if the checks are not successful, review the possible failure reasons in the channel surfaces documentation.

**Terminology:**

* Canonical name: Live activity channel configuration — Acronym: n/a — variants: channel configuration, Live activity configuration
* Synonyms: "App ID" = "App id" (the identifier for the mobile app, used for both the push credential and the channel configuration)
* Do not confuse: "[!UICONTROL Processing]" (status while the checks run) ≠ "[!UICONTROL Active]" (status once the checks are successful, ready to deliver)
* Do not confuse: "[!UICONTROL Key ID]" (10 character string for the .p8 auth key) ≠ "[!UICONTROL Team ID]" (string found under the Membership tab)

**FAQ:**

* **Q: Do I always need to create new push credentials?** — No; Step 1 is optional if push credentials are already configured, as they can be reused for the Live activity channel configuration.
* **Q: What are the naming rules for a configuration?** — Names must begin with a letter (A-Z) and can only contain alpha-numeric characters plus underscore, dot, and hyphen.
* **Q: Which platform do I select for a Live activity configuration?** — iOS, with the same App id as the push credential configured for the app.
* **Q: How do I associate consent to messages using this configuration?** — Select marketing action(s); all consent policies associated with the marketing action are leveraged to respect customer preferences.
* **Q: When is the configuration usable?** — Once the checks are successful and the channel configuration reaches the **[!UICONTROL Active]** status.
* **Q: What does Apply to all sandboxes do?** — It makes the push credentials available across all sandboxes; sandbox-specific credentials for the same Platform and App ID pair take precedence.

+++

<!-- ai-section-version: 1 | source-hash: dc335d03 -->
