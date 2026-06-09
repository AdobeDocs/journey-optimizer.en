---
solution: Journey Optimizer
product: journey optimizer
title: Use custom actions
description: Learn how to use custom actions
feature: Journeys, Actions, Custom Actions
topic: Content Management
role: User, Developer
level: Intermediate
keywords: action, custom, API,journey, configuration, service
exl-id: 2b1b3613-3096-43ec-a860-600dda1d83b2
version: Journey Orchestration
TQID: https://experienceleague.adobe.com/Sw-hR0cfAG8Lk8YbhJKj53UqG-er2bC3-7Ijih0PF44
product_v2:
  - id: cb954087-f4fc-4456-afb9-e939cabcdc79
    internal-label: Journey Optimizer
feature_v2:
  - id: d998adac-2f81-400b-a669-d07bb196e4eb
    internal-label: Journeys
subfeature_v2:
  - id: c2beecbb-b93e-4ae3-baa9-72adcdc06781
    internal-label: Action configuration
  - id: fa683eda-48de-4558-af32-2673edcd44fe
    internal-label: Events
role_v2:
  - id: b69b2659-1057-424e-8fc5-ed9e016dc554
    internal-label: User
  - id: ff6a42d2-313e-452e-93a6-792e4fad9ff8
    internal-label: Developer
level_v2:
  - id: b5a62a22-46f7-4f0d-b151-3fc640bef588
    internal-label: Intermediate
topic_v2:
  - id: c7d04a2c-412a-4c9d-9d7a-4456eaa5adeb
    internal-label: Governance
  - id: e0eb8757-182f-49f3-94a4-1587d16f5094
    internal-label: Personalization
  - id: f4e6943a-c91a-4134-a2c7-f4f20cfff2f0
    internal-label: Privacy
---
# Use custom actions {#use-custom-actions}

>[!CONTEXTUALHELP]
>id="ajo_journey_action_custom"
>title="Custom actions"
>abstract="Custom actions enable you to configure connection of a third-party system to send messages or API calls. An action can be configured with any service from any provider that can be called through a REST API with a JSON-formatted payload."

Use custom actions to enable connection to a third-party system to send messages or API calls. An action can be configured with any service from any provider that can be called through a REST API with a JSON-formatted payload.

Learn more about custom actions in [this section](../action/action.md).

Learn how to create and configure a custom action on [this page](../action/about-custom-action-configuration.md).

Learn how to use API call responses from custom actions for personalization on [this page](../action/action-response.md).

## Consent and data governance {#privacy}

In Journey Optimizer, you can apply data governance and consent policies to your custom actions to prevent specific fields from being exported to third-party systems or exclude customers who have not consented to receive email, push or SMS communication. For more information, refer to the following pages:

* [Data governance](../action/action-privacy.md).
* [Consent](../action/consent.md).

## URL configuration

The configuration pane of the **Custom action** activity shows the URL configuration parameters and the authentication parameters that are configured for the custom action. You cannot set up the static part of the URL in the journey, but in the global configuration of the custom action. [Learn more](../action/about-custom-action-configuration.md).

### Dynamic path

If the URL includes a dynamic path, specify the path in the **[!UICONTROL Path]** field.

To concatenate fields and plain text strings, use the String functions or the Plus sign (+) in the advanced expression editor. Enclose plain text strings in single quotation marks (') or in double quotation marks ("). [Learn more](expression/expressionadvanced.md).

This table shows an example of configuration:

| Field | Value |
| --- | --- |
| URL | `https://xxx.yyy.com:8080/somethingstatic/` |
| Path | `The _id + '/messages'` |

The concatenated URL has this form:

`https://xxx.yyy.com:8080/somethingstatic/`\<ID>`/messages` 

![Custom action URL configuration with dynamic parameter mapping](assets/journey-custom-action-url.png)

### Headers and query parameters {#headers}

The **[!UICONTROL URL Configuration]** section shows the dynamic header and query parameter fields, but not the constant fields. Dynamic header and query parameter fields are defined as variable in the action configuration screen. [Learn more](../action/about-custom-action-configuration.md#url-configuration)

To specify the value of dynamic header and query parameter fields, click inside the field or on the pencil icon and select the desired field.

![Dynamic header field configuration in custom action](assets/journey-dynamicheaderfield.png)

## Action parameters

In the **[!UICONTROL Action parameters]** section, you'll see the message parameters defined as _"Variable"_. For these parameters, you can define where to get this information (example: events, data sources), pass values manually or use the advanced expression editor for advanced use cases. Advanced uses cases can be data manipulation and other function usage. Refer to this [page](expression/expressionadvanced.md).

+++AI Assistant — Page context

* **TL;DR:** This page explains how to add and configure a custom action activity in a journey to call a third-party REST API with a JSON payload, including URL configuration, header/query parameter mapping, action parameter mapping, and applying data governance and consent policies.

**Intents:**

* Add a custom action activity to a journey to send data to a third-party system via REST API
* Configure a dynamic URL path by concatenating fields and static text in the expression editor
* Map dynamic header and query parameter values from journey events or datasources
* Map action parameters (defined as Variable) to event fields, datasource fields, or static values
* Apply data governance and consent policies to control what data is exported via custom actions

**Glossary:**

* **Custom action**: A journey action activity that calls an external REST API endpoint with a JSON-formatted payload to integrate third-party systems *(product-specific)*
* **Dynamic path**: The variable portion of the custom action URL that is defined per-execution using fields from the journey context *(product-specific)*
* **Action parameters**: Message payload fields defined as "Variable" in the custom action configuration, mapped to journey data at the journey level *(product-specific)*

**Guardrails:**

* The static part of the URL cannot be modified in the journey; it must be set in the global custom action configuration.
* Dynamic header and query parameter fields are defined as variable in the action configuration screen, not in the journey.
* Data governance and consent policies can be applied to prevent specific fields from being exported or to exclude non-consented customers.

**Terminology:**

* Canonical name: Custom action — Acronym: none — variants: custom actions, third-party action
* Synonyms: "action parameters" = "message parameters defined as Variable"
* Do not confuse: "static URL part" (set in global action config, not editable in journey) ≠ "dynamic path" (set in the journey per-execution)

**FAQ:**

* **Q: Can I change the base URL of a custom action inside the journey?** — No, only the dynamic path portion can be set in the journey; the static part of the URL is configured in the global custom action configuration.
* **Q: How do I build a dynamic URL path that includes a profile ID?** — Use the Path field with the advanced expression editor to concatenate the ID field with static strings, for example: `_id + '/messages'`.
* **Q: How do I apply consent rules to a custom action?** — Configure consent policies on the custom action to exclude customers who have not consented to receive the relevant communication; refer to the Consent page for details.
* **Q: Where do I map the values for dynamic headers?** — In the URL Configuration section of the activity pane, click inside the dynamic header field or use the pencil icon to select the desired field from events or datasources.
* **Q: What types of values can I assign to action parameters?** — You can map parameters to event fields, datasource fields, pass values manually, or use the advanced expression editor for data manipulation.

+++
