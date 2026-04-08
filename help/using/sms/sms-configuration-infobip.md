---
solution: Journey Optimizer
product: journey optimizer
title: Configure Infobip provider
description: Learn how to configure your environment to send text messages and MMS with Journey Optimizer with Infobip
feature: SMS, Channel Configuration
role: Admin
level: Intermediate
exl-id: 7b6dc89a-1a81-49c2-b2a7-bf24b9d215e3
---
# Configure Infobip provider {#sms-configuration-infobip}

>[!BEGINSHADEBOX]

If opt-in or opt-out keywords are not provided, standard consent messages are used to honor user privacy. Adding custom keywords automatically overrides the defaults.

**Default keywords:**

* **Opt-In**: SUBSCRIBE, YES, UNSTOP, START, CONTINUE, RESUME, BEGIN
* **Opt-Out**: STOP, QUIT, CANCEL, END, UNSUBSCRIBE, NO
* **Help**: HELP

>[!ENDSHADEBOX]

By integrating Infobip with Adobe Journey Optimizer, you can deliver text messages to your profiles as part of your journeys and campaigns.

To configure Infobip as your SMS provider, follow the steps below:

1. [Create API Credential](#api-credential)
1. [Create Webhook](sms-webhook.md)
1. [Create Channel configuration](sms-configuration-surface.md)
1. [Create Journey or Campaign with SMS channel action](create-sms.md)

## Configure API credentials for SMS {#api-credential}

To configure Infobip with Journey Optimizer, follow these steps:

1. In the left rail, browse to **[!UICONTROL Administration]** `>` **[!UICONTROL Channels]** and select the **[!UICONTROL API Credentials]** menu. Click the **[!UICONTROL Create new API credentials]** button.

1. Configure your SMS API credentials, as detailed below:

    +++ List of SMS credentials for configuration

    |Configuration fields|Description|
    |---|---|    
    |SMS vendor|Infobip|
    |Name|Choose a name for your API Credential.|
    |API base URL and API key| Access your web interface homepage or the API key management page to find your credentials. For regional or alternate domain endpoints, e.g. `api-ny2.infobip.com`, specify the complete base URL and verify your authorization token with Infobip support. </br>Learn more in [Infobip Documentation](https://www.infobip.com/docs/api){target="_blank"}|
    |Opt-In Keywords|**For new SMS configurations, use the [Webhooks menu](sms-webhook.md) to configure consent keywords. Existing configurations can continue using consent keywords in this section.** </br>Enter the default or custom keywords that will automatically trigger your Opt-In Message. For multiple keywords, use comma-separated values.|
    |Opt-In Message|**For new SMS configurations, use the [Webhooks menu](sms-webhook.md) to configure consent keywords. Existing configurations can continue using consent keywords in this section.** </br> Enter the custom response that is automatically sent as your Opt-In Message.|
    |Opt-Out Keywords|**For new SMS configurations, use the [Webhooks menu](sms-webhook.md) to configure consent keywords. Existing configurations can continue using consent keywords in this section.** </br> Enter the default or custom keywords that will automatically trigger your Opt-Out Message. For multiple keywords, use comma-separated values.|
    |Opt-Out Message|**For new SMS configurations, use the [Webhooks menu](sms-webhook.md) to configure consent keywords. Existing configurations can continue using consent keywords in this section.** </br>Enter the custom response that is automatically sent as your Opt-Out Message.|
    |Help Keywords|**For new SMS configurations, use the [Webhooks menu](sms-webhook.md) to configure consent keywords. Existing configurations can continue using consent keywords in this section.** </br>Enter the default or custom keywords that will automatically trigger your **Help Message**. For multiple keywords, use comma-separated values.|
    |Help Message|**For new SMS configurations, use the [Webhooks menu](sms-webhook.md) to configure consent keywords. Existing configurations can continue using consent keywords in this section.** </br>Enter the custom response that is automatically sent as your **Help Message**.|
    |Double Opt-In Keywords|**For new SMS configurations, use the [Webhooks menu](sms-webhook.md) to configure consent keywords. Existing configurations can continue using consent keywords in this section.** </br>Enter the keywords which trigger the double opt-in process. If a user profile does not exist, it is created upon successful confirmation. For multiple keywords, use comma-separated values. [Learn more about the SMS Double Opt-in](https://video.tv.adobe.com/v/3427129/?learn=on).|
    |Double Opt-In Message|**For new SMS configurations, use the [Webhooks menu](sms-webhook.md) to configure consent keywords. Existing configurations can continue using consent keywords in this section.** </br>Enter the custom response that is automatically sent in response to the double opt-in confirmation.|
    |Principal Entity ID|Enter your assigned DLT principal entity ID.|
    |Content Template ID|Enter your registered DLT content template ID.|
    |Validity Period| Enter the message validity period in hours. In the event that messages cannot be delivered within this timeframe, the system will make additional attempts to resend them. The default validity period is set to 48 hours.|
    |Callback Data| Enter the additional client data that will be sent on the Notify URL.|
    |Inbound Number|Add your unique inbound number. This allows you to use the same API credentials across different sandboxes, each with its own inbound number.|
    |Custom Inbound Keywords|Define unique, non consent related keywords for batch-based actions, e.g. DISCOUNT, OFFERS, ENROLL. These keywords are captured and stored as attributes in the profile, allowing you to trigger a batched segment qualification within the journey and deliver a customized response or action.|
    |Default Inbound Reply Message|Enter the default reply that is sent when a end user sends an inbound SMS that does not match any of the defined keywords.|

    +++

1. Enable the **[!UICONTROL Fuzzy Opt-out]** option to detect messages resembling opt-out keywords (e.g., 'CANCIL') and customize the confirmation reply in the **[!UICONTROL Fuzzy Auto Reply]** field. 

    **[!UICONTROL Fuzzy Opt-out]** identifies SMS messages that indicate a user wants to unsubscribe, even if the message does not exactly match a defined opt-out keyword. It can detect common opt-out phrases and certain offensive terms, helping ensure your campaigns respect user preferences and remain compliant.

1. Click **[!UICONTROL Submit]** when you finished the configuration of your API credentials.

1. In the **[!UICONTROL API Credentials]** menu, click the bin icon to delete your API credentials.

1. To modify existing credentials, locate the desired API credentials and click the **[!UICONTROL Edit]** option to make the necessary changes.

1. Click **[!UICONTROL Verify SMS connection]**, from your existing API credentials, to test and verify your SMS API credentials by sending a sample message to a designated device.

1. Fill in the **Number** and **Message** fields and click **[!UICONTROL Verify connection]**.

    >[!IMPORTANT]
    >
    >The message must be structured to align with the provider's payload format.

    ![](assets/verify-connection.png)

After creating and configuring your API credential, you now need to create a channel configuration for SMS and MMS messages. [Learn more](sms-configuration-surface.md)

## Configure API credential for RCS

RCS messaging is supported in Adobe Journey Optimizer through Infobip using the [Custom SMS Provider](sms-configuration-custom.md) feature. This enables the delivery of rich, interactive messages via verified business profiles, incorporating elements such as carousels, buttons, and multimedia content.

➡️ [Explore how Infobip supports RCS in Infobip documentation](https://www.infobip.com/docs/api/channels/rcs)

To enable RCS messaging with Infobip, new API credentials must be configured via a Custom SMS Provider. Existing Infobip SMS credentials are not compatible, as RCS requires a distinct payload format.

To configure RCS with Infobip:

1. **Register Your Business for RCS via Infobip**

    Begin by completing the RCS onboarding and registration process within the Infobip platform. This involves setting up your RCS sender profile and ensuring your account is RCS-enabled. Learn more in [Infobip documentation](https://www.infobip.com/docs/rcs/get-started)

1. **Create an SMS Webhook**

    [Configure a custom SMS webhook](sms-configuration-custom.md#webhook) in Journey Optimizer. This webhook will be responsible for handling delivery receipts, inbound RCS messages, and status updates from Infobip's platform.

1. **Create API Credential using Custom as SMS vendor**

    [Create a new API credential](sms-configuration-custom.md#api-credential) within Journey Optimizer, selecting "Custom" as the SMS provider. Use the appropriate RCS endpoint authentication method, base URL, and headers.

After creating and configuring your API credential, you now need to create [your Webhook](sms-webhook.md) and a channel configuration for your RCS messages. [Learn more](sms-configuration-surface.md)
