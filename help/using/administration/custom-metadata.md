---
solution: Journey Optimizer
product: journey optimizer
title: Custom metadata for journeys and campaigns
description: Learn how to define custom metadata fields to track business information on your journeys, campaigns and Orchestrated campaigns.
feature: Administration
topic: Content Management
role: Admin
level: Intermediate
hide: true
badge: label="Limited availability" type="Informative"
keywords: custom metadata, journey, campaign, orchestrated campaign, schema, reporting
---
# Custom metadata for journeys and campaigns {#custom-metadata}

>[!BEGINSHADEBOX]

**On this page:** Learn how to define custom metadata fields for your journeys, Action campaigns and Orchestrated campaigns, so you can track business information such as line of business, product or cost center, and use it for reporting and audience creation.

>[!ENDSHADEBOX]

>[!AVAILABILITY]
>
>This capability is available in Limited Availability. Contact your Adobe representative to gain access.

Custom metadata lets you create your own business fields and display them in the properties of your journeys, Action campaigns and Orchestrated campaigns. Use them to track information that goes beyond what tags and descriptions can capture, for example:

* Line of business or promotional region
* Product line
* Cost center
* Workfront project ID

The values you enter are recorded in the entity datasets. You can use them for downstream reporting, to export data, or to build audiences from the profiles who received a given journey or campaign.

## How custom metadata works {#how-it-works}

Custom metadata fields are defined in [!DNL Adobe Experience Platform] schemas. [!DNL Journey Optimizer] automatically provisions one schema for each type of entity. These schemas are based on the **AJO Entity** class:

* **AJO Campaign Custom Metadata Schema**
* **AJO Journey Custom Metadata Schema**
* **AJO Orchestration Campaign Custom Metadata Schema**

To add a custom field, browse to **[!UICONTROL Schemas]** in [!DNL Adobe Experience Platform] and edit the schema that matches the entity type. Fields that have a list of values are displayed as a drop-down list when users fill in the metadata.

## Select the fields to display {#select-fields}

Once your schemas are defined, choose which fields appear in the properties of your journeys and campaigns. <!-- TODO DOCAC-16114: confirm the exact name and location of the metadata panel with PM -->

1. Open the metadata panel. It contains one tab per entity type: **[!UICONTROL Journeys]**, **[!UICONTROL Campaigns]** and **[!UICONTROL Orchestrated campaigns]**.

1. In each tab, select the fields to display. The list is synchronized with the corresponding schema: when you add or change fields or lists of values in the schema, the changes are reflected in the field picker.

    >[!NOTE]
    >
    >It can take up to 5 minutes for schema changes to be displayed in the field picker.

1. Order the selected fields. The fields are displayed in this order in the properties of your journeys and campaigns, so place the most important ones first.

1. Optionally, mark fields as **required**. Required fields are displayed with an asterisk and are validated in the user interface, not in the schema. <!-- TODO DOCAC-16114: confirm that required fields block activation/publication; not blocking in the LA demo -->

1. Confirm your selection.

The configuration is independent for each entity type: you can select different fields, in a different order, for journeys, campaigns and Orchestrated campaigns.

>[!CAUTION]
>
>You can select up to **10 fields** per entity type. If your schema contains more fields, select the 10 you want to display.

## Fill in metadata values {#fill-values}

Once fields are configured, they appear in the properties of each entity:

* **Action campaigns**: in the **[!UICONTROL Properties]** tab when you create or edit the campaign. [Learn more](../campaigns/campaign-properties.md)
* **Journeys**: in the journey properties. [Learn more](../building-journeys/journey-properties.md#custom-metadata)
* **Orchestrated campaigns**: in the campaign properties. [Learn more](../orchestrated/create-orchestrated-campaign.md#create)

Enter or select a value for each field, then save and activate your journey or campaign as usual. Fields marked with an asterisk are required.

## Use custom metadata for reporting {#reporting}

When a journey or campaign is activated, its metadata values are sent to a custom metadata dataset. <!-- TODO DOCAC-16114: confirm dataset name(s) with PM/engineering -->

You can use this dataset to:

* Export the data for downstream reporting.
* Build audiences based on the metadata of the journeys and campaigns that profiles received.

## Related topics {#related}

* [Organize journeys with tags](../building-journeys/tags.md)
* [Search, filter and categorize](../start/search-filter-categorize.md)
