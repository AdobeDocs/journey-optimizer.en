---
solution: Journey Optimizer
product: journey optimizer
title: Personalization syntax
description: Learn how to use personalization syntax.
feature: Personalization
topic: Personalization
role: Developer
level: Intermediate
keywords: expression, editor, syntax, personalization
exl-id: 5a562066-ece0-4a78-92a7-52bf3c3b2eea
TQID: https://experienceleague.adobe.com/kZEw2lITdt8SMWMe-UT2vPzdoiAjB2vbItmK9zt-WJo
product_v2:
  - id: cb954087-f4fc-4456-afb9-e939cabcdc79
    internal-label: Journey Optimizer
feature_v2:
  - id: fda7be7c-b81e-42c0-95a9-616e5b893c03
    internal-label: Build expressions
role_v2:
  - id: ff6a42d2-313e-452e-93a6-792e4fad9ff8
    internal-label: Developer
level_v2:
  - id: b5a62a22-46f7-4f0d-b151-3fc640bef588
    internal-label: Intermediate
topic_v2:
  - id: e0eb8757-182f-49f3-94a4-1587d16f5094
    internal-label: Personalization
subfeature_v2:
  - id: ac5d9310-7772-40fb-9d78-864562e1bfd6
    internal-label: Operators
  - id: e51e8901-97d9-4f7d-a835-503025a90e32
    internal-label: Advanced expression editor
---
# Personalization syntax {#personalization-syntax}

>[!BEGINSHADEBOX]

**On this page:** Learn the Handlebars and PQL personalization syntax in Adobe Journey Optimizer, including general rules, reserved keywords, type coercion, available namespaces, and best practices.

>[!ENDSHADEBOX]

Personalization in [!DNL Journey Optimizer] uses two complementary syntaxes that work together in the same expression:

