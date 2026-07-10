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
  - id: d0a62d3c-b79e-47e4-929e-40ef3cffa037
    internal-label: Communication channels
subfeature_v2:
  - id: b3b09fe1-10f1-4793-9f6b-1ca0269eebe7
    internal-label: SMS and MMS channel
  - id: e30b0a1a-b594-47b8-af94-1e3a2be6df11
    internal-label: Get started
role_v2:
  - id: b69b2659-1057-424e-8fc5-ed9e016dc554
    internal-label: User
level_v2:
  - id: e8ccd51f-da0d-4e3b-939b-e30d5ebb1ea5
    internal-label: Beginner
topic_v2:
  - id: c13ff12d-60f1-49cd-833a-d43359628223
    internal-label: Mobile messaging
---
# Get started with Mobile messages {#get-started-sms}

>[!BEGINSHADEBOX]

**On this page:** Get started with mobile messaging in Adobe Journey Optimizer to create, personalize, and send SMS, MMS, and RCS messages in journeys and campaigns, including provider support, configuration requirements, and RCS prerequisites.

>[!ENDSHADEBOX]

Use [!DNL Journey Optimizer] to send mobile messages to your customers across three channels, **SMS**, **MMS**, and **RCS**, from a single SMS/MMS/RCS editor where you can create, personalize, and preview your content.

* **SMS (Short Message Service)**: Send text-only messages of up to 160 characters, supported across all mobile devices.
* **MMS (Multimedia Message Service)**: Enrich your messages with images, videos, audio clips, and GIFs, plus up to 1,600 characters of text. [Learn more about MMS limitations](../start/guardrails.md#sms-guardrails)
* **RCS (Rich Communication Services)**:Deliver branded, interactive content directly in your customers' native messaging app, with no additional app download required.

>[!IMPORTANT]
>
>If this is your first time creating mobile messages, make sure the Mobile message channel has been configured. [Learn more](mobile-configuration.md)

Mobile messages can be created and sent in a journey or in a campaign using the Mobile message action:

* In a **Journey**: Add a Mobile message action to your journey, define basic settings, then compose your content in the Mobile message Actions pane on the right. [Learn how to create a journey](../building-journeys/journey-gs.md) 

* In a **Campaign**:Create a campaign, select Mobile message as your action, define basic settings, then edit the message content. Learn how to create [an action campaign](../campaigns/campaign-action.md#action-campaign-action) | [an API-triggered campaign](../campaigns/api-triggered-campaigns.md) | [an orchestrated campaign](../orchestrated/create-orchestrated-campaign.md#create)

## Use cases {#use-cases}

SMS, MMS, and RCS work best when you need to reach users reliably, regardless of whether they have your app installed or an internet connection available.

| Benefit | Why | Example use cases |
| --- | --- | --- |
| Maximum reach and immediacy | No app or internet connection required to receive the message | Reaching users without a smartphone app installed |
| Guaranteed visibility | SMS has open rates above 90% | OTP codes, appointment reminders, delivery notifications |
| Rich content via MMS/RCS | Adds images, video, and interactive elements beyond plain text | Branded promotions, product catalogs |
| Reach users without app access | Works for recipients who have not installed or opened your app | Re-engaging lapsed app users, onboarding non-app customers |
| High-urgency CTAs | Delivered directly to a device users check frequently | Flash sales, fraud alerts, service outage notices |
| Layering with other channels | Complements push, email, and in-app messaging for broader coverage | Multi-channel journeys with SMS as a fallback channel |

## When not to use {#when-not-to-use}

SMS, MMS, and RCS are not always the most efficient or appropriate choice. Consider another channel in the following situations:

* Cost is a concern at high sending volumes, since SMS and MMS are billed per message and per-message costs add up quickly at scale
* The content is long-form or complex and better suited to email, which supports richer formatting and longer text
* Recipients have not explicitly opted in, which carries legal and compliance risk in most regions and messaging regulations

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

Browse the topics below to learn more about Mobile messaging in Journey Optimizer. See also the [SMS/MMS/RCS overview](https://experienceleague.adobe.com/en/docs/journey-optimizer-learn/mobile-learning-hub/mobile-channels-overview/sms-mms-rcs-overview){target="_blank"} in the Mobile Learning Hub for more use cases and best practices.

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
