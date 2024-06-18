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
 
To manage your fragments, access the fragment list from the **[!UICONTROL Content Management]** > **[!UICONTROL Fragments]** left menu.

All the fragments that were created on the current sandbox - either [from the **[!UICONTROL Fragments]** menu](#create-fragments), either using the [Save as fragment](#save-as-fragment) option - are displayed.

![](assets/fragment-list-filters.png)

You can filter fragments on their:

* Status (Draft or Live)
* Type (visual or expression)
* Creation or modification date
* State (archived or not)
* Tags

You can also choose to show all fragments, or only the items that the current user created or modified.

From the **[!UICONTROL More actions]** button next to each fragment, you can:

* Duplicate a fragment.
* Use the **[!UICONTROL Explore references]** option to see the journeys, campaigns or templates where it is used. [Learn more](#explore-references)
* Archive a fragment. [Learn more](#archive-fragments)
* Edit a fragment's tags [Learn how to work with Unified tags](../start/search-filter-categorize.md#tags).

![](assets/fragment-list-more-actions.png)

## Fragments' statuses

>[!CONTEXTUALHELP]
>id="ajo_fragment_statuses"
>title="New fragments statuses"
>abstract="Since **Draft** and **Live** statuses have been introduced with Journey Optimizer June release, all fragments created before this release have the "Draft" status, even if they are used in a journey or campaign. If you make any change to these fragments, you need to publish them to make them "Live" and propagate the changes to the associated campaigns and journeys. You also need to create a new journey/campaign version and publish it. Publishing requires a user permission."

>[!AVAILABILITY]
>
> Please note that fragments statuses are being rolled out gradually over the course of several days following Journey Optimizer June release. While some users will have immediate access, others may experience a delay before it becomes available in their environments. If this enhancement is not yet available in your environment, please note that fragment do not require to be **Live** to be used in your journeys and campaigns.

Fragments can have multiple statuses:

* **[!UICONTROL Draft]**: The fragment is being edited and has not been approved.

* **[!UICONTROL Live]**: The fragment has been approved and is live. [Learn how to publish a fragment](../content-management/create-fragments.md#publish)

    When a live fragment is being edited, a specific icon next to its status displays. Click this icon to open the draft version of the fragment.

* **[!UICONTROL Publishing]**: The fragment has been approved and is being published.
* **[!UICONTROL Archived]**: The fragment has been archived. [Learn how to archive fragments](#archive-fragments)

>[!CAUTION]
>
>Since **Draft** and **Live** statuses have been introduced with Journey Optimizer June release, all fragments created before this release have the "Draft" status, even if they are used in a journey or campaign. If you make any change to these fragments, you need to publish them to make them "Live" and propagate the changes to the associated campaigns and journeys. You also need to create a new journey/campaign version and publish it. Publishing requires a user permission.

## Edit fragments {#edit-fragments}

To edit a fragment, follow the steps below.

1. Click the desired fragment from the **[!UICONTROL Fragments]** list.

1. The fragment properties opens with a preview of its content.

1. If the fragment being edited has the **Live** status, click the **Modify** button to create a draft version of the fragment. The current version of the fragment will continue to be live, until you publish the draft version.

1. Make the desired changes to the fragment. To edit its content, click the **Edit** button then edit your content as you would do when creating a fragment from scratch. [Learn how to create a fragment](#create-from-scratch)

    >[!NOTE]
    >
    >When editing an expression fragment, you can remove any personalization field but cannot add new ones to the fragment content. If you want to add personalization fields, duplicate the fragment in order to create a new one.

    You can also check the list of the journeys, campaigns and content templates where the fragment is currently being used by selecting the **Explorer references** option. [Learn more](#explore-references)

    ![](assets/fragment-edit.png)

1. Once your changes are ready, click the **Publish** button to make your modifications live.

When you edit a fragment, the changes are automatically propagated to all contents using that fragment, including live journeys and campaigns, excepted for contents where you have broken inheritance from the original fragment. Learn how to break inheritance in the [Add visual fragments to your emails](../email/use-visual-fragments.md#break-inheritance) and [Leverage expression fragments](../personalization/use-expression-fragments.md#break-inheritance) sections.

>[!AVAILABILITY]
>
>Please note that propagation of fragments changes in live journeys and campaigns is being rolled out gradually over the course of several days following Journey Optimizer June release. While some users will have immediate access, others may experience a delay before it becomes available in their environments. If this enhancement is not yet available in your environment, your changes will not be propagated to content used in live journeys or campaigns.

## Explore references {#explore-references}

You can display the list of the journeys, campaigns and content templates that are currently using a fragment. To do so, select **[!UICONTROL Explore references]** either from the **[!UICONTROL More actions]** menu in the fragment list or from the fragment properties screen.

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
