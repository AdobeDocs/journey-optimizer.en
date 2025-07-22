---
solution: Journey Optimizer
product: journey optimizer
title: Personalize content using data from an external endpoint
description: Learn how to dynamically fetch data from an external endpoint to personalize inbound content.
badge: label="Limited Availability" type="Informative"
feature: Personalization, Rules
topic: Personalization
role: Data Engineer
level: Intermediate
keywords: expression, editor
---

# Personalize content using data from an external endpoint {#data-endpoint}

>[!AVAILABILITY]
>
>This capability is only available for a set of organizations (Limited Availability).

Journey Optimizer allows you to leverage data from an external endpoint to personalize your content in inbound channels such as the Code-based Experience, Web and In-App Message channels.

To do so, a dedicated helper function, `externalDataLookup`, is available in the personalization editor. To use the helper, you must first define a [!DNL Journey Optimizer] **Action** where you configure details about the external endpoint.

## Must-read

### Runtime Execution

When an inbound action includes an externalDataLookup helper, the endpoint is called dynamically at the time the personalization request is received and processed by the [!DNL Adobe Experience Platform] Edge Network. This means the external endpoint needs to be able to handle at least as much concurrent load and throughput as the client is sending for the given surface to the AEP Edge Network.

### Authentication

Authentication options in the Action configuration are not currently supported by the externalDataLookup helper.
In the meantime, for API key-based authentication or other plaintext authorization keys, you can specify them as header fields in the Action configuration.
For Adobe-internal endpoints ONLY: contact AJO Engineering to enable service token-based authentication for an endpoint.

### Guardrails & Limitations

Please refer to Custom Actions in AJO Inbound Channels Campaigns and Journeys#GuardrailsandGuidelines as well.

By default, AJO uses a timeout of 300ms when calling an external endpoint. Contact AJO Engineering to increase this timeout for an endpoint.
In the Personalization Editor, AJO does not let you browse the schema of the endpoint response when inserting expressions and does not validate references to JSON attributes from the response used in expressions.
The supported datatypes for payload variable parameters to be substituted via externalDataLookup helper are String, Integer, Decimal, Boolean, listString, listInt, listInteger, listDecimal
Changes to an Action configuration are not reflected in corresponding externalDataLookup calls in live campaigns and journeys. In order for a change to be reflected, you need to copy or modify any live campaigns or journeys that are using the Action in an externalDataLookup helper.
Usage of variables is not supported yet within external data lookup helper parameters yet.
Dynamic URL Path is currently not supported.  - Inbound Custom Actions Enhancements#DynamicPathSegments

## Create an Action

Create an Action to configure the endpoint for the lookup. This only needs to be done once for each endpoint and should be done by a technical user. See this page.

The same Action can be used both in a **[!UICONTROL Custom Action]** activity to fetch content in a journey, and in an `externalDataLookup` helper function to fetch data in an inbound action in a journey or campaign.

Browse to the **[!UICONTROL Administration]** / **[!UICONTROL Configurations]** menu. 

Note the Action ID and copy it to use in step 6.


## Personalize your content using fetched data

### Add the helper function to your content

1. Create an inbound campaign or journey action and edit its content.

1. Locate the content where you want use data feched  from the external endpoint and access the personalization editor.

1. Select the Helper functions menu and locate the `externalDataLookup` helper function.

1. Select to insert the associated syntax into your code and replace the `actionId` and `result` parameters values as follows:

    * `actionId` : Paste the actio nID copied when creating the Action.
    * `result`: Set this parameter to the name of your choice. You'll use this result variable to access the fetched content.

1. Add any variable parameter values to be passed as part of the endpoint call. For example, here is how you might pass a language parameter and a max items parameter.

### Personalize using fetched data

To access the data fetched from an external endpoint lookup call, you can reference fields defined in the response payload in the Action definition using personalization expressions and helper functions.

Use the `result` variable to access the fetched data and insert it into the content for the inbound action. For example, here is how you might return a JSON array of items fetched from the endpoint.

Let's take the example below, where the response payload in the Action has been configured as follows:

