---
solution: Journey Optimizer
product: journey optimizer
title: Add contextual attributes to published fragments
description: Learn how to add contextual attributes to published fragments (limited availability)
feature: Fragments
topic: Content Management
role: User
level: Intermediate, Experienced
hide: true
exl-id: a274656e-2570-4a9c-b72b-4e8e920b7462
TQID: https://experienceleague.adobe.com/yweu8QtcWU42ZI2z93vIf5-LUGP7pQ16bJUQnmDKNGY
product_v2:
  - id: cb954087-f4fc-4456-afb9-e939cabcdc79
    internal-label: Journey Optimizer
feature_v2:
  - id: ad78185d-8f79-40ad-9bad-cbde74af74ee
    internal-label: Guardrails and limitations
  - id: dc22c819-3f29-4e91-8b7d-5c6719831141
    internal-label: Content management
subfeature_v2:
  - id: c6e980f5-2d4f-494f-beef-186b9ecf1513
    internal-label: Fragments
  - id: fb9a80eb-bebc-492f-a0e9-584595621ebb
    internal-label: Publish
role_v2:
  - id: b69b2659-1057-424e-8fc5-ed9e016dc554
    internal-label: User
level_v2:
  - id: b5a62a22-46f7-4f0d-b151-3fc640bef588
    internal-label: Intermediate
topic_v2:
  - id: e0eb8757-182f-49f3-94a4-1587d16f5094
    internal-label: Personalization
---
# Add contextual attributes to published fragments {#adding-contextual-attributes}

>[!AVAILABILITY]
>
>This capability is only available for select customers and involves significant risks. Confirm with your Adobe representative that this capability is enabled for your organization.

By default, adding new [personalization attributes](../personalization/personalization-build-expressions.md) to a published fragment is not supported. Once a fragment is published, the set of profile or contextual attributes is locked for all campaigns and journeys.

However, for select customers, it is possible to add **contextual attributes** only to published fragments.

>[!WARNING]
>
>When adding personalization attributes to a published fragment, the validation process is less stringent and errors may not be detected. This could cause unintended breakages across journeys and campaigns using that fragment at scale.

## Guardrails and limitations {#limitations}

* Make sure all journeys and campaigns that currently use the fragment can handle the new contextual attributes.
* Profile attributes cannot be added to published fragments. Only contextual attributes are supported.
* Contextual attributes must be manually entered into the code editor—they cannot be selected from the personalization editor UI.
* When adding personalized attributes to live fragments, validations are relaxed, which means errors may not be detected and could cause unintended breakages at scale.
* Once published, any errors will immediately impact all communications using that fragment.

## Add contextual attributes {#add-contextual-attributes}

To add contextual attributes to a published fragment, follow the steps below.

>[!IMPORTANT]
>
>Only proceed if you fully [understand the impacts](#limitations) on journeys and campaigns referencing the fragment.

1. Navigate to **[!UICONTROL Content Management]** > **[!UICONTROL Fragments]**.

1. Select the published fragment and click **[!UICONTROL Modify]** to create a draft version.

    ![](assets/fragment-live-modify.png){width="70%" align="left"}

1. Click **[!UICONTROL Edit]** to open the fragment content editor.

1. Switch to **[!UICONTROL Code editor]** or **[!UICONTROL Advanced mode]** in the personalization editor.

1. Manually type or copy-paste the contextual attribute using the `{{context.attribute_name}}` syntax:

    Example for a `promotionCode` attribute:

    ```
    {{context.promotionCode}}
    ```

    >[!CAUTION]
    >
    >Double-check the attribute path for accuracy. Errors may not be detected and could disrupt journey or campaign communications at scale.

1. Save your changes.

1. Once confirmed, click **[!UICONTROL Publish]** to make your changes live.

>[!NOTE]
>To avoid unintended breakages across journeys and campaigns, you can test the contextual attribute paths in a non-production environment.

## Related topics {#related-topics}

* [Manage fragments](manage-fragments.md)
* [Edit a fragment](manage-fragments.md#edit-fragments)
* [API-triggered campaigns](../campaigns/api-triggered-campaigns.md)
* [Personalization syntax](../personalization/personalization-syntax.md)
