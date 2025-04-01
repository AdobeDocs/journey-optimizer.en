---
solution: Journey Optimizer
product: journey optimizer
title: Configure the WhatsApp channel
description: Learn how to configure your environment to send WhatsApp messages with Journey Optimizer
feature: Whatsapp, Channel Configuration
role: Admin
level: Intermediate
hide: yes
hidefromtoc: yes
badge: label="Beta" type="Informative"
exl-id: d1f40cd8-f311-4df6-b401-8858095cef3e
---
# Get started with WhatsApp configuration {#whatsapp-config}

>[!BEGINSHADEBOX]

**Table of content**

* [Get started with WhatsApp messages](get-started-whatsapp.md)
* **[Get started with WhatsApp configuration](whatsapp-configuration.md)**
* [Create a WhatsApp message](create-whatsapp.md)
* [Check and send your WhatsApp messages](send-whatsapp.md)

>[!ENDSHADEBOX]

Before sending your WhatsApp message, you must configure your Adobe Journey Optimizer environment and associate with your WhatsApp account. To perform this:

1. [Create your WhatsApp API credentials](#WhatsApp-credentials)
1. [Create your WhatsApp configuration](#WhatsApp-configuration)

These steps must be performed by an Adobe Journey Optimizer [System Administrator](../start/path/administrator.md).

## Create WhatsApp API credentials {#whatsapp-credentials}

1. In the left rail, browse to **[!UICONTROL Administration]** `>` **[!UICONTROL Channels]** and select the **[!UICONTROL API Credentials]** menu. Click the **[!UICONTROL Create new API credentials]** button.

1. Configure your API credentials, as detailed below:

    * **API Token**: Enter your API token. Learn more in [Meta Documentation](https://developers.facebook.com/docs/facebook-login/guides/access-tokens/)
    * **Business Account ID**: Enter the unique number related to your business portfolio. Learn more in [Meta Documentation](https://www.facebook.com/business/help/1181250022022158?id=180505742745347).

    ![](assets/whatsapp-api.png)

1. Click **[!UICONTROL Continue]**.

1. Choose the **Business Account** you want to connect to your WhatsApp API credentials.

    ![](assets/whatsapp-api-2.png)

1. Select the **Phone number** used to send your Whatsapp messages.

1. Your phone number settings is automatically filled:

    * **Quality Rating**: reflects customer feedback on messages sent in the past 24 hours.
        * Green: High quality
        * Yellow: Medium quality
        * Red: Low quality
        
        Learn more on [Quality rating](https://www.facebook.com/business/help/766346674749731#)

    * **Throughput**: indicates the rate at which your phone number can send messages.

1. Click **[!UICONTROL Submit]** when you finished the configuration of your API credentials.

After creating and configuring your API credential, you now need to create a channel configuration for WhatsApp messages. [Learn more](#whatsapp-configuration)

## Create WhatsApp configuration {#whatsapp-configuration}

1. In the left rail, browse to **[!UICONTROL Administration]** > **[!UICONTROL Channels]** and select **[!UICONTROL General settings]** > **[!UICONTROL Channel configurations]**. Click the **[!UICONTROL Create channel configuration]** button.

    ![](assets/whatsapp-config-1.png)

1. Enter a name and a description (optional) for the configuration, then select the WhatsApp channel.

    >[!NOTE]
    >
    > Names must begin with a letter (A-Z). It can only contain alpha-numeric characters. You can also use underscore `_`, dot`.` and hyphen `-` characters.

1. Select **[!DNL WhatsApp]** as your channel.

    ![](assets/whatsapp-config-2.png)

1. Select **[!UICONTROL Marketing action(s)]** to associate consent policies to the messages using this configuration. All consent policies associated with the marketing action are leveraged in order to respect the preferences of your customers. Learn more

1. Select the previously created **[!UICONTROL WhatsApp API configuration]**.

    ![](assets/whatsapp-config-3.png)

1. Enter the **[!UICONTROL Sender number]** ​you want to use for your communications.

1. Once all the parameters have been configured, click **[!UICONTROL Submit]** to confirm. You can also save the channel configuration as draft and resume its configuration later on.

1. Once the channel configuration has been created, it displays in the list with the **[!UICONTROL Processing]** status.

    >[!NOTE]
    >
    >If the checks are not successful, learn more on the possible failure reasons in [this section](../configuration/channel-surfaces.md).  

1. Once the checks are successful, the channel configuration gets the **[!UICONTROL Active]** status. It is ready to be used to deliver messages.

You are now ready to send WhatsApp messages with Journey Optimizer.
