---
solution: Journey Optimizer
product: journey optimizer
title: Operators
description: Learn about operators in advanced expressions
feature: Journeys
role: Data Engineer, Architect
level: Experienced
keywords: expression, syntax, operators, editor, journey
exl-id: 706e2e02-9bd9-46e7-a73d-dda3c9ae4ba8
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
