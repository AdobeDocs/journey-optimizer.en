---
product: journey optimizer
title: Conversion functions
description: Learn about conversion functions
feature: Journeys
role: Developer
level: Experienced
keywords: conversion, functions, expression, journey, type, cast
version: Journey Orchestration
---
# Conversion functions {#conversion-functions}

Conversion functions enable you to transform data from one type to another within your journey expressions. These functions are essential for ensuring data compatibility and proper type handling when working with different data sources and operations.

Use conversion functions when you need to:

* Convert string values to numeric, boolean, or date types ([toInteger](#toInteger), [toDecimal](#toDecimal), [toBool](#toBool))
* Transform dates and times between different formats and representations ([toDateTime](#toDateTime), [toDateTimeOnly](#toDateTimeOnly), [toDateOnly](#toDateOnly))
* Cast numeric values between integer and decimal types ([toInteger](#toInteger), [toDecimal](#toDecimal))
* Convert values to string format ([toString](#toString)) or duration ([toDuration](#toDuration))
* Ensure type compatibility for comparisons and operations
* Process data from external sources that may have different type formats

Each conversion function handles type-specific rules and edge cases automatically, making data transformation more reliable and predictable in your journey expressions.

## toBool {#toBool}

Converts an argument value into a boolean value, depending on its type.

* From string: try to convert the string value as a boolean, from "true" if the string value is "true", false otherwise
* From numerical: true if the numerical value is not equal to 0, false otherwise

+++Syntax

`toBool(<parameter>)`

+++

+++Parameters

* decimal
* boolean
* string
* integer

+++

+++Signatures and returned types

`toBool(<decimal>)`

`toBool(<boolean>)`

`toBool(<string>)`

`toBool(<integer>)`

Return a boolean.

+++

+++Examples

`toBool("true")`

`toBool(1)`

Returns true.

`toBool("this is not a boolean")`

Returns false.

+++

## toDateOnly {#toDateOnly}

Converts an argument into a dateOnly type value. To learn more about data types, refer to this [section](../expression/data-types.md).

+++Syntax

`toDateOnly(<parameters>)`

+++

+++Parameters

| Parameter | Type             |
|-----------|------------------|
| String representation of a date as "YYYY-MM-DD" (XDM format). Also supports ISO-8601 format: only **full-date** part is considered (Refer to [RFC 3339, section 5.6](https://www.rfc-editor.org/rfc/rfc3339#section-5.6) | string |
| date time | dateTime|
| date time without time zone | dateTimeOnly|
| integer value of an epoch in milliseconds| integer |

+++

+++Signatures and returned types

`toDateOnly(<dateTime>)`

`toDateOnly(<dateTimeOnly>)`

`toDateOnly(<string>)`

`toDateOnly(<integer>, <integer>, <integer>)`

Returns a dateOnly type value.

+++

+++Examples

`toDateOnly("2023-08-18")`

`toDateOnly("2023-08-18T00:00:00.000Z")`

`toDateOnly("2023-08-18T00:00:00")`

all return a dateOnly object representing 2023-08-18.

`toDateOnly(#{ExperiencePlatform.ProfileFieldGroup.person.birthDate})`

Returns a dateOnly.

+++

## toDateTime {#toDateTime}

Converts parameters into a date time value, depending on their types.

+++Syntax

`toDateTime(<parameters>)`

+++

+++Parameters

|Parameter|Description|
|--- |--- |
|string|date time in ISO-8601 format. A string representation of a datetime with timezone information|
|string|time zone id. A timezone identifier (e.g., "UTC", "Europe/Paris")|
|dateOnly|represents a date without a time zone, viewed as year-month-day|
|dateTimeOnly|represents a datetime without a time zone, viewed as year-month-day-hour-minute-second-millisecond|
|integer|integer value of an epoch in milliseconds|

+++

+++Signatures and returned types

`toDateTime(<string>)`

`toDateTime(<string>, <dateOnly>)`

`toDateTime(<string>, <dateTimeOnly>)`

`toDateTime(<integer>)`

Return a **dateTime**.

+++

+++Examples

`toDateTime("2023-08-18T23:17:59.123Z")`

Returns 2023-08-18T23:17:59.123Z

The ISO-8601 string already includes timezone information.

`toDateTime("Europe/Paris", toDateOnly("2023-08-18"))`

Returns 2023-08-18T00:00:00.000+02:00

This creates a dateTime by combining a timezone with a date-only value. The time is set to midnight (00:00:00) in the specified timezone.

`toDateTime("UTC", toDateTimeOnly("2023-08-18T23:17:59.123"))`

Returns 2023-08-18T23:17:59.123Z

This creates a dateTime by applying a timezone to a dateTimeOnly value (which has no timezone information).

`toDateTime(1560762190189)`

Returns 2019-06-17T09:03:10.189Z

Converts a Unix timestamp in milliseconds to a dateTime value.

+++

>[!NOTE]
>
>Time zone id must be a string constant. It cannot be a field reference nor an expression. For more information on data types, refer to [this page](../expression/data-types.md).

## toDateTimeOnly {#toDateTimeOnly}

Converts an argument value into a date time only value.

+++Syntax

`toDateTimeOnly(<parameters>)`

+++

+++Parameters

| Parameter | Type             |
|-----------|------------------|
| date time in ISO-8601 or "YYYY-MM-DD" format (XDM Date format) | string |
| date time | dateTime|

+++

+++Signatures and returned types

`toDateTimeOnly(<dateTime>)`

`toDateTimeOnly(<string>)`

Return a datetime without considering time zone.

+++

+++Examples

`toDateTimeOnly ("2023-08-18")`

returns a dateTime representing 2023-08-18T00:00:00.000

`toDateTimeOnly(now())`

+++

## toDecimal {#toDecimal}

Converts an argument value into a decimal value, depending on its type.

+++Syntax

`toDecimal(<parameter>)`

+++

+++Parameters

|Parameter|Description|
|--- |--- |
|string|converts the string value as a decimal|
|dateTime|converts the date as the number of milliseconds (epoch milliseconds)|
|boolean|converts the boolean value as 1 if true, 0 if false|
|integer|converts to a decimal (example.: 1 becomes 1.0)|

+++

+++Signatures and returned types

`toDecimal(<integer>)`

`toDecimal(<decimal>)`

`toDecimal(<string>)`

`toDecimal(<boolean>)`

Return a decimal.

+++

+++Examples

`toDecimal("4.0")`

Returns 4.0.

+++

## toDuration {#toDuration}

Converts an argument value to a duration. For more information on data types, refer to [this page](../expression/data-types.md).

+++Syntax

`toDuration(<parameter>)`

+++

+++Parameters

|Parameter|Description|
|--- |--- |
|string|formats based on the ISO-8601 duration format PnDTnHnMn.nS with days considered to be exactly 24 hours|
|integer|number of milliseconds|

If string expression: formats accepted are based on the ISO-8601 duration format PnDTnHnMn.nS with days considered to be exactly 24 hours.

The string starts with an optional sign, denoted by the ASCII negative or positive symbol. If negative, the whole period is negated. The ASCII letter "P" is next in upper or lower case. There are then four sections, each consisting of a number and a suffix. The sections have suffixes in ASCII of "D", "H", "M" and "S" for days, hours, minutes and seconds, accepted in upper or lower case. The suffixes must occur in order. The ASCII letter "T" must occur before the first occurrence, if any, of an hour, minute or second section. At least one of the four sections must be present, and if "T" is present there must be at least one section after the "T". The number part of each section must consist of one or more ASCII digits. The number may be prefixed by the ASCII negative or positive symbol. The number of days, hours and minutes must parse to along. The number of seconds must parse to along with optional fraction. The decimal point may be either a dot or a comma. The fractional part may have from zero to 9 digits.

+++

+++Signatures and returned type

`toDuration(<string>)`

`toDuration(<integer>)`

Returns a duration.

+++

+++Examples

`toDuration("PT10H")`

Returns duration of 10 hours.

`toDuration("PT4S")`

Returns duration of 4s.

`toDuration(4000)`

Returns duration of 4s.

+++

## toInteger {#toInteger}

Converts an argument value to an integer.

+++Syntax

`toInteger(<parameter>)`

+++

+++Parameters

|Parameter|Description|
|--- |--- |
|string|converts the string value as an integer|
|dateTime|converts the date as the number of milliseconds (epoch milliseconds)|
|decimal|converts into integer by removing the decimal part (example: 1.5 becomes 1)|
|boolean|converts the boolean value as 1 if true, 0 if false|

+++

+++Signatures and returned type

`toInteger(<dateTime>)`

`toInteger(<decimal>)`

`toInteger(<integer>)`

`toInteger(<string>)`

`toInteger(<boolean>)`

Return an integer.

+++

+++Examples

`toInteger("4")`

Returns 4.

+++

## toString {#toString}

Converts an argument value into a string value, depending on its type. For more information on data types, refer to [this page](../expression/data-types.md).

+++Syntax

`toString(<parameter>)`

+++

+++Parameters

|Parameter|Description|
|--- |--- |
|dateTime|converts the date in UTC date format|
|dateTimeOnly|converts the date in UTC date format|
|duration|convert into the corresponding number of milliseconds as a string|
|integer|converts to string representation of the value (1 becomes "1")|
|decimal|converts to string representation of the value (1.5 becomes "1.5")|
|boolean|convert the boolean value as 'true' if true, 'false' if false|

+++

+++Signatures and returned type

`toString(<dateTimeOnly>)`

`toString(<dateTime>)`

`toString(<duration>)`

`toString(<boolean>)`

`toString(<integer>)`

`toString(<decimal>)`

Return a string.

+++

+++Examples

`toString(4)`

Returns "4".

`toString(#{ExperiencePlatform.test_date.person.birthDate}))`

Returns the string representation of the given dateOnly field (XDM Date field), for example "2023-08-18".

`toString(toDuration(1520))`

Returns "PT1.52S".

+++

