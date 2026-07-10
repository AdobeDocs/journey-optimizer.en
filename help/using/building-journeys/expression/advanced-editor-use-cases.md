---
solution: Journey Optimizer
product: journey optimizer
title: Using the advanced expression editor
description: Learn how to build advanced expressions
feature: Journeys
role: Developer
level: Experienced
hide: true
keywords: expression, condition, use-cases, events
exl-id: 753ef9f4-b39d-4de3-98ca-e69a1766a78b
version: Journey Orchestration
TQID: https://experienceleague.adobe.com/UUeCcATC7MFHsLuI8TPoVHqwVe9GOXUq3U3RoAG-a1o
product_v2:
  - id: cb954087-f4fc-4456-afb9-e939cabcdc79
    internal-label: Journey Optimizer
feature_v2:
  - id: d998adac-2f81-400b-a669-d07bb196e4eb
    internal-label: Journeys
  - id: df64005d-8f9a-422e-ba4d-c6f6dc3454b4
    internal-label: Use cases
subfeature_v2:
  - id: fa683eda-48de-4558-af32-2673edcd44fe
    internal-label: Events
role_v2:
  - id: ff6a42d2-313e-452e-93a6-792e4fad9ff8
    internal-label: Developer
topic_v2:
  - id: e0eb8757-182f-49f3-94a4-1587d16f5094
    internal-label: Personalization
---
# Advanced expression examples{#advanced-expression-examples}

The Advanced expression editor can be used to create conditions to allow you to filter users in your journeys. These conditions enable you to target users on time, date, location, duration, so that they can be retargeted in the journey.

>[!CAUTION]
>
>Using experience events in journey expressions/conditions is not supported. If your use case requires the use of experience events, consider alternative methods. [Learn more](../exp-event-lookup.md)


## Building conditions on Experience Events


>[!CAUTION]
>
>Using experience events in journey expressions/conditions is not supported. If your use case requires the use of experience events, consider alternative methods. [Learn more](../exp-event-lookup.md)
>



The advanced expression editor is mandatory to perform queries on time series such as a list of purchases or past clicks on messages. Such queries cannot be performed using the simple editor.

>[!NOTE]
>
>Events starts with @, data sources with #.

The experience events are retrieved from Adobe Experience Platform as a collection in reverse chronological order, hence:

* first function will return the most recent event
* last function will return the oldest one.

For example, let's say you want to target customers with a cart abandonment in the last 7 days to send a message when the customer is getting near a store, with an offer on items they wanted that are in store.

**You need to build the following conditions:**

First of all, target customers who browsed the online store but did not finalize order in the last 7 days.

**This expression looks for a specified value in a string value:**

`In ("addToCart", #{field reference from experience event})`

**This expression looks for all events for this user specified in the last 7 days:**

Then it selects all the add to cart events that did not transform into a completePurchase.

>[!NOTE]
>
>To insert fields in the expression quickly, double-click the field in the left panel of the editor.

The specified timestamp is acting as the date time value, the second is number of days.

```json
        in( "addToCart", #{ExperiencePlatformDataSource
                        .ExperienceEventFieldGroup
                        .experienceevent
                        .all(
                        inLastDays(currentDataPackField.timestamp, 7 ))
                        .productData
                        .productInteraction})
        and
        not(in( "completePurchase", #{ExperiencePlatformDataSource
                        .ExperienceEventFieldGroup
                        .experienceevent
                        .all(
                        inLastDays(currentDataPackField.timestamp, 7 ))
                        .productData
                        .productInteraction}))
```

This expression returns a boolean.

**Now let's build an expression checking that the product is in stock**

* In Inventory, this expression looks for quantity field of a product and specify that it should be greater than 0.

`#{Inventory.fieldgroup3.quantity} > 0`

* At the right, the necessary values are specified, here, we need to retrieve the location of the store, that is mapped from the location of the event "ArriveLumaStudio":

 `#{ArriveLumaStudio._acpevangelists1.location.location}`

* And specify SKU, using the function `first` to retrieve the most recent "addToCart" interaction:  

    ```json
        #{ExperiencePlatformDataSource
                        .ExperienceEventFieldGroup
                        .experienceevent
                        .first(
                        currentDataPackField
                        .productData
                        .productInteraction == "addToCart"
                        )
                        .SKU}
    ```

From there you can add another path in your journey for when the product is not in store and send notification with engagement offer. Configure messages accordingly and use personalization data to enhance the message target.

## Timestamp filtering in expressions

When referencing multiple cart activity events, specify both a start and end timestamp window to avoid picking up historical data. For instance:

