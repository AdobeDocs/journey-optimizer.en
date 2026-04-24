---
solution: Journey Optimizer
product: journey optimizer
title: Add a Google TXT record to a subdomain
description: Learn how to add a Google TXT record to a subdomain
feature: Subdomains, Channel Configuration
topic: Administration
role: Admin
level: Experienced
keywords: subdomain, google, txt, record, gmail, deliverability
exl-id: 311eb2d1-e445-43e6-bc2c-c6288b637f47
TQID: https://experienceleague.adobe.com/FCUB2NeETecjNGYnVhkpkYtEZqgX6y-czXinn2t3J84
product_v2:
  - id: cb954087-f4fc-4456-afb9-e939cabcdc79
    internal-label: Journey Optimizer
feature_v2:
  - id: bb359667-ec7d-4d4b-8663-5850fc219d32
    internal-label: Administration
  - id: d556b755-390a-43f0-be32-a08cf6236126
    internal-label: Configuration
  - id: fe338112-e2ce-4876-8989-fc4d497613f1
    internal-label: Email
subfeature_v2:
  - id: e5329d1b-e590-4e24-a3fb-ef3fe0f2c721
    internal-label: Subdomains
role_v2:
  - id: c66ffd68-0f65-42bb-aa23-b4020f12e0bd
    internal-label: Admin
topic_v2:
  - id: eddd9b14-83bd-4ff4-9072-54a4a484abb7
    internal-label: Administration
---
# Add a Google TXT record to a subdomain {#google-txt-record}

>[!CONTEXTUALHELP]
>id="ajo_admin_subdomain_google"
>title="Google TXT records"
>abstract="To ensure successful delivery of emails to Gmail addresses, you can add special Google site verification TXT records to your subdomain to make sure that it is verified."

TXT records are a type of DNS record used to provide text information about a domain, that can be read by external sources.

In order to ensure optimal deliverability and successful delivery of emails to Gmail addresses, [!DNL Journey Optimizer] allows you to add special Google site verification TXT records to your subdomain to make sure that it is verified.

>[!CAUTION]
>
> This operation can only be performed once a subdomain has the **[!UICONTROL Success]** status. For more on subdomains' statuses, refer to [this section](delegate-subdomain.md#access-delegated-subdomains).

## Add a Google TXT record {#add-google-txt-record}

To add a Google TXT record to your subdomain, follow these steps:

1. Open the subdomain from the **[!UICONTROL Channels]** > **[!UICONTROL Email settings]** > **[!UICONTROL Subdomains]** menu.

1. In the **[!UICONTROL Google txt record]** section, enter the verification code generated from [Google Workspace](https://support.google.com/a/answer/183895){target="_blank"}<!--G Suite Admin tools-->, then click **[!UICONTROL Save]**.

    ![](assets/subdomain-google-txt.png)
    
1. Once the TXT record is added, you need to have it verified by Google. To do this, navigate to [Google Workspace](https://support.google.com/a/answer/183895){target="_blank"}<!--G Suite Admin tools-->, then launch the verification step.

## Update a Google TXT record {#update-google-txt-record}

To update an existing Google TXT record, follow these steps:

1. Open the subdomain from the **[!UICONTROL Subdomains]** menu.

1. Clear the existing value in the **[!UICONTROL Google txt record]** field and click **[!UICONTROL Save]**. This step replaces the previous Google TXT record value with an empty string.

1. Now reopen the same subdomain and enter the new verification code.

1. Click **[!UICONTROL Save]** again.

1. Verify the updated record through [Google Workspace](https://support.google.com/a/answer/183895){target="_blank"}.
