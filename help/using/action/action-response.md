---
solution: Journey Optimizer
product: journey optimizer
title: Custom action enhancements
description: Learn more about latest enhancements on custom actions
feature: Journeys, Actions, Custom Actions
topic: Administration
role: Developer, Admin
level: Experienced
keywords: action, third-party, custom, journeys, API
exl-id: d88daa58-20af-4dac-ae5d-4c10c1db6956
---
# Use API call responses in custom actions {#custom-action-enhancements}

You can leverage API call responses in custom actions and orchestrate your journeys based on these responses.

<!--
You can now leverage API call responses in custom actions and orchestrate your journeys based on these responses.

This capability was previously only available when using data sources. You can now use it with custom actions. 
-->

## Important notes{#custom-action-enhancements-notes}

<!--
* Custom actions should only be used with private or internal endpoints, and used with an appropriate capping or throttling limit. See [this page](../configuration/external-systems.md). 
-->

* Scalar arrays are supported in response payload:

    ```
    "dummyScalarArray": [
    "val1",
    "val2"
    ]
    ```

* Heterogeneous arrays are not supported in response payload:

    ```
    "dummyRandomArray": [
    20,
    "aafw",
    false
    ]
    ```

<!--
## Best practices{#custom-action-enhancements-best-practices}

A capping limit of 5000 calls/s is defined for all custom actions. This limit has been set based on customers usage, to protect external endpoints targeted by custom actions. You need to take this into account in your audience-based journeys by defining an appropriate reading rate (5000 profiles/s when custom actions are used). If needed, you can override this setting by defining a greater capping or throttling limit through our Capping/Throttling APIs. See [this page](../configuration/external-systems.md).

You should not target public endpoints with custom actions for various reasons:

* Without proper capping or throttling, there is a risk of sending too many calls to a public endpoint that may not support such volume.
* Profile data can be sent through custom actions, so targeting a public endpoint could lead to inadvertently sharing personal information externally.
* You have no control on the data being returned by public endpoints. If an endpoint changes its API or starts sending incorrect information, those will be made available in communications sent, with potential negative impacts.
-->

<!--
## Define the custom action {#define-custom-action}

When defining the custom action, two enhancements have been made available: the addition of the GET method and the new payload response field. The other options and parameters are unchanged. See [this page](../action/about-custom-action-configuration.md).

### Endpoint configuration {#endpoint-configuration}

The **URL configuration** section has been renamed **Endpoint configuration**.

In the **Method** drop-down, you can now select **GET**.

![](assets/action-response1.png){width="70%" align="left"}

### Payloads {#payloads-new}

The **Action parameters** section has been renamed **Payloads**. Two fields are available:

* The **Request** field: this field is only available for POST and PUT calling methods.
* The **Response** field: this is the new capability. This field as available for all calling methods.

>[!NOTE]
> 
>Both these fields are optional.

![](assets/action-response2.png){width="70%" align="left"}
-->

## Configure the custom action {#config-response}

1. Create the custom action. Refer to [this page](../action/about-custom-action-configuration.md).

1. Click inside the **Response** (success response) field. 

    ![](assets/action-response2.png){width="80%" align="left"}

1. Paste an example of the payload returned by the call. Verify that the field types are correct (string, integer, etc.). Here is an example of response payload captured during the call. Our local endpoint sends the number of loyalty points and the status of a profile. 

    ```
    {
    "customerID" : "xY12hye",    
    "status":"gold",
    "points": 1290 }
    ```

    ![](assets/action-response4.png){width="80%" align="left"}

    Each time the API is called, the system will retrieve all the fields included in the payload example.

1. (Optional) Enable an error response payload to capture the format returned when the call fails, then paste an example payload. To do this, select **Define a failure response payload** in the custom action configuration. Learn more about configuring the payload fields in [Configure a custom action](../action/about-custom-action-configuration.md).

    ```
    {
    "errorResponse" : "customer not found"
    }
    ```

    The error response payload is only available if you enable it in the custom action configuration.

1. Let's also add the customerID as a query parameter.

    ![](assets/action-response9.png){width="80%" align="left"}

1. Click **Save**.

## Leverage the response in a journey {#response-in-journey}

