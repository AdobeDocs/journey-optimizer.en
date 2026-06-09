---
solution: Journey Optimizer
product: journey optimizer
title: Check and test your WhatsApp messages
description: Learn how to check and send your WhatsApp messages in Journey Optimizer
feature: Whatsapp
topic: Content Management
role: User
level: Beginner
exl-id: 31acb095-de90-495f-8e8c-43a78dedfa06
TQID: https://experienceleague.adobe.com/u2OevVu38fPdytpuTmHeSdEx3Wvpih7ifk-j88rhDFI
product_v2:
  - id: cb954087-f4fc-4456-afb9-e939cabcdc79
    internal-label: Journey Optimizer
feature_v2:
  - id: d0a62d3c-b79e-47e4-929e-40ef3cffa037
    internal-label: Communication channels
subfeature_v2:
  - id: b3a93754-a8b8-46eb-9421-7eccaeeb3dff
    internal-label: Best practices
  - id: f8d2e9f0-69c9-40cd-890f-71336c8dfff7
    internal-label: Preview
  - id: b8df23d2-98a2-4406-86cc-2babe8728d36
    internal-label: WhatsApp channel
role_v2:
  - id: b69b2659-1057-424e-8fc5-ed9e016dc554
    internal-label: User
level_v2:
  - id: e8ccd51f-da0d-4e3b-939b-e30d5ebb1ea5
    internal-label: Beginner
---
# Check and send your WhatsApp messages {#send-whatsapp}

## Preview your WhatsApp message {#preview-whatsapp}

Once your message content has been defined, you can use test profiles or sample input data uploaded from a CSV / JSON file, or added manually to preview its content. If you inserted personalized content, you can check how this content is displayed in the message.

To do this, click **[!UICONTROL Simulate content]** then check your message using the test profile data.

Detailed information on how to preview & test content is available in the [Content Management](../content-management/preview-test.md) section.

## Validate your content {#whatsapp-validate}

You must check alerts in the upper section of the editor. Some of them are simple warnings, but others can prevent you from sending the message. Two types of alerts can happen: warnings and errors.

* **Warnings** refer to recommendations and best practices. For example, a warning message is displayed if your text message is empty.

* **Errors** prevent you from testing or activating the journey, or publishing the campaign, as long as they are not resolved. For example, an error message warns you when the subject line is missing.

## Send your WhatsApp messages {#whatsapp-send}

>[!IMPORTANT]
>
> If your campaign is subject to an approval policy, you will need to request approval in order to be able to send your text messages. [Learn more](../test-approve/gs-approval.md)

When your WhatsApp message is ready, complete the configuration of your [journey](../building-journeys/publish-journey.md) or [campaign](../campaigns/review-activate-campaign.md) to send it.

## Analyze WhatsApp interactions {#whatsapp-channel-context}

Journey Optimizer captures additional interaction data returned from the WhatsApp channel and stores it in the **AJO - Email Tracking Experience Event Dataset** under the `whatsAppChannelContext` field group. Use these fields to build [audiences](../audience/about-audiences.md), run [queries](../data/get-started-queries.md), and analyze WhatsApp engagement. [Learn more about system datasets](../data/get-started-datasets.md#system-datasets).

The following fields are captured:

| Field | Description |
|-|-|
| `messageType` | WhatsApp message type (for example, `templateBased`, `response`). |
| `inboundMessage` | Inbound reply content (for example, `stop`, `start`, `subscribe`). |
| `inboundNumber` | Sender ID where the inbound message was received. |
| `channelType` | Channel category (`Utility`, `Marketing`, or `Promotional`). |
| `profileNumber` | Phone number from which the inbound message was received. |
| `origTimestamp` | Original timestamp from Meta / WhatsApp. |
| `status` | Delivery status including standardized provider feedback (`sent`, `delivered`, `bounce`, `error`, `delay`, `duplicate`, `denylist`, `exclude`, or `unknown`) and the raw provider status message. |
| `reactionEvent` | Content of the user response: emoji for reactions, or message text for replies to a specific message. |
| `reactionMessageID` | ID of the original message being responded to. |
| `reactionActionName` | Type of response action (`react`, `unreact`, or `reply`). |
| `interactiveSelectedTitle` | User-selected title from a WhatsApp interactive message. |
| `interactiveType` | Interactive message type (`list reply`, `button reply`, or `button`). |
| `interactiveSelectedDescription` | Description of the selected WhatsApp interactive option. |
| `interactiveSelectedID` | ID of the selected option from WhatsApp. |

To query this dataset, use the `ajo_email_tracking_experience_event_dataset` table in Query Service. For query patterns and related use cases, see [Dataset query examples](../data/datasets-query-examples.md).
