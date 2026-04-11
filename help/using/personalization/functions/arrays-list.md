---
title: Arrays functions library
description: Arrays functions library
feature: Personalization
topic: Personalization
role: Developer
level: Experienced
exl-id: dfe611fb-9c50-473c-9eb7-b983e1e6f01e
---
# Arrays and list functions {#arrays}

Use these functions to make interaction with arrays, lists, and strings easier.

## Count only null {#count-only-null}

The `countOnlyNull` function is used to count the number of null values in a list.

**Syntax**

```sql
{%= countOnlyNull(array) %}
```

**Example**

```sql
{%= countOnlyNull([4,0,1,6,0,0]) %}
```

Returns 3.

## Count With Null {#count-with-null}

The `countWithNull` function is used to count all the elements of a list including null values.

**Syntax**

```sql
{%= countWithNull(array) %}
```

**Example**

```sql
{%= countOnlyNull([4,0,1,6,0,0]) %}
```

Returns 6.

## Distinct{#distinct}

The `distinct` function is used to get values from an array or list with duplicate values removed.

**Syntax**

```sql
{%= distinct(array) %}
```

**Example**

The following operation specifies people who have placed orders in more than one store.

```sql
{%= distinct(person.orders.storeId).count() > 1 %}
```

## Distinct Count With Null {#distinct-count-with-null}

The `distinctCountWithNull` function is used to count the number of different values in a list including the null values.

**Syntax**

```sql
{%= distinctCountWithNull(array) %}
```

**Example**

```sql
{%= distinctCountWithNull([10,2,10,null]) %}
```

Returns 3.

## First item{#head}

The `head` function is used to return the first item in an array or list.

**Syntax**

```sql
{%= head(array) %}
```

**Example**

The following operation returns the first of the top five orders with the highest price. More information about the `topN` function can be found in the [first `n` in array](#first-n) section.

```sql
{%= head(topN(orders,price, 5)) %}
```

## Sort and get first N in array {#first-n}

The `topN` function sorts an array in descending order based on the given numerical expression and returns the first `N` items. If the array size is less than `N`, it returns the entire sorted array.

This function 
**Syntax**

```sql
{%= topN(array, value, amount) %}
```

| Argument | Description |
| --------- | ----------- |
| `{ARRAY}` | The array or list that is to be sorted. |
| `{VALUE}` | The property in which to sort the array or list. |
| `{AMOUNT}` | The number of items to be returned. |

**Example**

The following operation returns the first five orders with the lowest price.

```sql
{%= topN(orders,price, 5) %}
```

## In{#in}

The `in` function is used to determine if an item is a member of an array or list.

**Syntax**

```sql
{%= in(value, array) %}
```

**Example**

The following operation defines people with birthdays in March, June, or September.

```sql
{%= in (person.birthMonth, [3, 6, 9]) %}
```

## Includes{#includes}

The `includes` function is used to determine if an array or list contains a given item.

**Syntax**

```sql
{%= includes(array,item) %}
```

**Example**

The following operation defines people whose favorite color includes red.

```sql
{%= includes(person.favoriteColors,"red") %}
```

## Intersects{#intersects}

The `intersects` function is used to determine if two arrays or lists have at least one common member.

**Syntax**

```sql
{%= intersects(array1, array2) %}
```

**Example**

The following operation defines people whose favorite colors include at least one of red, blue, or green.

```sql
{%= intersects(person.favoriteColors,["red", "blue", "green"]) %}
```


<!--
## Intersection{#intersection}

The `intersection` function is used to determine the common members of two arrays or lists.

**Syntax**

```sql
intersection({ARRAY},{ARRAY})
```

**Example**

The following operation defines if person 1 and person 2 both have favorite colors of red, blue, and green.

```sql
intersection(person1.favoriteColors,person2.favoriteColors) = ["red", "blue", "green"]
```
-->

## Sort and get last N in array {#last-n}

The `bottomN` function sorts an array in ascending order based on the given numerical expression and returns the first `N` items. If the array size is less than `N`, it returns the entire sorted array.

**Syntax**

```sql
{%= bottomN(array, value, amount) %}
```

| Argument | Description |
| --------- | ----------- |
| `{ARRAY}` | The array or list that is to be sorted. |
| `{VALUE}` | The property in which to sort the array or list. |
| `{AMOUNT}` | The number of items to be returned. |

**Example**

The following operation returns the last five orders with the highest price.

```sql
{%= bottomN(orders,price, 5) %}
```

## Not in{#notin}

The `notIn` function is used to determine if an item is not a member of an array or list.

>[!NOTE]
>
>The `notIn` function *also* ensures that neither value is equal to null. Therefore, the results are not an exact negation of the `in` function.

**Syntax**

```sql
{%= notIn(value, array) %}
```

**Example**

The following operation defines people with birthdays that are not in March, June, or September.

```sql
{%= notIn(person.birthMonth ,[3, 6, 9]) %}
```


## Subset of{#subset}

The `subsetOf` function is used to determine if a specific array (array A) is a subset of another array (array B). In other words, that all elements in array A are elements of array B.

**Syntax**

```sql
{%= subsetOf(array1, array2) %}
```

**Example**

The following operation defines people who have visited all of their favorite cities.

```sql
{%= subsetOf(person.favoriteCities,person.visitedCities) %}
```

## Superset of{#superset}

The `supersetOf` function is used to determine if a specific array (array A) is a superset of another array (array B). In other words, that array A contains all elements in array B.

**Syntax**

```sql
{%= supersetOf(array1, array2) %}
```

**Example**

The following operation defines people who have eaten sushi and pizza at least once.

```sql
{%= supersetOf(person.eatenFoods,["sushi", "pizza"]) %}
```

## Iterate over an array {#each-loop}

Use the Handlebars `{{#each}}` block helper to loop over an array and render content for each item in **personalized content** (email, SMS, push).

>[!NOTE]
>
>`{{#each}}` is available in the **personalization editor** only (email body, SMS, push content). It is **not** supported in the journey condition activity. To filter or match items from an array inside a journey condition, use [collection management functions](../../building-journeys/expression/collection-management-functions.md) instead.

**Syntax**

```handlebars
{{#each arrayAttribute}}
  {{this}}
{{/each}}
```

+++Example — List all items in an array

```handlebars
{{#each profile.purchases.items}}
  - {{this.name}}: {{this.price}}€
{{/each}}
```

Output (example):

```
- Running shoes: 89€
- Water bottle: 15€
- Gym bag: 45€
```

+++

+++Example — Access the loop index

Use `@index` to access the current loop position (0-based):

```handlebars
{{#each profile.preferences.languages}}
  {{@index}}: {{this}}
{{/each}}
```

Output (example):

```
0: English
1: French
2: Spanish
```

+++

+++Example — Conditional rendering inside a loop

Use the PQL `{% if %}` block inside `{{#each}}` to render content only when a condition is met:

```handlebars
{{#each profile.orders}}
  {% if this.status = "pending" %}
  Your order {{this.id}} is still pending.
  {% endif %}
{{/each}}
```

This is the recommended pattern to simulate a "break on condition" — only the items matching the condition produce output.

+++
