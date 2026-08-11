---
solution: Journey Optimizer
product: journey optimizer
title: Attach a PDF file to an email
description: Learn how to attach static or personalized PDF files to an email
feature: Email Design
topic: Content Management
role: User
level: Beginner
keywords: email, message, attachment, pdf, editor, personalized, API-triggered
exl-id: 71e218d0-5b3b-4db5-8b7b-d08df8f088c4
TQID: https://experienceleague.adobe.com/9IgYERskcUrIAhTb3xlNgWTRyY-04O58ZB8I0lYFh4g
product_v2:
  - id: cb954087-f4fc-4456-afb9-e939cabcdc79
    internal-label: Journey Optimizer
feature_v2:
  - id: dc22c819-3f29-4e91-8b7d-5c6719831141
    internal-label: Content management
  - id: fe338112-e2ce-4876-8989-fc4d497613f1
    internal-label: Email
subfeature_v2:
  - id: ee5bb250-0884-4d71-86eb-d8489e8bcadd
    internal-label: Email design
  - id: fb9a80eb-bebc-492f-a0e9-584595621ebb
    internal-label: Publish
role_v2:
  - id: b69b2659-1057-424e-8fc5-ed9e016dc554
    internal-label: User
level_v2:
  - id: e8ccd51f-da0d-4e3b-939b-e30d5ebb1ea5
    internal-label: Beginner
---
# Attach a PDF file to an email {#pdf-attachments}

>[!BEGINSHADEBOX]

**On this page:** Learn how to attach static or personalized PDF files to emails, including the supported campaign types and applicable count, size, and volume limits.

>[!ENDSHADEBOX]

>[!CONTEXTUALHELP]
>id="ajo_pdf_attachments"
>title="Add a PDF attachment"
>abstract="Browse to select a PDF file to attach to your email.</br>You can send up to 6 messages with a PDF attachment per profile per year. The maximum allowed file size for each attachment is 5 MB.</br>For any additional size or volume, you can purchase the PDF Attachments add-on. For more details, contact your Adobe representative."

You can attach a static PDF file to the email messages that you send with [!DNL Journey Optimizer]. If you use [API-triggered campaigns](../campaigns/api-triggered-campaigns.md), you can also attach a [personalized PDF file for each recipient](#personalized-attachments).

Note that personalized PDF attachments require additional file retrieval and processing. Campaigns using them may have higher processing latency and lower throughput than campaigns without attachments, particularly when using multiple or larger PDF files.

>[!IMPORTANT]
>
>* You can send up to 6 messages with a PDF attachment per profile per year, whether the attachment is static or personalized.
>
>* The maximum allowed file size for each attachment is 5 MB.
>
>For any additional size or volume, you can purchase the PDF Attachments add-on. For more details, contact your Adobe representative.

To attach a PDF file to an email message, follow the steps below.

1. Create an email in a journey or a campaign. [Learn more](create-email.md)

1. From the journey or campaign **[!UICONTROL Content]** tab, select **[!UICONTROL Add asset]** from the **[!UICONTROL Attachment]** section.

    ![](assets/email-select-pdf.png)

1. The Assets Essentials repository displays.

    >[!NOTE]
    >
    >When designing messages, you access the Assets Essentials repository directly from within the Journey Optimizer interface. To learn more about the embedded [!DNL Assets Essentials] user interface, refer to [Experience Manager Assets Essentials documentation](https://experienceleague.adobe.com/docs/experience-manager-assets-essentials/help/introduction.html){target="_blank"}.

1. Use the **[!UICONTROL PDF]** filter in the **[!UICONTROL MIME Type]** section to restrict selection to the correct file format.

    ![](assets/email-assets-pdf.png)

    >[!NOTE]
    >
    >Only the PDF format is allowed for attachments.

1. Select the file of your choice.

    * You can only select one file at a time.
    * The maximum allowed file size for each attachment is 5 MB.

1. Once done, the name and size of the selected file display in the **[!UICONTROL Attachment]** section.

    You can remove the selected file using the More actions icon next to the file name.

    ![](assets/email-remove-attachment.png)

>[!NOTE]
>
>When you save your message as [content template](../content-management/create-content-templates.md), the PDF attachment is not retained with the template. If you create a new email from the saved content template, you need to reattach the file.

## Attach personalized PDF files for API-triggered campaigns {#personalized-attachments}

You can also attach recipient-specific PDF files to a single email sent through an [API-triggered campaign](../campaigns/api-triggered-campaigns.md). Unlike a static attachment, each recipient can receive a different file, such as an invoice, a boarding pass, a contract, or a shipping label. 

The combined size of all static and personalized PDF attachments in an email is limited to 5 MB by default. Organizations with the applicable PDF Attachments add-on can use a combined limit of up to 10 MB.

>[!IMPORTANT]
>
>* Personalized PDF attachments are supported only for transactional API-triggered email campaigns.
>
>* You can include up to five PDF attachments in an email. This limit includes both static and personalized attachments. For example, an email containing one static PDF can include up to four personalized PDFs. If you need to send more, split them across multiple communications.
>
>* Personalized and static PDF attachments count toward the same quota. [Learn more](#pdf-attachments)

Personalized PDF attachments must be uploaded to the attachment-specific [Data Landing Zone](https://experienceleague.adobe.com/en/docs/experience-platform/sources/connectors/cloud-storage/data-landing-zone){target="_blank"} container, then referenced in the API payload. Data Landing Zone is currently the only supported storage location for personalized PDF attachments.

1. Retrieve the Data Landing Zone credentials for your sandbox using `type=ajoemailattachments` for the same IMS organization and sandbox as the execution request, as described in the [Adobe Experience Platform documentation](https://experienceleague.adobe.com/en/docs/experience-platform/sources/connectors/cloud-storage/data-landing-zone){target="_blank"}. Depending on the cloud provider, use the Azure container or AWS bucket and folder returned by the API.

1. Generate the PDF files with the tool of your choice, and upload them to your Data Landing Zone container. 
  
  Note that Data Landing Zone automatically deletes files after seven days, so make sure your PDF files remain available in the container until the message and any retries have been delivered.

1. In the API payload, for each recipient, add an `attachments` array containing the file name, content type, and Data Landing Zone path of the PDF to send. [Learn how to personalize your API-triggered campaign content](../campaigns/api-triggered-campaign-content.md#contextual)

At send time, [!DNL Journey Optimizer] fetches the file from the specified location and attaches it to the message for that recipient. Personalized PDF attachments are supported for [High Throughput](../campaigns/api-triggered-high-throughput.md) campaigns in the primary region. They are not supported during regional failover.

For the full API payload reference, see the [Interactive Message Execution API documentation](https://developer.adobe.com/journey-optimizer-apis/references/messaging#tag/execution){target="_blank"}.
