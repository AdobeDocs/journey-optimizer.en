---
solution: Journey Optimizer
product: journey optimizer
title: Configure Infobip provider
description: Learn how to configure your environment to send text messages and MMS with Journey Optimizer with Infobip
feature: SMS, Channel Configuration
role: Admin
level: Intermediate
---
# Configure Infobip provider {#sms-configuration-infobip}

To configure Infobip with Journey Optimizer, follow these steps:

1. In the left rail, browse to **[!UICONTROL Administration]** `>` **[!UICONTROL Channels]** and select the **[!UICONTROL API Credentials]** menu. Click the **[!UICONTROL Create new API credentials]** button.

    ![](assets/sms_6.png)

1. Configure your API credentials, as detailed below.

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

After creating and configuring your API credential, you now need to create a channel surface for SMS and MMS messages. [Learn more](sms-configuration-surface.md)
