---
title: Create an In-app notification in Journey Optimizer
description: Learn how to create an In-app message in Journey Optimizer
feature: In App
topic: Content Management
role: User
level: Beginner
keywords: in-app, message, creation, start
exl-id: b3b79fe2-7db3-490d-9c3d-87267aa55eea
---
# Create an In-app message {#create-in-app}

>[!CONTEXTUALHELP]
>id="ajo_campaigns_inapp_triggers"
>title="Manage In-app Triggers"
>abstract="Efficiently control your Triggers by selecting the specific events and criteria that will activate your messages. With the Rule builder, users can define precise conditions and values. When these conditions are met, they initiate a series of actions, including the delivery of in-app messages."

You can add an In-app message in a campaign or in a journey. Follow the steps detailed below to create an In-app message in both contexts.

Note that In-app messages are not impacted by the user's choice to opt-in or opt-out of push notifications at the operating system.

>[!BEGINTABS]

>[!TAB Add an In-app message to a journey]

To add an In-app message in a journey, follow these steps:

1. Open your journey, then drag and drop an **[!UICONTROL In-app]** activity from the **[!UICONTROL Actions]** section of the palette.

    When a profile reaches the end of their journey, any in-app messages displayed to them will automatically expire. For that reason, a Wait activity is automatically added after your In-app activity to ensure proper timing.

    ![](assets/in_app_journey_1.png)

1. Enter a **[!UICONTROL Label]** and **[!UICONTROL Description]** for your message.

