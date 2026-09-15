---
solution: Journey Optimizer
product: journey optimizer
title: Design content from scratch in Journey Optimizer
description: Learn how to design your content from scratch
feature: Email Design
topic: Content Management
role: User
level: Beginner, Intermediate
keywords: content, editor, email, start
exl-id: 151594f2-85e4-4c79-9c15-334fbd3768c4
TQID: https://experienceleague.adobe.com/mDgavy5F5CYnLmKBh84OSXFl-BHE82t-diUX6UXU27k
product_v2:
  - id: cb954087-f4fc-4456-afb9-e939cabcdc79
    internal-label: Journey Optimizer
feature_v2:
  - id: dc22c819-3f29-4e91-8b7d-5c6719831141
    internal-label: Content management
  - id: fe338112-e2ce-4876-8989-fc4d497613f1
    internal-label: Email
subfeature_v2:
  - id: c41e8697-e629-4c38-96b3-564faaa17acf
    internal-label: Dynamic content
  - id: ee5bb250-0884-4d71-86eb-d8489e8bcadd
    internal-label: Email design
  - id: f8d2e9f0-69c9-40cd-890f-71336c8dfff7
    internal-label: Preview
role_v2:
  - id: b69b2659-1057-424e-8fc5-ed9e016dc554
    internal-label: User
level_v2:
  - id: b5a62a22-46f7-4f0d-b151-3fc640bef588
    internal-label: Intermediate
  - id: e8ccd51f-da0d-4e3b-939b-e30d5ebb1ea5
    internal-label: Beginner
topic_v2:
  - id: cc72dcf1-72e1-48cc-b434-e7c27d62d67c
    internal-label: Accessibility
  - id: e0eb8757-182f-49f3-94a4-1587d16f5094
    internal-label: Personalization
---
# Design content from scratch with the Email Designer {#content-from-scratch}

>[!BEGINSHADEBOX]

**On this page:** Learn how to design email content from scratch in the Adobe Journey Optimizer Email Designer by adding structures and content components, then personalizing and previewing your email.

>[!ENDSHADEBOX]

>[!CONTEXTUALHELP]
>id="ac_structure_components_email"
>title="Add Structure components"
>abstract="Structure components define the layout of the email. Drag and drop a **Structure** component into the canvas to start designing your email content."

>[!CONTEXTUALHELP]
>id="ac_structure_components_landing_page"
>title="Add Structure components"
>abstract="Structure components define the layout of the landing page. Drag and drop a **Structure** component into the canvas to start designing the content of your landing page."

>[!CONTEXTUALHELP]
>id="ac_structure_components_fragment"
>title="Add Structure components"
>abstract="Structure components define the layout of the fragment. Drag and drop a **Structure** component into the canvas to start designing the content of your fragment."

>[!CONTEXTUALHELP]
>id="ac_structure_components_template"
>title="Add Structure components"
>abstract="Structure components define the layout of the template. Drag and drop a **Structure** component into the canvas to start designing the content of your template."


>[!CONTEXTUALHELP]
>id="ac_edition_columns_email"
>title="Define email columns"
>abstract="The Email Designer allows you to easily define the layout of your email by selecting the column structure."

>[!CONTEXTUALHELP]
>id="ac_edition_columns_landing_page"
>title="Define landing page columns"
>abstract="The Designer allows you to easily define the layout of your landing page by selecting the column structure."

>[!CONTEXTUALHELP]
>id="ac_edition_columns_fragment"
>title="Define fragment columns"
>abstract="The Designer allows you to easily define the layout of your fragment by selecting the column structure."

>[!CONTEXTUALHELP]
>id="ac_edition_columns_template"
>title="Define template columns"
>abstract="The Designer allows you to easily define the layout of your template by selecting the column structure."


Use the [!DNL Adobe Journey Optimizer] Email Designer to easily define the structure of your contents. By adding and moving structural elements with simple drag-and-drop actions, you can design the shape of your contents within seconds.

>[!NOTE]
>
>The [European accessibility act](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX%3A32019L0882){target="_blank"} states that all digital communications should be accessible. Make sure you follow the specific guidelines listed on [this page](accessible-content.md) when designing content in [!DNL Journey Optimizer].

To start building your content, follow the steps below:

1. From the Designer home page, select the **[!UICONTROL Design from scratch]** option.

    ![Create your email screen with the Design from scratch option highlighted, alongside Code your own and Import HTML options and sample templates below](assets/email_designer.png)

1. To get started quickly, use **[!UICONTROL Modules]** — ready-to-use, pre-designed content blocks such as headers, hero sections, and footers — to speed up email creation and keep your campaigns visually consistent. [Learn more about modules](email-modules.md)

    ![Email Designer with the Modules tab selected in the left panel, listing module categories such as Headers, Hero, Testimonial, Cards, Teams, and Footers](assets/email_designer_modules_tab.png)

