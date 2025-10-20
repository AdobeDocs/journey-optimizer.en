---
product: journey optimizer
title: filter
description: Learn about the function filter
feature: Journeys
role: Engineer
level: Experienced
keywords: filter, function, expression, journey
exl-id: 05e3d2ba-1a27-4f27-88cc-3d83eb3b14af
version: Journey Orchestration
---
# filter{#filter}

Returns a listObject with objects having the key attribute matching one of the given key values.

## Category

List

## Function syntax

`filter(<parameters>)`

## Parameters

| Parameter | Type             | Description             |
|-----------|------------------|------------------|
| listToFilter | listObject | list of objects, to be filtered. It must be a field reference. |
| keyAttributeName | string | attribute name in the objects of the given list, used as key for filtering |
| keyValueList | list | array of key values for filtering |

## Signatures and returned types

`filter(listObject, string, listString)`

`filter(listObject, string, listInteger)`

`filter(listObject, string, listDecimal)`

`filter(listObject, string, listDateTime)`

`filter(listObject, string, listDateTimeOnly)`

`filter(listObject, string, listDateOnly)`

`filter(listObject, string, listDuration)`

`filter(listObject, string, listBoolean)`

Returns a listObject.

## Examples

Here is an example of a payload passed in an incoming event "myevent":

```json
"productListItems": [{
   "id": "product1",
   "name": "the product 1",
   "price": 20
},{
   "id": "product2",
   "name": "the product 2",
   "price": 30
},{
   "id": "product3",
   "name": "the product 3",
   "price": 50
}]
```

You can use the following expression:

```json
filter(
 @event{myevent.productListItems},
 "id", 
 ["product2", "product3", "product4"]
)
```

Returns a listObject containing the two objects with "product2" and "product3" as id.