1. Choose your [In-app configuration](inapp-configuration.md#channel-prerequisites) to use.

    ![](assets/in_app_journey_2.png)

1. You can now start designing your content with the **[!UICONTROL Edit content]** button. [Learn more](design-in-app.md)

1. Click **[!UICONTROL Edit triggers]** to choose the event(s) and criteria that will trigger your message. Rule builders enable users to specify criteria and values that, when met, trigger a set of actions, such as sending an in-app message.

    ![](assets/in_app_journey_4.png)

    1. Click the event drop-down to change your Trigger if needed.
        
        +++See available Triggers.
        
        | Package | Trigger | Definition |
        |---|---|---|
        |Send data to Platform|Sent data to Platform|Triggered when the mobile app issues an edge experience event to send data to Adobe Experience Platform. Usually the API call [sendEvent](https://developer.adobe.com/client-sdks/documentation/edge-network/api-reference/#sendevent) from the AEP Edge extension.|
        |Core tracking|Track action| Triggered when the legacy functionality offered in mobile code API [trackAction](https://developer.adobe.com/client-sdks/documentation/mobile-core/api-reference/#trackaction) is called.|
        |Core tracking|Track state |Triggered when the legacy functionality offered in mobile code API [trackState](https://developer.adobe.com/client-sdks/documentation/mobile-core/api-reference/#trackstate) is called.|
        |Core tracking|Collect PII|Triggered when the legacy functionality offered in mobile code API [collectPII](https://developer.adobe.com/client-sdks/documentation/mobile-core/api-reference/#collectpii) is called.|
        |Application lifecycle|Application launch|Triggered at every run, including crashes and installs. Also triggered on a resume from the background when the lifecycle session timeout has been exceeded.|
        |Application lifecycle|Application install|Triggered at the first run after installation or re-installation.|
        |Application lifecycle|Application update|Triggered at the first run after an upgrade or when the version number changes.|
        |Application lifecycle|Application close|Triggered when the application is closed. |
        |Application lifecycle|Application crash|Triggered when the application is not backgrounded before being closed. The event is sent when the application is started after the crash. Adobe Mobile crash reporting does not implement a global uncaught exception handler.|
        |Places|Enter POI| Triggered by the Places SDK when your customer enters the Point of Interest (POI) that you configured.|
        |Places|Exit POI| Triggered by the Places SDK when your customer exits the Point of Interest (POI) that you configured.|

        +++
    
    1. Click **[!UICONTROL Add condition]** if you want the trigger to consider multiple events or criteria.

    1. Choose the **[!UICONTROL Or]** condition if you want to add more **[!UICONTROL Triggers]** to further expand your rule.

        ![](assets/in_app_create_3.png)

    1. Choose the **[!UICONTROL And]** condition if you want to add **[!UICONTROL Traits]** and better fine-tune your rule.

        +++See available Traits.
        
        | Package | Traits | Definition |
        |---|---|---|
        |Device info|Carrier name|Triggered when one of the Carrier name from the list is met.|
        |Device info|Device name|Triggered when one of the Device name is met.|
        |Device info|Locale|Triggered when one of the language from the list is met.|
        |Device info|OS version|Triggered when one of the specified OS version is met.|
        |Device info|Previous OS version|Triggered when one of the specified Previous OS version is met.|
        |Device info|Run mode|Triggered if Run mode is either application or extension.|
        |Application lifecycle|App ID| Triggered when the specified App ID is met.| 
        |Application lifecycle|Day of week|Triggered when the specified day of week is met.|
        |Application lifecycle|Day since first use|Triggered when the specified number of day since first use is met.|
        |Application lifecycle|Day since last use|Triggered when the specified number of day since last use is met.|
        |Application lifecycle|Day since upgrade|Triggered when the specified number of day since last upgrade is met.|
        |Application lifecycle|Install date|Triggered when the specified Install date is met.|
        |Application lifecycle|Launches|Triggered when the specified number of Launches is met.|
        |Application lifecycle|Time of day|Triggered when the specified Time of day is met.|
        |Places|Current POI|Triggered by the Places SDK when your customer enters the specified Point of Interest (POI).|
        |Places|Last entered POI|Triggered by the Places SDK depending on your customer last entered Point of Interest (POI).|
        |Places|Last exited POI|Triggered by the Places SDK depending on your customer last exited Point of Interest (POI).|

        +++
        
        ![](assets/in_app_create_8.png)

    1. Click **[!UICONTROL Make group]** to group triggers together.

        ![](assets/in_app_journey_3.png)

    1. Choose the frequency of your trigger when your In-app message is active:

        * **[!UICONTROL Show every time]**: Always show the message when the events selected in the **[!UICONTROL Mobile app trigger]** drop-down occur.
        * **[!UICONTROL Show once]**: Only show this message the first time the events selected in the **[!UICONTROL Mobile app trigger]** drop-down occur.
        * **[!UICONTROL Show until click through]**: Show this message when the events selected in the **[!UICONTROL Mobile app trigger]** drop-down occur until an interact event is sent by the SDK with an action of "clicked".
    
1. If necessary, complete your journey flow by dragging and dropping additional actions or events. [Learn more](../building-journeys/about-journey-activities.md)

1. Once your In-app message is ready, finalize the configuration and publish your journey to activate it.

For more information on how to configure a journey, refer to [this page](../building-journeys/journey-gs.md).

>[!TAB Add an In-app message to a campaign]

To add an In-app message in a campaign, follow these steps:

1. Access the **[!UICONTROL Campaigns]** menu, then click **[!UICONTROL Create campaign]**.

1. Select the type of campaign that you want to execute

    * **Scheduled - Marketing**: execute the campaign immediately or on a specified date. Scheduled campaigns are aimed at sending marketing messages. They are configured and executed from the user interface.

    * **API-triggered - Marketing/Transactional**: execute the campaign using an API call. API-triggered campaigns are aimed at sending either marketing, or transactional messages, i.e. messages sent out following an action performed by an individual: password reset, cart purchase etc.

1. From the **[!UICONTROL Properties]** section, enter the **[!UICONTROL Title]** and the **[!UICONTROL Description]** description.

1. To assign custom or core data usage labels to the In-app message, select **[!UICONTROL Manage access]**. [Learn more](../administration/object-based-access.md).

1. Click the **[!UICONTROL Select audience]** button to define the audience to target from the list of available Adobe Experience Platform audiences. [Learn more](../audience/about-audiences.md).

    ![](assets/in_app_create_2.png)

1. In the **[!UICONTROL Identity namespace]** field, choose the namespace to use in order to identify the individuals from the selected audience. [Learn more](../event/about-creating.md#select-the-namespace).

1. In the **[!UICONTROL Actions]** section, choose the **[!UICONTROL In-app message]** and select or create a new configuration.

    Learn more about In-app configuration in [this page](inapp-configuration.md).

    ![](assets/in_app_create_1.png)

1. Click **[!UICONTROL Create experiment]** to start configuring your content experiment and create treatments to measure their performance and identify the best option for your target audience. [Learn more](../content-management/content-experiment.md)

1. Click **[!UICONTROL Edit triggers]** to choose the event(s) and criteria that will trigger your message. Rule builders enable users to specify criteria and values that, when met, trigger a set of actions, such as sending an in-app message.

    1. Click the event drop-down to change your Trigger if needed.
        
        +++See available Triggers.
        
        | Package | Trigger | Definition |
        |---|---|---|
        |Send data to Platform|Sent data to Platform|Triggered when the mobile app issues an edge experience event to send data to Adobe Experience Platform. Usually the API call [sendEvent](https://developer.adobe.com/client-sdks/documentation/edge-network/api-reference/#sendevent) from the AEP Edge extension.|
        |Core tracking|Track action| Triggered when the legacy functionality offered in mobile code API [trackAction](https://developer.adobe.com/client-sdks/documentation/mobile-core/api-reference/#trackaction) is called.|
        |Core tracking|Track state |Triggered when the legacy functionality offered in mobile code API [trackState](https://developer.adobe.com/client-sdks/documentation/mobile-core/api-reference/#trackstate) is called.|
        |Core tracking|Collect PII|Triggered when the legacy functionality offered in mobile code API [collectPII](https://developer.adobe.com/client-sdks/documentation/mobile-core/api-reference/#collectpii) is called.|
        |Application lifecycle|Application launch|Triggered at every run, including crashes and installs. Also triggered on a resume from the background when the lifecycle session timeout has been exceeded.|
        |Application lifecycle|Application install|Triggered at the first run after installation or re-installation.|
        |Application lifecycle|Application update|Triggered at the first run after an upgrade or when the version number changes.|
        |Application lifecycle|Application close|Triggered when the application is closed. |
        |Application lifecycle|Application crash|Triggered when the application is not backgrounded before being closed. The event is sent when the application is started after the crash. Adobe Mobile crash reporting does not implement a global uncaught exception handler.|
        |Places|Enter POI| Triggered by the Places SDK when your customer enters the Point of Interest (POI) that you configured.|
        |Places|Exit POI| Triggered by the Places SDK when your customer exits the Point of Interest (POI) that you configured.|

        +++
    
    1. Click **[!UICONTROL Add condition]** if you want the trigger to consider multiple events or criteria.

    1. Choose the **[!UICONTROL Or]** condition if you want to add more **[!UICONTROL Triggers]** to further expand your rule.

        ![](assets/in_app_create_3.png)

    1. Choose the **[!UICONTROL And]** condition if you want to add **[!UICONTROL Traits]** and better fine-tune your rule.

        +++See available Traits.
        
        | Package | Traits | Definition |
        |---|---|---|
        |Device info|Carrier name|Triggered when one of the Carrier name from the list is met.|
        |Device info|Device name|Triggered when one of the Device name is met.|
        |Device info|Locale|Triggered when one of the language from the list is met.|
        |Device info|OS version|Triggered when one of the specified OS version is met.|
        |Device info|Previous OS version|Triggered when one of the specified Previous OS version is met.|
        |Device info|Run mode|Triggered if Run mode is either application or extension.|
        |Application lifecycle|App ID| Triggered when the specified App ID is met.| 
        |Application lifecycle|Day of week|Triggered when the specified day of week is met.|
        |Application lifecycle|Day since first use|Triggered when the specified number of day since first use is met.|
        |Application lifecycle|Day since last use|Triggered when the specified number of day since last use is met.|
        |Application lifecycle|Day since upgrade|Triggered when the specified number of day since last upgrade is met.|
        |Application lifecycle|Install date|Triggered when the specified Install date is met.|
        |Application lifecycle|Launches|Triggered when the specified number of Launches is met.|
        |Application lifecycle|Time of day|Triggered when the specified Time of day is met.|
        |Places|Current POI|Triggered by the Places SDK when your customer enters the specified Point of Interest (POI).|
        |Places|Last entered POI|Triggered by the Places SDK depending on your customer last entered Point of Interest (POI).|
        |Places|Last exited POI|Triggered by the Places SDK depending on your customer last exited Point of Interest (POI).|

        +++
        
        ![](assets/in_app_create_8.png)

    1. Click **[!UICONTROL Make group]** to group triggers together.

1. Choose the frequency of your trigger when your In-app message is active. The following options are available:

    * **[!UICONTROL Everytime]**: Always show the message when the events selected in the **[!UICONTROL Mobile app trigger]** drop-down occur.
    * **[!UICONTROL Once]**: Only show this message the first time the events selected in the **[!UICONTROL Mobile app trigger]** drop-down occur.
    * **[!UICONTROL Until click through]**: Show this message when the events selected in the **[!UICONTROL Mobile app trigger]** drop-down occur until an interact event is sent by the SDK with an action of "clicked".
    * **[!UICONTROL X number of times]**: Show this message X time.

1. If needed, choose which **[!UICONTROL Day of the week]** or **[!UICONTROL Time of day]** the In-app message will be displayed.

1. Campaigns are designed to be executed on a specific date or on a recurring frequency. Learn how to configure the **[!UICONTROL Schedule]** of your campaign in [this section](../campaigns/create-campaign.md#schedule). 

    ![](assets/in-app-schedule.png)

1. You can now start designing your content with the **[!UICONTROL Edit content]** button. [Learn more](design-in-app.md)

    ![](assets/in_app_create_4.png)

>[!ENDTABS]

## How-to videos{#video}

* The video below shows how to create, configure, and publish In-app messages in your campaigns.
    
    +++See video

    >[!VIDEO](https://video.tv.adobe.com/v/3410430?quality=12&learn=on)

    +++

* The video below shows how to configure and analyze content experiments to A/B test In-app messages.

    +++See video

    >[!VIDEO](https://video.tv.adobe.com/v/3419898/?learn=on&autoplay=true)

    +++

* The video below shows how to create an In-app message in a journey and how to test and publish your journey.

    +++See video

    >[!VIDEO](https://video.tv.adobe.com/v/3423077/?learn=on&autoplay=true)

    +++

**Related topics:**

* [Design In-app message](design-in-app.md)
* [Test and send your In-app message](send-in-app.md)
* [In-app report](../reports/campaign-global-report-cja-inapp.md)
* [In-app configuration](inapp-configuration.md)