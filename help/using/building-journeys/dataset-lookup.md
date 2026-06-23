---
solution: Journey Optimizer
product: journey optimizer
title: Use [!DNL Adobe Experience Platform] data in journeys
description: Learn how to use the Dataset Lookup Activity in [!DNL Adobe Journey Optimizer] to enrich customer journeys with external data from [!DNL Adobe Experience Platform].
feature: Journeys, Activities
topic: Content Management
role: User
level: Intermediate
version: Journey Orchestration
badge: label="Limited Availability" type="Informative"
exl-id: b6f54a79-b9e7-4b3a-9a6f-72d5282c01d3
TQID: https://experienceleague.adobe.com/4sQ3A15j47fQ6hI1G9oS6T6ne9nbxIaeqc-95zSUIq4
product_v2:
  - id: cb954087-f4fc-4456-afb9-e939cabcdc79
    internal-label: Journey Optimizer
feature_v2:
  - id: b3538224-471e-4c63-a444-9b19d89ae29c
    internal-label: Activities
  - id: d998adac-2f81-400b-a669-d07bb196e4eb
    internal-label: Journeys
subfeature_v2: []
role_v2:
  - id: b69b2659-1057-424e-8fc5-ed9e016dc554
    internal-label: User
level_v2:
  - id: b5a62a22-46f7-4f0d-b151-3fc640bef588
    internal-label: Intermediate
topic_v2:
  - id: a004cc84-67b9-4a33-a3a7-8ec7273ef4dc
    internal-label: Metadata
  - id: bce87dde-a4ab-44c9-8a18-ad66e4ddb377
    internal-label: Customer experience
  - id: d00e9f03-e50b-4162-b143-0c0817c937c2
    internal-label: Customer journeys
  - id: e0eb8757-182f-49f3-94a4-1587d16f5094
    internal-label: Personalization
---
# Use [!DNL Adobe Experience Platform] data in journeys {#datalookup}

>[!BEGINSHADEBOX]

**On this page:** Learn how to use the Dataset lookup activity to dynamically retrieve data from Adobe Experience Platform record datasets at runtime and enrich your journeys with external data for personalization and decision-making.

>[!ENDSHADEBOX]

>[!CONTEXTUALHELP]
>id="ajo_journey_dataset_lookup"
>title="Dataset lookup activity"
>abstract="The **[!UICONTROL Dataset lookup]** activity allows you to dynamically retrieve data from [!DNL Adobe Experience Platform] record datasets during runtime. By leveraging this capability, you can access data that may not reside in the profile or event payload, ensuring your customer interactions are both relevant and timely."

The **[!UICONTROL Dataset lookup]** activity allows you to dynamically retrieve data from [!DNL Adobe Experience Platform] record datasets during runtime. By leveraging this capability, you can access data that may not reside in the profile or event payload, ensuring your customer interactions are both relevant and timely.

>[!AVAILABILITY]
>
>This feature is currently available to all customers as a limited availability release.

Key Benefits:

* **Real-Time personalization**: Tailor customer experiences using enriched data.
* **Dynamic decision-making**: Use external data to drive journey logic and actions.
* **Enhanced data Access**: Retrieve product metadata, pricing tables, or relational data tied to specific keys.

## Must-read {#must-read}

Review these requirements before you configure dataset lookups.

### Dataset enablement

The dataset must be enabled for lookup in [!DNL Adobe Experience Platform]. Detailed information is available in this section: [Use [!DNL Adobe Experience Platform] data](../data/lookup-aep-data.md).

### Limits & restrictions

* Maximum of 10 Dataset Lookup activities per journey.
* Maximum of 20 selected fields.
* Maximum of 50 keys in the lookup keys array.
* Enriched data size is limited to 10KB.

### Additional performance considerations 

The below recommendations are guidance to avoid delays in deliverability:

| Consideration | Recommended limit | Description |
| ------- | ------- | ------- |
| Attributes per Lookup | Up to 20 | Number of data fields retrieved per record in a single lookup activity.|
| Lookup Activities | Up to 5 per journey | Each journey can contain up to 5 separate lookup activities. Each lookup can target a different dataset.|

## Configure the Dataset lookup activity {#configure}

To configure the **[!UICONTROL Dataset lookup]** activity, follow these steps:

1. Unfold the **[!UICONTROL Orchestration]** category and drop a **[!UICONTROL Dataset lookup]** activity into your canvas.

   ![[!DNL Adobe Experience Platform] dataset lookup activity in journey](assets/aep-data-activity.png)

