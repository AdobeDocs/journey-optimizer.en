---
title: Maps functions library
description: Maps functions library
feature: Personalization
topic: Personalization
role: Developer
level: Experienced
exl-id: de6a8da2-55cf-4105-ba93-40c556732626
TQID: https://experienceleague.adobe.com/KeitEe0NQxxc-snCyWSGlov-OyUgiva6ddzrCTxEKSs
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