```json
toDateTimeOnly(currentDataPackField.timestamp) >= toDateTimeOnly(@event{poc_UDXCartAddSavedCheckOutEv.timestamp})
AND
toDateTimeOnly(currentDataPackField.timestamp) < toDateTimeOnly(nowWithDelta(4, "hours"))
```

## Examples of string manipulations with the advanced expression editor

**In conditions**

This condition retrieves only the geofence events triggered in "Arlington":

```json
        @event{GeofenceEntry
                    .placeContext
                    .POIinteraction
                    .POIDetail
                    .name} == "Arlington"
```

Explanation: This is a strict string comparison (case sensitive), equivalent to a query in simple mode that uses `equal to` with `Is sensitive` checked.

The same query with `Is sensitive` unchecked will generate the following expression in advanced mode:

```json
        equalIgnoreCase(@event{GeofenceEntry
                        .placeContext
                        .POIinteraction
                        .POIDetail
                        .name}, "Arlington")
```

**In actions**

The following expression allows you to define the CRM ID in an action personalization field:

```json
substr(
   @event{MobileAppLaunch
   ._myorganization
   .identification
   .crmid},
   1, 
   lastIndexOf(
     @event{MobileAppLaunch
     ._myorganization
     .identification
     .crmid},
     '}'
   )
)
```

Explanation: This example uses `substr` and `lastIndexOf` functions to remove curly braces that enclose the CRM ID passed with a mobile app launch event.


For more on how to use the advanced expression editor, watch [this video](https://experienceleague.adobe.com/docs/journey-optimizer-learn/tutorials/create-journeys/introduction-to-building-a-journey.html).

+++ AI Knowledge Reference

This section contains structured knowledge intended to support interpretation, retrieval, and question answering related to this topic.

For complete understanding, this information should be combined with the documentation on this page. Neither source is intended to stand alone; the page describes the feature, while this section provides additional context that helps disambiguate terminology, intent, applicability, and constraints.

* **TL;DR:** This page provides practical examples of using the advanced expression editor to build journey conditions that filter users by cart activity, inventory status, geofence events, string manipulations, and timestamp windows.

**Intents:**

* Build a cart abandonment condition using `in()` and `inLastDays()` to target users who added items but did not complete purchase within 7 days
* Filter experience event collections by timestamp window to avoid capturing historical data
* Apply case-sensitive and case-insensitive string comparisons to geofence event fields
* Extract and manipulate CRM IDs from mobile app launch events using `substr` and `lastIndexOf`
* Check product inventory availability by comparing a quantity field against a threshold
* Combine multiple boolean expressions using `and` / `not` logic in journey conditions

**Glossary:**

* **Advanced expression editor**: The Journey Optimizer interface for writing complex, code-level expressions using functions, operators, and field references *(product-specific)*
* **currentDataPackField**: A loop variable used when iterating over data source collections inside `all()`, `first()`, or `last()` functions *(product-specific)*
* **inLastDays(timestamp, N)**: A date function that returns true if the given timestamp falls within the last N days *(product-specific)*
* **Experience Events**: Time-series behavioral data records stored in Adobe Experience Platform, retrieved in reverse chronological order *(product-specific)*

**Guardrails:**

* Using experience events directly in journey expressions/conditions is not supported; alternative methods such as computed attributes or audience segments should be used instead
* The advanced expression editor must be used (not the simple editor) for queries on time-series data such as collections of purchases or clicks
* Double-clicking a field in the left panel inserts it into the expression quickly; avoid typing field paths manually to reduce errors
* Expressions querying experience events return a boolean; ensure downstream logic expects a boolean type

**Terminology:**

* Canonical name: Advanced Expression Editor — Acronym: none — variants: expression editor, advanced editor
* Synonyms: "addToCart" = "add to cart interaction"; "completePurchase" = "purchase completion event"
* Do not confuse: events (prefixed with `@`) ≠ data sources (prefixed with `#`)

**FAQ:**

* **Q: Why must I use the advanced editor instead of the simple editor for cart abandonment queries?** — The simple editor cannot perform queries on time-series collections; the advanced editor is required for `all()`, `first()`, and `last()` collection functions.
* **Q: How do I reference the most recent "addToCart" event in an expression?** — Use the `first()` function on the experience event collection filtered by `productInteraction == "addToCart"`, since events are returned in reverse chronological order.
* **Q: How do I make a string comparison case-insensitive in the advanced editor?** — Use the `equalIgnoreCase()` function instead of the `==` operator.
* **Q: What is the purpose of adding a timestamp window when querying cart events?** — Specifying both a start and end timestamp prevents picking up historical data that falls outside the intended activity window.
* **Q: How do I remove curly braces from a CRM ID string passed in an event?** — Use `substr()` combined with `lastIndexOf()` to extract the content between the braces.

+++
