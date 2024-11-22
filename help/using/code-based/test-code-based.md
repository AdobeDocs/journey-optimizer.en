---
title: Test code-based experiences
description: Learn how to test code-based experiences in Journey Optimizer
feature: Code-based Experiences
topic: Content Management
role: User
level: Experienced
exl-id: 9a1c148c-a6c3-406b-8f2e-1cf8b8239e75
---
# Test code-based experiences {#test-code-based}

## Preview your code-based experience {#preview-code-based}

>[!CONTEXTUALHELP]
>id="ajo_code_based_preview"
>title="Preview your code-based experience"
>abstract="Get a simulation of what your code-based experience will look like."

To display a preview of your modified code-based experience, follow the steps below.

>[!CAUTION]
>
>You must have test profiles available to simulate which offers will be delivered to them. Learn how to [create test profiles](../audience/creating-test-profiles.md).

1. In the journey or campaign, from either the personalization editor or edit content screen, select **[!UICONTROL Simulate content]**.

    ![](assets/code-based-campaign-simulate.png)

1. Click **[!UICONTROL Manage test profiles]** to select one or more test profiles.

1. A preview of your modified code-based experience is displayed.

Detailed information on how to select test profiles and preview your content is available in [this section](../content-management/preview.md).

## Preview on device {#preview-on-device}

>[!CONTEXTUALHELP]
>id="ajo_code_based_preview_device"
>title="Preview your code-based experience on a real device"
>abstract="Get a preview of your personalized experiences right on your browser or on your mobile devices, to see how they look on real devices."

>[!CONTEXTUALHELP]
>id="ajo_code_based_preview_device_web"
>title="Preview your code-based web experience on device"
>abstract="Scan the QR code or copy the link to preview on device."

>[!CONTEXTUALHELP]
>id="ajo_code_based_preview_device_mobile"
>title="Preview your code-based mobile experience on device"
>abstract="Scan the QR code or copy the link to preview on device. Once connected, enter the pin on the device. You may need to restart your app to see the changes each time you update your preview links."

>[!CONTEXTUALHELP]
>id="ajo_code_based_preview_device_refresh"
>title="Refresh the preview link to reflect the current view"
>abstract="The on-device preview will show the content as of when you created or refreshed the preview link. If you've modified the content or selected a different test profile or treatment, refresh the preview to have it reflect the current view."

When building code-based experiences for web pages or mobile apps, you can preview your personalized experiences right on your browser or on your mobile devices, in order to see how these experiences look on real devices.

>[!WARNING]
>
>Preview on device is not available when using [decision policies](../experience-decisioning/create-decision.md) or [personalization](../personalization/personalization-build-expressions.md) contextual attributes.

1. From the **[!UICONTROL Simulate]** screen, click the **[!UICONTROL Open preview options]** button. The preview options depend on the platform selected in your [code-based configuration](code-based-configuration.md#create-code-based-configuration).

1. If you are using a [Web platform](code-based-configuration.md#web) in your code-based configuration, the **[!UICONTROL Device preview URL]** read-only field is pre-filled with the URL entered for the current channel configuration.

    ![](assets/preview-on-device-web.png)

    You can either:

    * Select the **[!UICONTROL Copy link]** button and paste the link into a browser tab. You can also share the link with your team and stakeholders, who can preview the new experience in any browser before the changes go live.

    * Click **[!UICONTROL Open in new tab]** to open the link in your current browser.

    * Scan the QR code with your mobile device to open the preview link on a mobile browser.

1. If you are using [Mobile platforms](code-based-configuration.md#mobile) (iOS / Android) in your code-based configuration, the **[!UICONTROL Deeplink]** read-only field is pre-filled with the **[!UICONTROL Preview URL]** value entered in the channel configuration for the selected platform.

    Toggle between the **[!UICONTROL iOS]** and **[!DNL Android]** tabs to preview your experience for the platform of your choice.

    ![](assets/preview-on-device-mobile.png)

    You can either:

    * Select the **[!UICONTROL Copy link]** button and share the link with your team and stakeholders, who can preview the new experience in any mobile browser before the changes go live.

    * Scan the QR code with your mobile device to open the preview link directly in the mobile application. You must enter the PIN on your device to establish the [Assurance](https://experienceleague.adobe.com/en/docs/experience-platform/assurance/tutorials/implement-assurance){target="_blank"} session.
       
        >[!NOTE]
        >
        >**Adobe Experience Platform Assurance** is a product from Adobe Experience Cloud to help you inspect, proof, simulate, and validate how you collect data or serve experiences in your mobile app. [Learn more](https://experienceleague.adobe.com/en/docs/experience-platform/assurance/home){target="_blank"}

1. Preview links are generated for the selected test profile and, if you are using [Content Experiment](../content-management/content-experiment.md) in your journey or campaign, for the selected treatment.

   <!--If you have modified the content or selected a different treatment or test profile, scroll down to the bottom of the **[!UICONTROL Preview on device]** pop-up and click **[!UICONTROL Refresh preview link]** to reflect the current state.

   ![](assets/preview-on-device-refresh.png)-->
   
   <!--When creating a content experiment, you need to select a given treatment and click the **[!UICONTROL Simulate content]** button to obtain the link corresponding to that treatment, then select another treatment, click the **[!UICONTROL Simulate content]** button to obtain a new preview link, and so on.-->

    >[!TIP]
    >
    >When updating the content, or selecting a different test profile or treatment, the preview link is automatically refreshed. You can copy the link into different browser tabs, and compare the experiences.
