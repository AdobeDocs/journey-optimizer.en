---
title: Operators functions library
description: Operators functions library
feature: Personalization
topic: Personalization
role: Developer
level: Experienced
exl-id: 75b0b380-d9a6-418e-b9f6-e64de385ba8d
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
