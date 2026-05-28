---
solution: Journey Optimizer
product: journey optimizer
title: Use visual fragments
description: Learn how to use visual fragments when creating emails in Journey Optimizer campaigns and journeys
feature: Email Design, Fragments
topic: Content Management
role: User
level: Beginner
exl-id: 25a00f74-ed08-479c-9a5d-4185b5f3c684
TQID: https://experienceleague.adobe.com/YbH8cXjrh5E9v9twpwxB3ENb606W-1JAonJRxnorl9c
product_v2:
  - id: cb954087-f4fc-4456-afb9-e939cabcdc79
    internal-label: Journey Optimizer
feature_v2:
  - id: d556b755-390a-43f0-be32-a08cf6236126
    internal-label: Configuration
  - id: dc22c819-3f29-4e91-8b7d-5c6719831141
    internal-label: Content management
  - id: fe338112-e2ce-4876-8989-fc4d497613f1
    internal-label: Email
subfeature_v2:
  - id: b3a93754-a8b8-46eb-9421-7eccaeeb3dff
    internal-label: Best practices
  - id: b5cb2dff-e9ba-4e50-a3eb-6a50eef729b8
    internal-label: Email rendering
  - id: c6e980f5-2d4f-494f-beef-186b9ecf1513
    internal-label: Fragments
  - id: d08afb72-92f6-4856-88e3-11ec34313c2f
    internal-label: Event configuration
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
topic_v2:
  - id: c1579802-ddd4-4214-8a91-97b2066abe11
    internal-label: Troubleshooting
  - id: e0eb8757-182f-49f3-94a4-1587d16f5094
    internal-label: Personalization
---
# Add visual fragments to your emails {#use-visual-fragments}

A fragment is a reusable component that can be referenced in one or more emails across Journey Optimizer campaigns, journeys or content template. This functionality allows to prebuilt multiple custom content blocks that can be used by marketing users to quickly assemble email contents in an improved design process. [Learn how to create and manage fragments](../content-management/fragments.md).

