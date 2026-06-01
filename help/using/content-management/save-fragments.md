---
solution: Journey Optimizer
product: journey optimizer
title: Save content as fragment
description: Learn how to save content as fragments to reuse content in Journey Optimizer campaigns and journeys
feature: Fragments
topic: Content Management
role: User
level: Beginner, Intermediate
exl-id: 70e88ea0-f2b0-4c13-8693-619741762429
TQID: https://experienceleague.adobe.com/hhnYseI-u0dIoI-pwrkE4UcBAi27g1J9TwaldimPyx0
product_v2:
  - id: cb954087-f4fc-4456-afb9-e939cabcdc79
    internal-label: Journey Optimizer
feature_v2:
  - id: dc22c819-3f29-4e91-8b7d-5c6719831141
    internal-label: Content management
  - id: fe338112-e2ce-4876-8989-fc4d497613f1
    internal-label: Email
subfeature_v2:
  - id: c6e980f5-2d4f-494f-beef-186b9ecf1513
    internal-label: Fragments
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
  - id: e8ccd51f-da0d-4e3b-939b-e30d5ebb1ea5
    internal-label: Beginner
topic_v2:
  - id: e0eb8757-182f-49f3-94a4-1587d16f5094
    internal-label: Personalization
---
# Save content as fragment {#save-as-fragment}
 
When editing content in [!DNL Journey Optimizer], you can save all or part of your content as fragment for future reuse. You can save content as fragment either [from the Email Designer](#save-as-visual-fragment), or [from the expression editor](#save-as-expression-fragment).

>[!NOTE]
>
>[Contextual attributes](../personalization/personalization-build-expressions.md) are not supported in fragments.
>
>When tracking is enabled in a journey or a campaign, if links are present in a saved fragment and if this fragment is used in a message, these links are tracked such as all other links included in the message. [Learn more on links and tracking](../email/message-tracking.md)

## Save as visual fragment {#save-as-visual-fragment}

To save content from the Email Designer as fragment, follow these steps:

1. In the [Email Designer](../email/get-started-email-design.md), click the ellipsis on top right of the screen.

1. Select **[!UICONTROL Save as fragment]** from the drop-down menu.

    ![](assets/fragment-save-as.png)

    >[!NOTE]
    >
    >Visual fragments cannot exceed 100KB.

1. The **[!UICONTROL Save as fragment]** screen displays. There select the elements you want to include into your fragment, including personalization fields and dynamic content.

    ![](assets/fragment-save-as-screen.png)

    >[!CAUTION]
    >
    >You can only select sections that are adjacent to each other. You cannot select an empty structure or another fragment.

1. Click **[!UICONTROL Create]** and fill in the fragment name and description (if needed).

1. To assign custom or core data usage labels to the fragment, click the **[!UICONTROL Manage access]** button in the upper section of the screen. [Learn more about Object Level Access Control (OLAC)](../administration/object-based-access.md).

1. Select or create Adobe Experience Platform tags from the **Tags** field to categorize your template for improved search. [Learn more](../start/search-filter-categorize.md#tags)

1. Click **[!UICONTROL Create]**. The fragment is added to the [fragment list](#access-manage-fragments) with the **Draft** status. It becomes a standalone fragment that can be used as any other visual fragment from that list. 

    >[!NOTE]
    >
    >Any change to that new fragment is not propagated to the email or template it comes from. Similarly, when the original content is edited within that email or template, the new fragment is not modified.

1. In order to be able to use the fragment in your journeys and campaigns, you need to make it live. [Learn how to preview and publish a fragment](../content-management/create-fragments.md#publish)

## Save as expression fragment {#save-as-expression-fragment}

>[!CONTEXTUALHELP]
>id="ajo_perso_library"
>title="Save as expression fragment"
>abstract="The [!DNL Journey Optimizer] personalization editor allows you to save content as expression fragments. These expressions are then available to build personalized content."

The [!DNL Journey Optimizer] personalization editor allows you to save content as expression fragments. These expressions are then available to build personalized content.

To save content as an expression fragment, follow the steps below.

1. In the [personalization editor](../personalization/personalization-build-expressions.md) interface, build an expression, then click **[!UICONTROL Save as fragment]**. 

    >[!NOTE]
    >
    >Expressions cannot exceed 200KB.

1. In the right pane, enter a name and a description for the expression to help users find it more easily.

    ![](assets/expression-fragment-save-as.png)

1. Click **[!UICONTROL Save fragment]**.

    <!--An expression fragment cannot be nested inside another fragment.-->

1. The fragment is added to the [fragment list](#access-manage-fragments) with the **Draft** status. It becomes a standalone fragment that can be used as any other expression fragment from that list. 

1. In order to be able to use the fragment in your journeys and campaigns, you need to make it live. [Learn how to preview and publish a fragment](../content-management/create-fragments.md#publish)
