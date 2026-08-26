---
solution: Journey Optimizer
product: journey optimizer
title: Reward Definition guide
description: Learn how to configure reward definitions for Loyalty Challenges reward providers in Adobe Journey Optimizer.
feature: Journeys
topic: Content Management
role: Admin
level: Intermediate
mini-toc-levels: 1
exl-id: 9b0fd9d8-18d1-4a51-8b6f-b2e2a4c6f1d7
feature_v2: []
subfeature_v2: []
---
# Reward definition guide {#reward-definition-guide}

>[!CONTEXTUALHELP]
>id="ajo_loyalty_reward_definition"
>title="Reward Definition guide"
>abstract="Use this guide to configure reward definitions for loyalty reward providers, including default definition behavior and fulfillment payload fields."

>[!BEGINSHADEBOX]

**Table of contents**

[Get started with Loyalty Challenges](get-started.md)

<table style="table-layout:fixed">
<tr style="border: 0;">
<td style="vertical-align:top;">

**Create and manage challenges**

* [Access & manage challenges and tasks](access-loyalty-challenges.md)
* [Create challenges](create-challenges.md)
* [Create tasks](create-tasks.md)
* [Monitor loyalty challenge performance](loyalty-reporting.md)

</td>
<td style="vertical-align:top;">

**Configure and integrate**

