---
solution: Journey Optimizer
product: journey optimizer
title: Adobe Campaign v7/v8 actions
description: Learn about Adobe Campaign v7/v8 actions
feature: Journeys, Actions, Custom Actions
topic: Administration
role: User
level: Intermediate
keywords: journey, integration, campaign, v7, v8
exl-id: 3da712e7-0e08-4585-8ca4-b6ff79df0b68
version: Journey Orchestration
TQID: https://experienceleague.adobe.com/Saqu6Kkm1Rdym10IuwLF88Fj-hT2crAwENajyKBeY5w
product_v2:
  - id: cb954087-f4fc-4456-afb9-e939cabcdc79
    internal-label: Journey Optimizer
feature_v2:
  - id: b3538224-471e-4c63-a444-9b19d89ae29c
    internal-label: Activities
  - id: d998adac-2f81-400b-a669-d07bb196e4eb
    internal-label: Journeys
subfeature_v2:
  - id: c2beecbb-b93e-4ae3-baa9-72adcdc06781
    internal-label: Action configuration
  - id: cfba2953-2ce9-4b00-a00c-71cd338ae63f
    internal-label: Custom actions
role_v2:
  - id: b69b2659-1057-424e-8fc5-ed9e016dc554
    internal-label: User
level_v2:
  - id: b5a62a22-46f7-4f0d-b151-3fc640bef588
    internal-label: Intermediate
topic_v2:
  - id: eddd9b14-83bd-4ff4-9072-54a4a484abb7
    internal-label: Administration
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

+++AI Assistant — Page context

* **TL;DR:** This page explains how to use Adobe Campaign v7/v8 as an action in Journey Optimizer journeys to send emails, push notifications, and SMS via Campaign Transactional Messaging.

**Intents:**

* Add a Campaign v7/v8 action to a journey to send transactional messages
* Map journey event or datasource fields to the Campaign message payload parameters
* Combine Campaign v7/v8 actions with native Journey Optimizer channel actions in the same journey
* Configure the dedicated action required for the Campaign v7/v8 integration

**Glossary:**

* **Campaign Transactional Messaging**: Adobe Campaign v7/v8 capability for sending triggered messages (email, SMS, push) via a dedicated action integrated with Journey Optimizer *(product-specific)*
* **Action parameters**: Fields in the journey activity pane that map journey data to the expected Campaign message payload *(product-specific)*

**Guardrails:**

* The connection between Journey Optimizer and the Campaign instance is set up by Adobe at provisioning time; contact Adobe to enable it.
* A dedicated action must be configured before Campaign v7/v8 actions are available in the journey palette.
* Campaign v7/v8 actions cannot be used with Read Audience or Audience Qualification activities.
* Access to Campaign Transactional Messaging and the required permissions in Campaign are prerequisites.

**Terminology:**

* Canonical name: Adobe Campaign v7/v8 — Acronym: ACC — variants: Campaign v7, Campaign v8, Campaign Classic
* Do not confuse: "Campaign v7/v8 actions" (can be used alongside native actions) ≠ "Campaign Standard actions" (cannot be combined with native actions in the same journey)

**FAQ:**

* **Q: Who sets up the connection between Journey Optimizer and Campaign v7/v8?** — Adobe sets up the connection at provisioning time; you must contact Adobe to have it configured.
* **Q: Can Campaign v7/v8 actions be combined with native Journey Optimizer channel actions in the same journey?** — Yes, Campaign v7/v8 actions can be used alongside native channel actions; this is not the case for Campaign Standard actions.
* **Q: Can Campaign v7/v8 actions be used with Read Audience or Audience Qualification activities?** — No, Campaign v7/v8 actions cannot be used with Read Audience or Audience Qualification activities.
* **Q: How do I map journey data to the Campaign message payload?** — In the Action parameters pane, map each expected payload field to the corresponding field from the journey event or datasource, the same way as custom actions.

+++