Simply add the custom action to a journey. You can then leverage the response payload fields in conditions, other actions and message personalization.

If you have defined an error response payload, it is exposed under **Contextual attributes** > **Journey Orchestration** > **Actions** > `<action name>` > **errorResponse**. You can use it in the timeout and error branch to drive fallback logic and error handling.

For example, you can add a condition to check the number of loyalty points. When the person enters the restaurant, your local endpoint sends a call with the profile's loyalty information. You can send a push if the profile is a gold customer. And if an error is detected in the call, send a custom action to notify your system administrator.

![](assets/action-response5.png)

1. Add your event and the Loyalty custom action created earlier. 

1. In the Loyalty custom action, map the customer ID query parameter with the profile ID. Check the option **Add an alternative path in case of a timeout or error**.

    ![](assets/action-response10.png)

1. In the first branch, add a condition and use the advanced editor to leverage the action response fields, under the **Context** node.

    ![](assets/action-response6.png)

1. Then add your push, and personalize your message using the response fields. In our example, we personalize the content using the number of loyalty points and the customer status. The action response fields are available under **Contextual attributes** > **Journey Orchestration** > **Actions**.

    ![](assets/action-response8.png)

    >[!NOTE]
    >
    >Each profile entering the custom action will trigger a call. Even if the response is always the same, Journey will still perform one call per profile.

1. In the timeout and error branch, add a condition and leverage the built-in **jo_status_code** field. In our example, we're using the 
**http_400** error type. See [this section](#error-status).

    ```
    @action{ActionLoyalty.jo_status_code} == "http_400"
    ```

    If an error response payload has been defined, you can also target its fields, for example:

    ```
    @action{ActionLoyalty.errorResponse.errorResponse} == "customer not found"
    ```

    ![](assets/action-response7.png)

1. Add a custom action that will be sent to your organization.

    ![](assets/action-response11.png)

## Test mode logs {#test-mode-logs}

You can access, through test mode, status logs related to custom action responses. If you have defined custom actions with responses in your journey, you will see an **actionsHistory** section on those logs displaying the payload returned by the external endpoint (as a response from that custom action). When an error response payload is defined, it is included for failed calls. This can be very useful in terms of debugging.

![](assets/action-response12.png)

## Error status {#error-status}

The **jo_status_code** field is always available even when no response payload is defined.

Here are the possible values for this field: 

* http status code: http_`<HTTP API call returned code>`, for instance http_200 or http_400
* timeout error: **timedout**
* capping error: **capped**
* internal error: **internalError**

An action call is considered in error when the returned http code is greater than 2xx or if an error occurs. The journey flows to the dedicated timeout or error branch in such cases.

If an error response payload has been configured for the custom action, its fields are exposed under the **errorResponse** node for failed calls. If no error response payload is configured, that node is not available.

>[!WARNING]
>
>Only newly created custom actions include the **jo_status_code** field out-of-the-box. If you want to use it with an existing custom action, you need to update the action. For example, you can update the description and save.

## Expression syntax {#exp-syntax}

Here is the syntax:

```json
#@action{myAction.myField} 
```

Here are a few examples:

```json
 // action response field
 @action{<action name>.<path to the field>}
 @action{ActionLoyalty.status}
```

```json
 // action response field
 @action{<action name>.<path to the field>, defaultValue: <default value expression>}
 @action{ActionLoyalty.points, defaultValue: 0}
 @action{ActionLoyalty.points, defaultValue: @event{myEvent.newPoints}}
```

While manipulating collections in a custom action response, you can rely on `currentActionField` to access the current item:

```json
count(
@action{MyAction.MyCollection.all(
currentActionField.description == "abc"
)}
)
```

### Using custom action responses in native channels {#response-in-channels}

Response payload fields from custom actions can be used in native channels (email, push, SMS) for message personalization. This includes the ability to iterate over arrays and nested data structures returned by external APIs.

For detailed examples and syntax for iterating over custom action response data in messages, refer to [Iterate over contextual data with Handlebars](../personalization/iterate-contextual-data.md#custom-action-responses).

## Additional resources

For more information, refer to these pages:

* [Field references](../building-journeys/expression/field-references.md).
* [Collection management functions](../building-journeys/expression/collection-management-functions.md)
