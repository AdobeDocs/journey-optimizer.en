---
solution: Journey Optimizer
product: journey optimizer
title: Test your content using sample input data (Beta)
description: Learn how to preview content and send email proof using sample input data from a CSV or JSON file or added manually.
feature: Email, Email Rendering, Personalization, Preview, Proofs
topic: Content Management
role: User
level: Intermediate
badge: label="Beta"
---

# Test your content using sample input data (Beta) {#custom-profiles}

>[!CONTEXTUALHELP]
>id="ajo_simulate_sample_profiles"
>title="Simulate using sample input"
>abstract="In this screen, you can test different variants of your content by providing values for personalization fields through a CSV or JSON template, or by manually entering the values."

>[!AVAILABILITY]
>
>This features is currently available to all customers as a public beta.

Journey optimizer allows you to test different variants of your content by previewing it and sending proofs using sample input data uploaded from a CSV or JSON file or added manually. All the profiles attributes used in your content for personalization are automatically detected by the system and can be used for your tests to create multiple variants.

>[!NOTE]
>
>For now, simulating content variations is available for the Email, SMS and Push notification channels only.

To access this experience, click the **[!UICONTROL Simulate content]** button and choose **[!UICONTROL Simulate content variations (Beta)]**.

![](assets/simulate-sample.png)

The main steps to test your content are as follows:

1. Add up to 30 variants with sample input data, either by uploading a file, or by adding data manually. [Learn how to add variants](#profiles)
1. Check the preview of your content using the different variants. [Learn how to preview your content](#preview)
1. For email content, send up to 10 proofs to email addresses using the different variants. [Learn how to send proofs](#proofs)


## Guardrails & limitations {#limitations}

Before starting testing your content using sample input data, consider the following guardrails and prerequisites.

* As of now, testing using sample input data is only available for the Email, SMS and Push notification channels. The experience cannot be accessed from the "Simulate content" button within the Email Designer.
* The following features are not available in the current experience: Inbox rendering, spam reports, multilingual content and content experiment. To use these features, select the **[!UICONTROL Simulate content]** button from your content to access the previous user interface.
* Only profile attributes are currently supported. If contextual attributes are used in your content for personalization, you won't be able to test your content using these attributes.
* Only the following data types are supported when entering data for your variants : number (integer and decimal), string, boolean and date type. Any other data type will show an error.

## Add variants {#profiles}

You can add up to 30 variants to test your content, either using a file, or manually.

>[!NOTE]
>
>The added variants only serve as testing purposes for your current content. The are not stored within Adobe Experience Platform, but into your user browser session, meaning that they won't display when logging off, or when working from another device.

### Add variant using a file {#file}

To add a variant from a file, follow these steps:

1. Click the **[!UICONTROL download sample]** link to retrieve a file template, then choose the file format you want to use (CSV, JSON or JSONLINES).

1. Click **[!UICONTROL Download]** then store the template at the desired location.

1. Open the file then fill in the template to suit your needs. The template includes a column for each profile attribute used in your content for personalization.

1. When your file is ready, click the **[!UICONTROL Upload Input data]** to load it to test your content.

1. Once the file has been uploaded, a box is added in the left pane for each line from the file. Each box contains all the profile attributes used in your content for personalization. You can now use the variants use them to preview your content in the right pane, and send proofs.

    ![](assets/simulate-custom-variants.png)

### Add variants manually {#manual}

To add a variant manually, follow these steps:

1. Click the **[!UICONTROL Create sample input]** button.

    A box is added in the left pane with all the profile attributes used in your content for personalization. 

1. Fill in the sample input data for the variant and click **[!UICONTROL Save]**.

    ![](assets/simulate-custom-add.png)

1. Once variants have been added, you can use them to preview your content in the right pane, and send proofs.

## Preview your content variants {#preview}

To preview your content using one of the variants, select the relevant box to update the content preview in the right section with the information entered for this variant.

You can remove a variant at anytime using the ellipsis button in the upper-right corner and selecting **[!UICONTROL Remove]**. To edit information for a variant, click the ellipsis button and select **[!UICONTROL Edit]**.

![](assets/simulate-custom-boxes.png)

## Send proofs {#proofs}

Journey Optimizer allows you to send proofs to email addresses while impersonating one or multiple variants that you have added in the simulation screen. The steps are as follows:

1. Verify that variants have been added to test your content and click the **[!UICONTROL Send Proof]** button.

1. In the **[!UICONTROL Recipients]** field, enter the email address to which you want to send the proof then click **[!UICONTROL Add]**. Repeat the operation to send the proof to additional email addresses. You can add up to 10 proof recipients.

1. In the bottom section of the screen, select the variant that you want to use in the proof. You can select multiple variants, in which case the email will include as many proofs as selected variants.

    For more information on a variant, select the **[!UICONTROL View profile details]** link. This allows you to display the information entered in the previous screen for the different variants.

    ![](assets/simulate-custom-proofs.png)

1. Click the **[!UICONTROL Send Proof]** button to start sending the proof.

1. To track the proof sending, click the **[!UICONTROL View proofs]** button in the simulate content screen.

![](assets/simulate-custom-sent-proofs.png)
