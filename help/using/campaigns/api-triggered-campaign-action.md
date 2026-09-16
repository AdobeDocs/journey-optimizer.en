---
solution: Journey Optimizer
product: journey optimizer
title: Configure the API triggered campaign action
description: Learn how to configure the API triggered campaign action.
feature: Campaigns, API
topic: Content Management
role: Developer
level: Experienced
keywords: campaigns, API-triggered, REST, optimizer, messages
exl-id: 322e035c-7370-40c9-b1cb-3428bc26e874
TQID: https://experienceleague.adobe.com/xqm-guUFMQvrDU3LSuedvImdkhIkRvFXa0B-g13OJIs
product_v2:
  - id: cb954087-f4fc-4456-afb9-e939cabcdc79
    internal-label: Journey Optimizer
feature_v2:
  - id: d556b755-390a-43f0-be32-a08cf6236126
    internal-label: Configuration
  - id: a653cc2e-bc85-4353-a306-399e5b247978
    internal-label: Journey Optimizer campaigns
subfeature_v2:
  - id: e23d48b5-7858-4d45-9c56-9e2b4be8500e
    internal-label: Business rules
  - id: f7479fa1-474b-479d-8c98-f6cee5865a38
    internal-label: API triggered campaigns
  - id: ee67bd4a-25ee-4cdd-9eab-0d7549fde0c6
    internal-label: Campaign management
role_v2:
  - id: ff6a42d2-313e-452e-93a6-792e4fad9ff8
    internal-label: Developer
topic_v2:
  - id: aa2f3246-cb95-4b30-8899-fdf7d73550cc
    internal-label: Reporting
  - id: bcc5edb5-84c3-4940-9f84-ed88b6c16274
    internal-label: Experimentation
  - id: cdd65e7e-8839-44a2-bc21-0e03623b5dd1
    internal-label: Optimization
---
# Configure the API triggered campaign action {#api-action}

>[!BEGINSHADEBOX]

**On this page:** Choose the channel and channel configuration your API triggered campaign sends through, and set tracking, content experiment, and multilingual options, so it delivers the right message on the right channel.

>[!ENDSHADEBOX]

Use the **[!UICONTROL Actions]** tab to select a channel configuration for your message and configure additional settings such as tracking, content experiment, or multilingual content.

