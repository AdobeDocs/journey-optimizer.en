---
solution: Journey Optimizer
product: journey optimizer
title: Set up Android mobile
description: Learn how to configure and monitor Android mobile channels
feature: Surface, Channel Configuration
topic: Administration
role: Admin
level: Experienced
keywords: channel, surface, technical, parameters, optimizer
hide: yes
hidefromtoc: yes
---
# Set up Android mobile configuration {#set-mobile-android}

>[!IMPORTANT]
>
>To ensure compatibility and optimal performance, please make sure to use the following SDK versions:
>
> * Core 3.1.0 or later
> * Messaging 3.1.0 or later

This Android setup streamlines the quick configuration of marketing channels, ensuring that all necessary resources are easily accessible within the Experience Platform, Journey Optimizer, and Data Collection apps. This enables your marketing team to promptly begin creating campaigns and journeys.

## Create a new Android set up {#new-setup-android}

>[!CONTEXTUALHELP]
>id="ajo_mobile_web_setup_android_initialization_code"
>title="Add initialization code"
>abstract="TBC"

>[!CONTEXTUALHELP]
>id="ajo_mobile_web_setup_android_dependencies_add"
>title="Add dependencies"
>abstract="You need to add the following libraries to your project using the app's Gradle file: Core, Assurance, Edge, Edge Identity, and Messaging."

>[!CONTEXTUALHELP]
>id="ajo_mobile_web_setup_android_dependencies_import"
>title="Import dependencies"
>abstract="In the Application class of your app, import the following packages: Mobile Core, Assurance, Edge, Edge Identity, and Messaging."
>additional-url="https://experienceleague.adobe.com/en/docs/platform-learn/implement-mobile-sdk/app-implementation/install-sdks#import-extensions" text="See Data collection documentation"

<!--
>[!CONTEXTUALHELP]
>id="ajo_mobile_web_setup_push_token_android"
>title="Retrieve the device token"
>abstract="TBC"

>[!CONTEXTUALHELP]
>id="ajo_mobile_web_setup_push_android_studio"
>title="Launch the application from Android Studio"
>abstract="TBC"
-->

1. From Journey Optimizer homepage, click **[!UICONTROL Begin]** from the **[!UICONTROL Set up mobile and web channels]** card.

    ![](assets/guided-setup-config-1.png)

1. Create a **[!UICONTROL New]** configuration.

    If you already have existing configurations, you can choose to select one, or create a new configuration.

    ![](assets/guided-setup-config-2.png)

1. Enter a **[!UICONTROL Name]** for your new configuration and select or create your **[!UICONTROL Datastream]**. This **[!UICONTROL Name]** will be used for every auto-created resources.

1. If your organization has multiple datastreams, please select one from the existing options. If you do not have a Datastream, one will be auto-created for you.

1. Select the Android platform you wish to set up and click **[!UICONTROL Auto-create resources]**.

    ![](assets/guided-setup-config-4.png)

1. To streamline the setup process, the necessary resources are automatically created to help you get started. This includes the creation of a new **[!UICONTROL Mobile Tag Property]** and installation of extensions.

    Below is a comprehensive list of all the resources that are auto generated:

    +++ Created resources

    <table>
    <thead>
    <tr>
    <th><strong>Solution</strong></th>
    <th><strong>Auto-created resources</strong></th>
    </tr>
    </thead>
    <tbody>
    <tr>
    <td>
    <p>Journey Optimizer</p>
    </td>
    <td>
    <ul>
    <li>Channel Configuration</li>
    <li>Push Credential (mobile push message only)</li>
    </ul>
    </td>
    </tr>
    <tr>
    <td>
    <p>Tags</p>
    </td>
    <td>
    <ul>
    <li>Mobile Tag Property</li>
    <li>Rules</li>
    <li>Data Elements</li>
    <li>Library</li>
    <li>Environments (staging, production, development)</li>
    </ul>
    </td>
    </tr>
    <tr>
    <td>
    <p>Tags Extensions</p>
    </td>
    <td>
    <ul>
    <li>Adobe Experience Platform Edge Network</li>
    <li>Adobe Journey Optimizer</li>
    <li>AEP Assurance</li>
    <li>Consent (with default consent policies enabled)</li>
    <li>Identity (with default ECID, with default stitching rules)</li>
    <li>Mobile Core</li>
    </ul>
    </td>
    </tr>
    <tr>
    <td>
    <p>Assurance</p>
    </td>
    <td>
    <p>Assurance Session</p>
    </td>
    </tr>
    <tr>
    <td>
    <p>Datastreams</p>
    </td>
    <td>
    <p>Datastream with Services</p>
    </td>
    </tr>
    <tr>
    <td>
    <p>Experience Platform</p>
    </td>
    <td>
    <ul>
    <li>Dataset</li>
    <li>Schema</li>
    </ul>
    </td>
    </tr>
    </tbody>
    </table>

    +++

