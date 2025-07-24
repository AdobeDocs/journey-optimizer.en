---
solution: Journey Optimizer
product: journey optimizer
title: Configure the campaign action
description: Learn how to configure the campaign action.
feature: Campaigns
topic: Content Management
role: User
level: Beginner
mini-toc-levels: 1
keywords: create, optimizer, campaign, surface, messages
exl-id: fed96e48-2e54-4bd4-ae17-77434d1b90eb
---
# Configure the campaign action {#action-campaign-action}

Use the **[!UICONTROL Actions]** tab to select a channel configuration for your message and configure additional settings such as tracking, content experiment, or multilingual content.

1. **Choose the channel**

    Navigate to the **[!UICONTROL Actions]** tab, click the **[!UICONTROL Add action]** button and select the communication channel. 

    ![](assets/create-campaign-add-action.png)

    >[!NOTE]
    >
    >Available channels vary based on your licensing model and add-ons.

1. **Select a channel configuration**

    A configuration is defined by a [System Administrator](../start/path/administrator.md). It contains all the technical parameters for sending the message, such as header parameters, subdomain, mobile apps, etc. [Learn how to set up channel configurations](../configuration/channel-surfaces.md)
    
    ![](assets/create-campaign-action.png)

1. **Create a content experiment**

    Use the **[!UICONTROL Content experiment]** section to define multiple delivery treatments in order to measure which one performs best for your target audience. Click the **[!UICONTROL Create experiment]** button then follow the steps detailed in this section: [Create a content experiment](../content-management/content-experiment.md).

1. **Add multilingual content**

    Use the **[!UICONTROL Languages]** section to create content in multiple languages within your campaign. To do so, click the **[!UICONTROL Add languages]** button and select the desired **[!UICONTROL Language settings]**. Detailed information on how to set up and use multilingual capabilities are available in this section: [Get started with multilingual content](../content-management/multilingual-gs.md)

Additional settings are available depending on the selected communication channel. Expand the sections below for more information.

+++**Apply capping rules** (Email, Direct mail, Push, SMS)

In the **[!UICONTROL Business rules]** drop-down list, select a rule set to apply capping rules to your campaign. Leveraging channel rule sets allows you you to set frequency capping by communication type to prevent overloading customers with similar messages. [Learn how to work with rule sets](../conflict-prioritization/rule-sets.md)

+++

+++**Track engagement** (Email, SMS).

Use the **[!UICONTROL Action tracking]** section to track how your recipients react to your email or SMS deliveries. Tracking results are accessible from the campaign report once the campaign has been executed. [Learn more about campaign reports](../reports/campaign-global-report-cja.md)

+++

+++**Enable Rapid delivery mode** (Push).

Rapid delivery mode is a [!DNL Journey Optimizer] add-on that allows very fast push message sending in large volumes though campaigns. Rapid delivery is used when delay in message delivery is business-critical, when you want to send an urgent push alert on mobile phones, for example a breaking news to users who have installed your news channel app. For more information on performances when using Rapid delivery mode, refer to [Adobe Journey Optimizer product description](https://helpx.adobe.com/legal/product-descriptions/adobe-journey-optimizer.html).

+++

+++**Assign priority scores** (Web, In-app, Code-based)

Assign a priority score to the campaign allows you to prioritize an inbou nd campaign when there is an imposed constraint such as a frequency cap. Enter a numeric value (from 0-100). Please note, the higher the number, the higher the priority. [Learn how to assign priority scores to journeys & campaigns](../conflict-prioritization/priority-scores.md)

+++

+++**Set additional delivery rules** (Content cards)

For content card campaigns, you can enable additional delivery rules to choose the event(s) and criteria which trigger your message. [Learn how to create content cards](../content-card/create-content-card.md)

+++

+++**Define triggers** (In-app)

For in-app messages, you can use the **[!UICONTROL Edit triggers]** button to choose the event(s) and criteria which trigger your message. [Learn how to create an In-app message](../in-app/create-in-app.md)

+++

## Next steps {#next}

Once your campaign action is ready, you can design its content. [Learn more](campaign-content.md)
