---
title: Decision Management events key information
description: Learn more about the key information sent with each Decision Management event.
feature: Offers
topic: Integrations
role: User
level: Intermediate
exl-id: 07be59e8-e994-4854-8089-25614d005dbe
---
# Decision Management events key information {#events-key-information}

Each event that is sent when a decision is made contains four key data points that you can leverage for analysis and reporting purposes. 

![](../assets/events-dataset-preview.png)

* **[!UICONTROL Fallback]**: Name and ID of the fallback offer, if no personalized offer was selected,
* **[!UICONTROL Placement]**: Name, ID and channel of the placement used to deliver the offer,
* **[!UICONTROL Selections]**: Name and ID of the offer selected for the profile,
* **[!UICONTROL Activity]**: Name and ID of the decision.

Additionally, you can also leverage the **[!UICONTROL identityMap]** and **[!UICONTROL Timestamp]** fields to retrieve information on the profile and the time at which the offer was delivered.

For more information on all the XDM fields that are sent with each decision, refer to [this section](xdm-fields.md).
