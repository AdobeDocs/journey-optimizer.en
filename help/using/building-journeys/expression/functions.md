---
solution: Journey Optimizer
product: journey optimizer
title: Functions
description: Learn about functions
feature: Journeys
role: Data Engineer, Architect
level: Experienced
keywords: function, expressions, editor, journey
exl-id: 5b978eef-7d3e-41fe-bb08-0cf37c3b125d
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
| Aggregation | [avg](../functions/functionavg.md)|
| Aggregation | [count](../functions/functioncount.md)|
| Aggregation | [countOnlyNull](../functions/functioncountonlynull.md)|
| Aggregation | [countWithNull](../functions/functioncountwithnull.md)|
| Aggregation | [distinctCount](../functions/functiondistinctcount.md)|
| Aggregation | [distinctCountWithNull](../functions/functiondistinctcountwithnull.md)|
| Aggregation | [max](../functions/functionmax.md)|
| Aggregation | [min](../functions/functionmin.md)|
| Aggregation | [sum](../functions/functionsum.md)|
| Conversion  | [toBool](../functions/functiontobool.md)|
| Conversion  | [toDateOnly](../functions/functiontodateonly.md)|
| Conversion  | [toDateTime](../functions/functiontodatetime.md)|
| Conversion  | [toDateTimeOnly](../functions/functiontodatetimeonly.md)|
| Conversion  | [toDecimal](../functions/functiontodecimal.md)|
| Conversion  | [toDuration](../functions/functiontoduration.md)|
| Conversion  | [toInteger](../functions/functiontointeger.md)|
| Conversion  | [toString](../functions/functiontostring.md)|
| Date        | [currentTimeInMillis](../functions/functioncurrenttimeinmillis.md)|
| Date        | [inLastDays](../functions/functioninlastdays.md)|
| Date        | [inLastHours](../functions/functioninlasthours.md)|
| Date        | [inLastMonths](../functions/functioninlastmonths.md)|
| Date        | [inLastYears](../functions/functioninlastyears.md)|
| Date        | [inNextDays](../functions/functioninnextdays.md)|
| Date        | [inNextHours](../functions/functioninnexthours.md)|
| Date        | [inNextMonths](../functions/functioninnextmonths.md)|
| Date        | [inNextYears](../functions/functioninnextyears.md)|
| Date        | [now](../functions/functionnow.md)|
| Date        | [nowWithDelta](../functions/functionnowwithdelta.md)|
| Date        | [setHours](../functions/functionsethours.md)|
| Date        | [setDays](../functions/functionsetdays.md)|
| Date        | [updateTimeZone](../functions/functionupdatetimezone.md)|
| List        | [distinct](../functions/functiondistinct.md)|
| List        | [distinctWithNull](../functions/functiondistinctwithnull.md)|
| List        | [filter](../functions/functionfilter.md)|
| List        | [getListItem](../functions/functiongetlistitem.md)|
| List        | [in](../functions/functionin.md)|
| List        | [intersect](../functions/functionintersect.md)|
| List        | [limit](../functions/functionlimit.md)|
| List        | [listSize](../functions/functionlistsize.md)|
| List        | [serializeList](../functions/functionserializelist.md)|
| List        | [sort](../functions/functionsort.md)|
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
