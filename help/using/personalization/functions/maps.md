---
title: Maps functions library
description: Maps functions library
feature: Personalization
topic: Personalization
role: Developer
level: Experienced
exl-id: de6a8da2-55cf-4105-ba93-40c556732626
---
# Maps Functions{#maps}

Use Map functions in personalization to make interaction with maps easier. 

## Get{#get}

The `get` function is used to retrieve the value of a map for a given key.

**Syntax**

```sql
{%= get(map, string) %}
```

**Example**

The following operation gets the value of the identity map for the key `example@example.com`.

```sql
{%= get(identityMap,"example@example.com") %}
```

## Keys{#keys}

The `keys` function is used to retrieve all the keys for a given map.

**Syntax**

```sql
{%= keys(map) %}
```

**Example**

The following operation gets all the keys for the map `identityMap`.

```sql
{%= keys(identityMap) %}
```

## Values{#values}

The `values` function is used to retrieve all the values of a given map.

**Syntax**

```sql
{%= values(map) %}
```

**Example**

The following operation gets all the values for the map `identityMap`.

```sql
{%= values(identityMap) %}
```
