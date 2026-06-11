---
solution: Journey Optimizer
product: journey optimizer
title: Send a message using Campaign v7/v8
description: Learn how to send a message using Campaign v7/v8
feature: Journeys, Integrations, Custom Actions, Use Cases
topic: Administration
role: Admin, Developer, User
level: Intermediate, Experienced
keywords: journey, message, campaign, integration
exl-id: b07feb98-b2ae-476c-8fcb-873b308176f0
version: Journey Orchestration
TQID: https://experienceleague.adobe.com/btOUMO8tgvwLD7kjVdgpj6I6QXRrj1iTD3P8AUrqJFM
product_v2:
  - id: cb954087-f4fc-4456-afb9-e939cabcdc79
    internal-label: Journey Optimizer
feature_v2:
  - id: d998adac-2f81-400b-a669-d07bb196e4eb
    internal-label: Journeys
subfeature_v2:
  - id: c2beecbb-b93e-4ae3-baa9-72adcdc06781
    internal-label: Action configuration
  - id: d08afb72-92f6-4856-88e3-11ec34313c2f
    internal-label: Event configuration
role_v2:
  - id: b69b2659-1057-424e-8fc5-ed9e016dc554
    internal-label: User
  - id: c66ffd68-0f65-42bb-aa23-b4020f12e0bd
    internal-label: Admin
  - id: ff6a42d2-313e-452e-93a6-792e4fad9ff8
    internal-label: Developer
level_v2:
  - id: b5a62a22-46f7-4f0d-b151-3fc640bef588
    internal-label: Intermediate
topic_v2:
  - id: e0eb8757-182f-49f3-94a4-1587d16f5094
    internal-label: Personalization
  - id: eddd9b14-83bd-4ff4-9072-54a4a484abb7
    internal-label: Administration
---
# Send a message with Campaign v7/v8 {#campaign-v7-v8-use-case}

This use case explains all the steps required to send an email using the integration with [!DNL Adobe Campaign] v7 and [!DNL Adobe Campaign] v8.

>[!NOTE]
>
>In order to use this integration, you must have Campaign v7/v8 build 9125 or higher.

First, create a transactional email template in Campaign. Then, in Journey Optimizer, create the event, action, and design the journey.

To learn more about the Campaign integration, refer to these pages:

* [Creating a Campaign action](../action/acc-action.md)
* [Using the action in a journey](../building-journeys/using-adobe-campaign-v7-v8.md).

**[!DNL Adobe Campaign]**

Your Campaign instance must be provisioned for this integration. The Transactional Messaging feature must be configured.

1. Log in to your Campaign control instance. 

1. Under **Administration** > **Platform** > **Enumerations**, select the **Event type** (eventType) enumeration. Create a new event type ("journey-event", in our example). Use the internal name of the event type when writing the JSON file later. 

    ![Configure an event in [!DNL Adobe Journey Optimizer] with schema and field selection](assets/accintegration-uc-1.png)

1. Disconnect and reconnect to the instance for the creation to take effect.

1. Under **Message Center** > **Transactional message templates**, create a new email template based on the event type previously created.

    ![Event configuration showing namespace and profile identifier settings](assets/accintegration-uc-2.png)

1. Design your template. In this example, personalization is applied to the profile's first name and the order number. The first name is in the [!DNL Adobe Experience Platform] data source, and the order number is a field from the Journey Optimizer event. Ensure you use the correct field names in Campaign. 

    ![Event payload preview showing JSON structure with profile and event data](assets/accintegration-uc-3.png)

1. Publish your transactional template.

    ![Event copy button to copy payload ID for API integration](assets/accintegration-uc-4.png)

1. Write the JSON payload corresponding to the template. 

```
{
     "channel": "email",
     "eventType": "journey-event",
     "email": "Email address",
     "ctx": {
          "firstName": "First name", "purchaseOrderNumber": "Purchase order number"
     }
}
```

* For the channel, you need to type "email".
* For the eventType, use the internal name of the event type created previously.
* The email address will be a variable, so you can type any label.
* Under ctx, the personalization fields are also variables.

