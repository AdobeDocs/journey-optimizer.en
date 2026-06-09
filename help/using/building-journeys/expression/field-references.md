---
solution: Journey Optimizer
product: journey optimizer
title: Field references
description: Learn about field references in advanced expressions
feature: Journeys
role: Developer
level: Experienced
keywords: journey, field, expression, event
exl-id: 2348646a-b205-4b50-a08f-6625e92f44d7
version: Journey Orchestration
TQID: https://experienceleague.adobe.com/G8ooc1R2PwL06V89EBs-jH8Lf43F6q5xj3I4Wl6hDHk
product_v2:
  - id: cb954087-f4fc-4456-afb9-e939cabcdc79
    internal-label: Journey Optimizer
feature_v2:
  - id: d998adac-2f81-400b-a669-d07bb196e4eb
    internal-label: Journeys
subfeature_v2:
  - id: fa683eda-48de-4558-af32-2673edcd44fe
    internal-label: Events
role_v2:
  - id: ff6a42d2-313e-452e-93a6-792e4fad9ff8
    internal-label: Developer
---
# Field references {#field-references}

A field reference can be attached to an event or a field group. The only meaningful information is the name of the field and its path. 

If you are using special characters in a field, you need to use double quotes or simple quotes. Here are the cases when quotes are needed:

* the field starts with numerical characters
* the field starts with the "-" character
* the field contains anything other than: _a_-_z_, _A_-_Z_, _0_-_9_, _ , _-_

For example if your field is _3h_: _#{OpenWeather.weatherData.rain.'3h'} > 0_

```json
// event field
@event{<event name>.<XDM path to the field>}
@event{LobbyBeacon.endUserIDs._experience.emailid.id}

// field group
#{<data source name>.<field group name>.<path to the field>}
#{ExperiencePlatform.ProfileFieldGroup.profile.personalEmail.address}
```

In the expression, event fields are referenced with "@" and data source fields are referenced with "#".

A syntax color is used to visually distinguish events fields (green) from field groups (blue).

## Default values for field references {#default-value}

A default value can be associated with a field name. The syntax is as follows:

```json
// event field
@event{<event name>.<XDM path to the field>, defaultValue: <default value expression>}
@event{LobbyBeacon.endUserIDs._experience.emailid.id, defaultValue: "example@adobe.com"}
// field group
#{<data source name>.<field group name>.<path to the field>, defaultValue: <default value expression>}
#{ExperiencePlatform.ProfileFieldGroup.profile.personalEmail.address, defaultValue: "example@adobe.com"}
```

>[!NOTE]
>
>The type of the field and the default value must be the same. For example, `@event{LobbyBeacon.endUserIDs._experience.emailid.id, defaultValue : 2}` is invalid because the default value is an integer whereas the expected value should be a string.

Examples:

```json
// for an event 'OrderEvent' having the following payload:
{
    "orderId": "12345"
}
 
expression example:
- @event{OrderEvent.orderId}                                    -> "12345"
- @event{OrderEvent.productId, defaultValue : "not specified" } -> "not specified" // default value, productId is not a field present in the payload
- @event{OrderEvent.productId}                                  -> null
 
 
// for an entity 'Profile' on datasource 'ACP' having fields person/lastName, with fetched data such as:
{
    "person": {
        "lastName":"Snow"
    },
    "emails": [
        { "email":"john.snow@winterfell.westeros" },
        { "email":"snow@thewall.westeros" }
    ]
}
 
expression examples:
- #{ACP.Profile.person.lastName}                 -> "Snow"
- #{ACP.Profile.emails.at(1).email}              -> "snow@thewall.westeros"
- #{ACP.Profile.person.age, defaultValue : -1}   -> -1 // default value, age is not a field present in the payload
- #{ACP.Profile.person.age}                      -> null
```

You can add any kind of expression as default value. The only constraint is that the expression must return the expected data type. When using a function, encapsulating the function with () is required.

```
#{ExperiencePlatform.Subscriptions.profile.consents.marketing.any.time, defaultValue : (now())} 
== date("2022-02-10T00:00:00Z")
```

## Reference to a field within collections

The elements defined within collections are referenced using the specific functions `all`, `first` and `last`. For more information, refer to [this page](../expression/collection-management-functions.md).

Example :

```json
@event{LobbyBeacon._experience.campaign.message.profile.pushNotificationTokens.all()
```

## Reference to a field defined in a map

### `entry` function

