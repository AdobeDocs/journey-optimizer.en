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

To configure Twilio with Journey Optimizer, you need to create a new API credentials used for Twilio:

1. In the left rail, browse to **[!UICONTROL Administration]** > **[!UICONTROL Channels]** and select the **[!UICONTROL API Credentials]** menu. Click the **[!UICONTROL Create new API credentials]** button.

1. Configure your SMS API credentials, as detailed below:

    * **[!UICONTROL SMS vendor]**: Twilio.

    * **[!UICONTROL Name]**: choose a name for your API Credential.

    * **[!UICONTROL Account SID]** and **[!UICONTROL Auth Token]**: access the **Account Info** pane of your Twilio Console Dashboard page to find your credentials.

    * **[!UICONTROL Message SID]**: enter the unique identifier assigned to every message created by Twilio's API. Learn more in [Twilio Documentation](https://support.twilio.com/hc/en-us/articles/223134387-What-is-a-Message-SID-){target="_blank"}.

1. Click **[!UICONTROL Submit]** when you finished the configuration of your API credentials.

After creating and configuring your API credential, you now need to create a channel surface for SMS and MMS messages. [Learn more](sms-configuration-surface.md)
