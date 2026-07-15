---
title: Manage API credentials for custom channels
description: Learn how to manage API credentials for custom channels in Adobe Journey Optimizer.
feature: Channel Configuration
topic: Content Management
role: Admin
level: Experienced
badge: label="Limited Availability" type="Informative"
---

# Manage API credentials {#api-credentials}

When a custom channel is created with an authentication type other than **None**, an initial set of API credentials is automatically generated when the channel is activated.

You can view, manage and edit credentials from **[!UICONTROL Administration]** > **[!UICONTROL Channels]** > **[!UICONTROL Channel builder]** > **[!UICONTROL API credentials]**.

![API credentials](assets/custom_channel_api_credentials.png){width="100%"}

Having multiple credentials for the same channel lets you attach different authentication values to different channel configurations - for example, for different brands or use cases - without duplicating the channel definition.

To edit an existing set of credentials, click an item from the inventory list. All fields are editable.

To create additional credentials for the same channel, follow the steps below.

1. From the **[!UICONTROL API credentials]** list, click **[!UICONTROL Create API credentials]**.

1. Provide a name and description.

   ![Create API credentials](assets/custom_channel_create_api_credentials.png){width="100%"}

1. Select the **[!UICONTROL Channel]** for which you are creating credentials.

   >[!NOTE]
   >
   >Only activated custom channels with an authentication type other than **None** display in the drop-down list.

1. Select the **[!UICONTROL Authentication type]** from the list.
1. Fill in the authentication-specific fields:
   * **[!UICONTROL API Key]** – Provide the key name, value, and location (query parameter or header).
   * **[!UICONTROL Basic auth]** – Provide a username and password.
   * **[!UICONTROL OAuth 2.0]** – Configure the payload for OAuth 2.0 authentication.
1. Click **[!UICONTROL Save]**.

## Next steps {#next-steps}

* [Delegate a subdomain](custom-channel-subdomains.md) (optional — required for link tracking)
* [Create a channel configuration](custom-channel-configuration.md)
