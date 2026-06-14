---
solution: Journey Optimizer
product: journey optimizer
title: Check and test your Mobile messages
description: Learn how to check and send your Mobile messages in Journey Optimizer
feature: SMS
topic: Content Management
role: User
level: Beginner
exl-id: 31c9b080-e334-4a11-af33-4c6f115c70a4
TQID: https://experienceleague.adobe.com/JPjBxyZzo13tgSLo0dqd5bFOwn9C6MHkA-DjLzlAdEI
product_v2:
  - id: cb954087-f4fc-4456-afb9-e939cabcdc79
    internal-label: Journey Optimizer
feature_v2:
  - id: d0a62d3c-b79e-47e4-929e-40ef3cffa037
    internal-label: Communication channels
subfeature_v2:
  - id: b3a93754-a8b8-46eb-9421-7eccaeeb3dff
    internal-label: Best practices
  - id: c41e8697-e629-4c38-96b3-564faaa17acf
    internal-label: Dynamic content
  - id: f8d2e9f0-69c9-40cd-890f-71336c8dfff7
    internal-label: Preview
  - id: b3b09fe1-10f1-4793-9f6b-1ca0269eebe7
    internal-label: SMS and MMS channel
role_v2:
  - id: b69b2659-1057-424e-8fc5-ed9e016dc554
    internal-label: User
level_v2:
  - id: e8ccd51f-da0d-4e3b-939b-e30d5ebb1ea5
    internal-label: Beginner
topic_v2:
  - id: aa2f3246-cb95-4b30-8899-fdf7d73550cc
    internal-label: Reporting
  - id: cdd65e7e-8839-44a2-bc21-0e03623b5dd1
    internal-label: Optimization
  - id: e0eb8757-182f-49f3-94a4-1587d16f5094
    internal-label: Personalization
---
# Check & send your Mobile message {#send-sms}

>[!BEGINSHADEBOX]

**On this page:** Learn how to preview, validate, and send your mobile messages in Adobe Journey Optimizer, including checking character encoding and limits and resolving alerts before delivery.

>[!ENDSHADEBOX]

## Preview your Mobile message {#preview-sms}

Once your message content has been defined, you can preview its content using either simulation method:

* Click **[!UICONTROL Simulate content]** to test content variations with sample input data or AI auto-generation. [Learn how to simulate content variations](../test-approve/simulate-sample-input.md)
* Click **[!UICONTROL Simulate content]**, then select **[!UICONTROL Simulate content (AEP profiles)]** from the dropdown to preview with test profiles.

![](assets/sms_preview_2.png)

Detailed information on how to preview & test content is available in the [Content Management](../content-management/preview-test.md) section.

### Character encoding and limits {#sms-character-limits}

A character count is displayed when accessing either simulation method from **[!UICONTROL Simulate content]** to assist in planning and managing your Mobile messages.

![](assets/sms_preview_3.png)

Journey Optimizer uses UTF-8 encoding in its SMS editor, allowing you to type or paste double-byte or Unicode characters. These characters are then transmitted to the service provider for delivery. Most SMS providers use GSM 7-bit encoding for standard messages with a 160-character limit and switch to UTF-16 (UCS-2) when non-GSM characters are detected with a 70-character limit.

Note that the character count does not reflect variations introduced by dynamic personalization or non-GSM 7-bit special characters.

>[!IMPORTANT]
>
>Journey Optimizer SMS delivery reporting does not account for concatenated messages and dynamic personalization, thus may not reflect the actual number of messages sent from the provider. For detailed usage and billing information, please contact your Adobe representative.
>
>To learn best practices for minimizing SMS billing overages, refer to [SMS Best Practices for Character Optimization](mobile-cost-optimization.md).

## Validate your content {#sms-validate}

>[!NOTE]
>
> To improve your deliverability, use the phone numbers in the formats supported by the provider. For example, Twilio and Sinch only support phone numbers in E.164 format.

You must check alerts in the upper section of the editor. Some of them are simple warnings, but others can prevent you from sending the message. Two types of alerts can happen: warnings and errors.

![](assets/sms-alert-button.png)

* **Warnings** refer to recommendations and best practices. For example, a warning message is displayed if your Mobile message is empty or if character limits may be exceeded with dynamic content.

    **Character limits:** 160 characters per segment (GSM 7-bit), 70 for Unicode/emojis, up to 1500 characters total.

* **Errors** prevent you from testing or activating the journey, or publishing the campaign, as long as they are not resolved. For example, an error message warns you when the subject line is missing.

The alert **"The SMS text character limit has been exceeded"** may appear even when your simulated message is shorter because validation calculates the **maximum possible length** by evaluating all conditional branches, personalization fields, and dynamic content at their longest.

Validation calculates maximum length for all possible profile data, while simulation shows actual output for one test profile.

## Send your Mobile messages {#sms-send}

>[!IMPORTANT]
>
> If your campaign is subject to an approval policy, you will need to request approval in order to be able to send your Mobile messages. [Learn more](../test-approve/gs-approval.md)

When your Mobile message is ready, complete the configuration of your [journey](../building-journeys/journey-gs.md) or [campaign](../campaigns/create-campaign.md) to send it.

**Related topics**

* [Configure SMS channel](mobile-configuration.md)
* [SMS/RCS/MMS reports](../reports/journey-global-report-cja-sms.md)
* [Create a Mobile message](create-mobile-message.md)
* [Add a message in a journey](../building-journeys/journey-action.md)
