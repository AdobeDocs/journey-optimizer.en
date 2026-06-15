---
solution: Journey Optimizer
product: journey optimizer
title: Attach a PDF file to an email
description: Learn how to attach static PDF files to an email
feature: Email Design
topic: Content Management
role: User
level: Beginner
keywords: email, messsage, attachment, pdf, editor
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

**On this page:** Learn how to attach a static PDF file to your emails, including the file size and sending volume limits that apply.

>[!ENDSHADEBOX]

>[!CONTEXTUALHELP]
>id="ajo_pdf_attachments"
>title="Add a PDF atttachment"
>abstract="Browse to select a PDF file to attach to your email.</br>You can send up to 6 messages with a PDF attachement per profile per year. The maximum allowed file size for each attachment is 5 MB.</br>For any additional size or volume, you can purchase an attachment pack add-on. For more details, contact your Adobe representative."

You can attach a static PDF file to the email messages that you send with [!DNL Journey Optimizer].

>[!IMPORTANT]
>
>* You can send up to 6 messages with a PDF attachement per profile per year.
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
