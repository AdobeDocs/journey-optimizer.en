---
solution: Journey Optimizer
product: journey optimizer
title: Check and test your text messages
description: Learn how to check and send your text messages in Journey Optimizer
feature: SMS
topic: Content Management
role: User
level: Beginner
exl-id: 31c9b080-e334-4a11-af33-4c6f115c70a4
---
# Check & send your text message (SMS/MMS){#send-sms}

## Preview your text message {#preview-sms}

Once your message content has been defined, you can use test profiles or sample input data uploaded from a CSV / JSON file, or added manually to preview its content. If you inserted personalized content, you can check how this content is displayed in the message. [Learn how to test your content using sample input data](../test-approve/simulate-sample-input.md)

To do this, click **[!UICONTROL Simulate content]** then check your message using the test profile data.

![](assets/sms_preview_2.png)

Detailed information on how to preview & test content is available in the [Content Management](../content-management/preview-test.md) section.

## Validate your content {#sms-validate}

You must check alerts in the upper section of the editor. Some of them are simple warnings, but others can prevent you from sending the message. Two types of alerts can happen: warnings and errors.

![](assets/sms-alert-button.png)

* **Warnings** refer to recommendations and best practices. For example, a warning message is displayed if your text message is empty.

* **Errors** prevent you from testing or activating the journey, or publishing the campaign, as long as they are not resolved. For example, an error message warns you when the subject line is missing.


>[!NOTE]
>
> To improve your deliverability, use the phone numbers in the formats supported by the provider. For example, Twilio and Sinch only support phone numbers in E.164 format.

## Send your text messages {#sms-send}

>[!IMPORTANT]
>
> If your campaign is subject to an approval policy, you will need to request approval in order to be able to send your text messages. [Learn more](../test-approve/gs-approval.md)

When your text message is ready, complete the configuration of your [journey](../building-journeys/journey-gs.md) or [campaign](../campaigns/create-campaign.md) to send it.

**Related topics**

* [Configure SMS channel](sms-configuration.md)
* [SMS/MMS reports](../reports/journey-global-report-cja-sms.md)
* [Create a text message](create-sms.md)
* [Add a message in a journey](../building-journeys/journeys-message.md)
