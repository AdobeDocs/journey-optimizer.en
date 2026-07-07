---
solution: Journey Optimizer
product: journey optimizer
title: Collection management functions
description: Learn about data types in collection management functions
feature: Journeys
hide: true
role: Developer
level: Experienced
keywords: query, collections, functions, payload, journey
version: Journey Orchestration
feature_v2: []
subfeature_v2: []
---
# Collection management functions 

The expression language also introduces a set of functions to query collections.

These functions are explained below. In the following example, let's use the event payload containing a collection:

```json
                { 
   "_experience":{ 
      "campaign":{ 
         "message":{ 
            "profile":{ 
               "pushNotificationTokens":[ 
                  { 
                     "token":"token_1",
                     "application":{ 
                        "_id":"APP1",
                        "name":"MarltonMobileApp",
                        "version":"1.0"
                     }
                  },
                  { 
                     "token":"token_2",
                     "application":{ 
                        "_id":"APP2",
                        "name":"MarketplaceApp",
                        "version":"1.0"
                     }
                  },
                  { 
                     "token":"token_3",
                     "application":{ 
                        "_id":"APP3",
                        "name":"VendorApp",
                        "version":"2.0"
                     }
                  }
               ]
            }
         }
      }
   },
   "timestamp":"1536160728"
}
```

**The function "all(`<condition>`)"**

The **[!UICONTROL all]** function enables the definition of a filter on a given collection by using a boolean expression.

   ```json
   <listExpression>.all(<condition>)
   ```

For example, among all the app users, you can get the ones using IOS 13 (boolean expression "app used == IOS 13"). The result of this function is the filtered list containing items matching the boolean expression (example: app user 1, app user 34, app user 432).

