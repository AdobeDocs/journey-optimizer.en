---
title: Send email proofs
description: Learn how to send email proofs.
feature: Preview, Proofs
role: User
level: Beginner
exl-id: e742c04e-2987-4466-84af-bdaf4d714552
---
# Send email proofs {#send-proofs}

A proof is a specific message that allows you to test a message before sending it to the main audience. Recipients of the proof are in charge of approving the message: rendering, content, personalization settings, configuration.

Note that [!DNL Journey optimizer] also allows you to test different variants of your content by previewing it and sending proofs using sample input data uploaded from a CSV / JSON file, or added manually. [Learn how to test your content using sample input data](../test-approve/simulate-sample-input.md)

>[!PREREQUISITES]
>
>To send proofs, you must have **Approve and publish** permissions for the specific resource (campaign or journey) associated with the email. In addition, to send proofs in a journey, the **Publish journey** permission is also required. [Learn more about permissions](../administration/ootb-permissions.md).


To send email proofs, you must first select [test profiles](test-profiles.md). Then, follow these steps:

1. In the **[!UICONTROL Simulate]** screen, click the **[!UICONTROL Send proof]** button.

    ![](../email/assets/send-proof-button.png)

1. From the **[!UICONTROL Send proof]** window, type in your recipient's email and click **[!UICONTROL Add]** to send the proof to yourself or members of your organizations.

    Note that you can add up to ten recipients for your proof delivery.

    ![](../email/assets/send-proof-add.png)

1. Select the **Test profiles** to use to personalize the message content. 
    
    Each recipient of the proof receives as many messages as the number of selected test profiles. For example, if you added five recipient emails and selected ten test profiles, then you will send fifty proof messages, and each recipient will receive ten of them.

1. You can add a prefix to the subject line of the proof if needed. Only alphanumeric characters and special characters such as . - _ ( ) [ ] are allowed as prefix to the subject line.

1. Click **[!UICONTROL Send proof]**. 

    ![](../email/assets/send-proof-select.png)

1. Back in the **[!UICONTROL Simulate]** screen, click the  **[!UICONTROL View proofs]** button to check status.

    ![](../email/assets/send-proof-view.png)

It is recommended to send proofs after each modification to the message content.

>[!NOTE]
>
>In the proof sent, the link to the mirror page is not active. It is only activated in the final messages.
