---
solution: Journey Optimizer
product: journey optimizer
title: Personalization syntax
description: Learn how to use personalization syntax.
feature: Personalization
topic: Personalization
role: Data Engineer
level: Intermediate
keywords: expression, editor, syntax, personalization
exl-id: 5a562066-ece0-4a78-92a7-52bf3c3b2eea
---
# Personalization syntax {#personalization-syntax}

Personalization in [!DNL Journey Optimizer] is based on the templating syntax called Handlebars. For a complete description of the Handlebars syntax, refer to [HandlebarsJS documentation](https://handlebarsjs.com/).

It uses a template and an input object to generate HTML or other text formats. Handlebars templates look like regular text with embedded Handlebars expressions.

Simple expression sample: 

`{{profile.person.name}}`

where:

* `profile` is a namespace.
* `person.name` is a token composed by attributes. The attributes structure is defined in an Adobe Experience Platform XDM Schema. [Learn more](https://experienceleague.adobe.com/docs/experience-platform/xdm/home.html){target="_blank"}.

## Syntax general rules {#general-rules}

* Identifiers may be any unicode character except for the following: 

    ```
    Whitespace ! " # % & ' ( ) * + , . / ; < = > @ [ \ ] ^ ` { | } ~
    ```

* The syntax is case sensitive.

* The words **true**, **false**, **null** and **undefined** are only allowed in the first part of a path expression.

* In Handlebars, the values returned by the {{expression}} are **HTML-escaped**. If the expression contains `&`, then the returned HTML-escaped output is generated as `&amp;`. If you don't want Handlebars to escape a value, use the "triple-stash".

* Regarding literal functions arguments, the templating language parser does not support single unescaped backslash (`\`) symbol. This character must be escaped with an additionnal backslash (`\`) symbol. Example :

    `{%= regexGroup("abc@xyz.com","@(\\w+)", 1)%}` 

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
    * ` {{profile.mobilePhone.number}}`
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

    All the references are validated against Offers Schema with a validation mechanism described in [this page](../personalization/personalization-build-expressions.md)

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

## Helpers{#helpers-all}

A Handlebars helper is a simple identifier that may be followed by parameters. Each parameter is a Handlebars expression. These helpers can be accessed from any context in a template.

These block helpers are identified by a `#` preceding the helper name and require a matching closing `/`, of the same name. 

Blocks are expressions that have a block opening (`{{# }}`) and closing (`{{/}}`).

For more information on helper functions, refer [this section](functions/helpers.md).

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
