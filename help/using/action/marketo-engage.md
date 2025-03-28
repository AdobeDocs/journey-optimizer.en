---
solution: Journey Optimizer
product: journey optimizer
title: Integrate with Marketo Engage
description: Learn how to use the Marketo Engage action
feature: Journeys, Actions, Custom Actions
topic: Administration
role: Data Engineer, Data Architect, Admin
level: Intermediate
keywords: marketo, marketo engage integration
exl-id: 70d1ef5a-743b-4362-bb65-93a8c996209f
---
# Integrate with Marketo Engage {#integrating-with-marketo-engage}

Embark on a journey of seamless data integration with Marketo Engage. This specific custom action in Journey Optimizer supports the ingestion of two key data types:

* Persons (Profiles): Marketo transforms profiles into actionable insights.
* Custom Objects: Tailor your data with custom objects, such as products, for a personalized marketing approach.

## Prerequisites {#prerequisites}

* The customer instance of Marketo Engage must be IMS-enabled.
* Marketo Engage instance and Adobe Experience Platform/Journey Optimizer instance must be in the same organization.
* The customer must be provisioned with **MktoSync: Ingestion Service access**

## Configuring the action {#configure-marketo-action}

* Navigate to Administration > Configurations > Actions and click on Manage
* From the Actions list, click Create Action. Read more on [Custom actions](../building-journeys/using-custom-actions.md){target="_blank"}.
* Enter Name, Description, and select Adobe Marketo Engage as Action type

![](assets/engage-customaction-creation.png){width="40%" align="left"}

* Click Edit payload for your **Request** and **Response** payloads.
* For both, compose your payload and Paste it in the dedicated popup.

![](assets/engage-customaction-payload.png){width="70%" align="left"}
  
* Inspect and configure payload values
    Note: To pass values dynamically, for each field change **Constant** to **Variable**.

![](assets/engage-customaction-payload-fields.png){width="70%" align="left"}

* Click **Save** in the Field configuration window then **Save** for your custom action.

You can now use your custom action on your dedicated canvas.


## Payload syntax {#payload-syntax}

### Person

![](assets/payload-person.png)

### CustomObject

![](assets/payload-customobject.png)


**Payload Example for Person**

```json
{
   "munchkinID": "388-KKG-245",  
   "person": {
    "priority": "normal",
    "partitionName": "XYZ",
    "dedupeFields": {
      "field1": "email",
      "field2": "firstName"
    },
    "objects": [
      {
        "email": "Email address",
        "firstName": "First name",
        "lastName": "Last name"
      }
    ]
  }
}
```

**Payload Example for Custom Object**

```json
{
  "munchkinID": "388-KKG-245", 
  "customObject": {
    "priority": "normal",
    "objectName": "products",
    "objects": [
      {
        "email": "Email Address",
        "productName": "Product Name",
        "productQty": "Product Quantity",
        "priceTotal": "Price Total"
      }
    ]
  }
}
```


## Using the action {#engage-using}

* Drag the custom action onto the journey canvas.
* In the **Request parameters** section, click Edit for each of the parameters with dynamic values that you have configured in the payload.

![](assets/engage-use-canvas.png){width="70%" align="left"}
