---
title: AI Knowledge Reference
---
# AI Knowledge Reference

+++ AI Knowledge Reference

This section contains structured knowledge intended to support interpretation, retrieval, and question answering related to this topic.

For complete understanding, this information should be combined with the documentation on this page. Neither source is intended to stand alone; the page describes the feature, while this section provides additional context that helps disambiguate terminology, intent, applicability, and constraints.

* **TL;DR:** This page explains what the errors returned when you manage the API credentials of a custom channel, publish an inbound action, or add a dataset to the reporting configuration mean, and how to fix each family of errors.

**Intents:**

* Find the cause and the fix for a CJMRT, CJMIAS, or CJMRPS error
* Fix errors when activating, deactivating, naming, or deleting custom channel credentials
* Fix errors and warnings when publishing a campaign or a journey that uses an inbound action
* Fix errors when adding a dataset to the reporting configuration
* Know what to note and whom to contact when an error persists after the listed steps

**Glossary:**

* **CJMRT, CJMIAS, CJMRPS**: Error code prefixes for custom channels, inbound actions, and reporting; an error code is the prefix, an error number, and an HTTP status (for example CJMIAS-0024-400) *(product-specific)*
* **Inbound action**: Action published by a campaign or a journey; it can be a code-based experience, an in-app message, a content card, or a web action *(product-specific)*
* **Reporting configuration**: Configuration to which datasets are added for reporting *(product-specific)*

**Guardrails:**

* Journey Optimizer supports a maximum of 500 active inbound actions across live campaigns and live journeys (CJMIAS-0024-400). Stop the campaigns or journeys that use inbound actions you no longer need, then publish again.
* A new or updated edge audience can take up to one hour to activate. Until then, eligible profiles can be excluded (CJMIAS-0027-400, warning).
* A merge policy with the Active-On-Edge option enabled is needed to publish an inbound action (CJMIAS-0028-400).
* Credentials that are used by an active channel configuration cannot be deactivated (CJMRT-081517-403).
* Credentials cannot be activated while the associated custom channel is not active (CJMRT-081518-403).
* A reporting dataset must be an event-type dataset with at least one supported field group (Application Details, Commerce Details, or Web Details), in addition to the Experience Event - Proposition Interactions field group (CJMRPS-1046-400, 1048-400).
* The reporting configuration has a maximum number of datasets (CJMRPS-1049-400, message "The maximum limit of {limit} datasets has been reached."). Remove a dataset you do not use, then add the new one.

**Terminology:**

* Canonical name: Custom channel — variants: custom channel authentication, credentials (as in the error messages and fixes)
* Do not confuse: CJMRT (custom channels) ≠ CJMIAS (inbound actions) ≠ CJMRPS (reporting)

**FAQ:**

* **Q: How is an error code structured?** — A prefix (**CJMRT** for custom channels, **CJMIAS** for inbound actions, **CJMRPS** for reporting), followed by an error number and an HTTP status, for example CJMRPS-1049-400.
* **Q: Why can I not deactivate custom channel credentials?** — CJMRT-081517-403: the credentials are used by an active channel configuration. Update the channel configuration first, then deactivate the credentials.
* **Q: Why can I not activate custom channel credentials?** — CJMRT-081518-403: the custom channel is not active. Activate the custom channel first.
* **Q: Why can I not publish my inbound action?** — Depending on the message: the maximum number of live inbound actions is reached (CJMIAS-0024-400), no merge policy is active on the edge (0028-400), a decision policy is missing (0029-400), some fields are invalid or missing (0030-400), or the channel configuration is missing or uses a surface (0031-400).
* **Q: Why can I not add my dataset to the reporting configuration?** — Depending on the message: the dataset has no supported field group (CJMRPS-1046-400: select or create a dataset that has at least one), the schema of the dataset is not an event type (1048-400: select or create an event-type dataset), the maximum number of datasets is reached (1049-400), provisioning of the sandbox is pending (1041-404) or ARES provisioning is pending (1045-400), or the dataset is not found (1042-400). If the dataset has already been added (1047-409), no action is needed; to confirm, open the list of datasets in **[!UICONTROL Administration]** > **[!UICONTROL Configurations]** > **[!UICONTROL Reporting]** > **[!UICONTROL Manage]**.
* **Q: What do I do if the error persists after the listed steps?** — Note the error code, the message, the request ID, and the campaign, journey, or activity concerned, and keep the logs or screenshots. Then contact your administrator for a permission or access error, or contact Adobe Support with these details. For all the support options, see the Getting support section of the error codes reference.

**Troubleshooting:**

* **Custom channels**: CJMRT-081705-400 ("A custom channel authentication with the name \"{name}\" already exists. Please use a unique name and try again."): enter a unique name. CJMRT-081704-403: the status of the credentials does not allow the operation named in the message; in **[!UICONTROL Administration]** > **[!UICONTROL Channels]** > **[!UICONTROL Channel builder]** > **[!UICONTROL API credentials]**, check the status of the credentials and use an operation that this status allows. CJMRT-081707-403: the status transition named in the message is not allowed; check the current status of the credentials in the same location and use an allowed transition. CJMRT-081709-403: the credentials cannot be deleted in their current status; check the status of the credentials in the same location, then delete them once their status allows it.
* **Inbound actions**: CJMIAS-0027-400 (warning): wait up to one hour for the edge audience to activate. CJMIAS-0028-400: enable the Active-On-Edge option on a merge policy, then publish again. CJMIAS-0029-400: check the decision policies of the action and recreate those that were deleted. CJMIAS-0030-400: open the action and complete its fields. CJMIAS-0031-400: select a channel configuration instead of a surface.
* **Reporting datasets**: CJMRPS-1041-404, 1045-400 ("Provisioning is pending for sandbox." and "ARES provisioning is pending. Add dataset after provisioning is complete."): wait until provisioning completes, then click **[!UICONTROL Add dataset]** again from the **[!UICONTROL Dataset]** tab. CJMRPS-1042-400 ("Dataset not found."): check that the dataset exists in the sandbox, or create it before you add it.

**Related pages:**

* Custom channel credentials: Manage API credentials for custom channels (custom-channel/custom-channel-api-credentials.md)
* Activating a custom channel: Get started with custom channels (custom-channel/get-started-custom-channel.md)
* Inbound actions: Troubleshoot inbound actions (building-journeys/troubleshooting-inbound.md)
* Inbound action limits: Guardrails and limitations (start/guardrails.md)
* Reporting datasets: Reporting and experimentation prerequisites (reports/reporting-configuration.md)
* Edge audiences: Define the Action campaign audience (campaigns/campaign-audience.md)
* Merge policy for inbound actions: Code-based experience prerequisites (code-based/code-based-prerequisites.md)
* Decision policies: Create decisions policies (experience-decisioning/create-decision-policy.md)
* Other error code prefixes: Error codes reference (building-journeys/error-codes-reference.md)
* Support options when an error persists: Getting support (building-journeys/error-codes-reference.md#getting-support)
* Contacting Adobe Support: Support ticket guidelines (start/user-interface.md#support-ticket-guidelines)

+++

<!-- ai-section-version: 1 | source-hash: 715accb2 -->