```

{
    "videos": [
        {
            "id": "integer",
            "title": "string",
            "description": "string",
            "thumbnail_url": "string",
            "video_page_url": "string",
            "url": "string",
            "video_type": "string",
            "start_timestamp": "dateOnly",
            "created_on": "dateOnly",
            ...
        }
    ]
}

```

Personalization example 1 - Display the description of the first video in a Code-based Experience HTML action:

```

{{externalDataLookup actionId="d130c8e2-9a2d-45d5-bcb6-bc39865b4a56" result="result"}}
 
First video description: <b>result.videos[0].description</b>

```

Personalization example 2 - Return an item array in a Code-based Experience JSON action:

```

{{externalDataLookup actionId="d130c8e2-9a2d-45d5-bcb6-bc39865b4a56" result="result"}}
 
[
{{#each result.videos as |item|}}
    {                                                  
        "title": "{{item.title}}",
        "url": "{{item.video_page_url}}",
        "thumbnail_url": "{{item.thumbnail_url}}",
        "start_timestamp": "{{item.start_timestamp}}"
    },
{{/each}}
]

```

## Timeouts and Error Handling

AJO uses a strict timeout when calling the external endpoint in order to maintain low-latency, high-throughput performance characteristics for the AEP Edge Network.

If the endpoint times out or there is any other sort of error reaching the endpoint, the result variable will be empty. Any references to attributes within the result variable in this case will also be empty. If you are simply displaying the attribute in the content, it will show as blank. If you are attempting to loop through an array attribute in the result, it will return no items.

If you want to more gracefully handle timeouts or errors by showing fallback content, you can check if the result of the lookup is empty and display fallback content in that case.

For example, you can show a fallback value for a single attribute like this:

First video description: {%=result.videos[0].description ?: "none found" %}


or you can conditionally render an entire block of content like this:

{{externalDataLookup actionId="d130c8e2-9a2d-45d5-bcb6-bc39865b4a56" result="result"}}
 
{%#if result%}
   ... do something with result ...
{%else%}
    ... return fallback content ...
{%/if%}
Debugging
To help with debugging, timeout and error details for external data lookups are included in the Edge Delivery view in AEP Assurance. If you are not seeing expected results for an externalDataLookup helper in an inbound action, you can start an Assurance session, initiate an AJO call from a web or mobile implementation, and use the Edge Delivery view to check for timeout or error details.

For example:

Under the Edge Delivery Section of assurance trace as part of execution details a new customActions block has been added with

request and response details similar to the one below. The errors section should help with debugging if there were any issues while executing custom action

## Frequently Asked Questions

+++How to pass a contextual attribute from the request as parameter to an external data lookup?

Use the Contexual Attributes > Datastream > Event menu to browse the Experience Event schema you're using and insert the relevant attribute as a parameter value like this: 

`{{externalDataLookup actionId="..." result="result" query.myQueryParameter=context.datastream.event.<schemaId>.my.xdm.attribute}}`

+++

+++Does AJO do any caching of external endpoint responses?

Not currently. This feature will be supported in the future.

+++









Syntax
{{externalDataLookup actionId="d130c8e2-9a2d-45d5-bcb6-bc39865b4a56" result="result" optional-parameters...}}



Passing Parameters
When the external endpoint is called, all constant header values, query parameters and request payload value defined in the Action will be sent with the values given in the Action configuration.

For any variable header values, query/path parameters or request payload values, you can pass values dynamically using parameters to the externalDataLookup helper.

Parameter names:

Header parameters: header.<parameter-name>
Query parameters: query.<parameter-name>
Payload parameters: payload.<parameter-name>
Path Parameters: dynamic_path.<parameter-name>
For example:

{{externalDataLookup actionId="..." result="result" header.myHeaderParameter="value1" query.myQueryParameter="value2" payload.myPayloadParameter="value3"}}
Parameter values can be fixed values or they can be personalized by referencing profile fields or other contextual attributes, e.g.:

{{externalDataLookup actionId="..." result="result" query.myQueryParameter=profile.myProfileValue}}
Payload parameters can be provided using dot notation to reference nested JSON attributes, e.g.:

{{externalDataLookup actionId="..." result="result" payload.context.channel="web"}}