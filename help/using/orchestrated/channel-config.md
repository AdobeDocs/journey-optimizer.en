---
solution: Journey Optimizer
product: journey optimizer
title: Configure your Channel configuration
description: Learn how to configure your Channel configuration
version: Campaign Orchestration
exl-id: 6793e9b8-06ca-403b-8cb0-3bcaef089837
---
# Configure your Channel configuration {#channel-configuration}

After setting up your [Target Dimension](target-dimension.md), you need to configure your **[!UICONTROL Channel Configuration]** and define the appropriate **[!UICONTROL Execution Details]**. This allows you to define :

* **The level of message delivery**: for example, sending one message per recipient, such as a single email per individual.

* **The execution address**: the specific contact field to be used for sending, such as an email address or phone number.

To configure you channel configuration:

1. Start by creating and configuring your **[!UICONTROL Channel configuration]**.

     You can also update an existing **[!UICONTROL Channel configuration]**.

     ➡️ [Follow the steps detailed in this page](../email/surface-personalization.md)

1. From the **[!UICONTROL Execution details]** section of your **[!UICONTROL Channel configuration]**, access the **[!UICONTROL Orchestrated campaigns]** tab.

     ![](assets/target-dimension-3.png)

1. Click **[!UICONTROL Enabled]** to make it compatible with Orchestrated campaigns.

1. Choose your delivery method:

     * **[!UICONTROL Target Dimension]**: send to the primary entity e.g., recipient.

     * **[!UICONTROL Target + Secondary Dimension]**: send using both primary and secondary entities e.g., recipient + contract.

1. Select from the drop-down your [previously created Target Dimension](#targeting-dimension).

     ![](assets/target-dimension-4.png)

1. If you selected **[!UICONTROL Target + Secondary Dimension]** as the delivery method, choose a **[!UICONTROL Secondary Dimension]** to define the context for message delivery.

1. Under the **[!UICONTROL Execution Address]** section, choose which **[!UICONTROL Source]** should be used to fetch the delivery address, such as the email address or phone number:

     * **[!UICONTROL Profile]**: Select this option if the delivery address, e.g. email, is stored directly in the main customer profile.

          Useful when sending messages to the main customer, not a specific associated entity.

     * **[!UICONTROL Target Dimension]**: Choose this if the delivery address is stored in the primary entity, e.g. a recipient.
     
          Useful when each recipient has their own delivery address such as a different email or phone number.

     * **[!UICONTROL Secondary Dimension]**: When using **[!UICONTROL Target + Secondary Dimension]** as the delivery method, select the relevant **[!UICONTROL Secondary Dimension]** that you previously configured.

          For example, if the secondary dimension represents a booking or subscription, the execution address, such as an email, can be taken from that level. This is useful in cases where profiles use a different contact detail when booking or subscribing to a service.

1. From the **[!UICONTROL Delivery address]** field, click ![edit icon](assets/do-not-localize/edit.svg) to choose the specific field to use for your message delivery.

     ![](assets/target-dimension-4.png)

1. Once configured, click **[!UICONTROL Submit]**.

Your channel is now ready to use with **Orchestrated Campaigns**, and messages will be delivered according to the selected target dimension.

## URL tracking parameters {#url-tracking}

When configuring your channel configuration, you can define URL tracking parameters to monitor the performance of your email campaigns by appending metadata to your tracked links - for analytics and reporting purposes.

To do this, contextual attributes specific to orchestrated campaigns are available using the `{{context.system.source.*}}` syntax:

* **`context.system.source.id`**: Orchestrated campaign ID
* **`context.system.source.name`**: Orchestrated campaign name
* **`context.system.source.versionId`**: Orchestrated campaign version ID
* **`context.system.source.actionId`**: Channel action node ID
* **`context.system.source.actionName`**: Channel action node name
* **`context.system.source.channel`**: Channel type (Email, SMS, Push)
* **`context.system.IdentityNamespace`**: Identity namespace used

For example:
  
```
www.YourLandingURL.com?utm_source=AJO&utm_campaign={{context.system.source.id}}&utm_content={{context.system.source.actionName}}
```

Learn more about URL tracking parameters in [this section](../email/url-tracking.md).
