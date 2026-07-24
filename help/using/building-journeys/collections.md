---
solution: Journey Optimizer
product: journey optimizer
title: Pass collections into custom action parameters
description: Learn how to pass collections dynamically in Journey Optimizer using custom actions
feature: Journeys, Use Cases, Custom Actions, Collections
topic: Content Management
role: Developer
level: Experienced
exl-id: 8832d306-5842-4be5-9fb9-509050fcbb01
version: Journey Orchestration
TQID: https://experienceleague.adobe.com/zhAlHWwS8UOup7yqqVc2d0lqj4JUj5gOvz7JAwVwZPk
product_v2:
  - id: cb954087-f4fc-4456-afb9-e939cabcdc79
    internal-label: Journey Optimizer
feature_v2:
  - id: d998adac-2f81-400b-a669-d07bb196e4eb
    internal-label: Journeys
subfeature_v2:
  - id: c2beecbb-b93e-4ae3-baa9-72adcdc06781
    internal-label: Action configuration
  - id: fa683eda-48de-4558-af32-2673edcd44fe
    internal-label: Events
role_v2:
  - id: ff6a42d2-313e-452e-93a6-792e4fad9ff8
    internal-label: Developer
topic_v2:
  - id: c1579802-ddd4-4214-8a91-97b2066abe11
    internal-label: Troubleshooting
  - id: e0eb8757-182f-49f3-94a4-1587d16f5094
    internal-label: Personalization
---
# Pass collections into custom action parameters {#passing-collection}

>[!BEGINSHADEBOX]

**On this page:** Learn how to pass simple and object collections into custom action parameters so they are dynamically populated at runtime.

>[!ENDSHADEBOX]

You can pass a collection in custom action parameters that is dynamically populated at runtime.

Two types of collections are supported:

* **Simple collections**

   Use simple collections for lists of basic values, such as strings, numbers, or booleans. These are useful when you only need to pass a list of items without additional properties.

   For example, a list of device types:

   ```json
   {
    "deviceTypes": [
        "android",
        "ios"
    ]
   }
   ```

* **Object collections**

   Use object collections when each item includes multiple fields or properties. These are typically used to pass structured data, such as product details, event records, or item attributes.

   For example:

   ```json
   {
   "products":[
      {
         "id":"productA",
         "name":"A",
         "price":20.1
      },
      {
         "id":"productB",
         "name":"B",
         "price":10.0
      },
      {
         "id":"productC",
         "name":"C",
         "price":5.99
      }
    ]
   }
   ```

