---
title: Aggregation functions library
description: Aggregation functions library
feature: Personalization
topic: Personalization
role: Developer
level: Experienced
exl-id: a029f716-ea1e-4d79-82b7-59770f05161b
TQID: https://experienceleague.adobe.com/y1ivXVJe-Y5aIkMu--Tz22U0j-cuGcTUYrdkCkl1xyE
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
# Aggregation Functions {#aggregation}

Aggregation functions are used to group together multiple values to form a single summary value.

## Average{#average}

The `average` function returns the arithmetic mean of all the selected values within the array.

**Syntax**

```sql
{%= average(array) %}
```

**Example**

The following operation returns the average price of all the orders.

```sql
{%=average(orders.order.price)%}
```

## Count{#count}

The `count` function returns the number of elements within the given array.

**Syntax**

```sql
{%= count(array) %}
```

**Example**

The following operation returns the number of orders in the array.

```sql
{%= count(orders) %}
```

## Maximum{#max}

The `max` function returns the largest of all the selected values within the array.

**Syntax**

```sql
{%= max(array) %}
```

**Example**

The following operation returns the highest price of all the orders.

```sql
{%=max(orders.order.price)%}
```

## Minimum{#min}

The `min` function returns the smallest of all the selected values within the array.

**Syntax**

```sql
{%= min(array) %}
```

**Example**

The following operation returns the lowest price of all the orders.

```sql
{%=min(orders.order.price) %}
```

## Sum{#sum}

The `sum` function returns the sum of all the selected values within the array.

**Syntax**

```sql
{%= sum(array) %}
```

**Example**

The following operation returns the sum of all the orders' prices.

```sql
{%=sum(orders.order.price)%}
```
