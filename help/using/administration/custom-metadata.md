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
hidefromtoc: true
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

Custom metadata lets you create your own business fields and display them in the properties of your journeys, Action campaigns and Orchestrated campaigns. Use them to track information that goes beyond what [tags](../start/search-filter-categorize.md#tags) and descriptions can capture, for example:

* Line of business or promotional region
* Product line
* Cost center
* Workfront project ID

The values you enter are recorded in the entity datasets. You can use them for downstream reporting, to export data, or to build audiences from the profiles who received a given journey or campaign.

## How custom metadata works {#how-it-works}

Custom metadata fields are defined in [!DNL Adobe Experience Platform] [schemas](../data/get-started-schemas.md). [!DNL Journey Optimizer] automatically provisions one record-based schema for each type of entity. These schemas use the **AJO Entity Class**:

* **AJO Campaign Custom Metadata Schema**
* **AJO Journey Custom Metadata Schema**
* **AJO Orchestrated Campaign Custom Metadata Schema**

## Define your custom metadata fields {#define-fields}

To define custom metadata fields, add them to a custom field group in the schema of the entity type where you want to use them. You can reuse the same field group in the schemas of other entity types.

1. In [!DNL Adobe Experience Platform], browse to **[!UICONTROL Schemas]** and from the **[!UICONTROL Browse]** tab, open one of the custom metadata schemas, for example **[!UICONTROL AJO Campaign Custom Metadata Schema]**.

    ![Custom metadata schemas in the Schemas browse tab](assets/metadata-campaign-schema.jpg)

    >[!NOTE]
    >
    >Do not edit the name of these schemas.

1. Click **[!UICONTROL Add]** and select **[!UICONTROL Create new field group]**. Select a display name, for example **AJO Custom Metadata**. [Learn how to add field groups and fields to a schema](https://experienceleague.adobe.com/en/docs/experience-platform/xdm/tutorials/create-schema-ui){target="_blank"}

    ![Add button for field groups in the campaign custom metadata schema](assets/metadata-schema-add-field-group.jpg){width="60%"}

1. Back in the **[!UICONTROL AJO Campaign Custom Metadata Schema]** structure, select the field group you created and click the plus icon next to the name of the schema to add a new field.

    ![Custom field group selected in the campaign custom metadata schema](assets/metadata-schema-add-field.jpg)

    >[!NOTE]
    >
    >You can also select the field group you want to assign the field to from the **[!UICONTROL Field Group]** dropdown at any time while defining the field.

1. For each field, define a name, a display name and, optionally, a description.

1. Define the field type. It must be **[!UICONTROL String]**.

1. To provide a list of values, define the field as an enum and add each value with its display name.

1. Make sure to follow these guidelines:

    * Do not define default values or patterns.
    * Do not mark fields as required in the schema. You can make fields required when you [select the fields to display](#select-fields) in the properties of your campaigns or journeys.

1. Click **[!UICONTROL Apply]** to save the new field.

1. Repeat these steps to add as many fields as needed.

1. Optionally, to use the same fields for other entity types, open the corresponding custom metadata schemas and add the same field group to them.

>[!NOTE]
>
>Field names must be unique in a sandbox. If a field with the same name already exists elsewhere in the sandbox, you might not be able to add it to your schema.

## Select the fields to display {#select-fields}

Once your fields are defined in the schemas, choose which ones appear in the properties of your journeys and campaigns.

1. In the left navigation, browse to **[!UICONTROL Administration]** > **[!UICONTROL Configurations]**, then click **[!UICONTROL Manage]** in the **[!UICONTROL Metadata]** card.

    ![Metadata card in the Configurations dashboard](assets/metadata-panel.jpg)

    The panel contains one tab per entity type: **[!UICONTROL Journeys]**, **[!UICONTROL Campaigns]** and **[!UICONTROL Orchestrated campaigns]**.

1. In each tab, select the fields to display. The list is synchronized with the corresponding schema: when you add or change fields or lists of values in the schema, the changes are reflected in the field picker.

    >[!NOTE]
    >
    >It can take up to 5 minutes for schema changes to be displayed in the field picker.

1. Order the selected fields. The fields are displayed in this order in the properties of your journeys and campaigns, so place the most important ones first.

1. Optionally, mark fields as **required**. Required fields are displayed with an asterisk. They are validated in the user interface and not in the schema, to avoid issues when data is inserted. <!-- TODO DOCAC-16114: confirm that required fields block activation/publication; not blocking in the LA demo -->

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
