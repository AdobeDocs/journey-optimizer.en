---
product: journey optimizer
title: String functions
description: Learn about string functions
feature: Journeys
role: Developer
level: Experienced
keywords: string, functions, expression, journey, text, manipulation
version: Journey Orchestration
---
# String functions {#string-functions}

String functions enable you to manipulate and work with text values within your journey expressions. These functions are essential for text processing, validation, transformation, and analysis in your customer journeys.

Use string functions when you need to:

* Concatenate and combine multiple text values ([concat](#concat))
* Search for specific text patterns or substrings ([contain](#contain), [containIgnoreCase](#containIgnoreCase), [indexOf](#indexOf), [lastIndexOf](#lastIndexOf), [matchRegExp](#matchRegExp))
* Compare strings with case-sensitive or case-insensitive matching ([equalIgnoreCase](#equalIgnoreCase), [notEqualIgnoreCase](#notEqualIgnoreCase))
* Check string starts and ends ([startWith](#startWith), [startWithIgnoreCase](#startWithIgnoreCase), [endWith](#endWith), [endWithIgnoreCase](#endWithIgnoreCase))
* Extract portions of text using substring operations ([substr](#substr))
* Transform text to uppercase or lowercase ([upper](#upper), [lower](#lower), [trim](#trim))
* Check if strings are empty or contain specific values ([isEmpty](#isEmpty), [isNotEmpty](#isNotEmpty))
* Replace text patterns with new values ([replace](#replace), [replaceAll](#replaceAll))
* Split strings into arrays for further processing ([split](#split))
* Get string length ([length](#length)) or generate unique identifiers ([uuid](#uuid))

String functions provide comprehensive text manipulation capabilities, enabling sophisticated data processing and conditional logic based on text content in your journey expressions.

## concat {#concat}

Concatenates two string parameters or a list of strings.

+++Syntax

`concat(<parameters>)`

+++

+++Parameters

| Parameter | Type             |
|-----------|------------------|
| List      | listString       |
| string   | string |

+++

+++Signature and returned type

`concat(<string>,<string>)`

`concat(<listString>)`

Returns a string.

+++

+++Examples

`concat("Hello","World")`

Returns "HelloWorld".

`concat(["Hello"," ","World"])`

Returns "Hello World".

+++

## contain {#contain}

Checks if the second argument string is contained in the first argument string.

+++Syntax

`contain(<parameters>)`

+++

+++Parameters

* string

+++

+++Signature and returned type

`contain(<string>,<string>)`

Returns a boolean.

+++

+++Examples

`contain("rowing is great", "great")`

Returns true.

+++

## containIgnoreCase {#containIgnoreCase}

Checks if the second argument string is contained in the first argument string, without taking into account the case.

+++Syntax

`containIgnoreCase(<parameters>)`

+++

+++Parameters

| Parameter | Type             |
|-----------|------------------|
| string   | string |
| string searched   | string |

+++

+++Signature and returned type

`containIgnoreCase(<string>,<string>)`

Returns a boolean.

+++

+++Examples

`containIgnoreCase("rowing is great", "GREAT")`

Returns true.

+++

## endWith {#endWith}

Returns true if the second parameter is a suffix of the first one.

+++Syntax

`endWith(<parameters>)`

+++

+++Parameters

| Parameter | Type             |
|-----------|------------------|
| string   | string |
| suffix   | string |

+++

+++Signature and returned type

`endWith(<string>,<string>)`

Returns a boolean.

+++

+++Examples

`endWith("Hello World", "World")`

Returns true.

`endWith("Hello World", "Hello")`

Returns false.

+++

## endWithIgnoreCase {#endWithIgnoreCase}

Checks if the first argument string ends with a specific string (second argument string), not taking into account the case.

+++Syntax

`endWithIgnoreCase(<parameters>)`

+++

+++Parameters

| Parameter | Type             |
|-----------|------------------|
| string   | string |
| suffix  | string |

+++

+++Signature and returned type

`endWithIgnoreCase(<string>,<string>)`

Returns a boolean.

+++

+++Examples

`endWithIgnoreCase("rowing is great", "AT")`

Returns true.

+++

## equalIgnoreCase {#equalIgnoreCase}

Compares the first argument string with the second argument string, ignoring case considerations.

+++Syntax

`equalIgnoreCase(<parameters>)`

+++

+++Parameters

* string

+++

+++Signature and returned type

`equalIgnoreCase(<string>,<string>)`

Returns a boolean.

+++

+++Examples

`equalIgnoreCase("rowing is great", "rowing is GREAT")`

Returns true.

+++

## indexOf {#indexOf}

Returns the position (in the first argument) of the first occurrence of the second parameter. Returns -1 if there is no match.

+++Syntax

`indexOf(<parameters>)`

+++

+++Parameters

| Parameter | Type             |
|-----------|------------------|
| string | String   |
| specified value | String |

+++

+++Signature and returned type

`indexOf(<string>,<string>)`

Returns an integer.

+++

+++Examples

`indexOf("Hello", "l")`

Returns 2.

Explanation:

In "Hello", the first occurrence of "l" is at position 2.

+++

## isEmpty {#isEmpty}

Returns true if the string in the parameter has no character.

+++Syntax

`isEmpty(<parameters>)`

+++

+++Parameters

* string

+++

+++Signature and returned type

`isEmpty(<string>)`

Returns a boolean.

+++

+++Examples

`isEmpty("")`

Returns true.

`isEmpty("Hello World")`

Returns false.

+++

## isNotEmpty {#isNotEmpty}

Returns true if the string in the parameter is not empty.

+++Syntax

`isNotEmpty(<parameters>)`

+++

+++Parameters

* string

+++

+++Signature and returned type

`isNotEmpty(<string>)`

Returns a boolean.

+++

+++Examples

`isNotEmpty("")`

Returns false.

`isNotEmpty("hello")`

Returns true.

+++

## lastIndexOf {#lastIndexOf}

Returns the position (in the first argument) of the last occurrence of the second parameter. Returns -1 if there is no match.

+++Syntax

`lastIndexOf(<parameters>)`

+++

+++Parameter

| Parameter | Type             |
|-----------|------------------|
|  string | String   |
|  specified value | String |

+++

+++Signature and returned type

`lastIndexOf(<string>,<string>)`

Returns an integer.

+++

+++Examples

`lastIndexOf("Hello", "l")`

Returns 3.

Explanation:

In "Hello", the last occurrence of "l" is at position 3.

+++

## length {#length}

Returns the number of characters of the string expression in the parameter.

+++Syntax

`length(<parameters>)`

+++

+++Parameter

* string

+++

+++Signature and returned type

`length(<string>)`

Returns an integer.

+++

+++Examples

`length("Hello World")`

Returns 11.

+++

## lower {#lower}

Returns a lowercase version of the parameter.

+++Syntax

`lower(<parameter>)`

+++

+++Parameter

* string

+++

+++Signature and returned type

`lower(<string>)`

Returns a string.

+++

+++Examples

`lower("A")`

Returns "a".

+++

## matchRegExp {#matchRegExp}

Returns true if the string in the first parameter matches the regular expression in the second parameter. For more information, see [this page](https://docs.oracle.com/javase/7/docs/api/java/util/regex/Pattern.html).

+++Syntax

`matchRegExp(<parameters>)`

+++

+++Parameters

|Parameter|Type|
|--- |--- |
|string|string|
|regexp|string|

+++

+++Signature and returned type

`matchRegExp(<string>,<string>)`

Returns a boolean.

+++

+++Examples

`matchRegExp("12345", "\\d+")`

Returns true.

+++

## notEqualIgnoreCase {#notEqualIgnoreCase}

Check if the first argument string with the second argument string are different, ignoring case considerations.

+++Syntax

`notEqualIgnoreCase(<parameters>)`

+++

+++Parameters

* string

+++

+++Signature and returned type

`notEqualIgnoreCase(<string>,<string>)`

Returns a boolean.

+++

+++Examples

`notEqualIgnoreCase(@event{iOSPushPermissionAllowed.device.model}, "iPad")`

+++

## replace {#replace}

Replaces the first occurrence matching the target string by the replacement string in the base string.

The replacement proceeds from the beginning of the string to the end, for example, replacing "aa" with "b" in the string "aaa" will result in "ba" rather than "ab".

+++Syntax

`replace(<parameters>)`

+++

+++Parameters

| Parameter | Type         |
|-----------|--------------|
| base      | string       |
| target    | string (RegExp)       |
| replacement  | string    |

+++

+++Signature and returned type

`replace(<base>,<target>,<replacement>)`

Return a string.

+++

+++Examples

`replace("Hello World", "l", "x")`

Returns "Hexlo World".

**Example with RegExp:**

Because the target parameter is a RegExp, depending on the string you want to replace, you may need to escape some characters. Here is an example:

* string to evaluate: `|OFFER_A|OFFER_B`
* provided by a profile attribute `#{ExperiencePlatform.myFieldGroup.profile.myOffers}`
* String to be replaced: `|OFFER_A`
* String replaced by: `''`
* You need to add `\\` before the `|` character.

The expression is:

`replace(#{ExperiencePlatform.myFieldGroup.profile.myOffers}, '\\|OFFER_A', '')`

The returned string is: `|OFFER_B`

You can also build the string to be replaced from a given attribute:

`replace(#{ExperiencePlatform.myFieldGroup.profile.myOffers}, '\\|' + #{ExperiencePlatform.myFieldGroup.profile.myOfferCode}, '')`

+++

## replaceAll {#replaceAll}

Replaces all occurrences matching the target string by the replacement string in the base string.

The replacement proceeds from the beginning of the string to the end, for example, replacing "aa" with "b" in the string "aaa" will result in "ba" rather than "ab".

+++Syntax

`replaceAll(<parameters>)`

+++

+++Parameters

| Parameter | Type         |
|-----------|--------------|
| base      | string       |
| target    | string (RegExp)       |
| replacement    | string       |

+++

+++Signature and returned type

`replaceAll(<baseString>,<sourceString>,<replacementString>)`

Returns a string.

+++

+++Examples

`replaceAll("Hello World", "l", "x")`

Returns "Hexxo Worxd".

Because the target parameter is a RegExp, depending on the string you want to replace, you may need to escape some characters. Refer to the example in the [replace](#replace) function.

+++

## split {#split}

Splits the first argument string with a separator string (second argument string, which can be a regular expression) to produce a list of strings (tokens).

+++Syntax

`split(<parameters>)`

+++

+++Parameters

|Parameter|Type|
|-----------|------------------|
|input string|string|
|separator string|string|

+++

+++Signatures and returned type

`split(<input string>, <separator string>)`

Returns a listString.

+++

+++Examples

`split("A_B_C", "_")`

Returns `["A","B","C"]`

Example with an event field 'event.appVersion' with value: "20.45.2.3434"

`split(@event{event.appVersion}, "\\.")`

Returns `["20", "45", "2", "3434"]`

+++

## startWith {#startWith}

Returns true if the second parameter is a prefix of the first one.

+++Syntax

`startWith(<parameters>)`

+++

+++Parameters

| Parameter   | Type  |
|-------------|--------|
| string      | string |
| prefix      | string |

+++

+++Signature and returned type

`startWith(<string>,<string>)`

Return a boolean.

+++

+++Examples

`startWith("Hello World", "Hello")`

Returns true.

`startWith("Hello World", "World")`

Returns false.

+++

## startWithIgnoreCase {#startWithIgnoreCase}

Returns true if the second parameter is a prefix of the first one without considering case.

+++Syntax

`startWithIgnoreCase(<parameters>)`

+++

+++Parameters

| Parameter   | Type  |
|-------------|--------|
| string      | string |
| prefix      | string |

+++

+++Signature and returned type

`startWithIgnoreCase(<string>,<string>)`

Return a boolean.

+++

+++Examples

`startWithIgnoreCase("rowing is great", "RO")`

Returns true.

+++

## substr {#substr}

Returns the sub-string of the string expression between the begin index and the end index. If the end index is not defined, then it is between the begin index and the end.

+++Syntax

`substr(<parameters>)`

+++

+++Parameters

| Parameter  | type |
|-------------|----------|
| string | string |
| beginIndex | integer |
| endIndex | integer |

+++

+++Signature and returned type

`substr(<string>,<beginIndex>)`

`substr(<string>,<beginIndex>,<endIndex>)`

Return a string.

+++

+++Examples

`substr("Hello World",6)`

Returns "World".

`substr("Hello World", 0, 5)`

Returns "Hello".

+++

## trim {#trim}

Removes start and end spaces.

+++Syntax

`trim(<parameters>)`

+++

+++Parameter

| Parameter | Type             |
|-----------|------------------|
| string   | string |

+++

+++Signature and returned type

`trim(<string>)`

Return a string.

+++

+++Examples

`trim(" Hello ")`

Returns "Hello".

+++

## upper {#upper}

Returns an uppercase version of the parameter.

+++Syntax

`upper(<parameters>)`

+++

+++Signature and returned type

`upper(<string>)`

Return a string.

+++

+++Examples

`upper("b")`

Returns "B".

+++

## uuid {#uuid}

Generates a random UUID (Universal Unique IDentifier).

+++Syntax

`uuid()`

+++

+++Parameters 

This function does not require parameters.

+++

+++Signature and returned type

`uuid()`

Returns a string.

+++

+++Examples

`uuid()`

Returns "79e70b7f-8a85-400b-97a1-9f9826121553".

+++

