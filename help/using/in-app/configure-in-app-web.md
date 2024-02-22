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