* [Configure loyalty challenges](loyalty-admin.md)
* **Reward Definition guide** ◀︎ **You are here**
* [Event Transformer guide](event-transformer-guide.md)
* [Loyalty data and datasets](loyalty-data-and-datasets.md)
* [Loyalty Challenges API reference](https://developer.adobe.com/journey-optimizer-apis/references/loyalty-challenges){target="_blank"}

</td>
</tr>
</table>

>[!ENDSHADEBOX]

When a challenge task, milestone, or challenge completes **and has a reward value configured**, the platform issues a reward by calling your reward provider's HTTP endpoint with a JSON payload. A **Reward Definition** describes what reward to issue and provides a [JSONata](https://docs.jsonata.org/overview) expression — `rewardJsonata` — that shapes the exact payload your provider expects.

This guide covers how to configure a reward provider, create reward definitions, write the `rewardJsonata` expression, and understand what context is available to it at evaluation time.

➡️ [Watch how to set up a loyalty reward provider](#video)

## Two-level model

Rewards are organized in two levels:

```
Reward Provider  (endpoint, auth, headers)
└── Reward Definition  (denomination, rewardJsonata)
└── Reward Definition
└── ...
```

A **Reward Provider** represents a single external rewards system — it holds the delivery endpoint URL, authentication, and any custom HTTP headers. One provider can hold multiple **Reward Definitions**, each describing a distinct reward type or denomination offered by that provider (e.g. "50 Stars", "Double Stars", "Free Item").

A challenge references the provider and definition by GUID. When a reward is issued, the platform evaluates the definition's `rewardJsonata` expression and POSTs the result to the provider's endpoint.

## Reward provider & definition fields

+++Reward provider fields

<table>
<colgroup>
<col style="width:160px">
<col style="width:80px">
<col style="width:160px">
<col>
</colgroup>
<tr><th>Field</th><th>Type</th><th>Required</th><th>Description</th></tr>
<tr><td><code>guid</code></td><td><code>String</code></td><td>No (system-assigned)</td><td>Unique identifier. Read-only.</td></tr>
<tr><td><code>name</code></td><td><code>String</code></td><td><strong>Yes</strong></td><td>Display name, unique within the org.</td></tr>
<tr><td><code>desc</code></td><td><code>String</code></td><td>No</td><td>Human-readable description of the provider.</td></tr>
<tr><td><code>enabled</code></td><td><code>Boolean</code></td><td>No</td><td>When <code>false</code>, reward delivery is<br>suspended for all definitions under this provider.</td></tr>
<tr><td><code>url</code></td><td><code>String</code></td><td><strong>Yes</strong></td><td>HTTP endpoint that receives the reward payload.<br>The platform POSTs the evaluated<br><code>rewardJsonata</code> output to this URL.</td></tr>
<tr><td><code>additionalHeaders</code></td><td><code>Object</code></td><td>No</td><td>Custom HTTP headers to include in every<br>delivery request (e.g. API keys,<br>content-type overrides).</td></tr>
<tr><td><code>maxRatePerSecond</code></td><td><code>Integer</code></td><td>No</td><td>Optional per-provider rate limit (1–5000).<br>Null means unlimited.</td></tr>
<tr><td><code>enableMTLS</code></td><td><code>Boolean</code></td><td>No</td><td>Whether the endpoint requires mutual TLS.</td></tr>
</table>

+++

+++Reward definition fields

<table>
<colgroup>
<col style="width:160px">
<col style="width:80px">
<col style="width:160px">
<col>
</colgroup>
<tr><th>Field</th><th>Type</th><th>Required</th><th>Description</th></tr>
<tr><td><code>guid</code></td><td><code>String</code></td><td>No (system-assigned)</td><td>Unique identifier. Read-only.</td></tr>
<tr><td><code>name</code></td><td><code>String</code></td><td><strong>Yes</strong></td><td>Display name, unique within the provider.</td></tr>
<tr><td><code>denomination</code></td><td><code>String</code></td><td>No</td><td>The unit of the reward, used in display<br>and available in expressions as<br><code>reward.denomination</code><br>(e.g. <code>"Stars"</code>, <code>"Points"</code>, <code>"Miles"</code>).</td></tr>
<tr><td><code>desc</code></td><td><code>String</code></td><td>No</td><td>Description of the reward, available<br>in expressions as <code>reward.desc</code>.</td></tr>
<tr><td><code>enabled</code></td><td><code>Boolean</code></td><td>No</td><td>When <code>false</code>, this definition is inactive<br>and will not issue rewards.</td></tr>
<tr><td><code>isDefault</code></td><td><code>Boolean</code></td><td>No</td><td>Marks this as the sandbox-wide default<br>reward definition. Only one definition<br>across all providers may be default at a time;<br>setting a new default clears the previous one.<br>Used to auto-populate reward details on<br>personalized challenges at publish time.</td></tr>
<tr><td><code>rewardJsonata</code></td><td><code>String</code></td><td><strong>Yes</strong></td><td>JSONata expression evaluated at<br>reward-issue time. Receives the full<br>reward context and must return the JSON<br>payload to POST to the provider.</td></tr>
</table>

+++

## The reward context

When `rewardJsonata` is evaluated, it receives a single root object containing everything known about the reward event. All paths in your expression are relative to this root.

```json
{
  "rewardContext": {
    "rewardValue": "50",
    "source":      "challenge"
  },
  "reward": {
    "name":         "500 Stars",
    "desc":         "Issue 500 Stars to the member",
    "denomination": "Stars",
    "enabled":      true
  },
  "task": { ... },
  "milestone": { ... },
  "challenge": { ... },
  "timestamp": "2026-02-10T00:29:22.538+00:00"
}
```

+++ Context fields

| Field                                  | Description |
|----------------------------------------|-------------|
| `rewardContext.rewardValue`            | The reward value string configured on the challenge, task, or milestone that triggered this issuance. |
| `rewardContext.source`                 | What triggered the reward: `"task"`, `"challenge"`, or `"milestone"`. |
| `reward`                               | The RewardDefinition itself — `name`, `desc`, `denomination`. |
| `task`                                 | The completing task, including its `accumulators`, `schedule`, and `reward`. |
| `task.accumulators.spend`              | Total qualifying spend accumulated by the task. |
| `task.accumulators.qty`                | Total qualifying item count accumulated by the task. |
| `task.accumulators.item_list`          | All qualifying items applied to the task. Each entry has `item`, `transactionId`, `timestamp`, `utcOffset`, `locationId`. |
| `task.accumulators.item_list[-1]`      | The most recent item applied (JSONata negative index). Useful for sourcing the last transaction ID or timestamp. |
| `task.schedule.currentStreak`          | Current consecutive-visit streak count (for streak challenges). |
| `task.schedule.currentVisits`          | Total visit count (for visit challenges). |
| `milestone`                            | The milestone that triggered this reward, or `null` if not a milestone reward. Includes `count` and `reward.rewardValue`. |
| `challenge.profileId`                  | The member's loyalty ID. |
| `challenge.kvpCustom`                  | Custom key-value pairs configured on the challenge. A common pattern for passing campaign IDs, product names, or provider-specific metadata. |
| `challenge.name`                       | Challenge name. |
| `challenge._id`                        | Challenge ID. |
| `timestamp`                            | ISO 8601 timestamp of the reward issuance. |

+++

## Writing the rewardJsonata expression

The expression receives the reward context as its input and must return a JSON object — the payload POSTed to the provider's endpoint. The shape of that object is entirely up to the provider's API; you map context fields onto whatever structure the provider expects.

+++Simple fixed payload

The simplest case: the provider needs a point count and a member ID, both known from the context.

```jsonata
{
  "memberId":   challenge.profileId,
  "points":     $number(rewardContext.rewardValue),
  "currency":   reward.denomination
}
```

**Output:**

```json
{
  "memberId": "ADB-0000030",
  "points":   50,
  "currency": "Stars"
}
```

> `rewardContext.rewardValue` is always a string. Use `$number()` to convert it if your provider expects a numeric value.

+++

+++Using `kvpCustom` for provider-specific metadata

Providers often require fields like campaign IDs or source system codes that are specific to each challenge run. Store these in `challenge.kvpCustom` when authoring the challenge, then reference them in the expression — keeping the expression reusable across campaigns.

```jsonata
{
  "memberId":         challenge.profileId,
  "points":           $number(rewardContext.rewardValue),
  "campaignId":       challenge.kvpCustom.campaignId,
  "transactionSource": "AJO"
}
```

You can also use `reward.kvpCustom` for constants that are fixed for a given reward type rather than per-challenge.

+++

+++Using task accumulator data

Task accumulators hold a record of every qualifying event. Use `item_list[-1]` to access the most recently applied item — its `transactionId` and `timestamp` are useful for audit trails and deduplication on the provider side.

```jsonata
{
  "memberId":       challenge.profileId,
  "points":         $number(rewardContext.rewardValue),
  "transactionId":  task.accumulators.item_list[-1].transactionId,
  "transactionDate": task.accumulators.item_list[-1].timestamp
}
```

+++

+++Constructing a text message

For notification-based providers (Slack, SMS, email), you can build a message string directly using JSONata's `&` concatenation operator:

```jsonata
{
  "text": "You just earned " & rewardContext.rewardValue & " " & reward.denomination & "!"
}
```

**Output:**

```json
{
  "text": "You just earned 50 Stars!"
}
```

+++

## Examples

+++Example 1 — Simple points provider

**Scenario:** A basic loyalty points API expects a member ID and a point amount.

**Reward Definition:**

```json
{
  "name":         "Standard Points",
  "denomination": "Points",
  "desc":         "Award loyalty points",
  "enabled":      true,
  "rewardJsonata": "{\"memberId\": challenge.profileId, \"pointQuantity\": $number(rewardContext.rewardValue), \"denomination\": reward.denomination}"
}
```

**Formatted expression:**

```jsonata
{
  "memberId":      challenge.profileId,
  "pointQuantity": $number(rewardContext.rewardValue),
  "denomination":  reward.denomination
}
```

**Payload POSTed to provider:**

```json
{
  "memberId":      "ADB-0000030",
  "pointQuantity": 50,
  "denomination":  "Points"
}
```

+++

+++Example 2 — Provider payload with campaign metadata

**Scenario:** The provider requires a structured award record that includes audit fields, campaign references, and member description. Campaign-specific values are stored in `challenge.kvpCustom` so the same reward definition works across campaigns without editing the expression.

**Challenge `kvpCustom`** (set when authoring the challenge):

```json
{
  "parentCampaignId": "CAMP-2026-Q1",
  "productName":      "Loyalty Program"
}
```

**Reward Definition:**

```json
{
  "name":         "Stars — Campaign Award",
  "denomination": "Stars",
  "desc":         "Issue Stars for completing a qualifying purchase",
  "enabled":      true,
  "rewardJsonata": "{\"awardPoints\":[{\"idType\":\"externalId\",\"id\":challenge.profileId,\"transactionId\":task.accumulators.item_list[-1].transactionId,\"transactionDate\":task.accumulators.item_list[-1].timestamp,\"originalTransactionId\":task.accumulators.item_list[-1].transactionId,\"transactionSource\":\"AJO\",\"channelSource\":\"Web\",\"parentCampaignId\":challenge.kvpCustom.parentCampaignId,\"productName\":challenge.kvpCustom.productName,\"memberAwardDescription\":reward.desc,\"pointQuantity\":$number(rewardContext.rewardValue)}]}"
}
```

**Formatted expression:**

```jsonata
{
  "awardPoints": [
    {
      "idType":                "externalId",
      "id":                    challenge.profileId,
      "transactionId":         task.accumulators.item_list[-1].transactionId,
      "transactionDate":       task.accumulators.item_list[-1].timestamp,
      "originalTransactionId": task.accumulators.item_list[-1].transactionId,
      "transactionSource":     "AJO",
      "channelSource":         "Web",
      "parentCampaignId":      challenge.kvpCustom.parentCampaignId,
      "productName":           challenge.kvpCustom.productName,
      "memberAwardDescription": reward.desc,
      "pointQuantity":         $number(rewardContext.rewardValue)
    }
  ]
}
```

**Payload POSTed to provider:**

```json
{
  "awardPoints": [
    {
      "idType":                "externalId",
      "id":                    "ADB-0000030",
      "transactionId":         "b4fa0e89-f4bb-41ce-b370-fb97f9c52f1a",
      "transactionDate":       "2026-02-08T00:12:00.000+00:00",
      "originalTransactionId": "b4fa0e89-f4bb-41ce-b370-fb97f9c52f1a",
      "transactionSource":     "AJO",
      "channelSource":         "Web",
      "parentCampaignId":      "CAMP-2026-Q1",
      "productName":           "Loyalty Program",
      "memberAwardDescription": "Issue Stars for completing a qualifying purchase",
      "pointQuantity":         50
    }
  ]
}
```

+++

+++Example 3 — Milestone reward

**Scenario:** A streak challenge issues a milestone reward every N visits. The expression includes the milestone count and the current streak for provider-side context.

**Formatted expression:**

```jsonata
{
  "memberId":       challenge.profileId,
  "points":         $number(rewardContext.rewardValue),
  "milestoneCount": milestone.count,
  "currentStreak":  task.schedule.currentStreak,
  "denomination":   reward.denomination,
  "source":         rewardContext.source
}
```

**Payload POSTed to provider** (at 2nd visit milestone):

```json
{
  "memberId":       "ADB-0000030",
  "points":         20,
  "milestoneCount": 2,
  "currentStreak":  2,
  "denomination":   "Stars",
  "source":         "milestone"
}
```

> When `rewardContext.source` is `"milestone"`, the `milestone` object is populated with `count` and `reward.rewardValue`. When the source is `"task"` or `"challenge"`, `milestone` is `null`.

+++

## API reference

+++Reward providers

```http
POST   /loyalty/metadata/config/rewards/providers
GET    /loyalty/metadata/config/rewards/providers
GET    /loyalty/metadata/config/rewards/providers/{providerId}
PUT    /loyalty/metadata/config/rewards/providers/{providerId}
DELETE /loyalty/metadata/config/rewards/providers/{providerId}
```

All requests require `x-gw-ims-org-id` and `x-sandbox-name` headers.

**Create a provider:**

```http
POST /loyalty/metadata/config/rewards/providers
x-gw-ims-org-id: {ORG_ID}
x-sandbox-name: {SANDBOX}
Content-Type: application/json

{
  "name":    "My Points Provider",
  "desc":    "Issues loyalty points via REST",
  "enabled": true,
  "url":     "https://rewards.example.com/award",
  "additionalHeaders": {
    "x-api-key": "YOUR_API_KEY"
  }
}
```

+++

+++Reward definitions

```http
POST   /loyalty/metadata/config/rewards/definitions/{providerId}
GET    /loyalty/metadata/config/rewards/definitions/{providerId}
GET    /loyalty/metadata/config/rewards/definitions/{providerId}/{rewardId}
PUT    /loyalty/metadata/config/rewards/definitions/{providerId}/{rewardId}
DELETE /loyalty/metadata/config/rewards/definitions/{providerId}/{rewardId}
```

**Create a reward definition:**

```http
POST /loyalty/metadata/config/rewards/definitions/{providerId}
x-gw-ims-org-id: {ORG_ID}
x-sandbox-name: {SANDBOX}
Content-Type: application/json

{
  "name":         "50 Stars",
  "denomination": "Stars",
  "desc":         "Award 50 Stars on task completion",
  "enabled":      true,
  "rewardJsonata": "{ \"memberId\": challenge.profileId, \"points\": $number(rewardContext.rewardValue) }"
}
```

+++

## Expression validation

`rewardJsonata` expressions are validated for syntax at publish time. If the expression is invalid, the API returns a `422` error with a description of the parse failure.

To develop and test an expression before publishing, use the [JSONata Exerciser](https://try.jsonata.org/). Paste the reward context JSON as the input document and your expression to verify the output matches what your provider expects. A representative reward context for each trigger type (`task`, `milestone`, `challenge`) is shown in the examples above.

## Common mistakes

| Mistake | Effect | Fix |
|---------|--------|-----|
| `rewardContext.rewardValue` used as a number without conversion | Type mismatch if provider validates the field as numeric | Wrap with `$number(rewardContext.rewardValue)` |
| `challenge.kvpCustom.someKey` returns null | Key not set on the challenge at authoring time | Ensure the key is present in `kvpCustom` on every challenge that uses this definition |
| `task.accumulators.item_list[-1]` is null | No items were applied before reward issued (non-purchase event) | Guard with a conditional or use `timestamp` from context instead |
| `milestone` accessed when source is `"task"` or `"challenge"` | `milestone` is null; expression throws or produces null fields | Check `rewardContext.source` before accessing `milestone`, or only use `milestone` in definitions attached to milestone rewards |
| Expression returns an array instead of an object | Provider receives unexpected payload structure | Wrap array-returning expressions in an outer object: `{ "items": [...] }` |

## How-to videos {#video}

➡️ Watch how to set up a loyalty reward provider

>[!VIDEO](https://video.tv.adobe.com/v/3497346?quality=12)
