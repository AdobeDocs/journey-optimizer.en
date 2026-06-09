---
solution: Journey Optimizer
product: journey optimizer
title: Data types
description: Learn about data types in advanced expressions
feature: Journeys
role: Developer
level: Experienced
keywords: expression, data, data type, journey
exl-id: fdfc3287-d733-45fb-ad11-b4238398820a
version: Journey Orchestration
TQID: https://experienceleague.adobe.com/0UKY3G4hyMnSkzh8wlMx-yQ1yymKjs6FuIBdGo1SJqc
product_v2:
  - id: cb954087-f4fc-4456-afb9-e939cabcdc79
    internal-label: Journey Optimizer
feature_v2:
  - id: d998adac-2f81-400b-a669-d07bb196e4eb
    internal-label: Journeys
role_v2:
  - id: ff6a42d2-313e-452e-93a6-792e4fad9ff8
    internal-label: Developer
subfeature_v2: []
---
# Data types {#data-types}

Technically, a constant always contains a data type. In the literal expression, we only specify the value. The data type can be inferred from the value (for example string, integer, decimal, etc.). For specific cases such as date time, we use dedicated functions for the representation.

The sections below provide information on the different data type expressions and how they are represented.

## string {#string}

**Description**

Common sequence of characters. It doesn't have any specific size except the implicit one that comes from the environment such as the amount of memory available.

JSON format: String

Serialization format: UTF-8

**Literal representation**

```json
"<value>"
```

```json
'<value>'
```

**Example**

```json
"hello world"
```

```json
'hello world'
```

## integer {#integer}

**Description**

Integer value from -2^63 to 2^63-1.

JSON format: Number

**Literal representation**

```json
<integer value>
```

**Example**

```json
42
```

## decimal {#decimal}

**Description**

Decimal number. It represents a floating value:

* largest positive finite value of type double, (2-2^-52)x2^1023
* smallest positive normal value of type double, 2-1022
* smallest positive nonzero value of type double, 2 p-1074

JSON format: Number

Serialization format: using '.' as the decimal separator.

**Literal representation**

```json
<integer value>.<integer value>
```

**Example**

```json
3.14
```

## boolean {#boolean}

**Description**

Boolean value written lowercase: true or false

JSON format: Boolean

**Literal representation**

```json
true
```

```json
false
```

**Example**

```json
true
```

## dateOnly {#date-only}

**Description**

Represents a date only without a time zone, viewed as a year-month-day.

It is a description of the date, as used for birthdays.

JSON format: String.

Format is: YYYY-MM-DD (ISO-8601), for example: "2021-03-11".

It can be encapsulated in a toDateOnly function.

