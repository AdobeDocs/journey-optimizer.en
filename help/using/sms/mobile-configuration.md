---
solution: Journey Optimizer
product: journey optimizer
title: Configure the SMS channel
description: Learn how to configure your environment to send text messages with Journey Optimizer
feature: SMS, Channel Configuration
role: Admin
level: Intermediate
exl-id: 4dcd22ed-bf7e-4789-ab7b-33544c857db8
TQID: https://experienceleague.adobe.com/dO8HoRdGLuYVFN2YVjRCiFJQHmWHApROU8qz2-hKmTs
product_v2:
  - id: cb954087-f4fc-4456-afb9-e939cabcdc79
    internal-label: Journey Optimizer
feature_v2:
  - id: bb359667-ec7d-4d4b-8663-5850fc219d32
    internal-label: Administration
  - id: d556b755-390a-43f0-be32-a08cf6236126
    internal-label: Configuration
subfeature_v2:
  - id: e30b0a1a-b594-47b8-af94-1e3a2be6df11
    internal-label: Get started
  - id: e5329d1b-e590-4e24-a3fb-ef3fe0f2c721
    internal-label: Subdomains
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

>[!CONTEXTUALHELP]
>id="ajo_admin_sms_api_header"
>title="Configure your SMS provider with Journey Optimizer"
>abstract="Adobe Journey Optimizer sends text messages through SMS service providers. Select your provider, and fill in your API credentials."

>[!CONTEXTUALHELP]
>id="ajo_admin_mms_api_header"
>title="Configure your MMS provider with Journey Optimizer"
>abstract="Adobe Journey Optimizer sends media content through MMS service providers. Select your provider, and fill in your API credentials."

>[!CONTEXTUALHELP]
>id="ajo_admin_sms_api"
>title="Configure your SMS/MMS provider with Journey Optimizer"
>abstract="Before sending text messages (SMS/MMS), you must integrate the provider settings with Journey Optimizer. Once done, you need to create an SMS/MMS configuration. These steps must be performed by an Adobe Journey Optimizer System Administrator."
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
    * [Infobip](sms-configuration-infobip.md)
    * [Sinch](sms-configuration-sinch.md)
    * [Twilio](sms-configuration-twilio.md)
    * [Custom provider](sms-configuration-custom.md)
1. [Create Webhook](sms-webhook.md)
1. [Create a Mobile configuration](sms-configuration-surface.md)

These steps must be performed by an Adobe Journey Optimizer [System Administrator](../start/path/administrator.md).

## Prerequisites{#sms-prerequisites}

Adobe Journey Optimizer currently integrates with third-party providers who offer text messaging services independent of Adobe Journey Optimizer. Supported providers for text messaging and MMS are: **Sinch**, **Twilio** and **Infobip**. Note that you can configure additional messaging providers using the [custom provider configuration](sms-configuration-custom.md).

Prior to Mobile channel configuration, you must create an account with one of these providers to get your **API Token** and **Service ID**, which you need to configure the connection between Adobe Journey Optimizer and the applicable provider. 

Your use of text messaging and MMS services is subject to additional terms and conditions from the applicable provider. As third-party solutions, Sinch, Twilio and Infobip are available to Adobe Journey Optimizer users via an integration. Adobe does not control, and is not responsible for third-party products. For any issues or requests for assistance related to the mobile messaging services, contact your provider.

>[!CAUTION]
>
>To access and edit SMS subdomains, you must have the **[!UICONTROL Manage SMS Subdomains]** permission on the production sandbox. Learn more about permissions on [this page](../administration/high-low-permissions.md#administration-permissions).
>

