---
solution: Journey Optimizer
product: journey optimizer
title: Test your content using custom profiles
description: Learn how to preview your content and send proofs using custom profiles.
feature: Overview, Get Started
topic: Content Management
role: User
level: Intermediate
badge: label="Beta"
hide: yes
hidefromtoc: yes
---

# Test your content using custom profiles {#custom-profiles}

>[!CONTEXTUALHELP]
>id="ajo_simulate_sample_profiles"
>title="Simulate using custom profiles"
>abstract="In this screen, you can preview your content and send proofs while impersonating custom profiles that you can upload from a CSV file or add manually directly from this screen."

>[!AVAILABILITY]
>
>This features is currently available as a beta to selected users only.
>
>Inbox rendering and spam reports are not available in the current experience. To use these features, select the **[!UICONTROL Simulate content]** button from your content to access the legacy user interface.

Journey optimizer allows you to preview and test your content using custom profiles that you can upload from a CSV file or add manually directly when simulating your content.

To access this experience, click the **[!UICONTROL Simulate content]** button and choose **[!UICONTROL Simulate with CSV(Beta)]**.

This screen allows you to select profiles to use to preview your content and send proofs. All the attributes used in your content for personalization are automatically detected by the system and can be used for your tests.

The main steps to test your content are as follows:

1. Add custom profiles, either by uploading a CSV file, or by adding them one by one manually. [Learn how to add custom profiles](#profiles)
1. Check the preview of your content using the added profiles. [Learn how to preview your content](#preview)
1. Send up to 10 proofs to the email addresses while impersonating the desired custom profiles. [Learn how to send proofs](#proofs)


## Add custom profiles {#profiles}

You can add custom profiles to test your content either using a CSV file, or manually:

* To upload profiles from a CSV file, click the **[!UICONTROL Download template]** link to retrieve a CSV file template. This templates includes a column for each personalization attribute used in your content.

    Fill in the CSV file then click the **[!UICONTROL Upload sample profiles]** to load it to test your content.

* To add a profile manually, click the **[!UICONTROL Create sample profile]** button and fill in the information for the profile. One field displays for each personalization attribute used in your content.

    ![](assets/simulate-custom-add.png)

Once profiles have been selected, one box appears for each profile on the left side of the screen. You can use these profiles to preview your content and send proofs.

## Preview your content using custom profiles {#preview}

To preview your content using one of the profiles, select the relevant box to update the content preview in the right section with the information entered for this profile.

You can remove a box at anytime using the ellipsis button in the upper-right corner and selecting **[!UICONTROL Remove]**. To edit information for a profile, click the ellipsis button and select **[!UICONTROL Edit]**.

![](assets/simulate-custom-boxes.png)

## Send proofs {#proofs}

Journey Optimizer allows you to send proofs to email addresses while impersonating one or multiple custom profiles that you have added in the simulation screen. The steps are as follows:

1. Verify that custom profiles have been added to test your content and clicck the **[!UICONTROL Send Proof]** button.

1. In the **[!UICONTROL Recipients]** field, enter the email address to which you want to send the proof then click **[!UICONTROL Add]**. Repeat the operation to send the proof to additional email addresses. You can add up to 10 proof recipients.

1. In the bottom section of the screen, select the custom profiles that you want to impersonate in the proof. You can select multiple profiles, in which case the email will include as many proofs as selected profiles.

    ![](assets/simulate-custom-proofs.png)

1. Click the **[!UICONTROL Send Proof]** button to start sending the proof.

You can track the sending at any time by clicking the **[!UICONTROL View proofs]** button in the simulate content screen.

![](assets/simulate-custom-sent-proofs.png)
