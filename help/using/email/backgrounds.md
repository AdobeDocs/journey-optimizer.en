---
solution: Journey Optimizer
product: journey optimizer
title: Personalize your email background
description: Learn how to personalize your email background
feature: Email Design
topic: Content Management
role: User
level: Beginner, Intermediate
keywords: background, email, color, editor
exl-id: 09a2e892-8c6f-460d-8b12-5026582c6ed0
TQID: https://experienceleague.adobe.com/8kFppIm3Q-zHDqalE0Vt0CK5Z1ts9fGspVu476TapSk
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
  - id: c41e8697-e629-4c38-96b3-564faaa17acf
    internal-label: Dynamic content
role_v2:
  - id: b69b2659-1057-424e-8fc5-ed9e016dc554
    internal-label: User
level_v2:
  - id: b5a62a22-46f7-4f0d-b151-3fc640bef588
    internal-label: Intermediate
  - id: e8ccd51f-da0d-4e3b-939b-e30d5ebb1ea5
    internal-label: Beginner
---
# Personalize your email background {#backgrounds}

>[!BEGINSHADEBOX]

**On this page:** Learn how to set background colors and images at the body, viewport, structure, and column levels of your email in the Email Designer.

>[!ENDSHADEBOX]

>[!CONTEXTUALHELP]
>id="ac_edition_backgroundimage"
>title="Background settings"
>abstract="You can personalize the background color or background image for your content. Note that background image is not supported by all email clients." 

When it comes to setting backgrounds with the Email Designer, Adobe recommends the following:

1. Apply a background color to the body of your email if required by your design.
1. Usually, set background colors at the column level.
1. Try not to use background colors on image or text components as they are difficult to manage.

Below are the available background settings that you can use.

1. Set a **[!UICONTROL Background color]** for the whole email. Make sure you select the body settings in the navigation tree accessible from the left Palette.

    ![](assets/background_1.png)

1. Set a **[!UICONTROL Viewport color]** to apply the same background color across all structure components, independently of the body's background color.

    ![](assets/background_2.png)

1. To apply a background color to a single structure component, select it and set a specific **[!UICONTROL Background color]** for that structure.

    ![](assets/background_3.png)

    >[!TIP]
    >
    >In that case, make sure you do not set a viewport background color as it may hide the structure background colors.

1. Set a **[!UICONTROL Background image]** for the content of a structure component.

    >[!NOTE]
    >
    >Some email programs do not support background images. When not supported, the row background color will be used instead. Make sure you select an appropriate fallback background color in case the image cannot be displayed.

    Once a background image is set, use the **[!UICONTROL Image placement]** dropdown to control how the image fills the structure or column:

    * **[!UICONTROL Fit]** - Stretches the image to fill the container on both axes, without preserving its aspect ratio.
    * **[!UICONTROL Full Width]** - Scales the image proportionally to the container's width and centers it vertically.
    * **[!UICONTROL Full Width - Top]** - Same as **[!UICONTROL Full Width]**, anchored to the top of the container. Overflow is cropped at the bottom.
    * **[!UICONTROL Full Width - Bottom]** - Same as **[!UICONTROL Full Width]**, anchored to the bottom of the container. Overflow is cropped at the top.
    * **[!UICONTROL Full Height]** - Scales the image proportionally to the container's height and centers it horizontally.
    * **[!UICONTROL Full Height - Left]** - Same as **[!UICONTROL Full Height]**, anchored to the left of the container. Overflow is cropped on the right.
    * **[!UICONTROL Full Height - Right]** - Same as **[!UICONTROL Full Height]**, anchored to the right of the container. Overflow is cropped on the left.
    * **[!UICONTROL Repeat]** - Tiles the image at its original size to fill the container.
    * **[!UICONTROL Left]**, **[!UICONTROL Right]**, **[!UICONTROL Center]**, **[!UICONTROL Top]**, **[!UICONTROL Bottom]** - Positions the image at its original size, anchored to the corresponding edge or center of the container.

    ![](assets/background_4.png)

    >[!NOTE]
    >
    >**[!UICONTROL Full Width - Top]**, **[!UICONTROL Full Width - Bottom]**, **[!UICONTROL Full Height - Left]**, and **[!UICONTROL Full Height - Right]** give you more control over which part of the image stays in view when it doesn't match the structure's proportions, compared to using **[!UICONTROL Fit]**, **[!UICONTROL Full Width]**, or **[!UICONTROL Full Height]** alone.

1. Finally, you can set a background color at the column level.

    ![](assets/background_5.png)

    >[!NOTE]
    >
    >This is the most common use case. Adobe recommends setting background colors at the column level as this allows for more flexibility when editing the whole email content.

    You can also set a background image at the column level, but this is rarely used.

![](assets/background_6.png)

{{$include /help/_includes/do-not-localize/email/ai-augmented-backgrounds.md}}
