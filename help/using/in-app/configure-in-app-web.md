---
title: Create a Web In-app message in Journey Optimizer
description: Learn how to create a Web In-app message in Journey Optimizer
feature: In App
topic: Content Management
role: User
level: Beginner
keywords: in-app, message, creation, start
---

# Configure the Web In-app channel {#configure-in-app-web}

## Prerequisites {#prerequisites}

* Ensure you are using the latest version for your **Adobe Experience Platform Web SDK** extension.

* Install the **Adobe Experience Platform Web SDK** extension in your **Tag properties** and enable the **Personalization Storage** option.
    
     This configuration is essential for storing event histories on the client, a prerequisite for implementing Frequency Rules in the Rules builder. [Learn more](https://experienceleague.adobe.com/docs/experience-platform/tags/extensions/client/web-sdk/web-sdk-extension-configuration.html?lang=en)

    ![](assets/configure_web_inapp_1.png)

## Configure Sent data to platform rule {#configure-sent-data-trigger}

1. Access your **Adobe Experience Platform Data Collection** instance and navigate to **Tag Properties** configured with the **Adobe Experience Platform Web SDK** extension.

1. From the **Authoring** menu, select **Rules** then **Create new rule** or **Add rule**.

    ![](assets/configure_web_inapp_2.png)

1. In the **Events** section, click **Add** and configure it as follows:

    * **Extension**: Core

    * **Event Type**: Library Loaded (Page Top).

    ![](assets/configure_web_inapp_3.png)

1. Click **Keep changes** to save the Event configuration.

1. In the **Actions** section, click **Add** and configure it as follows:

    * **Extension**: Adobe Experience Platform Web SDK

    * **Action Type**: Send event

    ![](assets/configure_web_inapp_4.png)

1. In the **Personalization** section of your **Action** type, enable the **Render visual personalization decisions** option.

    ![](assets/configure_web_inapp_5.png)

1. In the **Decision Context** section, define the **Key** and **Value** pairs that determine which experience to deliver.

    ![](assets/configure_web_inapp_6.png)

1. Save your **Action** configuration by clicking **Keep changes**.

1. Navigate to the **Publishing flow** menu. Create a new **Library** or select an existing **Library** and add your newly created **Rule** to it. [Learn more](https://experienceleague.adobe.com/docs/experience-platform/tags/publish/libraries.html?lang=en#create-a-library)

1. From your **Library**, select **Save & Build to development**.

    ![](assets/configure_web_inapp_7.png)

## Configure Manual rule {#configure-manual-trigger}

1. Access your **Adobe Experience Platform Data Collection** instance and navigate to **Tag Properties** configured with the **Adobe Experience Platform Web SDK** extension.

1. From the **Authoring** menu, select **Rules** then **Create new rule** or **Add rule**.

    ![](assets/configure_web_inapp_8.png)

1. In the **Events** section, click **Add** and configure it as follows:

    * **Extension**: Core

    * **Event Type**: Click

    ![](assets/configure_web_inapp_9.png)

1. In the **Click configuration**, define the **Selector** that will be evaluated.

    ![](assets/configure_web_inapp_10.png)

1. Click **Keep changes** to save the **Event** configuration.

1. In the **Actions** section, click **Add** and configure it as follows:

    * **Extension**: Adobe Experience Platform Web SDK

    * **Action Type**: Evaluate rulesets

    ![](assets/configure_web_inapp_11.png)

1. In the **Evaluate rulesets action** section of your **Action** type, enable the **Render visual personalization decisions** option.

    ![](assets/configure_web_inapp_13.png)

1. In the **Decision Context** section, define the **Key** and **Value** pairs that determine which experience to deliver.

1. Access the **Publishing flow** menu, create a new **Library** or select an existing **Library** and add your newly created **Rule**. [Learn more](https://experienceleague.adobe.com/docs/experience-platform/tags/publish/libraries.html?lang=en#create-a-library)

1. From your **Library**, select **Save & Build to development**.

    ![](assets/configure_web_inapp_14.png)

## Create an In-app web configuration {#in-app-config}

1. Access the **[!UICONTROL Channels]** > **[!UICONTROL General settings]** > **[!UICONTROL Channel configurations]** menu, then click **[!UICONTROL Create channel configuration]**.

    ![](assets/in-app-web-config-1.png)

1. Enter a name and a description (optional) for the configuration, then select the channel to configure.

    >[!NOTE]
    >
    > Names must begin with a letter (A-Z). It can only contain alpha-numeric characters. You can also use underscore `_`, dot`.` and hyphen `-` characters.

1. To assign custom or core data usage labels to the configuration, you can select **[!UICONTROL Manage access]**. [Learn more on Object Level Access Control (OLAC)](../administration/object-based-access.md).

1. Select **[!UICONTROL Marketing action]**(s) to associate consent policies to the messages using this configuration. All consent policies associated with the marketing action are leveraged in order to respect the preferences of your customers. [Learn more](../action/consent.md#surface-marketing-actions)

1. Select **In-app messaging** channel.

1. Define an App configuration. You have two options for making changes:

    * You can either input a **[!UICONTROL Page URL]** to apply changes to a specific page.

    * You can create a rule to target multiple URLs that follow the same pattern. 

        +++ How to build a Pages matching rule.

        1. Select **[!UICONTROL Pages matching rule]** as App configuration and enter your **[!UICONTROL Page URL]**.

        1. In the **[!UICONTROL Edit configuration rule]** window, define your criteria for the **[!UICONTROL Domain]** and **[!UICONTROL Page]** fields.
        1. From the condition dropdowns, further personalize your criteria.

            Here, for example, to edit elements that are displayed on all the sales product pages of your Luma website, select Domain > Starts with > luma and Page > Contains > sales.

            ![](assets/in_app_web_surface_4.png)

        1. Click **[!UICONTROL Add another page rule]** to create another rule if needed.

        1. Select the **[!UICONTROL Default authoring and preview URL]**.

        1. Save your changes. The rule is displayed in the **[!UICONTROL Create campaign]** screen.

        +++

1. Submit your In-app web configuration.

You can now [create a web In-app](../in-app/create-in-app-web.md) inside a campaign.
