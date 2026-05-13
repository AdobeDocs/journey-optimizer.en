---
title: Objects functions library
description: Objects functions library
feature: Personalization
topic: Personalization
role: Developer
level: Experienced
exl-id: 6ce70e32-aac3-4a2c-bfeb-c370521853ca
TQID: https://experienceleague.adobe.com/EdvzBXdtv1Mm4yIZ8ehu4tx6uQBxnpcXTMVQIc1oQkI
product_v2:
  - id: cb954087-f4fc-4456-afb9-e939cabcdc79
    internal-label: Journey Optimizer
role_v2:
  - id: ff6a42d2-313e-452e-93a6-792e4fad9ff8
    internal-label: Developer
topic_v2:
  - id: e0eb8757-182f-49f3-94a4-1587d16f5094
    internal-label: Personalization
---
# Object Functions {#objects}

## Is null{#isNull}

The `isNull` function determines if an object reference does not exist.

**Syntax**

```sql
{%= isNull(object) %}
```

**Example**

The following operation checks if the person's home address does not exist.

```sql
{%= isNull(person.homeAddress) %}
```

## Is not null{#isNotNull}

The `isNotNull` function determines if an object reference exists.

**Syntax**

```sql
{%= isNotNull(object) %}
```

**Example**

The following operation checks if the person's home address exists.

```sql
{%= isNotNull(person.homeAddress) %}
```
