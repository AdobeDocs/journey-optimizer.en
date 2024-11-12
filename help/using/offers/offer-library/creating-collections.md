---
title: Create collections
description: Learn how to organize offers using collections
feature: Decision Management, Collections
topic: Integrations
role: User
level: Intermediate
exl-id: 0c8808e3-9148-4a33-9fd5-9218e02c2dfd
---
# Create collections {#create-collections}

>[!CONTEXTUALHELP]
>id="ajo_decisioning_decision_collection"
>title="About offer collections"
>abstract="With offer collections, you can organize your offers by regrouping them into categories of your choice."

>[!CONTEXTUALHELP]
>id="ajo_decisioning_collection_dynamic"
>title="Dynamic collection"
>abstract="Use collection qualifiers to dynamically qualify offers for a collection."

>[!CONTEXTUALHELP]
>id="ajo_decisioning_collection_static"
>title="Static collection"
>abstract="Manually select and group offers together using criteria such as status, collection qualifiers, date and channel."

>[!CONTEXTUALHELP]
>id="ajo_decisioning_collection_static_select"
>title="Static collection preview"
>abstract="Static collections are built by manually selecting individual offers to include in the collection. The collection can only be updated by manually adding more offers to it."

>[!CONTEXTUALHELP]
>id="ajo_decisioning_collection_dynamic_select"
>title="Dynamic collection preview"
>abstract="Dynamic collections collect offers based on collection qualifiers. These collections are updated automatically. For example, if a new offer is created with the "sports" collection qualifier, it will automatically be added to the corresponding collection."

Collections allows you to organize your offers by regrouping them into categories of your choice. You can, for example, create a "sport" collection that will contain sport-related offers only. 

➡️ [Discover this feature in video](#video)

The list of offer collections is accessible in the **[!UICONTROL Offers]** menu.   

![](../assets/collections_list.png)

You can create two types of collections: 

* **Dynamic collections** are collections of offers based on collection qualifiers (previously known as "tags"). These collections are updated automatically. For example, if a new offer is created with the selected collection qualifier, it will automatically be added to the collection.

* **Static collections** are collections built by manually selecting individual offers to include in the Collection. The collection can only be updated by manually adding more offers to it.

To create a collection, follow these steps:

1. Go to the **[!UICONTROL Collections]** tab, then click **[!UICONTROL Create collection]**.

1. Specify the name and type of collection to create.

    ![](../assets/collection_create.png)

1. To create a dynamic collection, use the left pane to select the collection qualifier of the offers to add to the collection, then click **[!UICONTROL Save]**. All the offers with the selected collection qualifier will be saved in the collection.

    For more on collection qualifiers creation, see [Create collection qualifiers](../offer-library/creating-tags.md).

    ![](../assets/dynamic_collection.png)

1. To create a static collection, use the left pane to filter the list of offers (status, collection qualifier, date, channel, content type), then select the offers to add to the collection.

    ![](../assets/static_collection.png)

    >[!NOTE]
    >
    >Static collections are not updated automatically. To add offers to a static collection, you need to edit it and add them manually.

1. To assign custom or core data usage labels to a static collection, select **[!UICONTROL Manage access]**. [Learn more on Object Level Access Control (OLAC)](../../administration/object-based-access.md)

    >[!NOTE]
    >
    >The use of OLAC is not available for dynamic collections. It has to be managed at the offer level. Consequently, it is possible that you don't see any offers in a dynamic collection if you don't have access to any of these offers.
    
1. Once the collection is created, it displays in the list. You can select it to edit or delete it.

    ![](../assets/collection_created.png)

## How-to video {#video}

>[!VIDEO](https://video.tv.adobe.com/v/329376?quality=12)


