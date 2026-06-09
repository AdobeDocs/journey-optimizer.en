---
solution: Journey Optimizer
product: journey optimizer
title: Operators
description: Learn about operators in advanced expressions
feature: Journeys
role: Developer
level: Experienced
keywords: expression, syntax, operators, editor, journey
exl-id: 706e2e02-9bd9-46e7-a73d-dda3c9ae4ba8
version: Journey Orchestration
TQID: https://experienceleague.adobe.com/sK2GNHkkiJ4M5V99Uucc-b68iESNW7kCNBjHVNT-dMs
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
# Operators {#operators}

There are two kinds of operators: unary operators and binary operators. There are left-hand unary operators and right-hand unary operators.

```json
// left-hand unary operators
// <operator> <operand> 
// operand is an expression
not (@event{LobbyBeacon.endUserIDs._experience.emailid.id}=="example@adobe.com")

// right-hand unary operators
// <operator> <operand> 
// operand is an expression
@event{LobbyBeacon.endUserIDs._experience.emailid.id} is not null

// binary operators
// <operand1> <operator> <operand2>
// operand is an expression
(@event{LobbyBeacon.endUserIDs._experience.emailid.id}=="example1@adobe.com") or (@event{LobbyBeacon.endUserIDs._experience.emailid.id}=="example2@adobe.com") 
```

## Important notes{#important-notes}

* When using a multiplication (`*`), both operation fields must have the same type, either integer or decimal. Example : 
   * the following example is correct: `3.0 * 4.0`
   * `3 * 4.0` will lead to an error

* When using the `+` operator, the expression needs to be encapsulated in parentheses. Example:
   * `toDateTimeOnly(toDateTime((currentTimeInMillis()) + 1))` is correct
   * `toDateTimeOnly(toDateTime(currentTimeInMillis() + 1))` will lead to an error

## Logical  {#logical}

### and

```json
<expression1> and <expression2>
```

Both &lt;expression1&gt; and &lt;expression2&gt; must be boolean. The result is boolean.

Example:

```json
3.14 > 2 and 3.15 < 1
```

### or

```json
<expression1> or <expression2>
```

Both &lt;expression1&gt; and &lt;expression2&gt; must be boolean. The result is boolean.

Example:

```json
3.14 > 2 or 3.15 < 1
```

### not

```json
not <expression>
```

&lt;expression&gt; must be boolean. The result is boolean.

Example:

```json
not 3.15 < 1
```

## Comparison {#comparison}

### is null

```json
<expression> is null
```

The result is boolean.

Note that null means the expression has no evaluated value.

Example:

```json
@event{BarBeacon.location} is null
```

### is not null

```json
<expression> is not null
```

The result is boolean.

Note that null means the expression has no evaluated value.

Example:

```json
@event{BarBeacon.location} is not null
```

### has null

```json
<expression> has null
```

&lt;expression&gt; must be a list. The result is boolean.

Useful to identify that a list contains at least one null value.

Example:

```json
["foo", "bar", null] has null
```

Returns true

```json
["foo", "bar", ""] has null
```

Returns false because "" is not considered as null.

### ==

```json
<expression1> == <expression2>
```

>[!NOTE]
>
>For &lt;expression1&gt; and &lt;expression2&gt; there is no data type control. 

Example:

```json
3.14 == 42
```

```json
"foo" == "bar"
```

### !=

```json
<expression1> != <expression2>
```

>[!NOTE]
>
>For &lt;expression1&gt; and &lt;expression2&gt; there is no data type control. 

The result is boolean.

Example:

```json
3.14 != 42
```

```json
"foo" != "bar"
```

### >

```json
<expression1> > <expression2>
```

Datetime can be compared with Datetime.

Datetimeonly can be compared with Datetimeonly.

Both integer or decimal can be compared with both integer or decimal.

Any other combination is forbidden.

The result is boolean.

Example:

```json
3.14 > 42
```

### >=

```json
<expression1> >= <expression2>
```

Datetime can be compared with Datetime.

Datetimeonly can be compared with Datetimeonly.

Both integer or decimal can be compared with both integer or decimal.

Any other combination is forbidden.

The result is boolean.

Example:

```json
42 >= 3.14
```

### <

```json
<expression1> < <expression2>
```

Datetime can be compared with Datetime.

Datetimeonly can be compared with Datetimeonly.

Both integer or decimal can be compared with both integer or decimal.

Any other combination is forbidden.

The result is boolean.

Example:

```json
42 < 3.14
```

### <=

```json
<expression1> <= <expression2>
```

Datetime can be compared with Datetime.

Datetimeonly can be compared with Datetimeonly.

Both integer or decimal can be compared with both integer or decimal.

Any other combination is forbidden.

The result is boolean.

Example:

```json
42 <= 3.14
```

## Arithmetic {#arithmetic}

### +

```json
<expression1> + <expression2>
```

Both expressions must be numeric (integer or decimal). 

The result is also numeric.

Example:

```json
1 + 2
```

Returns 3

### -

```json
<expression1> - <expression2>
```

Both expressions must be numeric (integer or decimal).

The result is also numeric.

Example:

```json
2 - 1 
```

Returns 1

### /

```json
<expression1> / <expression2>
```

Both expressions must be numeric (integer or decimal). 

