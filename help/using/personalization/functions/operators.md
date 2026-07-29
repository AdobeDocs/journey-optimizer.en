---
title: Operators functions library
description: Operators functions library
feature: Personalization
topic: Personalization
role: Developer
level: Experienced
exl-id: 75b0b380-d9a6-418e-b9f6-e64de385ba8d
TQID: https://experienceleague.adobe.com/b4Tz4auDyWb-iaUYAie31DL5hlHh97n3rYm7EP-JjIw
product_v2:
  - id: cb954087-f4fc-4456-afb9-e939cabcdc79
    internal-label: Journey Optimizer
role_v2:
  - id: ff6a42d2-313e-452e-93a6-792e4fad9ff8
    internal-label: Developer
topic_v2:
  - id: e0eb8757-182f-49f3-94a4-1587d16f5094
    internal-label: Personalization
feature_v2:
  - id: fda7be7c-b81e-42c0-95a9-616e5b893c03
    internal-label: Build expressions
subfeature_v2: []
---
# Operators {#operators}

## Boolean functions {#boolean-functions}

Boolean functions are used to perform boolean logic on different elements.

### And{#and}

The `and` function is used to create a logical conjunction.

**Syntax**

```sql
{%= query1 and query2 %}
```

**Example**

The following operation will return all people with home country as France and birth year of 1985.

```sql
{%= profile.homeAddress.country = "France" and profile.person.birthYear = 1985 %}
```

### Or{#or}

The `or` function is used to create a logical disjunction.

**Syntax**

```sql
{%= query1 or query2 %}
```

**Example**

The following operation will return all people with home country as France or birth year of 1985.

```sql
{%= profile.homeAddress.country = "France" or profile.person.birthYear = 1985 %}
```

<!--
## Not{#not}

The `not` (or `!`) function is used to create a logical negation.

**Syntax**

```sql
not ({QUERY})
!({QUERY})
```

**Example**

The following operation will return all people who do not have their home country as Canada.

```sql
not (homeAddress.countryISO = "CA")
```
-->

## Comparison functions {#comparison-functions}

Comparison functions are used to compare between different expressions and values, returning true or false accordingly. 

### Equals{#equals}

The `=` (equals) function checks whether one value or expression is equal to another value or expression.

**Syntax**

```sql
{%= expression = value %}
```

**Example**

The following operation checks if the home address country is France.

```sql
{%= profile.homeAddress.country = "France" %}
```

### Not equal{#notequal}

The `!=` (not equal) function checks whether one value or expression is **not** equal to another value or expression.

**Syntax**

```sql
{%= expression != value %}
```

**Example**

The following operation checks if the home address country is not France.

```sql
{%= profile.homeAddress.country != "France" %}
```

### Greater than{#greaterthan}

The `>` (greater than) function is used to check if the first value is greater than the second value.

**Syntax**

```sql
{%= expression1 > expression2 %}
```

**Example**

The following operation defines people born strictly after 1970.

```sql
{%= profile.person.birthYear > 1970 %}
```

### Greater than or equal to{#greaterthanorequal}

The `>=` (greater than or equal to) function is used to check if the first value is greater than or equal to the second value.

**Syntax**

```sql
{%= expression1 >= expression2 %}
```

**Example**

The following operation defines people born in or after 1970.

```sql
{%= profile.person.birthYear >= 1970 %}
```

### Less than{#lessthan}

The `<` (less than) comparison function is used to check if the first value is less than the second value.

**Syntax**

```sql
{%= expression1 < expression2 %}
```

**Example**

The following operation defines people born before 2000.

```sql
{%= profile.person.birthYear < 2000 %}
```

### Less than or equal to{#lessthanorequal}

The `<=` (less than or equal to) comparison function is used to check if the first value is less than or equal to the second value.

**Syntax**

```sql
{%= expression1 <= expression2 %}
```

**Example**

The following operation defines people born in 2000 or before.

```sql
{%= profile.person.birthYear <= 2000 %}
```

**Operations with numbers**

## Template Migration Functions {#template-migration-functions}

Template Migration Functions are available in the personalization editor to assist with migrating existing templates to Journey Optimizer.

### Compare via operator{#amp-compare}

The `ampCompare` function compares two values using the specified comparison operator.

**Syntax**

```sql
{%= ampCompare(value1, value2, operator) %}
```

| Argument | Description |
| --------- | ----------- |
| `value1` | First value to compare. |
| `value2` | Second value to compare. |
| `operator` | Integer representing the comparison operator to use. |

**Example**

```sql
{%= ampCompare(profile.person.age, 18, 4) %}
```

### Substring range{#amp-substr}

The `ampSubstr` function returns a portion of a string between the specified start and end indices.

**Syntax**

```sql
{%= ampSubstr(string, startIndex, endIndex) %}
```

| Argument | Description |
| --------- | ----------- |
| `string` | The source string. |
| `startIndex` | Start index of the substring (integer). |
| `endIndex` | End index of the substring (integer). |

**Example**

The following expression returns the first five characters of the string "Hello World".

```sql
{%= ampSubstr("Hello World", 0, 5) %}
```

Returns `Hello`.

### Compare To{#compare-to}

The `compareTo` function compares two strings lexicographically. It returns a negative integer if the first string comes before the second, zero if they are equal, or a positive integer if the first string comes after the second.

**Syntax**

```sql
{%= compareTo(string1, string2) %}
```

| Argument | Description |
| --------- | ----------- |
| `string1` | First string to compare. |
| `string2` | Second string to compare. |

**Example**

```sql
{%= compareTo("apple", "banana") %}
```
