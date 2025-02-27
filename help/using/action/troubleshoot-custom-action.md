---
solution: Journey Optimizer
product: journey optimizer
title: Troubleshoot your custom actions
description: Learn how to troubleshoot a custom action
badge: label="Limited Availability"
feature: Journeys, Actions, Custom Actions
topic: Administration
role: Data Engineer, Data Architect, Admin
level: Experienced
keywords: action, third-party, custom, journeys, API
exl-id: c0bb473a-82dc-4604-bd8a-020447ac0c93
---
# Troubleshoot your custom actions {#troubleshoot-a-custom-action}

>[!AVAILABILITY]
>
>This capability is only available for a set of organizations (Limited Availability). To gain access, contact your Adobe representative.
>

You can test your custom actions by sending API calls from the administration section of Journey Optimizer user interface. This capability helps you troubleshoot your custom actions before or after using them in a journey.

As an administrator, use the **[!UICONTROL Send test request]** capability to validate your custom action configurations by making real API calls directly from Adobe Journey Optimizer. This feature ensures that the request structure, headers, authentication, and payload are correctly formatted before being used in a journey.

![](assets/send-test-request.png){width="70%" align="left"}

Use this capability streamlines the testing and validation process, ensuring that custom actions function correctly in live journeys.

## Prerequisites {#troubleshoot-custom-action-prereq}

To use the **[!UICONTROL Send test request]** capability, a **custom action** must be pre-configured with a URL, headers, and authentication settings.

For the administrators to use this capability, the following permissions are required:

* Users must have the **[!DNL Manage journeys events, data sources and actions]** permission.
* This permission is included in the *Journey Administrators* role.
* The **[!DNL View journeys events]** permission alone is not sufficient.

Learn more about journey permissions in [this section](../administration/high-low-permissions.md#journey-capability).

## How to use the Send test request feature {#troubleshoot-custom-action-use}

To test a custom action, follow these steps: 

1. Navigate to the **Actions** configuration screen, and select a custom action.
1. Click on the **[!UICONTROL Send test request]** button at the bottom of the action configuration screen. 
  ![Send test request button in the Action configuration panel](assets/test-request.png){width="70%" align="left"}
1. In the pop-up window, allowing you to specify request parameters:

   * If the **custom action method is GET**, no payload is required.
   * If the **custom action method is POST**, you must provide a JSON payload.

        >[!NOTE]
        >
        >Adobe Journey Optimizer will raise an error if the structure of this JSON is incorrect, but will not do it if there is a mismatch with a data type. For instance, there will be no error if an integer parameter is used for what should be a string.

   * If authentication is defined, you will be prompted to enter authentication details.

1. Click **Send** to execute the request.
1. The response from the API, including headers and status codes, will be displayed in the interface.

## Authentication handling {#troubleshoot-custom-action-auth}

When a custom action includes authentication, Adobe Journey Optimizer requires the user to enter authentication details for each test request:

* **Basic Authentication:** The user must provide the *password*.
* **API Key Authentication:** The user must enter the API key *value*.
* **Custom Authentication:** The user must supply the authentication parameters in the request *bodyParam*. Two sections are added in this case: **Authentication request** and **Authentication response**.

## Key benefits {#troubleshoot-custom-action-benefits}

As a Journey Optimizer administrator, you can also use external tools (e.g., Postman) to test your custom actions. Key benefits of the in-product troubleshooting capability compared to an external testing are listed below: 

* The test request is executed by **AJO Journey**, meaning:

  * The exact request structure (including Adobe Journey Optimizer specific headers) is used.
  * The source IP and headers match those used in live journeys.

* The **[!UICONTROL Send test request]** capability can be used for troubleshooting **live journeys**, as the custom action is already deployed.

* This in-product testing capability eliminates the need to manually copy configuration details between tools, reducing the risk of errors.

## Troubleshooting {#troubleshoot-custom-action-check}

If the request fails, you can check:

* The authentication credentials entered in the test.
* The request method (GET vs. POST) and corresponding payload.
* The API endpoint and headers defined in the custom action.
* Use the response data to identify potential misconfigurations.
