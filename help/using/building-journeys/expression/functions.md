---
solution: Journey Optimizer
product: journey optimizer
title: Functions
description: Learn about functions
feature: Journeys
role: Developer
level: Experienced
keywords: function, expressions, editor, journey
exl-id: 5b978eef-7d3e-41fe-bb08-0cf37c3b125d
version: Journey Orchestration
---
# Functions {#functions}

A function can have different signatures (a different set of ordered parameters). A function signature can have 0-N expressions as ordered parameters.

`<function name>`(`<expression as param 1>`, `<expression as param 2>`, ... ,`<expression as param N>`)

Each function has a specific returned type. 

Here is the list of supported functions.

## Main functions

| Category    | Function              |
|-------------|-----------------------|
| Adobe Experience Platform | [inAudience](../functions/functioninaudience.md)|
| Aggregation | [avg](../functions/aggregation-functions.md#avg)|
| Aggregation | [count](../functions/aggregation-functions.md#count)|
| Aggregation | [countOnlyNull](../functions/aggregation-functions.md#countOnlyNull)|
| Aggregation | [countWithNull](../functions/aggregation-functions.md#countWithNull)|
| Aggregation | [distinctCount](../functions/aggregation-functions.md#distinctCount)|
| Aggregation | [distinctCountWithNull](../functions/aggregation-functions.md#distinctCountWithNull)|
| Aggregation | [max](../functions/aggregation-functions.md#max)|
| Aggregation | [min](../functions/aggregation-functions.md#min)|
| Aggregation | [sum](../functions/aggregation-functions.md#sum)|
| Conversion  | [toBool](../functions/conversion-functions.md#toBool)|
| Conversion  | [toDateOnly](../functions/conversion-functions.md#toDateOnly)|
| Conversion  | [toDateTime](../functions/conversion-functions.md#toDateTime)|
| Conversion  | [toDateTimeOnly](../functions/conversion-functions.md#toDateTimeOnly)|
| Conversion  | [toDecimal](../functions/conversion-functions.md#toDecimal)|
| Conversion  | [toDuration](../functions/conversion-functions.md#toDuration)|
| Conversion  | [toInteger](../functions/conversion-functions.md#toInteger)|
| Conversion  | [toString](../functions/conversion-functions.md#toString)|
| Date        | [currentTimeInMillis](../functions/date-functions.md#currentTimeInMillis)|
| Date        | [inLastDays](../functions/date-functions.md#inLastDays)|
| Date        | [inLastHours](../functions/date-functions.md#inLastHours)|
| Date        | [inLastMonths](../functions/date-functions.md#inLastMonths)|
| Date        | [inLastYears](../functions/date-functions.md#inLastYears)|
| Date        | [inNextDays](../functions/date-functions.md#inNextDays)|
| Date        | [inNextHours](../functions/date-functions.md#inNextHours)|
| Date        | [inNextMonths](../functions/date-functions.md#inNextMonths)|
| Date        | [inNextYears](../functions/date-functions.md#inNextYears)|
| Date        | [now](../functions/date-functions.md#now)|
| Date        | [nowWithDelta](../functions/date-functions.md#nowWithDelta)|
| Date        | [setHours](../functions/date-functions.md#setHours)|
| Date        | [setDays](../functions/date-functions.md#setDays)|
| Date        | [updateTimeZone](../functions/date-functions.md#updateTimeZone)|
| List        | [distinct](../functions/list-functions.md#distinct)|
| List        | [distinctWithNull](../functions/list-functions.md#distinctWithNull)|
| List        | [filter](../functions/list-functions.md#filter)|
| List        | [getListItem](../functions/list-functions.md#getListItem)|
| List        | [in](../functions/list-functions.md#in)|
| List        | [intersect](../functions/list-functions.md#intersect)|
| List        | [limit](../functions/list-functions.md#limit)|
| List        | [listSize](../functions/list-functions.md#listSize)|
| List        | [serializeList](../functions/list-functions.md#serializeList)|
| List        | [sort](../functions/list-functions.md#sort)|
| Math        | [random](../functions/functionrandom.md)|
| Math        | [round](../functions/functionround.md)|
| String      | [concat](../functions/functionconcat.md)|
| String      | [contain](../functions/functioncontain.md)|
| String      | [containIgnoreCase](../functions/functioncontainwithignorecase.md)|
| String      | [endWith](../functions/functionendwith.md)|
| String      | [endWithIgnoreCase](../functions/functionendwithignorecase.md)|
| String      | [equalIgnoreCase](../functions/functionequalignorecase.md)|
| String      | [indexOf](../functions/functionindexof.md)|
| String      | [isEmpty](../functions/functionisempty.md)|
| String      | [isNotEmpty](../functions/functionisnotempty.md)|
| String      | [lastIndexOf](../functions/functionlastindexof.md)|
| String      | [length](../functions/functionlength.md)|
| String      | [lower](../functions/functionlower.md)|
| String      | [matchRegExp](../functions/functionmatchregexp.md)|
| String      | [notEqualIgnoreCase](../functions/functionnotequalignorecase.md)|
| String      | [replace](../functions/functionreplace.md)|
| String      | [replaceAll](../functions/functionreplaceall.md)|
| String      | [split](../functions/functionsplit.md)|
| String      | [startWith](../functions/functionstartwith.md)|
| String      | [startWithIgnoreCase](../functions/functionstartwithignorecase.md)|
| String      | [substr](../functions/functionsubstr.md)|
| String      | [trim](../functions/functiontrim.md)|
| String      | [upper](../functions/functionupper.md)|
| String      | [uuid](../functions/functionuuid.md)|