The result is also numeric.

&lt;expression2&gt; must not be equal to 0 (returns 0).

Example:

```json
4 / 2
```

Returns 2

### *

```json
<expression1> * <expression2>
```

Both expressions must be numeric (integer or decimal).

The result is also numeric.

Example:

```json
3 * 4
```

Returns 12

### %

```json
<expression1> % <expression2>
```

Both expressions must be numeric (integer or decimal).

The result is also numeric.

Example:

```json
3 % 2
```

Returns 1.

## Math {#math}

### is numeric

```json
<expression> is numeric
```

The type of the expression is integer or decimal.

Example:

```json
@ is numeric
```

### is integer

```json
<expression> is integer
```

The type of the expression is integer.

Example:

```json
@ is integer
```

### is decimal

```json
<expression> is decimal
```

The type of the expression is decimal.

Example:

```json
@ is decimal
```

## String {#string}

### + 

```json
<string> + <expression>
```

```json
<expression> + <string>
```

It concatenates two expressions. 

One expression must be a chained string.

Example:

```json
"the current time is " + (now())
```

Returns "the current time is 2023-09-23T09:30:06.693Z"

```json
(now()) + " is the current time"
```

Returns "2023-09-23T09:30:06.693Z is the current time"

```json
"a" + "b" + "c" + 1234
```

Returns "abc1234".

## Date {#date}

### +

```json
<expression> + <duration>
```

Append a duration to a dateTime, a dateTimeOnly or a duration.

Example:

```json
(toDateTime("2023-12-03T15:15:30Z")) + (toDuration("PT15M"))  
```

Returns a _dateTime_ 2023-12-03T15:30:30Z

```json
(toDateTimeOnly("2023-12-03T15:15:30")) + (toDuration("PT15M"))
```

Returns a _dateTimeOnly_ 2023-12-03T15:30:30 

```json
(now()) + (toDuration("PT1H"))
```

Returns a _dateTime_ (with UTC time zone) one hour later from current time

```json
(toDuration("PT1H")) + (toDuration("PT1H"))
```

Returns a _duration_ PT2H

+++AI Assistant — Page context

* **TL;DR:** This page is a complete reference of operators available in the Journey advanced expression editor, covering logical (`and`, `or`, `not`), comparison (`==`, `!=`, `>`, `>=`, `<`, `<=`, `is null`, `is not null`, `has null`), arithmetic (`+`, `-`, `/`, `*`, `%`), math type-check (`is numeric`, `is integer`, `is decimal`), string concatenation, and date arithmetic operators.

**Intents:**

* Combine boolean conditions using logical operators `and`, `or`, and `not`
* Check whether a field or expression value is null or not null using `is null` / `is not null`
* Detect null values within a list using the `has null` operator
* Compare numeric, datetime, and datetimeonly values using `>`, `>=`, `<`, `<=`, `==`, and `!=`
* Perform arithmetic on numeric values using `+`, `-`, `/`, `*`, and `%`
* Add a duration to a dateTime, dateTimeOnly, or duration value using the `+` operator

**Glossary:**

* **Unary operator**: An operator applied to a single operand; can be left-hand (e.g. `not`) or right-hand (e.g. `is null`) *(product-specific)*
* **Binary operator**: An operator applied between two operands (e.g. `and`, `==`, `+`) *(product-specific)*
* **has null**: A right-hand unary operator that returns true if a list contains at least one null element *(product-specific)*
* **is numeric / is integer / is decimal**: Type-check operators that return a boolean based on the numeric subtype of the expression *(product-specific)*

**Guardrails:**

* When using multiplication (`*`), both operands must be the same numeric type (both integer or both decimal) — mixing types causes an error
* When using the `+` operator for date arithmetic, the expression must be wrapped in parentheses to avoid parsing errors
* Comparison operators (`>`, `>=`, `<`, `<=`) are only valid between compatible types: Datetime with Datetime, DatetimeOnly with DatetimeOnly, or numeric with numeric — any other combination is forbidden
* An empty string `""` is not considered null — `has null` returns false for a list containing `""`
* The `==` and `!=` operators perform no data type control between operands

**Terminology:**

* Canonical name: Operators — Acronym: none — variants: expression operators, journey operators
* Synonyms: `and` = "logical AND"; `or` = "logical OR"; `not` = "logical NOT"; `%` = "modulo"
* Do not confuse: `is null` (expression has no evaluated value) ≠ `== null` (not a valid syntax); `has null` (list contains null) ≠ `is null` (expression itself is null)

**FAQ:**

* **Q: Can I multiply an integer by a decimal directly?** — No; both operands of `*` must be the same type. Use `3.0 * 4.0` (both decimal) or `3 * 4` (both integer).
* **Q: How do I add 15 minutes to a dateTime?** — Use `(toDateTime("...")) + (toDuration("PT15M"))`.
* **Q: What is the difference between `is null` and `has null`?** — `is null` checks whether a single expression has no evaluated value; `has null` checks whether a list contains at least one null element.
* **Q: Does `"" has null` return true?** — No; an empty string is not considered null, so the result is false.
* **Q: Why does `3 * 4.0` cause an error?** — The `*` operator requires both operands to be the same numeric type; mixing integer and decimal is not allowed.

+++
