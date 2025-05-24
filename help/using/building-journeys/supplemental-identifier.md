---
title: Supplemental identifier in event-triggered journeys
description: Learn how to use supplemental identifier in event-triggered journeys.
badge: label="Limited availability" type="Informative"
---

# Supplemental identifier in event-triggered journeys

>[!AVAILABILITY]
>
>This capability is only available for a set of organizations (Limited Availability). To gain access, contact your Adobe representative.

By default, event-triggered journeys are executed in the context of a **profile ID**. This means that, as long as the profile is active in a given journey, it won't be able to re-enter another journey. To prevent this, Journey Optimizer allows you to capture a **supplemental identifier** in your events, such as an order ID, subscription ID, prescription ID, in addition to the profile ID. 
In this example, we have added a booking ID as a supplemental identifier. 

![](assets/event-supplemental-id.png){width=40% zoomable}

By doing so, journeys triggered by the event are executed in the context of the profile ID associated to the supplemental identifier (here, the booking ID). One instance of the journey is executed for each iteration of the supplemental identifier. This allows multiple entrances of the same profile ID in journeys if they have made different bookings. 

In addition, Journey Optimizer allows you to leverage attributes of the supplemental identifier (e.g., booking number, prescription renewal date, product type) for message customization, ensuring highly relevant communications. <!--Example: A healthcare provider can send renewal reminders for each prescription in a patient's profile.-->

## Guardrails & limitations

* **Concurrent instance limits**: Profiles cannot have more than 10 concurrent journey instances.

<!--* **Array depth**: Supplemental identifier objects can have a maximum depth of 3 levels (2 levels of nesting).

    +++Example

    ```
    [
    (level 1) "Atorvastatin" : {
    "description" : "used to lower cholesterol",
    "renewal_date" : "11/20/25",
    "dosage" : "10mg"
    (level 2) "ingredients" : [
    (level 3) "Atorvastatin calcium",
    "lactose monohydrate",
    "microcrystalline cellulose",
    "other" ]
    }
    ]
    ```

    +++
-->
* **Exit Criteria**: Exit criteria, if triggered, would exit all instances of the profile live in the journey at that moment. It would not be contextual to the profile ID + supplemental identifier combination.

* **Frequency rules**: Each journey instance created from supplemental identifier usage counts towards frequency capping, even if a single event results in multiple journey instances.

* **Data type and schema structure**: The supplemental identifier must be of type `string`. It can be an independent string attribute or it can be a string attribute within an array of objects. The independent string attribute will result in a single journey instance, whereas the string attribute within an array of objects will result in a unique journey instance per iteration of the object array. String arrays and maps are not supported.

## Add a supplemental identifier and leverage it in a journey

To use a supplemental identifier in a journey, follow these steps:

1. **Mark the attribute as an identifier in the event schema**

    1. Access the event schema and locate the attribute you want to use as a supplemental identifier (e.g., booking ID, subscription ID) and mark it as an ID. [Learn how to work with schemas](../data/get-started-schemas.md)

    1. Mark the identifier as an **[!UICONTROL Identity]**.

        ![](assets/supplemental-ID-schema.png)

        >[!IMPORTANT]
        >
        >Make sure you do not mark the attribute as **Primary identity**.

    1. Select the namespace to associate with the supplemental ID. This must be a non-person identifier namespace.

1. **Add the supplemental ID to the event**

    1. Create or edit the desired event. [Learn how to configure a unitary event](../event/about-creating.md)

    1. In the event configuration screen, check the **[!UICONTROL Use supplemental identifier]** option.

        ![](assets/supplemental-ID-event.png)

    1. Use the expression editor to select the attribute you marked as the supplemental ID.

    1. After selecting the supplemental ID, the associated namespace is displayed in the event configuration screen as read-only.

1. **Add the event to the journey**

    Drag the configured event onto the journey canvas. It will trigger journey entry based on both the profile ID and the supplemental ID.

      ![](assets/supplemental-ID-journey.png)

1. **Leverage supplemental ID attributes**

    Use the expression editor and personalization editor to reference attributes of the supplemental identifier for personalization or conditional logic. Attributes are accessible from the **[!UICONTROL Contextual attributes]** menu.

      ![](assets/supplemental-ID-perso.png)

    >[!NOTE]
    >
    >If you are working with arrays (e.g., multiple prescriptions or policies), use a formula to extract specific elements.

    +++ See examples

    In an object array with the supplemental ID as `bookingNum and an attribute at the same level called `bookingCountry`, the journey will iterate through the array object based on the bookingNum and create a journey instance for each object.
    
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

1. **Publish the journey**

   Once configured, publish the journey to begin using multiple concurrent entries based on supplemental identifiers.

## Example use cases

### **Policy Renewal Notifications**

* **Scenario**: An insurance provider sends renewal reminders for each active policy held by a customer.
* **Execution**:
  * Profile: "John".
  * Supplemental IDs: `"AutoPolicy123", "HomePolicy456"`.
  * Journey executes separately for each policy, with personalized renewal dates, coverage details, and premium information.

### **Subscription Management**

* **Scenario**: A subscription service sends tailored messages for each subscription tied to a customer profile.
* **Execution**:
  * Profile: "Jane".
  * Supplemental IDs: `"Luma Yoga Program ", "Luma Fitness PlPrograman"`.
  * Journey executes separately for each subscription, with personalized renewal offers.

### **Product Recommendations**

* **Scenario**: An e-commerce platform sends recommendations based on specific products purchased by a customer.
* **Execution**:
  * Profile: "Alex".
  * Supplemental IDs: `"productID1234", "productID5678"`.
  * Journey executes separately for each product, with personalized upsell opportunities.
