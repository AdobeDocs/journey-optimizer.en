---
title: String functions library
description: String functions library
feature: Personalization
topic: Personalization
role: Data Engineer
level: Experienced
exl-id: 8674ef9e-261b-49d9-800e-367f9f7ef979
---
# String Functions {#string}

Learn how to use String functions in the personalization editor.

## Camel Case {#camelCase}

The `camelCase` function capitalizes the first letter of each word of a string.

**Syntax**

```sql
{%= camelCase(string)%}
```

**Example**

The following function will capitalize the first letter of word in the profile's street address.

```sql
{%= camelCase(profile.homeAddress.street) %}
```

## Char code at {#char-code-at}

The `charCodeAt` function returns ASCII value of a character, like the charCodeAt function in JavaScript. It takes a string and an integer (defining the position of character) as input arguments and returns its corresponding ASCII value.

**Syntax**

```sql
{%= charCodeAt(string,int) %}: int
```

**Example**

The following function returns the ASCII value of o i.e 111.

```sql
{%= charCodeAt("some", 1)%}
```

## Concat {#concate}

The `concat` function combines two strings into one.

**Syntax**

```sql
{%= concat(string,string) %}
```

**Example**

The following function will combine profile city and country in a single string.

```sql
{%= concat(profile.homeAddress.city,profile.homeAddress.country) %}
```

## Contains {#contains}

The `contains` function is used to determine if a string contains a specified substring.

**Syntax**

```sql
{%= contains(STRING_1, STRING_2, CASE_SENSITIVE) %}
```

| Argument | Description |
| --------- | ----------- |
| `STRING_1` | The string to perform the check on. |
| `STRING_2` | The string to search for within the first string. |
| `CASE_SENSITIVE` | An optional parameter to determine if the check is case sensitive. Possible values: true (default) / false. |

**Examples**

* The following function will check if the profile first name contains the letter A (in upper or lower case). If this is the case, it will return 'true', else it will return 'false'.

    ```sql
    {%= contains(profile.person.name.firstName, "A", false) %}
    ```

* The following query determines, with case sensitivity, if the person's email address contains the string "2010@gm".

    ```sql
    {%= contains(profile.person.emailAddress,"2010@gm") %}
    ```

## Does not contain{#doesNotContain}

The `doesNotContain` function is used to determine if a string does not contain a specified substring.

**Syntax**

```sql
{%= doesNotContain(STRING_1, STRING_2, CASE_SENSITIVE)%}
```

| Argument | Description |
| --------- | ----------- |
| `STRING_1` | The string to perform the check on. |
| `STRING_2` | The string to search for within the first string. |
| `CASE_SENSITIVE` | An optional parameter to determine if the check is case sensitive. Possible values: true (default) / false. |

**Example**

The following query determines, with case sensitivity, if the person's email address does not contain the string "2010@gm".

```sql
{%= doesNotContain(profile.person.emailAddress,"2010@gm")%}
```


## Does not end with{#doesNotEndWith}

The `doesNotEndWith` function is used to determine if a string does not end with a specified substring.

**Syntax**

```sql
{%= doesNotEndWith(STRING_1, STRING_2, CASE_SENSITIVE)%}
```

| Argument | Description |
| --------- | ----------- |
| `{STRING_1}` | The string to perform the check on. |
| `{STRING_2}` | The string to search for within the first string. |
| `{CASE_SENSITIVE}` | An optional parameter to determine if the check is case sensitive. Possible values: true (default) / false. |

**Example**

The following query determines, with case sensitivity, if the person's email address does not end with ".com".

```sql
doesNotEndWith(person.emailAddress,".com")
```

## Does not start with{#doesNotStartWith}

The `doesNotStartWith` function is used to determine if a string does not start with a specified substring.

**Syntax**

```sql
{%= doesNotStartWith(STRING_1, STRING_2, CASE_SENSITIVE)%}
```

| Argument | Description |
| --------- | ----------- |
| `{STRING_1}` | The string to perform the check on. |
| `{STRING_2}` | The string to search for within the first string. |
| `{CASE_SENSITIVE}` | An optional parameter to determine if the check is case sensitive. Possible values: true (default) / false. |

**Example**

The following query determines, with case sensitivity, if the person's name does not start with "Joe".

```sql
{%= doesNotStartWith(person.name,"Joe")%}
```

## Encode 64{#encode64}

The `encode64` function is used to encode a string to preserve Personal Information (PI) if to be included for example in a URL.

**Syntax**

```sql
{%= encode64(string) %}
```

## Ends with{#endsWith}

The `endsWith` function is used to determine if a string ends with a specified substring.

**Syntax**

```sql
{%= endsWith(STRING_1, STRING_2, CASE_SENSITIVE) %}
```

