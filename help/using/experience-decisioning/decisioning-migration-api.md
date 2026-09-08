---
title: Decisioning Migration API
description: Learn how to use the Decisioning Migration Service API to migrate Decision management objects between sandboxes with automated dependency resolution and rollback support.
feature: Decisioning
topic: Integrations
role: Developer
level: Experienced
exl-id: 3ec084ca-af9e-4b5e-b66f-ec390328a9d6
feature_v2:
  - id: a4cb03e1-327e-499d-9de8-e0c0db8a63a2
    internal-label: Decisioning
subfeature_v2:
  - id: a7a194a0-75e2-4913-8a83-14714fbf68e6
    internal-label: Decisioning API
  - id: eb547372-2a95-4d13-b0fd-f720c9895880
    internal-label: Edge Decisioning
---
# Decisioning Migration API {#decisioning-migration-api}

>[!BEGINSHADEBOX]

**On this page:** Use the Decisioning Migration Service API to move Decision management objects between sandboxes with automated dependency analysis and rollback support, so you can transition decisioning content across environments while preserving data integrity.

>[!ENDSHADEBOX]

The Decisioning Migration Service API enables you to migrate Decision management objects from one sandbox to another. The migration process runs as asynchronous workflows that include dependency analysis, execution, and optional rollback capabilities.

This API allows you to seamlessly transition your decisioning content between environments <!--(e.g., from development to staging, or staging to production) -->while maintaining data integrity and relationships.

To learn about the benefits and capabilities of Decisioning compared to Decision management, refer to [this page](migrate-to-decisioning.md).

## Capabilities {#capabilities}

The Decisioning Migration Service API provides the following capabilities:

* **Dependency analysis** - Identify all required dependencies between source and target sandboxes, including attributes, segments, and dataset requirements.
* **Flexible migration scope** - Run migrations at sandbox, offer, or decision level based on your needs.
* **Rollback support** - Revert a completed migration if issues are discovered during validation.

## Prerequisites {#prerequisites}

### Required permissions {#permissions}

To use the Migration API, you need appropriate permissions in both the source and target sandboxes:

**Source sandbox** - Read access to Decision management objects

**Target sandbox** - Create and edit access to Decisioning objects

Typical permissions include:

* Manage / View Decisioning
* Manage / View Decisions
* Manage Offers
* Manage Ranking Strategies
* Manage Campaigns (if migrating campaign-related artifacts)
* Manage / View Datastreams (if creating a datastream)
* Manage / View Schemas

