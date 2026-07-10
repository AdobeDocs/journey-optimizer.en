---
solution: Journey Optimizer
product: journey optimizer
title: Get started with WhatsApp messages
description: Learn how to create and send WhatsApp messages in Journey Optimizer
feature: Whatsapp
topic: Content Management
role: User
level: Beginner
exl-id: 22df2bfa-4d86-464e-ad83-3aa457e3a747
TQID: https://experienceleague.adobe.com/uHzRC9X6rB9EXH4gIFiRxFaeNcrTD0-40RrxZkN4XFg
product_v2:
  - id: cb954087-f4fc-4456-afb9-e939cabcdc79
    internal-label: Journey Optimizer
feature_v2:
  - id: d0a62d3c-b79e-47e4-929e-40ef3cffa037
    internal-label: Communication channels
subfeature_v2:
  - id: b8df23d2-98a2-4406-86cc-2babe8728d36
    internal-label: WhatsApp channel
  - id: e30b0a1a-b594-47b8-af94-1e3a2be6df11
    internal-label: Get started
role_v2:
  - id: b69b2659-1057-424e-8fc5-ed9e016dc554
    internal-label: User
level_v2:
  - id: e8ccd51f-da0d-4e3b-939b-e30d5ebb1ea5
    internal-label: Beginner
---
# Get started with WhatsApp messages {#get-started-whatsapp}

>[!BEGINSHADEBOX]

**On this page:** Understand how the WhatsApp channel works in Journey Optimizer, along with its prerequisites and limitations, so you can decide how to add WhatsApp to your journeys and campaigns.

>[!ENDSHADEBOX]

You can now send WhatsApp messages directly through Journey Optimizer via Meta's [Cloud API](https://developers.facebook.com/docs/whatsapp/cloud-api/). This feature enables seamless integration of WhatsApp into journeys and campaigns, enhancing communication and engagement with recipients.

* In a **Journey**. Create a journey, add a **WhatsApp** activity, and define basic settings, then browse to the **[!UICONTROL Actions: WhatsApp]** right pane to create the content for the WhatsApp message. Learn how to create a journey on [this page](../building-journeys/journey-gs.md).

* In a **Campaign**. Create a campaign, select **WhatsApp** as your action and define basic settings, then edit the message content to define the WhatsApp message to send. Learn how to create [an action campaign](../campaigns/campaign-action.md#action-campaign-action) | [an API-triggered campaign](../campaigns/api-triggered-campaigns.md) | [an orchestrated campaign](../orchestrated/create-orchestrated-campaign.md#create)

![](assets/do-not-localize/whatsapp-beta.png){zoomable="yes"}

## Use cases {#use-cases}

WhatsApp works best when your audience already uses the platform and you want to combine rich content with a genuinely two-way conversation.

| Benefit | Why | Example use cases |
| --- | --- | --- |
| High global engagement | Widely used messaging platform with strong adoption in many regions | Reaching international audiences already active on WhatsApp |
| Rich, interactive messages | Supports images, videos, buttons, and quick replies | Product catalogs, appointment confirmations with quick-reply options |
| Two-way conversational experiences | Recipients can reply within the same thread | Customer support conversations, order tracking questions |
| Compliance and trust via official API | Delivered through Meta's verified Cloud API with sender verification | Brand-verified communications that build recipient trust |
| Integration with other channels | Can be layered with journeys and campaigns alongside other channels | Multi-channel journeys using WhatsApp as a complementary touchpoint |

## When not to use {#when-not-to-use}

WhatsApp depends on audience adoption and explicit consent, so it is not suited to every scenario. Consider another channel in the following situations:

* Your audience does not use WhatsApp, since adoption varies widely by region and demographic
* Recipients have not given explicit opt-in, which is required by Meta's messaging policies
* The message is urgent and needs guaranteed delivery, which SMS or push handles better given WhatsApp's delivery and template review constraints
* The content is lengthy or complex and better suited to email, which offers more space and richer formatting
* Real-time conversational support is not feasible on your side, since two-way WhatsApp threads set an expectation of a timely reply

## Pre-requisites {#prereq}

Integrating WhatsApp with Journey Optimizer requires the following:

* Meta Business Manager account
* [WhatsApp Business Account with verified sender name and phone number](https://developers.facebook.com/docs/whatsapp/overview/business-accounts/)
* [User authorization token with appropriate permissions](https://developers.facebook.com/blog/post/2022/12/05/auth-tokens/) 
* [Approved Meta templates](https://developers.facebook.com/docs/whatsapp/message-templates/guidelines/)

You also need to acknowledge the following before proceeding with integration:

* [WhatsApp content rules](https://www.whatsapp.com/legal/messaging-guidelines)
* [Compliance with Meta Policies](https://www.whatsapp.com/legal)
* [24 Hour conversation limits](https://developers.facebook.com/docs/whatsapp/messaging-limits/)

## Limitations {#limitations}

The following limitations apply to the WhatsApp channel:

* The WhatsApp channel in Adobe Journey Optimizer is HIPAA-ready, but third-party vendors are not covered under Adobe's BAA. Customers are responsible for their own compliance and vendor validation.

* Note that automated or predefined response messages are not yet supported.

* Starting April 2025, delivery of all marketing template messages to WhatsApp users who have a United States phone number (a number composed of a +1 dialing code and a US area code) has been temporally suspended. [Learn more in Meta documentation](https://developers.facebook.com/docs/whatsapp/cloud-api/guides/send-message-templates#per-user-marketing-template-message-limits)

* The native integration functionality does not allow integration with third-party Business Service Provider (BSP).

## How-to video {#video}

The video below shows how to integrate WhatsApp as a native channel in Adobe Journey Optimizer to deliver secure, real-time, personalized messages at scale.

+++ See video

>[!VIDEO](https://video.tv.adobe.com/v/3470244?learn=on)

+++

## Additional learning resources

Explore more video tutorials on WhatsApp messaging and configuration.

➡️ [WhatsApp channel tutorials](https://experienceleague.adobe.com/en/docs/journey-optimizer-learn/tutorials/channels/whatsapp/whatsapp-introduction){target="_blank"}

