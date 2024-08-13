---
solution: Journey Optimizer
product: journey optimizer
title: Integrate with Marketo Engage
description: Learn how to use the Marketo Engage action
feature: Journeys, Actions, Custom Actions
topic: Administration
role: Data Engineer, Data Architect, Admin
level: Intermediate
hide: yes
hidefromtoc: yes
keywords: marketo, marketo engage integration
---

# Integrate with Marketo Engage {#integrating-with-marketo-engage}

Embark on a journey of seamless data integration with Marketo Engage. This specific custom action in Journey Optimizer supports the ingestion of two key data types:

* Persons (Profiles): Marketo transforms profiles into actionable insights.
* Custom Objects: Tailor your data with custom objects, such as products, for a personalized marketing approach.

## Prerequisites {#prerequisites}

* The customer instance of Marketo Engage must be IMS-enabled.
* Marketo Engage instance and AEP/AJO instance must be in the same IMS Org. +link
* The customer must be provisioned with MktoSync: Ingestion Service access (NOTE TO ADD HERE + link)

## Configuring the action {#configure-marketo-action}

* Navigate to Administration > Configurations > Actions and click on Manage
* From the Actions list, click Create Action. Read more on Custom action creation here (+link)
* Enter Name, Description, and select Adobe Marketo Engage as Action type

![](assets/engage-customaction-creation.png)

* Click Edit payload for your **Request** and **Response** payloads.
* For both, compose your payload and Paste it in the dedicated popup.

![](assets/engage-customaction-payload.png)
  
* Inspect and configure payload values
    Note: To pass values dynamically, for each field change **Constant** to **Variable**.

![](assets/engage-customaction-payload-fields.png)

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

* Drag the custom action onto the journey canvas. (See how to use a custom action / link)
* In Request parameters, click Edit for each of the parameters with dynamic values that you have configured in the payload.

![](assets/engage-use-canvas.png)

