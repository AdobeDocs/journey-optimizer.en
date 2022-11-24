---
title: Helpers
description: Helpers
feature: Personalization
topic: Personalization
role: Data Engineer
level: Experienced
exl-id: b08dc0f8-c85f-4aca-85eb-92dc76b0e588
---
# Helpers {#gs-helpers}

## Default Fallback Value{#default-value}

The `Default Fallback Value` helper is used to return a default fallback value if an attribute is empty or null. This mechanism works for Profile attributes and Journey events.

**Syntax**

```sql
Hello {%=profile.personalEmail.name.firstName ?: "there" %}!
```

In this example, the value `there` is displayed if the `firstName` attribute of this profile is empty or null.

## Conditions{#if-function}

The `if` helper is used to define a conditional block.
If the expression evaluation returns true, the block is rendered otherwise it is skipped.

**Syntax**

```sql
{%#if contains(profile.personalEmail.address, ".edu")%}
<a href="https://www.adobe.com/academia">Check out this link</a>
```

Following the `if` helper, you can enter an `else` statement to specify a block of code to be executed, if the same condition is false.
The `elseif` statement will specify a new condition to test if the first statement returns false.


**Format**

```sql
{
    {
        {%#if condition1%} element_1 
        {%else if condition2%} element_2 
        {%else%} default_element 
        {%/if%}
    }
}
```

**Examples**

1. **Render different store links based on conditional expressions**

    ```sql
    {%#if profile.homeAddress.countryCode = "FR"%}
    <a href="https://www.somedomain.com/fr">Consultez notre catalogue</a>
    {%else%}
    <a href="https://www.somedomain.com/en">Checkout our catalogue</a>
    {%/if%}
    ```

1. **Determine email address extension**

    ```sql
    {%#if contains(profile.personalEmail.address, ".edu")%}
    <a href="https://www.adobe.com/academia">Checkout our page for Academia personals</a>
    {%else if contains(profile.personalEmail.address, ".org")%}
    <a href="https://www.adobe.com/orgs">Checkout our page for Non Profits</a>
    {%else%}
    <a href="https://www.adobe.com/users">Checkout our page</a>
    {%/if%}
    ```

1. **Add a conditional link**

    The following operation will add a link to the 'www.adobe.com/academia' website for profiles with '.edu' email addresses only, to the 'www.adobe.com/org' website for profiles with '.org' email addresses, and the default URL 'www.adobe.com/users' for all other profiles:

    ```sql
    {%#if contains(profile.personalEmail.address, ".edu")%}
    <a href="https://www.adobe.com/academia">Checkout our page for Academia personals</a>
    {%else if contains(profile.personalEmail.address, ".org")%}
    <a href="https://www.adobe.com/orgs">Checkout our page for Non Profits</a>
    {%else%}
    <a href="https://www.adobe.com/users">Checkout our page</a>
    {%/if%}
    ```

1. **Conditional content based on segment membership**

    ```sql
    {%#if profile.segmentMembership.get("ups").get("5fd513d7-d6cf-4ea2-856a-585150041a8b").status = "existing"%}
    Hi! Esteemed gold member. <a href="https://www.somedomain.com/gold">Checkout your exclusive perks </a>
    {%else%} if 'profile.segmentMembership.get("ups").get("5fd513d7-d6cf-4ea2-856a-585150041a8c").status = "existing"'%}
    Hi! Esteemed silver member. <a href="https://www.somedomain.com/silver">Checkout your exclusive perks </a>
    {%/if%}
    ```

1. **Determine if a profile is already a member**

    ```sql
    {%#if profile.segmentMembership.get(segments.`123e4567-e89b-12d3-a456-426614174000`.id)%}
        You're a member!
    {%else%}
        You should be a member! Sign up now!
    {%/if%}
    ```

>[!NOTE]
>
>To learn more about segmentation and segmentation service, refer to this [section](../../segment/about-segments.md).


## Unless{#unless}

The `unless` helper is used to define a conditional block. By opposition to the The `if`  helper, if the expression evaluation returns false, the block is rendered.

**Syntax**

```sql
{%#unless unlessCondition%} element_1 {%else%} default_element {%/unless%}
```

**Example**

Render some content based on email address extension:

```sql
{%#unless endsWith(profile.personalEmail.address, ".edu")%}
Some Normal Content
{%else%}
Some edu specific content Content
{%/unless%}
```

## Each{#each}

The `each` helper is used to iterate over an array.
The syntax of the helper is ```{{#each ArrayName}}``` YourContent {{/each}} 
We can refer to the individual array items by using the keyword **this** inside the block. The index of the array’s element can be rendered by using {{@index}}. 

**Syntax**

```sql
{{#each profile.productsInCart}}
    <li>{{this.name}}</li>
    </br>
{{/each}}
```

**Example**

```sql
{{#each profile.homeAddress.city}}
  {{@index}} : {{this}}<br>
{{/each}}
```

**Example**

Render a list of products that this user has in their cart:

```sql
{{#each profile.products as |product|}}
    <li>{{product.productName}} {{product.productRating}}</li>
   </br>
{{/each}}
```

## With{#with}

The `with` helper is used to change the evaluation token of template-part.

**Syntax**

```sql
{{#with profile.person.name}}
{{this.firstName}} {{this.lastName}}
{{/with}}
```

The `with` helper is useful to define a shortcut variable too.

**Example**

Use with for aliasing long variable names to shorter ones:

```sql
{{#with profile.person.name as |name|}}
 Hi {{name.firstName}} {{name.lastName}}!
 Checkout our trending products for today!
{{/with}}
```

## Let{#let}

The `let` function allows an expression to be stored as a variable to be used later in a query.

**Syntax**

```sql
{% let variable = expression %} {{variable}}
```

**Example**

The following example lets all sums of product totals with the transaction in USD where the sum is greater than $100 and less than $1000.

```sql
{% let variable = expression %} {{variable}}
```
