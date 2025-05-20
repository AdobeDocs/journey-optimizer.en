---
solution: Journey Optimizer
product: journey optimizer
title: Publish the journey
description: Learn how to publish a journey
feature: Journeys
topic: Content Management
role: User
level: Intermediate
keywords: publish, journey, live, validity, check
exl-id: e0ca8aef-4f1d-4631-8c34-1692d96e8b51
---
# Publish your journey {#publishing-the-journey}

To activate a journey and allow new profiles to enter it, you must publish it. Publishing makes the journey live and functional. Before publishing, you must ensure the journey is complete and valid, and fix any errors, as a journey cannot be published if it contains errors.

➡️ [Discover this feature in video](#video)

## Publication process {#journey-publication}

Steps to publish a journey are detailed below:

1. Before publishing your journey, make sure it's valid and error-free. Journeys cannot be published if they contain any errors. 

    * Learn how to test your journey on [this page](testing-the-journey.md).
    * Learn how to troubleshoot your journey errors in [this section](../building-journeys/troubleshooting.md#checking-for-errors-before-testing).

1. To publish the journey, click on the **[!UICONTROL Publish]** option, located in the top right drop-down menu.

    >[!NOTE]
    >
    > If your journey is subject to an approval policy, you must request approval before you can publish it. [Learn more](../test-approve/gs-approval.md)


    ![](assets/journeyuc1_18.png)

When the journey is published, it is in **read-only** mode. When a journey is read-only, you can only modify the activity labels and descriptions, the journey's name and the journey's description. If you need to make more modifications to a published journey, create [a new version](journey-ui.md#journey-versions) of your journey. 

When you stop a journey, it is permanently stopped: all the persons flowing in the journey are permanently stopped, and the journey stops allowing new entrances. If you need to run the journey again, you must duplicate it and publish the new journey.


>[!IMPORTANT]
>
>If changes are made to an offer decision which is being used in a journey's message, you need to unpublish the journey and republish it.  This will ensure that the changes are incorporated into the journey's message and that the message is consistent with the latest updates.


## Journey versions {#journey-versions}

In the journey list, all journey versions are displayed with the version number. When you search for a journey, newest versions appear at the top of the list the first time the application opens. Then, you can define the sorting you want and the application will keep it as a user preference. The journey's version is also displayed at the top of the journey edition interface, above the canvas.

![](assets/journeyversions1.png)

>[!NOTE]
>
>Usually, a profile cannot be present multiple times in the same journey, at the same time, for all active versions of the journey. If reentrance is enabled, a profile can reenter a journey, but cannot do it until they fully exited that previous instance of the journey. [Read more](entry-management.md).

### Create a new version of a journey {#journey-create-new-version}

If you need to modify to a live journey, create a new version of your journey. To create a new version of an existing journey, follow the steps below:

1. Open the latest version of your live journey, click **[!UICONTROL Create a new version]** and confirm.

    ![](assets/journeyversions2.png)

    >[!NOTE]
    >
    >You can only create a new version from the latest version of a journey.

1. Make your modifications, click **[!UICONTROL Publish]** and confirm.

From the moment the journey is published, individuals will start to flow into the latest version of the journey. People who have already entered a previous version stay in it until they finish the journey. If they later reenter the same journey, they will go into the latest version.

Journey versions can be stopped individually. All versions of journeys have the same name.

When you publish a new version of a journey, the previous version automatically ends and switches to the **Closed** status. No entrance in the journey can happen. Even if you stop the latest version, the previous version stays closed.


>[!NOTE]
>
>Specific guardrails and limitation apply to the versioning of the journeys. Learn more on [this page](../start/guardrails.md#journey-versions-journey-versions-g).


## How-to video {#video}

Learn how to publish a journey in this video:

>[!VIDEO](https://video.tv.adobe.com/v/3424998?quality=12) 