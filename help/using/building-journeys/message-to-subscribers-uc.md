---
solution: Journey Optimizer
product: journey optimizer
title: Send a message to subscribers
description: Learn how to build a journey to send a message to the subscribers of a list
feature: Journeys, Use Cases, Subscriptions
topic: Content Management
role: User, Developer
level: Intermediate, Experienced
keywords: journey, use case, message, subscribers, list, read
exl-id: 2540938f-8ac7-43fa-83ff-fed59f6bc417
version: Journey Orchestration
---
# Send a message to the subscribers of a list {#send-a-message-to-the-subscribers-of-a-list}

The purpose of this use case is to create a journey to send a message to the subscribers of a list.

In this example, the **[!UICONTROL Consent and Preference Details]** field group from [!DNL Adobe Experience Platform] is used. To find this field group, from the **[!UICONTROL Data Management]** menu, choose **[!UICONTROL Schemas]**. On the **[!UICONTROL Field groups]** tab, enter the name of the field group in the search field.

![This field group includes the subscriptions element](assets/consent-and-preference-details-field-group.png)

To configure this journey, follow these steps:

1. Create a journey that starts with a **[!UICONTROL Read]** activity. Learn more in [Create your first journey](journey-gs.md).
1. Add an **[!UICONTROL Email]** action activity to the journey. Learn how to [Work with channel actions](journey-action.md).
1. In the **[!UICONTROL Email parameters]** section of the **[!UICONTROL Email]** activity settings, replace the default email address (`PersonalEmail.adress`) with the email address of the list subscribers:

   1. Click the **[!UICONTROL Enable parameter override]** icon at the right of the **[!UICONTROL Address]** field, then click the **[!UICONTROL Edit]** icon.

      ![Journey flow with Read Audience for subscriber list targeting](assets/message-to-subscribers-uc-1.png)

   1. In the expression editor, enter the expression to retrieve the subscribers' email addresses. [Read more](expression/expressionadvanced.md).

      This example shows an expression that includes references to map fields:

      ```json
      #{ExperiencePlatform.Subscriptions.profile.consents.marketing.email.subscriptions.entry('daily-email').subscribers.firstEntryKey()}
      ```
      
      In this example, these functions are used:

      | Function | Description | Example |
      | --- | --- | --- |
      | `entry` | Refers to a map element according to the selected namespace | Refer to a specific subscription list |
      | `firstEntryKey` | Retrieves the first entry key of a map | Retrieve the first email address of subscribers |

      In this example, the subscription list is named `daily-email`. Email addresses are defined as keys in the `subscribers` map, which is linked to the subscription list map.

      Read more about [references to fields](expression/field-references.md) in expressions.

      ![Email configuration with personalized content for subscribers](assets/message-to-subscribers-uc-2.png)

   1. In the **[!UICONTROL Add an expression]** dialog box, click **[!UICONTROL Ok]**.

>[!CAUTION]
>
>Email address override should only be used for specific use cases. Most of the time, you do not need to change the email address because the value defined as the primary address in the **[!UICONTROL Execution fields]** is the one that should be used. [Learn more](../configuration/primary-email-addresses.md)
