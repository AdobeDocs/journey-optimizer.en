---
solution: Journey Optimizer
product: journey optimizer
title: Adobe Campaign Standard actions
description: Learn about Adobe Campaign Standard actions
feature: Journeys, Actions, Custom Actions
topic: Administration
role: User
level: Intermediate
keywords: journey, integration, standard, campaign, ACS
exl-id: 50565cd9-7415-4c6a-9651-24fefeded3f5
version: Journey Orchestration
TQID: https://experienceleague.adobe.com/spxxZT-JH5yzziL8-oSkJdBcKEppm-4ZzeLC2-laCaM
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
  - id: d8353d85-5da7-453d-bd68-40ad33fa0ab7
    internal-label: Action activities
  - id: fa683eda-48de-4558-af32-2673edcd44fe
    internal-label: Events
role_v2:
  - id: b69b2659-1057-424e-8fc5-ed9e016dc554
    internal-label: User
level_v2:
  - id: b5a62a22-46f7-4f0d-b151-3fc640bef588
    internal-label: Intermediate
topic_v2:
  - id: b5ce8718-c3af-4fdb-a1a9-fca32f83a87c
    internal-label: Implementation
  - id: e0eb8757-182f-49f3-94a4-1587d16f5094
    internal-label: Personalization
  - id: eddd9b14-83bd-4ff4-9072-54a4a484abb7
    internal-label: Administration
---
# [!DNL Adobe Campaign] Standard actions {#using_campaign_action}

>[!BEGINSHADEBOX]

**On this page:** Learn how to use the built-in Adobe Campaign Standard email, push, and SMS action activities in your journeys by relying on Campaign Standard Transactional Messaging templates.

>[!ENDSHADEBOX]

>[!CONTEXTUALHELP]
>id="ajo_journey_action_custom_acs"
>title="Custom actions"
>abstract="An integration is available if you have [!DNL Adobe Campaign] Standard. It allows you to send emails, push notifications and SMS using [!DNL Adobe Campaign] Transactional Messaging capabilities."

If you have [!DNL Adobe Campaign] Standard, the following built-in action activities are available: **[!UICONTROL Email]**, **[!UICONTROL Push]** and **[!UICONTROL SMS]**. 

>[!NOTE]
>
>For this, you need to configure the built-in action. Refer to [this page](../action/acs-action.md).

