---
solution: Journey Optimizer
product: journey optimizer
title: Manage fragments
description: Learn how to manage your content fragments
feature: Fragments
topic: Content Management
role: User
level: Beginner, Intermediate
exl-id: 1fc708e1-a993-4a2a-809c-c5dc08a4bae1
---
# Manage fragments {#manage-fragments}

>[!CONTEXTUALHELP]
>id="ajo_fragment_statuses"
>title="New fragments statuses"
>abstract="Since **Draft** and **Live** statuses have been introduced with Journey Optimizer June release, all fragments created before this release have the "Draft" status, even if they are used in a journey or campaign. If you make any change to these fragments, you need to publish them to make them "Live" and propagate the changes to the associated campaigns and journeys. You also need to create a new journey/campaign version and publish it."

To manage your fragments, access the fragment list from the **[!UICONTROL Content Management]** > **[!UICONTROL Fragments]** left menu.

![](assets/fragment-list.png)

All the fragments that were created on the current sandbox - either [from the **[!UICONTROL Fragments]** menu](#create-fragments), either using the [Save as fragment](#save-as-fragment) option - are displayed.

You can filter fragments on their:

* Type: **[!UICONTROL Visual]** or **[!UICONTROL Expression]**
* Tags
* Creation or modification date

You can choose to show all fragments, or only the items that the current user created or modified.

You can also display the **[!UICONTROL Archived]** fragments. [Learn more](#archive-fragments)

![](assets/fragment-list-filters.png)

From the **[!UICONTROL More actions]** button next to each fragment, you can:

* Duplicate a fragment.

* Use the **[!UICONTROL Explore references]** option to see the journeys, campaigns or templates where it is used. [Learn more](#explore-references)

* Archive a fragment. [Learn more](#archive-fragments)

* Edit a fragment's [tags](../start/search-filter-categorize.md#tags).

![](assets/fragment-list-more-actions.png)

## Edit fragments {#edit-fragments}

To edit a fragment, follow the steps below.

1. Click the desired item from the **[!UICONTROL Fragments]** list.
1. From the fragment properties, you can [explore references](#explore-references), [manage its access](../administration/object-based-access.md), and update the fragment details including [tags](../start/search-filter-categorize.md#tags).

    ![](../email/assets/fragment-edit-content.png)

1. Select the corresponding button to edit content as you would do when creating a fragment from scratch. [Learn more](#create-from-scratch)

>[!NOTE]
>
>When you edit a fragment, the changes are automatically propagated to all contents using that fragment, except content used in **[!UICONTROL Live]** journeys or campaigns. You can also break inheritance from the original fragment. Learn more in the [Add visual fragments to your emails](../email/use-visual-fragments.md#break-inheritance) and [Leverage expression fragments](../personalization/use-expression-fragments.md#break-inheritance) sections.

## Explore references {#explore-references}

You can display the list of the journeys, campaigns and content templates that are currently using a fragment. 

To do so, select **[!UICONTROL Explore references]** either from the **[!UICONTROL More actions]** menu in the fragment list or from the fragment properties screen.

![](assets/fragment-explore-references.png)

Select a tab to toggle between journeys, campaigns, templates and fragments. You can see their status and click a name to be redirected to the corresponding item where the fragment is referenced.

![](assets/fragment-usage-screen.png)

>[!NOTE]
>
>If the fragment is used in a journey, campaign or template that has a label preventing you from accessing it, you will see an alert message on top of the selected tab. [Learn more on Object Level Access Control (OLAC)](../administration/object-based-access.md)

## Archive fragments {#archive-fragments}

You can clean the fragment list from the items that are no longer relevant to your brand.

To do so, click the **[!UICONTROL More actions]** button next to the desired fragment and select **[!UICONTROL Archive]**. It will disappear from the fragment list, which prevents users from using it in future emails or templates.

![](assets/fragment-list-archive.png)

>[!NOTE]
>
>If you archive a fragment that is used in a content, <!--it will remain in the email or template, but you won't be able to select it from the fragment list to edit it-->that content will not be affected.

To unarchive a fragment, filter on the **[!UICONTROL Archived]** items and select **[!UICONTROL Unarchive]** from the **[!UICONTROL More actions]** menu. It is now again accessible from the fragment list, and can be used in any email or template.

![](assets/fragment-list-unarchive.png)
