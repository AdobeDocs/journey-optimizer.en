---
solution: Journey Optimizer
product: journey optimizer
title: Configure the SMS surface
description: Learn how to configure your SMS/MMS surface to send text messages with Journey Optimizer
feature: SMS, Channel Configuration
role: Admin
level: Intermediate
exl-id: 0d541520-016e-468f-b011-808712847556
---
# Create a SMS/MMS surface {#message-preset-sms}

>[!CONTEXTUALHELP]
>id="ajo_admin_surface_sms_type"
>title="Define the message category"
>abstract="Select the type of text messages using this surface: Marketing for promotional messages, which require user consent, or Transactional for non-commercial messages, such as password reset."
>additional-url="https://experienceleague.adobe.com/docs/journey-optimizer/using/privacy/consent/opt-out.html#sms-opt-out-management" text="Opt-out in marketing text messages"

Once your SMS/MMS channel has been configured, you must create a channel surface to be able to send SMS and MMS messages from **[!DNL Journey Optimizer]**. 

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

    When creating a SMS/MMS, you must choose a valid channel surface matching the category you selected for your message.

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
    >To be able to select a subdomain, make sure you have previously configured at least one SMS/MMS subdomain. [Learn how](sms-subdomains.md)

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
