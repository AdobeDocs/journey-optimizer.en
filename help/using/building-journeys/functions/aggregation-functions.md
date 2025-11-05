---
product: journey optimizer
title: Aggregation functions
description: Learn about aggregation functions
feature: Journeys
role: Developer
level: Experienced
keywords: aggregation, functions, expression, journey, avg, count, max, min, sum
version: Journey Orchestration
---
# Aggregation functions {#aggregation-functions}

Aggregation functions perform calculations on a set of values and return a single summarized result. These functions enable you to analyze data within your journey expressions by calculating averages, finding minimum and maximum values, counting elements, and summing numeric values.

Use aggregation functions when you need to:

* Calculate statistical values from lists or arrays (average, sum, min, max)
* Count elements in collections, with options to include or exclude null values
* Determine unique values within data sets
* Make data-driven decisions based on computed metrics

Aggregation functions automatically handle null values according to their specific behavior, making it easier to work with real-world data that may contain missing or undefined values.


## avg {#avg}

Returns the average value among a set of expressions, given either as a list or two expressions. Null values are ignored.

+++Syntax

`avg(<parameter>)`

+++

+++Parameters

Supported types:

* listInteger
* listDecimal
* decimal
* integer

+++

+++Signatures and returned type

`avg(<listInteger>)`

`avg(<listDecimal>)`

`avg(<decimal>,<decimal>)`

`avg(<decimal>,<integer>)`

`avg(<integer>,<decimal>)`

`avg(<integer>,<integer>)`

Returns a decimal.

+++

+++Examples

`avg(@event{BarBeacon.inventory},5)`

`avg([10,3,8])`

Returns 7.0.

`avg(10.2, 3)`

Returns 6.6.

+++

## count {#count}

Counts the elements of the list not taking into account the null values.

+++Syntax

`count(<listAny>)`

`count(<listObject>)`

+++

+++Parameters

| Parameter | Type             | Description             |
|-----------|------------------|------------------|
| listToProcess | listString, listBoolean, listInteger, listDecimal, listDuration, listDateTime, listDateTimeOnly, listDateOnly, or listObject | List to process. For listObject, it must be a field reference. A listObject cannot contain null object. |

+++

+++Signatures and returned type

`count(<listAny>)`

Returns an integer.

+++

+++Examples

`count([10,2,10,null])`

Returns 3.

`count(@event{my_event.productListItems})`

Returns the number of objects in the given array of objects (listObject type). Remark: a listObject cannot contain null object

+++

## countOnlyNull {#countOnlyNull}

Counts the number of null values in the list.

+++Syntax

`countOnlyNull(<listAny>)`

+++

+++Parameters

| Parameter | Type             |
|-----------|------------------|
| listToProcess | listString, listBoolean, listInteger, listDecimal, listDuration, listDateTime, listDateTimeOnly, listDateOnly|

+++

+++Signatures and returned type

`countOnlyNull(<listAny>)`

Returns an integer.

+++

+++Examples

`countOnlyNull([10,2,10,null])`

Returns 1.

+++

**Note:** The parameter `<listObject>` is not supported in this function.

## countWithNull {#countWithNull}

Counts all the elements of the list including null values.

+++Syntax

`countWithNull(<listAny>)`

+++

+++Parameters

| Parameter | Type             |
|-----------|------------------|
| listToProcess | listString, listBoolean, listInteger, listDecimal, listDuration, listDateTime, listDateTimeOnly, listDateOnly|

+++

+++Signatures and returned type

`countWithNull(<listAny>)`

Returns an integer.

+++

+++Examples

`countWithNull([10,2,10,null])`

Returns 4.

+++

**Note:** The parameter `<listObject>` is not supported in this function.

## distinctCount {#distinctCount}

Counts the number of different values ignoring the null values.

+++Syntax

`distinctCount(<listAny>)`

+++

+++Parameters

| Parameter | Type             | Description             |
|-----------|------------------|------------------|
| listToProcess | listString, listBoolean, listInteger, listDecimal, listDuration, listDateTime, listDateTimeOnly, listDateOnly, or listObject | List to process. For listObject, it must be a field reference. |
| keyAttributeName | string | This parameter is optional and only for listObject. If the parameter is not provided, an object is considered as duplicated if all the attributes have the same values. Otherwise, an object is considered as duplicated if the given attribute has the same value. |

+++

+++Signatures and returned type