In order to retrieve an element in a map, we use the entry function with a given key. For example, it is used when defining the key of an event, according to the selected namespace. For more information, see [this page](../../event/about-creating.md#select-the-namespace).

```json
@event{MyEvent.identityMap.entry('Email').first().id}
```

In this expression, we are getting the entry for 'Email' key of the 'IdentityMap' field of an event. The 'Email' entry is a collection, from which we take the 'id' in the first element using 'first()'. For more information, see [this page](../expression/collection-management-functions.md).

### `firstEntryKey` function

To retrieve the first entry key of a map, use the `firstEntryKey` function.

This example shows how to retrieve the first email address of the subscribers of a specific list:

```json
#{ExperiencePlatform.Subscriptions.profile.consents.marketing.email.subscriptions.entry('daily-email').subscribers.firstEntryKey()}
```

In this example, the subscription list is named `daily-email`. Email addresses are defined as keys in the `subscribers` map, which is linked to the subscription list map.

### `keys` function

To retrieve to all the keys of a map, use the `keys` function.

This example shows how to retrieve, for a specific profile, all the email addresses that are associated with the subscribers of a specific list:

```json
#{ExperiencePlatform.Subscriptions.profile.consents.marketing.email.subscriptions.entry('daily-mail').subscribers.keys()
```

## Parameter values of a data source (data source dynamic values)

If you select a field from an external data source requiring a parameter to be called, a new tab appears at the right to let you specify this parameter. See [this page](../expression/expressionadvanced.md).

For more complex use cases, if you want to include the parameters of the data source in the main expression, you can define their values using the keyword _params_. A parameter can be any valid expression even from another data source that also includes another parameter.

>[!NOTE]
>
>When you define the parameter values in the expression, the tab at the right disappears.

Use the following syntax:

```json
#{<datasource>.<field group>.fieldName, params: {<params-1-name>: <params-1-value>, <params-2-name>: <params-2-value>}}
```

* **`<params-1-name>`**: exact name of the first parameter from the data source.
* **`<params-1-value>`**: the value of the first parameter. It can be any valid expression.

Example:

```json
#{Weather.main.temperature, params: {localisation: @event{Profile.address.localisation}}}
#{Weather.main.temperature, params: {localisation: #{GPSLocalisation.main.coordinates, params: {city: @event{Profile.address.city}}}}}
```

+++AI Assistant — Page context

* **TL;DR:** This page explains how to reference event fields and data source field groups in journey expressions, including default value syntax, map access functions (`entry`, `firstEntryKey`, `keys`), and inline data source parameter passing with the `params` keyword.

**Intents:**

* Reference an event field in an expression using the `@event{eventName.fieldPath}` syntax
* Reference a data source field group using the `#{dataSourceName.fieldGroupName.fieldPath}` syntax
* Assign a fallback default value to a field reference so expressions do not return null
* Retrieve a specific entry from an identity map or subscription map using the `entry()` function
* Retrieve all keys from a map field using the `keys()` function
* Pass parameter values to an external data source inline using the `params` keyword

**Glossary:**

* **Field reference**: An expression syntax that points to a named field within an event payload or data source field group *(product-specific)*
* **defaultValue**: An optional fallback expression appended to a field reference that is returned when the field is absent or null *(product-specific)*
* **entry(key)**: A map function that retrieves the collection entry associated with the given key *(product-specific)*
* **firstEntryKey()**: A map function that returns the first key of a map field *(product-specific)*
* **keys()**: A map function that returns all keys of a map field *(product-specific)*
* **params keyword**: Inline syntax for specifying parameter values for external data source fields within the main expression *(product-specific)*

**Guardrails:**

* Field names containing special characters (starting with a digit, containing `-`, or characters outside `a-z A-Z 0-9 _`) must be wrapped in single or double quotes
* The default value expression must return the same data type as the field — mismatched types are invalid
* When the `params` keyword is used to define parameter values inline, the separate parameter tab on the right of the editor disappears
* Functions used as default values must be encapsulated in parentheses

**Terminology:**

* Canonical name: Field References — Acronym: none — variants: field path, field expression
* Synonyms: `@event{...}` = "event field reference"; `#{...}` = "data source field reference"
* Do not confuse: event fields (prefixed `@`) ≠ data source fields (prefixed `#`)

**FAQ:**

* **Q: How do I reference a field whose name starts with a number?** — Wrap the field name in single or double quotes, e.g. `#{OpenWeather.weatherData.rain.'3h'}`.
* **Q: What happens when a referenced field is missing from the event payload and no default value is set?** — The expression returns `null`.
* **Q: How do I set a dynamic default value using a function?** — Wrap the function call in parentheses, e.g. `defaultValue: (now())`.
* **Q: How do I retrieve the email address stored as the first key in a subscriber map?** — Use the `firstEntryKey()` function on the subscribers map field.
* **Q: How do I pass a parameter to an external data source without using the right-side tab?** — Use the `params` keyword inline: `#{DataSource.group.field, params: {paramName: value}}`.

+++
