---
title: Create a direct mail message
description: Learn how to create a direct mail message in Journey Optimizer
feature: Direct Mail
topic: Content Management
role: User
level: Beginner
keywords: direct mail, message, campaign
exl-id: 6b438268-d983-4ab8-9276-c4b7de74e6bd
---
# Create a direct mail message {#create-direct}

>[!CONTEXTUALHELP]
>id="ajo_direct_mail"
>title="Direct mail creation"
>abstract="Create direct mail messages in scheduled campaigns and design the extraction files required by direct mail providers to send mail to your customers."

To create direct mail messages, create a scheduled campaign, and configure the extraction file. This file is required by direct mail providers to send mail to your customers.

>[!IMPORTANT]
>
>Before creating a direct mail message, make sure you have configured:
>
>1. A [file routing configuration](../direct-mail/direct-mail-configuration.md#file-routing-configuration) which specifies the server where the extraction file should be uploaded and stored,
>1. A [direct mail message surface](../direct-mail/direct-mail-configuration.md#direct-mail-surface) which will reference the file routing configuration.


## Create a direct mail campaign{#create-dm-campaign}

To create a direct mail campaign, follow these steps:

1. Create a new scheduled campaign, and choose **[!UICONTROL Direct mail]** as the action.

1. Select the **[!UICONTROL Direct mail surface]** to use and click **[!UICONTROL Create]**. [Learn how to create a direct mail surface](direct-mail-configuration.md#direct-mail-surface).

   ![](assets/direct-mail-campaign.png){width="800" align="center"}

1. In the **[!UICONTROL Properties]** section, edit your Campaign's **[!UICONTROL Title]** and **[!UICONTROL Description]**.

1. To define your target audience, click the **[!UICONTROL Select audience]** button and choose from the available Adobe Experience Platform audiences. [Learn more](../audience/about-audiences.md).

   >[!IMPORTANT]
   >
   >For now, audience selection is restricted to 3 million profiles. This limitation can lifted upon request to your Adobe representative.

1. In the **[!UICONTROL Identity namespace]** field, select the appropriate namespace to identify individuals within the chosen audience. [Learn more](../event/about-creating.md#select-the-namespace).

   ![](assets/direct-mail-campaign-properties.png){width="800" align="center"}

1. Campaigns can be scheduled for a specific date or set to recur at regular intervals. Learn how to configure the **[!UICONTROL Schedule]** of your campaign in [this section](../campaigns/create-campaign.md#schedule). 
    
You can now start configuring the extraction file to send to your direct mail provider.

## Configure the extraction file {#extraction-file}

>[!CONTEXTUALHELP]
>id="ajo_direct_mail_data_fields"
>title="Data Fields"
>abstract="Add and configure the columns and the information to be displayed in the extraction file required by direct mail providers to send mail to your customers. You can add up to 50 columns."

>[!CONTEXTUALHELP]
>id="ajo_direct_mail_formatting"
>title="Extraction file formatting"
>abstract="For each field, specify a label and the information to display using the personalization editor. <br/><br/> The <b>Sort by</b> option allows you to use the selected field to sort the extraction file's columns."

1. Configure the columns and the information to be displayed in the extraction file:

   1. Click the **[!UICONTROL Add]** button to create a new column.

   1. The **[!UICONTROL Formatting]** pane displays on the right-hand side, allowing you to set up the selected column. Specify a **[!UICONTROL Label]** for the column.
   
   1. In the **[!UICONTROL Data]** field, select the profile attributes to display using the [personalization editor](../personalization/personalization-build-expressions.md).

   1. To sort the extraction file using a column, select the column and toggle on the **[!UICONTROL Sort by]** option. The **[!UICONTROL Sort By]** icon displays next to the column's label in the **[!UICONTROL Data Fields]** section.







The extraction file is required by direct mail providers to send mail to your customers. To define the extraction file configuration, follow these steps:

1. From the campaign configuration screen, click the **[!UICONTROL Edit content]** button to configure the extraction file content.

1. Adjust the extraction file properties:

   1. Specify the desired **[!UICONTROL Filename]** for the extraction file.
   
   1. Optionally, enable the **[!UICONTROL Append timestamp to export filename]** option if you want to add an automatic timestamp to the specified file name.

   1. Sometimes you may need to add information at the beginning or at the end of the extraction file. To do this, use the **[!UICONTROL Notes]** field then specify if you want to include the note as header or footer.

      ![](assets/direct-mail-properties.png){width="800" align="center"}

1. Configure the columns and the information to be displayed in the extraction file:

   1. Click the **[!UICONTROL Add]** button to create a new column.

   1. The **[!UICONTROL Formatting]** pane displays on the right-hand side, allowing you to set up the selected column. Specify a **[!UICONTROL Label]** for the column.
   
   1. In the **[!UICONTROL Data]** field, select the profile attributes to display using the [personalization editor](../personalization/personalization-build-expressions.md).

   1. To sort the extraction file using a column, select the column and toggle on the **[!UICONTROL Sort by]** option. The **[!UICONTROL Sort By]** icon displays next to the column's label in the **[!UICONTROL Data Fields]** section.

      ![](assets/direct-mail-content.png){width="800" align="center"}

   1. Repeat these steps to add as many columns as needed for your extraction file. Note that you can add up to 50 columns.

      To change the position of a column, drag and drop it to the desired location in the **[!UICONTROL Data field]** section. To delete a column, select it and click the **[!UICONTROL Remove]** button in the **[!UICONTROL Formatting]** pane.

You can now test your direct mail message and send it to your audience. [Learn how to test & send direct mail messages](test-send-direct-mail.md)