| Argument | Description |
| --------- | ----------- |
| `{STRING_1}` | The string to perform the check on. |
| `{STRING_2}` | The string to search for within the first string. |
| `{CASE_SENSITIVE}` | An optional parameter to determine if the check is case sensitive. Possible values: true (default) / false.  |

**Example**

The following query determines, with case sensitivity, if the person's email address ends with ".com".

```sql
{%= endsWith(person.emailAddress,".com") %}
```


## Equals{#equals}

The `equals` function is used to determine if a string is equal to the specified string, with case sensitivity.

**Syntax**

```sql
{%= equals(STRING_1, STRING_2) %}
```

| Argument | Description |
| --------- | ----------- |
| `{STRING_1}` | The string to perform the check on. |
| `{STRING_2}` | The string to compare with the first string. |

**Example**

The following query determines, with case sensitivity, if the person's name is "John".

```sql
{%=equals(profile.person.name,"John") %}

```

## Equals Ignore Case{#equalsIgnoreCase}

The `equalsIgnoreCase` function is used to determine if a string is equal to the specified string, without case sensitivity.

**Syntax**

```sql
{%= equalsIgnoreCase(STRING_1, STRING_2) %}
```

| Argument | Description |
| --------- | ----------- |
| `{STRING_1}` | The string to perform the check on. |
| `{STRING_2}` | The string to compare with the first string. |

**Example**

The following query determines, without case sensitivity, if the person's name is "John".

```sql
{%= equalsIgnoreCase(profile.person.name,"John") %}

```

## Extract Email Domain {#extractEmailDomain}

The `extractEmailDomain` function is used to extract the domain of an email address.

**Syntax**

```sql
{%= extractEmailDomain(string) %}
```

**Example**

The following query extracts the email domain of the personal email address.

```sql
{%= extractEmailDomain(profile.personalEmail.address) %}
```

## Format currency {#format-currency}

The `formatCurrency` function is used to convert any number into its corresponding language-sensitive currency representation depending on the locale passed as a string in the second argument.

**Syntax**

```sql
{%= formatCurrency(number/double,string) %}: string
```

**Example**

This query returns £56.00

```sql
{%= formatCurrency(56L,"en_GB") %}
```

## Get url host {#get-url-host}

The `getUrlHost` function is used to retrieve the hostname of a URL.

**Syntax**

```sql
{%= getUrlHost(string) %}: string
```

**Example**

```sql
{%= getUrlHost("https://www.myurl.com/contact") %}
```

Returns "www.myurl.com"

## Get url path {#get-url-path}

The `getUrlPath` function is used to retrieve the path after the domain name of a URL.

**Syntax**

```sql
{%= getUrlPath(string) %}: string

```

**Example**

```sql
{%= getUrlPath("https://www.myurl.com/contact.html") %}
```

Returns "/contact.html"

## Get url protocol {#get-url-protocol}

The `getUrlProtocol` function is used to retrieve the protocol of a URL.

**Syntax**

```sql
{%= getUrlProtocol(string) %}: string
```

**Example**

```sql
{%= getUrlProtocol("https://www.myurl.com/contact.html") %}
```

Returns "http"

## Index Of {#index-of}

The `indexOf` function is used to return the position (in the first argument) of the first occurrence of the second parameter. Returns -1 if there is no match.

**Syntax**

```sql
{%= indexOf(STRING_1, STRING_2) %}: integer
```

| Argument | Description |
| --------- | ----------- |
| `{STRING_1}` | The string to perform the check on. |
| `{STRING_2}` | The string to search in the first parameter|

**Example**

```sql
{%= indexOf("hello world","world" ) %}
```

Returns 6.

## Is empty {#isEmpty}

The `isEmpty` function is used to determine if a string is empty.

**Syntax**

```sql
{%= isEmpty(string) %}
```

**Example**

The following function returns 'true' if the profile's mobile phone number is empty. Else, it will return 'false'.

```sql
{%= isEmpty(profile.mobilePhone.number) %}
```

## Is Not Empty {#is-not-empty}

The `isNotEmpty` function is used to determine if a string is not empty.

**Syntax**

```sql
{= isNotEmpty(string) %}: boolean
```

**Example**

The following function returns 'true' if the profile's mobile phone number is not empty. Else, it will return 'false'.

```sql
{%= isNotEmpty(profile.mobilePhone.number) %}
```

## Last Index Of {#last-index-of}

The `lastIndexOf` function is used to return the position (in the first argument) of the last occurrence of the second parameter. Returns -1 if there is no match.

**Syntax**

```sql
{= lastIndexOf(STRING_1, STRING_2) %}: integer
```