1. Once resources generation is done, click **[!UICONTROL Set up]** to start configuring your SDK.

    ![](assets/guided-setup-config-android-1.png)

1. You first need to add and import dependencies as described in the user interface. [Learn more](https://experienceleague.adobe.com/en/docs/platform-learn/implement-mobile-sdk/app-implementation/install-sdks).

1. Copy-paste the following code to your Application's onCreate() method.

1. To validate your SDK directly on your mobile application, simply open your mobile application and allow access to [Adobe Assurance](https://experienceleague.adobe.com/en/docs/experience-platform/assurance/home). Assurance is a powerful tool that allows you to thoroughly test and validate your implementation, ensuring that everything is working correctly. 

    Once connected, your device will be automatically detected and listed in the **[!UICONTROL Available Device]** drop-down menu, allowing you to seamlessly monitor and troubleshoot your setup in real time.

    ![](assets/guided-setup-config-android-2.png)

1. Click **[!UICONTROL Connect]**.

1. You can now configure your [In-app](#inapp-channel) and/or [Push](#push-channel) channels.

1. After completing the configuration, share the auto-generated **[!UICONTROL Channel Configuration]** with the team members responsible for creating Journeys and Campaigns. 

    The **[!UICONTROL Channel Configuration]** should be referenced in the Campaigns or Journeys interface, enabling a seamless connection between your setup and the execution of targeted journeys and campaigns for your audience.

    ![](assets/guided-setup-config-ios-8.png)

## Modify an existing configuration {#reconnect}

After creating your configuration, you can easily revisit it at any time to add additional channels or make further adjustments to suit your needs

1. From Journey Optimizer homepage, click **[!UICONTROL Begin]** from the **[!UICONTROL Set up mobile and web channels]** card.

    ![](assets/guided-setup-config-1.png)

1. Select **[!UICONTROL Existing]** and choose your existing **[!UICONTROL Tag property]** from the drop-down.

    ![](assets/guided-setup-config-6.png)

1. When accessing your existing configuration, you need to reconnect with Adobe Assurance. From the SDK Setup menu, click **[!UICONTROL Reconnect]**.

1. Select your device from the **[!UICONTROL Available devices]** drop-down and click **[!UICONTROL Connect]**.

1. You can now update your configuration as needed.

## Set up In-app channel {#inapp-channel}

>[!CONTEXTUALHELP]
>id="ajo_mobile_web_setup_inapp_tag_property"
>title="Choose your tag property"
>abstract="TBC"

The In-app channel requires no additional setup. To verify that your configuration is accurate, you can effortlessly send a test message using the Assurance feature. This will provide immediate feedback on the system's readiness to deliver In-app messages effectively.

To do this, simply click **[!UICONTROL Display In-app message]**.

To streamline the setup process, the necessary resources are automatically created to help you get started. This includes the creation of a Channel Configuration.

You can now send In-app messages using the previously configured **[!UICONTROL Channel Configuration]**. [Learn how to create In-app messages](../in-app/create-in-app.md)

## Set up Push channel {#push-channel}

>[!CONTEXTUALHELP]
>id="ajo_mobile_web_setup_push_token"
>title="Retrieve the device token"
>abstract="To ensure the device's push token is properly synchronized with your Adobe Experience Platform profile, you need to incorporate the following code into your application. This integration is essential for maintaining up-to-date communication capabilities and ensuring a seamless user experience."

>[!CONTEXTUALHELP]
>id="ajo_mobile_web_setup_push_xcode"
>title="Launch the application from Xcode"
>abstract="TBC"

>[!CONTEXTUALHELP]
>id="ajo_mobile_web_push_certificate_fcm"
>title="Provide a push certificate"
>abstract="Drag and drop your .json private key file. This file contains authentication information required for secure integration and communication between your application and the server."

1. Once your mobile SDK has been configured, click **[!UICONTROL Add]** from the Push notification card.

1. Retrieve the Device token by inserting the provided code within the `FireBaseMessaging.getInstance.getToken ()` callback function in the user interface.

1. Register the Messaging Service by adding the provided code in the user interface to your `AndroidManifest.xml` file.

1. Drag and drop your .json private key file.

1. To verify that your configuration is accurate, you can effortlessly send a test message using the Assurance feature. This will provide immediate feedback on the system's readiness to deliver push notifications effectively.

    To do this, simply click **[!UICONTROL Send push message]**.

To streamline the setup process, the necessary resources are automatically created to help you get started. This includes the creation of a **[!UICONTROL Channel Configuration]** and **[!UICONTROL Push Credential]**.

You can now send push notifications using the previously configured **[!UICONTROL Channel Configuration]**. [Learn how to create push notification](../push/create-push.md)
