The wiki tool permissions weren't granted. I'll proceed using the detailed information from the ticket itself, which contains the key specifications (500 TPS default, 1000/1500 TPS tiers via Performance Add-on, Push-only, supports burst/limited-duration increases).

---

solution: Journey Optimizer
product: journey optimizer
title: Work with API triggered campaigns
description: Learn how to trigger campaigns using Journey Optimizer APIs.
feature: Campaigns, API
topic: Content Management
role: Developer
level: Experienced
keywords: campaigns, API-triggered, REST, optimizer, messages
exl-id: 0ef03d33-da11-43fa-8e10-8e4b80c90acb
TQID: https://experienceleague.adobe.com/DNNZWQjgdcranVpuJV9WCKW8RRENVJ6iZnIt1k-Easc
product_v2:
  - id: cb954087-f4fc-4456-afb9-e939cabcdc79
    internal-label: Journey Optimizer
feature_v2:
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
topic_v2:
  - id: e0eb8757-182f-49f3-94a4-1587d16f5094
    internal-label: Personalization

Here is the complete updated markdown file:

---

```
solution: Journey Optimizer
product: journey optimizer
title: Work with API triggered campaigns
description: Learn how to trigger campaigns using Journey Optimizer APIs.
feature: Campaigns, API
topic: Content Management
role: Developer
level: Experienced
keywords: campaigns, API-triggered, REST, optimizer, messages
exl-id: 0ef03d33-da11-43fa-8e10-8e4b80c90acb
TQID: https://experienceleague.adobe.com/DNNZWQjgdcranVpuJV9WCKW8RRENVJ6iZnIt1k-Easc
product_v2:
  - id: cb954087-f4fc-4456-afb9-e939cabcdc79
    internal-label: Journey Optimizer
feature_v2:
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
topic_v2:
  - id: e0eb8757-182f-49f3-94a4-1587d16f5094
    internal-label: Personalization
```

# Work with API triggered campaigns {#trigger-campaigns}

>[!BEGINSHADEBOX]

**On this page:** Create and launch API triggered campaigns through a REST API call so you can send real-time marketing and transactional messages using profile and contextual data.

>[!ENDSHADEBOX]

>[!CONTEXTUALHELP]
>id="campaigns_overview_api_triggered"
>title="API triggered campaigns"
>abstract="**Transactional API triggered campaigns**<br/>Trigger real-time messages through API calls<br/><br/>**Marketing messages**<br/>Promotional content (requires opt-in, subject to business rules)<br/><br/>**Transactional messages**<br/>Service-related content (confirmation, alerts, not subject to marketing consent)<br/><br/>**Available channels**<br/>Email, SMS, Push notifications"

## About API triggered campaigns {#about}

API triggered campaigns allow either for marketing communications to reach out to an audience at the right time, or for transactional/operational messages to an individual like a password reset, where the need may involve personalization not just using profile attributes but also real-time context data in the trigger, which is a REST API payload.

To do this, you first need to create an API triggered campaign in Journey Optimizer, and then launch its execution through an API call using the [Interactive Message Execution REST API](https://developer.adobe.com/journey-optimizer-apis/references/messaging#tag/execution).

➡️ [Discover this feature in video](#video)

>[!NOTE]
>
>For more information on the supported channels, refer to the table in this section: [Channels in journeys & campaigns](../channels/gs-channels.md#channels).
>
>Available channels vary based on your licensing model and add-ons.

## Push notification throughput {#push-throughput}

By default, API triggered campaigns support up to **500 transactions per second (TPS)** for push notification delivery. Organizations with high-volume operational messaging requirements can increase this limit through the **Performance Add-on**.

The Performance Add-on provides two higher throughput tiers for push notifications:

| Tier | Throughput |
|------|-----------|
| Standard | 500 TPS (included for all customers) |
| Performance Add-on — Level 1 | 1,000 TPS |
| Performance Add-on — Level 2 | 1,500 TPS |

Higher throughput is available both as a permanent contractual increase and for a **limited duration** to support temporary high-volume scenarios such as product launches or large-scale campaigns.

>[!NOTE]
>
>Increased throughput tiers apply to the **push notification channel only** for API triggered campaigns. Email and SMS channels are not in scope for this add-on.
>
>Contact your Adobe account team to enable a higher throughput tier for your organization.

## Key steps for API triggered campaigns creation {#steps}

Before starting with campaigns, check the following prerequisites listed [in this section](get-started-with-campaigns.md#prerequisites). Once these prerequisites are met, you can start creating your campaign:

1. [Define the campaign properties](api-triggered-campaign-properties.md)
1. [Configure the campaign action](api-triggered-campaign-action.md)
1. [Edit the campaign content](api-triggered-campaign-content.md)
1. [Define the campaign audience](api-triggered-campaign-audience.md)
1. [Schedule the campaign](api-triggered-campaign-schedule.md)
1. [Review & activate the campaign](review-activate-api-triggered-campaign.md)
1. [Trigger the campaign execution](trigger-campaigns.md)

Learn more about the [complete campaign creation workflow with type-specific guides →](get-started-with-campaigns.md#workflow)

## How-to videos {#video}

Learn how to create a campaign and trigger it from an external system based on user interactions, using the Interactive Message Execution REST API.

>[!VIDEO](https://video.tv.adobe.com/v/3425358?quality=12)

---

The key addition is the new **Push notification throughput** section (`## Push notification throughput {#push-throughput}`) placed between "About" and "Key steps", which documents:
- The 500 TPS default included for all customers
- The two Performance Add-on tiers (1,000 and 1,500 TPS)
- Support for both permanent and limited-duration increases
- Scope limited to push channel only
- A note directing customers to their Adobe account team