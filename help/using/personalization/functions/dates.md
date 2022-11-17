---
title: Date Time functions library
description: Date Time functions library
feature: Personalization
topic: Personalization
role: Data Engineer
level: Experienced
exl-id: edc040de-dfb3-4ebc-91b4-239e10c2260b
---
# Date Time Functions{#date-time}

Date and time functions are used to perform date and time operations on values within Journey Optimizer.

## Age{#age}

The `age` function is used to retrieve the age from a given date.

**Format**

```sql
 {%= age(datetime) %}
```

<!--
**Example**

The following operation gets the value of the identity map for the key `example@example.com`.

```sql
 {%= age(datetime) %}
```
-->

## Current time in milliseconds{#current-time}

The `currentTimeInMillis` function is used to retrieve current time in epoch milliseconds.

**Format**

```sql
{%= currentTimeInMillis() %}
```

<!--
**Example**

The following operation gets all the keys for the map `identityMap`.

```sql
{%= keys(identityMap) %}
```
-->

## Date difference{#date-diff}

The `dateDiff` function is used to retrieve the difference between two dates in number of days.

**Format**

```sql
{%= dateDiff(datetime,datetime) %}
```

<!--
**Example**

The following operation gets all the values for the map `identityMap`.

```sql
{%= values(identityMap) %}
```
-->


## Day of week{#day-week}

The `dayOfWeek` function is used to retrieve the day of week.

**Format**

```sql
{%= dayOfWeek(datetime) %}
```

<!--
**Example**

The following operation gets all the values for the map `identityMap`.

```sql
{%= values(identityMap) %}
```
-->

## Day of year{#day-year}

The `dayOfYear` function is used to retrieve the day of year.

**Format**

```sql
{%= dayOfYear(datetime) %}
```

<!--
**Example**

The following operation gets all the values for the map `identityMap`.

```sql
{%= values(identityMap) %}
```
-->

## Format date{#format-date}

The `formatDate` function is used to format a date time value. The format should be a valid Java DateTimeFormat pattern.

**Format**

```sql
{%= formatDate(datetime, format) %}
```

Where the first string is the date attribute and the second value is how you would like the date to be converted and displayed.

>[!NOTE]
>
> If a date pattern is invalid the date will fallback to ISO standard format.
>
> You can use Java date formatting functions as summarized [in Oracle documentation](https://docs.oracle.com/javase/8/docs/api/java/time/format/DateTimeFormatter.html){_blank}

**Example**

The following operation will return the date in the following format: MM/DD/YY.

```sql
{%= formatDate(profile.timeSeriesEvents._mobile.hotelBookingDetails.bookingDate, "MM/DD/YY") %}
```

## Set days{#set-days}

The `setDays` function is used to set the day of the month for the given date-time.

**Format**

```sql
{%= setDays(datetime, day) %}
```

<!--
**Example**

The following operation gets all the values for the map `identityMap`.

```sql
{%= values(identityMap) %}
```
-->

## Set hours{#set-hours}

The `setHours` function is used to set the hour of the date-time.

**Format**

```sql
{%= setHours(datetime, hour) %}
```

<!--
**Example**

The following operation gets all the values for the map `identityMap`.

```sql
{%= values(identityMap) %}
```
-->


## To UTC{#to-utc}

The `toUTC` function is used to convert a datetime to UTC.


**Format**

```sql
{%= toUTC(datetime) %}
```

<!--
**Example**

The following operation gets all the values for the map `identityMap`.

```sql
{%= values(identityMap) %}
```
-->


## Week of year UTC{#week-of-year}

The `weekOfYear` function is used to retrieve the week of the year.

**Format**

```sql
{%= weekOfYear(datetime) %}
```

<!--
**Example**

The following operation gets all the values for the map `identityMap`.

```sql
{%= values(identityMap) %}
```
-->
