---
solution: Journey Optimizer
product: journey optimizer
title: Create a fragment
description: Learn how to create fragments to reuse content in Journey Optimizer campaigns and journeys
feature: Fragments
topic: Content Management
role: User
level: Beginner, Intermediate
exl-id: da3ffe9c-a244-4246-b4b5-a3a1d0508676
---
# Create a fragment from scratch {#create-fragments}

>[!CONTEXTUALHELP]
>id="ajo_create_visual_fragment"
>title="Select the visual type"
>abstract="Create a standalone visual fragment to make your content reusable in an email within a journey or a campaign, or in a content template."
>additional-url="https://experienceleague.adobe.com/docs/journey-optimizer/using/email/design-email/add-content/use-visual-fragments.html" text="Add visual fragments to your emails"

>[!CONTEXTUALHELP]
>id="ajo_create_expression_fragment"
>title="Select the expression type"
>abstract="Create a standalone expression fragment to make your content reusable across multiple journeys and campaigns. When using the personalization editor, you can leverage all the expression fragments that have been created on the current sandbox."
>additional-url="https://experienceleague.adobe.com/docs/journey-optimizer/using/content-management/personalization/expression-editor/use-expression-fragments.html" text="Leverage expression fragments"

Fragments are created from the **[!UICONTROL Fragments]** left menu. In addition, you can also save a portion of existing content as fragment when designing content. [Learn how](#save-as-fragment)

Once saved, your fragment is available for use in a journey, a campaign or a template. You can now use this fragment when building any content within [!DNL Journey Optimizer]. See [Add visual fragments](../email/use-visual-fragments.md) and [Leverage expression fragments](../personalization/use-expression-fragments.md)

To create a fragment from scratch, follow the steps below.

1. [Access the fragment list](#access-manage-fragments) through the **[!UICONTROL Content Management]** > **[!UICONTROL Fragments]** left menu.

1. Select **[!UICONTROL Create fragment]**.

1. Fill in the fragment details, i.e. name and description (if needed).

    ![](assets/fragment-details.png)

1. Select or create Adobe Experience Platform tags from the **[!UICONTROL Tags]** field to categorize your fragment for improved search. [Learn more](../start/search-filter-categorize.md#tags)

1. Select the fragment type: [Visual fragment](#create-visual-fragment) or [Expression fragment](#create-expression-fragment).

    >[!NOTE]
    >
    >Currently for visual fragments only the **Email** channel is supported.

1. If you are creating an expression fragment, select the type of code you want to use: **[!UICONTROL HTML]**, **[!UICONTROL JSON]** or **[!UICONTROL Text]**.

    ![](assets/fragment-expression-type.png)

1. To assign custom or core data usage labels to the fragment, select **[!UICONTROL Manage access]**. [Learn more on Object Level Access Control (OLAC)](../administration/object-based-access.md).

1. Click **[!UICONTROL Create]**.

1. The [Email Designer](../email/get-started-email-design.md) or the personalization editor opens, depending on the type of fragment you are creating.

    * For visual fragments, edit your content as needed, the same way you would do for any email inside a journey or a campaign.

        >[!NOTE]
        >
        >You can add personalization fields and dynamic content, but contextual attributes are not supported in fragments.

        ![](assets/fragment-designer.png)

    * For expression fragments, leverage the [!DNL Journey Optimizer] personalization editor with all its personalization and authoring capabilities to build your fragment content. [Learn more](../personalization/personalization-build-expressions.md)

        ![](assets/fragment-expression-editor.png)

1. Once your fragment is ready, click **[!UICONTROL Save]**.

The fragment is added to the [fragment list](#access-manage-fragments). It is now ready to be used when building any content within the [!DNL Journey Optimizer] Email Designer or personalization editor. 

* [Learn how to use visual fragments](../email/use-visual-fragments.md)
* [Learn how to use expression fragments](../personalization/use-expression-fragments.md)
