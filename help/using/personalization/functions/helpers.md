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

1. **Conditional content based on audience membership**

    ```sql
    {%#if profile.segmentMembership.get("ups").get("5fd513d7-d6cf-4ea2-856a-585150041a8b").status = "existing"%}
    Hi! Esteemed gold member. <a href="https://www.somedomain.com/gold">Checkout your exclusive perks </a>
    {%else if profile.segmentMembership.get("ups").get("5fd513d7-d6cf-4ea2-856a-585150041a8c").status = "existing"%}
    Hi! Esteemed silver member. <a href="https://www.somedomain.com/silver">Checkout your exclusive perks </a>
    {%/if%}
    ```

>[!NOTE]
>
>To learn more about audiences and the segmentation service, refer to [this section](../../audience/about-audiences.md).


## Unless{#unless}

The `unless` helper is used to define a conditional block. By opposition to the `if`  helper, if the expression evaluation returns false, the block is rendered.

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
Some edu specific content
{%/unless%}
```

## Each{#each}

The `each` helper is used to iterate over an array.
The syntax of the helper is ```{{#each ArrayName}}``` YourContent {{/each}} 
We can refer to the individual array items by using the keyword **this** inside the block. The index of the array's element can be rendered by using {{@index}}. 

**Syntax**

```sql
{{#each profile.productsInCart}}
    <li>{{this.name}}</li>
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

The following example lets you calculate the total sum of prices for products in the cart with prices between 100 and 1000.

```sql
{% let sum = 0%}
    {{#each profile.productsInCart as |p|}}
        {%#if p.price>100 and p.price<1000%}
            {%let sum = sum + p.price %}
        {%/if%}
    {{/each}}
{{sum}}
```

## Execution Metadata {#execution-metadata}

>[!AVAILABILITY]
>
>This capability is available in Limited Availability. Contact your Adobe representative to gain access.

The `executionMetadata` helper allows to dynamically capture and store custom key-value pairs into the message execution context.

**Syntax**

```
{{executionMetadata key="your_key" value="your_value"}}
```

In this syntax, `key` refers to the metadata name and `value` is the metadata to persist.

**Use case**

With this function, you can append contextual information to any native action from your campaigns or journeys. This enables you to export real-time delivery contextual data to external systems for various purposes such as tracking, analytics, personalization and downstream processing.

>[!NOTE]
>
>The Execution Metadata function is not supported by [custom actions](../../action/action.md).

For instance, you can use the Execution Metadata helper to append a specific ID to each delivery sent to each profile. This information is generated during runtime and the enriched execution metadata can then be exported for downstream reconciliation with an external reporting platform.

**How it works**

Select any element from your channel content inside a campaign or a journey and, using the personalization editor, add the `executionMetadata` helper to this element. 

>[!NOTE]
>
>The Execution Metadata function is not visible when the content itself is displayed.


Upon runtime, the metadata value is added to the existing **[!UICONTROL Message Feedback Event Dataset]** with the following schema addition:

```
"_experience": {
  "customerJourneyManagement": {
    "messageExecution": {
      "metadata": {
        "your_key": "your_value"
      }
    }
  }
}
```

>[!NOTE]
>
>Learn more on datasets in [this section](../../data/get-started-datasets.md).

**Limitation**

There is an upper limit of 2kb on the key value pairs per action.

If the 2Kb limit is exceeded, the message is still delivered, but any of the key value pairs can be truncated.

**Example**

```
{{executionMetadata key="firstName" value=profile.person.name.firstName}}
```

In this example, assuming `profile.person.name.firstName` = "Alex", the resulting entity is:

```
{
  "key": "firstName",
  "value": "Alex"
}
```

