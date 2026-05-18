---
solution: Journey Optimizer
product: journey optimizer
title: Configure Sinch provider
description: Learn how to configure your environment to send text messages with Journey Optimizer with Sinch
feature: SMS, Channel Configuration
role: Admin
level: Intermediate
exl-id: 85412a85-edf0-4069-8bc7-b80371375f1f
TQID: https://experienceleague.adobe.com/24n9GhVTfQ9y4hlvY6g67dyL0FHqNOJW0aP-WIpzRqs
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
  - id: fdac7813-bd56-47ae-9f6d-fa94ad1c5dee
    internal-label: Overview
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
# Configure Sinch provider {#sms-configuration-sinch}

When using the Sinch provider with Journey Optimizer, you can find three distinct options:

* **SMS Configuration**: Set up your Sinch API credentials to send SMS messages seamlessly.

* **MMS Configuration**: For multimedia messaging (MMS), configure your Sinch MMS API credentials. Note that tracking and responding to inbound messages, are handled by the SMS configuration. MMS setup is only for outbound delivery of the MMS message.

* **RCS Configuration**: Set up your Sinch API credentials to send RCS messages seamlessly.

To configure your Sinch provider, follow the steps below:

1. [Create API Credential](#create-api)
1. [Create Webhook](sms-webhook.md)
1. [Create Channel configuration](sms-configuration-surface.md)
1. [Create Journey or Campaign with SMS channel action](create-sms.md)

## Configure API credentials for SMS{#create-api}

To configure your Sinch provider to send SMS messages and MMS with Journey Optimizer, follow these steps:

1. In the left rail, browse to **[!UICONTROL Administration]** > **[!UICONTROL Channels]** `>` **[!UICONTROL SMS Settings]** and select the **[!UICONTROL API Credentials]** menu. Click the **[!UICONTROL Create new API credentials]** button.

1. Configure your SMS API credentials, as detailed below:

    +++ List of SMS credentials for configuration

    |Configuration fields|Description|
    |---|---|
    |SMS vendor|Sinch|
    |Name|Choose a name for your API Credential.|
    |Service ID and API Token|Access the APIs page, you can find your credentials under the SMS tab. Learn more in [Sinch Documentation](https://developers.sinch.com/docs/sms/getting-started/){target="_blank"}.|
    |Inbound Number|Add your unique inbound number or short code. This allows you to use the same API credentials across different sandboxes, each with its own inbound number or short code.|
    |Override URL| Enter your custom URL to replace the default endpoints for SMS delivery reports, feedback data, inbound messages or event notifications. Sinch will send all relevant updates to this URL instead of the predefined ones.|

    +++

<!--
1. Choose how user consent should be tracked for messaging:

    * **[!UICONTROL Sender short code]**: Inbound keyword consent is keyed to your **sender short code** only. Use when one inbound number is enough to represent consent.

    * **[!UICONTROL Sender short code + profile number]**: Consent is keyed to the **sender short code** and the profile **mobile number**. Use when profiles can have several numbers, or when opt-in/out must apply per sender and recipient pair.
-->

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

After creating and configuring your API credential, you now need to create [your Webhook](sms-webhook.md) and a channel configuration for your RCS messages. [Learn more](sms-configuration-surface.md)

## Configure API credentials for MMS{#sinch-mms}

>[!IMPORTANT]
>
> Along with MMS setup, you also need to create Sinch API credentials specifically for tracking inbound messages and managing consent requests.

To configure Sinch MMS to send MMS with Journey Optimizer, follow these steps:

1. In the left rail, browse to **[!UICONTROL Administration]** > **[!UICONTROL Channels]** `>` **[!UICONTROL SMS Settings]** and select the **[!UICONTROL API Credentials]** menu. Click the **[!UICONTROL Create new API credentials]** button.

1. Configure your MMS API credentials, as detailed below:

    * **[!UICONTROL SMS vendor]**: Sinch MMS.

    * **[!UICONTROL Name]**: enter a name for your API credential.

    * **[!UICONTROL Project ID]**, **[!UICONTROL App ID]** and **[!UICONTROL API Token]**: follow the steps below to gather your MMS API credentials.

        * For **[!UICONTROL Project ID]** and **[!UICONTROL App ID]**: Access the [Conversation API Overview](https://dashboard.sinch.com/convapi/overview) page of your Sinch project on your Sinch Dashboard.
        * For **[!UICONTROL API Token]**: Obtain the [Access keys](https://community.sinch.com/t5/Customer-Dashboard/Sinch-Access-Keys/ta-p/12638) for your Sinch Project and generate a **Base64 API Token** out of your Sinch Project **Access keys**.

1. Click **[!UICONTROL Submit]** when you finished the configuration of your API credentials.

1. In the **[!UICONTROL API Credentials]** menu, click the bin icon to delete your API credentials.

1. To modify existing credentials, locate the desired API credentials and click the **[!UICONTROL Edit]** option to make the necessary changes.

After creating and configuring your API credential, you now need to create [your Webhook](sms-webhook.md) and a channel configuration for your RCS messages. [Learn more](sms-configuration-surface.md)

## Configure API credential for RCS

<!--![](assets/do-not-localize/rcs-sms.png)-->

RCS (Rich Communication Services) messaging is supported in Journey Optimizer through Sinch, allowing the sending of basic messages using verified business profiles with branding elements such as logos and sender names. 

Native RCS authoring requires Sinch RCS. Twilio, Infobip, and other providers must use a [custom provider integration](sms-configuration-custom.md).

Note that messages automatically fall back to SMS when the profile's device does not support RCS or is temporarily unreachable via RCS.

To configure Sinch RCS to send RCS with Journey Optimizer, follow these steps:

1. In the left rail, browse to **[!UICONTROL Administration]** > **[!UICONTROL Channels]** `>` **[!UICONTROL SMS Settings]** and select the **[!UICONTROL API Credentials]** menu. Click the **[!UICONTROL Create new API credentials]** button.

1. Configure your RCS API credentials, as detailed below:

    * **[!UICONTROL SMS vendor]**: Sinch RCS.

    * **[!UICONTROL Name]**: enter a name for your API credential.

    * **[!UICONTROL Project ID]**, **[!UICONTROL App ID]** and **[!UICONTROL API Token]**: enter the project ID, app ID, and API token from your Sinch RCS account.

    * **[!UICONTROL Service Plan ID]**: enter the service plan ID associated with your Sinch account.

    * **[!UICONTROL SMS API Token]**: enter the SMS API token from your Sinch account.

    ![](assets/rcs-config.png)

1. Optionally, enable the **[!UICONTROL Use custom dataset for inbound]** option to store inbound RCS messages in a custom dataset.

1. Set the **[!UICONTROL API rate limit (requests per second)]** to cap the maximum number of API calls per second, use your provider's recommended value to avoid throttling, or leave it at 0 for unlimited requests.

1. Click **[!UICONTROL Submit]** when you finished the configuration of your API credentials.

1. In the **[!UICONTROL API Credentials]** menu, click the bin icon to delete your API credentials.

1. To modify existing credentials, locate the desired API credentials and click the **[!UICONTROL Edit]** option to make the necessary changes.

After creating and configuring your API credential, you now need to create [your Webhook](sms-webhook.md) and a channel configuration for your RCS messages. [Learn more](sms-configuration-surface.md)


<!--
### Basic RCS Messages

>[!AVAILABILITY]
>
> Basic RCS messages is only available upon Adobe RCS add-on offering.

1. **Set up your branded RCS agent**

    Create a branded RCS agent in the Sinch Dashboard. [Learn more on branded RCS agent](https://community.sinch.com/t5/RCS/Getting-Started-with-RCS-using-Conversation-API/ta-p/17844)

1. **Set up your [Custom API credentials](sms-configuration-custom.md)**
    
    Once your RCS agent is approved, you need to set up your Sinch API credentials, which include your access key, secret, and service plan ID. These credentials will be used by Journey Optimizer to authenticate and send messages through Sinch's platform.

1. **Create a [channel configuration](sms-configuration-surface.md) for your RCS messages**

    Configure a channel surface in Journey Optimizer by linking your Sinch credentials and defining the messaging parameters. This setup enables you to compose and send RCS messages from Journey Optimizer.

1. **Create and personalize your [SMS message](../sms/create-sms.md)**

    Your messages automatically falls back to SMS when the profile's device does not support RCS or is temporarily unreachable via RCS.
-->