| Argument | Description |
| --------- | ----------- |
| `{STRING_1}` | The string to perform the check on. |
| `{STRING_2}` | The string to search in the first parameter|

**Example**

```sql
{%= lastIndexOf("hello world","o" ) %}
```

Returns 7.

## Left trim {#leftTrim}

The `leftTrim` function is used to remove white spaces from beginning of a string.

**Syntax**

```sql
{%= leftTrim(string) %}
```

## Length {#length}

The `length` function is used to get the number of characters in a string or an expression.

**Syntax**

```sql
{%= length(string) %}
```

**Example**

The following function returns the length of the profile's city name.

```sql
{%= length(profile.homeAddress.city) %}
```

## Like{#like}

The `like` function is used to determine if a string matches a specified pattern.

**Syntax**

```sql
{%= like(STRING_1, STRING_2) %}
```

| Argument | Description |
| --------- | ----------- |
| `{STRING_1}` | The string to perform the check on. |
| `{STRING_2}` | The expression to match against the first string. There are two supported special characters for creating an expression: `%` and `_`. <ul><li>`%` is used to represent zero or more characters.</li><li>`_` is used to represent exactly one character.</li></ul> |

**Example**

The following query retrieves all the cities where profiles live containing the pattern "es".

```sql
{%= like(profile.homeAddress.city, "%es%")%}
```

## Lower Case{#lower}

The `lowerCase` function converts a string to lower case letters.

**Syntax**

```sql
{%= lowerCase(string) %}
```

**Example**

This function converts the profile first name to lower case letters.

```sql
{%= lowerCase(profile.person.name.firstName) %}
```

## Matches{#matches}

