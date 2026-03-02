---
solution: Journey Optimizer, Experience Platform
product: Journey Optimizer
title: Supported functions in the expression editor
description: Learn which personalization editor functions are supported in Decision management (Offer Decisioning).
badge: label="Legacy" type="Informative"
feature: Decision Management
topic: Integrations
role: User
level: Intermediate
version: Journey Orchestration
exl-id: c4df41a2-d740-437c-acc3-957508c4a1c0
---
# Supported functions in the expression editor {#personalization-editor-supported-functions}

In Decision management, you build expressions using the personalization editor. You use this editor in particular when:

* **Defining offer content** – when you [add representations](offer-library/add-representations.md) and personalize the offer content (images, text, links)
* **Creating decision rules** – when you [define eligibility](offer-library/creating-decision-rules.md) for offers
* **Building ranking formulas** – when you [create ranking formulas](ranking/create-ranking-formulas.md) to order offers

The Offer Decisioning backend supports only a **subset** of the functions available in the personalization editor. This page lists every function you can safely use. Expand each section to see the supported operators, helpers, and functions.

## Supported functions list {#supported-functions-list}

+++ Operators

* `+` `-` `*` `/` `%` (arithmetic)
* `and` `or` `!` (logical)
* `=` `!=` `>` `>=` `<` `<=` (comparison)

+++

+++ Helpers

* Each
* With
* If
* Unless
* Let
* Default fallback value
* fragment
* datasetLookup
* externalDataLookup (Alpha)
* Inline
* Url
* Execution Metadata
* valueAtPath

+++

+++ String functions

| Display name | Internal name |
|--------------|---------------|
| Lower case | lowerCase |
| Upper case | upperCase |
| Camel case | camelCase |
| Title case | titleCase |
| Trim | trim |
| Left Trim | leftTrim |
| Right Trim | rightTrim |
| Is Empty | isEmpty |
| Equals Ignore Case | equalsIgnoreCase |
| Not Equal With Ignore Case | notEqualWithIgnoreCase |
| Replace | replace |
| Replace All | replaceAll |
| Concat | concat |
| Split | split |
| Encode64 | encode64 |
| Length | length |
| MD5 | md5 |
| SHA256 | sha256 |
| Like | like |
| Starts with | startsWith |
| Does not start with | doesNotStartWith |
| Ends with | endsWith |
| Does not end with | doesNotEndWith |
| Contains | contains |
| Does not contain | doesNotContain |
| Equals | equals |
| Not equal to | notEqualTo |
| Matches | matches |
| Regular expression group | regexGroup |
| String to number | stringToNumber |
| String to date | stringToDate |
| To Date Time | toDateTime |
| To Date Time Only | toDateTimeOnly |
| Extract email domain | extractEmailDomain |
| Extract email username | extractEmailUsername |
| Is Not Empty | isNotEmpty |
| Index Of | indexOf |
| Last Index Of | lastIndexOf |
| Sub string | substr |
| To Bool | toBool |
| String to integer | string_to_integer |
| Mask | mask |
| Get format currency | formatCurrency |
| Get unicode value of character | charCodeAt |
| Get Qr Code for any text | qrCode |

+++

+++ Array, list and set functions

| Display name | Internal name |
|--------------|---------------|
| Distinct | distinct |
| In | in |
| Not in | notIn |
| Intersects | intersects |
| Subset of | subsetOf |
| Superset of | supersetOf |
| Includes | includes |
| Sort and get first N in array | topN |
| Sort and get last N in array | bottomN |
| First item | head |
| Count | count |
| Sum | sum |
| Average | average |
| Minimum | min |
| Maximum | max |

+++

+++ Map functions

| Display name | Internal name |
|--------------|---------------|
| Get | get |
| Keys | keys |
| Values | values |

+++

+++ Object functions

| Display name | Internal name |
|--------------|---------------|
| Is null | isNull |
| Is not null | isNotNull |

+++

+++ Math functions

| Display name | Internal name |
|--------------|---------------|
| To Percentage | toPercentage |
| Round Up | roundUp |
| Round down | roundDown |
| To Precision | toPrecision |
| Absolute | absolute |
| Random | random |
| To Hexadecimal | toHexString |
| Get number to locale | formatNumber |
| To String | toString |
| To Int | toInt |
| To Long | toLong |

+++

+++ Date time functions

| Display name | Internal name |
|--------------|---------------|
| Now | now |
| Get CurrentZonedDateTime | getCurrentZonedDateTime |
| To Date | toDate |
| To Time | toTime |
| To Date Time | toDateTime |
| To Date Time Only | toDateTimeOnly |
| To Date Only | toDateOnly |
| To Time Only | toTimeOnly |
| To Time Zone | toTimeZone |
| Format date | formatDate |
| Format date time | formatDateTime |
| Format time | formatTime |
| Parse date | parseDate |
| Parse date time | parseDateTime |
| Parse time | parseTime |
| Add Days | addDays |
| Add Months | addMonths |
| Add Years | addYears |
| Add Hours | addHours |
| Add Minutes | addMinutes |
| Add Seconds | addSeconds |
| Subtract Days | subtractDays |
| Subtract Months | subtractMonths |
| Subtract Years | subtractYears |
| Subtract Hours | subtractHours |
| Subtract Minutes | subtractMinutes |
| Subtract Seconds | subtractSeconds |
| Difference in Days | diffDays |
| Difference in Months | diffMonths |
| Difference in Years | diffYears |
| Difference in Hours | diffHours |
| Difference in Minutes | diffMinutes |
| Difference in Seconds | diffSeconds |
| Start of day | startOfDay |
| End of day | endOfDay |
| Is Before | isBefore |
| Is After | isAfter |

+++

+++ URL functions

| Display name | Internal name |
|--------------|---------------|
| Encode URL | encodeUrl |
| Decode URL | decodeUrl |
| Get URL query param | getUrlQueryParam |
| Get URL protocol | getUrlProtocol |
| Get URL host | getUrlHost |

+++

>[!NOTE]
>
>If you use a function that is not in the list above, the expression may fail at runtime or produce unexpected results. For the full set of functions available in [!DNL Journey Optimizer] personalization, see [Helper functions list](../personalization/functions/functions.md). Only the subset documented on this page is supported in Offer Decisioning.
