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

## Add Days {#add-days}

The `addDays` function adjusts a given date by a specified number of days, using positive values to increment and negative values to decrement.

**Syntax**

```sql
{%= addDays(date, number) %}
```

+++Example

* Input: `{%= addDays(stringToDate("2024-11-01T17:19:51Z"),10) %}`
* Output: `2024-11-11T17:19:51Z`

+++

## Add Hours {#add-hours}

The `addHours` function adjusts a given date by a specified number of hours, using positive values to increment and negative values to decrement.

**Syntax**

```sql
{%= addHours(date, number) %}
```

+++Example

* Input: `{%= addHours(stringToDate("2024-11-01T17:19:51Z"),1) %}`
* Output: `2024-11-01T18:19:51Z`

+++

## Add Minutes {#add-minutes}

The `addMinutes` function adjusts a given date by a specified number of minutes, using positive values to increment and negative values to decrement

**Syntax**

```sql
{%= addMinutes(date, number) %}
```

+++Example

* Input: `{%= addMinutes(stringToDate("2024-11-01T17:59:51Z"),10) %}`
* Output: `2024-11-01T18:09:51Z`

+++

## Add Months {#add-months}

The `addMonths` function adjusts a given date by a specified number of months, using positive values to increment and negative values to decrement.

**Syntax**

```sql
{%= addMonths(date, number) %}
```

+++Example

* Input: `{%= addMonths(stringToDate("2024-11-01T17:19:51Z"),2) %}`
* Output: `2025-01-01T17:19:51Z`

+++

## Add Seconds {#add-seconds}

The `addSeconds` adjusts a given date by a specified number of seconds, using positive values to increment and negative values to decrement.

**Syntax**

```sql
{%= addSeconds(date, number) %}
```

+++Example

* Input: `{%= addSeconds(stringToDate("2024-11-01T17:19:51Z"),10) %}`
* Output: `2024-11-01T17:20:01Z`

+++

## Add Years {#add-years}

The `addYears` adjusts a given date by a specified number of years, using positive values to increment and negative values to decrement.

**Syntax**

```sql
{%= addYears(date, number) %}
```

+++Example

* Input: `{%= addYears(stringToDate("2024-11-01T17:19:51Z"),2) %}`
* Output: `2026-11-01T17:19:51Z`

+++

## Age{#age}

The `age` function is used to retrieve the age from a given date.

**Syntax**

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

## Age In Days {#age-days}

The `ageInDays` function calculates the age of a given date in days, i.e. the number of days elapsed between the given date and the current date, negative for future dates and positive for past dates.

**Syntax**

```sql
{%= ageInDays(date) %}
```

+++Example

currentDate = 2025-01-07T12:17:10.720122+05:30 (Asia/Kolkata)

* Input: `{%= ageInDays(stringToDate("2025-01-01T17:19:51Z"))%}`
* Output: `5`

+++

## Age In Months {#age-months}

The `ageInMonths` function calculates the age of a given date in months, i.e. the number of months elapsed between the given date and the current date , negative for future dates and positive for past dates.

**Syntax**

```sql
{%= ageInMonths(date) %}
```

+++Example

currentDate = 2025-01-07T12:22:46.993748+05:30(Asia/Kolkata)

* Input: `{%=ageInMonths(stringToDate("2024-01-01T00:00:00Z"))%}`
* Output: `12`

+++

## Compare Dates {#compare-dates}

The `compareDates` function compares the first input date with the other. Returns 0 if date1 is equal to date2, -1 if date1 comes before date2 and 1 if date1 comes after date2.

**Syntax**

```sql
{%= compareDates(date1, date2) %}
```

+++Example

* Input: `{%=compareDates(stringToDate("2024-12-02T00:00:00Z"), stringToDate("2024-12-03T00:00:00Z"))%}`
* Output: `-1`

+++

## Convert ZonedDateTime {#convert-zoned-date-time}

The `convertZonedDateTime` function converts a date-time to a given timezone.

**Syntax**

```sql
{%= convertZonedDateTime(dateTime, timezone) %}
```

+++Example

* Input: `{%=convertZonedDateTime(stringToDate("2019-02-19T08:09:00Z"), "Asia/Tehran")%}`
* Output: `2019-02-19T11:39+03:30[Asia/Tehran]`

+++

## Current time in milliseconds{#current-time}

