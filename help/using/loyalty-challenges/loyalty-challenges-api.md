---
solution: Journey Optimizer
product: journey optimizer
title: Loyalty Challenges APIs
description: Learn how to use the Loyalty Challenges REST APIs to programmatically manage challenges and query profile participation state in Adobe Journey Optimizer.
feature: Journeys
topic: Content Management
role: Developer
level: Intermediate
exl-id: a1b2c3d4-e5f6-7890-abcd-ef1234567890
feature_v2: []
subfeature_v2: []
---

# Loyalty Challenges APIs {#loyalty-challenges-api}

>[!BEGINSHADEBOX]

**On this page:** Learn how to use the Loyalty Challenges REST APIs to programmatically create and manage challenges, and to query and update challenge participation state for individual profiles.

>[!ENDSHADEBOX]

## Quick access {#quick-access}

Two REST APIs are available for Loyalty Challenges:

* **[Loyalty challenge metadata API](https://developer.adobe.com/journey-optimizer-apis/references/loyalty-challenges){target="_blank"}** — Create, retrieve, update, publish, archive, and duplicate challenges programmatically.
* **[Loyalty challenge state API](https://developer.adobe.com/journey-optimizer-apis/references/loyalty-challenges-state){target="_blank"}** — Query and update challenge participation state for individual profiles.

## Loyalty challenge metadata API {#metadata-api}

The Loyalty challenge metadata API lets you manage the full lifecycle of challenges outside the Journey Optimizer UI. Use it to automate challenge operations or integrate loyalty program management into your own tools and workflows. You can, for example, create, publish, and archive challenges, retrieve all challenges with filtering and sorting, or duplicate an existing challenge including its journey metadata and campaigns.

➡️ [Loyalty challenge metadata API reference](https://developer.adobe.com/journey-optimizer-apis/references/loyalty-challenges){target="_blank"}

## Loyalty challenge state API {#state-api}

The Loyalty challenge state API lets you interact with challenge participation records at the profile level. Use it to query a profile's current participation status, progress, and task completion — for example, retrieve all challenge participation records for a profile, check the state of a specific task within a challenge, or withdraw a profile from one or more challenges.

➡️ [Loyalty challenge state API reference](https://developer.adobe.com/journey-optimizer-apis/references/loyalty-challenges-state){target="_blank"}

## Authentication {#authentication}

All Loyalty Challenges API calls require the following headers:

| Header | Description |
|---|---|
| `Authorization` | Bearer token from your IMS access token |
| `x-gw-ims-org-id` | Your IMS organization ID |
| `x-api-key` | Your client ID (API key) |
| `x-sandbox-name` | The name of the sandbox to target |

Follow the [authentication tutorial](https://developer.adobe.com/journey-optimizer-apis/references/authentication){target="_blank"} to retrieve these credentials.
