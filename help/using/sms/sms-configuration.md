---
solution: Journey Optimizer
product: journey optimizer
title: Configure the SMS channel
description: Learn how to configure your environment to send text messages with Journey Optimizer
feature: SMS, Channel Configuration
role: Admin
level: Intermediate
exl-id: 4dcd22ed-bf7e-4789-ab7b-33544c857db8
---
# Configure SMS channel {#sms-configuration}

Before sending SMS, you must configure your Adobe Journey Optimizer environment. To preform this:

* [Integrate the provider settings](#create-api) with Journey Optimizer
* [Create an SMS surface](#message-preset-sms) (i.e. SMS preset)

These steps must be performed by an Adobe Journey Optimizer [System Administrator](../start/path/administrator.md).

## Prerequisites{#sms-prerequisites}

Adobe Journey Optimizer currently integrates with third-party providers who offer text messaging services independent of Adobe Journey Optimizer. Supported providers for text messaging are: **Sinch**, **Twilio** and **Infobip**.

Prior to SMS channel configuration, you must create an account with one of these providers to get your **API Token** and **Service ID**, which you need to configure the connection between Adobe Journey Optimizer and the applicable provider. 

Your use of text messaging services is subject to additional terms and conditions from the applicable provider. As third-party solutions, Sinch, Twilio and Infobip are available to Adobe Journey Optimizer users via an integration. Adobe does not control, and is not responsible for third-party products. For any issues or requests for assistance related to the text messaging services, contact your provider.

>[!CAUTION]
>
>To access and edit SMS subdomains, you must have the **[!UICONTROL Manage SMS Subdomains]** permission on the production sandbox. Learn more about permissions in [this page](../administration/high-low-permissions.md#administration-permissions).
>

## Create new API credentials {#create-api}

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
>title="Configure your SMS provider with Journey Optimizer"
>abstract="Before sending text messages, you must integrate the provider settings with Journey Optimizer. Once done, you need to create an SMS surface. These steps must be performed by an Adobe Journey Optimizer System Administrator."
>additional-url="https://experienceleague.adobe.com/docs/journey-optimizer/using/sms/sms-configuration.html#message-preset-sms" text="Create an SMS channel surface"

>[!CONTEXTUALHELP]
>id="ajo_admin_sms_configuration"
>title="Select the SMS vendor configuration"
>abstract="Select the API credentials configured for your SMS vendor."

### Sinch {#sinch-api}

To configure Sinch with Journey Optimizer, follow these steps:

1. In the left rail, browse to **[!UICONTROL Administration]** > **[!UICONTROL Channels]** and select the **[!UICONTROL API Credentials]** menu. Click the **[!UICONTROL Create new API credentials]** button.

    ![](assets/sms_6.png)

1. Configure your SMS API credentials, as detailed below:

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

After creating and configuring your API credential, you now need to create a channel surface (i.e. message preset) for SMS messages.

<!--
### Sinch MMS

For **[!DNL Sinch MMS]**

        * **[!UICONTROL Name]**: choose a name for your API Credential.

        * **[!UICONTROL Project ID]**, **[!UICONTROL App ID]** and **[!UICONTROL API Token]**: from the Conversation API menu, you can find your credentials in the App menu. Learn more in [Sinch Documentation](https://docs.cc.sinch.com/cloud/service-configuration/en/oxy_ex-1/common/wln1620131604643.html){target="_blank"}.
-->

### Twilio {#twilio-api}

To configure Twilio with Journey Optimizer, follow these steps:

1. In the left rail, browse to **[!UICONTROL Administration]** > **[!UICONTROL Channels]** and select the **[!UICONTROL API Credentials]** menu. Click the **[!UICONTROL Create new API credentials]** button.

    ![](assets/sms_6.png)

1. Configure your SMS API credentials, as detailed below:

    * **[!UICONTROL Name]**: choose a name for your API Credential.

    * **[!UICONTROL Account SID]** and **[!UICONTROL Auth Token]**: access the **Account Info** pane of your Twilio Console Dashboard page to find your credentials.

    * **[!UICONTROL Message SID]**: enter the unique identifier assigned to every message created by Twilio's API. Learn more in [Twilio Documentation](https://support.twilio.com/hc/en-us/articles/223134387-What-is-a-Message-SID-){target="_blank"}.

1. Click **[!UICONTROL Submit]** when you finished the configuration of your API credentials.

After creating and configuring your API credential, you now need to create a channel surface (i.e. message preset) for SMS messages.

### Infobip {#infobip-api}

To configure Infobip with Journey Optimizer, follow these steps:

1. In the left rail, browse to **[!UICONTROL Administration]** > **[!UICONTROL Channels]** and select the **[!UICONTROL API Credentials]** menu. Click the **[!UICONTROL Create new API credentials]** button.

    ![](assets/sms_6.png)

1. Configure your SMS API credentials, as detailed below.

    * **[!UICONTROL Name]**: choose a name for your API Credential.

    * **[!UICONTROL API base URL]** and **[!UICONTROL API key]**: access your web interface homepage or the API key management page to find your credentials. Learn more in [Infobip Documentation](https://www.infobip.com/docs/api){target="_blank"}.

    * **[!UICONTROL Opt-In Keywords]**: enter the default or custom keywords that will automatically trigger your **[!UICONTROL Opt-In Message]**. For multiple keywords, use comma-separated values.

    * **[!UICONTROL Opt-In Message]**: enter the custom response that is automatically sent as your **[!UICONTROL Opt-In Message]**.

    * **[!UICONTROL Opt-Out Keywords]**: enter the default or keywords that will automatically trigger your **[!UICONTROL Opt-Out Message]**. For multiple keywords, use comma-separated values.

    * **[!UICONTROL Opt-Out Message]**: enter the custom response that is automatically sent as your **[!UICONTROL Opt-Out Message]**.

    * **[!UICONTROL Help Keywords]**: enter the default or custom keywords that will automatically trigger your **Help Message**. For multiple keywords, use comma-separated values.

    * **[!UICONTROL Help Message]**: enter the custom response that is automatically sent as your **Help Message**.

    * **[!UICONTROL Double Opt-In Keywords]**: enter the keywords which trigger the double opt-in process. If a user profile does not exist, it is created upon successful confirmation. For multiple keywords, use comma-separated values.

    * **[!UICONTROL Double Opt-In Message]**: enter the custom response that is automatically sent in response to the Double Opt-In confirmation.

    * **[!UICONTROL Principal Entity ID]**: enter your assigned DLT principal entity ID.

    * **[!UICONTROL Content Template ID]**: enter your registered DLT content template ID.

    * **[!UICONTROL Validity Period]**: enter the message validity period in hours. In the event that messages cannot be delivered within this timeframe, the system will make additional attempts to resend them. The default validity period is set to 48 hours.

    * **[!UICONTROL Callback Data]**: enter the additional client data that will be sent on the Notify URL.

1. Click **[!UICONTROL Submit]** when you finished the configuration of your API credentials.

After creating and configuring your API credential, you now need to create a channel surface (i.e. message preset) for SMS messages.

## Create a SMS surface {#message-preset-sms}

>[!CONTEXTUALHELP]
>id="ajo_admin_surface_sms_type"
>title="Define the message category"
>abstract="Select the type of text messages using this surface: Marketing for promotional messages, which require user consent, or Transactional for non-commercial messages, such as password reset."
>additional-url="https://experienceleague.adobe.com/docs/journey-optimizer/using/privacy/consent/opt-out.html#sms-opt-out-management" text="Opt-out in marketing text messages"

Once your SMS channel has been configured, you must create a channel surface to be able to send SMS messages from **[!DNL Journey Optimizer]**. 

To create a channel surface, follow these steps:

1. In the left rail, browse to **[!UICONTROL Administration]** > **[!UICONTROL Channels]** and select **[!UICONTROL Branding]** > **[!UICONTROL Channel surfaces]**. Click the **[!UICONTROL Create channel surface]** button.

    ![](assets/preset-create.png)

1. Enter a name and a description (optional) for the surface, then select the SMS channel.

    ![](assets/sms-create-surface.png)

    >[!NOTE]
    >
    > Names must begin with a letter (A-Z). It can only contain alpha-numeric characters. You can also use underscore `_`, dot`.` and hyphen `-` characters.

1. Define the **SMS settings**.

    ![](assets/sms-surface-settings.png)

    Start by selecting the **[!UICONTROL SMS Type]** that will be sent with the surface: **[!UICONTROL Transactional]** or **[!UICONTROL Marketing]**.

    * Choose **Marketing** for promotional text messages: these messages require user consent.
    * Choose **Transactional** for non-commercial messages such as order confirmation, password reset notifications, or delivery information for example.

    When creating a SMS message, you must choose a valid channel surface matching the category you selected for your message.

    >[!CAUTION]
    >
    >**Transactional** messages can be sent to profiles who unsubscribed from marketing communications. These messages can only be sent in specific contexts.
    
1. Select the **[!UICONTROL SMS configuration]** to associate with the surface.
        
    For more on how to configure your environment to send SMS messages, refer to [this section](#create-api).

1. Enter the **[!UICONTROL Sender number]** ​you want to use for your communications.

1. Select your **[!UICONTROL SMS Execution Field]** to select the **[!UICONTROL Profile attribute]** associated with the profiles' phone numbers.

1. If you want to use the URL shortening function in your SMS messages, select an item from the **[!UICONTROL Subdomain]** list.

    >[!NOTE]
    >
    >To be able to select a subdomain, make sure you have previously configured at least one SMS subdomain. [Learn how](sms-subdomains.md)

1. Enter the **[!UICONTROL Opt-out number]** you want to use for this surface. When profiles opt out from this number, you are still able to send them messages from other numbers you may be using to send out text messages with [!DNL Journey Optimizer].

    >[!NOTE]
    >
    >In [!DNL Journey Optimizer], opt-out for text messages is no longer managed at the channel level. It is now specific to a number.

1. Once all the parameters have been configured, click **[!UICONTROL Submit]** to confirm. You can also save the channel surface as draft and resume its configuration later on.

    ![](assets/sms-submit-surface.png)

1. Once the channel surface has been created, it displays in the list with the **[!UICONTROL Processing]** status.

    >[!NOTE]
    >
    >If the checks are not successful, learn more on the possible failure reasons in [this section](#monitor-channel-surfaces).  

1. Once the checks are successful, the channel surface gets the **[!UICONTROL Active]** status. It is ready to be used to deliver messages.

    ![](assets/preset-active.png)

You are now ready to send text messages with Journey Optimizer.

**Related topics**

* [Create a text message](create-sms.md)
* [Add a message in a journey](../building-journeys/journeys-message.md)
* [Add a message in a campaign](../campaigns/create-campaign.md)

