---
solution: Journey Optimizer
product: journey optimizer
title: Get started with journey activities
description: Get started with journey activities
feature: Journeys, Activities, Overview
topic: Content Management
role: User
level: Beginner, Intermediate
keywords: journey, activities, get started, events, action
exl-id: 239b3d72-3be0-4a82-84e6-f219e33ddca4
---
# Get started with journey activities {#about-journey-activities}

Combine the different event, orchestration and action activities to build your multi-step cross-channel scenarios.

## Events activities {#event-activities}

Personalized journeys are triggered by events, such as an online purchase. Once a profile enters a journey, they move through as an individual, and no two individuals are moving along at the same rate or along the same path. When you start your journey with an event, the journey is triggered when the event is received. Each person in the journey then follows, individually, the next steps defined in your journey. 

Events configured by the technical user (see [this page](../event/about-events.md)) are all displayed in the first category of the palette, on the left side of the screen. The following events activities are available:

* [General events](../building-journeys/general-events.md)
* [Reaction](../building-journeys/reaction-events.md)
* [Audience Qualification](../building-journeys/audience-qualification-events.md)

 ![](assets/journey43.png)

Start your journey by drag and dropping an event activity. You can also double-click on it.

 ![](assets/journey44.png)

## Orchestration activities {#orchestration-activities}

Orchestration activities are different conditions that help determine the next step in the journey. It can be if the person has an open support case or not, the weather forecast at their current location, if they completed a purchase or not, or reached 10 000 loyalty points.

From the palette, on the left-hand side of the screen, the following orchestration activities are available:

* [Condition](../building-journeys/condition-activity.md)
* [Wait](../building-journeys/wait-activity.md)
* [Read Audience](../building-journeys/read-audience.md)

![](assets/journey49.png)

## Action activities {#action-activities}

Actions are what you want to happen as result of some kind of trigger, like sending a message. It is the piece of journey that the customer experiences. 

From the palette, on the left-hand side of the screen, below **[!UICONTROL Events]** and **[!UICONTROL Orchestration]**, you can find the **[!UICONTROL Actions]** category. The following action activities are available:

* [Email, SMS, Push](../building-journeys/journeys-message.md)
* [Custom actions](../building-journeys/using-custom-actions.md)
* [Jump](../building-journeys/jump.md)

![](assets/journey58.png)

These activities represent the different available communication channels. You can combine them to create a cross-channel scenario. 

If you have configured custom actions, they also appear here. [Learn more](../building-journeys/using-custom-actions.md)).

## Best practices {#best-practices}

### Add a label

Most activities allow you to define a **[!UICONTROL Label]**. This adds a suffix to the name that will appear under your activity in the canvas. This is useful if you use the same activity several times in your journey and want to identify them more easily. It will also make debugging easier in case of errors and it will make reports easier to read. You can also add an optional **[!UICONTROL Description]**.

![](assets/journey-action-label.png)

>[!NOTE]
>
>For some activities, their ID is also visible in the pane. This ID can be used in reporting as a more stable key than the label, which can change.

### Manage the advanced parameters {#advanced-parameters}

Most activities display a number of advanced and/or technical parameters that you cannot modify.

![](assets/journey-advanced-parameters.png)

For better readability, you can hide these parameters using the **[!UICONTROL Hide read-only fields]** button.

![](assets/journey-hide-read-only-fields.png)

In some particular contexts, you can override the values of these parameters for specific use. To force a value, click the **[!UICONTROL Enable parameter override]** icon to the right of the field. [Learn more](../configuration/primary-email-addresses.md#journey-parameters)

![](assets/journey-enable-parameter-override.png)

### Add an alternative path

When an error occurs in an action or a condition, the journey of an individual stops. The only way to make it continue is to check the box **[!UICONTROL Add an alternative path in case of a timeout or an error]**. See [this section](../building-journeys/using-the-journey-designer.md#paths).

![](assets/journey42.png)
