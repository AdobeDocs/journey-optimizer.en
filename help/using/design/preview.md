---
title: Preview messages and send proofs
description: Learn how to preview and test your messages
feature: Journeys
topic: Content Management
role: User
level: Intermediate
exl-id: f2c2a360-a4b2-4416-bbd0-e27dd014e4ac
---
# Preview and test your messages{#preview-and-proof}

Once your message content has been defined, you can use test profiles to preview and test it. If you inserted [personalized content](../personalization/personalize.md), you can check how this content is displayed in the message, leveraging test profile data.

To detect possible errors in email content or personalization settings, send proofs to test profiles. A proof should be sent each time a change is made, to validate latest content. 

>[!CAUTION]
>
>You need to have test profiles available to be able to preview your messages and send proofs. 
>
>Learn how to create test profiles in [this page](../segment/creating-test-profiles.md). 

To test your message content, you need to:

* [select test profiles](#select-test-profiles)
* [check the message preview](#preview-your-messages)

You will then be able to [send proofs](#send-proofs) to your test profiles.

In addition, leverage your **Litmus** account into [!DNL Journey Optimizer] to instantly preview your **email rendering** in popular email clients. You can then ensure your email content looks great and works properly in every inbox. Learn how to unlock Litmus Email Previews in [this section](#email-rendering)

>[!CAUTION]
>
>When previewing a message or sending proofs, only profile personalization data is displayed. Personalization based on context data, such as event information, can only be tested in the context of a journey. Learn how to test personalization in [this use case](../personalization/personalization-use-case.md).

➡️ [Learn how to preview, proof, and publish your email in this video](#video-preview)

## Select test profiles{#select-test-profiles}

>[!CONTEXTUALHELP]
>id="ac_preview_testprofiles"
>title="Preview and test your messages"
>abstract="Once your message content has been defined, you can use test profiles to preview and test it."
>additional-url="https://experienceleague.adobe.com/docs/journey-optimizer/using/messages/validate/preview.html?lang=en#email-rendering" text="Email rendering"
>additional-url="https://experienceleague.adobe.com/docs/journey-optimizer/using/messages/validate/preview.html?lang=en#preview-your-messages" text="Preview"

Use [Test profiles](../segment/creating-test-profiles.md) to target additional recipients who do not match the defined targeting criteria.

To select test profiles, follow the steps below: 

1. In the message interface or in the email designer, click the **[!UICONTROL Simulate Content]** button to access the test profile selection.

    ![](assets/email-preview-button.png)

1. Select the namespace to use to identify test profiles by clicking the **[!UICONTROL Identity namespace]** selection icon. 

    ![](assets/previewselect-namespace.png)

    Learn more about Adobe Experience Platform identity namespaces [in this section](../segment/get-started-identity.md).
    
    In the example below, we will use the **Email** namespace.

1. Use the search field to find the namespace, select it and click **[!UICONTROL Select]** 

    ![](assets/preview-email-namespace.png)

1. Enter the value to identify the test profile and click **[!UICONTROL Add profile]**.

    ![](assets/preview-identity-value.png)

1. If you added personalization in your message, add other profiles so that you can test different variants of the message depending on profile data. Once added, profiles are listed under the selection fields.

    ![](assets/preview-profile-list.png)

    Based on the message personalization elements, this list displays data for each test profile in the related columns.

## Preview messages{#preview-your-messages}

Once [test profiles](#select-test-profiles) are selected, you can preview your messages and check content.

### Email preview{#preview-email}

To preview an email content, follow the steps below:

1. Click the **[!UICONTROL Simulate content]** button above the email content. 

1. Select a test profile. You can check the values available in the columns. Use the right/left arrows to browse data.

    ![](assets/preview-tab-select-profile.png)

1. Click the **[!UICONTROL Select data]** icon above the list to add or remove columns.

    ![](assets/preview-select-data.png)
    
    You can see personalization fields specific to the current message at the end of the list. In this example, the profile city, first name and last name. Select those fields and make sure these values are populated in your test profiles.

1. In the message preview, personalized elements are replaced by the selected test profile data.

    For example, for this message, both email content and email subject are personalized:

    ![](assets/preview-test-profile.png)

1. Select other test profiles to preview email rendering for each variant of your message.

### Push preview{#preview-push}

To preview a push notification content, follow the steps below:

1. Click the **[!UICONTROL Simulate content]** button above the push content. 

1. Select a test profile. You can check the values available in the columns. Use the right/left arrows to browse data.


1. Switch to the **[!UICONTROL Push]** message and.

1. Apply the same steps as described above to select a test profile, and select the type of device to preview content: **[!UICONTROL iOS]** or **[!UICONTROL Android]**.

    ![](assets/preview-iOS.png)

1. In the push preview, test profile data is leveraged in the message content.

    For example, for this push notification, both title and body are personalized:

    ![](assets/preview-android.png)

## Send proofs{#send-proofs}

A proof is a specific message that allows you to test a message before sending it to the main audience. Recipients of the proof are in charge of approving the message: rendering, content, personalization settings, configuration.

Once [test profiles](#select-test-profiles) are selected, you can send proofs.

1. In the **[!UICONTROL Preview]** screen, click the **[!UICONTROL Send proof]** button.

    ![](assets/send-proof-button.png)

1. From the **[!UICONTROL Send proof]** window, type in your recipient's email and click **[!UICONTROL Add]** to send the proof to yourself or members of your organizations.

    Note that you can add up to ten recipients for your proof delivery.

    ![](assets/send-proof-button_2.png)

1. Then, select the **Test profiles** which will be used to personalize the message content. 
    
    Each recipient of the proof will receive as many messages as the number of selected test profiles. For example, if you added five recipient emails and selected ten test profiles, then you will send fifty proof messages, and each recipient will receive ten of them.

1. You can add a prefix to the subject line of the proof if needed. Only alphanumeric characters and special characters e.g., . - _ ( ) [ ], are allowed as prefix to the subject line.

1. Click **[!UICONTROL Send proof]**. 

    ![](assets/send-proof-select.png)

1. Back in the  **[!UICONTROL Preview]** screen, click the  **[!UICONTROL View proofs]** button to check status.

    ![](assets/send-proof-view.png)

It is recommended to send proofs after each modification to the message content.

>[!NOTE]
>
>In the proof sent to the test profiles, the link to the mirror page is not active. It is only activated in the final messages.

## Email rendering{#email-rendering}

You can leverage your **Litmus** account into [!DNL Journey Optimizer] to instantly preview your **email rendering** in popular email clients.

To access Email rendering capabilities, you need to:

* Have a Litmus account
* [Select test profiles](#select-test-profiles)

Then, follow the steps below:

1. In the Email Designer, click the **[!UICONTROL Preview]** button and select the **[!UICONTROL Email rendering]** tab.

1. Click **Connect your Litmus account** on the upper right section.

    ![](assets/email-rendering-litmus.png)

1. Enter your credentials and sign in.

    ![](assets/email-rendering-credentials.png)

1. Click the **Run test** button to generate email previews.

1. Check your email content in popular desktop, mobile and web-based clients.

    ![](assets/email-rendering-previews.png)

>[!CAUTION]
>
>When connecting your **Litmus** account with [!DNL Journey Optimizer], you agree that test messages are sent to Litmus: once sent, these emails are no longer managed by Adobe. As a consequence, Litmus data retention email policy applies to these emails, including personalization data that may be included in these test messages.

## How-to video{#video-preview}

Learn how to test email rendering across inboxes, how to preview your personalized emails against test profiles, send proofs, and publish your email.

>[!VIDEO](https://video.tv.adobe.com/v/334239?quality=12)