➡️ [Learn how to manage, author and use fragments in this video](../content-management/fragments.md#video-fragments)

## Use a fragment {#use-fragment}

To use a fragment into an email, follow the steps below.

>[!NOTE]
>
>You can add up to 30 fragments in a given delivery. Fragments can only be nested up to 1 level.

1. Open any email or template content using the [Email Designer](get-started-email-design.md).

1. Select the **[!UICONTROL Fragments]** icon from the left rail.

    ![](assets/fragments-in-designer.png)

1. The list of all visual fragments created on the current sandbox is displayed. They are sorted by creation date: recently added visual fragments are shown first in the list. You can:

    * Search for a specific fragment by starting typing its label.
    * Sort fragments in ascending or descending order.
    * Change the way the fragments are displayed (cards or list view).
    * Refresh the list.

    >[!NOTE]
    >
    >If some fragments were modified or added while you are editing your content, the list will be updated with the latest changes.

1. Drag and drop any fragment from the list into the area where you want to insert it.

    ![](assets/fragment-insert.png)

    >[!CAUTION]
    >
    >You can add any **Draft** or **Live** fragment to your content. However, you won't be able to activate your journey or campaign if a fragment with the Draft status is being used in it. At journey or campaign publication, draft fragments will show an error and you'll need to approve them to be able to publish.
    
1. Like any other component, you can move the fragment around in your content.

1. Select the fragment to display the corresponding pane on the right. From there, you can delete the fragment from your content, or duplicate it. You can also perform these actions directly from the contextual menu that displays on top of the fragment.

    ![](assets/fragment-right-pane.png)

1. From the **[!UICONTROL Settings]** tab, you can:

    * Choose the devices you want the fragment to be displayed on.
    * Open the fragment in a new tab to edit it if needed. [Learn more](../content-management/fragments.md#fragments)
    * Explore references. [Learn more](../content-management/fragments.md#visual-expression)

1. You can further customize your fragment using the **[!UICONTROL Styles]** tab.

1. If needed, you can break the inheritance with the original fragment. [Learn more](#break-inheritance)

1. Add as many fragments as you want and **[!UICONTROL Save]** your changes.

### Limitations when using dynamic content in fragments {#fragment-dynamic-content}

>[!CAUTION]
>
>When working with fragments that contain Dynamic Content (conditional content), be aware of the following limitation:
>
>**Nesting fragments with Dynamic Content is not supported.** You cannot place a fragment containing Dynamic Content inside an unlocked fragment that also contains Dynamic Content. This unsupported configuration can cause:
>
>* Loss of conditional content mappings
>* Compatibility mode warnings in the Email Designer
>* Inconsistent email rendering
>
>**Recommended approach:** When using multiple fragments with Dynamic Content in your email, add each fragment directly into its own structure block at the email level. This ensures proper functionality and prevents the issues mentioned above.

## Best practices for fragments with dynamic content {#fragment-best-practices}

Follow these best practices when working with visual fragments and Dynamic Content (conditional content):

* **Structure your email properly**: When building emails with fragments containing Dynamic Content, add each fragment into a dedicated structure block at the email level. Avoid nesting fragments with Dynamic Content inside other unlocked fragments that also contain Dynamic Content.

* **Plan ahead**: Before adding fragments to your email, identify which ones contain Dynamic Content and plan your layout accordingly. This helps prevent configuration issues and ensures a clean structure from the start.

* **Design reusable fragments carefully**: When creating fragments that will include Dynamic Content, consider how they will be used. If a fragment needs to be nested within other fragments, avoid adding Dynamic Content to both the parent and child fragments.

* **Troubleshooting**: If you experience lost conditional content mappings or compatibility mode warnings:
    * Check your email structure for nested fragments containing Dynamic Content
    * Restructure by moving each fragment with Dynamic Content into its own structure block at the email level
    * Save and verify that conditional content mappings are properly restored

## Use implicit variables {#implicit-variables-in-fragments}

The implicit variables enhance the existing fragment functionality to improve efficiency for content reusability & scripting use cases. Fragments can use input variables and create output variables usable in campaign and journey content.

Learn how to use implicit variables in [this section](../personalization/use-expression-fragments.md#implicit-variables).

## Customize editable fields {#customize-fields}

If certain portions of the selected fragment have been made editable, you can override their default value after adding the fragment into your content. [Learn how to make fragments customizable](../content-management/customizable-fragments.md)

To customize editable fields in a fragment, follow these steps.

1. Add the fragment to your email content, and select it to open the properties pane on the right-hand side.

1. All editable fields in the fragment are displayed in the **[!UICONTROL Settings]** tab, under the **[!UICONTROL Fragment]** section.

    ![](assets/fragment-editable-rich-field.png)

1. Hover over each editable component in the central canvas. The component highlights in green and a pencil icon appears when clicking on it.

    ![](assets/fragment-editable-field-selected.png){width="70%" align="center"}

1. You can also select the editable fields on the right pane, making it easy to identify their locations in your content. However, the fields in the right-hand panel are read-only for customizable fragments.

1. In the example below, the image source and alt text can be edited, as well as the "Click here" button URL.

    ![](assets/fragment-editable.png)

1. Directly edit the content of the editable fields inline in the Email Designer canvas.

1. The Email Designer toolbar gives access to rich text options — bold, italic, hyperlinks, and more — for **Text**, **Button**, and **Html** components.

    >[!IMPORTANT]
    >
    >Fragments created before the rich-text editing capability was introduced have editable fields set to text-only mode by default. To enable rich text, go to the fragment editor and use the **Convert** button to upgrade it to HTML-compatible mode. [Learn how](../content-management/customizable-fragments.md#rich-text-visual)

    ![](assets/fragment-legacyeditable-fragment.png)

>[!CAUTION]
>
>When both the **label** and **URL** of a button component are made editable in a fragment, tracking reports show the URL instead of the button label. [Learn more about tracking](../email/message-tracking.md)

## Break inheritance {#break-inheritance}

When you edit a visual fragment, the changes are synchronized. They are automatically propagated to all draft or live journeys/campaigns and content templates containing that fragment.

When added to an email or a content template, fragments are synchronized by default. However, you can break the inheritance from the original fragment. In that case, the content of the fragment is copied into the current design, and the changes are not synchronized anymore.

To break inheritance, follow the steps below:

1. Select the fragment.

1. Click the unlock icon from the contextual toolbar.

    ![](assets/fragment-break-inheritance.png)

1. That fragment becomes a standalone element that is not linked anymore to the original fragment. Edit it as any other content component in your content. [Learn more](content-components.md)

### Locked fragments {#locked-fragments}

If the fragment was locked by its author, the unlock icon is greyed out and cannot be used to break inheritance.

![](assets/fragment-locked.png)

Locked fragments remain synchronized everywhere they appear, preventing local edits that could break brand standards or compliance requirements.

Learn how to lock a fragment in [this section](../content-management/create-fragments.md#lock-visual-fragment).

>[!NOTE]
>
>The fragment author can change the setting later for future usages by resetting its behavior to **[!UICONTROL Allow inheritance to be broken]** in the fragment settings.

