---
solution: Journey Optimizer
product: journey optimizer
title: Configure Infobip provider
description: Learn how to configure your environment to send text messages and MMS with Journey Optimizer with Infobip
feature: SMS, Channel Configuration
role: Admin
level: Intermediate
exl-id: 7b6dc89a-1a81-49c2-b2a7-bf24b9d215e3
TQID: https://experienceleague.adobe.com/hkloRlDuOO-lNSezWvOcD3dtsHrhDqCJGo3cHq5pWog
product_v2:
  - id: cb954087-f4fc-4456-afb9-e939cabcdc79
    internal-label: Journey Optimizer
feature_v2:
  - id: bb359667-ec7d-4d4b-8663-5850fc219d32
    internal-label: Administration
  - id: d556b755-390a-43f0-be32-a08cf6236126
    internal-label: Configuration
subfeature_v2:
  - id: d2e8a157-b3b0-4143-9ff3-809bf400be56
    internal-label: Sandboxes
role_v2:
  - id: c66ffd68-0f65-42bb-aa23-b4020f12e0bd
    internal-label: Admin
level_v2:
  - id: b5a62a22-46f7-4f0d-b151-3fc640bef588
    internal-label: Intermediate
topic_v2:
  - id: eddd9b14-83bd-4ff4-9072-54a4a484abb7
    internal-label: Administration
  - id: f4e6943a-c91a-4134-a2c7-f4f20cfff2f0
    internal-label: Privacy
---
# Configure Infobip provider {#sms-configuration-infobip}

By integrating Infobip with Adobe Journey Optimizer, you can deliver text messages to your profiles as part of your journeys and campaigns. 

To configure Infobip as your SMS provider, follow the steps below:

1. [Create API Credential](#api-credential)
1. [Create Webhook](mobile-webhook.md)
1. [Create Channel configuration](mobile-configuration-surface.md)
1. [Create Journey or Campaign with SMS channel action](create-mobile-message.md)

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
    |Principal Entity ID|Enter your assigned DLT principal entity ID.|
    |Content Template ID|Enter your registered DLT content template ID.|
    |Validity Period| Enter the message validity period in hours. In the event that messages cannot be delivered within this timeframe, the system will make additional attempts to resend them. The default validity period is set to 48 hours.|
    |Callback Data| Enter the additional client data that will be sent on the Notify URL.|
    |Inbound Number|Add your unique inbound number. This allows you to use the same API credentials across different sandboxes, each with its own inbound number.|

    +++

1. Enable the **[!UICONTROL Fuzzy Opt-out]** option to detect messages resembling opt-out keywords (e.g., 'CANCIL') and customize the confirmation reply in the **[!UICONTROL Fuzzy Auto Reply]** field. 

    **[!UICONTROL Fuzzy Opt-out]** identifies SMS messages that indicate a user wants to unsubscribe, even if the message does not exactly match a defined opt-out keyword. It can detect common opt-out phrases and certain offensive terms, helping ensure your campaigns respect user preferences and remain compliant. 

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

RCS messaging is supported in Adobe Journey Optimizer through Infobip using the [Custom SMS Provider](mobile-configuration-custom.md) feature. This enables the delivery of rich, interactive messages via verified business profiles, incorporating elements such as carousels, buttons, and multimedia content.

➡️ [Explore how Infobip supports RCS in Infobip documentation](https://www.infobip.com/docs/api/channels/rcs)

To enable RCS messaging with Infobip, new API credentials must be configured via a Custom SMS Provider. Existing Infobip SMS credentials are not compatible, as RCS requires a distinct payload format.

To configure RCS with Infobip:

1. **Register Your Business for RCS via Infobip**

    Begin by completing the RCS onboarding and registration process within the Infobip platform. This involves setting up your RCS sender profile and ensuring your account is RCS-enabled. Learn more in [Infobip documentation](https://www.infobip.com/docs/rcs/get-started)

1. **Create an SMS Webhook**

    [Configure a custom SMS webhook](mobile-configuration-custom.md#webhook) in Journey Optimizer. This webhook will be responsible for handling delivery receipts, inbound RCS messages, and status updates from Infobip's platform.

1. **Create API Credential using Custom as SMS vendor**

    [Create a new API credential](mobile-configuration-custom.md#api-credential) within Journey Optimizer, selecting "Custom" as the SMS provider. Use the appropriate RCS endpoint authentication method, base URL, and headers.

After creating and configuring your API credential, you now need to create [your Webhook](mobile-webhook.md) and a channel configuration for your RCS messages. [Learn more](mobile-configuration-surface.md)
