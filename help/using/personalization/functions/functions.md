---
title: Get started with Helper functions
description: Journey Optimizer Helper functions library
feature: Personalization
topic: Personalization
role: Data Engineer
level: Experienced
exl-id: 9b0b0d8e-a819-4d2e-a241-f3c4d104eab9
---
# Get started with Helper functions{#functions}

Use [!DNL Journey Optimizer] templating language to perform operations on data, such as calculations, data formatting or conversions, conditions, and manipulate them in the context of personalization. Learn personalization syntax guidelines in [this page](../personalization-syntax.md).



➡️ [Learn how to use helper functions in this video](#video)

Templating language is leveraged in helper functions available in personalization drop-down list of the personalization editor, as below:

![](../assets/access-helper-functions.png)

>[!NOTE]
>
>The functions and capabilities available in the personalization editor differ from the ones available in the [Journey advanced expression editor](../../building-journeys/expression/expressionadvanced.md).  

In the [!DNL Journey Optimizer] personalization editor, helper functions are grouped into three categories: [Functions](#functions-helper), [Helpers](#helper-helper) and [Operators](#operators-helper).

Select a category, to access sub-categories and functions.

Access to sub-categories by clicking the `>` icon. Select a function by clicking on the `+` icon: the function is automatically added to the personalization screen. 

Click the `...` icon to view the description of the function and add it to your favorites. [Learn more](../personalize.md#fav)

## Functions{#functions-helper}

### Aggregation and Array Functions
 
<table>
    <tr>
        <td><a href="aggregation.md#average">Average</a></td><td>This function returns the arithmetic mean of all the selected values within the array</td>
    </tr>
    <tr>
        <td><a href="aggregation.md#count">Count</a></td><td>This function returns the number of elements within the given array</td>
    </tr>
    <tr>
        <td><a href="aggregation.md#count-only-null">Count Only Null</a></td><td>This function counts the number of null values in the list.</td>
    </tr>
    <tr>
        <td><a href="aggregation.md#count-with-null">Count With Null</a></td><td>This function counts all the elements of the list including null values</td>
    </tr>
    <tr>
        <td><a href="arrays-list.md#distinct">Distinct</a></td><td>This function gets values from an array or a list with duplicate values removed</td>
    </tr>
    <tr>
        <td><a href="arrays-list.md#distinct-count-with-null">Distinct Count With Null</a></td><td>This function counts the number of different values including the null values</td>
    </tr>
    <tr>
        <td><a href="arrays-list.md#head">First item</a></td><td>This function returns the first item in an array or a list</td>
    </tr>
    <tr>
        <td><a href="arrays-list.md#first-n">First n in array</a></td><td>This function returns the first `N` items in an array, when sorted in ascending order based on the given numerical expression</td>
    </tr>
    <tr>
        <td><a href="arrays-list.md#in">In</a></td><td>This function is used to determine if an item is a member of an array or list</td>
    </tr>
    <tr>
        <td><a href="arrays-list.md#includes">Includes</a></td><td>This function determines if an array or list contains a given item</td>
    </tr>
    <tr>
        <td><a href="arrays-list.md#intersects">Intersects</a></td><td>This function determines if two arrays or lists have at least one common member</td>
    </tr>
    <tr>
        <td><a href="arrays-list.md#last-n">Last n in array</a></td><td>This function returns the last `N` items in an array, when sorted in ascending order based on the given numerical expression</td>
    </tr>
    <tr>
        <td><a href="aggregation.md#max">Maximum</a></td><td>This function returns the largest of all the selected values within an array</td>
    </tr>
    <tr>
        <td><a href="aggregation.md#min">Minimum</a></td><td>This function returns the smallest of all the selected values within the array</td>
    </tr>
    <tr>
        <td><a href="arrays-list.md#notin">Not in</a></td><td>This function determines if an item is not a member of an array or list</td>
    </tr>
    <tr>
        <td><a href="arrays-list.md#subset">Subset of</a></td><td>This function determines if a specific array (array A) is a subset of another array (array B), i.e. if all elements in array A are elements of array B</td>
    </tr>
    <tr>
        <td><a href="aggregation.md#sum">Sum</a></td><td>This function returns the sum of all the selected values within the array</td>
    </tr>
    <tr>
    <td><a href="arrays-list.md#superset">Superset of</a></td><td>This function determines if a specific array (array A) is a superset of another array (array B), i.e. if that array A contains all elements in array B</td>
    </tr>
</table>

### Date Time Functions{#date-functions}

<table>
    <tr>
        <td><a href="dates.md#add-days">Add Days</a></td><td>This function adjusts a given date by a specified number of days, using positive values to increment and negative values to decrement.</td>
    </tr>
    <tr>
        <td><a href="dates.md#add-hours">Add Hours</a></td><td>This function adjusts a given date by a specified number of hours, using positive values to increment and negative values to decrement.</td>
    </tr>
    <tr>
        <td><a href="dates.md#add-minutes">Add Minutes</a></td><td>This function adjusts a given date by a specified number of minutes, using positive values to increment and negative values to decrement.</td>
    </tr>
    <tr>
        <td><a href="dates.md#add-months">Add Months</a></td><td>This function adjusts a given date by a specified number of months, using positive values to increment and negative values to decrement.</td>
    </tr>
    <tr>
        <td><a href="dates.md#add-seconds">Add Seconds</a></td><td>This function adjusts a given date by a specified number of seconds, using positive values to increment and negative values to decrement.</td>
    </tr>
    <tr>
        <td><a href="dates.md#add-years">Add Years</a></td><td>This function adjusts a given date by a specified number of years, using positive values to increment and negative values to decrement.</td>
    </tr>
    <tr>
        <td><a href="dates.md#age">Age</a></td><td>This function retrieves the age from a given date.</td>
    </tr>
    <tr>
        <td><a href="dates.md#age-days">Age In Days</a></td><td>This function calculates the age of a given date in days, i.e. the number of days elapsed between the given date and the current date, negative for future dates and positive for past dates.</td>
    </tr>
    <tr>
        <td><a href="dates.md#age-months">Age In Months</a></td><td>This function calculates the age of a given date in months, i.e. the number of months elapsed between the given date and the current date , negative for future dates and positive for past dates.</td>
    </tr>
    <tr>
        <td><a href="dates.md#compare-dates">Compare Dates</a></td><td>This function compares the first input date with the other. Returns 0 if date1 is equal to date2, -1 if date1 comes before date2 and 1 if date1 comes after date2.</td>
    </tr>
    <tr>
        <td><a href="dates.md#convert-zoned-date-time">Convert ZonedDateTime</a></td><td>This function converts a date-time to a given timezone.</td>
    </tr>
    <tr>
        <td><a href="dates.md#current">Current time in milliseconds</a></td><td>This function retrieves current time in epoch millisecond.</td>
    </tr>
    <tr>
        <td><a href="dates.md#date-diff">Date difference</a></td><td>This function retrieves the difference between two dates in number of days.</td>
    </tr>
    <tr>
        <td><a href="dates.md#day-month">Day of month</a></td><td>This function returns the number representing the day of the month.</td>
    </tr>
    <tr>
        <td><a href="dates.md#day-week">Day of week</a></td><td>This function retrieves the day of week.</td>
    </tr>
    <tr>
        <td><a href="dates.md#day-year">Day of year</a></td><td>This function retrieves the day of year.</td>
    </tr>
    <tr>
        <td><a href="dates.md#diff-seconds">Diff In Seconds</a></td><td>This function returns the difference between two dates in terms of seconds.</td>
    </tr>
    <tr>
        <td><a href="dates.md#extract-hours">Extract Hours</a></td><td>This function extracts the hour component from a given timestamp.</td>
    </tr>
    <tr>
        <td><a href="dates.md#extract-minutes">Extract Minutes</a></td><td>This function extracts the minute component from a given timestamp.</td>
    </tr>
    <tr>
        <td><a href="dates.md#extract-months">Extract Months</a></td><td>This function extracts the month component from a given timestamp.</td>
    </tr>
    <tr>
        <td><a href="dates.md#extract-seconds">Extract Seconds</a></td><td>This function extracts the second component from a given timestamp.</td>
    </tr>
    <tr>
        <td><a href="dates.md#format-date">Format date</a></td><td>This function formats a date time value.</td>
    </tr>
    <tr>
        <td><a href="dates.md#format-date-locale">Format date with locale support</a></td><td>This function formats a date time value into its corresponding language sensitive representation, i.e in a desired locale.</td>
    </tr>
    <tr>
        <td><a href="dates.md#get-current-zoned-date-time">Get CurrentZonedDateTime</a></td><td>This function returns the current date and time with time zone information.</td>
    </tr>
    <tr>
        <td><a href="dates.md#hours-difference">Hours Difference</a></td><td>This function returns the difference between two dates in terms of hours.</td>
    </tr>
    <tr>
        <td><a href="dates.md#diff-minutes">Minutes Difference</a></td><td>This function returns the difference between two dates in terms of minutes.</td>
    </tr>
    <tr>
        <td><a href="dates.md#months-difference">Months Difference</a></td><td>This function returns the difference between two dates in terms of months.</td>
    </tr>
    <tr>
        <td><a href="dates.md#set-days">Set Days</a></td><td>This function sets the day of the month for the given date-time.</td>
    </tr>
    <tr>
        <td><a href="dates.md#set-hours">Set Hours</a></td><td>This function sets the hour of the date-time.</td>
    </tr>
    <tr>
        <td><a href="dates.md#to-date-time">To Date Time</a></td><td>This function converts string to date. It returns the epoch date as output for invalid input.</td>
    </tr>
    <tr>
        <td><a href="dates.md#to-utc">To UTC</a></td><td>This function converts a datetime to UTC.</td>
    </tr>
    <tr>
        <td><a href="dates.md#truncate-day">Truncate to Start Of Day</a></td><td>This function modifies a given date-time by setting it to the start of the day with the time set to 00:00.</td>
    </tr>
    <tr>
        <td><a href="dates.md#truncate-quarter">truncateToStartOfQuarter</a></td><td>This function truncates a date-time to the first day of its quarter (e.g., Jan 1, Apr 1, Jul 1, Oct 1) at 00:00.
</td>
    </tr>
    <tr>
        <td><a href="dates.md#truncate-week">truncateToStartOfWeek</a></td><td>This function modifies a given date-time by setting it to the start of the week(Monday at 00:00).</td>
    </tr>
    <tr>
        <td><a href="dates.md#truncate-year">truncateToStartOfYear</a></td><td>This function modifies a given date-time by truncating it to the first day of the year (January 1st) at 00:00.</td>
    </tr>
    <tr>
        <td><a href="dates.md#week-of-year">Week of year</a></td><td>This function returns the week of the year</td>
    </tr>
    <tr>
        <td><a href="dates.md#diff-years">Years Difference</a></td><td>This function returns the difference between two dates in terms of years.</td>
    </tr>
</table>
</table>

### Map Functions {#map-functions}

<table>
    <tr>
        <td><a href="maps.md#get">Get</a></td><td>This function is used to retrieve the value of a map for a given key</td>
    </tr>
    <tr>
        <td><a href="maps.md#keys">Keys</a></td><td>This function is used to retrieve all the keys for a given map</td>
    </tr>
    <tr>
        <td><a href="maps.md#values">Values</a></td><td>This function retrieves all the values of a given map</td>
    </tr>
</table>

### Math Functions {#math-functions}

<table>
    <tr>
        <td><a href="math.md#absolute">Absolute</a></td><td>This function formats any number into its language-sensitive representation.</td>
    </tr>
    <tr>
        <td><a href="math.md#format-number">Format number</a></td><td>This function formats any number into its language-sensitive representation.</td>
    </tr>
    <tr>
        <td><a href="math.md#random">Random</a></td><td>This function returns a random value between 0 and 1</td>
    </tr>
    <tr>
        <td><a href="math.md#round-down">Round down</a></td><td>This function rounds down a number</td>
    </tr>
    <tr>
        <td><a href="math.md#round-up">Round up</a></td><td>This function rounds up a number</td>
    </tr>
    <tr>
    <td><a href="math.md#to-hex-string">To hex string</a></td><td>cconverts any number into its hexadecimal string.</td>
    </tr>
    <tr>
    <td><a href="math.md#to-int">ToInt</a></td><td>Converts any of these types (number, double, int, long, float, short, byte, boolean, string) into an integer.</td>
    </tr>
    <tr>
        <td><a href="math.md#to-percentage">To percentage</a></td><td>This function converts a number to percentage</td>
    </tr>
    <tr>
        <td><a href="math.md#to-precision">To precision</a></td><td>This function converts a number to required precision</td>
    </tr>
    <tr>
        <td><a href="math.md#to-string">To string</a></td><td>This function converts any number into its string representation. </td>
    </tr>
</table>

### Object Functions {#object-functions}

<table>
    <tr>
        <td><a href="objects.md#isNotNull">Is not null</a></td><td>This function is used to determine if an object reference exists</td>
    </tr>
    <tr>
        <td><a href="objects.md#isNull">Is null</a></td><td>This function is used to determine if an object reference does not exist</td>
    </tr>
</table>

### String Functions {#string-functions}

<table>
    <tr>
        <td><a href="string.md#camelCase">Camel Case</a></td><td>This function is used to capitalize the first letter of each word of a string</td>
    </tr>
    <tr>
        <td><a href="string.md#char-code-at">Char code at</a></td><td>This function returns ASCII value of a character, like the charCodeAt function in JavaScript</td>
    </tr>
    <tr>
        <td><a href="string.md#concat">Concat</a></td><td>This function is used to combine two strings into one</td>
    </tr>
    <tr>
        <td><a href="string.md#contains">Contains</a></td><td>This function is used to determine if a string contains a specified substring</td>
    </tr>
    <tr>
        <td><a href="string.md#doesNotContain">Does not contain</a></td><td>This function is used to determine if a string does not contain a specified substring</td>
    </tr>
    <tr>
        <td><a href="string.md#doesNotEndWith">Does not end with</a></td><td>This function is used to determine if a string does not end with a specified substring</td>
    </tr>
    <tr>
        <td><a href="string.md#doesNotStartWith">Does not start with</a></td><td>This function is used to determine if a string does not start with a specified substring</td>
    </tr>
    <tr>
        <td><a href="string.md#encode64">Encode 64</a></td><td>This function is used to encode or decode a string</td>
    </tr>
    <tr>
        <td><a href="string.md#endsWith">Ends with</a></td><td>This function is used to determine if a string ends with a specified substring</td>
    </tr>
        </tr>
    <tr>
        <td><a href="string.md#equals">Equals</a></td><td>This function is used to determine if a string does not start with a specified substring, with case sensitivity</td>
    </tr>
    <tr>
        <td><a href="string.md#equalsIgnoreCase">Equals Ignore Case</a></td><td>This function is used to determine if a string does not start with a specified substring, without case sensitivity</td>
    </tr>
    <tr>
        <td><a href="string.md#extractEmailDomain">Extract Email Domain</a></td><td>This function is used to extract the domain of an email address</td>
    </tr>
    <tr>
        <td><a href="string.md#format-currency">Format currency</a></td><td>This function converts any number into its corresponding language-sensitive currency representation depending on the locale passed as a string in the second argument</td>
    </tr>
    <tr>
        <td><a href="string.md#get-url-host">Get url host</a></td><td>This function is used to get url host.</td>
    </tr>
    <tr>
        <td><a href="string.md#get-url-path">Get url path</a></td><td>This function is used to get url path</td>
    </tr>
    <tr>
        <td><a href="string.md#get-url-protocol">Get url protocol</a></td><td>This function is used to get url protocol</td>
    </tr>
    <tr>
        <td><a href="string.md#index-of">Index Of</a></td><td>This function returns the position (in the first argument) of the first occurrence of the second parameter. Returns -1 if there is no match</td>
    </tr>
    <tr>
        <td><a href="string.md#isEmpty">IsEmpty</a></td><td>This function is used to check if a string or expression is empty.</td>
    </tr>
    <tr>
        <td><a href="string.md#is-not-empty">Is Not Empty</a></td><td>This function returns true if the string in the parameter is not empty.</td>
    </tr>
    <tr>
        <td><a href="string.md#last-index-of">Last Index Of</a></td><td>This function returns the position (in the first argument) of the last occurrence of the second parameter. Returns -1 if there is no match.</td>
    </tr>
    <tr>
        <td><a href="string.md#leftTrim">Left trim</a></td><td>This function removes white spaces from beginning of a string</td>
    </tr>
    <tr>
        <td><a href="string.md#length">Length</a></td><td>This function is used to get the number of characters in a string or an expression</td>
    </tr>
    <tr>
        <td><a href="string.md#like">Like</a></td><td>This function is used to determine if a string matches a specified pattern</td>
    </tr>
    <tr>
        <td><a href="string.md#lower">Lower Case</a></td><td>This function converts a string to lower case letters</td>
    </tr>
    <tr>
        <td><a href="string.md#mask">Mask</a></td><td>This function is used to replace a part of a string with "X" characters.</td>
    </tr>
    <tr>
        <td><a href="string.md#matches">Matches</a></td><td>This function is used to determine if a string matches a specific regular expression</td>
    </tr>
    <tr>
        <td><a href="string.md#md5">MD5</a></td><td>This function returns md5 hash of input string.</td>
    </tr>
    <tr>
        <td><a href="string.md#notEqualTo">Not equal to</a></td><td>This function is used to determine if a string is not equal to the specified string</td>
    </tr>
    <tr>
        <td><a href="string.md#not-equal-with-ignore-case">Not Equal With Ignore Case</a></td><td>This function compares two strings ignoring case.</td>
    </tr>
    <tr>
        <td><a href="string.md#regexGroup">Regular expression group</a></td><td>This function is used to extract specific information, based on the regular expression provided</td>
    </tr>
    <tr>
        <td><a href="string.md#replace">Replace</a></td><td>This function replaces a given substring in a string with another substring</td>
    </tr>
    <tr>
        <td><a href="string.md#replaceAll">Replace all</a></td><td>This function replaces all substrings of a text that matches the "target" with the specified literal "replacement" string</td>
    </tr>
    <tr>
        <td><a href="string.md#rightTrim">Right trim</a></td><td>This function removes white spaces from end of a string </td>
    </tr>
    <tr>
        <td><a href="string.md#split">Split</a></td><td>This function is used to split a string by a given character</td>
    </tr>
    <tr>
        <td><a href="string.md#startsWith">Starts with</a></td><td>This function is used to determine if a string starts with a specified substring</td>
    </tr>
    <tr>
        <td><a href="string.md#string-to-date">String to date</a></td><td>This function converts a string value into a date-time value</td>
    </tr>
    <tr>
        <td><a href="string.md#string-to-integer">String to integer</a></td><td>This function Converts a string value into an integer value.</td>
    </tr>
    <tr>
        <td><a href="string.md#string-to-number">String to number</a></td><td>This function is used to convert a string into number. It returns the same string as output for invalid input.</td>
    </tr>
    <tr>
        <td><a href="string.md#sub-string">Sub string</a></td><td>This function returns the sub-string of the string expression between the begin index and the end index.</td>
    </tr>
    <tr>
        <td><a href="string.md#titleCase">Title Case</a></td><td>This function is used to capitalize first letters of each word of a string</td>
    </tr>
    <tr>
        <td><a href="string.md#to-bool">To Bool</a></td><td>This function Converts an argument value into a boolean value, depending on its type.</td>
    </tr>
    <tr>
        <td><a href="string.md#to-date-time">To Date Time</a></td><td>This function is used to convert string to date. It returns the epoch date as output for invalid input.</td>
    </tr>
    <tr>
        <td><a href="string.md#to-date-time-only">To Date Time only</a></td><td>This function converts an argument value into a date time only value. It returns the epoch date as output for invalid input.</td>
    </tr>
    <tr>
        <td><a href="string.md#trim">Trim</a></td><td>This function removes white spaces from the beginning and from end of a string</td>
    </tr>
    <tr>
        <td><a href="string.md#upper">Upper case</a></td><td>This function converts a string to upper case letters</td>
    </tr>
    <tr>
        <td><a href="string.md#url-decode">Url decode</a></td><td>This function is used to decode a url encoded string.</td>
    </tr>
    <tr>
        <td><a href="string.md#url-encode">Url encode</a></td><td>This function is used to url encode a string.</td>
    </tr>
</table>


## Helpers{#helper-helper}

Helpers are detailed in [this page](helpers.md).


<table>
    <tr>
        <td><a href="helpers.md#default">Default fallback value</a></td><td>This function is used to render a variable with default</td>
    </tr>
    <tr>
        <td><a href="helpers.md#each">Each</a></td><td>This function is used to iterate over an array</td>
    </tr>
    <tr>
        <td><a href="helpers.md#if-function">If</a></td><td>This function is used to define a conditional block - if the expression evaluation returns true, the block is rendered</td>
    </tr>
    <tr>
        <td><a href="helpers.md#let">Let</a></td><td>This function allows an expression to be stored as a variable to be used later in a query</td>
    </tr>
   <tr>
        <td><a href="helpers.md#unless">Unless</a></td><td>This function is used to define a conditional block - if the expression evaluation returns false, the block is rendered</td>
    </tr>
    <tr>
        <td><a href="helpers.md#with">With</a></td><td>This function is used to change the evaluation token of template-part</td>
    </tr>
</table>

## Operators{#operators-helper}

### Arithmetic functions {#arithmetic-helper}

Arithmetic functions are used to perform basic calculations on values.

<table>
    <tr>
        <td><a href="arithmetic-functions.md#add">Addition</a></td><td>This operator is used to find the sum of two argument expressions</td>
    </tr>
    <tr>
        <td><a href="arithmetic-functions.md#divide">Divide</a></td><td>This operator is used to find the quotient of two argument expressions</td>
    </tr>
    <tr>
        <td><a href="arithmetic-functions.md#multiply">Multiplication</a></td><td>This operator is used to find the product of two argument expressions</td>
    </tr>
    <tr>
        <td><a href="arithmetic-functions.md#remainder">Remainder</a> </td><td>This operator is used to  find the remainder after dividing the two argument expressions</td>
    </tr>
    <tr>
        <td><a href="arithmetic-functions.md#substract">Subtraction</a> </td><td>This operator finds the difference between two expressions</td>
    </tr>
</table>


### Boolean functions {#boolean-functions}

Boolean functions are used to perform boolean logic on different elements.

<table>
    <tr>
        <td><a href="operators.md#and">And</a></td><td>This operator creates a logical conjunction</td>
    </tr>
    <tr>
        <td><a href="operators.md#or">Or</a></td><td>This operator creates a logical disjunction</td>
    </tr>
</table>


### Comparison functions {#comparison-functions}

Comparison functions are used to compare between different expressions and values, returning true or false accordingly.

<table>
    <tr>
        <td><a href="operators.md#equals">Equals</a></td><td>This operation checks if values are equal</td>
    </tr>
    <tr>
        <td><a href="operators.md#greaterthan">Greater than</a></td><td>This operator checks if first value is greater than the second value</td>
    </tr>
    <tr>
        <td><a href="operators.md#greaterthanorequal">Greater or equals to</a></td><td>This operator checks if first value is greater than or equal to the second value</td>
    </tr>
    <tr>
        <td><a href="operators.md#lessthanorequal">Less than or equals to</a> </td><td>This operator checks if first value is smaller than or equal to the second value</td>
    </tr>
    <tr>
        <td><a href="operators.md#notequal">Not equals to</a></td><td>This operator checks if given expression not equal to give value</td>
    </tr>
</table>

## How-to video{#video}

Learn how to transform personalization values using personalization helper functions and understand different use cases for helper functions.

>[!VIDEO](https://video.tv.adobe.com/v/334244?quality=12)
