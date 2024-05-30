---
solution: Journey Optimizer
product: journey optimizer
title: Configure Sinch provider
description: Learn how to configure your environment to send text messages with Journey Optimizer with Sinch
feature: SMS, Channel Configuration
role: Admin
level: Intermediate
exl-id: 85412a85-edf0-4069-8bc7-b80371375f1f
---
# Configure Sinch provider {#sms-configuration-sinch}

When using the Sinch provider with Journey Optimizer, you can find two distinct options:

* **SMS Configuration**: Set up your Sinch API credentials to send SMS messages seamlessly.

* **MMS Configuration**: For multimedia messaging (MMS), configure your Sinch MMS API credentials. Note that tracking and responding to inbound messages, are handled by the SMS configuration. MMS setup is only for outbound delivery of the MMS message.

## Sinch API credentials{#create-api}

To configure your Sinch provider to send SMS messages and MMS with Journey Optimizer, follow these steps:

1. In the left rail, browse to **[!UICONTROL Administration]** > **[!UICONTROL Channels]** and select the **[!UICONTROL API Credentials]** menu. Click the **[!UICONTROL Create new API credentials]** button.

1. Configure your SMS API credentials, as detailed below:

    * **[!UICONTROL SMS vendor]**: Sinch.

    * **[!UICONTROL Name]**: choose a name for your API Credential.

    * **[!UICONTROL Service ID]** and **[!UICONTROL API Token]**: access the APIs page, you can find your credentials under the SMS tab. Learn more in [Sinch Documentation](https://developers.sinch.com/docs/sms/getting-started/){target="_blank"}.

    * **[!UICONTROL Opt-In Keywords]**: enter the default or custom keywords that will automatically trigger your **[!UICONTROL Opt-In Message]**. For multiple keywords, use comma-separated values.

    * **[!UICONTROL Opt-In Message]**: enter the custom response that is automatically sent as your **[!UICONTROL Opt-In Message]**.

    * **[!UICONTROL Opt-Out Keywords]**: enter the default or custom keywords that will automatically trigger your **[!UICONTROL Opt-Out Message]**. For multiple keywords, use comma-separated values.

    * **[!UICONTROL Opt-Out Message]**: enter the custom response that is automatically sent as your **[!UICONTROL Opt-Out Message]**.

    * **[!UICONTROL Help Keywords]**: enter the default or custom keywords that will automatically trigger your **Help Message**. For multiple keywords, use comma-separated values.

    * **[!UICONTROL Help Message]**: enter the custom response that is automatically sent as your **Help Message**.

    * **[!UICONTROL Double Opt-In Keywords]**: enter the keywords which trigger the double opt-in process. If a user profile does not exist, it is created upon successful confirmation. For multiple keywords, use comma-separated values. [Learn more on the SMS Double Opt-in](https://video.tv.adobe.com/v/3427129/?learn=on).

    * **[!UICONTROL Double Opt-In Message]**: enter the custom response that is automatically sent in response to the double opt-in confirmation.

1. Click **[!UICONTROL Submit]** when you finished the configuration of your API credentials.

After creating and configuring your API credential, you now need to create a channel surface for SMS messages. [Learn more](sms-configuration-surface.md)

## Sinch MMS API credentials {#sinch-mms}

>[!IMPORTANT]
>
> Along with MMS setup, you also need to create Sinch API credentials specifically for tracking inbound messages and managing consent requests.

To configure Sinch MMS to send MMS with Journey Optimizer, follow these steps:

1. In the left rail, browse to **[!UICONTROL Administration]** > **[!UICONTROL Channels]** and select the **[!UICONTROL API Credentials]** menu. Click the **[!UICONTROL Create new API credentials]** button.

1. Configure your MMS API credentials, as detailed below:

    * **[!UICONTROL SMS vendor]**: Sinch MMS.

    * **[!UICONTROL Name]**: choose a name for your API Credential.

    * **[!UICONTROL Project ID]**, **[!UICONTROL App ID]** and **[!UICONTROL API Token]**: follow the steps below to gather your MMS API credentials.

        * For **[!UICONTROL Project ID]** and **[!UICONTROL App ID]**: Access the [Conversation API Overview](https://dashboard.sinch.com/convapi/overview) page of your Sinch project on your Sinch Dashboard.
        * For **[!UICONTROL API Token]**: Obtain the [Access keys](https://community.sinch.com/t5/Customer-Dashboard/Sinch-Access-Keys/ta-p/12638) for your Sinch Project and generate a **Base64 API Token** out of your Sinch Project **Access keys**.

    * **[!UICONTROL Service Plan ID]** and **[!UICONTROL SMS API Token]**: your **[!UICONTROL Service Plan ID]** and **[!UICONTROL SMS API Token]** are located on the SMS tab of the APIs page.

1. Click **[!UICONTROL Submit]** when you finished the configuration of your API credentials.

After creating and configuring your API credential, you now need to create a channel surface for MMS messages. [Learn more](sms-configuration-surface.md)
