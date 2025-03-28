---
solution: Journey Optimizer
product: journey optimizer
title: Check and send your push notification
description: Learn how to check and send your push notification in Journey Optimizer
feature: Push
topic: Content Management
role: User
level: Beginner
exl-id: aad4e08a-3369-454d-9e32-974347a3b393
---
# Check & send your push notification {#send-push}

## Preview your push notification {#preview-push}

Once your message content has been defined, you can use test profiles or sample input data uploaded from a CSV / JSON file, or added manually to preview its content. If you inserted personalized content, you can check how this content is displayed in the message. [Learn how to test your content using sample input data](../test-approve/simulate-sample-input.md)

To do this, click **[!UICONTROL Simulate content]**. You can then select the type of device to preview content: **[!UICONTROL iOS]** or **[!UICONTROL Android]**.

![](assets/push_preview_3.png)

Detailed information on how to preview & test content is available in the [Content Management](../content-management/preview-test.md) section.

## Validate your push notification {#push-validate}

You must check alerts in the upper section of the editor. Some of them are simple warnings, but others can prevent you from sending the message. Two types of alerts can happen: warnings and errors.

* **Warnings** refer to recommendations and best practices.

* **Errors** prevent you from testing or activating the journey as long as they are not resolved, such as:

    * **[!UICONTROL The push version of the message is empty]**: this error is displayed when the push notification body or title is missing. Learn how to define push notification content in [this section](create-push.md).

    * **[!UICONTROL configuration doesn't exist]**: you cannot use your message if the configuration you have selected is deleted after the message creation. If this error occurs, select another configuration in the message **[!UICONTROL Properties]**. Learn more on channel configurations in [this section](../configuration/channel-surfaces.md).

    * **[!UICONTROL Push iOS/Android payload has exceeded limit of 4KB]**: the push notification size cannot exceed 4KB. To respect this limit, try to reduce the use of images or emojis. Learn how to manage your push notification content in [this section](../push/create-push.md).

    ![](assets/push_alert.png)


>[!NOTE]
>
> For better deliverability, you should always use the phone numbers in the formats supported by the provider. For example, Twilio and Sinch only support phone numbers in E.164 format.

## Send your push notification{#push-send}

>[!IMPORTANT]
>
> If your campaign is subject to an approval policy, you will need to request approval in order to be able to send your Push notification. [Learn more](../test-approve/gs-approval.md)

When your push message is ready, complete the configuration of your [journey](../building-journeys/journey-gs.md) or [campaign](../campaigns/create-campaign.md) to send it.

**Related topics**

* [Configure push channel](push-configuration.md)
* [Push notification report](../reports/journey-global-report-cja-push.md)
* [Create a push notification](create-push.md)
* [Add a message in a journey](../building-journeys/journeys-message.md)
* [Add a message in a campaign](../campaigns/create-campaign.md)

