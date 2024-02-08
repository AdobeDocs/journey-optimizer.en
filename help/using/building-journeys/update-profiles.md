---
solution: Journey Optimizer
product: journey optimizer
title: Update Profile
description: Learn how to use the Update Profile activity in a journey
feature: Journeys, Profiles, Activities
topic: Content Management
role: User
level: Intermediate
keywords: profile, update, journey, activity
exl-id: 8b2b2d1e-9bd1-439d-a15e-acdbab387c4b
---
# Update Profile {#update-profile}

>[!CONTEXTUALHELP]
>id="ajo_journey_update_profiles"
>title="Update Profile activity"
>abstract="The Update Profile action activity allows you to update an existing Adobe Experience Platform profile with information coming from the event, a datasource or using a specific value."

Use the **[!UICONTROL Update Profile]** action activity to update an existing Adobe Experience Platform profile with information coming from an event, a datasource or with a specific value.

## Recommendations

* The **Update Profile** action can only be used in journeys starting with an event that has a namespace.
* The action only updates existing fields, it does not create new profile fields.
* You cannot use the **Update Profile** action to generate experience events, for example a purchase.
* Just like any other action, you can define an alternative path in case of error or timeout, and you cannot place two actions in parallel.
* The update request sent to Adobe Experience Platform is immediate/within a second. It will take normally a few seconds but sometimes more with no guarantee. As a result, for example, if an action is using "field 1" updated by an **Update Profile** action positioned right before, you should not expect that "field 1" will be updated in the action.
* The **Update profile** activity does not support XDM fields that are defined as an enumeration.
* The **[!UICONTROL Update profile]** activity only updates the [Profile Store](https://experienceleague.adobe.com/docs/experience-platform/profile/home.html#profile-data-store){target="_blank"}, not the Data Lake.
* When selecting a dataset in the **[!UICONTROL Update profile]** activity, it is advised to use one not targeted by data ingestion flows. Because **Update profile** updates are only stored in the [Profile Store](https://experienceleague.adobe.com/docs/experience-platform/profile/home.html#profile-data-store){target="_blank"}, there is a risk of overwriting such changes with a data ingestion flow. 

   Additionally, the **Update Profile** activity configuration does not require an identity namespace. As such, ensure that the selected dataset uses the same Identity namespace that was used by the action that launched the journey as it is this namespace these updates will use. The identity map can also be used by the selected dataset. Failure to select a data set with the correct namespace or one that uses identity map will cause the **Update Profile** activity to fail.



## Using the profile update

1. Design your journey by starting with an event. See this [section](../building-journeys/journey.md).

1. In the **Action** section of the palette, drop the **Update Profile** activity into the canvas.

   ![](assets/profileupdate0.png)

1. Select a schema from the list.

1. Click on **Field** to select the field you want to update. Only one field can be selected.

   ![](assets/profileupdate2.png)

1. Select a dataset from the list. 

   >[!NOTE]
   >
   >The **Update Profile** action updates the profile data in realtime, but it does not update datasets. The dataset selection is needed as the profile is a record related to a dataset.

1. Click on the **Value** field to define the value you want to use:

   * Using the simple expression editor, you can select a field from a data source or from the incoming event.

      ![](assets/profileupdate4.png)

   * If you want to define a specific value or leverage advanced functions, click on **Advanced mode**.

      ![](assets/profileupdate3.png)

The **Update Profile** is now configured.

![](assets/profileupdate1.png)


## Using the test mode {#using-the-test-mode}

In test mode, the profile update will not be simulated. The update will be performed on the test profile. 

Only test profiles can enter a journey in test mode. You can either create a new test profile or turn an existing profile into a test profile. In Adobe Experience Platform, you can update profiles attributes via a csv file import or API calls. A simpler method is to use an **Update Profile** action activity and change the test profile boolean field from false to true.

For more information on the how to turn an existing profile into a test profile, refer to this [section](../audience/creating-test-profiles.md#create-test-profiles-csv).