1. Add a label and description.

1. In the **[!UICONTROL Dataset]** field, select the dataset with the attributes you need.

   >[!NOTE]
   >
   >If the dataset you are looking for does not display in the list, make sure you have enabled it for lookup. For more details, refer to the [Must read](#must-read) section.

1. Select the specific fields you want to fetch from the dataset.

   * You can only select leaf nodes (fields at the lowest level of the schema). The field must be a primitive value (string, number, boolean, date, etc.).

   * Lists (arrays) and maps (key–value objects) cannot be selected.

   +++Example
   
   ![Dataset field selection showing primitive data types and structure](assets/aep-data-leaf-primitive.png)
   
   +++

1. In the **[!UICONTROL Lookup key(s)]** field, choose a joining key that exists in both the decision item attributes and the dataset. This key is used by the system to search in the selected dataset.

   * Keys can be expressions derived from the journey context, such as SKUs, email IDs, or other identifiers. Example: `@profile.email` or `list(@event{purchase_event.products.sku})`.

   * Only **strings** or **lists of strings** are supported.

   >[!IMPORTANT]
   >
   >You must define the lookup key using **advanced mode**. If you use simple mode to set the key, the dataset lookup activity output will not be available as a context attribute in downstream activities, and the `@datasetLookup{}` syntax will fail with a "Dataset lookup not found" error in condition activities.

   +++Example
   
   ![Expression editor with dataset field lookup and string functions](assets/aep-data-strings.png)

   +++

## Use enriched data in the journey

The data retrieved by the **[!UICONTROL Dataset lookup]** activity is stored in the Journey context as an array of objects. It is available in the journey expression editor and personalization editor, enabling conditional logic and personalized messaging based on enriched data. 

* **Journey Expression Editor**:

   Access the **[!UICONTROL Advanced mode]** editor and use the syntax: `@datasetLookup{MyDatasetLookUpActivity1.entities}`. [Learn how to work with the advanced expression editor](../building-journeys/expression/expressionadvanced.md)

* **Personalization Editor**:

   Use the syntax: `{{context.journey.datasetLookup.1482319411.entities}}`.

>[!NOTE]
>
>Enriched data is transient and available only during the runtime of the journey, and in the personalization of outbound activities (Email, Push, SMS, etc.)

## Examples of use cases

+++Product Category-Based Filtering

**Scenario**:Send a coupon to users who spend more than $40 on household products.

**Journey flow**:

1. **Purchase Event**: Capture SKUs from the user's cart.

1. **Dataset lookup activity**:

   * Dataset: `products-dataset` (SKU as the primary key).
   * Lookup Keys: `list(@event{purchase_event.products.sku})`.
   * Fields to Return: `["SKU", "category", "price"]`.
   
1. **Condition activity**:

   * Filter SKUs where the category is "household".

      ```
      @event{purchase_event.products.all( in(currentEventField.sku, @datasetlookup{MyDatasetLookupActivity1.entities.all(currentDatasetLookupField.category == 'household').sku} ) )} 
      ```

   OR

   * Aggregate the total spend on household products and compare it to the $40 threshold.

      ```
      sum(@event{purchase_event.products.all( in(currentEventField.sku, @datasetlookup{MyDatasetLookUpActivity1.entities.all(currentDatasetLookupField.category == 'household').sku} ) )}.price}, ',', true ) > 40
      ```

1. **Personalization Editor**:

   Use the enriched data to personalize the email content:

   ```
   {% let householdTotal = 0 %}
   {{#each journey.datasetlookup.3709000.entities as |product|}}
   {%#if get(product, "category") = "household"%}
   {% let householdTotal = householdTotal + product.price %}{%/if%}
   {{/each}}
   "Hi, thanks for spending " + {%= householdTotal %} + " on household products. Here is your reward!"
   ```

+++

+++Personalization using external loyalty data

**Scenario**: Identify which email account for a profile has a Loyalty Status of Platinum. In this scenario, loyalty account is associated to an email ID and loyalty data is not available in the standard profile lookup store.  

**Journey flow**:

1. **Profile Event Trigger**: Capture email IDs from the profile or event context.

1. **Dataset Lookup activity**:
   * Dataset: `loyalty-member-dataset` (email as the primary key).
   * Lookup Keys: `@profile.email`.
   * Fields to Return: `["email", "loyaltyTier"]`.

1. **Condition activity**:

   Branch the journey based on the loyalty tier:

   ```
   @datasetLookup{MyDatasetLookUpActivity1.entity.loyaltyMember.loyaltyTier} == 'Platinum'
   ```

1. **Personalization Editor**:

   Use the enriched loyalty tier data to personalize outbound communication:
    
   ```
   {{context.journey.datasetLookup.1482319411.entity.loyaltyMember.loyaltyTier}}
   ```

+++

## Troubleshooting {#troubleshooting}

### "Dataset lookup not found" error in condition activity {#troubleshooting-not-found}

**Symptom:** The `@datasetLookup{}` syntax in a condition activity's advanced expression editor returns a "Dataset lookup not found" error, even though the dataset lookup activity is correctly configured in the journey.

**Cause:** The lookup key in the dataset lookup activity was set using simple mode. When the key is not defined in advanced mode, the activity output is not exposed as a context attribute in downstream activities.

**Fix:** Open the dataset lookup activity, locate the **[!UICONTROL Lookup key(s)]** field, and switch to **advanced mode** to redefine the key expression. Save the activity and republish the journey.

+++ AI Knowledge Reference

This section contains structured knowledge intended to support interpretation, retrieval, and question answering related to this topic.

For complete understanding, this information should be combined with the documentation on this page. Neither source is intended to stand alone; the page describes the feature, while this section provides additional context that helps disambiguate terminology, intent, applicability, and constraints.

* **TL;DR:** This page explains how to configure the Dataset lookup activity to dynamically retrieve AEP record dataset data at journey runtime for real-time personalization and conditional logic.

**Intents:**

* Add a Dataset lookup activity to a journey to fetch external AEP record data at runtime
* Select specific dataset fields (leaf nodes / primitive values) to retrieve during lookup
* Define a lookup key in advanced mode to join journey context with dataset records
* Use enriched dataset data in the journey expression editor or personalization editor
* Troubleshoot "Dataset lookup not found" errors caused by using simple mode for the lookup key

**Glossary:**

* **Dataset lookup activity**: A journey orchestration activity that retrieves data from AEP record datasets at runtime using a joining key *(product-specific)*
* **Leaf node**: A field at the lowest level of a schema hierarchy that holds a primitive value (string, number, boolean, date) *(product-specific)*
* **Lookup key**: The joining expression (string or list of strings) used to match journey context data against records in the selected dataset *(product-specific)*
* **Enriched data**: Data retrieved by a Dataset lookup activity and stored transiently in the journey context for use in downstream activities *(product-specific)*

**Guardrails:**

* Maximum of 10 Dataset lookup activities per journey.
* Maximum of 20 selected fields per lookup activity.
* Maximum of 50 keys in the lookup keys array.
* Enriched data size is limited to 10KB.
* The dataset must be enabled for lookup in Adobe Experience Platform before it appears in the activity configuration.
* Only leaf nodes (primitive values) can be selected; arrays and maps cannot be selected.
* Only strings or lists of strings are supported as lookup keys.
* The lookup key must be defined in advanced mode; using simple mode causes the activity output to be unavailable as a context attribute downstream.
* Enriched data is transient and available only during journey runtime and in outbound activity personalization.
* For performance, up to 5 lookup activities per journey and up to 20 attributes per lookup are recommended.

**Terminology:**

* Canonical name: Dataset lookup activity — Acronym: n/a — variants: AEP data lookup, data enrichment activity
* Synonyms: "lookup key" = "joining key"
* Do not confuse: "Dataset lookup activity" ≠ "Experience event lookup" — dataset lookup retrieves record dataset data, not time-series experience events

**FAQ:**

* **Q: Why doesn't my dataset appear in the Dataset field dropdown?** — The dataset must be enabled for lookup in Adobe Experience Platform. Follow the instructions in the Must-read section to enable it.
* **Q: Why does `@datasetLookup{}` return a "Dataset lookup not found" error in a condition?** — The lookup key was defined using simple mode instead of advanced mode. Redefine it in advanced mode and republish the journey.
* **Q: Can I retrieve arrays or map fields from the dataset?** — No, only primitive leaf node fields (string, number, boolean, date) can be selected.
* **Q: How do I access enriched data in an email?** — Use the personalization editor with the syntax `{{context.journey.datasetLookup.<activityId>.entities}}`.
* **Q: Is enriched data persisted after the journey ends?** — No, enriched data is transient and only available during the journey runtime session.

+++