In a Data Source Condition activity you can check if the result of the **[!UICONTROL all]** function is null or not. You can also combine this **[!UICONTROL all]** function with other functions such as **[!UICONTROL count]**. For more information, see [Data Source Condition activity](../conditions.md#data_source_condition).


## Examples

>[!CAUTION]
>
>Using experience events in journey expressions/conditions is supported but not recommended. If your use case requires the use of experience events, consider alternative methods such as [computed attributes](../../audience/computed-attributes.md), or creating a segment using the events and incorporating that segment into [`inAudience` expressions](../../building-journeys/functions/functioninaudience.md).

**Example 1:**

We want to check if a user has installed a specific version of an application. For this we get all the push notification tokens associated with mobile applications for which the version is 1.0. Then, we perform a condition with the **[!UICONTROL count]** function to check that the returned list of tokens contains at least one element.

   ```json
   count(@event{LobbyBeacon._experience.campaign.message.profile.pushNotificationTokens.all(currentEventField.application.version == "1.0").token}) > 0
   ```

The result is true.

**Example 2:**

Here we use the **[!UICONTROL count]** function to check if there are push notification tokens in the collection.

   ```json
   count(@event{LobbyBeacon._experience.campaign.message.profile.pushNotificationTokens.all().token}) > 0
   ```

The result will be true.

<!--
Alternatively, you can check if there is no token in the collection:

   ```json
   count(@event{LobbyBeacon._experience.campaign.message.profile.pushNotificationTokens.all().token}) == 0
   ```

The result will be false.

Here we use the count function in a condition to count the number of push notification tokens in the event.

`count(@event{LobbyBeacon._experience.campaign.message.profile.pushNotificationTokens.all().token})`

The result is true.

Note that when the condition in the **all()** function is empty, the filter will return all the elements in the list. Hence, the expression above is equivalent to:

`count(@event{LobbyBeacon._experience.campaign.message.profile.pushNotificationTokens.application.name})`

In both cases, the result of the expression is **3**.

A query of experience events recorded on the Adobe Experience Platform may or may not include the current event that triggered the current Journey. This will depend on the relative processing time with which [!DNL Journey Orchestration] sees an event and started evaluating conditions, versus the time it takes for that event to be ingested into the Adobe Experience Platform. For example, when using the .all() syntax to query experience events from the Adobe Experience Platform, we recommend enforcing the exclusion of the current event (by requiring an
earlier timestamp) in order to only consider prior events.
-->

   >[!NOTE]
   >
   >When the filtering condition in the **all()** function is empty, the filter will return all the elements in the list. **However, in order to count the number of elements of a collection, the all function is not required.**


   ```json
   count(@event{LobbyBeacon._experience.campaign.message.profile.pushNotificationTokens.token})
   ```

   The result of the expression is **3**.

**Example 3:**

Here we check if an individual has not received any communication within the last 24 hours. We filter the collection of experience events retrieved from the ExperiencePlatform datasource, using two expressions based on two elements of the collection. In particular, the timestamp of the event is compared to the dateTime returned by the **[!UICONTROL nowWithDelta]** function.

```json
count(#{ExperiencePlatform.MarltonExperience.experienceevent.all(
   currentDataPackField.directMarketing.sends.value > 0 and
   currentDataPackField.timestamp > nowWithDelta(-1, "days")).timestamp}) == 0
```

The result will be true if there is no experience event matching the two conditions.

**Example 4:**

Here we want to check if an individual has launched at least once an application in the last 7 days, in order for instance to trigger a push notification inviting them to start a tutorial.

```json
count(
 #{ExperiencePlatform.AnalyticsData.experienceevent.all(
 nowWithDelta(-7,"days") <= currentDataPackField.timestamp
 and currentDataPackField.application.firstLaunches.value > 0
)._id}) > 0
```

<!--
**"All + Count" example 4:** here we use the count function in a boolean expression to see if there is push notification tokens in the collection.

`count(@event{LobbyBeacon._experience.campaign.message.profile.pushNotificationTokens.all().application.name}) > 0`

The result will be:

`true`

Alternatively, you can check if there is NO token in the collection:

`count(@event{LobbyBeacon._experience.campaign.message.profile.pushNotificationTokens.all().application.name}) =0`

The result will be:

`false`
-->

>[!NOTE]
>
>**[!UICONTROL currentEventField]** is only available when manipulating event collections, **[!UICONTROL currentDataPackField]** when manipulating data source collections and **[!UICONTROL currentActionField]** when manipulating custom action response collections.
>
>When processing collections with **[!UICONTROL all]**, **[!UICONTROL first]** and **[!UICONTROL last]**, we loop on each element of the collection one by one. **[!UICONTROL currentEventField]**, **currentDataPackField** and **[!UICONTROL currentActionField]** correspond to the element being looped.

**The functions "first(`<condition>`)" and "last(`<condition>`)"**

The **[!UICONTROL first]** and **[!UICONTROL last]** functions also enable the definition of a filter on the collection while returning the first/last element of the list that meets the filter.

_`<listExpression>.first(<condition>)`_

_`<listExpression>.last(<condition>)`_

**Example 1:** 

This expression returns the first push notification token associated with mobile applications for which the version is 1.0.

   ```json
   @event{LobbyBeacon._experience.campaign.message.profile.pushNotificationTokens.first(currentEventField.application.version == "1.0").token
   ```

The result is "token_1".

**Example 2:** 

This expression returns the last push notification token associated with mobile applications for which the version is 1.0.

   ```json
   @event{LobbyBeacon._experience.campaign.message.profile.pushNotificationTokens.last(currentEventField.application.version == "1.0").token}
   ```

   The result is "token_2".

   >[!NOTE]
   >
   >The experience events are retrieved from Adobe Experience Platform as a collection in reverse chronological order, hence :
   >
   >* **[!UICONTROL first]** function will return the most recent event
   >* **[!UICONTROL last]** function will return the oldest one.

**Example 3:**

We check whether the first (most recent) Adobe Analytics event with a non-zero value for DMA ID has a value equal to 602.

   ```json
   #{ExperiencePlatform.AnalyticsProd_EvarsProps.experienceevent.first(
   currentDataPackField.placeContext.geo.dmaID > 0).placeContext.geo.dmaID} == 602
   ```

**The function "at(`<index>`)"**

The **[!UICONTROL at]** function allows you to reference a specific element in a collection according to an index.
Index 0 is the first index of the collection. 

_`<listExpression>`.at(`<index>`)_

**Example:** 

This expression returns the second push notification token of the list.

   ```json
   @event{LobbyBeacon._experience.campaign.message.profile.pushNotificationTokens.at(1).token}
   ```

The result is "token_2".

**Other examples**

This expression returns the product names based on the SKU value. The list of these products is included in the events list, with the condition being the event ID.

```json
#{ExperiencePlatform.ExperienceEventFieldGroup.experienceevent.all(currentDataPackField._aepgdcdevenablement2.purchase_event.receipt_nbr == "10-337-4016"). 
_aepgdcdevenablement2.purchase_event.productListItems.all(currentDataPackField.SKU == "AB17 1234 1775 19DT B4DR 8HDK 762").name}
```

This expression retrieves the name of the last product in the product list of a commerce event where the event type is 'productListAdds' and the total price is greater than or equal to 150.

```json
 #{ExperiencePlatform.ExperienceEventFieldGroup.experienceevent.last(
currentDataPackField.eventType == "commerce.productListAdds").productListItems.last(currentDataPackField.priceTotal >= 150).name}
```

+++ AI Knowledge Reference

This section contains structured knowledge intended to support interpretation, retrieval, and question answering related to this topic.

For complete understanding, this information should be combined with the documentation on this page. Neither source is intended to stand alone; the page describes the feature, while this section provides additional context that helps disambiguate terminology, intent, applicability, and constraints.

* **TL;DR:** This page explains the collection management functions `all()`, `first()`, `last()`, and `at()` available in the Journey expression language, with examples using push notification token payloads and experience event data.

**Intents:**

* Filter a collection using a boolean condition with `all(<condition>)` to retrieve matching elements
* Count elements in a collection using the `count()` function combined with `all()`
* Retrieve the first or last element of a filtered collection using `first()` or `last()`
* Access a specific element in a collection by index using `at(<index>)`
* Combine nested collection queries to look up product names by SKU or by event type and price threshold

**Glossary:**

* **all(condition)**: Collection function that filters a list and returns items matching the given boolean expression *(product-specific)*
* **first(condition)**: Collection function that returns the first (most recent, for experience events) element matching the condition *(product-specific)*
* **last(condition)**: Collection function that returns the last (oldest, for experience events) element matching the condition *(product-specific)*
* **at(index)**: Collection function that returns the element at a specific zero-based index *(product-specific)*
* **currentEventField**: Loop variable available when iterating over event collections inside `all()`, `first()`, or `last()` *(product-specific)*
* **currentDataPackField**: Loop variable available when iterating over data source collections *(product-specific)*
* **currentActionField**: Loop variable available when iterating over custom action response collections *(product-specific)*

**Guardrails:**

* Using experience events in journey expressions/conditions is supported but not recommended; consider computed attributes or audience segments as alternatives
* `currentEventField` is only available for event collections; `currentDataPackField` for data source collections; `currentActionField` for custom action response collections
* The `all` function is not required to count elements of a collection — `count()` can be applied directly to the collection field
* Experience events are retrieved in reverse chronological order: `first()` returns the most recent event, `last()` returns the oldest

**Terminology:**

* Canonical name: Collection Management Functions — Acronym: none — variants: collection functions, query collection functions
* Synonyms: "all()" = "filter function"; "first()" = "most recent element function" (for experience events)
* Do not confuse: `first()` (most recent experience event) ≠ first element by insertion order

**FAQ:**

* **Q: What does `all()` return when the condition is empty?** — It returns all elements in the list, equivalent to no filtering.
* **Q: How do I count the number of push notification tokens in a collection?** — Use `count()` directly on the token field path without requiring `all()`, e.g. `count(@event{...pushNotificationTokens.token})`.
* **Q: How do I get the second element of a collection?** — Use `at(1)` since index 0 is the first element.
* **Q: Why does `first()` return the most recent experience event?** — Experience events are retrieved from Adobe Experience Platform in reverse chronological order, so `first()` picks the top (newest) item.
* **Q: How do I check if a user has not received any communication in the last 24 hours?** — Filter the experience event collection with `nowWithDelta(-1, "days")` as a timestamp lower bound and use `count(...) == 0`.

+++