1. **Choose the channel**.

    Navigate to the **[!UICONTROL Actions]** tab, click the **[!UICONTROL Add action]** button and select the communication channel. 

    ![](assets/api-triggered-channel.png)

    >[!NOTE]
    >
    >For more information on the supported channels, refer to the table in this section: [Channels in journeys & campaigns](../channels/gs-channels.md#channels). Available channels vary based on your licensing model and add-ons.
    >
    >High Throughput API triggered campaigns currently support the email channel only.

1. **Select a channel configuration**

    A configuration is defined by a [System Administrator](../start/path/administrator.md). It contains all the technical parameters for sending the message, such as header parameters, subdomain, mobile apps, etc. [Learn how to set up channel configurations](../configuration/channel-surfaces.md)
    
    ![](assets/api-triggered-create-campaign-action.png)

1. **Leverage Optimization**

    Use the **[!UICONTROL Message Optimization]** section to run content experiments, leverage targeting rules, or use advanced combinations of both experimentation and targeting. These different options and the steps to follow are detailed in this section: [Optimization in campaigns](../content-management/gs-message-optimization.md).
<!--
1. **Create a content experiment**

    Use the **[!UICONTROL Content experiment]** section to define multiple delivery treatments in order to measure which one performs best for your target audience. Click the **[!UICONTROL Create experiment]** button then follow the steps detailed in this section: [Create a content experiment](../content-management/content-experiment.md).
-->

1. **Add multilingual content**

    Use the **[!UICONTROL Languages]** section to create content in multiple languages within your campaign. To do so, click the **[!UICONTROL Add languages]** button and select the desired **[!UICONTROL Language settings]**. Detailed information on how to set up and use multilingual capabilities are available in this section: [Get started with multilingual content](../content-management/multilingual-gs.md)

Additional settings are available depending on the selected communication channel. Expand the sections below for more information.

+++**Apply capping rules** (Email, Push, SMS)

In the **[!UICONTROL Business rules]** drop-down list, select a rule set to apply capping rules to your campaign. Leveraging channel rule sets allows you to set frequency capping by communication type to prevent overloading customers with similar messages. [Learn how to work with rule sets](../conflict-prioritization/rule-sets.md)

+++

+++**Override email channel configuration** (Email)

When building your campaigns, you can override some of the email parameters derived from the selected [channel configuration](../email/email-settings.md) directly at the campaign action level.

This enables you to change only specific fields of the configuration without creating a new channel configuration, allowing for targeted adjustments while maintaining the overall setup.

For more precise control, you can also personalize these override fields using contextual data in addition to profile attributes and helper functions, which is not the case in the channel configuration. [Learn how to use the personalization editor](../personalization/personalization-build-expressions.md)

After selecting a channel configuration, enable the **[!UICONTROL Override email channel configuration]** option.

![Email action with Override email channel configuration toggle enabled](assets/create-campaign-action-override.png)

You can override the following fields:

* The email header fields - **[!UICONTROL From name]**, **[!UICONTROL From email prefix]**, **[!UICONTROL Reply to name]**, and **[!UICONTROL Reply to email]**. Overriding these fields allows sender details to reflect information such as the relevant advisor, location, or branch for each recipient, rather than routing all sends through a single corporate address. Learn more on [email header parameters](../email/header-parameters.md)

  ![Email header override fields including From and Reply-to parameters](assets/create-campaign-action-override-header.png){width=80%}

  For example, you may want to override the name and email address of the sender to match the details of the specific relationship manager handling the recipient's account.

* The execution address - **[!UICONTROL Delivery address]** field. When several email addresses are available for a given profile, [!DNL Journey Optimizer] uses the execution field which is set in the [general settings](../configuration/primary-email-addresses.md) or in the [channel configuration](../email/email-settings.md#execution-address) to determine which email address to use from the profile service in priority. In some cases, you may want to override the delivery address set globally and define here a different value at the campaign action level.

* The list-unsubscribe values - **[!UICONTROL Mailto (unsubscribe)]** and **[!UICONTROL One-click unsubscribe URL]**. The one-click [List unsubscribe](../email/list-unsubscribe.md) URL is an unsubscribe link or button displayed next to the email sender information, and lets recipients instantly opt out of your mailing lists with a single click. Here you can replace the unsubscribe address and one-click unsubscribe URL set at the channel configuration level.

  ![Execution address and list unsubscribe override fields in the email action](assets/create-campaign-action-override-list.png){width=80%}

The configured value displays under each field. To keep the configured value for a setting, leave that field empty.

>[!NOTE]
>
>For API-triggered campaigns, contextual attributes used in override fields are not available for selection in the personalization editor. Enter them manually using the exact payload path (for example: `{{context.a.b}}` or `{{context.RM.name}}`). The expression must match the structure sent in the API payload.

+++

+++**Track engagement** (Email, SMS).

Use the **[!UICONTROL Action tracking]** section to track how your recipients react to your email or SMS deliveries. Tracking results are accessible from the campaign report once the campaign has been executed. [Learn more about campaign reports](../reports/campaign-global-report-cja.md)

+++

+++**Enable Rapid delivery mode** (Push).

Rapid delivery mode is a [!DNL Journey Optimizer] add-on that allows very fast push message sending in large volumes though campaigns. Rapid delivery is used when delay in message delivery is business-critical, when you want to send an urgent push alert on mobile phones, for example a breaking news to users who have installed your news channel app. Learn how to enable Rapid delivery mode for Push notifications [on this page](../push/create-push.md#rapid-delivery).

For more information on performances when using Rapid delivery mode, refer to [Adobe Journey Optimizer product description](https://helpx.adobe.com/legal/product-descriptions/adobe-journey-optimizer.html){target="_blank"}.

+++

## Next steps {#next}

Once your campaign configuration and content are ready, you can design its content. [Learn more](api-triggered-campaign-content.md)
