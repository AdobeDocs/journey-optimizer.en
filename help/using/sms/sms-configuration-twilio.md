---
solution: Journey Optimizer
product: journey optimizer
title: Configure Twilio provider
description: Learn how to configure your environment to send text messages with Journey Optimizer with Twilio
feature: SMS, Channel Configuration
role: Admin
level: Intermediate
exl-id: d6f74566-c913-4727-83b9-473a798a0158
---
# Configure Twilio provider {#sms-configuration-twilio}

## Configure API credential for SMS/MMS

To configure Twilio with Journey Optimizer, you need to create a new API credentials used for Twilio:

1. In the left rail, browse to **[!UICONTROL Administration]** > **[!UICONTROL Channels]** `>` **[!UICONTROL SMS Settings]** and select the **[!UICONTROL API Credentials]** menu. Click the **[!UICONTROL Create new API credentials]** button.

1. Configure your SMS API credentials, as detailed below:

    * **[!UICONTROL SMS vendor]**: Twilio.

    * **[!UICONTROL Name]**: choose a name for your API Credential.

    * **[!UICONTROL Account SID]** and **[!UICONTROL Auth Token]**: access the **Account Info** pane of your Twilio Console Dashboard page to find your credentials.

    * **[!UICONTROL Message SID]**: enter the unique identifier assigned to every message created by Twilio's API. Learn more in [Twilio Documentation](https://support.twilio.com/hc/en-us/articles/223134387-What-is-a-Message-SID-){target="_blank"}.

    * **[!UICONTROL Inbound Number]**: add your unique inbound number. This allows you to use the same API credentials across different sandboxes, each with its own inbound number.

1. Click **[!UICONTROL Submit]** when you finished the configuration of your API credentials.

1. In the **[!UICONTROL API Credentials]** menu, click the bin icon to delete your API credentials.

1. To modify existing credentials, locate the desired API credentials and click the **[!UICONTROL Edit]** option to make the necessary changes.

After creating and configuring your API credential, you now need to create a channel configuration for SMS and MMS messages. [Learn more](sms-configuration-surface.md)

## Configure API credential for RCS

RCS messaging is supported in Adobe Journey Optimizer through Twilio using the [Custom SMS Provider](sms-configuration-custom.md) feature. This enables the delivery of rich, interactive messages via verified business profiles, incorporating elements such as carousels, buttons, and multimedia content.

➡️ [Explore how Twilio supports RCS in Twilio documentation](https://www.twilio.com/docs/rcs)

To enable RCS messaging with Twilio, new API credentials must be configured via a Custom SMS Provider. Existing Twilio SMS credentials are not compatible, as RCS requires a distinct payload format.

To configure RCS with Twilio:

1. **Register for RCS Messaging in Twilio**

    Begin by completing the RCS registration process in the Twilio platform. This includes setting up your business profile and enabling RCS capabilities for your account.

1. **Create an SMS Webhook**

    [Configure an SMS Webhook](sms-configuration-custom.md#webhook) that can receive incoming RCS message responses or delivery updates. This webhook must be properly linked to your Twilio setup for two-way communication.

1. **Create API Credential using Custom as SMS vendor**

    In Journey Optimizer, [define new API credentials](sms-configuration-custom.md#api-credential) specifically for RCS using "Custom" as the SMS vendor. Use the appropriate RCS endpoint authentication method, base URL, and headers.

After creating and configuring your API credential, you now need to create a channel configuration for your RCS messages. [Learn more](sms-configuration-surface.md)