The `currentTimeInMillis` function is used to retrieve current time in epoch milliseconds.

**Syntax**

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

**Syntax**

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

## Day of month {#day-month}

The `dayOfWeek` returns the number representing the day of the month.

**Syntax**

```sql
{%= dayOfMonth(datetime) %}
```

+++Example

* Input: `{%= dayOfMonth(stringToDate("2024-11-05T17:19:51Z")) %}`
* Output: `5`

+++


## Day of week {#day-week}

The `dayOfWeek` function is used to retrieve the day of week.

**Syntax**

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

**Syntax**

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

## Diff In Seconds {#diff-seconds}

The `diffInSeconds` function returns the difference between two dates in terms of seconds.

**Syntax**

```sql
{%= diffInSeconds(endDate, startDate) %}
```

+++Example

* Input: `{%=diffInSeconds(stringToDate("2024-11-01T17:19:51Z"), stringToDate("2024-11-01T17:19:01Z"))%}`
* Output: `50`

+++

## Extract Hours {#extract-hours}

The `extractHours` function extracts the hour component from a given timestamp.

**Syntax**

```sql
{%= extractHours(date) %}
```

+++Example

* Input: `{%= extractHours(stringToDate("2024-11-01T17:19:51Z"))%}`
* Output: `17`

+++

## Extract Minutes {#extract-minutes}

The `extractMinutes` function extracts the minute component from a given timestamp.

**Syntax**

```sql
{%= extractMinutes(date) %}
```

+++Example

* Input: `{%= extractMinute(stringToDate("2024-11-01T17:19:51Z"))%}`
* Output: `19`

+++

## Extract Months {#extract-months}

The `extractMonth` function extracts the month component from a given timestamp.

**Syntax**

```sql
{%= extractMonths(date) %}
```

+++Example

* Input: `{%=extractMonth(stringToDate("2024-11-01T17:19:51Z"))%}`
* Output: `11`

+++

## Extract Seconds {#extract-seconds}

The `extractSeconds` function extracts the second component from a given timestamp.

**Syntax**

```sql
{%= extractSeconds(date) %}
```

+++Example

* Input: `{%=extractSeconds(stringToDate("2024-11-01T17:19:51Z"))%}`
* Output: `51`

+++

## Format date{#format-date}

The `formatDate` function is used to format a date time value. The format should be a valid Java DateTimeFormat pattern.

**Syntax**

```sql
{%= formatDate(datetime, format) %}
```

Where the first string is the date attribute and the second value is how you would like the date to be converted and displayed.

