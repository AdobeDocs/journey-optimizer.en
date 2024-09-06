---
solution: Journey Optimizer
product: journey optimizer
title: Reactions events
description: Learn about reaction events
feature: Journeys, Activities
topic: Content Management
role: User
level: Intermediate
keywords: journey, events, reaction, tracking, platform
exl-id: 235384f3-0dce-4797-8f42-1d4d01fa42d9
---
# Reaction events {#reaction-events}

>[!CONTEXTUALHELP]
>id="ajo_journey_event_reaction"
>title="Reaction events"
>abstract="This activity allows you to react to tracking data related to a message sent within the same journey. We capture this information in real-time at the moment it is shared with Adobe Experience Platform."

Among the different event activities available in the palette, you will find the built-in **[!UICONTROL Reactions]** event. This activity allows you to react to tracking data related to a message sent within the same journey. We capture this information in real-time at the moment it is shared with Adobe Experience Platform. 

You can react to clicked or opened messages. 

You can also use this mechanism to perform an action when there is no reaction to your messages. To do this, create a second path parallel to the reaction activity and add a wait activity. If there is no reaction during the period defined in the wait activity, the second path will be chosen. You can choose to send, for example, a follow-up message. 

Note that you can only use a reaction activity in the canvas if there is a channel action activity before (Email and push).

See [About action activities](../building-journeys/about-journey-activities.md#action-activities).

 ![](assets/journey45.png)

Here are the different steps to configure the reaction events:

1. Add a **[!UICONTROL Label]** to the reaction. This step is optional.
1. From the drop-down list, select the action activity you want to react to. You can select any action activity positioned in the previous steps of the path.
1. Depending on the action you selected, choose what you want to react to. 
1. You can define an event timeout (between 40 seconds and 90 days) and a timeout path. This creates a second path for individuals who did not react within the defined duration. When testing a journey that uses a reaction event, the test mode **[!UICONTROL Wait time]** default and minimum value is 40 seconds. See [this section](../building-journeys/testing-the-journey.md).

>[!NOTE]
>
>
>Reaction events cannot track messages that take place in a different journey.
>
>Reaction events track clicks on links of the type "tracked". Unsubscription and mirror page links are not taken into account.

>[!IMPORTANT]
>
>Email clients such as Gmail allow image blocking. Email opens are tracked using a 0-pixel image included in the email. If images are blocked, email opens will not be taken into account.
