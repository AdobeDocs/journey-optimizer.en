---
solution: Journey Optimizer
product: journey optimizer
title: Get started with Mobile messages
description: Learn how to create and send Mobile messages in Journey Optimizer
feature: SMS
topic: Content Management
role: User
level: Beginner
exl-id: c1027268-0bbe-4e35-a5a6-2aef78083dd3
TQID: https://experienceleague.adobe.com/Ev0xJ86fpweQxgf-VjGUEl4ebk6BdzhVof2BgiMR9EM
product_v2:
  - id: cb954087-f4fc-4456-afb9-e939cabcdc79
    internal-label: Journey Optimizer
feature_v2:
  - id: ad78185d-8f79-40ad-9bad-cbde74af74ee
    internal-label: Guardrails and limitations
  - id: d556b755-390a-43f0-be32-a08cf6236126
    internal-label: Configuration
  - id: d998adac-2f81-400b-a669-d07bb196e4eb
    internal-label: Journeys
  - id: dc22c819-3f29-4e91-8b7d-5c6719831141
    internal-label: Content management
subfeature_v2:
  - id: cf64c7f6-7428-4ae5-b158-8df9771f38f4
    internal-label: Channel configurations
  - id: e5329d1b-e590-4e24-a3fb-ef3fe0f2c721
    internal-label: Subdomains
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
  - id: c13ff12d-60f1-49cd-833a-d43359628223
    internal-label: Mobile messaging
  - id: d00e9f03-e50b-4162-b143-0c0817c937c2
    internal-label: Customer journeys
  - id: e0eb8757-182f-49f3-94a4-1587d16f5094
    internal-label: Personalization
  - id: f4e6943a-c91a-4134-a2c7-f4f20cfff2f0
    internal-label: Privacy
---
# Get started with Mobile messages {#get-started-sms}

>[!IMPORTANT]
>
>If this is your first time creating mobile messages, make sure the Mobile message channel has been configured. [Learn more](mobile-configuration.md)

Use [!DNL Journey Optimizer] to send mobile messages to your customers across three channels, **SMS**, **MMS**, and **RCS**, from a single SMS/MMS/RCS editor where you can create, personalize, and preview your content.

