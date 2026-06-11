---
title: Use supplemental identifiers in journeys
description: Learn how to use supplemental identifiers in journeys.
exl-id: f6ebd706-4402-448a-a538-e9a4c2cf0f8b
version: Journey Orchestration
TQID: https://experienceleague.adobe.com/ABOlJ-ZF0a3xLNY-hH6jjFqu53ph4PynNalGkgQ6P8k
product_v2:
  - id: cb954087-f4fc-4456-afb9-e939cabcdc79
    internal-label: Journey Optimizer
feature_v2:
  - id: b3538224-471e-4c63-a444-9b19d89ae29c
    internal-label: Activities
  - id: d998adac-2f81-400b-a669-d07bb196e4eb
    internal-label: Journeys
subfeature_v2:
  - id: d08afb72-92f6-4856-88e3-11ec34313c2f
    internal-label: Event configuration
  - id: fa683eda-48de-4558-af32-2673edcd44fe
    internal-label: Events
topic_v2:
  - id: c7d04a2c-412a-4c9d-9d7a-4456eaa5adeb
    internal-label: Governance
  - id: e0eb8757-182f-49f3-94a4-1587d16f5094
    internal-label: Personalization
---
# Use supplemental identifiers in journeys {#supplemental-id}

>[!CONTEXTUALHELP]
>id="ajo_journey_parameters_supplemental_identifier"
>title="Use supplemental identifier"
>abstract="The supplemental identifier is a secondary identifier that provides additional context for the execution of a journey. It consists of the field used as the supplemental identifier and a namespace associated with it."

<table style="border-collapse: collapse; width: 100%;">
  <tr>
    <td style="vertical-align: top; padding-right: 20px; border: none;">
      <p>By default, journeys are executed in the context of a <b>profile ID</b>. This means that, as long as the profile is active in a given journey, it won't be able to re-enter another journey. To prevent this, Journey Optimizer allows you to capture a <b>supplemental identifier</b>, such as an order ID, subscription ID, prescription ID, in addition to the profile ID.  
      <p>In this example, we have added a <b>booking ID</b> as a supplemental identifier.</p>
      <p>By doing so, journeys are executed in the context of the profile ID associated to the supplemental identifier (here, the booking ID). One instance of the journey is executed for each iteration of the supplemental identifier. This allows multiple entrances of the same profile ID in journeys if they have made different bookings.</p>
      <p>In addition, Journey Optimizer allows you to leverage attributes of the supplemental identifier (e.g., booking number, prescription renewal date, product type) for message customization, ensuring highly relevant communications.</p>
    </td>
    <td style="vertical-align: top; border: none; text-align: center; width: 40%;">
      <img src="assets/event-supplemental-id.png" alt="Supplemental identifier example" style="max-width:100%;" />
    </td>
  </tr>
</table>