1. Otherwise, design your content by drag and dropping **[!UICONTROL Structures]** into the canvas to define the layout of your email.

   >[!TIP]
   >
   >Alternatively, accelerate your email creation with Generate Content to generate complete email content, including text and images, using [Generate full content with AI](../content-management/generative-full-content.md). You can then skip ahead to previewing and validating your content.

1. Add as many **[!UICONTROL Structures]** as needed and edit their settings in the dedicated pane on the right.

    ![Email Designer with the Structures panel showing available column layouts, and the Settings and Styles tabs highlighted in the right Structure panel](assets/email_designer_structure_components.png)

    >[!NOTE]
    >
    >On narrow screens (e.g. mobile), columns stack vertically by default for readability. Some email clients don't support this behavior, in which case columns remain side-by-side. You can also turn this off using the **[!UICONTROL Do not stack columns on mobile]** toggle in the **[!UICONTROL Settings]** tab.

1. Most of the structures (**[!UICONTROL 1:1 column]**, **[!UICONTROL 2:2 column]**, **[!UICONTROL 1:2 column Left]**, and so on) are fixed presets. Select the **[!UICONTROL n:n column]** component instead to define any number of columns of your choice (between 3 and 10).

    ![Email Designer showing the Settings tab for a selected structure component, with the Columns number field highlighted](assets/email_designer_structure_columns.png)

    You can increase the **[!UICONTROL Columns number]** of an existing structure at any time from the **[!UICONTROL Settings]** tab, even after adding content to it — your existing content is preserved instead of being lost.

    You can also adjust the width of each column directly on the canvas or by editing the percentages in the **[!UICONTROL Settings]** tab.

    >[!NOTE]
    >
    >Each column size cannot be under 10% of the total width of the structure component. You cannot remove a column that is not empty.

1. From the **[!UICONTROL Contents]** section, add as many elements as you need into one or more structure components. [Learn more about content components](content-components.md)

1. Each component can be further customized using the **[!UICONTROL Settings]** or **[!UICONTROL Style]** tabs in the right menu. For example, you can change the text style, padding or margin of each component. [Learn more about alignment and padding](alignment-and-padding.md)

    ![Email Designer with the Contents panel highlighted on the left and the Settings tab for a selected Image component highlighted on the right, showing image source, alt text, and link fields](assets/email_designer_structure_component.png)

1. From the **[!UICONTROL Asset picker]**, you can directly select assets stored in the **[!UICONTROL Assets library]**. [Learn more about asset management](../integrations/assets.md)

    Double-click the folder which contains your assets. Drag and drop them into a structure component.

    ![Email Designer Assets panel showing the asset library files, with an image being dragged into the canvas](assets/email_designer_asset_picker.png)

1. Insert personalization fields to customize your content from profiles attributes, audience memberships, Contextual attributes, and more. [Learn more about content personalization](../personalization/personalize.md)

    ![Email Designer text toolbar with the Add Personalization button highlighted above a selected text block](assets/email_designer_personalization.png)

1. Click **[!UICONTROL Enable condition content]** to add dynamic content and adapt the content to the targeted profiles based on conditional rules. [Get started with dynamic content](../personalization/get-started-dynamic-content.md)

    ![Email Designer toolbar showing the Enable conditional content option above a text block containing a profile personalization token](assets/email_designer_dynamic-content.png)

1. Click the **[!UICONTROL Links]** tab from the left pane to display all the URLs of your content that will be tracked. You can modify their **[!UICONTROL Tracking Type]** or **[!UICONTROL Label]** and add **[!UICONTROL Tags]** if needed. [Learn more about links and tracking](message-tracking.md)

    ![Email Designer Links panel listing tracked URLs with their label and tracking type, and the details of a selected link expanded](assets/email_designer_links.png)

1. If needed, you can further personalize your email by clicking **[!UICONTROL Switch to code editor]** from the advanced menu. This allows you to edit the email source code, for example to add tracking or custom HTML tags. [Learn more about the code editor](code-content.md)

    >[!CAUTION]
    >
    >You cannot revert back to the visual designer for this email after switching to the code editor.

1. Once your content is ready, use either simulation method to check rendering. You can choose the desktop or mobile view. Detailed information is available in the [Content Management](../content-management/preview-test.md) section.

    ![Email Designer canvas with the Simulate Content button highlighted in the top toolbar](assets/email_designer_simulate_content.png)

1. You can also validate your content quality to assess readability, effectiveness, and content cohesiveness. [Learn more about content quality validation](../content-management/brands-score.md#validate-quality)

1. When your content is ready, click **[!UICONTROL Save]**.

{{$include /help/_includes/do-not-localize/email/ai-augmented-content-from-scratch.md}}
