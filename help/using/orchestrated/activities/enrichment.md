---
solution: Journey Optimizer
product: journey optimizer
title: Use the Enrichment activity
description: Learn how to use the Enrichment activity
exl-id: 8a0aeae8-f4f2-4f1d-9b89-28ce573fadfd
version: Campaign Orchestration
TQID: https://experienceleague.adobe.com/Q7lT1NR61ALn475i9akX7z80pybh93kbx06Gc8TcCuI
product_v2:
  - id: cb954087-f4fc-4456-afb9-e939cabcdc79
    internal-label: Journey Optimizer
feature_v2:
  - id: b3538224-471e-4c63-a444-9b19d89ae29c
    internal-label: Activities
  - id: d556b755-390a-43f0-be32-a08cf6236126
    internal-label: Configuration
---
# Enrichment {#enrichment}

>[!CONTEXTUALHELP]
>id="ajo_orchestration_enrichment"
>title="Enrichment activity"
>abstract="The **Enrichment** activity allows you to enhance the targeted data with additional information from the database. It is commonly used in a campaign after segmentation activities."

The **[!UICONTROL Enrichment]** activity is a **[!UICONTROL Targeting]** activity that lets you enhance your audience data with additional attributes.

You can leverage this information to segment your audience more precisely, based on behaviors, preferences, or needs, and to craft personalized messages that better connect with each profile.

## Add an Enrichment activity {#enrichment-configuration}

>[!CONTEXTUALHELP]
>id="ajo_targetdata_personalization_enrichmentdata"
>title="Enrichment data"
>abstract="Select the data to use to enrich your Orchestrated campaign. You can select two types of enrichment data: a single enrichment attribute from the target dimension, or a collection link, which is a link with a 1-N cardinality between tables."

>[!CONTEXTUALHELP]
>id="ajo_orchestration_enrichment_data"
>title="Enrichment activity"
>abstract="Once enrichment data has been added to the Orchestrated campaign, it can be used in the activities added after the Enrichment activity to segment customers into distinct groups based on their behaviors, preferences, and needs, or to create personalized marketing messages and campaigns that are more likely to resonate with your target audience."

Follow these steps to configure the **Enrichment** activity:

1. Add an **Enrichment** activity.

