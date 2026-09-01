---
product: journey optimizer
title: Date functions
description: Learn about date functions
feature: Journeys
role: Developer
level: Experienced
keywords: date, functions, expression, journey, time
version: Journey Orchestration
exl-id: 68c102c1-f1c7-44b7-893f-9a3b7e0854b6
TQID: https://experienceleague.adobe.com/C2Z5SufckUxCNf9TsloziZS-Q3KPzmgMVNGJGiwDQ08
product_v2:
  - id: cb954087-f4fc-4456-afb9-e939cabcdc79
    internal-label: Journey Optimizer
feature_v2:
  - id: d998adac-2f81-400b-a669-d07bb196e4eb
    internal-label: Journeys
role_v2:
  - id: ff6a42d2-313e-452e-93a6-792e4fad9ff8
    internal-label: Developer
topic_v2:
  - id: d00e9f03-e50b-4162-b143-0c0817c937c2
    internal-label: Customer journeys
  - id: e0eb8757-182f-49f3-94a4-1587d16f5094
    internal-label: Personalization
subfeature_v2: []
---
# Date functions {#date-functions}

Date functions enable you to manipulate and work with date and time values within your journey expressions. These functions are essential for time-based conditions, scheduling, and temporal calculations in your customer journeys.

Use date functions when you need to:

