---
solution: Journey Optimizer
product: journey optimizer
title: [!DNL Adobe Campaign] v7/v8 actions
description: Learn about [!DNL Adobe Campaign] v7/v8 actions
feature: Journeys, Actions, Custom Actions
topic: Administration
role: User
level: Intermediate
keywords: journey, integration, campaign, v7, v8
exl-id: 3da712e7-0e08-4585-8ca4-b6ff79df0b68
version: Journey Orchestration
---
# [!DNL Adobe Campaign] v7/v8 actions {#using_campaign_v7-v8} 

>[!CONTEXTUALHELP]
>id="ajo_journey_action_custom_acc"
>title="Custom actions"
>abstract="An integration is available if you have [!DNL Adobe Campaign] v7 or v8. It allows you to send emails, push notifications and SMS using [!DNL Adobe Campaign] Transactional Messaging capabilities."

An integration is available if you have [!DNL Adobe Campaign] v7 or v8. It allows you to send emails, push notifications and SMS using [!DNL Adobe Campaign] Transactional Messaging capabilities.

The connection between the Journey Optimizer and Campaign instances is setup by Adobe at provisioning time. Contact Adobe.

**When to use**: Use Campaign v7/v8 actions when your messaging relies on Campaign transactional templates, Campaign-specific data models, or existing Campaign delivery workflows.

**Prerequisites**

* Your [!DNL Adobe Campaign] v7/v8 instance is provisioned and connected to Journey Optimizer by Adobe.
* You have access to Campaign Transactional Messaging and the required permissions.

For this to work, you need to configure a dedicated action. Refer to this [section](../action/acc-action.md).

An end-to-end use case is presented in this [section](../building-journeys/ajo-ac.md).

1. Design your journey, starting with an event. See this [section](../building-journeys/journey.md).
1. In the **Action** section of the palette, select a Campaign action and add it to your journey.
1. In the **Action parameters**, all the fields expected in the message payload are displayed. You need to map each of these fields with the field you want to use, either from the event or from the data source. This is similar to custom actions. Refer to this [section](../building-journeys/using-custom-actions.md).

>[!NOTE]
>
>* Campaign v7/v8 actions can be used alongside native channel actions in the same journey. This does not apply to Campaign Standard actions. See [Campaign activity guardrails](../start/guardrails.md#ac-g).
>* Campaign v7/v8 actions cannot be used with Read Audience or Audience Qualification activities. See the Read Audience and Audience Qualification guardrails in the Guardrails page.

![[!DNL Adobe Campaign] v7/v8 action configuration and integration settings](assets/accintegration2.png)