➡️ [Discover this feature in video](#video)

## Guardrails & limitations {#guardrails}

* **Supported journeys**: Supplemental identifiers are supported for **event-triggered** and **Read audience** journeys. They are **not supported** for Audience qualification journeys (i.e., journeys starting with an Audience qualification activity). 

* **Concurrent instance limits**: Profiles cannot have more than 10 concurrent journey instances.

* **Frequency rules**: Each journey instance created from supplemental identifier usage counts towards frequency capping, even if the use of supplement identifiers results in multiple journey instances.

* **Data type and schema structure**: The supplemental identifier must be of type `string`. It can be an independent string attribute or it can be a string attribute within an array of objects. The independent string attribute will result in a single journey instance, whereas the string attribute within an array of objects will result in a unique journey instance per iteration of the object array. String arrays and maps are not supported.

* **Journey reentrance**

  Journey reentrance behavior with supplemental identifiers follows the existing reentrance policy:

  * If the journey is non-reentrant, the same profile ID + supplemental ID combination cannot reenter the journey.
  * If the journey is reentrant with a time window, the same profile ID + supplemental ID combination can reenter after the defined time window.

* **Data Use Labelling and Enforcement (DULE)** - No DULE validation checks are performed on the supplemental ID. This means that this attribute will not be considered when the journey is looking for data governance policy violations.

* **Downstream events configuration**

  If you are using another event downstream in the journey, it must use the same supplemental ID and have the same ID namespace.

* **Read audience journeys**

  * Supplemental ID is disabled if you use a business event.
  * Supplemental ID must be a field from the profile (i.e., not an event/context field).
  * For read audience journeys using supplemental IDs, the reading rate of the read audience activity for each journey instance is limited to a maximum of 500 profiles per second.
  * Only Unified Profile Service audiences are supported when using Read audience journeys with supplemental IDs.

## Exit criteria behavior with supplemental IDs {#exit-criteria}

Precondition: Journey enabled for supplemental ID (via unitary event or read audience activities)

The table below explains the behavior of profiles in a supplemental ID-enabled journey when exit criteria is configured:

| Exit criteria configuration | Behavior when exit criteria is met |
| ---------------------------- | ---------------------------------- |
| Based on a non-supplemental ID event | All instances of the corresponding profile in that journey are exited. |
| Based on a supplemental ID event <br/>*Note: Supplemental ID namespace must match that of the initial node.* | Only the matching profile + supplemental ID instance is exited. |
| Based on an audience | All instances of the corresponding profile in that journey are exited. |

## Add a supplemental identifier and leverage it in a journey {#add}

>[!BEGINTABS]

>[!TAB Event-triggered journey]

To use a supplemental identifier in an event-triggered journey, follow these steps:

1. **Mark the attribute as an identifier in the event schema**

    1. Access the event schema and locate the attribute you want to use as a supplemental identifier (e.g., booking ID, subscription ID) and mark it as an ID. [Learn how to work with schemas](../data/get-started-schemas.md)

    1. Mark the identifier as an **[!UICONTROL Identity]**.

        ![Schema configuration with supplemental identifier field group](assets/supplemental-ID-schema.png)

        >[!IMPORTANT]
        >
        >Make sure you do not mark the attribute as **Primary identity**.

    1. Select the namespace to associate with the supplemental ID. This must be a non-person identifier namespace.

        After applying the non-person identity namespace to a schema, you must create a new event in order to use the supplemental identifier. Existing entities cannot be refreshed to recognize the new identifier.

1. **Add the supplemental ID to the event**

    1. Create or edit the desired event. [Learn how to configure a unitary event](../event/about-creating.md)

    1. In the event configuration screen, check the **[!UICONTROL Use supplemental identifier]** option.

        ![Event configuration with supplemental identifier namespace selection](assets/supplemental-ID-event.png)

    1. Use the expression editor to select the attribute you marked as the supplemental ID.

        >[!NOTE]
        >
        >Make sure you are using the expression editor in **[!UICONTROL Advanced mode]** to select the attribute.

    1. After selecting the supplemental ID, the associated namespace is displayed in the event configuration screen as read-only.

1. **Add the event to the journey**

    Drag the configured event onto the journey canvas. It will trigger journey entry based on both the profile ID and the supplemental ID.

      ![Journey using supplemental identifier for event triggering](assets/supplemental-ID-journey.png)

>[!TAB Read audience journey]

To use a supplemental identifier in a Read audience journey, follow these steps:

1. **Mark the attribute as an identifier in the union/profile schema**

    1. Access the union/profile schema and locate the attribute you want to use as a supplemental identifier (e.g., booking ID, subscription ID) and mark it as an ID. [Learn how to work with schemas](../data/get-started-schemas.md)

    1. Mark the identifier as an **[!UICONTROL Identity]**.

        ![Profile schema with supplemental identifier field configured](assets/supplemental-ID-schema-profile.png)

        >[!IMPORTANT]
        >
        >Make sure you do not mark the attribute as **Primary identity**.

    1. Select the namespace to associate with the supplemental ID. This must be a non-person identifier namespace.
    
        After applying the non-person identity namespace to a schema, you must create a new field group in order to use the supplemental identifier. Existing entities cannot be refreshed to recognize the new identifier.

<!--
1. **Add the supplemental ID field to the data source**

    1. Navigate to the **[!UICONTROL Configuration]** / **[!UICONTROL Data Sources]** menu, then locate the "ExperiencePlatformDataSource" data source.

        ![Data source configuration with supplemental identifier mapping](assets/supplemental-ID-data-source.png)

    1. Open the field selector then select the attribute you want to use as a supplemental identifier (e.g., booking ID, subscription ID).
-->

1. **Add and configure a Read audience activity in the journey**

    1. Drag a **[!UICONTROL Read audience]** activity in your journey.

    1. In the activity properties pane, toggle on the **[!UICONTROL Use supplemental identifier]** option.

        ![Read Audience activity with supplemental identifier configuration](assets/supplemental-ID-read-audience.png)

    1. In the **[!UICONTROL Supplement identifier]** field, use the expression editor to select the attribute you marked as the supplemental ID.

        >[!NOTE]
        >
        >Make sure you are using the expression editor in **[!UICONTROL Advanced mode]** to select the attribute.
  
    1. After selecting the supplemental ID, the associated namespace is displayed in the **[!UICONTROL Supplemental namespace]** field as read-only.

>[!ENDTABS]

## Leverage supplemental ID attributes

Use the expression editor and personalization editor to reference attributes of the supplemental identifier for personalization or conditional logic. Attributes are accessible from the **[!UICONTROL Contextual attributes]** menu.

![Personalization editor showing supplemental identifier fields for content](assets/supplemental-ID-perso.png)

For event-triggered journeys if you are working with arrays (e.g., multiple prescriptions or policies), use a formula to extract specific elements.

+++ See examples

In an object array with the supplemental ID as `bookingNum` and an attribute at the same level called `bookingCountry`, the journey will iterate through the array object based on the bookingNum and create a journey instance for each object.
    
* The following expression in the condition activity will iterate through the object array and check whether the value of `bookingCountry` is equal to "FR":

  ```
  @event{<event_name>.<object_path>.<object_array_name>.all(currentEventField.<attribute_path>.bookingNum==${supplementalId}).at(0).<attribute_path>.bookingCountry}=="FR"
  ```

* The following expression in the email personalization editor will iterate through the object array, pull out the `bookingCountry` applicable to the current journey instance, and display it in the content:

  ```
  {{#each context.journey.events.<event_ID>.<object_path>.<object_array_name> as |l|}} 

  {%#if l.<attribute_path>.bookingNum = context.journey.technicalProperties.supplementalId%} {{l.<attribute_path>.bookingCountry}}  {%/if%}

  {{/each}}
  ```
      
* Example of the event used to trigger the journey:

  ```
  "bookingList": [
        {
            "bookingInfo": {
                "bookingNum": "x1",
                      "bookingCountry": "US"
            }
        },
        {
            "bookingInfo": {
                "bookingNum": "x2",
                "bookingCountry": "FR"
            }
        }
    ]
  ```

+++

## Example use cases

These examples show how supplemental identifiers support multiple related records.

### **Policy renewal notifications**

* **Scenario**: An insurance provider sends renewal reminders for each active policy held by a customer.
* **Execution**:
  * Profile: "John".
  * Supplemental IDs: `"AutoPolicy123", "HomePolicy456"`.
  * Journey executes separately for each policy, with personalized renewal dates, coverage details, and premium information.

### **Subscription Management**

* **Scenario**: A subscription service sends tailored messages for each subscription when an event is triggered for that subscription.
* **Execution**:
  * Profile: "Jane".
  * Supplemental IDs: `"Luma Yoga Program ", "Luma Fitness Program"`.
  * Each event includes a subscription ID and details about that subscription. Journey executes separately for each event/subscription, allowing personalized renewal offers per subscription.

### **Product Recommendations**

* **Scenario**: An e-commerce platform sends recommendations based on specific products purchased by a customer.
* **Execution**:
  * Profile: "Alex".
  * Supplemental IDs: `"productID1234", "productID5678"`.
  * Journey executes separately for each product, with personalized upsell opportunities.

## How-to video {#video}

Learn how to enable and apply a supplemental identifier in [!DNL Adobe Journey Optimizer]. 

>[!VIDEO](https://video.tv.adobe.com/v/3464792?quality=12)

+++AI Assistant — Page context

* **TL;DR:** This page explains how to use supplemental identifiers in Adobe Journey Optimizer journeys to allow a single profile to have multiple concurrent journey instances, each scoped to a distinct secondary ID such as a booking, subscription, or policy ID.

**Intents:**
* Understand when and why to use a supplemental identifier instead of relying solely on a profile ID
* Configure a supplemental identifier in an event-triggered journey by marking an attribute as an identity in the event schema
* Configure a supplemental identifier in a Read audience journey by enabling the option in the Read audience activity
* Reference supplemental identifier attributes for message personalization and conditional logic using the expression editor
* Apply the correct expression syntax to iterate over object arrays keyed by a supplemental ID
* Identify guardrails and limitations before implementing supplemental identifiers in a journey

**Glossary:**
* **Supplemental identifier**: A secondary identifier (e.g., order ID, booking ID, subscription ID) used alongside the profile ID to scope a journey instance to a specific record, enabling multiple concurrent instances per profile *(product-specific)*
* **Profile ID**: The primary identifier used by default to execute journeys; a profile active in a journey cannot re-enter another journey without a supplemental ID
* **Non-person identifier namespace**: An identity namespace that does not represent a person (required for supplemental IDs); must be distinct from the primary identity namespace
* **joai namespace**: Not applicable to this page (see inbound actions troubleshooting)
* **DULE**: Data Use Labelling and Enforcement — the data governance policy validation framework in Adobe Experience Platform; supplemental IDs are not subject to DULE checks

**Guardrails:**
* Supplemental identifiers are supported only for event-triggered and Read audience journeys; not supported for Audience qualification journeys
* A profile cannot have more than 10 concurrent journey instances
* Each journey instance counts toward frequency capping even when created via supplemental identifiers
* The supplemental identifier must be of type `string`; string arrays and maps are not supported
* The supplemental ID attribute must not be marked as Primary identity in the schema
* The namespace used for the supplemental ID must be a non-person identifier namespace
* After applying the non-person identity namespace to a schema, a new event or field group must be created; existing entities cannot be refreshed
* For Read audience journeys with supplemental IDs: the reading rate is limited to 500 profiles per second per journey instance; only Unified Profile Service audiences are supported; supplemental ID must be a profile field (not an event/context field)
* Downstream events in the same journey must use the same supplemental ID and namespace
* Supplemental ID is disabled for Read audience journeys that use a business event

**Terminology:**
* Canonical name: Supplemental identifier — Acronym: none — variants: supplemental ID, secondary identifier
* Synonyms: "supplemental identifier" = "supplemental ID" (used interchangeably in the UI and documentation)
* Do not confuse: "supplemental identifier" ≠ "primary identity" — the supplemental ID must never be marked as the primary identity in the schema

**FAQ:**
* **Q: What is a supplemental identifier used for?** — It allows a single profile to enter and execute a journey multiple times simultaneously, with each instance scoped to a different secondary record such as a booking, subscription, or policy ID.
* **Q: Which journey types support supplemental identifiers?** — Event-triggered journeys and Read audience journeys. Audience qualification journeys do not support supplemental identifiers.
* **Q: How many concurrent journey instances can a profile have with supplemental identifiers?** — A maximum of 10 concurrent journey instances per profile.
* **Q: Can I use the supplemental ID attributes for message personalization?** — Yes. Reference them via the Contextual attributes menu in the expression editor or personalization editor.
* **Q: Does the supplemental ID need to be marked as a Primary identity in the schema?** — No. It must be marked as an Identity but must not be set as the Primary identity.
* **Q: Are DULE governance policies applied to the supplemental identifier?** — No. DULE validation checks are not performed on the supplemental ID.

+++
