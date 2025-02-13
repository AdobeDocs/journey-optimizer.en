---
solution: Journey Optimizer
product: journey optimizer
title: About the Time-to-live (TTL) and streaming segmentation changes
description: Time-to-live and streaming segmentation changes in Adobe Journey Optimizer
feature: Data Model, Datasets, Data Management
role: Data Engineer, Data Architect, Admin
level: Experienced
keywords: platform, data lake, create, lake, datasets, profile
exl-id: 08633a79-5601-4e36-b8cf-080234956d99
---
# Time-to-live and streaming segmentation changes {#ttl-guardrail}
 
## Streaming segmentation updates {#segmentation-update}

Starting November 1st, 2024, streaming segmentation will no longer support the use of send and open events from Journey Optimizer tracking and feedback datasets. This change will apply to all customer sandboxes and organizations. Information on why this practice has been discouraged in the past can be found [here](../audience/about-audiences.md#streaming-segmentation-events-guardrails).

**Frequently Asked Questions**

+++ Will these changes impact the use of clicks or other tracking events?

This change only impacts the use of send and open events; clicks and other tracking events can still be used in a streaming segment.

+++

+++ Will batch segmentation be impacted by this change?

This change only impacts streaming segmentation; send and open events can still be used in a batch segment. If they are used in a streaming segment, they will be evaluated in a batch manner.

+++

+++ Will this change impact the collection of tracking data?

This change does not impact the collection of tracking data. Send and open events will continue to be collected.

+++

+++ Are reaction events impacted by this change?

Reaction events in Journeys are not impacted by this change.

+++

+++ Will this change apply to production sandboxes only or will it apply to dev sandboxes as well?

This change will apply to all sandbox types.

+++ 

+++ Are feedback events resulting from the send event also impacted by the change?

This change also applies to exclusion events and bounce/delay events resulting from the send.

+++

## Phased time-to-live (TTL) update {#ttl}

Starting in February 2025, a time-to-live (TTL) guardrail will be rolled out to Journey Optimizer system-generated datasets in **new sandboxes and new organizations** as follows:

* 90 days for data in the profile store
* 13 months for data in the data lake 

This change will be rolled out to **existing customer sandboxes** in a subsequent phase.
 
**Frequently Asked Questions**

+++ Will this change apply to production sandboxes only or will it apply to dev sandboxes as well?

This change will apply to all sandbox types.

+++

+++ For the 90 day TTL in profile store, are profiles themselves impacted?

The system-generated dataset data in the profile is dropped after 90 days, not the profiles themselves.

+++

+++ If a system-generated dataset data is pushed to Customer Journey Analytics (CJA), will the data in CJA also be impacted by the TTL?

Data in CJA is kept in sync with Experience Platform. Therefore, a removal of data due to a TTL on system-generated dataset data will also impact the data in CJA.

+++
