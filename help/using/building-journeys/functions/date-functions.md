---
product: journey optimizer
title: Date functions
description: Learn about date functions
feature: Journeys
role: Developer
level: Experienced
keywords: date, functions, expression, journey, time
version: Journey Orchestration
---
# Date functions {#date-functions}

Date functions enable you to manipulate and work with date and time values within your journey expressions. These functions are essential for time-based conditions, scheduling, and temporal calculations in your customer journeys.

Use date functions when you need to:

* Get the current time or date with specific timezone handling ([now](#now), [nowWithDelta](#nowWithDelta), [currentTimeInMillis](#currentTimeInMillis))
* Check if a date falls within a specific time range ([inLastDays](#inLastDays), [inLastHours](#inLastHours), [inLastMonths](#inLastMonths), [inLastYears](#inLastYears), [inNextDays](#inNextDays), [inNextHours](#inNextHours), [inNextMonths](#inNextMonths), [inNextYears](#inNextYears))
* Modify date and time components ([setHours](#setHours), [setDays](#setDays), [updateTimeZone](#updateTimeZone))
* Perform time-based calculations and comparisons
* Convert between different time formats and representations

Date functions provide precise control over temporal logic, allowing you to create time-sensitive journey paths and conditions that respond to specific timeframes and schedules.

## currentTimeInMillis {#currentTimeInMillis}

Returns current time in epoch milliseconds.

+++Syntax

`currentTimeInMillis()`

+++

+++Parameters

This function uses no parameters.

+++

+++Signatures and returned type

`currentTimeInMillis()`

Returns an integer.

+++

+++Examples

`currentTimeInMillis()`

Returns "1544712617131".

+++

## inLastDays {#inLastDays}

Returns true if a given dateTime is between now and now - delta days.

+++Syntax

`inLastDays(<dateTime>,<delta>)`

+++

+++Parameters

| Parameter | Type             |
|-----------|------------------|
| date time | dateTime    |
| delta   | integer     |

+++

+++Signatures and returned type

`inLastDays(<dateTime>,<integer>)`

Returns a boolean.

+++

+++Examples

`inLastDays(toDateTime('2023-12-12T01:11:00Z'), 4)`

Returns true.

+++

## inLastHours {#inLastHours}

Returns true if the given date time is between now and now - delta hours.

+++Syntax

`inLastHours(<dateTime>,<delta>)`

+++

+++Parameters

| Parameter | Type             |
|-----------|------------------|
| date time | dateTime    |
| delta   | integer     |

+++

+++Signatures and returned type

`inLastHours(<dateTime>,<integer>)`

Returns a boolean.

+++

+++Examples

`inLastHours(toDateTime('2023-12-12T01:11:00Z'), 4)`

Returns true.

`inLastHours(@event{MyEvent.timestamp}, 4)`

Returns true.

+++

## inLastMonths {#inLastMonths}

Returns true if a given date or dateTime is between now and now - delta months.

+++Syntax

`inLastMonths(<dateTime>,<delta>)`

+++

+++Parameters

| Parameter | Type             |
|-----------|------------------|
| date time | dateTime    |
| delta   | integer     |

+++

+++Signatures and returned type

`inLastMonths(<dateTime>,<integer>)`

Returns a boolean.

+++

+++Examples

`inLastMonths(toDateTime('2023-12-12T01:11:00Z'), 4)`

Returns true.

+++

## inLastYears {#inLastYears}

Returns true if a given date or dateTime is between now and now - delta years.

+++Syntax

`inLastYears(<dateTime>,<delta>)`

+++

+++Parameters

| Parameter | Type             |
|-----------|------------------|
| date time | dateTime    |
| delta   | integer     |

+++

+++Signatures and returned type

`inLastYears(<dateTime>,<integer>)`

Returns a boolean.

+++

+++Examples

`inLastYears(toDateTime('2023-12-12T01:11:00Z'), 4)`

Returns true.

+++

## inNextDays {#inNextDays}

Returns true if a given date or dateTime is between now and now + delta days.

+++Syntax

`inNextDays(<dateTime>,<delta>)`

+++

+++Parameters

| Parameter | Type             |
|-----------|------------------|
| date time | dateTime    |
| delta   | integer     |

+++

+++Signatures and returned type

`inNextDays(<dateTime>,<integer>)`

Returns a boolean.

+++

+++Examples

`inNextDays(toDateTime('2023-12-12T01:11:00Z'), 4)`

Returns true.

+++

## inNextHours {#inNextHours}

Returns true if a given date or dateTime is between now and now + delta hours.

+++Syntax

`inNextHours(<dateTime>,<delta>)`

+++

+++Parameters

| Parameter | Type             |
|-----------|------------------|
| date time | dateTime    |
| delta   | integer     |

+++

+++Signatures and returned type

`inNextHours(<dateTime>,<integer>)`

Returns a boolean.

+++

+++Examples

`inNextHours(toDateTime('2023-12-12T01:11:00Z'), 4)`

Returns true.

+++

## inNextMonths {#inNextMonths}

Returns true if a given date or dateTime is between now and now + delta months.

+++Syntax

`inNextMonths(<dateTime>,<delta>)`

+++

+++Parameters

| Parameter | Type             |
|-----------|------------------|
| date time | dateTime    |
| delta   | integer     |

+++

+++Signatures and returned type

`inNextMonths(<dateTime>,<integer>)`

Returns a boolean.

+++

+++Examples

`inNextMonths(toDateTime('2023-01-12T01:11:00Z'), 4)`

Returns true.

+++

## inNextYears {#inNextYears}

Returns true if a given date or dateTime is between now and now + delta years.

+++Syntax

`inNextYears(<dateTime>,<delta>)`

+++

+++Parameters

| Parameter | Type             |
|-----------|------------------|
| date time | dateTime    |
| delta   | integer     |

+++

+++Signatures and returned type

`inNextYears(<dateTime>,<integer>)`

Returns a boolean.

+++

+++Examples

`inNextYears(toDateTime('2021-12-12T01:11:00Z'), 4)`

Returns true.

+++

## now {#now}

Returns the current date in date time format. For more information on data types, refer to [this page](../expression/data-types.md).

+++Syntax

`now(<parameter>)`

+++

+++Parameters

|Parameter|Description|
|--- |--- |
|string|Time zone identifier (optional)|

+++

+++Signatures and returned type

`now()`

`now("<timeZone id>")`

Returns a dateTime.

+++

+++Examples

`now()`

Returns 2023-06-03T06:30Z.

`toString(now())`

Returns "2023-06-03T06:30Z"

`now("Europe/Paris")`

Returns 2023-06-03T08:30+02:00.

+++

## nowWithDelta {#nowWithDelta}

Returns the current datetime including an offset. If a time zone id is specified, the time zone offset will be applied. For more information on data types, refer to [this page](../expression/data-types.md).

+++Syntax

`nowWithDelta(<parameters>)`

+++

+++Parameters

|Parameter|Description|
|--- |--- |
|delta|positive or negative integer value|
|date part|years, months, days, hours, minutes or seconds as a string|
|time zone id|string representation of the time zone value. For more, see [Data types](../expression/data-types.md). Time zone id must be a string constant. It cannot be a field reference nor an expression.|

+++

+++Signatures and returned type

`nowWithDelta(<delta>,<date part>`

`nowWithDelta(<delta>,<date part>,"<timeZone id>")`

Returns a dateTime.

+++

+++Examples

`nowWithDelta(-2, "hours")`

`nowWithDelta(-2, "hours", "Europe/Paris")`

Returns a dateTime exactly 2 hours ago.

+++

## setHours {#setHours}

Sets the hours of a date time or date time only. For example, if you want to wait until a certain hour tomorrow, you can force the hour.

+++Syntax

`setHours(<parameter>)`

+++

+++Parameters

|Parameter|Type|
|--- |--- |
|date time|dateTime|
|date time without considering time zone|dateTimeOnly|
|hours|integer|

+++

+++Signatures and returned type

`setHours(<dateTime>,<hours>)`

Returns a datetime.

`setHours(<dateTimeOnly>,<hours>)`

Returns a datetime without considering time zone.

+++

+++Examples

`setHours(toDateTime('2023-12-12T01:11:00Z'), 4)`

Returns 2023-12-12T04:11:00Z.

`setHours(nowWithDelta(1, "days"), 20)`

Returns tomorrow at 8:XY PM, XY being the minutes at the moment of the current time evaluation. If the evaluation happens at 2:45 AM, the returned time will be 8:45 PM.

+++

## setDays {#setDays}

Sets the day of a date time or date time only. For example, if you want to wait until a certain day of the month, you can force the day.

+++Syntax

`setDays(<parameter>)`

+++

+++Parameters

|Parameter|Type|
|--- |--- |
|date time|dateTime|
|date time without considering time zone|dateTimeOnly|
|days|integer|

+++

+++Signatures and returned type

`setDays(<dateTime>,<days>)`

Returns a datetime.

`setDays(<dateTimeOnly>,<days>)`

Returns a datetime without considering time zone.

+++

+++Examples

`setDays(toDateTime('2023-12-12T01:11:00Z'), 25)`

Returns 2023-12-25T01:11:00Z.

`setDays(toDateTimeOnly(@event{MyEvent.registrationDate}), 1)`

+++

## updateTimeZone {#updateTimeZone}

Returns a new date time, with a new time zone on the same instant.

+++Syntax

`updateTimeZone(<parameters>)`

+++

+++Parameters

* time zone id: string
* dateTime

+++

+++Signature and returned type

`updateTimeZone(<dateTime>,<timeZone id>)`

Returns a datetime.

+++

+++Examples

`updateTimeZone( toDateTime("2023-08-28T08:15:30.123-07:00"), "Europe/Paris"))`

Returns 2023-08-28T17:15:30.123+02:00.

`updateTimeZone(@event{MyExpEvent.timestamp}, "Australia/Sydney")`

If the value of the timestamp field is `2021-11-16T16:55:12.939318+01:00`, then the function returns `2021-11-17T02:55:12.942115+11:00`.

+++

