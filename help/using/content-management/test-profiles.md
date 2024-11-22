---
title: Select test profiles
description: Learn how to select test profiles to preview and test content.
feature: Preview, Proofs
role: User
level: Beginner
exl-id: c51e4089-7f51-437d-a5ed-de10bab46cf8
---
# Select test profiles {#select-test-profiles}

>[!CONTEXTUALHELP]
>id="ajo_preview_test_profiles"
>title="Use test profiles to check your content"
>abstract="Use test profiles to preview and test your content. If you added personalized fields, you can check how they are displayed using test profile data."

Before previewing or testing your content, you first need to select test profiles, which are additional recipients who do not match the defined targeting criteria. [Learn how to create test profiles](../audience/creating-test-profiles.md)

>[!NOTE]
>
>In addition to test profiles, [!DNL Journey optimizer] also allows you to test different variants of your content by previewing it and sending proofs using sample input data uploaded from a CSV / JSON file, or added manually. [Learn how to test your content using sample input data](../test-approve/simulate-sample-input.md)

To select test profiles, follow these steps: 

1. From the edit content screen of your message or in the Email Designer, click the **[!UICONTROL Simulate content]** button.

1. Click the **[!UICONTROL Manage test profiles]** button then select the namespace to use to identify test profiles by clicking the **[!UICONTROL Identity namespace]** selection icon. [Learn more about Adobe Experience Platform identity namespaces](../audience/get-started-identity.md).
    
    In the example below, we use the **Email** namespace.

    ![](../email/assets/previewselect-namespace.png)

1. Use the search field to find the namespace, select it and click **[!UICONTROL Select]** 

    ![](../email/assets/preview-email-namespace.png)

1. In the **[!UICONTROL Identity value]** field, enter the value (here the email address) to identify the test profile and click **[!UICONTROL Add profile]**.

    <!--![](assets/preview-identity-value.png)-->

1. If you added personalization to your message, add other profiles so that you can test different variants of the message depending on profile data. Once added, profiles are listed under the selected fields.

    ![](../email/assets/preview-profile-list.png)

    Based on the message personalization elements, this list displays data for each test profile in the related columns.