>[!NOTE]
>
>Learn how to assign Decisioning permissions in [this section](gs-experience-decisioning.md#steps). For the full list of permissions, refer to the [Built-in permissions](../administration/ootb-permissions.md#ootb-permissions) page.

### Prepare your target sandbox {#target-sandbox-preparation}

Before running a migration, ensure your target sandbox is properly configured:

* **Attributes** - Verify that required profile attributes and context attributes exist in the target sandbox, or prepare mappings for them.
* **Segments** - Ensure required segments exist in the target sandbox, or plan to map them using namespace and ID.
* **Dataset** - Identify a dataset name to use for the migration (`dependency.datasetName`).
* **Datastream** - Decide whether the migration should create a datastream (`createDataStream`).

For more information about sandbox management, refer to [Use and assign sandboxes](../administration/sandboxes.md).

>[!NOTE]
>
>The target sandbox can be the same as the source sandbox. The migration process handles this scenario and ensures data integrity regardless of whether objects are migrated within the same sandbox or to a different one.

### Cross-Sandbox Migration Prerequisites {#cross-sandbox-prerequisites}

When source sandbox ≠ target sandbox, the following items are required:

* **Profile Attributes** - Must exist in target sandbox or have pre-defined mappings
* **Segment IDs** - Must be pre-created in target sandbox with old→new ID mappings  
* **Identity Mapping** - Must be configured for consistent identity resolution

## API basics {#api-basics}

### Base URL {#base-url}

Use the following base URL:

* **Production**: `https://decisioning-migration.adobe.io`

### Authentication {#authentication}

All API requests require the following headers:

* `Authorization: Bearer <IMS_ACCESS_TOKEN>`
* `x-gw-ims-org-id: <IMS_ORG_ID>`
* `Content-Type: application/json`

For detailed instructions on setting up authentication, refer to the [Journey Optimizer authentication guide](https://developer.adobe.com/journey-optimizer-apis/references/authentication){target="_blank"}.

## Migration workflow {#migration-workflow}

The migration process consists of two main steps: analyzing dependencies and executing the migration. Follow these steps to ensure a successful migration.

### Step 1: Analyze dependencies {#analyze-dependencies}

Before migrating, use the dependency workflow to identify what needs to be mapped from Decision management to Decisioning in your target sandbox. This analysis helps you understand the relationships between objects and prepare the necessary mappings.

#### Create a dependency workflow {#create-dependency-workflow}

Use the following API call to create a dependency analysis workflow.

**API format**

```http
POST /workflows/generate-dependencies
```

**Sandbox-level dependency (recommended first)**

Start with a sandbox-level analysis to get a complete view of all dependencies:

```shell
curl --request POST \
  --url "https://decisioning-migration.adobe.io/workflows/generate-dependencies?request-level=sandbox" \
  --header "Authorization: Bearer <IMS_ACCESS_TOKEN>" \
  --header "x-gw-ims-org-id: <IMS_ORG_ID>" \
  --header "Content-Type: application/json" \
  --data '{
    "imsOrgId": "<IMS_ORG_ID>",
    "sourceSandboxDetails": { "sandboxName": "<SOURCE_SANDBOX_NAME>" },
    "targetSandboxDetails": { "sandboxName": "<TARGET_SANDBOX_NAME>" }
  }'
```

**Offer-level dependency**

To analyze dependencies for specific offers only, call the same endpoint with `request-level=offer` in the query string and provide an `offersList` array in the body with the offer IDs you want to analyze.

**Decision-level dependency**

To analyze dependencies for specific decisions only, use `request-level=decision` in the query string and provide a `decisionsList` array in the body with the decision IDs you want to analyze.

#### Check dependency workflow status {#poll-dependency-status}

Poll the dependency workflow to check when the analysis is complete.

**API format**

```http
GET /workflows/generate-dependencies/{id}
```

**Request**

```shell
curl --request GET \
  --url "https://decisioning-migration.adobe.io/workflows/generate-dependencies/<WORKFLOW_ID>" \
  --header "Authorization: Bearer <IMS_ACCESS_TOKEN>" \
  --header "x-gw-ims-org-id: <IMS_ORG_ID>"
```

When the `status` field shows `Completed`, the dependency analysis is ready. Use the workflow output to build your migration dependency mappings:

* **profileAttributes** - Maps source profile attributes to target profile attributes
* **contextAttributes** - Maps source context attributes to target context attributes
* **segments** - Maps each source segment key to a target segment identifier (`{namespace, id}`)
* **datasetName** - The target Experience Event dataset used for the migration. It must be attached to a datastream that is enabled for Journey Optimizer Edge (Web SDK) calls; its schema is used to add the migrated context attributes.

You supply these mappings in the `dependency` object of the migration request in Step 2.

### Step 2: Execute the migration {#execute-migration}

Once you have analyzed the dependencies and prepared your mappings, you can execute the migration.

#### Create a migration workflow {#create-migration-workflow}

Use the dependency mappings from Step 1 to configure and execute your migration.

**API format**

```http
POST /workflows/migration
```

**Sandbox-level migration**

To migrate all decisioning objects from one sandbox to another:

```shell
curl --request POST \
  --url 'https://decisioning-migration.adobe.io/workflows/migration?request-level=sandbox' \
  --header 'Authorization: Bearer <IMS_ACCESS_TOKEN>' \
  --header 'Content-Type: application/json' \
  --header 'x-gw-ims-org-id: <IMS_ORG_ID>' \
  --data '{
    "imsOrgId": "<IMS_ORG_ID>",
    "sourceSandboxDetails": { "sandboxName": "<SOURCE_SANDBOX_NAME>" },
    "targetSandboxDetails": { "sandboxName": "<TARGET_SANDBOX_NAME>" },
    "createDataStream": true,
    "dependency": {
      "profileAttributes": {
        "sourceAttr1": "targetAttr1"
      },
      "segments": {
        "sourceSegmentKey1": {
          "namespace": "<TARGET_SEGMENT_NAMESPACE>",
          "id": "<TARGET_SEGMENT_ID>"
        }
      },
      "contextAttributes": {
        "sourceCtx1": "targetCtx1"
      },
      "datasetName": "<TARGET_DATASET_NAME>"
    }
  }'
```

**Offer-level migration**

To migrate specific offers only, use `request-level=offer` in the query string and add an `offersList` array to the body:

```json
"offersList": ["offer-id-1", "offer-id-2"]
```
 
**Decision-level migration**

To migrate specific decisions only, use `request-level=decision` in the query string and add a `decisionsList` array to the body:

```json
"decisionsList": ["decision-id-1", "decision-id-2"]
```

**Request fields**

* **request-level** (query) - Migration scope: `sandbox`, `offer`, or `decision`.
* **imsOrgId** (required) - Your IMS Org ID.
* **sourceSandboxDetails.sandboxName** (required) - Source sandbox that holds the Decision management entities.
* **targetSandboxDetails.sandboxName** (required) - Target sandbox where the Decisioning entities are created.
* **dependency.datasetName** (required) - Target Experience Event dataset. It must be attached to a datastream enabled for Journey Optimizer Edge (Web SDK) calls; its schema is used to add the migrated context attributes.
* **createDataStream** - `true` creates a new Journey Optimizer-enabled datastream; `false` reuses the one already attached to the dataset in `dependency.datasetName`.
* **dependency.profileAttributes** - Map of source → target profile attributes.
* **dependency.contextAttributes** - Map of source → target context attributes.
* **dependency.segments** - Map of source segment key → target segment (`{namespace, id}`).
* **offersList[]** / **decisionsList[]** - The offer or decision IDs to migrate; required when `request-level` is `offer` or `decision` respectively.

#### Monitor migration status {#poll-migration-status}

Poll the migration workflow to track its progress.

**API format**

```http
GET /workflows/migration/{id}
```

**Request**

```shell
curl --request GET \
  --url "https://decisioning-migration.adobe.io/workflows/migration/<WORKFLOW_ID>" \
  --header "Authorization: Bearer <IMS_ACCESS_TOKEN>" \
  --header "x-gw-ims-org-id: <IMS_ORG_ID>"
```

**Migration results**

When the `status` field shows `Completed`, the migration was successful. The workflow `result` includes:
* Mappings of migrated objects
* Any warnings encountered during migration

When the `status` field shows `Failed`, review the `errors[]` array and `result.error` field for details about what went wrong.

Every workflow (dependency, migration, and rollback) returns the same resource fields:

* **id** - Workflow identifier (UUID); poll its status with the matching `GET /{id}`.
* **status** - Lifecycle state: `New`, `Running`, `Completed`, or `Failed`.
* **result** - Present on `Completed`; the workflow output (for example, mappings of migrated objects and any warnings).
* **errors[]** - Present on `Failed`; structured error details (see also `result.error`).
* **_links.self** - URL of the workflow resource.

## Validate your migration {#validate-migration}

After the migration completes successfully, verify that all objects were migrated correctly.

### Validation checklist {#validation-checklist}

1. **Segments** - Verify that all referenced segments resolve correctly in the target sandbox according to your mappings.
2. **Attributes** - Confirm that all profile attributes and context attributes exist in the target sandbox and are mapped correctly.
3. **Decisioning objects** - Review migrated objects in the Journey Optimizer user interface:
   * Offers (decision items)
   * Eligibility rules
   * Ranking formulas
   * Selection strategies
   * Decision policies
4. **Datastream testing** - If a datastream was created, test runtime delivery using the Edge Interact API.

### Example {#test-runtime-delivery}

If your migration created a datastream, you can test offer delivery using the following example:

```shell
curl --request POST \
  --url "https://edge.adobedc.net/ee/or2/v1/interact?configId=<DATASTREAM_ID>" \
  --header "Content-Type: application/json" \
  --header "x-request-id: <uuid>" \
  --data '{ "events": [ ... ] }'
```

## Rollback a migration {#rollback}

If you discover issues during validation, you can roll back a completed migration to restore the target sandbox to its previous state.

### Create a rollback workflow {#create-rollback-workflow}

Initiate a rollback by creating a rollback workflow that references the migration you want to revert.

**API format**

```http
POST /workflows/rollback
```

**Request**

```shell
curl --request POST \
  --url "https://decisioning-migration.adobe.io/workflows/rollback" \
  --header "Authorization: Bearer <IMS_ACCESS_TOKEN>" \
  --header "x-gw-ims-org-id: <IMS_ORG_ID>" \
  --header "Content-Type: application/json" \
  --data '{ "rollbackWorkflowId": "<MIGRATION_WORKFLOW_ID>" }'
```

Replace `<MIGRATION_WORKFLOW_ID>` with the ID of the migration workflow you want to roll back.

### Monitor rollback status {#poll-rollback-status}

Poll the rollback workflow to track its progress.

**API format**

```http
GET /workflows/rollback/{rollbackWorkflowId}
```

**Request**

```shell
curl --request GET \
  --url "https://decisioning-migration.adobe.io/workflows/rollback/<ROLLBACK_WORKFLOW_ID>" \
  --header "Authorization: Bearer <IMS_ACCESS_TOKEN>" \
  --header "x-gw-ims-org-id: <IMS_ORG_ID>"
```

## Handle concurrent workflows {#handle-concurrency}

The Migration API allows only one workflow to run at a time per organization. If you attempt to create a new workflow while another is in progress, you will receive a **409 Conflict** error response ("A workflow is already in progress...").

In this case, wait for the in-progress workflow to complete, or retrieve the workflow ID and poll its status. Once the current workflow finishes, you can create a new one.

## Migration scope and coverage {#migration-scope}

Understanding the scope of the migration helps you plan and validate your transition from Decision management to Decisioning. This section outlines what is covered by the migration process and what requires manual action.

### In-Scope: What is covered {#in-scope}

The Migration API handles the following items and capabilities:

* **Use cases** - Only inbound/Edge decisioning use cases are in scope. Outbound or OD in Journey Optimizer Email channel migration are supported but require manual updates.
* **Code-Based Experience Campaigns** - Automatically created during migration, one Campaign per migrated decision scope in your target sandbox.
* **Channel Configuration/Surface** - Channel configurations/surfaces created per Decision management placement, ensuring proper routing of decisioning responses.
* **Offer content types** - Offers are migrated only if their content type is JSON or Text. Other content types require manual recreation.
* **Offer characteristics** - Preserved in the `offer_item_custom_attributes` field group on the "Personalized Offer Items – Experience Decisioning" schema, maintaining custom metadata.
* **Context attributes** - Added to the Experience Event schema in the `custom_context_attributes` field group for tracking and personalization.
* **Decision scopes** - One Decision management Decision Scope maps to one Selection Strategy + one Decision Policy + one Campaign in Decisioning, ensuring proper entity hierarchy.
* **API-only eligibility rules** - Eligibility rules created via API only (not in Decision management UI) are migrated and remain API-only in Decisioning. UI-created rules are also migrated.

### Out-of-Scope: What is not covered or requires manual action {#out-of-scope}

The following items require manual action or are not supported by the migration tooling:

* **Decisioning Placements** - No Placements are created by the migration tooling. You must create these manually in Decisioning before or after migration based on your architecture.
* **Placement-level capping** - Placement-level frequency capping is not migrated.
* **Non-JSON/Text offer content** - Offers with content types other than JSON or Text (e.g., HTML, images) are NOT migrated and require manual recreation in Decisioning.
* **Profile attributes and segments** - Profile attributes and segment memberships are NEVER created or edited by migration tooling. These must already exist in your target sandbox before running the migration.
* **Segment ID mapping** - Segment IDs must be pre-created in the target sandbox. You must supply an old→new ID mapping in the Migration API request for segment resolution.
* **Data collection code changes** - Client-side and server-side event tracking code changes are NOT automated. Your implementation team must update event collection to use Decisioning request/response formats and decisioning event schemas.

## Entity mapping reference {#entity-mapping}

When migrating from Decision management to Decisioning, entities are mapped according to the following table. The mappings include the primary Decisioning entities and additional associated entities created or used during migration.

### Decision management to Decisioning Entity Mapping

| Decision management Entity | Decisioning Entity | Additional Entities |
|-----------|--------------|-------------------|
| Decision | Selection Strategy | Item Collection, Eligibility Rule, Ranking Formula |
| | Decision Policy | Item Count, Selection Strategies, Fallback Offer Item |
| | Code Based Experience Campaign | Decision Policy, Content, Channel Configuration, Journey Optimizer Fragments |
| Placement | Channel Configuration | — |
| Collection | Item Collection | Unified Tags, Offer Items |
| Collection Qualifier | Unified Tags | — |
| Rule | Decisioning Rule | — |
| Ranking Formula | Decisioning Ranking Formula | — |
| Offer | Offer Item | Eligibility Rule, Journey Optimizer Fragments, Unified Tags, Frequency Capping |
| | Offer Item Schema | — |
| | Journey Optimizer Fragments | — |

### Naming Conventions

The migration process applies naming conventions using the `ExD_` prefix to ensure consistency and prevent naming conflicts.

| Source Object | Decision management Name Pattern | Decisioning Name Pattern |
|---------------|-----------------|-------------------|
| Offer | `<offerName>` | `ExD_<offerName>` |
| Eligibility Rule | `<ruleName>` | `ExD_<ruleName>` |
| Ranking Formula | `<formulaName>` | `ExD_<formulaName>` |
| Collection | `<collectionName>` | `ExD_<collectionName>_<placementName>` |
| Decision → Selection Strategy | `<decisionName>` | `ExD_<decisionName>_selection_strategy_<index>` |
| Decision → Decision Policy | `<decisionName>` | `ExD_<decisionName>_<placementName>` |
| Journey Optimizer Fragment | `<offerName>` | `ExD_<offerName>_<placementName>_<index>` |
| Placement → Surface | `<placementName>` | `ExD_<placementName>` *(spaces/dots converted to underscores)* |
| Unified Tag | `<sourceName>, <targetName>` | `ExDMigration_<sourceName>_<targetName>` |
| CBE Campaign | `<decisionName>, <placementName>` | `Campaign for <decisionName> : <placementName>` |

### Additional Attributes

| Source Attribute | Target Location |
|-----------------|-----------------|
| Offer attributes | "migratedofferattributes" field in the Personalized offer item schema |
| Context attributes | "migratedcontextattributes" field in the schema attached to the dataset provided during migration |

## Request and response model {#request-response-model}

When migrating from Decision management to Decisioning, your application code must be updated to use the new request and response formats. Both systems use the Edge Network endpoint, but with different payload structures and field names.

### Decision management Edge Request (Current) {#dm-request}

The current Decision management Edge request follows this structure:

**Endpoint:**

```
POST https://edge.adobedc.net/ee/v2/interact
```

**Headers:**
- `Authorization: Bearer <IMS_ACCESS_TOKEN>`
- `x-api-key: <API_KEY>` (from Developer Console)
- `x-gw-ims-org-id: <IMS_ORG_ID>` (format: `{ORG_ID}@AdobeOrg`)
- `x-request-id: <UNIQUE_REQUEST_ID>` (for tracing and deduplication)
- `Content-Type: application/vnd.adobe.xdm+json; schema="…/decision-request;version=1.0"`
- `Accept: application/vnd.adobe.xdm+json; schema="…/decision-response;version=1.0"`
- `x-sandbox-name: <SANDBOX_NAME>` (e.g., prod, dev)

**Request Body Parameters:**
- `xdm:dryRun` (true/false) - Test requests without polluting reporting
- `xdm:propositionRequests[]` - Array of decision requests:
  - `activityId` - Decision activity identifier
  - `placementId` - Placement identifier
  - `itemCount` - Maximum number of offers to return
- `xdm:profiles[].xdm:identityMap` - Identity mapping (email, ECID, etc.)
- `xdm:validateContextData` - Strict context data validation flag
- `xdm:responseFormat.xdm:includeContent` - Include actual content vs. IDs only

**Example request body:**

```json
{
  "xdm": {
    "dryRun": false,
    "propositionRequests": [
      { "activityId": "<ACTIVITY_ID>", "placementId": "<PLACEMENT_ID>", "itemCount": 3 }
    ],
    "profiles": [
      { "identityMap": { "ECID": [ { "id": "<ECID>", "primary": true } ] } }
    ],
    "validateContextData": true,
    "responseFormat": { "includeContent": true }
  }
}
```

>[!NOTE]
>For the full Decision management (OD) request/response reference, see [Edge Decisioning API](https://experienceleague.adobe.com/en/docs/journey-optimizer/using/decisioning/offer-decisioning/api-reference/offer-delivery-api/edge-decisioning-api) (the Web SDK / Edge variant, which uses base64-encoded `decisionScopes` carrying `activityId` and `placementId`).

### Decisioning Edge Request (After Migration) {#decisioning-request}

After migration, use the Decisioning request format via the same Edge Network endpoint.

**Endpoint:**

```
POST https://edge.adobedc.net/ee/v2/interact
```

**Key Request Fields:**
- `query.identity.fetch` - Array of identity types to resolve (e.g., `["ECID"]`)
- `event.xdm.environment.type` - Environment type: `"browser"`, `"app"`, or `"server"`
- `event.xdm.environment.browserDetails` - Browser metadata (`viewportWidth`, `viewportHeight`, `userAgent`)
- `event.xdm.identityMap` - Same identity mapping as Decision management
- `event.xdm.timestamp` - ISO 8601 timestamp
- `query.personalization.surfaces` - Array of target surfaces (e.g., `["web://site.com/homepage"]`) — replaces `decisionScope`
- `query.personalization.schemas` - Content schemas to return (e.g., `["json-content-item", "html-content-item"]`)
- `data.__adobe.ajo.allowDuplicateDecisionItems` - Deduplication control (defaults to `true`; set `false` so an item that qualifies for multiple surfaces is returned only once, with the other surfaces receiving a fallback/empty item). Replaces the Decision management `allowDuplicatePropositions`.
- `data.__adobe.ajo.dryRun` - Test flag; suppresses feedback events for both reporting and capping counters. Replaces the Decision management `xdm:dryRun`. Remove before production.

**Example request body (server-side):**

```json
{
  "events": [
    {
      "query": {
        "identity": { "fetch": ["ECID"] },
        "personalization": {
          "surfaces": ["web://my-web/IP_NLI_HP_GET_LOAN_WIDGET"],
          "schemas": [
            "https://ns.adobe.com/personalization/json-content-item",
            "https://ns.adobe.com/personalization/html-content-item"
          ]
        }
      },
      "xdm": {
        "eventType": "decisioning.propositionFetch",
        "environment": {
          "type": "browser",
          "browserDetails": { "viewportWidth": 1280, "viewportHeight": 900, "userAgent": "<USER_AGENT>" }
        },
        "identityMap": {
          "ECID": [ { "id": "<ECID>", "authenticatedState": "ambiguous", "primary": true } ]
        },
        "timestamp": "2025-09-08T12:00:00.000Z"
      },
      "data": {
        "__adobe": { "ajo": { "allowDuplicateDecisionItems": false } }
      }
    }
  ],
  "meta": {
    "state": {
      "domain": "my-web",
      "cookiesEnabled": true,
      "entries": [
        { "key": "kndctr_<ORG>_AdobeOrg_identity", "value": "<identity-cookie>" },
        { "key": "kndctr_<ORG>_AdobeOrg_cluster", "value": "<cluster-cookie>" }
      ]
    }
  }
}
```

>[!NOTE]
>For the full Journey Optimizer Decisioning Web SDK / Edge reference, see [Code-based experience: Decisioning implementations](https://experienceleague.adobe.com/en/docs/journey-optimizer/using/channels/code-based-experience/configure-code-based-channel/code-based-decisioning-implementations).

### Decisioning Edge Response {#decisioning-response}

The Decisioning response contains multiple handles organized by concern type: `personalization:decisions` (the offers), `locationHint:result`, and `state:store` (the cookies to persist).

**Response Structure:**

```json
{
  "requestId": "<REQUEST_ID>",
  "handle": [
    {
      "type": "personalization:decisions",
      "eventIndex": 0,
      "payload": [
        {
          "id": "103ae599-e6d8-4631-baf3-51dd8c6ed4c1",
          "scope": "web://my-web/IP_NLI_HP_GET_LOAN_WIDGET",
          "scopeDetails": {
            "decisionProvider": "AJO",
            "correlationID": "<CORRELATION_ID>",
            "characteristics": {
              "eventToken": "<base64 message-level event token>",
              "subPropositions": "<base64-encoded array of decision items>"
            },
            "rank": 1,
            "activity": {
              "id": "<campaignId>#<actionId>",
              "priority": 0,
              "matchedSurfaces": ["web://my-web/IP_NLI_HP_GET_LOAN_WIDGET"]
            }
          },
          "items": [
            {
              "id": "36646bab-af1b-44c6-b632-bbfb9c357919",
              "schema": "https://ns.adobe.com/personalization/json-content-item",
              "data": { "content": "{ ...offer JSON... }" }
            }
          ]
        }
      ]
    },
    {
      "type": "locationHint:result",
      "payload": [
        { "scope": "EdgeNetwork", "hint": "ind1", "ttlSeconds": 1800 }
      ]
    },
    {
      "type": "state:store",
      "payload": [
        { "key": "kndctr_<ORG>_AdobeOrg_cluster", "value": "<cluster-cookie>", "maxAge": 1800 },
        { "key": "kndctr_<ORG>_AdobeOrg_identity", "value": "<identity-cookie>", "maxAge": 34128000 }
      ]
    }
  ]
}
```

**Key Response Fields:**
- `handle[].type` - Handle type (`personalization:decisions`, `locationHint:result`, `state:store`)
- `payload[].id` - Unique proposition instance ID — echo back on display/interact events
- `payload[].scope` - Surface URI the proposition was resolved for
- `payload[].scopeDetails.decisionProvider` - Confirms engine is `AJO`
- `payload[].scopeDetails.correlationID` - Links decision instance to serving event
- `payload[].scopeDetails.rank` / `payload[].scopeDetails.activity` - Rank and campaign/action metadata for the proposition
- `payload[].scopeDetails.characteristics.eventToken` - Message-level tracking token
- `payload[].scopeDetails.characteristics.subPropositions` - Base64-encoded **array of the decision items**; each item carries its own per-item `token`. These per-item tokens are what you pass in `propositionAction.tokens` on display/interact events
- `payload[].items[].schema` / `payload[].items[].data.content` - Content schema and actual offer content (JSON/HTML) to render
- `state:store` payload - The identity and cluster cookies to persist and forward on subsequent requests (server-side)

The `characteristics.subPropositions` string base64-decodes to the array of served items, each with its per-item `token`:

```json
[
  {
    "id": "1ae75277-8832-4c23-bbbc-09f01cfe6c8b",
    "scope": "web://my-web/IP_NLI_HP_GET_LOAN_WIDGET",
    "scopeDetails": { "decisionProvider": "EXD", "correlationID": "<CORRELATION_ID>-0", "rank": 1 },
    "items": [
      { "id": "dps:<schema>:1be64ff83a612488", "name": "ExD_Personal Loan Offer", "score": 997.0, "token": "CLaefQnVLcLbCtzEXV3Jeg" },
      { "id": "dps:<schema>:1be6516838e1248c", "name": "ExD_Home Loan Offer",     "score": 995.0, "token": "ALlB5KV1B0e+CpHoahi7Ew" },
      { "id": "dps:<schema>:1be650da3cd06e98", "name": "ExD_Auto Loan Offer",     "score": 994.0, "token": "koJTRQcwFkR92AqbZ88ytQ" },
      { "id": "dps:<schema>:1be65612d5a1248d", "name": "ExD_Fallback Offer",      "itemSelection": { "selectionDetail": { "selectionType": "fallback" } }, "token": "GHo4ow7h6iCzBOhYR1+6jg" }
    ]
  }
]
```

## Implementation patterns {#implementation-patterns}

Decisioning supports three implementation approaches:

### Client-Side Implementation (Web SDK / Mobile SDK) {#client-side}

The Web SDK or Mobile SDK handles all requests and cookie management automatically. The SDK stores and forwards both identity and cluster cookies with each request.

**Cookie handling:** Automatic — Web SDK manages `kndctr_<OrgId>_identity` and `kndctr_<OrgId>_cluster` cookies.

### Server-Side Implementation (Edge Network API) {#server-side}

The application server POSTs directly to Edge Network and must manually manage cookie forwarding. The server extracts browser cookies from incoming requests and forwards them to Edge Network via `meta.state.entries[]`, then returns cookies in the response.

**Cookie handling:** Manual — App server must extract cookies from browser request, forward to Edge Network in request body, and set in response. Cookies must be explicitly forwarded in `meta.state.entries` for identity consistency.

### Hybrid Implementation {#hybrid}

Combines server-side rendering (initial page load) with client-side SDK (subsequent interactions). The server renders initial content via Edge Network, then Web SDK takes over for subsequent personalization requests.

**Cookie handling:** Mixed — Server side requires manual cookie forwarding to Edge Network; client side handled automatically by Web SDK. Ensure identity tokens from server-side rendering are available to client-side SDK for consistent identity resolution.

## Event tracking and data collection {#event-tracking}

To properly attribute decisioning results, enable frequency capping, and power AI-based ranking optimization, you must implement event tracking using the Decisioning event schema.

### Required Event Fields {#event-fields}

Both `eventType` and `_experience.decisioning.propositionEventType` are required. If either is missing, the corresponding display/interact counter will not increment.

* **`eventType`** - Specifies the event category:
  - `decisioning.propositionDisplay` — Impression event (offer shown to user)
  - `decisioning.propositionInteract` — Interaction event (user clicked or engaged with the offer)

* **`_experience.decisioning.propositionEventType`** - Flags the event subtype. Include **exactly one** event-type key set to `1` (each value is `1` or `0`; do not set multiple event types to `1` in the same object):
  - `{ "display": 1 }` — Impression event
  - `{ "interact": 1 }` — Interaction event
  - If all of `display`/`interact`/`dismiss` are `0` — or `eventType` is any value other than `decisioning.proposition<Display|Interact|Dismiss>` — the event is treated as a **custom event**.

* **`_experience.decisioning.propositionAction.tokens[]`** - Per-item token(s) identifying which served item(s) to increment counters for:
  - Copy each item's `token` from the decoded `subPropositions` array — **not** `scopeDetails.characteristics.eventToken`, which is a different, message-level token.
  - Pass the token exactly as received, unmodified.
  - **Interact events:** provide **exactly one** token (the clicked item).
  - **Display events:** optional — provide token(s) to increment specific items, or **omit** `tokens` to increment the counter for **all** items in `subPropositions`.

* **`_experience.decisioning.propositions[]`** - Echo back the served proposition(s), including `id`, `scope`, and the full `scopeDetails` from the response (which carries `characteristics.subPropositions` and requires `decisionProvider`). You do not need to build an explicit `items[]` array.

### Schema Requirements {#schema-requirements}

Associate the Decisioning field group to your event dataset schema before migration:

1. In Experience Platform, open your event dataset schema
2. Add the `Experience Event - Proposition Details` field group
3. Ensure the following fields are mapped:
   - `_experience.decisioning.*` fields
   - `_experience.decisioning.propositionAction.tokens`
   - `_experience.decisioning.propositionEventType`

### Tracking Token Handling {#tracking-token}

The tracking token must be handled according to these requirements:

* **Per-item token drives the counters** — the value(s) in `propositionAction.tokens` are each served item's `token` from `subPropositions`, not the message-level `characteristics.eventToken`.
* **Interact events** — provide exactly one token (the clicked item).
* **Display events** — tokens are optional; omit to increment all items in `subPropositions`, or provide specific tokens to increment only those items.
* **Do not modify the token** — pass the value exactly as received; do not encode, parse, or alter it.

## Decisioning Event Examples {#event-examples}

Each example echoes back the served proposition (including its `scopeDetails`, which carries `characteristics.subPropositions`) and sets both `eventType` and `propositionEventType`. Counters increment against the items in `subPropositions`; `propositionAction.tokens` selects which items.

### Display Events

Display events notify Decisioning when an offer is shown to a user. Provide the token(s) of the shown item(s), or omit `tokens` to increment the display counter for all items in `subPropositions`:

```json
{
  "header": {
    "imsOrgId": "YOUR_ORG_ID",
    "sandboxId": "sandbox-id",
    "sandboxName": "sandbox-name",
    "source": { "name": "ajo-inbound" }
  },
  "body": {
    "xdmEntity": {
      "identityMap": {
        "ECID": [ { "id": "ecid-123", "primary": true } ]
      },
      "eventType": "decisioning.propositionDisplay",
      "_experience": {
        "decisioning": {
          "propositionEventType": { "display": 1 },
          "propositionAction": {
            "id": "b96f842b-5dd9-4c55-9dae-647d96250028",
            "tokens": ["CLaefQnVLcLbCtzEXV3Jeg", "ALlB5KV1B0e+CpHoahi7Ew"]
          },
          "propositions": [
            {
              "id": "103ae599-e6d8-4631-baf3-51dd8c6ed4c1",
              "scope": "web://my-web/IP_NLI_HP_GET_LOAN_WIDGET",
              "scopeDetails": {
                "decisionProvider": "AJO",
                "characteristics": {
                  "eventToken": "<base64 eventToken from response>",
                  "subPropositions": "<base64 subPropositions from response>"
                }
              }
            }
          ]
        }
      }
    }
  }
}
```

### Interact (Click) Events

Interact events track when a user clicks or engages with a displayed offer. You **must** provide **exactly one** token identifying the clicked item:

```json
{
  "header": {
    "imsOrgId": "YOUR_ORG_ID",
    "sandboxId": "sandbox-id",
    "sandboxName": "sandbox-name",
    "source": { "name": "ajo-inbound" }
  },
  "body": {
    "xdmEntity": {
      "identityMap": {
        "ECID": [ { "id": "ecid-123", "primary": true } ]
      },
      "eventType": "decisioning.propositionInteract",
      "_experience": {
        "decisioning": {
          "propositionEventType": { "interact": 1 },
          "propositionAction": {
            "id": "b96f842b-5dd9-4c55-9dae-647d96250028",
            "tokens": ["CLaefQnVLcLbCtzEXV3Jeg"]
          },
          "propositions": [
            {
              "id": "103ae599-e6d8-4631-baf3-51dd8c6ed4c1",
              "scope": "web://my-web/IP_NLI_HP_GET_LOAN_WIDGET",
              "scopeDetails": {
                "decisionProvider": "AJO",
                "characteristics": {
                  "eventToken": "<base64 eventToken from response>",
                  "subPropositions": "<base64 subPropositions from response>"
                }
              }
            }
          ]
        }
      }
    }
  }
}
```

### Custom Events

A custom event uses a customer-defined `eventType` (any value other than `decisioning.proposition<Display|Interact|Dismiss>`) and sets all of `display`/`interact`/`dismiss` to `0` in `propositionEventType` (classified as `OTHER`). Custom events are decoded like display events (multi-token filtering) against `subPropositions`, and are evaluated via the configured PQL:

```json
{
  "header": {
    "imsOrgId": "YOUR_ORG_ID",
    "sandboxId": "sandbox-id",
    "sandboxName": "sandbox-name",
    "originalTimestamp": 1700000
  },
  "body": {
    "xdmEntity": {
      "identityMap": {
        "ECID": [ { "id": "ecid-123", "primary": true } ]
      },
      "eventType": "add-to-cart",
      "_experience": {
        "decisioning": {
          "propositionEventType": { "display": 0, "interact": 0, "dismiss": 0 },
          "propositionAction": {
            "id": "b96f842b-5dd9-4c55-9dae-647d96250028",
            "tokens": ["CLaefQnVLcLbCtzEXV3Jeg"]
          },
          "propositions": [
            {
              "id": "103ae599-e6d8-4631-baf3-51dd8c6ed4c1",
              "scope": "web://my-web/IP_NLI_HP_GET_LOAN_WIDGET",
              "scopeDetails": {
                "decisionProvider": "AJO",
                "characteristics": {
                  "eventToken": "<base64 eventToken from response>",
                  "subPropositions": "<base64 subPropositions from response>"
                }
              }
            }
          ]
        }
      }
    }
  }
}
```

These events enable frequency capping, out-of-the-box reporting, and AI-driven ranking optimization in Decisioning. For sending proposition events with the Web SDK, see [Code-based experience: Decisioning implementations](https://experienceleague.adobe.com/en/docs/journey-optimizer/using/channels/code-based-experience/configure-code-based-channel/code-based-decisioning-implementations).

## End-to-end Migration Process {#migration-process}

1. Validate prerequisites — Ensure your target sandbox is prepared and all prerequisite dependencies are identified and ready before starting the migration (profile attributes, segment IDs, ID mapping).

1. Call the Migration API — Execute the Migration API to migrate Decision management objects to Decisioning using your prepared prerequisites and mappings.

1. Draft Decisioning entities generation — Tooling creates Campaigns, Decision Policies, Selection Strategies, Offer Items, etc. in Draft state per entity mapping. Review all generated Decisioning objects in the target sandbox. Validate naming, entity types, and references are correct. Nothing is customer-facing yet, Decision Management keeps serving live traffic.

1. Update client & server code — Implement required code changes to use the new Decisioning request/response formats and implement event tracking with required fields.

1. Activate & cutover — Activate your Decisioning objects (strategies, policies, campaigns, surfaces) and shift traffic away from Decision Management on your own timeline.

## Related topics {#related-topics}

* [Migrate from Decision management to Decisioning](migrate-to-decisioning.md) - Understand the benefits and capabilities of migrating to Decisioning
* [Get started with Decisioning](gs-experience-decisioning.md)
* [Decisioning guardrails and limitations](decisioning-guardrails.md)
* [Get started with Decisioning APIs](api-reference/getting-started.md)