* Get the current time or date with specific timezone handling ([now](#now), [nowWithDelta](#nowWithDelta), [currentTimeInMillis](#currentTimeInMillis))
* Calculate the difference between two dates or date-times, in days or milliseconds depending on the parameter type ([dateDiff](#dateDiff))
* Check if a date falls within a specific time range ([inLastDays](#inLastDays), [inLastHours](#inLastHours), [inLastMonths](#inLastMonths), [inLastYears](#inLastYears), [inNextDays](#inNextDays), [inNextHours](#inNextHours), [inNextMonths](#inNextMonths), [inNextYears](#inNextYears))
* Modify date and time components ([setHours](#setHours), [setDays](#setDays), [updateTimeZone](#updateTimeZone))
* Perform time-based calculations and comparisons
* Convert between different time formats and representations

Date functions provide precise control over temporal logic, allowing you to create time-sensitive journey paths and conditions that respond to specific timeframes and schedules.

>[!NOTE]
>
>The functions on this page are available in journey expressions. Some functions like `now()` are not available in the personalization editor for email content. [Learn more](../../personalization/functions/dates.md)

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

## dateDiff {#dateDiff}

Returns the difference between two dates or date-times of the same type. The unit of the result depends on the parameter type: `dateOnly` parameters return the difference in **days**, while `dateTimeOnly` and `dateTime` parameters return the difference in **milliseconds**. Returns `null` if either parameter is `null`.

>[!NOTE]
>
>This is a different function from the `dateDiff` available in the [personalization editor](../../personalization/functions/dates.md#date-diff). The personalization editor version only accepts `dateTime` parameters and always returns the difference in days.

+++Syntax

`dateDiff(<date1>,<date2>)`

+++

+++Parameters

| Parameter | Type                                 |
|-----------|--------------------------------------|
| date 1    | dateOnly, dateTimeOnly, or dateTime  |
| date 2    | dateOnly, dateTimeOnly, or dateTime  |

Both parameters must use the same data type; mixing types (for example, `dateOnly` with `dateTime`) is not supported. Parameters can be literal date values, other functions such as `now()`, or contextual attributes (event payload fields, custom action response fields, profile or entity fields, and variables) as long as they are typed as `dateOnly`, `dateTimeOnly`, or `dateTime`.

+++

+++Signatures and returned type

`dateDiff(<dateOnly>,<dateOnly>)`

Returns an integer representing the number of days between the two dates.

`dateDiff(<dateTimeOnly>,<dateTimeOnly>)`

Returns an integer representing the number of milliseconds between the two date-times.

`dateDiff(<dateTime>,<dateTime>)`

Returns an integer representing the number of milliseconds between the two date-times.

+++

+++Examples

`dateDiff(toDateOnly('2023-12-15'), toDateOnly('2023-12-12'))`

Returns 3 (days).

`dateDiff(toDateTimeOnly('2023-12-15T00:00:00'), toDateTimeOnly('2023-12-12T00:00:00'))`

Returns 259200000 (milliseconds, equivalent to 3 days).

`dateDiff(now(), toDateTime('2024-12-25T00:00:00Z'))`

Returns the number of milliseconds between today and December 25, 2024.

`dateDiff(#{ExperiencePlatform.ProfileFieldGroup.person.birthDate}, toDateOnly('2023-01-01'))`

Returns the number of days between the profile's `birthDate` field and January 1, 2023, assuming `birthDate` is typed as `dateOnly`.

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

>[!NOTE]
>
>This function is only available in journey expressions. For email personalization and other content, use `getCurrentZonedDateTime()` instead. [Learn more](../../personalization/functions/dates.md#get-current-zoned-date-time)

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

`nowWithDelta(1, "months", "Asia/Tokyo")`

When evaluated on 2026-01-31, returns 2026-02-28T...; when evaluated on 2026-05-31, returns 2026-06-30T...

`nowWithDelta()` uses calendar-month arithmetic. If the target month has fewer days than the current day-of-month, the result is normalized to the last valid day of that month. The function does not roll over into the following month.

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

+++ AI Knowledge Reference

This section contains structured knowledge intended to support interpretation, retrieval, and question answering related to this topic.

For complete understanding, this information should be combined with the documentation on this page. Neither source is intended to stand alone; the page describes the feature, while this section provides additional context that helps disambiguate terminology, intent, applicability, and constraints.

* **TL;DR:** This page documents all date and time functions available in AJO journey expressions, covering how to get the current time, check whether a date falls within a relative time window, and modify date/time components.

**Intents:**
* Get the current datetime (with optional timezone) using `now` or `nowWithDelta`
* Retrieve the current time as an epoch integer using `currentTimeInMillis`
* Calculate the difference between two dates or date-times using `dateDiff`
* Check if a datetime falls within the last N days, hours, months, or years using `inLastDays`, `inLastHours`, `inLastMonths`, `inLastYears`
* Check if a datetime falls within the next N days, hours, months, or years using `inNextDays`, `inNextHours`, `inNextMonths`, `inNextYears`
* Force a specific hour or day of the month on a datetime value using `setHours` or `setDays`
* Convert a datetime to a different timezone while preserving the same instant using `updateTimeZone`

**Glossary:**
* **dateOnly**: A date value with no time or timezone information *(product-specific)*
* **dateTime**: A date-time value that includes timezone offset information *(product-specific)*
* **dateTimeOnly**: A date-time value with no timezone information *(product-specific)*
* **epoch milliseconds**: An integer representing the number of milliseconds elapsed since 1970-01-01T00:00:00Z
* **delta**: An integer offset (positive or negative) used with `nowWithDelta` to shift the current time by a number of years, months, days, hours, minutes, or seconds

**Guardrails:**
* `now()` is only available in journey expressions; for email personalization use `getCurrentZonedDateTime()` instead
* The timezone ID in `nowWithDelta` must be a string constant — field references and dynamic expressions are not supported
* The timezone ID in `updateTimeZone` must be a string constant
* `dateDiff` requires both parameters to be the same data type (`dateOnly`, `dateTimeOnly`, or `dateTime`); mixing types is not supported
* `dateDiff` returns `null` if either parameter is `null`
* `dateDiff` returns days for `dateOnly` parameters, but milliseconds (not days) for `dateTimeOnly` and `dateTime` parameters — convert accordingly when comparing results across types

**Terminology:**
* Canonical name: Date functions — Acronym: none — variants: date-time functions, temporal functions
* Synonyms: "now()" = "current datetime"; "currentTimeInMillis()" = "current epoch milliseconds"
* Do not confuse: "inLastDays" (looks back in time) ≠ "inNextDays" (looks forward in time)
* Do not confuse: "setHours" (replaces the hour component) ≠ "nowWithDelta" (offsets the current time)
* Do not confuse: "updateTimeZone" (same instant, different timezone representation) ≠ "setHours" (changes the time value itself)
* Do not confuse: the journey expression editor's `dateDiff` (accepts `dateOnly`, `dateTimeOnly`, or `dateTime`; returns days or milliseconds depending on type) ≠ the personalization editor's `dateDiff` (accepts only `dateTime`; always returns days)

**FAQ:**
* **Q: Can I use `now()` in email personalization content?** — No, `now()` is only available in journey expressions. Use `getCurrentZonedDateTime()` for email personalization.
* **Q: How do I check if an event happened in the last 24 hours?** — Use `inLastHours(@event{MyEvent.timestamp}, 24)`.
* **Q: How do I get the current time offset by 2 hours in the past?** — Use `nowWithDelta(-2, "hours")`.
* **Q: What does `updateTimeZone` do differently from `setHours`?** — `updateTimeZone` keeps the same instant in time but expresses it in a different timezone, while `setHours` actually changes the hour component of the datetime value.
* **Q: Can the timezone parameter in `nowWithDelta` be a profile field?** — No, the timezone ID must be a string constant; field references are not supported.
* **Q: What happens when `nowWithDelta()` is used with months and the current date is a month-end date?** — The function uses calendar-month arithmetic and normalizes the result to the last valid day of the target month. For example, adding 1 month to January 31 returns February 28 (not March 3).

+++
