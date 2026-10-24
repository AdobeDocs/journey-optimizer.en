---
title: AI Knowledge Reference
---
# AI Knowledge Reference

+++ AI Knowledge Reference

This section contains structured knowledge intended to support interpretation, retrieval, and question answering related to this topic.

For complete understanding, this information should be combined with the documentation on this page. Neither source is intended to stand alone; the page describes the feature, while this section provides additional context that helps disambiguate terminology, intent, applicability, and constraints.

* **TL;DR:** This page explains how administrators use the Send test request capability to validate custom action configurations by making real API calls directly from Journey Optimizer, before or after using them in a journey.

**Intents:**

* Send a real test API call to validate a custom action configuration
* Provide the correct payload depending on whether the method is GET or POST
* Enter the authentication details required for each test request
* Understand the benefits of in-product testing compared to external tools
* Check what to verify when a test request fails
* Diagnose discard events and idle timeouts when a custom action in one journey triggers an event meant to start a second journey

**Glossary:**

* **Send test request**: The capability administrators use to validate custom action configurations by making real API calls directly from Adobe Journey Optimizer, checking the request structure, headers, authentication, and payload *(product-specific)*
* **AJO Journey**: The executor of the test request; the exact request structure (including Adobe Journey Optimizer specific headers) is used, and the source IP and headers match those used in live journeys *(product-specific)*
* **Discard event**: An event that is received but discarded when it does not meet the second journey's entry conditions, appearing in logs with codes such as `notSuitableInitialEvent` *(product-specific)*
* **Idle timeout**: A timeout that may occur if the second journey is not ready, leading to discard events in the logs *(product-specific)*
* **IP (egress) proxy**: When enabled for your organization, it is bypassed by the Send test request call *(product-specific)*

**Guardrails:**

* If the custom action method is GET, no payload is required; if the method is POST, you must provide a JSON payload.
* Adobe Journey Optimizer raises an error if the structure of the JSON is incorrect, but not if there is a mismatch with a data type; for instance, no error is raised if an integer parameter is used for what should be a string.
* The Send test request call bypasses the IP (egress) proxy if your organization has it enabled; to confirm proxy routing, run a test or live journey.
* For each test request, Adobe Journey Optimizer requires the user to enter authentication details if the custom action includes authentication.
* For chained journeys, ensure the second journey is published or in test mode before the custom action is triggered, and within its active date window.

**Prerequisites and permissions:**

* A custom action pre-configured with a URL, headers, and authentication settings.
* The **Manage journeys events, data sources and actions** permission, which is included in the Journey Administrators role; the **View journeys events** permission alone is not sufficient.

**Terminology:**

* Canonical name: Send test request — variants: test request, in-product troubleshooting capability
* Do not confuse: "Basic Authentication" (the user provides the password) ≠ "API Key Authentication" (the user enters the API key value) ≠ "Custom Authentication" (the user supplies the authentication parameters in the request bodyParam, and the sections Authentication request and Authentication response are added)
* Do not confuse: "GET" method (no payload required) ≠ "POST" method (JSON payload required)

**FAQ:**

* **Q: What does the Send test request capability do?** — It validates custom action configurations by making real API calls directly from Adobe Journey Optimizer, ensuring the request structure, headers, authentication, and payload are correctly formatted before being used in a journey.
* **Q: What permissions are required?** — The Manage journeys events, data sources and actions permission, included in the Journey Administrators role; the View journeys events permission alone is not sufficient.
* **Q: Do I need a payload for the test request?** — If the custom action method is GET, no payload is required; if the method is POST, you must provide a JSON payload.
* **Q: Does Journey Optimizer validate the payload data types?** — It raises an error if the JSON structure is incorrect, but not if there is a data type mismatch, so an integer used where a string is expected does not raise an error.
* **Q: Can I use this capability for live journeys?** — Yes, the Send test request capability can be used for troubleshooting live journeys, as the custom action is already deployed.
* **Q: Why is an event discarded when a custom action triggers a second journey?** — If the event does not meet the second journey's entry conditions, it can be discarded and appear in logs with codes such as `notSuitableInitialEvent`; idle timeouts may occur if the second journey is not ready, leading to discard events in the logs.

**Troubleshooting:**

* A test request fails: check the authentication credentials entered in the test, the request method (GET vs. POST) and corresponding payload, and the API endpoint and headers defined in the custom action; use the response data to identify potential misconfigurations.
* Event discarded (`notSuitableInitialEvent`), event qualification not met: the second journey uses a rule-based event with a qualification condition (for example, `isNotEmpty` on a specific field) and the event payload does not satisfy it, so the event is received but discarded and the second journey is not triggered; the page describes this as expected behavior. Verify that the payload sent by the custom action includes all fields and values required by the second journey's event configuration.
* Idle timeout, second journey not ready: the second journey is not yet active (for example, not in test mode or not live), or there is a timing gap between the custom action firing and the second journey being ready to receive. Ensure the target journey is published or in test mode before the custom action is triggered.
* Discard events in logs: check journey logs and Splunk traces to confirm whether the event was received but discarded due to qualification or timing; ensure the second journey's start date and configuration are correct and that the journey is within its active date window.

**Related pages:**

* Learning what a custom action is: Get started with custom actions (action/action.md)
* Creating and configuring a custom action: Configure your custom actions (action/about-custom-action-configuration.md)
* Using custom actions in journeys: Use custom actions (building-journeys/using-custom-actions.md)
* Passing a collection in custom action parameters: Pass collections into custom action parameters (building-journeys/collections.md)
* IP (egress) proxy and enablement: Integrate with external systems (configuration/external-systems.md)
* Configuring rule-based events: Configure rule-based events (event/about-creating.md)
* Troubleshooting event reception in journey execution: Troubleshoot your live journey execution (building-journeys/troubleshooting-execution.md)
* Journey permissions: Permission levels (administration/high-low-permissions.md)

+++

<!-- ai-section-version: 2 | source-hash: 0b5cc032 -->