>[!NOTE]
>
> If a date pattern is invalid the date will fallback to ISO standard format.
>
> You can use Java date formatting functions as summarized in [Oracle documentation](https://docs.oracle.com/javase/8/docs/api/java/time/format/DateTimeFormatter.html){_blank}

**Example**

The following operation will return the date in the following format: MM/DD/YY.

```sql
{%= formatDate(profile.timeSeriesEvents._mobile.hotelBookingDetails.bookingDate, "MM/dd/YY") %}
```

## Format date with locale support{#format-date-locale}

The `formatDate` function is used to format a date time value into its corresponding language sensitive representation, i.e in a desired locale. The format should be a valid Java DateTimeFormat pattern.

**Syntax**

```sql
{%= formatDate(datetime, format, locale) %}
```

Where the first string is the date attribute, second value is how you would like the date to be converted and displayed and the third value represents the locale in string format.

>[!NOTE]
>
> If a date pattern is invalid the date will fallback to ISO standard format.
>
> You can use Java date formatting functions as summarized in [Oracle documentation](https://docs.oracle.com/javase/8/docs/api/java/time/format/DateTimeFormatter.html).
>
> You can use formatting and valid locales as summarized in [Oracle documentation](https://docs.oracle.com/javase/8/docs/api/java/util/Locale.html) and [Supported locales](https://www.oracle.com/java/technologies/javase/jdk11-suported-locales.html).

**Example**

The following operation will return the date in the following format: MM/DD/YY and locale FRANCE.

```sql
{%= formatDate(profile.timeSeriesEvents._mobile.hotelBookingDetails.bookingDate, "MM/DD/YY", "fr_FR") %}
```

## Get CurrentZonedDateTime {#get-current-zoned-date-time}

The `getCurrentZonedDateTime` function returns the current date and time with time zone information.

**Syntax**

```sql
{%= getCurrentZonedDateTime() %}
```

+++Example

* Input: `{%= getCurrentZonedDateTime() %}`
* Output: `2024-12-06T17:22:02.281067+05:30[Asia/Kolkata]`

+++

## Hours Difference {#hours-difference}

The `diffInHours` function returns the difference between two dates in terms of hours.

**Syntax**

```sql
{%= diffInHours(endDate, startDate) %}
```

+++Example

* Input: `{%= diffInHours(stringToDate("2024-11-01T17:19:51Z"), stringToDate("2024-11-01T07:19:51Z"))%}`
* Output: `10`

+++

## Minutes Difference{#diff-minutes}

The `diffInMinutes` function is used to return the difference between two dates in terms of minutes.

**Syntax**

```sql
{%= diffInMinutes(endDate, startDate) %}
```

+++Example

* Input: `{%= diffInMinutes(stringToDate("2024-11-01T17:19:51Z"), stringToDate("2024-11-01T16:19:51Z"))%}`
* Output: `60`

+++

## Months Difference {#months-difference}

The `diffInMonths` function returns the difference between two dates in terms of months.

**Syntax**

```sql
{%= diffInMonths(endDate, startDate) %}
```

+++Example

* Input: `{%=diffInMonths(stringToDate("2024-11-01T17:19:51Z"), stringToDate("2024-08-01T17:19:51Z"))%}`
* Output: `3`

+++

## Set days{#set-days}

The `setDays` function is used to set the day of the month for the given date-time.

**Syntax**

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

**Syntax**

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

## To Date Time {#to-date-time}

The `ToDateTime` function converts string to date. It returns the epoch date as output for invalid input.

**Syntax**

```sql
{%= toDateTime(string, string) %}
```

+++Example

* Input: `{%=toDateTime("2024-11-01T17:19:51Z")%}`
* Output: `2024-11-01T17:19:51Z`

+++

## To UTC{#to-utc}

The `toUTC` function is used to convert a datetime to UTC.

**Syntax**

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

## Truncate to Start Of Day {#truncate-day}

The `truncateToStartOfDay` function is used to modify a given date-time by setting it to the start of the day with the time set to 00:00.

**Syntax**

```sql
{%= truncateToStartOfDay(date) %}
```

+++Example

* Input: `{%= truncateToStartOfDay(stringToDate("2024-11-01T17:19:51Z")) %}`
* Output: `2024-11-01T00:00Z`

+++

## truncateToStartOfQuarter {#truncate-quarter}

The `truncateToStartOfQuarter` function is used to truncate a date-time to the first day of its quarter (e.g., Jan 1, Apr 1, Jul 1, Oct 1) at 00:00.

**Syntax**

```sql
{%= truncateToStartOfQuarter(dateTime) %}
```

+++Example

* Input: `{%=truncateToStartOfQuarter(stringToDate("2024-11-01T17:19:51Z"))%}`
* Output: `2024-10-01T00:00Z`

+++

## truncateToStartOfWeek {#truncate-week}

The `truncateToStartOfWeek` function modifies a given date-time by setting it to the start of the week(Monday at 00:00).

**Syntax**

```sql
{%= truncateToStartOfWeek(dateTime) %}
```

+++Example

* Input: `truncateToStartOfWeek(stringToDate("2024-11-19T17:19:51Z"))%} // tuesday`
* Output: `2024-11-18T00:00Z // monday`

+++

## truncateToStartOfYear {#truncate-year}

The `truncateToStartOfYear` function is used to modify a given date-time by truncating it to the first day of the year (January 1st) at 00:00.

**Syntax**

```sql
{%= truncateToStartOfYear(dateTime) %}
```

+++Example

* Input: `{%=truncateToStartOfYear(stringToDate("2024-11-01T17:19:51Z"))%}`
* Output: `2024-01-01T00:00Z`

+++

## Week of year {#week-of-year}

The `weekOfYear` function is used to retrieve the week of the year.

**Syntax**

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

## Years Difference {#diff-years}

The `diffInYears` function is used to return the difference between two dates in terms of years.

**Syntax**

```sql
{%= diffInYears(endDate, startDate) %}: int
```

+++Example

* Input: `{%=diffInYears(stringToDate("2024-11-01T17:19:51Z"), stringToDate("2019-10-01T17:19:51Z"))%}`
* Output: `5`

+++