>[!NOTE]
>
>Nested arrays within collections are only partially supported in custom action request payloads. For details, see [Limitations](#limitations).

## General procedure {#general-procedure} 

In this section, we use the following JSON payload example. This is an array of objects with a field that is a simple collection.

```json
{
  "ctxt": {
    "products": [
      {
        "id": "productA",
        "name": "A",
        "price": 20.1,
        "color":"blue",
        "locations": [
          "Paris",
          "London"
        ]
      },
      {
        "id": "productB",
        "name": "B",
        "price": 10.99
      }
    ]
  }
}
```

You can see that `products` is an array of two objects. You need to have at least one object.

1. Create your custom action. Learn more on [this page](../action/about-custom-action-configuration.md).

1. In the **[!UICONTROL Action parameters]** section, paste the JSON example. The displayed structure is static: when pasting the payload, all fields are defined as constants. 

   ![Expression editor showing collection functions and operations](assets/uc-collection-1.png)

1. If needed, adjust the field types. The following field types are supported for collections: listString, listInteger, listDecimal, listBoolean, listDateTime, listDateTimeOnly, listDateOnly, listObject

   >[!NOTE]
   >
   >The field type is automatically inferred according to the payload example.

1. If you want to pass objects dynamically, you need to set them as variables. In this example we set `products` as variable. All the object fields included in the object are set to variables automatically.

    >[!NOTE]
    >
    >The first object of the payload example is used to define the fields.

1. For each field, define the label which will be displayed in the journey canvas.

   ![Filter collection function with condition builder interface](assets/uc-collection-2.png){width="70%"}

1. Create your journey and add the custom action you created. Learn more on [this page](../building-journeys/using-custom-actions.md).

1. In the **[!UICONTROL Action parameters]** section, define the array parameter (`products` in our example) using the advanced expression editor.

   ![Collection filtering expression with field selection](assets/uc-collection-3.png)

1. For each of the following object field, type the corresponding field name from the source XDM schema. If the names are identical, this is not needed. In our example, we only need to define `product id` and "color".

   ![Collection sort function with ordering configuration](assets/uc-collection-4.png){width="50%"}

For the array field, you can also use the advanced expression editor to perform data manipulation. In the following example, we use the [filter](functions/list-functions.md#filter) and [intersect](functions/list-functions.md#intersect) functions:

![Complete collection expression with filter, sort, and limit operations](assets/uc-collection-5.png)

## Limitations {#limitations}

While collections in custom actions provide flexibility for passing dynamic data, there are certain structural constraints to be aware of:

* **Support for Nested Arrays in Custom Actions**

   [!DNL Adobe Journey Optimizer] supports nested arrays of objects in custom action **response payloads**, but this support is limited in **request payloads**.

   In request payloads, nested arrays are only supported when they contain a fixed number of items, as defined in the custom action configuration. For example, if a nested array always includes exactly three items, it can be configured as a constant. When the number of items needs to be dynamic, only non-nested arrays (arrays at the bottom level) can be defined as variables.

   Example:
   
   1. The following example illustrates a **non-supported use case**.

      In this example, the products array includes a nested array (`locations`) with a dynamic number of items, which is not supported in request payloads.

      ```json
      {
      "products": [
         {
            "id": "productA",
            "name": "A",
            "price": 20,
            "locations": [
            { "name": "Paris" },
            { "name": "London" }
            ]
         }
      ]
      }
      ```
      
   2. Supported example, with fixed items defined as constants. 

      In this case, the nested locations are replaced by fixed fields (`location1`, `location2`), allowing the payload to remain valid within the supported configuration.

      ```json
      {
      "products": [
         {
            "id": "productA",
            "name": "A",
            "price": 20,
            "location1": { "name": "Paris" },
            "location2": { "name": "London" }
         }
      ]
      }
      ```


* **Testing collections**: To test collections using test mode, you must use code view mode. Note that code view mode is not supported for business events, so in that case, you can only send a collection containing a single element.


## Particular cases{#examples}

For heterogeneous types and arrays of arrays, the array is defined with the listAny type. You can only map individual items, but cannot change the array to variable.

![Heterogeneous collection with mixed data types and field selection](assets/uc-collection-heterogeneous.png){width="70%"}

Example of heterogenous type:

```json
{
    "data_mixed-types": [
        "test",
        "test2",
        null,
        0
    ]
}
```

Example of array of arrays:

```json
{
    "data_multiple-arrays": [
        [
            "test",
            "test1",
            "test2"
        ]
    ]
}
```

## Additional resources

Browse the sections below to learn more about configuring, using and troubleshooting your custom actions:

* [Get started with custom actions](../action/action.md) - Learn what is a custom action and how they help you connect to your third-party systems
* [Configure your custom actions](../action/about-custom-action-configuration.md) - Learn how to create and configure a custom action
* [Use custom actions](../building-journeys/using-custom-actions.md) - Learn how to use custom actions in your journeys
* [Custom action troubleshooting](../action/troubleshoot-custom-action.md) - Learn how to troubleshoot a custom action
* [Iterate over contextual data](../personalization/iterate-contextual-data.md#arrays-in-journeys) - Learn how to work with arrays in Journey expressions and iterate over custom action responses, event data, and dataset lookups in message personalization

+++ AI Knowledge Reference

This section contains structured knowledge intended to support interpretation, retrieval, and question answering related to this topic.

For complete understanding, this information should be combined with the documentation on this page. Neither source is intended to stand alone; the page describes the feature, while this section provides additional context that helps disambiguate terminology, intent, applicability, and constraints.

* **TL;DR:** This page explains how to pass simple and object collections dynamically into custom action parameters in Journey Optimizer, including supported field types, the configuration procedure, and known limitations around nested arrays.

**Intents:**
* Configure a custom action to accept a collection (simple or object) as a dynamic parameter
* Define array parameters as variables in the advanced expression editor when building a journey
* Apply filter and intersect functions to manipulate array data in the expression editor
* Understand and work within the nested array limitations for custom action request payloads
* Test collection parameters using code view mode in journey test mode

**Glossary:**
* **Simple collection**: A list of basic scalar values (strings, numbers, booleans) passed as a custom action parameter *(product-specific)*
* **Object collection**: A list of structured objects, each with multiple fields, passed as a custom action parameter *(product-specific)*
* **listObject**: The field type used in custom action configuration to represent an array of objects *(product-specific)*
* **listAny**: The field type used for heterogeneous arrays or arrays of arrays where items have mixed types *(product-specific)*
* **Variable (vs. Constant)**: In action parameter configuration, a field set to "variable" is populated dynamically at runtime from the journey context, while a "constant" is a fixed value set at configuration time *(product-specific)*

**Guardrails:**
* Nested arrays in request payloads are only supported when they contain a fixed number of items (defined as constants); dynamic nested arrays are not supported
* Code view mode is required to test collections in test mode; code view is not supported for business events, so only single-element collections can be sent in that case
* At least one object must be present in the payload example used to define collection fields
* The first object of the payload example defines the fields for the entire collection

**Terminology:**
* Canonical name: Collection — Acronym: none — variants: array, list, dynamic collection
* Synonyms: "simple collection" = "list of scalar values" ; "object collection" = "array of objects"
* Do not confuse: "listAny" ≠ "listObject" (listAny handles heterogeneous or nested arrays; listObject handles uniform arrays of structured objects)

**FAQ:**
* **Q: What is the difference between a simple collection and an object collection?** — A simple collection contains basic scalar values (strings, numbers, booleans), while an object collection contains structured objects each with multiple named fields.
* **Q: How do I make a collection parameter dynamic at runtime?** — In the custom action's Action parameters section, set the array field to "variable"; all object fields within it are then automatically set to variables.
* **Q: Are nested arrays supported in custom action request payloads?** — Only partially. Nested arrays with a fixed, known number of items can be defined as constants. Nested arrays with a dynamic number of items are not supported in request payloads.
* **Q: How do I test a collection in journey test mode?** — Use code view mode in the test interface. Note that business events do not support code view, so only single-element collections can be tested in that context.
* **Q: What field types are supported for collections?** — listString, listInteger, listDecimal, listBoolean, listDateTime, listDateTimeOnly, listDateOnly, and listObject are all supported.

+++
