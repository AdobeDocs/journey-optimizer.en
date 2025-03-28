---
solution: Journey Optimizer
product: journey optimizer
title: Configure Infobip provider
description: Learn how to configure your environment to send text messages and MMS with Journey Optimizer with Infobip
feature: SMS, Channel Configuration
role: Admin
level: Intermediate
exl-id: 7b6dc89a-1a81-49c2-b2a7-bf24b9d215e3
---
# Configure Infobip provider {#sms-configuration-infobip}

To configure Infobip with Journey Optimizer, follow these steps:

1. In the left rail, browse to **[!UICONTROL Administration]** `>` **[!UICONTROL Channels]** and select the **[!UICONTROL API Credentials]** menu. Click the **[!UICONTROL Create new API credentials]** button.

1. Configure your API credentials, as detailed below.

    * **[!UICONTROL SMS vendor]**: Infobip.

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

    * **[!UICONTROL Inbound Number]**: add your unique inbound number. This allows you to use the same API credentials across different sandboxes, each with its own inbound number.

    * **[!UICONTROL Custom Inbound Keywords]**: define unique keywords for specific actions, e.g. DISCOUNT, OFFERS, ENROLL. These keywords are captured and stored as attributes in the profile, allowing you to trigger a streaming segment qualification within the journey and deliver a customized response or action.

    * **[!UICONTROL Default Inbound Reply Message]**: enter the default reply that is sent when a end user sends an inbound SMS that does not match any of the defined keywords.

1. Click **[!UICONTROL Submit]** when you finished the configuration of your API credentials.

1. In the **[!UICONTROL API Credentials]** menu, click the bin icon to delete your API credentials.

1. To modify existing credentials, locate the desired API credentials and click the **[!UICONTROL Edit]** option to make the necessary changes.

After creating and configuring your API credential, you now need to create a channel configuration for SMS and MMS messages. [Learn more](sms-configuration-surface.md)
