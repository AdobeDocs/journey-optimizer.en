---
title: Arithmetic functions library
description: Arithmetic functions library
feature: Personalization
topic: Personalization
role: Developer
level: Experienced
exl-id: 21ef8f50-8389-4675-a8e5-0438a3eee592
---
# Arithmetic functions {#maths}

Arithmetic functions are used to perform basic calculations on values.

## Add{#add}

The `+` (addition) function is used to find the sum of two argument expressions.

**Syntax**

```sql
{%= double + double %}
```

**Example**

The following operation sums the price of two different products.

```sql
{%= product1.price + product2.price %}
```

## Multiply{#multiply}

The `*` (multiplication) function is used to find the product of two argument expressions.

**Syntax**

```sql
{%= double * double %}
```

**Example**

The following operation finds the product of the inventory and the price of a product to find the gross value of the product.

```sql
{%= product.inventory * product.price %}
```

## Subtract{#substract}

The `-` (subtraction) function is used to find the difference of two argument expressions.

**Syntax**

```sql
{%= double - double %}
```

**Example**

The following operation finds the difference in price between two different products.

```sql
{%= product1.price - product2.price %}
```

## Divide{#divide}

The `/` (division) function is used to find the quotient of two argument expressions.

**Syntax**

```sql
{%= double / double %}
```

**Example**

The following operation finds the quotient between the total products sold and total money earned to see the average cost per item.

```sql
{%= totalProduct.price / totalProduct.sold %}
```

## Remainder{#remainder}

The `%` (modulo/remainder) function is used to find the remainder after dividing the two argument expressions. 

**Syntax**

```sql
{%= double % double %}
```

**Example**

The following operation checks if the person's age is divisible by five.

```sql
{%= person.age % 5 = 0 %}
```