**Journey Optimizer**

1. Create an event. Include the "purchaseOrderNumber" field.

    ![Custom action configuration screen for [!DNL Adobe Campaign] Classic integration](assets/accintegration-uc-5.png)

1. Create an action in Journey Optimizer corresponding to your Campaign template. In the **Action type** drop-down, select **[!DNL Adobe Campaign] Classic**. 

    ![Action type selection showing [!DNL Adobe Campaign] Classic option](assets/accintegration-uc-6.png)

1. Click the **Payload field** and paste the JSON created earlier.

    ![Campaign account selection dropdown for action integration](assets/accintegration-uc-7.png)

1. For the email address and the two personalization fields, change **Constant** to **Variable**.

    ![Action payload configuration with field mapping for Campaign integration](assets/accintegration-uc-8.png)

1. Now create a new journey and start with the event previously created.

    ![Journey canvas with event and Campaign action configured](assets/accintegration-uc-9.png)

1. Add the action and map each field to the correct field in Journey Optimizer. 

    ![Action parameter mapping with expression editor for dynamic values](assets/accintegration-uc-10.png)

1. Test your journey.

    ![Complete journey flow with event trigger and Campaign action execution](assets/accintegration-uc-11.png)

1. You can now publish your journey.

+++AI Assistant — Page context

* **TL;DR:** This page provides a step-by-step use case for sending a transactional email from Adobe Journey Optimizer using the integration with Adobe Campaign v7/v8, covering Campaign template creation, event and action configuration, and journey design.

**Intents:**
* Configure a transactional email template in Adobe Campaign v7/v8 for use with Journey Optimizer
* Create an event in Journey Optimizer that includes custom fields such as a purchase order number
* Create and configure a Campaign Classic action in Journey Optimizer with a JSON payload
* Map journey event fields to Campaign personalization variables in the action configuration
* Build and publish a journey that triggers a Campaign transactional email

**Glossary:**
* **Transactional Messaging**: A Campaign feature that sends real-time, triggered emails based on events; must be configured before this integration can be used *(product-specific)*
* **Event type (eventType)**: An enumeration value defined in Campaign that identifies the type of transactional event; its internal name is referenced in the JSON payload *(product-specific)*
* **Campaign Classic action**: A Journey Optimizer action type that connects to Adobe Campaign v7/v8 to send transactional messages *(product-specific)*
* **Payload field**: The JSON structure pasted into a Journey Optimizer action that defines the data fields sent to Campaign *(product-specific)*

**Guardrails:**
* Campaign v7/v8 build 9125 or higher is required for this integration
* The Transactional Messaging feature must be configured in the Campaign instance before use
* After creating a new event type in Campaign, you must disconnect and reconnect to the instance for it to take effect
* Personalization field values set as "Constant" in the action must be changed to "Variable" to allow dynamic population at runtime

**Terminology:**
* Canonical name: Adobe Campaign v7/v8 — Acronym: ACC — variants: Campaign Classic, Campaign v7, Campaign v8
* Synonyms: "eventType" = "event type internal name"
* Do not confuse: "Campaign Classic action" ≠ "custom action" (Campaign Classic action is a specific built-in action type for ACC integration)

**FAQ:**
* **Q: What Campaign version is required for this integration?** — Campaign v7/v8 build 9125 or higher is required.
* **Q: What must be configured in Campaign before starting?** — The Transactional Messaging feature must be configured and a transactional email template must be created based on the event type.
* **Q: How do I make personalization fields dynamic in the Journey Optimizer action?** — In the action payload configuration, change the field configuration from "Constant" to "Variable" for fields that will be populated at runtime.
* **Q: Where does the first name personalization data come from in this use case?** — The first name comes from the Adobe Experience Platform data source, while the order number comes from the Journey Optimizer event payload.
* **Q: How do I connect the Journey Optimizer action to the Campaign template?** — Select "Adobe Campaign Classic" as the Action type, then paste the JSON payload that matches the transactional message template structure.

+++
