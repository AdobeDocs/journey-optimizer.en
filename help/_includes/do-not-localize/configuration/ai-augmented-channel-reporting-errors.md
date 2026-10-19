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

**Glossary:**

* **CJMRT, CJMIAS, CJMRPS**: Error code prefixes for custom channels, inbound actions, and reporting; an error code is the prefix, an error number, and an HTTP status (for example CJMIAS-0024-400) *(product-specific)*
* **Inbound action**: Action published by a campaign or a journey; it can be a code-based experience, an in-app message, a content card, or a web action *(product-specific)*
* **Reporting configuration**: Configuration to which datasets are added for reporting *(product-specific)*

**Guardrails:**

* An organization can have a maximum of 500 live inbound actions across campaigns and journeys (CJMIAS-0024-400). Stop campaigns or journeys that use inbound actions you no longer need.
* A new or updated edge audience can take up to one hour to activate. Until then, eligible profiles can be excluded (CJMIAS-0027-400, warning).
* A merge policy with the Active-On-Edge option enabled is needed to publish an inbound action (CJMIAS-0028-400).
* Credentials that are used by an active channel configuration cannot be deactivated (CJMRT-081517-403).
* Credentials cannot be activated while the associated custom channel is not active (CJMRT-081518-403).
* A reporting dataset must be an event-type dataset with at least one supported field group (Application Details, Commerce Details, or Web Details), in addition to the Experience Event - Proposition Interactions field group (CJMRPS-1046-400, 1048-400).
* The reporting configuration has a maximum number of datasets (CJMRPS-1049-400, message "The maximum limit of {limit} datasets has been reached."). Remove a dataset you do not use, then add the new one.

**Terminology:**

* Canonical name: Custom channel — variants: custom channel authentication, credentials (as in the error messages and fixes)
* Canonical name: Channel configuration — variants: surface, channel surface (as in the error messages)
* Do not confuse: CJMRT (custom channels) ≠ CJMIAS (inbound actions) ≠ CJMRPS (reporting)

**FAQ:**

* **Q: How is an error code structured?** — A prefix (**CJMRT** for custom channels, **CJMIAS** for inbound actions, **CJMRPS** for reporting), followed by an error number and an HTTP status, for example CJMRPS-1049-400.
* **Q: Why can I not deactivate custom channel credentials?** — CJMRT-081517-403: the credentials are used by an active channel configuration. Update the channel configuration first, then deactivate the credentials.
* **Q: Why can I not activate custom channel credentials?** — CJMRT-081518-403: the custom channel is not active. Activate the custom channel first.
* **Q: Why can I not publish my inbound action?** — Depending on the message: the maximum number of live inbound actions is reached (CJMIAS-0024-400), no merge policy is active on the edge (0028-400), a decision policy is missing (0029-400), some fields are invalid or missing (0030-400), or the channel configuration is missing or uses a surface (0031-400).
* **Q: Why can I not add my dataset to the reporting configuration?** — Depending on the message: the dataset has no supported field group or is not event type (CJMRPS-1046-400, 1048-400), the maximum number of datasets is reached (1049-400), provisioning of the sandbox is pending (1041-404, 1045-400), or the dataset is not found (1042-400). If the dataset has already been added (1047-409), no action is needed.

**Troubleshooting:**

* **Custom channels**: CJMRT-081705-400 ("A custom channel authentication with the name \"{name}\" already exists. Please use a unique name and try again."): enter a unique name. CJMRT-081704-403, 081707-403, 081709-403: the status of the credentials does not allow the action (change, status transition, or deletion); check the status of the credentials and use an allowed transition.
* **Inbound actions**: CJMIAS-0027-400 is described as a warning on the page. CJMIAS-0028-400: enable the Active-On-Edge option on a merge policy, then publish again. CJMIAS-0029-400: check the decision policies of the action and recreate those that were deleted. CJMIAS-0030-400: open the action and complete its fields. CJMIAS-0031-400: select a channel configuration.
* **Reporting datasets**: CJMRPS-1041-404, 1045-400 ("Provisioning is pending for sandbox." and "ARES provisioning is pending. Add dataset after provisioning is complete."): wait until provisioning completes, then add the dataset. CJMRPS-1042-400 ("Dataset not found."): check that the dataset exists in the sandbox.

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

+++

<!-- ai-section-version: 1 | source-hash: 45b5d89a -->
