---
solution: Journey Optimizer
product: journey optimizer
title: Adobe Experience Platform data source
description: Learn how to configure Adobe Experience Platform data source
feature: Journeys, Data Sources
topic: Administration
role: Data Engineer, Data Architect, Admin
level: Intermediate, Experienced
keywords: built-in, source, data, platform, integration 
exl-id: 9083e355-15e3-4d1f-91ae-03095e08ad16
---
# Adobe Experience Platform data source {#adobe-experience-platform-data-source}

>[!CONTEXTUALHELP]
>id="ajo_journey_data_source_built_in"
>title="Adobe Experience Platform data source"
>abstract="Adobe Experience Platform data source defines the connection to Adobe Real-time Customer Profile. This data source is built-in and pre-configured, and cannot be deleted. It is designed to retrieve and use data from the Real-time Customer Profile Service (for example, check if the person who entered a journey is a female). It allows you to use Profile data and Experience Events data."

Adobe Experience Platform data source defines the connection to Adobe Real-time Customer Profile. This data source is built-in and pre-configured, and cannot be deleted. This data source is designed to retrieve and use data from the Real-time Customer Profile Service (for example, check if the person who entered a journey is a female). It allows you to use Profile data and Experience Events data. For more information about Adobe Real-time Customer Profile, refer to [Adobe Experience Platform documentation](https://experienceleague.adobe.com/docs/experience-platform/profile/home.html){target="_blank"}.

To allow the connection to the Real-time Customer Profile Service, we must use a key to identify a person, and a namespace that contextualizes the key. As a result, you can only use this data source if your journeys start with an event containing a key and a namespace. [Learn more](../building-journeys/journey.md).

You can edit the pre-configured field group named “ProfileFieldGroup”, add new ones and remove the ones that are not used in any draft or live journeys. [Learn more](../datasource/configure-data-sources.md#define-field-groups).

>[!NOTE]
>
>You can retrieve the 1000 latest experience events created less than a year ago.

Here are the main steps to add field groups to the build-in data source.

1. From the list of data sources, select the build-in Adobe Experience Platform data source.

    This opens the data source configuration pane on the right-hand side of the screen.

    ![](assets/journey23.png)

1. Click **[!UICONTROL Add a New Field Group]** to define a new series of fields to retrieve. [Learn more](../datasource/configure-data-sources.md#define-field-groups).

    ![](assets/journey24.png)

1. Select a schema from the **[!UICONTROL Schema]** drop-down. This field lists Profile and Experience Events schemas available in Adobe Experience Platform. Schema creation is not performed in [!DNL Journey Optimizer]. It’s performed in Adobe Experience Platform.
1. Select the fields you want to use.
1. Click on **[!UICONTROL Save]**.

When you place the cursor on the name of a field group, you’ll see two icons on the right. They allow you to delete and duplicate the field group. Note that the **[!UICONTROL Delete]** icon is only available if the field group is not used in any live or draft journey (information displayed in the **[!UICONTROL Used in]** field).