`distinctCount(<listAny>)`

Returns an integer.

`distinctCount(<listObject>)`

`distinctCount(<listObject>,<string>)`

Returns a list of objects.

+++

+++Examples

`distinctCount([10,2,10,null])`

Returns 2.

`distinctCount(@event{my_event.productListItems})`

Returns the number of strictly distinct objects in the given array of objects (listObject type).

`distinctCount(@event{my_event.productListItems}, "SKU")`

Returns the number of objects which have a distinct "SKU" attribute value{}.

+++

## distinctCountWithNull {#distinctCountWithNull}

Counts the number of different values including the null values.

+++Syntax

`distinctCountWithNull(<listAny>)`

+++

+++Parameters

| Parameter | Type             |
|-----------|------------------|
| listToProcess | listString, listBoolean, listInteger, listDecimal, listDuration, listDateTime, listDateTimeOnly, listDateOnly|

+++

+++Signatures and returned type

`distinctCountWithNull(<listAny>)`

Returns an integer.

+++

+++Examples

`distinctCountWithNull([10,2,10,null])`

Returns 3.

+++

**Note:** The parameter `<listObject>` is not supported in this function.

## max {#max}

Returns the maximum value among a set of expressions, given either as a list or two expressions. Null values are ignored.

+++Syntax

`max(<parameter>)`

+++

+++Parameters

* listDuration
* listInteger
* listDecimal
* listDateTime
* listDateTimeOnly
* listDateOnly
* duration
* integer
* decimal
* dateTime
* dateTimeOnly

+++

+++Signatures and returned types

`max(<listDuration>)`

Returns a duration.

`max(<listInteger>)`

Returns a duration.

`max(<listDateTimeOnly>)`

Returns a datetime without considering time zone.

`max(<listDateTime>)`

Returns a datetime.

`max(<listDateOnly>)`

Returns a date.

`max(<listDecimal>)`

Returns a decimal.

`max(<decimal>,<decimal>)`

Returns a decimal.

`max(<duration>,<duration>)`

Returns a duration.

`max(<dateTime>,<dateTime>)`

Returns a datetime.

`max(<dateTimeOnly>,<dateTimeOnly>)`

Returns a datetime without considering time zone.

`max(<integer>,<integer>)`

Returns an integer.

+++

+++Examples

`max(@event{BarBeacon.inventory},5)`

`max([10,3,8])`

Returns 10.

`max([10,null,8])`

Returns 10.

+++

## min {#min}

Returns the minimum value among a set of expressions, given either as a list or two expressions. Null values are ignored.

+++Syntax

`min(<parameters>)`

+++

+++Parameters

* listDuration
* listInteger
* listDecimal
* listDateTime
* listDateTimeOnly
* listDateOnly
* duration
* integer
* decimal
* dateTime
* dateTimeOnly

+++

+++Signatures and returned types

`min(<listDuration>)`

Returns a duration.

`min(<listInteger>)`

Returns a duration.

`min(<listDateTimeOnly>)`

Returns a datetime without considering time zone.

`min(<listDateTime>)`

Returns a datetime.

`min(<listDateOnly>)`

Returns a date.

`min(<listDecimal>)`

Returns a decimal.

`min(<decimal>,<decimal>)`

Returns a decimal.

`min(<duration>,<duration>)`

Returns a duration.

`min(<dateTime>,<dateTime>)`

Returns a datetime.

`min(<dateTimeOnly>,<dateTimeOnly>)`

Returns a datetime without considering time zone.

`min(<integer>,<integer>)`

Returns an integer.

+++

+++Examples

`min(@event{BarBeacon.inventory},5)`

`min([10,3,8])`

Returns 3.

`min([10,null,8])`

Returns 8.

+++

## sum {#sum}

Returns the sum of the values of a set of expressions. Null values are ignored.

+++Syntax

`sum(<parameters>)`

+++

+++Parameters

* listInteger
* listDecimal
* duration
* integer
* decimal

+++

+++Signatures and returned types

`sum(<listDecimal>)`

Returns a decimal.

`sum(<listInteger>)`

Returns an integer.

`sum(<integer>,<integer>)`

Returns an integer.

`sum(<decimal>,<decimal>)`

Returns a decimal.

+++

+++Examples

`sum(@event{BarBeacon.inventory},5)`

`sum([10,3,8])`

Returns 21.

`sum([10.5,null,8.1])`

Returns 18.6.

+++