1. Click **Add enrichment data** and select the attribute to use to enrich the data.

    You can select two types of enrichment data: a single enrichment attribute from the target dimension, or a collection link. Each of these types is detailed in the examples below:
    
    * [Single enrichment attribute](#single-attribute)
    * [Collection link](#collection-link)

    ![](../assets/enrichment-1.png)
 
1. Click **[!UICONTROL Add link]** to create a link between the working table data and Adobe Journey Optimizer. [Learn more](#create-links)

    For example, if you load data from a file containing customer loyalty tier and last purchase date, you need to create a link to the profiles table to enrich recipient records with these attributes and use them for personalization or targeting.

    ![](../assets/enrichment-1.png)

## Create links between tables {#create-links}

>[!CONTEXTUALHELP]
>id="ajo_orchestration_enrichment_simplejoin"
>title="Link definition"
>abstract="Create a link between the working table data and Adobe Journey Optimizer. For example, if you load data from a file which contains the account number, country and email of recipients, you have to create a link towards the country table in order to update this information in their profiles."

Use the **[!UICONTROL Link definition]** section to define a relationship between the working table and another data source. For example, if you import a file containing customer loyalty tier and last purchase date, you can create a link to the profiles table to make those attributes available for personalization and targeting.

To create a link:

1. In the **[!UICONTROL Link definition]** section, click **[!UICONTROL Add link]**.

    ![](../assets/enrichment-1.png)

1. From the **[!UICONTROL Relation type]** drop-down, select the type of relationship between the primary set and the linked data:

    * **[!UICONTROL 1 cardinality simple link]**: Each record in the primary set maps to exactly one record in the linked data.
    * **[!UICONTROL 0 or 1 cardinality simple link]**: Each record in the primary set maps to zero or one record in the linked data.
    * **[!UICONTROL N cardinality collection link]**: Each record in the primary set can map to multiple records in the linked data.

    ![](../assets/enrichment-8.png)

1. Select the target to link the primary set to:

    * **[!UICONTROL Database schema]**: Link to an existing table in the database. Select the table from the **[!UICONTROL Target schema]** field.
    * **[!UICONTROL Temporary schema]**: Link to data arriving from an input transition. Select the relevant transition from the list.

1. Define the join conditions used to match records between the primary set and the linked schema:

    * **[!UICONTROL Simple join]**: Match records on a specific attribute pair. Click **[!UICONTROL Add join]**, then select the **[!UICONTROL Source]** and **[!UICONTROL Destination]** attributes to use as matching criteria.
    * **[!UICONTROL Advanced join]**: Build custom matching logic using the rule builder. Click **[!UICONTROL Create condition]** to get started.

## Examples {#example}

### Single enrichment attribute {#single-attribute}

In this example, you enrich the audience with a single attribute, such as the date of birth, from the current targeting dimension.

To do this:

1. Click **[!UICONTROL Add enrichment data]**.

1. Select a simple field, such as **[!UICONTROL Date of birth]**, from the current dimension.

    ![](../assets/enrichment-2.png)

1. Click **[!UICONTROL Confirm]**.

### Collection link {#collection-link}

This use case enriches your audience with data from a linked table. For example, you want to retrieve the three most recent purchases under $100.

To achieve this, configure the enrichment as follows:

* **Enrichment attribute**: **[!UICONTROL Price]**

* **Number of records to retrieve**: 3

* **Filter**: Only include purchases where the **[!UICONTROL Price]** is less than $100

#### Add the attribute {#add-attribute}

First, select the collection link that contains the data you want to enrich with.

1. Click **[!UICONTROL Add enrichment data]**.

1. From the **[!UICONTROL Purchases]** table, select the **[!UICONTROL Price]** field.

    ![](../assets/enrichment-2.png)

#### Define the collection settings{#collection-settings}

Next, configure how the data should be collected and how many entries to include.

1. In the **[!UICONTROL Select how the data is collected]** dropdown, choose **[!UICONTROL Collect data]**.

    ![](../assets/enrichment-4.png)

1. In the **[!UICONTROL Lines to retrieve (Columns to create)]** field, enter `3`. 

1. To perform an aggregation (e.g., average purchase amount), select **[!UICONTROL Aggregated data]**, then choose **[!UICONTROL Average]** from the **[!UICONTROL Aggregate function]** dropdown.

    ![](../assets/enrichment-5.png)

1. Use the **[!UICONTROL Label]** and **[!UICONTROL Alias]** fields to make the enriched attributes easier to identify in subsequent activities.

#### Define the filters{#collection-filters}

Finally, apply filters to ensure only relevant records are included:

1. Click **[!UICONTROL Create filters]**.

1. Add these two conditions:

    * **[!UICONTROL Price]** exists (to exclude NULLs)

    * **[!UICONTROL Price]** is less than 100
    
    ![](../assets/enrichment-6.png)

1. Click **[!UICONTROL Confirm]**.


<!--
#### Define the sorting{#collection-sorting}

We now need to apply sorting in order to retrieve the three **latest** purchases.

1. Activate the **Enable sorting** option.
1. Click inside the **Attribute** field.
1. Select the **Order date** field.
1. Click **Confirm**. 
1. Select **Descending** from the **Sort** drop-down.

![](../assets/workflow-enrichment7bis.png)


## Data reconciliation {#reconciliation}

>[!CONTEXTUALHELP]
>id="ajo_orchestration_enrichment_reconciliation"
>title="Reconciliation"
>abstract="The **Enrichment** activity can be used to reconcile data from the Journey Optimizer schema with data from another schema, or with data coming from a temporary schema such as data uploaded using a Load file activity. This type of link defines a reconciliation towards a unique record. Journey Optimizer creates a link to a target table by adding a foreign key in it for storing a reference to the unique record."

The **Enrichment** activity can be used to reconcile data from the the Campaign database schema with data from another schema, or with data coming from a temporary schema such as data uploaded using a Load file activity. This type of link defines a reconciliation towards a unique record. Journey Optimizer creates a link to a target table by adding a foreign key in it for storing a reference to the unique record.

For example, you can use this option to reconcile a profile's country, specified in an uploaded file, with one of the countries available in the dedicated table of the Campaign database. 

Follow the steps to configure an **Enrichment** activity with a reconciliation link: 

1. Click the **Add link** button in the **Reconciliation** section.
1. Identify the data you want to create a reconciliation link with.

    * To create a reconciliation link with data from the Campaign database, select **Database schema** and choose the schema where the target is stored. 
    * To create a reconciliation link with data coming from the input transition, select **Temporary schema** and choose the Orchestrated campaign transition where the target data is stored. 

1. The **Label** and **Name** fields are automatically populated based on the selected target schema. You can change their values if necessary.

1. In the **Reconciliation criteria** section, specify how you want to reconcile data from the source and destination tables:

    * **Simple join**: Reconcile a specific field from the source table with another field in the destination table. To do this, click the **Add join** button and specify the **Source** and **Destination** fields to use for the reconciliation.

        >[!NOTE]
        >
        >You can use one or more **Simple join** criteria, in which case they must all be verified so that the data can be linked together.

    * **Advanced join**: Use the rule builder to configure the reconciliation criteria. To do this, click the **Create condition** button then define your reconciliation criteria by building your own rule using AND and OR operations.

The example below shows an Orchestrated campaign configured to create a link between Journey Optimizer profiles table and a temporary table generated a **Load file** activity. In this example, the **Enrichment** activity reconciliates both tables using the email address as reconciliation criteria.

![](../assets/enrichment-reconciliation.png)

### Enrichment with linked data {#link-example}

The example below shows an Orchestrated campaign configured to create a link between two transitions. The first transitions targets profile data using a **Query** activity, while the second transition includes purchase data stored into a file loaded through a Load file activity.

![](../assets/enrichment-uc-link.png)

* The first **Enrichment** activity links the primary set (data from the **Query** activity) with the schema from the **Load file** activity. This allows us to match each profile targeted by the query with the corresponding purchase data.

    ![](../assets/enrichment-uc-link-purchases.png)

* A second **Enrichment** activity is added in order to enrich data from the Orchestrated campaign table with the purchase data coming from the **Load file** activity. This allows us to use those data in further activities, for example, to personalize messages sent to the customers with information on their purchase.

    ![](../assets/enrichment-uc-link-data.png)

## Add offers {#add-offers}

>[!CONTEXTUALHELP]
>id="ajo_orchestration_enrichment_offer_proposition"
>title="Offer proposition"
>abstract="The Enrichment activity allows you to add offers for each profile."

The **[!UICONTROL Enrichment]** activity allows you to add offers for each profile.

To do so, follow the steps to configure an **[!UICONTROL Enrichment]** activity with an offer: 

1. In the **[!UICONTROL Enrichment]** activity, at the **[!UICONTROL Offer proposition]** section, click on the **[!UICONTROL Add offer]** button

    ![](../assets/enrichment-addoffer.png)

1. You have two choices for the offer selection :

    * **[!UICONTROL Search for the best offer in category]** : check this option and specify the offer engine call parameters (offer space, category or theme(s), contact date, number of offers to keep). The engine will calculate the best offer(s) to add according to these parameters. We recommend completing either the Category or the Theme field, rather than both at the same time.

        ![](../assets/enrichment-bestoffer.png)

    * **[!UICONTROL A predefined offer]** : check this option and specify an offer space, a specific offer, and a contact date to directly configure the offer that you would like to add, without calling the offer engine.

        ![](../assets/enrichment-predefinedoffer.png)

1. After selecting your offer, click on **[!UICONTROL Confirm]** button.

You can now use the offer in the delivery activity.



### Using the offers from Enrichment activity

Within an Orchestrated campaign, if you want to use the offers you get from an enrichment activity in your delivery, follow the steps below:

1. Open the delivery activity and go in the content edition. Click on **[!UICONTROL Offers settings]** button and select in the drop-down list the **[!UICONTROL Offers space]** corresponding to your offer. 
If you want to to view only offers from the enrichment activity, set the number of **[!UICONTROL Propositions]** to 0, and save the modifications.

    ![](../assets/offers-settings.png) 

1. In the Email Designer, when adding a personalization with offers, click on the **[!UICONTROL Propositions]** icon, it will display the offer(s) you get from the **[!UICONTROL Enrichment]** activity. Open the offer you want to choose by clicking on it.

    ![](../assets/offers-propositions.png) 

    Go in **[!UICONTROL Rendering functions]** and choose **[!UICONTROL HTML rendering]** or **[!UICONTROL Text rendering]** according to your needs.

    ![](../assets/offers-rendering.png) 

>[!NOTE]
>
>If you choose to have more than one offer in the **[!UICONTROL Enrichment]** activity at the **[!UICONTROL Number of offers to keep]** option, all the offers are displayed when clicking on the **[!UICONTROL Propositions]** icon.
-->