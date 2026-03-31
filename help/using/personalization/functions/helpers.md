---
title: Helpers
description: Helpers
feature: Personalization
topic: Personalization
role: Developer
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
    <a href="https://www.somedomain.com/en">Checkout our catalog</a>
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
The syntax of the helper is ```{{#each ArrayName}}``` YourContent `{{/each}}` 
We can refer to the individual array items by using the keyword **this** inside the block. The index of the array's element can be rendered by using `{{@index}}`. 

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

>[!NOTE]
>
>You can also use the `each` helper to iterate over arrays returned from custom action responses. For an example of iterating over nested arrays from a custom action response, see [Using custom action responses in native channels](../../action/action-response.md#response-in-channels).

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
>* The Execution Metadata function is not supported by [custom actions](../../action/action.md).
>* The Execution Metadata function is not visible when the content itself is displayed.

For instance, you can use the Execution Metadata helper to append a specific ID to each delivery sent to each profile. This information is generated during runtime and the enriched execution metadata can then be exported for downstream reconciliation with an external reporting platform.

**How it works**

Select any element from your channel content inside a campaign or a journey and, using the personalization editor, add the `executionMetadata` helper to this element.


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

**Limitations**

There is an upper limit of 2kb on the key value pairs per action. If the 2Kb limit is exceeded, the message is still delivered, but any of the key value pairs can be truncated.

Metadata is not captured for profiles excluded from the action. When a profile is excluded from receiving a message, no metadata entry is created for that profile in the dataset.

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

## URL parameter encryption {#url-parameter-encryption-helper}

>[!AVAILABILITY]
>
>This feature is available in Limited Availability. Contact your Adobe representative to gain access.
>
>This capability is currently only available for the Email channel.

The `EncryptParam` helper lets you encrypt any expression value at render time—commonly a profile attribute, a token, or even a stringified JSON structure you build in the expression—before it is written into a query parameter on tracking links or landing pages.

Values that would appear as plain text in the URL (including PII or other sensitive data) are not readable when the link is inspected or forwarded. Only the values you wrap with this helper are encrypted; the rest of the URL is unchanged.

You can apply the helper to one parameter, several, or all parameters in a link, depending on your URL design and length constraints.

**Prerequisites**

* URL parameter encryption must be enabled for your organization (Limited Availability). Contact your Adobe representative to gain access.
* An administrator must create at least one active key in the sandbox-level key registry. [Learn how to create and manage keys](../url-parameter-encryption.md)

**How it works**

1. From the helper list, select the `EncryptParam` helper.

1. Pass `data`: the value or expression to encrypt (for example `profile` fields, a variable, or a composed string token).

1. Pass `key`: an active key identifier from your sandbox key registry.

>[!NOTE]
>
>Using a revoked or otherwise non-active key should cause the personalization to fail at render time so a message is not sent with an invalid key.

**Example**

Suppose you define or compute a value (for example a variable `stringToken` that holds a JSON payload or concatenated identifiers) that must not appear as plain text in the `token` query parameter. A final URL can follow this pattern—replace `stringToken` with your expression and `encrypt-key` with an active key ID from the key registry:

```text
https://example.com/verify?token={{encrypt data=stringToken key="encrypt-key"}}
```

**Guardrails**

Decryption is handled outside [!DNL Journey Optimizer] on your landing pages, apps, or APIs. Plan key lifecycle and rotation with your security team so historical payloads can still be decrypted where needed.

Revoked keys must not be used for new encryption. Follow your security policy for rotation and decommissioning.

