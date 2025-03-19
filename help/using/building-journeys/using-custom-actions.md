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
---
# Use custom actions {#use-custom-actions}

>[!CONTEXTUALHELP]
>id="ajo_journey_action_custom"
>title="Custom actions"
>abstract="Custom actions enable you to configure connection of a third-party system to send messages or API calls. An action can be configured with any service from any provider that can be called through a REST API with a JSON-formatted payload."

Use custom actions to enable connection to a third-party system to send messages or API calls. An action can be configured with any service from any provider that can be called through a REST API with a JSON-formatted payload.

Learn more about custom actions in [this section](../action/action.md).

Learn how to create and configure a custom action in [this page](../action/about-custom-action-configuration.md).

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

![](assets/journey-custom-action-url.png)

### Headers and query parameters {#headers}

The **[!UICONTROL URL Configuration]** section shows the dynamic header and query parameter fields, but not the constant fields. Dynamic header and query parameter fields are defined as variable in the action configuration screen. [Learn more](../action/about-custom-action-configuration.md#url-configuration)

To specify the value of dynamic header and query parameter fields, click inside the field or on the pencil icon and select the desired field.

![](assets/journey-dynamicheaderfield.png)

## Action parameters

In the **[!UICONTROL Action parameters]** section, you'll see the message parameters defined as _"Variable"_. For these parameters, you can define where to get this information (example: events, data sources), pass values manually or use the advanced expression editor for advanced use cases. Advanced uses cases can be data manipulation and other function usage. Refer to this [page](expression/expressionadvanced.md).

