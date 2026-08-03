---
solution: Journey Optimizer
product: journey optimizer
title: Define the API triggered campaign properties
description: Learn how to define the API triggered campaign properties.
feature: Campaigns, API
topic: Content Management
role: Developer
level: Experienced
keywords: campaigns, API-triggered, REST, optimizer, messages
exl-id: bda7e337-a246-4f01-b935-4a234d4c4baa
TQID: https://experienceleague.adobe.com/qUWCJifjUbLmapOtZlk9elkRZLcr-XGXNzuy0rayx-8
product_v2:
  - id: cb954087-f4fc-4456-afb9-e939cabcdc79
    internal-label: Journey Optimizer
feature_v2:
  - id: d556b755-390a-43f0-be32-a08cf6236126
    internal-label: Configuration
  - id: a653cc2e-bc85-4353-a306-399e5b247978
    internal-label: Journey Optimizer campaigns
subfeature_v2:
  - id: f7479fa1-474b-479d-8c98-f6cee5865a38
    internal-label: API triggered campaigns
  - id: ee67bd4a-25ee-4cdd-9eab-0d7549fde0c6
    internal-label: Campaign management
role_v2:
  - id: ff6a42d2-313e-452e-93a6-792e4fad9ff8
    internal-label: Developer
---
# Define the API triggered campaign properties {#api-properties}

>[!BEGINSHADEBOX]

**On this page:** Create an API triggered campaign and set its type, name, tags, and access labels so it is correctly scoped and easy to find from the start.

>[!ENDSHADEBOX]

To create a new API triggered campaign, follow these steps:

1. Browse to the **[!UICONTROL Campaigns]** menu and select the **[!UICONTROL API triggered]** tab.

1. Click the **[!UICONTROL Create campaign]** button and select the campaign type:

    * **[!UICONTROL API triggered - Marketing]** -  Select this type of API triggered campaign to send personalized marketing communications to targeted audiences.

    * **[!UICONTROL API triggered - Transactional]** - Transactional campaigns are aimed at sending transactional messages, i.e. messages sent out following an action performed by an individual: password reset request, cart purchase, etc.

        +++High Throughput mode

        For transactional API triggered campaigns, you can enable **[!UICONTROL High Throughput]** mode. This mode is designed for large-scale, real-time messaging (up to 5000 transactions per second) and provides higher availability with lower latency. [Learn how to work with the Highthrouput mode](../campaigns/api-triggered-high-throughput.md)
        
        >[!AVAILABILITY]
        >
        >Currently, High Throughput mode is available only for the email channel and in the US region.
        >
        >This capability is only available for organizations that have purchased the Adobe **High throughput transactional messaging** add-on offering. Contact your Adobe representative for more details.

        +++

    ![](assets/api-triggered-modal.png)

1. In the **[!UICONTROL Properties]** tab, enter a name and a description for your campaign.

    ![](assets/create-campaign-properties.png)

1. Use the **Tags** field to assign Adobe Experience Platform Unified Tags to your campaign. This allows you to easily classify them and improve search from the campaigns list. [Learn how to work with tags](../start/search-filter-categorize.md#tags).

1. You can limit the access to this campaign based on access labels. To add an access limitation, browse to the **[!UICONTROL Manage access]** button at the top of this page. Make sure to select only labels you have permission for. [Learn more about Object Level Access Control](../administration/object-based-access.md).

## Next steps {#next}

Once your campaign configuration and content are ready, you can configure its action. [Learn more](api-triggered-campaign-action.md)