It uses DateTimeFormatter ISO_LOCAL_DATE_TIME to deserialize and serialize the value. [Learn more](https://datatracker.ietf.org/doc/html/rfc3339#section-5.6)

**Literal representation**

```json
date("<dateOnly in ISO-8601 format>")  
```

**Example**

```json
date("2021-02-19")
```

## dateTimeOnly {#date-time-only}

**Description**

Represents a date time without a time zone, viewed as year-month-day-hour-minute-second-millisecond.

JSON format: String.

It does not store or represent a time zone. Instead, it is a description of the date, as used for birthdays, combined with the local time as seen on a wall clock.

It cannot represent an instant on the time-line without additional information such as an offset or time zone.

It can be encapsulated in a toDateTimeOnly function.

Serialization format: ISO-8601 extended offset date-time format.

It uses DateTimeFormatter ISO_LOCAL_DATE_TIME to deserialize and serialize the value. [Learn more](https://docs.oracle.com/javase/8/docs/api/java/time/format/DateTimeFormatter.html#ISO_LOCAL_DATE_TIME"){_blank}.

**Literal representation**

```json
date("<dateTimeOnly in ISO-8601 format>")  
```

**Examples**

```json
date("2024-02-19T00.00.000")
date("2024-02-19T00.00")
```

## dateTime {#date-time}

**Description**

Date time constant that also considers time zone. It represents a date-time with an offset from UTC.

It can be viewed as an instant in time with the additional information of the offset. It is a way to represent a specific "moment" at a certain place of the world.

JSON format: String.

It can be encapsulated in a toDateTime function.

Serialization format: ISO-8601 extended offset date-time format.

It uses DateTimeFormatter ISO_OFFSET_DATE_TIME to deserialize and serialize the value. [Learn more](https://docs.oracle.com/javase/8/docs/api/java/time/format/DateTimeFormatter.html#ISO_OFFSET_DATE_TIME){_blank}.

You can also pass an integer passing an epoch value. [Read more](https://www.epochconverter.com){_blank}.

Time zone can be specified by an offset or a time zone code (example: Europe/Paris, Z - meaning UTC).

**Literal representation**

```json
toDateTime("<dateTime in ISO-8601 format>")
```

```json
date("<dateTime in ISO-8601 format>")
```

```json
toDateTime(<integer value of an epoch in milliseconds>)
```

**Examples**

```json
date("2024-02-19T00.00.000Z")
```

```json
toDateTime("1977-04-22T06:00:00Z")
```

```json
toDateTime("2023-12-03T15:15:30Z")
```

```json
toDateTime("2023-12-03T15:15:30.123Z")
```

```json
toDateTime("2023-12-03T15:15:30.123+02:00")
```

```json
toDateTime("2023-12-03T15:15:30.123-00:20")
```

```json
toDateTime(1560762190189)
```

## duration {#duration}

**Description**

It represents a time-based amount of time, such as '34.5 seconds'. It models a quantity or amount of time in terms of milliseconds.

The supported temporal units are: milliseconds, seconds, minutes, hours, days where a day equals to 24 hours. Years and months are not supported since they're not a fixed amount of time.

JSON format: String.

It must be encapsulated in a toDuration function.

Serialization format: To deserialize a time zone ID, it uses the java function java.time.

Duration.parse: the formats accepted are based on the ISO-8601 duration format PnDTnHnMn.nS with days considered to be exactly 24 hours. [Learn more](https://docs.oracle.com/javase/8/docs/api/java/time/Duration.html#parse-java.lang.CharSequence-){_blank}.

**Literal representation**

```json
toDuration("<duration in ISO-8601 format>")
```

```json
toDuration(<duration in milliseconds>)
```

**Example**

```json
toDuration("PT5S") -- parses as 5 seconds
```

```json
toDuration(500) -- parses as 500ms
```

```json
toDuration("PT20.345S") -- parses as "20.345 seconds"
```

```json
toDuration("PT15M") -- parses as "15 minutes" (where a minute is 60 seconds)
```

```json
toDuration("PT10H")  -- parses as "10 hours" (where an hour is 3600 seconds)
```

```json
toDuration("P2D") -- parses as "2 days" (where a day is 24 hours or 86400 seconds)
```

```json
toDuration("P2DT3H4M") -- parses as "2 days, 3 hours and 4 minutes"
```

```json
toDuration("P-6H3M") -- parses as "-6 hours and +3 minutes"
```

```json
toDuration("-P6H3M") -- parses as "-6 hours and -3 minutes"
```

```json
toDuration("-P-6H+3M") -- parses as "+6 hours and -3 minutes"
```

## list {#list}

**Description**

Comma separated list of expressions using square brackets as delimiters.

Polymorphism is not supported, hence all the expressions contained in the list should have the same type.

**Literal representation**

```json
[<expression>, <expression>, ... ]
```

**Example**

```json
["value1","value2"]
```

```json
[3,5]
```

```json
[toDuration(500),toDuration(800)]
```

+++AI Assistant — Page context

* **TL;DR:** This page describes every data type supported in the Journey advanced expression editor — string, integer, decimal, boolean, dateOnly, dateTimeOnly, dateTime, duration, and list — with their JSON formats, serialization rules, and literal representation syntax.

**Intents:**

* Identify the correct literal syntax for each data type when writing journey expressions
* Understand the difference between `dateOnly`, `dateTimeOnly`, and `dateTime` types and when to use each
* Represent a duration value using ISO-8601 format or milliseconds with the `toDuration()` function
* Construct a list expression with square bracket syntax for use in collection operations
* Use conversion functions (`toDateTime`, `toDateTimeOnly`, `toDuration`, `toDateOnly`) to create typed constants

**Glossary:**

* **dateOnly**: A date without time or time zone, formatted as YYYY-MM-DD; suitable for birthdays or calendar dates *(product-specific)*
* **dateTimeOnly**: A date and time without time zone information; cannot represent a specific instant without an offset *(product-specific)*
* **dateTime**: A date-time constant that includes a UTC offset, representing a specific instant; can also be created from an epoch integer *(product-specific)*
* **duration**: A time-based amount modelled in milliseconds; uses ISO-8601 `PnDTnHnMn.nS` format; years and months are not supported *(product-specific)*
* **list**: A comma-separated collection of expressions of the same type, delimited by square brackets *(product-specific)*

**Guardrails:**

* Duration supports milliseconds, seconds, minutes, hours, and days only — years and months are not supported as they are not fixed amounts of time
* A `duration` value must be wrapped in `toDuration()` — it cannot be expressed as a bare literal
* All expressions in a `list` must have the same type — polymorphism is not supported
* `dateTimeOnly` cannot represent an instant in time without an additional offset or time zone

**Terminology:**

* Canonical name: Data Types — Acronym: none — variants: expression data types, journey data types
* Synonyms: "dateTime" = "date-time with timezone"; "dateTimeOnly" = "local date-time"
* Do not confuse: `dateOnly` (no time) ≠ `dateTimeOnly` (date + time, no timezone) ≠ `dateTime` (date + time + timezone/offset)

**FAQ:**

* **Q: What is the difference between `dateTimeOnly` and `dateTime`?** — `dateTimeOnly` has no time zone or offset and cannot represent a precise instant; `dateTime` includes a UTC offset and represents a specific moment in time.
* **Q: How do I express a duration of 2 days and 3 hours?** — Use `toDuration("P2DT3H")`.
* **Q: Can I mix integers and strings in a list expression?** — No; all expressions in a list must be the same type.
* **Q: How do I create a `dateTime` from an epoch timestamp in milliseconds?** — Use `toDateTime(<epoch in milliseconds>)`, for example `toDateTime(1560762190189)`.
* **Q: Is `true` or `True` the correct boolean literal?** — Use lowercase `true` or `false`; uppercase variants are not valid.

+++
