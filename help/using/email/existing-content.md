---
solution: Journey Optimizer
product: journey optimizer
title: Import your email content
description: Learn how to import email content
feature: Email Design
topic: Content Management
role: User
level: Intermediate
keywords: email, import, content, html, zip, css
exl-id: 52011299-0c65-49c3-9edd-ba7bed5d7205
TQID: https://experienceleague.adobe.com/R0Csd9gbvY-iyW81G-clHoXozEBYWBfjb0y9PWq4zZA
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
  - id: b5a62a22-46f7-4f0d-b151-3fc640bef588
    internal-label: Intermediate
---
# Import your email content {#existing-content}

>[!BEGINSHADEBOX]

**On this page:** Learn how to import existing HTML content, either as an HTML file or a .zip folder, and convert it so you can edit and personalize it with the Email Designer.

>[!ENDSHADEBOX]

[!DNL Journey Optimizer] allows you to import existing HTML content to design your emails. This content can be:

* An **HTML file** with an incorporated style sheet;
* A **.zip folder** including an HTML file, the style sheet (.css) and images.

    >[!NOTE]
    >
    >There are no constraints on the .zip file structure. However, references must be relative and fit with the tree structure of the .zip folder.


>[!TIP]
>
>If you have image designs (JPEG or PNG) instead of HTML files, you can use the [image to HTML converter](../content-management/image-to-html.md) to automatically convert them into editable HTML email templates using AI.

To import a file containing HTML content, follow the steps below:

1. From the Email Designer home page, select **[!UICONTROL Import HTML]**.

    ![](assets/import-html_2.png)

1. Drag and drop the HTML or .zip file containing your HTML content and click **[!UICONTROL Import]**.

    ![](assets/html-imported_2.png)

1. Once the HTML content is uploaded, your content will be in **[!UICONTROL Compatibility mode]**. 

    In this mode, you can only personalize your text, add links, or include assets to your content.

1. To be able to leverage the Email Designer content components, access the **[!UICONTROL HTML converter]** tab and click **[!UICONTROL Convert]**.

    ![](assets/html-imported.png)

    >[!NOTE]
    >
    > Using a `<table>` tag as the first layer in an HTML file can cause style loss, including background and width settings in the top layer tag.

1. You can now personalize your imported file as needed with the Email Designer functionalities. [Learn more](content-from-scratch.md)

## How-to video {#video}

Learn how to import existing HTML content, tweak the design, add mirror page and unsubscribe links, and how to code your content.

>[!VIDEO](https://video.tv.adobe.com/v/334102?quality=12)