* **Handlebars** (`{{...}}`) — used to render profile attributes, loop over arrays, and call block helpers. Refer to the [HandlebarsJS documentation](https://handlebarsjs.com/) for a complete reference.
* **Profile Query Language (PQL)** (`{%= ... %}`) — used to call built-in functions (e.g. `upperCase()`, `formatDate()`, `dateDiff()`) and evaluate conditional expressions.

Understanding which context you are in is key to avoiding runtime errors. For example, a PQL function call placed inside `{{...}}` will fail because Handlebars tries to resolve it as a helper rather than evaluate it as a PQL expression.

**Examples:**

| Use case | Syntax |
|----------|--------|
| Render a profile attribute | `{{profile.person.name.firstName}}` |
| Call a PQL function | `{%= upperCase(profile.person.name.firstName) %}` |
| Conditional block | `{%#if profile.loyalty.tier = "gold"%}...{%/if%}` |
| Loop over an array | `{{#each profile.orders}}...{{/each}}` |

The attributes structure is defined in an Adobe Experience Platform XDM Schema. [Learn more](https://experienceleague.adobe.com/docs/experience-platform/xdm/home.html){target="_blank"}.

>[!TIP]
>
>For ready-to-use expressions that apply these syntaxes to real-world scenarios — date formatting, countdowns, conditional fallbacks, and more — see the **[Personalization recipes](personalization-recipes.md)** page.

## Syntax general rules {#general-rules}

* Identifiers may be any unicode character except for the following special characters, which are reserved for the Handlebars syntax:

    ```
    Whitespace ! " # % & ' ( ) * + , . / ; < = > @ [ \ ] ^ ` { | } ~
    ```

* The syntax is case sensitive.

* The words **true**, **false**, **null** and **undefined** are only allowed in the first part of a path expression.

* In Handlebars, the values returned by the {{expression}} are **HTML-escaped**. If the expression contains `&`, then the returned HTML-escaped output is generated as `&amp;`. If you do not want Handlebars to escape a value, use the "triple-stash".

    Suppose the value of the field `profile.person.name` is "Mark & Mary". The syntax `{{profile.person.name}}` will display `Mark &amp; Mary`, while `{{{profile.person.name}}}` will show `Mark & Mary`.

* Regarding literal functions arguments, the templating language parser does not support single unescaped backslash (`\`) symbol. This character must be escaped with an additional backslash (`\`) symbol. Example:

    `{%= regexGroup("abc@xyz.com","@(\\w+)", 1)%}`

* To include a **literal double quote** inside a string value (e.g. when generating JSON output), escape it with a backslash (`\"`):

    ```handlebars
    { "message": "Hello \"{{profile.person.name.firstName}}\"" }
    ```

    Output: `{ "message": "Hello \"John\"" }`

    Alternatively, use the triple-stash `{{{ }}}` to output unescaped HTML when the value itself contains special characters you do not want HTML-encoded.

## Reserved keywords {#reserved-keywords}

Certain keywords are reserved in Profile Query Language (PQL) and cannot be used directly as field or variable names in personalization expressions. If your XDM schema contains fields with names that match reserved keywords, you must escape them using backticks (`` ` ``) to reference them in your expressions.

**Reserved keywords include:**

* `next`
* `last`
* `this`

**Example:**

If your profile schema has a field named `next`, you must wrap it in backticks:

```
{{profile.person.`next`.name}}
```

Without the backticks, the personalization editor will fail validation with an error.

>[!NOTE]
>
>Backtick escaping for reserved keywords applies to both `{{...}}` Handlebars paths and `{%= ... %}` PQL expressions, because these keywords are reserved at the path resolution level. This is different from hyphenated field names, where backtick escaping is only supported inside PQL expressions. See [Hyphenated attribute keys](#hyphenated-keys).

## PQL syntax rules for special attribute keys {#pql-special-keys}

Beyond reserved keywords, two additional cases require backtick escaping in PQL expressions.

### Hyphenated attribute keys {#hyphenated-keys}

If your XDM schema contains field names with hyphens (e.g. `my-field`, `event-type`) or names that start with or contain numbers, wrap the key in backticks inside PQL expressions:

```sql
{%= profile.events.`order-total` > 100 %}
```

>[!NOTE]
>
>Backtick escaping is only supported inside PQL expressions (`{%= ... %}`). It is not supported in Handlebars interpolation (`{{...}}`). However, hyphenated field names can be referenced directly in `{{...}}` blocks (e.g. `{{profile.my-custom-field}}`); only backtick syntax fails there.

Without backticks in a PQL expression, the hyphen is interpreted as a subtraction operator and causes a PQL syntax error.

### Numeric event IDs in context attributes {#numeric-event-ids}

When referencing context event attributes where the event ID is a number (e.g. `1697323153`), wrap it in backticks. This also applies inside functions like `formatDate()`:

```handlebars
{% let ts = formatDate(toDateTime(context.journey.events.`1697323153`.timestamp), "dd/MM/yyyy") %}
{{ts}}
```

## Type coercion {#type-coercion}

PQL is strongly typed. When comparing or passing values, both sides must be the same type. Common cases:

| Scenario | Solution |
|----------|----------|
| Numeric value stored as a string | Use `stringToNumber()` before arithmetic or comparison: `{%= stringToNumber(profile.loyalty.pointsBalance) > 500 %}` |
| Integer stored as string | Use `string_to_integer()` or `stringToNumber()` before arithmetic |
| Boolean stored as string | Use `toBool()` to convert: `{%= toBool(profile.consents.email.val) = true %}` |

## Available namespaces {#namespaces}

* **Profile**

    This namespace allows you to reference all the attributes defined in the profile schema described in [Adobe Experience Platform Data Model (XDM) documentation](https://experienceleague.adobe.com/docs/experience-platform/xdm/home.html){target="_blank"}.

    The attributes need to be defined in the schema before being referenced in a [!DNL Journey Optimizer] personalization block.

    For more information how to leverage profile attributes in conditions, refer to [this section](functions/helpers.md#if-function).

    +++Sample references

    * `{{profile.person.name.fullName}}`
    * `{{profile.person.name.firstName}}`
    * `{{profile.person.gender}}`
    * `{{profile.personalEmail.address}}`
    * `{{profile.mobilePhone.number}}`
    * `{{profile.homeAddress.city}}`
    * `{{profile.faxPhone.number}}`

    +++

* **Audience**

    To learn more about the segmentation service, refer to [this documentation](https://experienceleague.adobe.com/docs/experience-platform/segmentation/home.html){target="_blank"}.

* **Offers**

    This namespace allows you to reference existing offers decisions.

    To reference an offer you need to declare a path with the different information that define an offer. This path has the following structure:

    `offers.Type.[Placement Id].[Activity Id].Attribute`

    where:

    * `offers` identifies the path expression belonging to offer namespace
    * `Type`  determines the type of offer representation. Possible values are: `image`, `html` and `text`
    * `Placement Id` and `Activity Id` are placement and activity identifiers
    * `Attributes` are offer specific attributes which depend on the offer type. Example: `deliveryUrl` for images

    For more information on Decisions API and on Offer representations, refer to [this page](../offers/api-reference/offer-delivery-api/decisioning-api.md)

    All the references are validated against Offers Schema with a validation mechanism described on [this page](../personalization/personalization-build-expressions.md)

    +++Sample references

    * Location where the image is hosted:

        `offers.image.[offers:xcore:offer-placement:126f767d74b0da80].[xcore:offer-activity:125e2c6889798fd9].deliveryUrl`

    * Target URL when you click on the image:

        `offers.image.[offers:xcore:offer-placement:126f767d74b0da80].[xcore:offer-activity:125e2c6889798fd9].linkUrl`

    * Text content of the offer coming from the decisioning engine:

        `offers.text.[offers:xcore:offer-placement:126f767d74b0da80].[xcore:offer-activity:125e2c6889798fd9].content`

    * HTML content of the offer coming from the decisioning engine:

        `offers.html.[offers:xcore:offer-placement:126f767d74b0da80].[xcore:offer-activity:125e2c6889798fd9].content`

    +++

## Helpers {#helpers-all}

A Handlebars helper is a simple identifier that may be followed by parameters. Each parameter is a Handlebars expression. These helpers can be accessed from any context in a template.

These block helpers are identified by a `#` preceding the helper name and require a matching closing `/`, of the same name. 

Blocks are expressions that have a block opening (`{{# }}`) and closing (`{{/}}`).

For more information on helper functions, refer to [this section](functions/helpers.md).

## Literal types {#literal-types}

[!DNL Adobe Journey Optimizer] supports the following literal types:

| Literal | Definition |
| ------- | ---------- |
| String | A data type comprised of characters surrounded by double quotes. <br>Examples: `"prospect"`, `"jobs"`, `"articles"` |
| Boolean | A data type that is either true or false.|
| Integer | A data type representing a whole number. It can be positive, negative, or zero. <br>Examples: `-201`, `0`, `412` |
| Array | A data type that is comprised as a group of other literal values. It uses square brackets to group and commas to delimit between different values. <br> **Note:** You cannot directly access properties of items within an array. <br> Examples: `[1, 4, 7]`, `["US", "FR"]` |

>[!CAUTION]
>
>The use of **xEvent** variable is not available in personalization expressions. Any reference to xEvent will result in validation failures.

## Best practices {#best-practices}

Review these syntax rules before building personalization expressions. Most runtime errors come from mixing up Handlebars and PQL contexts.

**Use the correct conditional block syntax**

Always use `{%#if%}` / `{%else if%}` / `{%else%}` / `{%/if%}`. The `{% if %}` / `{% elseif %}` / `{% endif %}` syntax is not supported.

```handlebars
{%#if profile.loyalty.tier = "gold"%}
Gold member content
{%else if profile.loyalty.tier = "silver"%}
Silver member content
{%else%}
Default content
{%/if%}
```

**Do not call PQL functions inside `{{...}}` Handlebars blocks**

`{{...}}` resolves Handlebars variables and helpers only — it does not evaluate PQL. Wrapping a PQL function like `upperCase()` inside `{{...}}` causes a "could not find helper" error. Use `{%= ... %}` instead:

| Incorrect | Correct |
|-----------|---------|
| `{{upperCase(cleanName)}}` | `{%= upperCase(cleanName) %}` |

**Use a named loop alias when combining `{{#each}}` with `{%#if%}`**

`this.field` is resolved by the Handlebars renderer but not by the PQL evaluator inside a `{%#if%}` condition. Define a named alias with `as |item|` so both contexts can resolve the field:

```handlebars
{{#each profile.orders as |order|}}
  {%#if order.status = "pending"%}
  Order {{order.id}} is pending.
  {%/if%}
{{/each}}
```

**Assign PQL function results to a variable before looping**

PQL UDFs such as `topN` cannot be called directly inside `{{#each}}`. Evaluate them first with `{% let %}`, then iterate over the result:

```handlebars
{% let topOrders = topN(profile.orders, price, 3) %}
{{#each topOrders}}
  {{this.name}} — {{this.price}}&euro;
{{/each}}
```

**Use `{% let %}` to avoid repeating function calls**

When a computed value is needed more than once, store it in a variable. This improves readability and prevents redundant evaluations:

```handlebars
{% let cleanName = replaceAll(profile.person.name.firstName, "[^a-zA-Z]", "") %}
Hi {{cleanName}}, your code is: WELCOME-{%= upperCase(cleanName) %}
```

**Use the correct argument order for `dateDiff`**

`dateDiff(start, end)` takes the earlier date first. To compute days remaining until a future date, pass the current date as the first argument:

```handlebars
{% let daysLeft = dateDiff(getCurrentZonedDateTime(), stringToDate(profile.loyalty.expiryDate)) %}
```

**Use `=` for equality comparisons in PQL, not `==`**

PQL uses a single `=` operator for equality. Using `==` results in a syntax error.

**Use backticks for hyphenated field names — in PQL expressions only**

If an XDM schema field name contains a hyphen (e.g. `order-total`), wrap it in backticks to prevent the hyphen from being parsed as a subtraction operator. This is only supported inside `{%= ... %}` PQL expressions, not in `{{...}}` Handlebars blocks:

```sql
{%= profile.events.`order-total` > 100 %}
```

For ready-to-use expressions you can copy directly into your content, see [Personalization recipes](personalization-recipes.md).
