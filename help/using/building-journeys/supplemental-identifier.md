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

>[!BEGINSHADEBOX]

**On this page:** Learn how to use supplemental identifiers — secondary identifiers such as an order or booking ID — to run a separate journey instance per identifier and personalize messages with its attributes.

>[!ENDSHADEBOX]

>[!CONTEXTUALHELP]
>id="ajo_journey_parameters_supplemental_identifier"
>title="Use supplemental identifier"
>abstract="The supplemental identifier is a secondary identifier that provides additional context for the execution of a journey. To define it, select any non-identity attribute (or non-person identity) from the audience or event to use as the supplemental identifier."

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

* **Inbound actions**: Supplemental identifiers are currently not supported for inbound actions, such as in-app and web actions.

* **Concurrent instance limits**: Profiles cannot have more than 10 concurrent journey instances.

* **Data type and schema structure**: The supplemental identifier must be of type `string`. It can be an independent string attribute or it can be a string attribute within an array of objects. The independent string attribute will result in a single journey instance, whereas the string attribute within an array of objects will result in a unique journey instance per iteration of the object array. String arrays and maps are not supported.

* **Journey reentrance**

  Journey reentrance behavior with supplemental identifiers follows the existing reentrance policy:

  * If the journey is non-reentrant, the same profile ID + supplemental ID combination cannot reenter the journey.
  * If the journey is reentrant with a time window, the same profile ID + supplemental ID combination can reenter after the defined time window.

* **Data Use Labelling and Enforcement (DULE)** - No DULE validation checks are performed on the supplemental ID. This means that this attribute will not be considered when the journey is looking for data governance policy violations.

* **Downstream events configuration**

  If you are using another event downstream in the journey, it must use the same supplemental ID and have the same ID namespace.