* **SMS (Short Message Service)**: Send text-only messages of up to 160 characters, supported across all mobile devices.
* **MMS (Multimedia Message Service)**: Enrich your messages with images, videos, audio clips, and GIFs, plus up to 1,600 characters of text. [Learn more about MMS limitations](../start/guardrails.md#sms-guardrails)
* **RCS (Rich Communication Services)**:Deliver branded, interactive content directly in your customers' native messaging app, with no additional app download required.

Mobile messages can be created and sent in a journey or in a campaign using the Mobile message action:

* In a **Journey**: Add a Mobile message action to your journey, define basic settings, then compose your content in the Mobile message Actions pane on the right. [Learn how to create a journey](../building-journeys/journey-gs.md) 

* In a **Campaign**:Create a campaign, select Mobile message as your action, define basic settings, then edit the message content. Learn how to create [an action campaign](../campaigns/campaign-action.md#action-campaign-action) | [an API-triggered campaign](../campaigns/api-triggered-campaigns.md) | [an orchestrated campaign](../orchestrated/create-orchestrated-campaign.md#create)


## Key features {#key-features}

| Feature | Description |
|---|---|
| **Personalization** | Tailor messages with profile attributes, conditional content, and dynamic data using the personalization editor. [Learn more](../personalization/personalize.md) |
| **Provider support** | Connect with [Sinch](mobile-configuration-sinch.md), [Twilio](mobile-configuration-twilio.md), [Infobip](mobile-configuration-infobip.md), or any [custom provider](mobile-configuration-custom.md) via API integration. |
| **URL shortening** | Add shortened, trackable URLs to monitor engagement. Requires subdomain configuration. [Learn more](mobile-subdomains.md) |
| **Opt-out management** | Built-in handling of standard opt-out keywords (STOP, QUIT, CANCEL, etc.) for Sinch and Infobip. [Learn more](mobile-opt-out.md) |
| **Preview & testing** | Validate content with test profiles and sample data before sending. [Learn more](send-mobile-message.md) |
| **Reporting** | Track campaign and journey performance with dedicated [campaign reports](../reports/campaign-global-report-cja-sms.md) and [journey reports](../reports/journey-global-report-cja-sms.md). |

## Configuration requirements {#configuration-requirements}

Before sending Mobile messages, you must:

1. **Choose an SMS provider**: Select from Sinch, Twilio, Infobip, or configure a custom provider
2. **Set up API credentials**: Integrate your provider's API tokens and service IDs with Journey Optimizer
3. **Create channel configurations**: Set up SMS configurations for marketing and transactional messages
4. **Configure subdomains (optional)**: Required only if you plan to use URL shortening in your messages

These configuration steps are typically performed by a System Administrator. [Get started with SMS configuration](mobile-configuration.md)

### Requirements for RCS {#requirement-rcs}

The following prerequisites are required to use RCS in Journey Optimizer:

* **Sinch RCS API credentials**: An administrator must configure API credentials for the Sinch RCS vendor (Project ID, App ID, and API Token). [Learn more](mobile-configuration-sinch.md)
* **Mobile Message channel configuration**: An administrator must create a channel configuration with an RCS-enabled credential selected, so messages are delivered as RCS rather than SMS. [Learn more](mobile-configuration.md)
* **Fallback SMS**: Strongly recommended. Recipients whose devices do not support RCS will not receive the message unless SMS fallback is available. Customers without existing SMS volume should purchase SMS and a short code. [Learn more](design-mobile.md#rcs-content)
* **Supported vendor**: Native RCS authoring requires Sinch RCS (Adobe resell or direct). Twilio, Infobip, and other providers must use a custom provider integration.
* **Device support**: RCS delivery is supported on Android and iOS devices. Carrier and regional availability varies, RCS is not universally available globally.

## Additional resources {#additional-resources}

Browse the topics below to learn more about Mobile messaging in Journey Optimizer.

+++Configuration guides

Learn how to set up and configure your SMS environment:

* [SMS channel configuration overview](mobile-configuration.md)
* [Create SMS channel configurations](mobile-configuration-surface.md)
* [Configure SMS subdomains for URL shortening](mobile-subdomains.md)

+++

+++Provider setup guides

Step-by-step configuration for each SMS service provider:

* [Configure Sinch provider](mobile-configuration-sinch.md)
* [Configure Twilio provider](mobile-configuration-twilio.md)
* [Configure Infobip provider](mobile-configuration-infobip.md)
* [Configure custom SMS provider](mobile-configuration-custom.md)

+++

+++Content creation & management

Create, personalize, and manage your Mobile message content:

* [Create SMS/RCS/MMS messages](create-mobile-message.md)
* [Preview, test and send messages](send-mobile-message.md)
* [Personalization in Mobile messages](../personalization/personalize.md)
* [Dynamic content](../personalization/get-started-dynamic-content.md)
* [Generate SMS content with AI Assistant](../content-management/generative-text.md)

+++

+++Compliance & privacy

Ensure your Mobile messaging complies with regulations and privacy standards:

* [Opt-out management](mobile-opt-out.md)
* [Privacy and consent](../privacy/opt-out.md#opt-out-decision-management)

+++

+++Performance tracking

Monitor and analyze your SMS campaigns and journey performance:

* [SMS campaign reports](../reports/campaign-global-report-cja-sms.md)
* [SMS journey reports](../reports/journey-global-report-cja-sms.md)

+++

+++Journey & Campaign integration

Learn how to incorporate SMS into your customer journeys and campaigns:

* [Add SMS messages to journeys](../building-journeys/journey-action.md)
* [Create SMS campaigns](../campaigns/create-campaign.md)

+++

+++Frequently asked questions for RCS

**Is native RCS messaging available with Twilio or Infobip?**

No. The native RCS designer in Journey Optimizer is not available when using third-party SMS providers such as Twilio or Infobip. RCS messages can, however, be sent via a [custom provider integration](mobile-configuration-custom.md).

**Why purchase SMS alongside RCS?**

SMS volume and a short code should be purchased to enable SMS fallback, which is the recommended path. If SMS is not configured, profiles whose device or carrier does not support RCS will not receive the message at all.

**Is native RCS messaging available for Sinch direct customers?**

Yes. Customers using Sinch's Conversational API have access to native RCS authoring, including both Adobe resell and Sinch direct customers.

**Is RCS available everywhere?**

No. Carrier adoption continues to grow globally, but RCS is not universally supported across all carriers and regions. Regional availability and carrier support should be researched when planning RCS campaigns.

**Where do RCS messages appear on the device?**

RCS messages appear in the same place as standard SMS messages — in the device's native messaging application. They arrive from a branded, verified sender, giving recipients the trust signals to know the message is legitimate.

**What are the character limits for an RCS message?**

Rich Media (Single) message types support up to 3,072 characters, significantly more than the 160-character limit for standard SMS. Basic RCS message types are limited to 160 characters, matching the standard SMS limit.

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
