---
solution: Journey Optimizer
product: journey optimizer
title: Functions
description: Learn about functions in journey expressions
feature: Journeys
role: Developer
level: Experienced
keywords: function, expressions, editor, journey, data, manipulation
exl-id: 5b978eef-7d3e-41fe-bb08-0cf37c3b125d
version: Journey Orchestration
---
# Functions {#functions}

Functions are the building blocks of dynamic journey expressions in Adobe Journey Optimizer. They enable you to transform, calculate, validate, and manipulate data in real-time to create personalized customer experiences. With over 60 functions organized into intuitive categories, you can build sophisticated conditions, perform complex calculations, and make data-driven decisions at every step of the customer journey.

## Understanding functions

Functions in journey expressions follow a consistent syntax pattern:

`<function name>`(`<expression as param 1>`, `<expression as param 2>`, ... ,`<expression as param N>`)

**Key characteristics:**

* **Multiple signatures**: A function can have different signatures (different sets of ordered parameters) to accommodate various use cases
* **Type-specific returns**: Each function has a specific returned type (string, integer, boolean, date, list, etc.)
* **Zero to N parameters**: Functions can accept 0-N expressions as ordered parameters, providing flexibility in how you use them

## Why use functions?

Functions empower you to:

* **Create dynamic conditions** - Branch journey paths based on real-time data evaluation
* **Personalize at scale** - Tailor content and experiences using customer data and behavioral insights
* **Automate decisions** - Build intelligent logic without manual intervention
* **Transform data** - Convert, format, and manipulate data types to ensure compatibility
* **Perform calculations** - Execute mathematical operations and statistical analysis
* **Validate inputs** - Check data quality and completeness before taking action

## Functions by category

Browse functions organized by their primary purpose to quickly find the right tool for your needs.

### Adobe Experience Platform {#aep-functions}

**Audience segmentation and targeting**

Evaluate audience membership to create personalized journey paths based on customer segments defined in Adobe Experience Platform.

| Function | Description |
|----------|-------------|
| [inAudience](../functions/functioninaudience.md) | Check if an individual belongs to a specific audience |

[View Adobe Experience Platform function details →](../functions/functioninaudience.md)

### Aggregation functions {#aggregation-functions}

**Statistical calculations and data summarization** 

Perform calculations on sets of values to derive insights such as averages, counts, sums, and min/max values. Essential for data-driven decision making.

