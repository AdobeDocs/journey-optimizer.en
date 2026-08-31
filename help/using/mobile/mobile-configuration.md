---
solution: Journey Optimizer
product: journey optimizer
title: Configure the SMS channel
description: Learn how to configure your environment to send Mobile messages with Journey Optimizer
feature: SMS, Channel Configuration
role: Admin
level: Intermediate
exl-id: 4dcd22ed-bf7e-4789-ab7b-33544c857db8
TQID: https://experienceleague.adobe.com/dO8HoRdGLuYVFN2YVjRCiFJQHmWHApROU8qz2-hKmTs
product_v2:
  - id: cb954087-f4fc-4456-afb9-e939cabcdc79
    internal-label: Journey Optimizer
feature_v2:
  - id: d0a62d3c-b79e-47e4-929e-40ef3cffa037
    internal-label: Communication channels
subfeature_v2:
  - id: e30b0a1a-b594-47b8-af94-1e3a2be6df11
    internal-label: Get started
  - id: b3b09fe1-10f1-4793-9f6b-1ca0269eebe7
    internal-label: SMS and MMS channel
  - id: cf64c7f6-7428-4ae5-b158-8df9771f38f4
    internal-label: Channel configurations
role_v2:
  - id: c66ffd68-0f65-42bb-aa23-b4020f12e0bd
    internal-label: Admin
level_v2:
  - id: b5a62a22-46f7-4f0d-b151-3fc640bef588
    internal-label: Intermediate
topic_v2:
  - id: eddd9b14-83bd-4ff4-9072-54a4a484abb7
    internal-label: Administration
---
# Get started with Mobile configuration {#sms-configuration}

>[!BEGINSHADEBOX]

**On this page:** Learn how to configure your Adobe Journey Optimizer environment to send SMS, MMS, and RCS messages by integrating a provider such as Sinch, Twilio, or Infobip, creating a webhook, and setting up a mobile configuration.

>[!ENDSHADEBOX]

>[!CONTEXTUALHELP]
>id="ajo_admin_sms_api_header"
>title="Configure your SMS provider with Journey Optimizer"
>abstract="Adobe Journey Optimizer sends Mobile messages through SMS service providers. Select your provider, and fill in your API credentials."

>[!CONTEXTUALHELP]
>id="ajo_admin_mms_api_header"
>title="Configure your MMS provider with Journey Optimizer"
>abstract="Adobe Journey Optimizer sends media content through MMS service providers. Select your provider, and fill in your API credentials."

>[!CONTEXTUALHELP]
>id="ajo_admin_sms_api"
>title="Configure your SMS/RCS/MMS provider with Journey Optimizer"
>abstract="Before sending Mobile messages (SMS/RCS/MMS), you must integrate the provider settings with Journey Optimizer. Once done, you need to create an SMS/RCS/MMS configuration. These steps must be performed by an Adobe Journey Optimizer System Administrator."
>additional-url="https://experienceleague.adobe.com/en/docs/journey-optimizer/using/channels/sms/configure-sms/sms-configuration-surface" text="Create an SMS channel configuration"

>[!CONTEXTUALHELP]
>id="ajo_admin_sms_configuration"
>title="Select the SMS vendor configuration"
>abstract="Select the API credentials configured for your SMS vendor."

>[!CONTEXTUALHELP]
>id="ajo_admin_fuzzy_opt_out"
>title="Fuzzy Opt-out"
>abstract="When enabled, Fuzzy Opt-out detects inbound messages that closely resemble defined opt-out keywords (e.g., CANCIL) and automatically sends a confirmation reply to verify the user's unsubscribe intent. If the user confirms via the defined prompt, they are unsubscribed."

Before sending SMS, MMS or RCS, you must configure your Adobe Journey Optimizer environment. To perform this: 

1. Integrate the provider settings with Journey Optimizer. 
    Steps depend on your SMS provider. Browse the links below to access detailed documentation:
    * [Infobip](mobile-configuration-infobip.md)
    * [Sinch](mobile-configuration-sinch.md)
    * [Twilio](mobile-configuration-twilio.md)
    * [Custom provider](mobile-configuration-custom.md)
1. [Create Webhook](mobile-webhook.md)
1. [Create a Mobile configuration](mobile-configuration-surface.md)

{{$include /help/_includes/mobile-opt-out-keyword-override.md}}

If you purchase SMS through Adobe Journey Optimizer, you can also [view SMS usage metrics](sms-usage-report.md) to reconcile MO and MT volume with vendor billing.

These steps must be performed by an Adobe Journey Optimizer [System Administrator](../start/path/administrator.md).

## Prerequisites{#sms-prerequisites}

Adobe Journey Optimizer currently integrates with third-party providers who offer Mobile messaging services independent of Adobe Journey Optimizer. Supported providers for Mobile messaging and MMS are: **Sinch**, **Twilio** and **Infobip**. Note that you can configure additional messaging providers using the [custom provider configuration](mobile-configuration-custom.md).

Prior to Mobile channel configuration, you must create an account with one of these providers to get your **API Token** and **Service ID**, which you need to configure the connection between Adobe Journey Optimizer and the applicable provider. 

Your use of Mobile messaging and MMS services is subject to additional terms and conditions from the applicable provider. As third-party solutions, Sinch, Twilio and Infobip are available to Adobe Journey Optimizer users via an integration. Adobe does not control, and is not responsible for third-party products. For any issues or requests for assistance related to the mobile messaging services, contact your provider.

>[!CAUTION]
>
>To access and edit SMS subdomains, you must have the **[!UICONTROL Manage SMS Subdomains]** permission on the production sandbox. Learn more about permissions on [this page](../administration/high-low-permissions.md#administration-permissions).
>

