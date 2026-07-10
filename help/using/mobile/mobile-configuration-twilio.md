---
solution: Journey Optimizer
product: journey optimizer
title: Configure Twilio provider
description: Learn how to configure your environment to send Mobile messages with Journey Optimizer with Twilio
feature: SMS, Channel Configuration
role: Admin
level: Intermediate
exl-id: d6f74566-c913-4727-83b9-473a798a0158
TQID: https://experienceleague.adobe.com/EbPWXkbbXG4zazPUQsqaEeXx5wUi6VzFGrEeYmlAASY
product_v2:
  - id: cb954087-f4fc-4456-afb9-e939cabcdc79
    internal-label: Journey Optimizer
feature_v2:
  - id: d0a62d3c-b79e-47e4-929e-40ef3cffa037
    internal-label: Communication channels
subfeature_v2:
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
# Configure Twilio provider {#sms-configuration-twilio}

>[!BEGINSHADEBOX]

**On this page:** Learn how to integrate Twilio with Adobe Journey Optimizer by creating API credentials for SMS, MMS, and RCS messaging so you can deliver mobile messages in your journeys and campaigns.

>[!ENDSHADEBOX]

By integrating Twilio with Adobe Journey Optimizer, you can deliver Mobile messages to your profiles as part of your journeys and campaigns.

To configure Twilio as your SMS provider, follow the steps below: 

1. [Create API Credential](#api-credential)
1. [Create Webhook](mobile-webhook.md)
1. [Create Channel configuration](mobile-configuration-surface.md)
1. [Create Journey or Campaign with SMS channel action](create-mobile-message.md)

## Configure API credential for SMS/RCS/MMS {#api-credential}

To configure Twilio with Journey Optimizer, you need to create new API credentials for Twilio:

1. In the left rail, browse to **[!UICONTROL Administration]** > **[!UICONTROL Channels]** `>` **[!UICONTROL SMS Settings]** and select the **[!UICONTROL API Credentials]** menu. Click the **[!UICONTROL Create new API credentials]** button.

1. Configure your SMS API credentials, as detailed below:

    * **[!UICONTROL SMS vendor]**: Twilio.

    * **[!UICONTROL Name]**: choose a name for your API Credential.

    * **[!UICONTROL Account SID]** and **[!UICONTROL Auth Token]**: access the **Account Info** pane of your Twilio Console Dashboard page to find your credentials.

    * **[!UICONTROL Message SID]**: enter the unique identifier assigned to every message created by Twilio's API. Learn more in [Twilio Documentation](https://support.twilio.com/hc/en-us/articles/223134387-What-is-a-Message-SID-){target="_blank"}.

    * **[!UICONTROL Inbound Number]**: add your unique inbound number. This allows you to use the same API credentials across different sandboxes, each with its own inbound number.

1. Select **[!UICONTROL Use custom dataset for inbound]** to route this credential's inbound SMS to a pre-created dataset you choose from the dropdown. [Learn more about using a custom dataset for inbound keywords](custom-dataset-inbound-keywords.md)

    >[!NOTE]
    >
    >The dataset schema must be **[!UICONTROL XDM ExperienceEvent]** and include at least these field groups:
    >* Adobe CJM ExperienceEvent - Message interaction details
    >* Adobe CJM ExperienceEvent - Message Execution Details
    >* Adobe CJM ExperienceEvent - Message Profile Details
    >
    >The schema and dataset must be enabled for Profile. 

1. Click **[!UICONTROL Submit]** when you finished the configuration of your API credentials.

1. In the **[!UICONTROL API Credentials]** menu, click the bin icon to delete your API credentials.

1. To modify existing credentials, locate the desired API credentials and click the **[!UICONTROL Edit]** option to make the necessary changes.

1. Click **[!UICONTROL Verify SMS connection]**, from your existing API credentials, to test and verify your SMS API credentials by sending a sample message to a designated device.

1. Fill in the **Number** and **Message** fields and click **[!UICONTROL Verify connection]**.

    >[!IMPORTANT]
    >
    >The message must be structured to align with the provider's payload format.

    ![](assets/verify-connection.png)

After creating and configuring your API credential, you now need to create a channel configuration for SMS and MMS messages. [Learn more](mobile-configuration-surface.md)

## Configure API credential for RCS

RCS messaging is supported in Adobe Journey Optimizer through Twilio using the [Custom SMS Provider](mobile-configuration-custom.md) feature. This enables the delivery of rich, interactive messages via verified business profiles, incorporating elements such as carousels, buttons, and multimedia content.

➡️ [Explore how Twilio supports RCS in Twilio documentation](https://www.twilio.com/docs/rcs)

To enable RCS messaging with Twilio, new API credentials must be configured via a Custom SMS Provider. Existing Twilio SMS credentials are not compatible, as RCS requires a distinct payload format.

To configure RCS with Twilio:

1. **Register for RCS Messaging in Twilio**

    Begin by completing the RCS registration process in the Twilio platform. This includes setting up your business profile and enabling RCS capabilities for your account.

1. **Create an SMS Webhook**

    [Configure an SMS Webhook](mobile-configuration-custom.md#webhook) that can receive incoming RCS message responses or delivery updates. This webhook must be properly linked to your Twilio setup for two-way communication.

1. **Create API Credential using Custom as SMS vendor**

    In Journey Optimizer, [define new API credentials](mobile-configuration-custom.md#api-credential) specifically for RCS using "Custom" as the SMS vendor. Use the appropriate RCS endpoint authentication method, base URL, and headers.

After creating and configuring your API credential, you now need to create a channel configuration for your RCS messages. [Learn more](mobile-configuration-surface.md)







