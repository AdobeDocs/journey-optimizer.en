---
solution: Journey Optimizer
product: journey optimizer
title: Get started with text messages (SMS/MMS/RCS)
description: Learn how to create and send text messages in Journey Optimizer
feature: SMS
topic: Content Management
role: User
level: Beginner
exl-id: c1027268-0bbe-4e35-a5a6-2aef78083dd3
---
# Get started with text messaging {#get-started-sms}

Use [!DNL Journey Optimizer] to send text messages (SMS/MMS/RCS) to your customers on their mobile devices. You can create, personalize, and preview messages in text format from the SMS/MMS/RCS editor.

Text messages can be created and sent in a journey or in a campaign. For SMS, MMS, and RCS, use the SMS action.

* In a **Journey**. Create a journey, add an SMS activity, and define basic settings. Then, browse to the SMS Actions pane on the right to create the content for the SMS, MMS, or RCS message. [Learn how to create a journey](../building-journeys/journey-gs.md)

* In a **Campaign**. Create a campaign, select SMS as your action and define basic settings. Then, edit the message content to define the SMS, MMS, or RCS message to send. [Learn how to create a campaign](../campaigns/create-campaign.md#configure)

>[!IMPORTANT]
>
>If this is your first time creating text messages, make sure the SMS channel has been configured. [Learn more](sms-configuration.md)

## Text messaging capabilities {#sms-capabilities}

Adobe Journey Optimizer provides comprehensive text messaging capabilities to engage your customers across multiple channels:

**SMS (Short Message Service)**

Send text-only messages of up to 160 characters. SMS is the most widely supported text messaging format across all mobile devices.

**MMS (Multimedia Message Service)**

Enhance your communication with multimedia content, including videos, images, audio clips, and GIFs. MMS messages allow up to 1600 characters of text in addition to media files. [Learn more about MMS limitations](../start/guardrails.md#sms-guardrails)

**RCS (Rich Communication Services)**

Send branded, interactive messages with advanced features such as carousels, rich cards, suggested actions, and enhanced media support. RCS provides a richer messaging experience on supported devices.

## Key features {#key-features}

**Personalization & Dynamic Content**

Create personalized text messages using the personalization editor. Add profile attributes, conditional content, and dynamic data to tailor messages to individual recipients. [Learn about personalization](../personalization/personalize.md)

**Multiple Provider Support**

Adobe Journey Optimizer integrates with leading SMS service providers:

* **Sinch** - [Configuration guide](sms-configuration-sinch.md)
* **Twilio** - [Configuration guide](sms-configuration-twilio.md)
* **Infobip** - [Configuration guide](sms-configuration-infobip.md)
* **Custom providers** - Configure any other SMS provider using custom API integration. [Learn more](sms-configuration-custom.md)

**URL Shortening & Tracking**

Add shortened, trackable URLs to your messages to monitor engagement. Subdomain configuration is required for URL shortening functionality. [Learn how to configure SMS subdomains](sms-subdomains.md)

**Opt-out Management**

Ensure compliance with industry standards and regulations through built-in opt-out management. Journey Optimizer automatically handles standard opt-out keywords (STOP, QUIT, CANCEL, etc.) for Sinch and Infobip providers. [Learn about opt-out management](sms-opt-out.md)

**Preview & Testing**

Test your text messages before sending using test profiles and sample data. Preview personalization, content, and formatting to ensure your messages display correctly. [Learn how to send messages](send-sms.md)

**Reporting & Analytics**

Track the performance of your SMS campaigns and journeys with comprehensive reporting capabilities:

* [SMS campaign reports](../reports/campaign-global-report-cja-sms.md)
* [SMS journey reports](../reports/journey-global-report-cja-sms.md)

## Configuration requirements {#configuration-requirements}

Before sending text messages, you must:

1. **Choose an SMS provider** - Select from Sinch, Twilio, Infobip, or configure a custom provider
2. **Set up API credentials** - Integrate your provider's API tokens and service IDs with Journey Optimizer
3. **Create channel configurations** - Set up SMS configurations for marketing and transactional messages
4. **Configure subdomains (optional)** - Required only if you plan to use URL shortening in your messages

These configuration steps are typically performed by a System Administrator. [Get started with SMS configuration](sms-configuration.md)

## Quick start guide {#quick-start}

<table style="table-layout:fixed"><tr style="border: 0;">
<td>
<a href="sms-configuration.md">
<img alt="Validation" src="../assets/do-not-localize/sms-config.jpg">
</a>
<div>
<a href="sms-configuration.md"><strong>Configure SMS channel</strong></a>
</div>
<p>Set up your SMS provider and channel configurations</p>
</td>
<td>
<a href="create-sms.md">
<img alt="Lead" src="../assets/do-not-localize/sms-create.jpeg">
</a>
<div><a href="create-sms.md"><strong>Create a text message</strong></a>
</div>
<p>Design and personalize your SMS, MMS, or RCS content</p>
</td>
<td>
<a href="send-sms.md">
<img alt="Infrequent" src="../assets/do-not-localize/sms-sending.jpg">
</a>
<div>
<a href="send-sms.md"><strong>Preview & send</strong></a>
</div>
<p>Test and send your text messages to your audience</p>
</td>
<td>
<a href="sms-opt-out.md">
<img alt="Validation" src="../assets/do-not-localize/sms-opt-out.jpg">
</a>
<div>
<a href="sms-opt-out.md"><strong>Manage opt-outs</strong></a>
</div>
<p>Handle unsubscribe requests and ensure compliance</p>
</td>
</tr></table>

## Additional resources {#additional-resources}

Browse the topics below to learn more about text messaging in Journey Optimizer.

+++Configuration guides

Learn how to set up and configure your SMS environment:

* [SMS channel configuration overview](sms-configuration.md)
* [Create SMS channel configurations](sms-configuration-surface.md)
* [Configure SMS subdomains for URL shortening](sms-subdomains.md)

+++

+++Provider setup guides

Step-by-step configuration for each SMS service provider:

* [Configure Sinch provider](sms-configuration-sinch.md)
* [Configure Twilio provider](sms-configuration-twilio.md)
* [Configure Infobip provider](sms-configuration-infobip.md)
* [Configure custom SMS provider](sms-configuration-custom.md)

+++

+++Content creation & management

Create, personalize, and manage your text message content:

* [Create SMS/MMS messages](create-sms.md)
* [Preview, test and send messages](send-sms.md)
* [Personalization in text messages](../personalization/personalize.md)
* [Dynamic content](../personalization/get-started-dynamic-content.md)

+++

+++Compliance & privacy

Ensure your text messaging complies with regulations and privacy standards:

* [Opt-out management](sms-opt-out.md)
* [Privacy and consent](../privacy/opt-out.md#sms-opt-out-management-sms-opt-out-management)

+++

+++Performance tracking

Monitor and analyze your SMS campaigns and journey performance:

* [SMS campaign reports](../reports/campaign-global-report-cja-sms.md)
* [SMS journey reports](../reports/journey-global-report-cja-sms.md)

+++

+++Journey & Campaign integration

Learn how to incorporate SMS into your customer journeys and campaigns:

* [Add SMS messages to journeys](../building-journeys/journeys-message.md)
* [Create SMS campaigns](../campaigns/create-campaign.md)

+++

## How-to videos {#videos}

**Configure and send SMS messages**

Learn how to configure, author, and include SMS messaging into your customer journeys.

+++See video

>[!VIDEO](https://video.tv.adobe.com/v/3420509?learn=on)

+++

**Explore mobile messaging capabilities**

Discover the comprehensive mobile messaging capabilities that Adobe Journey Optimizer offers to marketers.

+++See video

>[!VIDEO](https://video.tv.adobe.com/v/3426021?quality=12&learn=on)

+++

**Send branded RCS messages**

Learn how to configure and send branded, interactive RCS messages in Adobe Journey Optimizer using a custom SMS provider.

+++See video

>[!VIDEO](https://video.tv.adobe.com/v/3464755)

+++

**Related topics**

* [Add messages in journeys](../building-journeys/journeys-message.md)
* [Create marketing campaigns](../campaigns/create-campaign.md)
* [Guardrails and limitations](../start/guardrails.md#sms-guardrails)
* [SMS and mobile messaging tutorials](https://experienceleague.adobe.com/en/docs/journey-optimizer-learn/tutorials/channels/sms-channel/sms-mms-messages-overview){target="_blank"}