For each of these channels, you select an [!DNL Adobe Campaign] Standard Transactional Messaging **template**. For the built-in email, SMS and push channels, we rely on Transactional Messaging to execute message sending. It means that if you want to use a certain message template in your journeys, you must publish it in [!DNL Adobe Campaign] Standard. Refer to [this page](https://experienceleague.adobe.com/docs/campaign-standard/using/communication-channels/transactional-messaging/getting-started-with-transactional-msg.html) to learn how to use this feature.

>[!NOTE]
>
>The Campaign Standard transactional message and its associated event must be published in order to be used in Journey Optimizer. If the event is published but the message is not, it will not be visible in the Journey Optimizer interface. If the message is published but its associated event is not, it will be visible in the Journey Optimizer interface but it will not be usable.

![[!DNL Adobe Campaign] Standard action configuration in journey](assets/journey59.png)

You can use an event (also known as real-time) or profile transactional messaging template.

>[!NOTE]
>
>When we send real-time transactional messages (rtEvent) or when we route messages with a third-party system thanks to a custom action, a specific setup is required for fatigue, block list or unsubscription management. For example, if an "unsubscribe" attribute is stored in [!DNL Adobe Experience Platform] or in a third-party system, a condition will have to be added before the message sending to check this condition.

When you select a template, all the fields expected in the message payload are displayed in the activity configuration pane under **[!UICONTROL Address]** and **[!UICONTROL Personalization Data]**. You need to map each of these fields with the field you want to use, either from the event or from the data source. You can also use the advanced expression editor to pass a value manually, perform data manipulation on retrieved information (for example convert a string to uppercase) or use functions such as "if, then, else". See [this page](expression/expressionadvanced.md).

![Campaign Standard message template selection interface](assets/journey60.png)

## Email and SMS {#section_asc_51g_nhb}

For **[!UICONTROL Email]** and **[!UICONTROL SMS]**, the parameters are identical.

>[!NOTE]
>
>When using a profile's transactional template for email, the unsubscription mechanism is automatically handled by [!DNL Adobe Campaign] Standard.
>Include an **[!UICONTROL Unsubscription link]** content block within [the transactional email template](https://experienceleague.adobe.com/docs/campaign-standard/using/communication-channels/transactional-messaging/getting-started-with-transactional-msg.html).
>If you are using an event-based template (rtEvent), incorporate a link in the message that passes the recipient's email as a URL parameter and directs them to an unsubscription landing page.
>Create the landing page and ensure that the recipient's unsubscribe decision is transmitted to Adobe.

First, you need to choose a transactional messaging template.

Two categories are available: **[!UICONTROL Address]** and **[!UICONTROL Personalization Data]**.

You can easily define where to retrieve the **[!UICONTROL Address]** or the **[!UICONTROL Personalization Data]** using the interface. You can browse through events and available data source's fields. You can also use the advanced expression editor for more advanced use cases such as using a data source that requires the passing of parameters or performing manipulations. See [this page](expression/expressionadvanced.md).

**[!UICONTROL Address]**

>[!NOTE]
>
>This category is only visible if you select an "event" transactional message. For "profile" messages, the **[!UICONTROL Address]** field is automatically retrieved from [!DNL Adobe Campaign] Standard by the system.

These are the fields the system requires to know where to send the message. For an email template, it's the email address. For an SMS, it's the mobile phone number.

![Message parameter configuration for Campaign Standard integration](assets/journey61.png)

**[!UICONTROL Personalization Data]**

>[!NOTE]
>
>You cannot pass a collection in personalization data. If the transactional email or SMS expects collections, it will not work. Also note that the personalization data has an expected format (example: string, decimal, etc.). You must be careful to respect these expected formats. 

These are the fields expected by the [!DNL Adobe Campaign] Standard message. These fields can be used to personalize the message, apply conditional formatting, or pick a specific message variant. 

![Field mapping between Journey Optimizer and Campaign Standard](assets/journey62.png)

## Push {#section_im3_hvf_nhb}

Prior to using the push activity, your mobile app needs to be configured along with Campaign Standard to send push notifications. Use this [article](https://helpx.adobe.com/campaign/kb/integrate-mobile-sdk.html) to take the necessary implementation steps for mobile.

First, you need to choose a mobile app from the drop-down list and a transactional message.

![Advanced expression editor for Campaign Standard parameter mapping](assets/journey62bis.png)

Two categories are available: **[!UICONTROL Target]** and **[!UICONTROL Personalization Data]**.

**[!UICONTROL Target]**

>[!NOTE]
>
>This category is only visible if you select an event message. For profile messages, the **[!UICONTROL Target]** fields are automatically retrieved by the system using the reconciliation performed by [!DNL Adobe Campaign] Standard.

In this section, you need to define the **[!UICONTROL Push platform]**. The drop-down list allows you to select **[!UICONTROL Apple Push Notification Server]** (iOS) or **[!UICONTROL Firebase Cloud Messaging]** (Android). You can alternatively select a specific field from an event or a data source, or define an advanced expression.

You also need to define the **[!UICONTROL Registration Token]**. The expression depends on how the token is defined in the event payload or in other [!DNL Journey Optimizer] information. It can be a simple field or a more complex expression in case the token is defined in a collection for instance:

```
@event{Event_push._experience.campaign.message.profileSnapshot.pushNotificationTokens.first().token}
```

**[!UICONTROL Personalization Data]**

>[!NOTE]
>
>You cannot pass a collection in personalization data. If the transactional push expects collections, it will not work. Also note that the personalization data has an expected format (example: string, decimal, etc.). You must be careful to respect these expected formats.

These are the fields expected by the transactional template used in your [!DNL Adobe Campaign] Standard message. These fields can be used to personalize your message, apply conditional formatting, or pick a specific message variant.

+++AI Assistant — Page context

* **TL;DR:** This page explains how to use the built-in Adobe Campaign Standard Email, SMS, and Push action activities in Journey Optimizer journeys via Campaign Transactional Messaging templates.

**Intents:**

* Configure Email, SMS, or Push action activities in a journey using Adobe Campaign Standard integration
* Select and map a Campaign Standard transactional messaging template to journey fields
* Map Address and Personalization Data fields from journey events or datasources to the message payload
* Handle unsubscription for event-based and profile-based transactional email templates
* Configure push notification target platform and registration token for Campaign Standard push actions

**Glossary:**

* **Transactional Messaging**: Adobe Campaign Standard capability for sending triggered, real-time messages (email, SMS, push) based on events *(product-specific)*
* **rtEvent**: Real-time event transactional message template in Adobe Campaign Standard, used for event-based messaging *(product-specific)*
* **Profile transactional template**: A Campaign Standard transactional message template that uses profile data for recipient resolution and unsubscription handling *(product-specific)*
* **Registration Token**: Device-level identifier required to target a push notification to a specific mobile app installation *(product-specific)*

**Guardrails:**

* The built-in action must be configured before use; refer to the action configuration page.
* Both the Campaign Standard transactional message and its associated event must be published for the template to be usable in Journey Optimizer.
* Collections cannot be passed in Personalization Data fields.
* For event-based (rtEvent) templates, unsubscription management must be handled manually with a condition before sending.
* For profile-based push messages, the Target fields are retrieved automatically; the Target category is only visible for event messages.
* Mobile app must be configured with Campaign Standard before the push activity can be used.

**Terminology:**

* Canonical name: Adobe Campaign Standard — Acronym: ACS — variants: Campaign Standard
* Synonyms: "event transactional message" = "rtEvent"; "real-time transactional message" = "rtEvent"
* Do not confuse: "profile transactional template" (unsubscription handled automatically) ≠ "event transactional template" (unsubscription must be handled manually)

**FAQ:**

* **Q: What channels are available through the Adobe Campaign Standard integration?** — Email, SMS, and Push notification channels are available as built-in action activities.
* **Q: Does the transactional message need to be published in Campaign Standard before using it in Journey Optimizer?** — Yes, both the transactional message and its associated event must be published; an unpublished message will not be usable even if visible in the interface.
* **Q: How is unsubscription handled for profile-based email templates?** — Unsubscription is automatically handled by Adobe Campaign Standard when using a profile transactional template; include an Unsubscription link content block in the template.
* **Q: Can I pass a collection as personalization data?** — No, collections cannot be passed in Personalization Data; the transactional message must not expect collections.
* **Q: Where do I map the recipient address for an event-based email?** — The Address category in the activity configuration pane is only visible for event transactional messages; for profile messages the address is retrieved automatically.

+++
