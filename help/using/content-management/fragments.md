---
solution: Journey Optimizer
product: journey optimizer
title: Get started with fragments
description: Learn how to work with content fragments to reuse content in Journey Optimizer campaigns and journeys
feature: Fragments
topic: Content Management
role: User
level: Beginner, Intermediate
exl-id: 7131a953-baca-4e7c-a8df-97c0bd6ac567
TQID: https://experienceleague.adobe.com/2XVXr3MjYnD-7o0C2ARXQ8j3sJOFfJfvjfCEZdkV50I
product_v2:
  - id: cb954087-f4fc-4456-afb9-e939cabcdc79
    internal-label: Journey Optimizer
feature_v2:
  - id: a653cc2e-bc85-4353-a306-399e5b247978
    internal-label: Journey Optimizer campaigns
  - id: d998adac-2f81-400b-a669-d07bb196e4eb
    internal-label: Journeys
  - id: dc22c819-3f29-4e91-8b7d-5c6719831141
    internal-label: Content management
  - id: fe338112-e2ce-4876-8989-fc4d497613f1
    internal-label: Email
subfeature_v2:
  - id: c6e980f5-2d4f-494f-beef-186b9ecf1513
    internal-label: Fragments
  - id: d595a60b-bcf5-4a63-a189-66a0be755cc7
    internal-label: Templates
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
# Get started with fragments {#fragments}
 
>[!CONTEXTUALHELP] 
>id="ajo_create_fragment"
>title="Define your own fragments"
>abstract="Create and manage standalone fragments to make your content reusable across multiple journeys and campaigns."
>additional-url="https://experienceleague.adobe.com/en/docs/journey-optimizer/using/content-management/fragments/create-fragments" text="Create fragments"

A fragment is a reusable component that can be referenced in one or more emails across [!DNL Journey Optimizer] campaigns and journeys. This functionality allows you to prebuild multiple custom content blocks that can be used by marketing users to quickly assemble email contents in an improved design process.

![](../rn/assets/do-not-localize/fragments.gif)

➡️ [Learn how to manage, author and use fragments in these videos](#video-fragments)

To make the best use of fragments:

* **Create your own fragments**: Create visual or expression fragments, either from scratch or by saving content as fragment. [Learn how to create a fragment](create-fragments.md). In addition, you can leverage Journey Optimizer **Content REST API** to manage content fragments. For more on this, refer to the [Journey Optimizer APIs documentation](https://developer.adobe.com/journey-optimizer-apis/references/content){target="_blank"}.
* **Reuse your fragments:** Use them as many times as needed in your content. See [Add visual fragments](../email/use-visual-fragments.md) and [Leverage expression fragments](../personalization/use-expression-fragments.md)

## Before starting {#fragment-prerequisites}

To create, edit, archive, and publish fragments you need the **[!DNL Manage library items]** and **[Publish Fragment]** permissions included in the **[!DNL Content Library Manager]** product profile. [Learn more](../administration/ootb-product-profiles.md#content-library-manager)

In this version, the following limitations apply:

* **Visual fragments** are available for the Email channel only.
* **Expression fragments** are not available for the In-app channel.

More guardrails applying to fragments are available in [this section](../start/guardrails.md#fragments-guardrails).

## Visual & expression fragments {#visual-expression}

Two types of fragments are available:

* **Visual fragments** are pre-defined visual blocks that you can reuse across multiple email deliveries using the [Email Designer](../email/get-started-email-design.md), or in [content templates](../email/use-email-templates.md).
* **Expression fragments** are pre-defined expressions that are available from a dedicated entry in the [personalization editor](../personalization/personalization-build-expressions.md).

All created fragments are accessible from the **[!UICONTROL Content Management]** > **[!UICONTROL Fragments]**  left menu. [Learn how to manage fragments](../content-management/manage-fragments.md)

![](assets/fragment-list.png)

## How-to video {#video-fragments}

Learn how to manage, author, and use **visual fragments** in [!DNL Journey Optimizer].

>[!VIDEO](https://video.tv.adobe.com/v/3419932/?quality=12)

Learn how to manage, author, and use **expression fragments** in [!DNL Journey Optimizer].

>[!VIDEO](https://video.tv.adobe.com/v/3424587/?quality=12)
