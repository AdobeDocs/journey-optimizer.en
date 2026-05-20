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
  - id: d556b755-390a-43f0-be32-a08cf6236126
    internal-label: Configuration
  - id: d998adac-2f81-400b-a669-d07bb196e4eb
    internal-label: Journeys
  - id: dc22c819-3f29-4e91-8b7d-5c6719831141
    internal-label: Content management
subfeature_v2:
  - id: b3a93754-a8b8-46eb-9421-7eccaeeb3dff
    internal-label: Best practices
  - id: c41e8697-e629-4c38-96b3-564faaa17acf
    internal-label: Dynamic content
  - id: f8d2e9f0-69c9-40cd-890f-71336c8dfff7
    internal-label: Preview
  - id: fb9a80eb-bebc-492f-a0e9-584595621ebb
    internal-label: Publish
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

## Preview your Mobile message {#preview-sms}

Once your message content has been defined, you can use test profiles or sample input data (uploaded from a CSV/JSON file or added manually) to preview its content. If you inserted personalized content, you can check how this content is displayed in the message.  

To do this, click **[!UICONTROL Simulate content]** then check your message using the test profile data.

![](assets/sms_preview_2.png)

Detailed information on how to preview & test content is available in the [Content Management](../content-management/preview-test.md) section.

### Character encoding and limits {#sms-character-limits}

A character count is displayed when accessing **[!UICONTROL Simulate content]** menu to assist in planning and managing your Mobile messages.

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
* [SMS/MMS reports](../reports/journey-global-report-cja-sms.md)
* [Create a Mobile message](create-mobile-message.md)
* [Add a message in a journey](../building-journeys/journey-action.md)
