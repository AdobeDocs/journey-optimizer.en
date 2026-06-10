---
title: Check and send your In-app notification
description: Learn how to check and send an In-app message in Journey Optimizer
feature: In App
topic: Content Management
role: User
level: Beginner
keywords: in-app, message, creation, start
exl-id: 9e9c235a-b78c-4669-af82-822b6f1e6fca
TQID: https://experienceleague.adobe.com/lInGr6DN0-ED3ouErpV09-9ovLvOL1oHiSZEO-NBA7c
product_v2:
  - id: cb954087-f4fc-4456-afb9-e939cabcdc79
    internal-label: Journey Optimizer
feature_v2:
  - id: d0a62d3c-b79e-47e4-929e-40ef3cffa037
    internal-label: Communication channels
subfeature_v2:
  - id: f8d2e9f0-69c9-40cd-890f-71336c8dfff7
    internal-label: Preview
  - id: cc5c44e2-54a1-4927-b794-442cd87d8f74
    internal-label: In App channel
  - id: c96d2aa5-76a2-443d-8d23-5de95577c909
    internal-label: Mobile SDK
role_v2:
  - id: b69b2659-1057-424e-8fc5-ed9e016dc554
    internal-label: User
level_v2:
  - id: e8ccd51f-da0d-4e3b-939b-e30d5ebb1ea5
    internal-label: Beginner
topic_v2:
  - id: aa2f3246-cb95-4b30-8899-fdf7d73550cc
    internal-label: Reporting
---
# Check & send your In-app notification {#create-in-app}

## Preview on device {#preview-device}

If you want to get a sneak peek of the In-app notification before it goes live for all users, you have the ability to preview it on a specific device. This functionality allows you to ensure that the notification looks and functions as intended on the chosen device, providing a better user experience for your audience.

To perform this, follow the steps below: 

1. Click **[!UICONTROL Preview on device]**.

    ![](assets/in_app_create_6.png)

1. From the **[!UICONTROL Connect to device]** window, click **[!UICONTROL Start]**.

1. Enter the **[!UICONTROL Base URL]** of your application and click **[!UICONTROL Next]**.

    ![](assets/in_app_create_7.png)

1. Scan the QR code with your device and enter the PIN code displayed. 
 
Your In-app message can now be triggered directly on your device allowing you to preview and review your message on an actual device. 

## Preview with test profiles {#simulate}

Once your in-app message has been defined, you can preview it using either simulation method:

* Click **[!UICONTROL Simulate content]** to test content variations with sample input data or AI auto-generation. [Learn how to simulate content variations](../test-approve/simulate-sample-input.md)
* Click **[!UICONTROL Simulate content]**, then select **[!UICONTROL Simulate content (AEP profiles)]** from the dropdown to preview with test profiles and add a test profile to check your message.

Detailed information on how to select test profiles and preview your content is available in the [Content Management](../content-management/preview-test.md) section.

## Review and activate your In-App notification{#in-app-review}

>[!IMPORTANT]
>
> If your campaign is subject to an approval policy, you will need to request approval in order to be able to send your In-App notification. [Learn more](../test-approve/gs-approval.md)

Once your In-App message is created, and its content defined and personalized, you can review and activate it.

To perform this, follow the steps below:

1. Use the **[!UICONTROL Review to activate]** button to display a summary of your message.

    The summary allows you to modify your campaign if necessary, and to check if any parameter is incorrect or missing.

    ![](assets/in_app_create_5.png)

1. Check that your campaign is correctly configured, then click **[!UICONTROL Activate]**.

Your campaign is now activated. The In-App notification configured in the campaign is sent immediately, or on the specified date.

Once sent, you can measure the impact of your In-App messages within the Campaign or Journey reports. For more on reporting, refer to [this section](../reports/campaign-global-report-cja-inapp.md).

**Related topics:**

* [Create an In-app message](create-in-app.md)
* [Design In-app message](design-in-app.md)
* [In-app report](../reports/campaign-global-report-cja-inapp.md)
* [In-app configuration](inapp-configuration.md)
