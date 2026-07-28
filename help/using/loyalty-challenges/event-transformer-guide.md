---
solution: Journey Optimizer
product: journey optimizer
title: Event Transformer guide
description: Learn how to configure schema and transformer settings for Loyalty Challenges event definitions in Adobe Journey Optimizer.
feature: Journeys
topic: Content Management
role: Admin
level: Intermediate
mini-toc-levels: 1
exl-id: d3ad85f0-7f7e-40ab-b8c4-fc0c1234be87
feature_v2: []
subfeature_v2: []
---
# Event Transformer guide {#event-transformer-guide}

>[!CONTEXTUALHELP]
>id="ajo_loyalty_event_transformer"
>title="Event Transformer guide"
>abstract="Use this guide to configure schema validation and transformer expressions for Loyalty Challenges event definitions."

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
* [Reward Definition guide](reward-definition-guide.md)
* **Event Transformer guide** ◀︎ **You are here**
* [Loyalty data and datasets](loyalty-data-and-datasets.md)
* [Loyalty Challenges API reference](https://developer.adobe.com/journey-optimizer-apis/references/loyalty-challenges){target="_blank"}

</td>
</tr>
</table>

>[!ENDSHADEBOX]

Before a customer transaction can be applied to a loyalty challenge, it must be in the **Adobe Loyalty Event** format that the Challenge Service understands. Customer events — from a POS system, a mobile app, an e-commerce platform, or any other source — typically use the customer's own data schema. **Event Transformers** bridge this gap without requiring any changes to the upstream system.

## Overview

An **Event Definition** tells the platform two things:

* **Which events to claim** — how to recognize that an incoming event belongs to this definition (matching)
* **How to reshape them** — a [JSONata](https://docs.jsonata.org/overview) expression that maps the customer's fields to the Loyalty Event format (transformation)

Multiple event definitions can be configured per org. The platform evaluates them in order and applies the first one that matches. Events that don't match any definition fall through to native ingestion (see [Fallback — Native Loyalty Events](#fallback--native-loyalty-events)).

## The Adobe Loyalty Event Format

Every event definition must produce a JSON object in the following format. This is the input the Challenge Service processes.

```json
{
  "_id":              "string — optional; used for duplicate detection if enabled",
  "event_name":       "string — used for internal metrics and reporting only (e.g. 'purchase', 'visit')",
  "timestamp":        "ISO 8601 date-time string — when the event occurred",
  "utc_offset":       "string — UTC offset of the store or device (e.g. '-07:00'); required for daypart matching",
  "location_id":      "string — optional; store or location identifier",
  "transaction_id":   "string — optional; dedup key for the transaction",
  "loyalty_identity": {
    "id": "string — the member's loyalty ID"
  },
  "item_list": [
    {
      "item_set":   ["string", "..."],  // one or more identifiers — SKU, category, event code, etc.
      "item_name":  "string — optional human-readable label",
      "quantity":   1,                  // integer; how many units
      "unit_price": 4.99,               // float; price per unit
      "sub_total":  4.99                // float; line total (quantity × unit_price)
    }
  ]
}
```

### Field Notes

| Field                          | Required           | Notes |
|--------------------------------|--------------------|-------|
| `loyalty_identity`             | **Yes**            | Must contain `id` — the member's loyalty ID. |
| `item_list`                    | **Yes**            | Must have ≥1 item; empty item_list is rejected. |
| `item_set`                     | **Yes** (per item) | Identifiers task include/exclude lists match against. |
| `timestamp`                    | **Yes**            | Used for date-window evaluation. Must be ISO 8601. |
| `utc_offset`                   | Recommended        | Needed for daypart matching and streak-day counting. |
| `_id`                          | No                 | Used for dedup if org has duplicate detection enabled. |
| `sub_total`                    | No                 | Spend-threshold tasks use this; omit means zero spend. |

## Event Definition Fields

| Field                          | Type             | Required             | Description |
|--------------------------------|------------------|----------------------|-------------|
| `guid`                         | String           | No (system-assigned) | System-assigned unique ID; read-only. |
| `name`                         | String           | **Yes**              | Human-readable label, e.g. `"Starbucks POS Purchase"`. |
| `xdmSchemaId`                  | String           | **Yes**              | Matches events by XDM schema ID (see How Matching Works). |
| `schema`                       | String           | No                   | [JSON Schema](https://json-schema.org/) (as a string) to validate incoming events. |
| `transformer`                  | String           | **Yes**              | JSONata expression mapping the event to Loyalty format. |

## How Matching Works

Events arriving through the Data Collection Core Service (DCCS) carry an XDM schema reference in their envelope. The platform reads the schema ID from `/body/xdmMeta/schemaRef/id` and compares it against each definition's `xdmSchemaId`.

The platform walks the org's event definitions **in order** and applies the first match. Once a match is found, the `xdmEntity` body is passed to the transformer.

## Writing the Transformer

The `transformer` field is a [JSONata](https://docs.jsonata.org/overview) expression. It receives the incoming event JSON as its input and must return a valid Adobe Loyalty Event object.

+++Basic Mapping Pattern

Map each top-level field of the target format to the corresponding path in your source event:

```jsonata
{
  "_id":            sourceEvent._id,
  "event_name":     sourceEvent.eventType,
  "timestamp":      sourceEvent.timestamp,
  "utc_offset":     sourceEvent.storeInfo.utcOffset,
  "location_id":    sourceEvent.storeInfo.storeId,
  "transaction_id": sourceEvent.transaction.id,
  "loyalty_identity": {
    "id": sourceEvent.member.loyaltyId
  },
  "item_list": sourceEvent.transaction.items.{
    "item_set":   [itemSku, itemCategory],
    "item_name":  itemDescription,
    "quantity":   quantity,
    "unit_price": unitPrice,
    "sub_total":  lineTotal
  }
}
```

+++

+++Hardcoding the Event Name

If all events matching this definition represent the same logical activity, hardcode the `event_name`:

```jsonata
{
  "event_name": "in-store-purchase",
  ...
}
```

`event_name` is used for internal metrics and reporting. It is not used as a task filter — task qualification is determined by `item_set` contents, not the event name.

+++

+++Mapping Identity for DCCS/XDM Events

For events arriving via the DCCS route, the member's identity is typically carried in the standard XDM `identityMap` field rather than a custom tenant property. `identityMap` is a map keyed by namespace — the key itself is the namespace name, and the value is an array of identity objects.

```jsonata
"loyalty_identity": {
  "id": identityMap.Email[0].id
}
```

* **Namespace substitution:** Replace `Email` with whatever namespace your org uses for loyalty members — `Loyalty`, `ECID`, `CRMID`, etc. Always read from the namespace that holds the primary loyalty profile identity.

* **Always use `[0]`:** `identityMap.Email` is an array. Without the index, JSONata returns a sequence rather than a single value if more than one identity is present, and `loyalty_identity.id` becomes a list. Pin it to the first element with `[0]`.

* **Avoid custom tenant fields for identity:** Custom field groups sometimes expose an email-looking field (e.g. `_yourtenant.identification.core.email`). In sample data this returns a value and looks correct, but in production events it is frequently empty. The reliable source of identity is always `identityMap`.

+++

+++Building `item_set`

`item_set` is an array of string identifiers. Include every field that your challenge tasks might filter on:

```jsonata
"item_set": [itemSku, productCategory, departmentCode]
```

For non-transactional events (a check-in, a survey completion, a custom trigger), a single identifier is sufficient:

```jsonata
"item_set": [eventName]
```

+++

+++Mapping `unit_price`

`unit_price` should be a per-unit price. Some source schemas store a line total (price × quantity) instead. If your source field is a line total, divide by quantity to get the unit price:

```jsonata
"unit_price": priceTotal / quantity
```

> Only divide if your source field is a line total. If it already stores a per-unit price, map it directly — dividing a unit price by quantity will silently produce a wrong value.

+++

+++Deriving `transaction_id`

If your source event doesn't include a transaction identifier, you can derive a stable one from the timestamp:

```jsonata
"transaction_id": "txn_" & $string($toMillis(timestamp))
```

This converts the ISO timestamp to epoch milliseconds and produces a deterministic value for a given event. Use your platform's own ID generation function if one is available.

+++

+++Using JSONata Functions

The full JSONata function library is available. Useful examples:

```jsonata
/* String concatenation */
"item_set": [skuId & ':' & categoryId]

/* Number formatting */
"item_set": ["spend:" & $formatNumber(totalAmount, '0.00')]

/* Conditional field */
"event_name": eventType ? eventType : "unknown"

/* Array transformation */
"item_list": items.{ "item_set": [sku], "quantity": qty, "sub_total": price * qty }
```

+++

## Examples

+++Example 1 — Simple Custom Event (non-transactional)

**Scenario:** A mobile app sends a check-in event. There are no line items — the event itself is the qualifying activity.

**Incoming Event:**

```json
{
  "_id":       "evt-001",
  "eventName": "store-checkin",
  "timestamp": "2025-10-15T14:22:00Z",
  "storeId":   "STORE-042",
  "member": {
    "loyaltyId": "LM-8827361"
  }
}
```

**Event Definition:**

```json
{
  "name":        "Mobile Store Check-In",
  "xdmSchemaId": "https://ns.adobe.com/yourtenant/schemas/store-checkin-v1",
  "transformer": "{\"_id\": _id, \"event_name\": eventName, \"timestamp\": timestamp, \"location_id\": storeId, \"loyalty_identity\": {\"id\": member.loyaltyId}, \"item_list\": [{\"item_set\": [eventName], \"quantity\": 1}]}"
}
```

**Formatted Transformer (for readability):**

```jsonata
{
  "_id":        _id,
  "event_name": eventName,
  "timestamp":  timestamp,
  "location_id": storeId,
  "loyalty_identity": {
    "id": member.loyaltyId
  },
  "item_list": [
    {
      "item_set": [eventName],
      "quantity": 1
    }
  ]
}
```

**Output Adobe Loyalty Event:**

```json
{
  "_id":        "evt-001",
  "event_name": "store-checkin",
  "timestamp":  "2025-10-15T14:22:00Z",
  "location_id": "STORE-042",
  "loyalty_identity": { "id": "LM-8827361" },
  "item_list": [{ "item_set": ["store-checkin"], "quantity": 1 }]
}
```

A challenge task with no include/exclude restrictions will count this event as a qualifying visit — the single `item_set` entry `["store-checkin"]` matches any task that allows all items.

+++

+++Example 2 — POS Purchase with Line Items

**Scenario:** A point-of-sale system sends a transaction payload. Each line item has a SKU and belongs to a category. Challenge tasks use SKU and category to determine what qualifies.

**Incoming Event:**

```json
{
  "_id":       "txn-20251015-4492",
  "timestamp": "2025-10-15T14:35:00Z",
  "storeInfo": {
    "storeId":   "STORE-042",
    "utcOffset": "-07:00"
  },
  "transaction": {
    "transactionId": "4492",
    "items": [
      { "sku": "COFFEE-001", "category": "BEVERAGE", "qty": 2, "unitPrice": 4.50, "lineTotal": 9.00 },
      { "sku": "MUFFIN-007", "category": "FOOD",     "qty": 1, "unitPrice": 3.25, "lineTotal": 3.25 }
    ]
  },
  "member": {
    "loyaltyId": "LM-8827361"
  }
}
```

**Event Definition:**

```json
{
  "name":        "Retail POS Purchase",
  "xdmSchemaId": "https://ns.adobe.com/yourtenant/schemas/retail-pos-purchase-v1",
  "transformer": "{\"_id\": _id, \"event_name\": \"purchase\", \"timestamp\": timestamp, \"utc_offset\": storeInfo.utcOffset, \"location_id\": storeInfo.storeId, \"transaction_id\": transaction.transactionId, \"loyalty_identity\": {\"id\": member.loyaltyId}, \"item_list\": transaction.items.{\"item_set\": [sku, category], \"quantity\": qty, \"unit_price\": unitPrice, \"sub_total\": lineTotal}}"
}
```

**Formatted Transformer:**

```jsonata
{
  "_id":            _id,
  "event_name":     "purchase",
  "timestamp":      timestamp,
  "utc_offset":     storeInfo.utcOffset,
  "location_id":    storeInfo.storeId,
  "transaction_id": transaction.transactionId,
  "loyalty_identity": {
    "id": member.loyaltyId
  },
  "item_list": transaction.items.{
    "item_set":   [sku, category],
    "quantity":   qty,
    "unit_price": unitPrice,
    "sub_total":  lineTotal
  }
}
```

**Output Adobe Loyalty Event:**

```json
{
  "_id":            "txn-20251015-4492",
  "event_name":     "purchase",
  "timestamp":      "2025-10-15T14:35:00Z",
  "utc_offset":     "-07:00",
  "location_id":    "STORE-042",
  "transaction_id": "4492",
  "loyalty_identity": { "id": "LM-8827361" },
  "item_list": [
    { "item_set": ["COFFEE-001", "BEVERAGE"], "quantity": 2, "unit_price": 4.50, "sub_total": 9.00 },
    { "item_set": ["MUFFIN-007", "FOOD"],     "quantity": 1, "unit_price": 3.25, "sub_total": 3.25 }
  ]
}
```

A challenge task with `include: ["BEVERAGE"]` would see the coffee line item qualify (its `item_set` contains `"BEVERAGE"`) and accumulate $9.00 of spend toward that task. The muffin line item would be excluded.

+++

+++Example 3 — AEP Experience Event (XDM Schema Matching)

**Scenario:** Events flow through Adobe Journey Optimizer. The incoming event is an XDM Experience Event with a known schema ID. The platform uses the schema ID for matching rather than a path/value check.

**Incoming XDM Entity Body** (the `xdmEntity` extracted from the AJO event):

```json
{
  "_brandname": {
    "identities": {
      "loyaltyId": "LM-8827361"
    },
    "transactions": {
      "transactionId": "TXN-9901",
      "storeNumber":   "042",
      "utcOffset":     "-07:00",
      "lineItems": [
        { "skuNumber": "11143053", "priceAmount": 345, "qty": 1, "category": "BEVERAGE" },
        { "skuNumber": "11161387", "priceAmount": 495, "qty": 1, "category": "FOOD" }
      ],
      "totalAmount": 840
    }
  },
  "_id":       "87c0cccf-5809-38e0-a703-3994e80173ab",
  "timestamp": "2025-07-04T16:03:32.000Z"
}
```

**Event Definition:**

```json
{
  "name":        "AJO Brand Purchase",
  "xdmSchemaId": "https://ns.adobe.com/brandname/schemas/purchase-event-v1",
  "transformer":  "{\"_id\": _id, \"event_name\": \"purchase\", \"timestamp\": timestamp, \"utc_offset\": _brandname.transactions.utcOffset, \"location_id\": _brandname.transactions.storeNumber, \"transaction_id\": _brandname.transactions.transactionId, \"loyalty_identity\": {\"id\": _brandname.identities.loyaltyId}, \"item_list\": _brandname.transactions.lineItems.{\"item_set\": [skuNumber, category], \"quantity\": qty, \"unit_price\": priceAmount, \"sub_total\": priceAmount * qty}}"
}
```

**Formatted Transformer:**

```jsonata
{
  "_id":            _id,
  "event_name":     "purchase",
  "timestamp":      timestamp,
  "utc_offset":     _brandname.transactions.utcOffset,
  "location_id":    _brandname.transactions.storeNumber,
  "transaction_id": _brandname.transactions.transactionId,
  "loyalty_identity": {
    "id": _brandname.identities.loyaltyId
  },
  "item_list": _brandname.transactions.lineItems.{
    "item_set":   [skuNumber, category],
    "quantity":   qty,
    "unit_price": priceAmount,
    "sub_total":  priceAmount * qty
  }
}
```

> **Note:** When an event matches by XDM schema ID, the transformer receives only the `xdmEntity` portion of the event — not the outer AJO envelope. All paths in your transformer expression are relative to the XDM entity body.

+++

## Adding JSON Schema Validation (Optional)

If you want the platform to validate the structure of incoming events before attempting transformation, set the `schema` field to a [JSON Schema](https://json-schema.org/draft-04) document encoded as a JSON string.

Events that fail schema validation are rejected before transformation runs. The error response includes the specific validation failure, making it easy to diagnose malformed upstream events.

+++Example Schema (for Example 2 above)

```json
{
  "$schema": "http://json-schema.org/draft-04/schema#",
  "type": "object",
  "required": ["_id", "timestamp", "transaction", "member"],
  "properties": {
    "_id":       { "type": "string" },
    "timestamp": { "type": "string", "format": "date-time" },
    "member": {
      "type": "object",
      "required": ["loyaltyId"],
      "properties": {
        "loyaltyId": { "type": "string" }
      }
    },
    "transaction": {
      "type": "object",
      "required": ["items"],
      "properties": {
        "transactionId": { "type": "string" },
        "items": {
          "type": "array",
          "items": {
            "type": "object",
            "required": ["sku", "qty", "lineTotal"],
            "properties": {
              "sku":       { "type": "string" },
              "category":  { "type": "string" },
              "qty":       { "type": "number" },
              "unitPrice": { "type": "number" },
              "lineTotal": { "type": "number" }
            }
          }
        }
      }
    }
  }
}
```

+++

Pass this schema as a minified JSON string in the `schema` field of the event definition.

## Fallback — Native Loyalty Events

If no event definition matches an incoming event, the platform attempts to ingest it directly as a native Adobe Loyalty Event. If the payload already conforms to the Loyalty Event format described above, no transformer is needed and the event is applied as-is. This allows customers who have pre-formatted their events to bypass transformation entirely.

## API Reference

All event definition operations use the base path `/loyalty/metadata/config/events`.

+++Create an Event Definition

```http
POST /loyalty/metadata/config/events
x-gw-ims-org-id: {ORG_ID}
x-sandbox-name: {SANDBOX}
Content-Type: application/json

{
  "name":        "Retail POS Purchase",
  "xdmSchemaId": "https://ns.adobe.com/yourtenant/schemas/retail-pos-purchase-v1",
  "transformer": "{ ... }"
}
```

+++

+++List Event Definitions

```http
GET /loyalty/metadata/config/events
x-gw-ims-org-id: {ORG_ID}
x-sandbox-name: {SANDBOX}
```

+++

+++Update an Event Definition

```http
PUT /loyalty/metadata/config/events/{eventId}
x-gw-ims-org-id: {ORG_ID}
x-sandbox-name: {SANDBOX}
Content-Type: application/json

{
  "name":        "Retail POS Purchase (v2)",
  "transformer": "{ ... updated expression ... }"
}
```

+++

+++Delete an Event Definition

```http
DELETE /loyalty/metadata/config/events/{eventId}
x-gw-ims-org-id: {ORG_ID}
x-sandbox-name: {SANDBOX}
```

+++

## Transformer Validation

JSONata expressions are validated for syntax when the event definition is saved. If the expression is invalid, the API returns a `422` error with a description of the parse failure.

To test a transformer before deploying, use the [JSONata Exerciser](https://try.jsonata.org/) — paste your source event as the input and your transformer expression to verify the output matches the expected Loyalty Event format.

## Common Pitfalls

These mistakes all run without error on a simple single-item test payload, which is exactly why they slip through undetected. Always test your transformer against a payload with two or more products before deploying.

+++Building one object instead of mapping over the array

The most frequent mistake. Using a single object literal with `productListItems.SKU` pulls every SKU and every quantity into lumped sequences rather than producing one line item per product.

**✗ Collapses all items into one:**

```jsonata
"item_list": [
  {
    "item_set": [ productListItems.SKU ],
    "quantity": productListItems.quantity
  }
]
```

With two products, `item_set` holds both SKUs and `quantity` becomes an array like `[1, 4]`.

**✓ One line item per product:**

```jsonata
"item_list": [
  productListItems.{
    "item_set": [SKU],
    "quantity": quantity
  }
]
```

The `.{ }` map runs once per product so each becomes its own entry.

+++

+++Forgetting the array index on the identity

`identityMap.Email` is an array. Without `[0]`, if a profile has more than one identity in that namespace, `id` becomes a list of values instead of a single string.

**✗** `identityMap.Email.id`

**✓** `identityMap.Email[0].id`

+++

+++Sourcing identity from a custom tenant field

Custom field groups sometimes expose an email-looking field such as `_yourtenant.identification.core.email`. In sample data it returns a value and looks correct, but in production events it is frequently empty, causing `loyalty_identity.id` to come out null. Always use `identityMap` as the source of identity.

+++

+++A nested array leaking into `item_set`

Adding a category field to `item_set` looks straightforward, but if `productCategories` is itself an array the result expands unpredictably.

**✗ May produce more entries than expected:**

```jsonata
"item_set": [SKU, productCategories.categoryID]
```

A product with three categories produces an `item_set` with four values.

**✓ Index the nested array to get exactly one value:**

```jsonata
"item_set": [SKU, productCategories[0].categoryID]
```

+++

+++`item_list` is empty or missing

An event with an empty or absent `item_list` is rejected as invalid. For non-transactional events (check-ins, custom triggers) there are no natural line items, so produce a synthetic one:

```jsonata
"item_list": [{ "item_set": [eventName], "quantity": 1 }]
```

+++

+++`timestamp` as a Unix epoch integer instead of ISO 8601

The platform expects an ISO 8601 string. If your source event carries milliseconds since epoch, convert it:

```jsonata
"timestamp": $fromMillis(timestamp)
```

+++

+++`utc_offset` omitted

Without `utc_offset`, daypart window matching and consecutive-day streak counting are both skipped. Map the store or device UTC offset from your source event wherever it is available.

+++

+++Transformer paths relative to the AJO envelope on a DCCS event

For DCCS events, the transformer receives only the `xdmEntity` body — not the outer AJO envelope. All paths must be relative to the XDM entity root. If your expression references fields that live in the outer envelope (e.g. `/body/xdmMeta/...`) they will not be found and will silently produce null.

+++

