---
title: Math functions library
description: Math functions library
feature: Personalization
topic: Personalization
role: Data Engineer
level: Experienced
exl-id: b9149ad6-2be7-4bdf-82eb-7ab52780cb4e
---
# Math Functions {#math}

Learn how to use Math functions in the Expression editor.

## Absolute {#absolute}

The `absolute` function is used to convert a number it's absolute value.

**Syntax**

```sql
{%= absolute(int) %}: int
```

## formatNumber {#format-number}

The `formatNumber` function is used to format any number into its language-sensitive representation.

It accepts a number and a string representing the locale, and returns a formatted string of the number in the desired locale.

**Syntax**

```sql
{%= formatNumber(number/double,string) %}: string
```

You can use formatting and valid locales as summarized in [Oracle documentation](https://docs.oracle.com/javase/8/docs/api/java/util/Locale.html) and [Supported locales](https://www.oracle.com/java/technologies/javase/jdk11-suported-locales.html){_blank}

**Example**

This query returns a formatted string in Arabic corresponding to 123456.789 as input number.

```sql
{%= formatNumber(123456.789, "ar_EG") %}
```

## Random {#random}

The `random` function is used to return a random value between 0 and 1.

**Syntax**

```sql
{%= random() %}: double
```

## Round down {#round-down}

The `roundDown` function is used to round down a number.

**Syntax**

```sql
{%= roundDown(double) %}: double
```

## Round Up {#round-up}

The `Count only null` function is used round up a number.

**Syntax**

```sql
{%= roundUp(double) %}: double
```

## To hex string {#to-hex-string}

The `toHexString` function converts any number into its hexadecimal string.

**Syntax**

```sql
{%= toHexString(number) %}: string
```

**Example**

This query returns the hexadecimal value of 158 i.e 9e.

```sql
{%= toHexString(158) %}
```

## To Int {#to-int}

The `toInt` function is used to convert any of these types (number, double, int, long, float, short, byte, boolean, string) into an integer.

**Syntax**

```sql
{%= toInt(<valueToConvert>) %}: integer
```

**Example**

This query returns the integer value of 42,6 i.e 42.

```sql
{%= toInt(42.6) %}: integer
```

## To Percentage {#to-percentage}

The `toPercentage` function is used to convert a number to percentage.

**Syntax**

```sql
{%= toPercentage(double) %}: string
```

## To Precision {#to-precision}

The `toPrecision` function is used to convert a number to required precision.

**Syntax**

```sql
{%= toPrecision(double,int) %}: string
```

## To string {#to-string}

The **toString** function converts any number into its string representation. 

**Syntax**

```sql
{%= toString(string) %}: string
```

**Example**

This query returns "12".

```sql
{%= toString(12) %} 
```