The `matches` function is used to determine if a string matches a specific regular expression. Please refer to [this document](https://docs.oracle.com/javase/8/docs/api/java/util/regex/Pattern.html) for more information on matching patterns in regular expressions.

**Syntax**

```sql
{%= matches(STRING_1, STRING_2) %}
```

**Example**

The following query determines, without case sensitivity, if the person's name starts with "John".

```sql
{%= matches(person.name.,"(?i)^John") %}
```

## Mask {#mask}

The `Mask` function is used to replace a part of a string with "X" characters.

**Syntax**

```sql
{%= mask(string,integer,integer) %}
```

**Example**

The following query replaces the "123456789" string with "X" characters, excepted for the first and the last 2 characters.

```sql
{%= mask("123456789",1,2) %}
```

The query returns `1XXXXXX89`.

## MD5 {#md5}

The `md5` function is used to calculate and return the md5 hash of a string.

**Syntax**

```sql
{%= md5(string) %}: string
```

**Example**

```sql
{%= md5("hello world") %}
```

Returns "5eb63bbbe01eeed093cb22bb8f5acdc3"

## Not equal to{#notEqualTo}

The `notEqualTo` function is used to determine if a string is not equal to the specified string.

**Syntax**

```sql
{%= notEqualTo(STRING_1, STRING_2) %}
```

| Argument | Description |
| --------- | ----------- |
| `{STRING_1}` | The string to perform the check on. |
| `{STRING_2}` | The string to compare with the first string. |

**Example**

The following query determines, with case sensitivity, if the person's name is not "John".

```sql
{%= notEqualTo(profile.person.name,"John") %}
```

## Not Equal With Ignore Case {#not-equal-with-ignore-case}

The `notEqualWithIgnoreCase` function is used to compare two strings ignoring case.

**Syntax**

```sql
{= notEqualWithIgnoreCase(STRING_1,STRING_2) %}: boolean
```

| Argument | Description |
| --------- | ----------- |
| `{STRING_1}` | The string to perform the check on. |
| `{STRING_2}` | The string to compare with the first string. |

**Example**

The following query determines if the person's name is not "john", with no case sensitivity.

```sql
{%= notEqualTo(profile.person.name,"john") %}
```

## Regular expression group{#regexGroup}

The `Group` function is used to extract specific information, based on the regular expression provided.

**Syntax**

```sql
{%= regexGroup(STRING, EXPRESSION, GROUP) %}
```

| Argument | Description |
| --------- | ----------- |
| `{STRING}` | The string to perform the check on. |
| `{EXPRESSION}` | The regular expression to match against the first string. |
| `{GROUP}` | Expression group to match against. |

**Example**

The following query is used to extract the domain name from an email address.

```sql
{%= regexGroup(emailAddress,"@(\\w+)", 1) %}
```

## Replace {#replace}

The `replace` function is used to replace a given substring in a string with another substring.

**Syntax**

```sql
{%= replace(STRING_1,STRING_2,STRING_3) %}:string
```

| Argument | Description |
| --------- | ----------- |
| `{STRING_1}` | The string where the substring must be replaced. |
| `{STRING_2}` | The substring to replace. |
| `{STRING_3}` | The replacement substring. |

**Example**

```sql
{%= replace("Hello John, here is your monthly newsletter!","John","Mark") %}
```

Returns "Hello Mark, here is your monthly newsletter!"

## Replace All{#replaceAll}

The `replaceAll` function is used to replace all substrings of a text that matches the "regex" expression with the specified literal "replacement" string. Regex has special handling of "\" and "+" and all regex expressions follow PQL escaping strategy. The replacement proceeds from the beginning of the string to the end, for example, replacing "aa" with "b" in the string "aaa" will result in "ba" rather than "ab".

**Syntax**

```sql
{%= replaceAll(string,string,string) %}
```

>[!NOTE]
>
> When the expression taken as second argument is a special regex character, use double back-slash (`//`).  Special regex characters are: [., +, *, ?, ^, $, (, ), [, ], {, }, |, \.]
> 
> Learn more in [Oracle documentation](https://docs.oracle.com/javase/7/docs/api/java/util/regex/Pattern.html){_blank}.
>

## Right trim {#rightTrim}

The `rightTrim` function is used removes white spaces from end of a string.

**Syntax**

```sql
{%= rightTrim(string) %}
```

## Split {#split}

The `split` function is used to split a string by a given character.

**Syntax**

```sql
{%= split(string,string) %}
```

## Starts with{#startsWith}

The `startsWith` function is used to determine if a string starts with a specified substring.

**Syntax**

```sql
{%= startsWith(STRING_1, STRING_2, CASE_SENSITIVE) %}

```

| Argument | Description |
| --------- | ----------- |
| `{STRING_1}` | The string to perform the check on. |
| `{STRING_2}` | The string to search for within the first string. |
| `{CASE_SENSITIVE}` | An optional parameter to determine if the check is case sensitive. By default, this is set to true. |

**Example**

The following query determines, with case sensitivity, if the person's name starts with "Joe".

```sql
{%= startsWith(person.name,"Joe") %}
```

## String to date {#string-to-date}

The `stringToDate` function converts a string value into a date-time value. It takes two arguments: string representation of a date-time and string representation of the formatter.

**Syntax**

```sql
{= stringToDate("date-time value","formatter" %}
```

**Example**

```sql
{= stringToDate("2023-01-10 23:13:26", "yyyy-MM-dd HH:mm:ss") %}
```

## String to integer {#string-to-integer}

The `string_to_integer` function is used to convert a string value into an integer value.

**Syntax**

```sql
{= string_to_integer(string) %}: int
```

## String to number {#string-to-number}

The `stringToNumber` function is used to convert a string into number. It returns the same string as output for invalid input.

**Syntax**

```sql
{%= stringToNumber(string) %}: double
```

## Sub string {#sub-string}

The `Count string` function is used to return the sub-string of the string expression between the begin index and the end index.
**Syntax**

```sql
{= substr(string, integer, integer) %}: string
```

## Title Case{#titleCase}

The **titleCase** function is used to capitalize first letters of each words of a string.

**Syntax**

```sql
{%= titleCase(string) %}
```

**Example**

If the person lives in Washington high street, this function will return Washington High Street.

```sql
{%= titleCase(profile.person.location.Street) %}
```

## To Bool {#to-bool}

The `toBool` function is used to convert an argument value into a boolean value, depending on its type.

**Syntax**

```sql
{= toBool(string) %}: boolean
```

## To Date Time {#to-date-time}

The `toDateTime` function is used to convert string to date. It returns the epoch date as output for invalid input.

**Syntax**

```sql
{%= toDateTime(string, string) %}: date-time
```

## To Date Time Only {#to-date-time-only}

The `toDateTimeOnly` function is used to convert an argument value into a date time only value. It returns the epoch date as output for invalid input. This function accepts string, date, long and int field types.

**Syntax**

```sql
{%= toDateTimeOnly(string/date/long/int) %}: date-time
```

## Trim {#trim}

The **trim** function removes all white spaces from the beginning and at the end of a string.

**Syntax**

```sql
{%= trim(string) %}
```

## Upper Case{#upper}

The **upperCase** function converts a string to upper case letters.

**Syntax**

```sql
{%= upperCase(string) %}
```

**Example**

This function converts the profile last name to upper case letters.

```sql
{%= upperCase(profile.person.name.lastName) %}
```

## Url decode {#url-decode}

The `urlDecode` function is used to decode a url encoded string.

**Syntax**

```sql
{%= urlDecode(string) %}: string
```

## Url encode {#url-encode}

The `Count only null` function is used to url encode a string.

**Syntax**

```sql
{%= urlEncode(string) %}: string
```