| Function | Description |
|----------|-------------|
| [avg](../functions/aggregation-functions.md#avg) | Calculate average value |
| [count](../functions/aggregation-functions.md#count) | Count non-null elements |
| [countOnlyNull](../functions/aggregation-functions.md#countOnlyNull) | Count null values only |
| [countWithNull](../functions/aggregation-functions.md#countWithNull) | Count all elements including nulls |
| [distinctCount](../functions/aggregation-functions.md#distinctCount) | Count unique non-null values |
| [distinctCountWithNull](../functions/aggregation-functions.md#distinctCountWithNull) | Count unique values including nulls |
| [max](../functions/aggregation-functions.md#max) | Find maximum value |
| [min](../functions/aggregation-functions.md#min) | Find minimum value |
| [sum](../functions/aggregation-functions.md#sum) | Calculate total sum |

[View all aggregation functions →](../functions/aggregation-functions.md)

### Conversion functions {#conversion-functions}

**Data type transformation**

Convert data between different types (string, integer, decimal, boolean, date, duration) to ensure compatibility across operations and data sources.

| Function | Description |
|----------|-------------|
| [toBool](../functions/conversion-functions.md#toBool) | Convert to boolean |
| [toDateOnly](../functions/conversion-functions.md#toDateOnly) | Convert to date only (no time) |
| [toDateTime](../functions/conversion-functions.md#toDateTime) | Convert to date with time |
| [toDateTimeOnly](../functions/conversion-functions.md#toDateTimeOnly) | Convert to date-time without timezone |
| [toDecimal](../functions/conversion-functions.md#toDecimal) | Convert to decimal number |
| [toDuration](../functions/conversion-functions.md#toDuration) | Convert to duration |
| [toInteger](../functions/conversion-functions.md#toInteger) | Convert to integer |
| [toString](../functions/conversion-functions.md#toString) | Convert to string |

[View all conversion functions →](../functions/conversion-functions.md)

### Date functions {#date-functions}

**Date and time manipulation**

Work with dates, times, and timezones to create time-based conditions, schedule actions, and perform temporal calculations.

| Function | Description |
|----------|-------------|
| [currentTimeInMillis](../functions/date-functions.md#currentTimeInMillis) | Get current time in milliseconds |
| [inLastDays](../functions/date-functions.md#inLastDays) | Check if date is within last N days |
| [inLastHours](../functions/date-functions.md#inLastHours) | Check if date is within last N hours |
| [inLastMonths](../functions/date-functions.md#inLastMonths) | Check if date is within last N months |
| [inLastYears](../functions/date-functions.md#inLastYears) | Check if date is within last N years |
| [inNextDays](../functions/date-functions.md#inNextDays) | Check if date is within next N days |
| [inNextHours](../functions/date-functions.md#inNextHours) | Check if date is within next N hours |
| [inNextMonths](../functions/date-functions.md#inNextMonths) | Check if date is within next N months |
| [inNextYears](../functions/date-functions.md#inNextYears) | Check if date is within next N years |
| [now](../functions/date-functions.md#now) | Get current date-time |
| [nowWithDelta](../functions/date-functions.md#nowWithDelta) | Get current time with offset |
| [setHours](../functions/date-functions.md#setHours) | Set specific hours in date-time |
| [setDays](../functions/date-functions.md#setDays) | Set specific days in date-time |
| [updateTimeZone](../functions/date-functions.md#updateTimeZone) | Update timezone of date-time |

[View all date functions →](../functions/date-functions.md)

### List functions {#list-functions}

**Collection manipulation and analysis**

Filter, sort, transform, and analyze arrays and lists to work with complex data structures and perform set operations.

| Function | Description |
|----------|-------------|
| [distinct](../functions/list-functions.md#distinct) | Get unique values (excludes nulls) |
| [distinctWithNull](../functions/list-functions.md#distinctWithNull) | Get unique values (includes nulls) |
| [filter](../functions/list-functions.md#filter) | Filter list based on criteria |
| [getListItem](../functions/list-functions.md#getListItem) | Get item at specific index |
| [in](../functions/list-functions.md#in) | Check if value exists in list |
| [intersect](../functions/list-functions.md#intersect) | Find common elements between lists |
| [limit](../functions/list-functions.md#limit) | Limit number of items returned |
| [listSize](../functions/list-functions.md#listSize) | Get size of list |
| [serializeList](../functions/list-functions.md#serializeList) | Convert list to string |
| [sort](../functions/list-functions.md#sort) | Sort list elements |

[View all list functions →](../functions/list-functions.md)

### Math functions {#math-functions}

**Mathematical operations**

Perform numerical calculations and transformations for data processing and business logic.

| Function | Description |
|----------|-------------|
| [random](../functions/math-functions.md#random) | Generate random number (0-1) |
| [round](../functions/math-functions.md#round) | Round to nearest integer |

[View all math functions →](../functions/math-functions.md)

### String functions {#string-functions}

**Text manipulation and validation**

Process, transform, search, and validate text data for dynamic content creation and conditional logic.

| Function | Description |
|----------|-------------|
| [concat](../functions/string-functions.md#concat) | Concatenate strings |
| [contain](../functions/string-functions.md#contain) | Check if string contains substring |
| [containIgnoreCase](../functions/string-functions.md#containIgnoreCase) | Check contains (case-insensitive) |
| [endWith](../functions/string-functions.md#endWith) | Check if string ends with suffix |
| [endWithIgnoreCase](../functions/string-functions.md#endWithIgnoreCase) | Check ends with (case-insensitive) |
| [equalIgnoreCase](../functions/string-functions.md#equalIgnoreCase) | Compare strings (case-insensitive) |
| [indexOf](../functions/string-functions.md#indexOf) | Find first occurrence position |
| [isEmpty](../functions/string-functions.md#isEmpty) | Check if string is empty |
| [isNotEmpty](../functions/string-functions.md#isNotEmpty) | Check if string is not empty |
| [lastIndexOf](../functions/string-functions.md#lastIndexOf) | Find last occurrence position |
| [length](../functions/string-functions.md#length) | Get string length |
| [lower](../functions/string-functions.md#lower) | Convert to lowercase |
| [matchRegExp](../functions/string-functions.md#matchRegExp) | Match regular expression |
| [notEqualIgnoreCase](../functions/string-functions.md#notEqualIgnoreCase) | Check not equal (case-insensitive) |
| [replace](../functions/string-functions.md#replace) | Replace first occurrence |
| [replaceAll](../functions/string-functions.md#replaceAll) | Replace all occurrences |
| [split](../functions/string-functions.md#split) | Split string into array |
| [startWith](../functions/string-functions.md#startWith) | Check if string starts with prefix |
| [startWithIgnoreCase](../functions/string-functions.md#startWithIgnoreCase) | Check starts with (case-insensitive) |
| [substr](../functions/string-functions.md#substr) | Extract substring |
| [trim](../functions/string-functions.md#trim) | Remove leading/trailing spaces |
| [upper](../functions/string-functions.md#upper) | Convert to uppercase |
| [uuid](../functions/string-functions.md#uuid) | Generate UUID |

[View all string functions →](../functions/string-functions.md)

## Next steps

Now that you understand the available functions, explore:

* **[Advanced expression editor](expressionadvanced.md)** - Learn how to build complex expressions using the advanced editor
* **[Expression syntax](generalities.md)** - Master the syntax rules for writing journey expressions
* **[Operators](operators.md)** - Discover operators you can use with functions to build logic
* **[Field references](field-references.md)** - Understand how to reference data fields in your expressions