* **Read audience journeys**

  * **Business events**: Supplemental ID is disabled if you use a business event.
  * **Event and context fields**: The supplemental identifier must not be sourced from an event or journey context field.
  * **Attribute selection**: Any non-identity attribute (or non-person identity) can be used as the supplemental ID, for all audience types (Unified Profile Service, CSV import, and Federated Audience Composition). Person-based identity attributes are not permitted. For external audiences, see [Supplemental identifiers with external audiences](#external-audiences) for supported data patterns and configuration requirements.
  * **Reading rate**: For read audience journeys using an array-type supplemental ID field, the reading rate of the Read audience activity is limited to a maximum of 500 profiles per second.

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

1. **Add the supplemental ID to the event**

    1. Create or edit the desired event. [Learn how to configure a unitary event](../event/about-creating.md)

    1. In the event configuration screen, check the **[!UICONTROL Use supplemental identifier]** option.

        ![Event configuration with supplemental identifier option](assets/supplemental-ID-event.png)

    1. Use the expression editor to select the field you want to use as the supplemental ID (e.g., booking ID, subscription ID).

        >[!NOTE]
        >
        >Make sure you are using the expression editor in **[!UICONTROL Advanced mode]** to select the attribute.

1. **Add the event to the journey**

    Drag the configured event onto the journey canvas. It will trigger journey entry based on both the profile ID and the supplemental ID.

      ![Journey using supplemental identifier for event triggering](assets/supplemental-ID-journey.png)

>[!TAB Read audience journey]

To use a supplemental identifier in a Read audience journey, follow these steps:

1. **Add and configure a Read audience activity in the journey**

    1. Drag a **[!UICONTROL Read audience]** activity in your journey.

    1. In the activity properties pane, toggle on the **[!UICONTROL Use supplemental identifier]** option.

        ![Read Audience activity with supplemental identifier configuration](assets/supplemental-ID-read-audience.png)

    1. In the **[!UICONTROL Supplemental identifier]** field, use the expression editor to select the supplemental identifier attribute.
    
      For audiences [imported from a CSV file](https://experienceleague.adobe.com/docs/experience-platform/segmentation/ui/overview.html#import-audience){target="_blank"}, if your CSV audience contains multiple rows per profile ID, make sure Express Activation is enabled first — see [Supplemental identifiers with external audiences](#external-audiences).

        >[!NOTE]
        >
        >Make sure you are using the expression editor in **[!UICONTROL Advanced mode]** to select the attribute.

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

## Supplemental ID and journey arbitration {#arbitration}

Journey arbitration (including concurrency caps and entry counting within rulesets) operates at the profile ID level, not the (profile ID, supplemental ID) pair level. This means a concurrency cap of 1 may block a second journey instance for the same profile even when it carries a different supplemental ID value.

Contact your Adobe representative for guidance on arbitration behavior before relying on specific arbitration settings in production.

**Related documentation:**

* [Journey capping & arbitration](../conflict-prioritization/journey-capping.md)
* [Work with rule sets](../conflict-prioritization/rule-sets.md)
* [Conflict management & prioritization](../conflict-prioritization/gs-conflict-prioritization.md)

## Supplemental identifiers with external audiences {#external-audiences}

Supplemental ID is supported for external audiences, including audiences [imported from a CSV file](https://experienceleague.adobe.com/docs/experience-platform/segmentation/ui/overview.html#import-audience){target="_blank"} and audiences created with [Federated Audience Composition](../audience/get-started-audience-orchestration.md). When configuring a journey that reads from a CSV or Federated Audience Composition audience, you can designate any non-identity attribute in that audience as the supplemental ID. Journey Optimizer then creates a separate journey instance per unique profile + supplemental ID combination.

* Use case 1: One row per unique profile + supplemental ID pair

  This is the primary use case for CSV and Federated Audience Composition audiences. The audience contains multiple rows where each row represents a unique combination of a profile (e.g., a customer) and a supplemental ID (e.g., an account or order ID). Each row is treated as an independent activation record.

  | profile_id | account_id *(Supplemental ID)* | other_attributes |
  | --- | --- | --- |
  | customer_001 | ACC-1001 | … |
  | customer_001 | ACC-1002 | … |
  | customer_002 | ACC-2001 | … |

  In this example, `customer_001` has two accounts. Journey Optimizer creates a separate journey instance for each unique profile + `account_id` pair.

* Use case 2: One row per profile with an array of supplemental IDs

  This use case is available for audience types that support arrays. A single row in the audience contains a profile with an array attribute holding multiple supplemental ID values. Journey Optimizer creates one journey instance per value in the array.

  | profile_id | account_ids *(array, Supplemental ID)* | other_attributes |
  | --- | --- | --- |
  | customer_001 | [ACC-1001, ACC-1002] | … |
  | customer_002 | [ACC-2001] | … |

  In this example, Journey Optimizer generates two journey instances for `customer_001` (one per account ID) and one instance for `customer_002`. This behaves consistently with how supplemental ID works for Unified Profile Service audiences.

### How to configure {#external-configuration}

For CSV audiences using Use Case 1 (where the audience intentionally contains multiple rows for the same profile ID)you must enable Express Activation before configuring the journey. See the prerequisite below. For all other cases, configure the journey directly.

+++ Prerequisite: Enable Express Activation on CSV audiences via API

>[!IMPORTANT]
>
>This prerequisite applies only to CSV audiences where the audience intentionally contains multiple rows for the same profile ID (Use Case 1). Federated Audience Composition audiences have Express Activation enabled by default and do not require this step. The Audience Portal UI does not support setting `expressActivation` — you must use the External Audience API.

You must enable `expressActivation` on the audience at creation time. This tells Journey Optimizer to activate every record independently, without deduplication by profile ID. This flag cannot be changed after the audience is created.

Use the following API call when creating the audience:

Endpoint:

```http
POST https://platform.adobe.io/data/core/ais/external-audience
```

Required headers:

```http
Authorization: Bearer {ACCESS_TOKEN}
Content-Type: application/json
x-api-key: {API_KEY}
x-gw-ims-org-id: {IMS_ORG}
x-sandbox-name: {SANDBOX_NAME}
```

Request body (set `expressActivation: true`):

```json
{
  "name": "my_audience_name",
  "fields": [ ... ],
  "sourceSpec": { ... },
  "audienceType": "people",
  "namespace": "CustomerAudienceUpload",
  "expressActivation": true
}
```

>[!NOTE]
>
>`expressActivation` defaults to `false`. It must be set at audience creation time and cannot be changed after creation. All Federated Audience Composition audiences have Express Activation enabled by default and do not require this flag.

See the [create external audience API documentation](https://experienceleague.adobe.com/en/docs/experience-platform/segmentation/tutorials/create-external-audience#create){target="_blank"} for the full reference.

+++

To configure the journey:

1. Open or create a journey with a **[!UICONTROL Read audience]** node.
1. In the **[!UICONTROL Read audience]** node settings, select your CSV or Federated Audience Composition audience.
1. Toggle on the **[!UICONTROL Use supplemental identifier]** option, then in the **[!UICONTROL Supplemental identifier]** field, use the expression editor in **[!UICONTROL Advanced mode]** to choose the attribute you want to use as the secondary identifier (e.g., `account_id`, `order_number`).
1. The selected attribute is treated as the supplemental ID for the journey — no identity registration is required.

### Deduplication behavior {#external-dedup}

When an audience has Express Activation enabled (always true for Federated Audience Composition - must be set explicitly for CSV), Journey Optimizer handles deduplication based on how the journey is configured:

| Scenario | Example audience rows | Behavior |
| --- | --- | --- |
| **Journey with supplemental ID — no duplicate (profile ID, supplemental ID) pairs** | (P1, S1), (P1, S2) | Intended use case. Journey Optimizer creates a separate journey instance per unique profile + supplemental ID combination. All rows are admitted. |
| **Journey with supplemental ID — duplicate (profile ID, supplemental ID) pairs exist** | (P1, S1), (P1, S1), (P1, S2) | Rows sharing the same (profile ID, supplemental ID) combination are filtered out by normal journey reentrance logic. Only the first matching row per unique combination is admitted. |
| **Journey without supplemental ID configured** | (P1, S1), (P1, S2) | Without a supplemental ID, Journey Optimizer treats all rows for the same profile ID as the same profile. Only one journey instance per profile ID is admitted; additional rows for the same profile are discarded. |

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

{{$include /help/_includes/do-not-localize/building-journeys/ai-augmented-supplemental-identifier.md}}
