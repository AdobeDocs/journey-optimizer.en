---
title: Decisioning Migration API
description: Learn how to use the Decisioning Migration Service API to migrate Decision management objects between sandboxes with automated dependency resolution and rollback support.
feature: Decisioning
topic: Integrations
role: Developer
level: Experienced
exl-id: 3ec084ca-af9e-4b5e-b66f-ec390328a9d6
---
# Decisioning Migration API {#decisioning-migration-api}

The Decisioning Migration Service API enables you to migrate Decision management objects from one sandbox to another. The migration process runs as asynchronous workflows that include dependency analysis, execution, and optional rollback capabilities.

This API allows you to seamlessly transition your decisioning content between environments (e.g., from development to staging, or staging to production) while maintaining data integrity and relationships.

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

## API basics {#api-basics}

### Base URLs {#base-urls}

Use the following base URLs depending on your environment:

* **Production**: `https://platform.adobe.io`
* **Staging**: `https://platform-stage.adobe.io`

### Authentication {#authentication}

All API requests require the following headers:

* `Authorization: Bearer <IMS_ACCESS_TOKEN>`
* `x-gw-ims-org-id: <IMS_ORG_ID>`
* `x-api-key: <CLIENT_API_KEY>`
* `Content-Type: application/json`

For detailed instructions on setting up authentication, refer to the [Journey Optimizer authentication guide](https://developer.adobe.com/journey-optimizer-apis/references/authentication/){target="_blank"}.

### Workflow model {#workflow-model}

Each API call creates or retrieves a workflow resource. Workflows are asynchronous operations that track the progress and results of migration tasks.

A workflow has the following properties:

* `id` - Unique workflow identifier (UUID)
* `status` - Current workflow status: `New`, `Running`, `Completed`, `Failed`, or `Cancelled`
* `result` - Workflow output when completed (includes migration results and warnings)
* `errors` - Structured error details when failed
* `_etag` - Version identifier used for delete operations (service users only)
* `_links.self` - Workflow URL for retrieving status

## Migration workflow {#migration-workflow}

The migration process consists of two main steps: analyzing dependencies and executing the migration. Follow these steps to ensure a successful migration.

### Step 1: Analyze dependencies {#analyze-dependencies}

Before migrating, use the dependency workflow to identify what needs to be mapped from Decision management to Decisioning in your target sandbox. This analysis helps you understand the relationships between objects and prepare the necessary mappings.

#### Create a dependency workflow {#create-dependency-workflow}

Use the following API call to create a dependency analysis workflow.

**API format**

```http
POST /migration/service/dependency
```

**Sandbox-level dependency (recommended first)**

Start with a sandbox-level analysis to get a complete view of all dependencies:

```shell
curl --request POST \
  --url "https://platform.adobe.io/migration/service/dependency" \
  --header "Authorization: Bearer <IMS_ACCESS_TOKEN>" \
  --header "x-gw-ims-org-id: <IMS_ORG_ID>" \
  --header "x-api-key: <CLIENT_API_KEY>" \
  --header "Content-Type: application/json" \
  --data '{
    "imsOrgId": "<IMS_ORG_ID>",
    "sourceSandboxDetails": { "sandboxName": "<SOURCE_SANDBOX_NAME>" },
    "targetSandboxDetails": { "sandboxName": "<TARGET_SANDBOX_NAME>" },
    "requestLevel": "sandbox"
  }'
```

**Offer-level dependency**

To analyze dependencies for specific offers only, set `requestLevel: "offer"` and provide an `offersList` array with the offer IDs you want to analyze.

**Decision-level dependency**

To analyze dependencies for specific decisions only, set `requestLevel: "decision"` and provide a `decisionsList` array with the decision IDs you want to analyze.

#### Check dependency workflow status {#poll-dependency-status}

Poll the dependency workflow to check when the analysis is complete.

**API format**

```http
GET /migration/service/dependency/{id}
```

**Request**

```shell
curl --request GET \
  --url "https://platform.adobe.io/migration/service/dependency/<WORKFLOW_ID>" \
  --header "Authorization: Bearer <IMS_ACCESS_TOKEN>" \
  --header "x-gw-ims-org-id: <IMS_ORG_ID>" \
  --header "x-api-key: <CLIENT_API_KEY>"
```

When the `status` field shows `Completed`, the dependency analysis is ready. Use the workflow output to build your migration dependency mappings:

* **profileAttributeDependency** - Maps source profile attributes to target profile attributes
* **contextAttributeDependency** - Maps source context attributes to target context attributes  
* **segmentsDependency** - Maps source segment keys to target segment identifiers (`{segmentNamespace, segmentId}`)
* **datasetName** - Specifies the target dataset name for the migration

### Step 2: Execute the migration {#execute-migration}

Once you have analyzed the dependencies and prepared your mappings, you can execute the migration.

#### Create a migration workflow {#create-migration-workflow}

Use the dependency mappings from Step 1 to configure and execute your migration.

**API format**

```http
POST /migration/service/migrations
```

**Sandbox-level migration**

To migrate all decisioning objects from one sandbox to another:

```shell
curl --request POST \
  --url "https://platform.adobe.io/migration/service/migrations" \
  --header "Authorization: Bearer <IMS_ACCESS_TOKEN>" \
  --header "x-gw-ims-org-id: <IMS_ORG_ID>" \
  --header "x-api-key: <CLIENT_API_KEY>" \
  --header "Content-Type: application/json" \
  --data '{
    "imsOrgId": "<IMS_ORG_ID>",
    "sourceSandboxDetails": { "sandboxName": "<SOURCE_SANDBOX_NAME>" },
    "targetSandboxDetails": { "sandboxName": "<TARGET_SANDBOX_NAME>" },
    "createDataStream": true,
    "dependency": {
      "profileAttributeDependency": {
        "sourceAttr1": "targetAttr1"
      },
      "segmentsDependency": {
        "sourceSegmentKey1": {
          "segmentNamespace": "<TARGET_SEGMENT_NAMESPACE>",
          "segmentId": "<TARGET_SEGMENT_ID>"
        }
      },
      "contextAttributeDependency": {
        "sourceCtx1": "targetCtx1"
      },
      "datasetName": "<TARGET_DATASET_NAME>"
    },
    "requestLevel": "sandbox"
  }'
```

**Offer-level migration**

To migrate specific offers only, use `requestLevel: "offer"` and add an `offersList` array:

```json
"offersList": ["offer-id-1", "offer-id-2"]
```

**Decision-level migration**

To migrate specific decisions only, use `requestLevel: "decision"` and add a `decisionsList` array:

```json
"decisionsList": ["decision-id-1", "decision-id-2"]
```

#### Monitor migration status {#poll-migration-status}

Poll the migration workflow to track its progress.

**API format**

```http
GET /migration/service/migrations/{id}
```

**Request**

```shell
curl --request GET \
  --url "https://platform.adobe.io/migration/service/migrations/<WORKFLOW_ID>" \
  --header "Authorization: Bearer <IMS_ACCESS_TOKEN>" \
  --header "x-gw-ims-org-id: <IMS_ORG_ID>" \
  --header "x-api-key: <CLIENT_API_KEY>"
```

**Migration results**

When the `status` field shows `Completed`, the migration was successful. The workflow `result` includes:
* Mappings of migrated objects
* Any warnings encountered during migration

When the `status` field shows `Failed`, review the `errors[]` array and `result.error` field for details about what went wrong.

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
POST /migration/service/rollbacks/{migrationWorkflowId}
```

Replace `{migrationWorkflowId}` with the ID of the migration workflow you want to roll back.

**Request**

```shell
curl --request POST \
  --url "https://platform.adobe.io/migration/service/rollbacks/<MIGRATION_WORKFLOW_ID>" \
  --header "Authorization: Bearer <IMS_ACCESS_TOKEN>" \
  --header "x-gw-ims-org-id: <IMS_ORG_ID>" \
  --header "x-api-key: <CLIENT_API_KEY>"
```

### Monitor rollback status {#poll-rollback-status}

Poll the rollback workflow to track its progress.

**API format**

```http
GET /migration/service/rollbacks/{rollbackWorkflowId}
```

**Request**

```shell
curl --request GET \
  --url "https://platform.adobe.io/migration/service/rollbacks/<ROLLBACK_WORKFLOW_ID>" \
  --header "Authorization: Bearer <IMS_ACCESS_TOKEN>" \
  --header "x-gw-ims-org-id: <IMS_ORG_ID>" \
  --header "x-api-key: <CLIENT_API_KEY>"
```

## Handle concurrent workflows {#handle-concurrency}

The Migration API allows only one workflow to run at a time per organization. If you attempt to create a new workflow while another is in progress, you will receive a **409 Conflict** error response ("A workflow is already in progress...").

In this case, wait for the in-progress workflow to complete, or retrieve the workflow ID and poll its status. Once the current workflow finishes, you can create a new one.

## Entity mapping reference {#entity-mapping}

When migrating from Decision management to Decisioning, entities are mapped as follows:

| Decision management | Decisioning |
|-------------------|-------------|
| Offer | Decision item |
| Offer collection | Item collection |
| Eligibility rule | Eligibility rule |
| Ranking formula | Ranking formula |
| Decision | Selection strategy + Decision policy |
| Campaign | Campaign *(basic content only)* |
| Placement | Surface + Channel configuration |
| Tag | Unified tag |

## Workflow cleanup {#cleanup}

Workflow resources can be deleted by service users only. Delete operations require an `If-Match` header with the workflow's `_etag` value.

**Available delete operations:**

* `DELETE /migration/service/dependency/{id}`
* `DELETE /migration/service/migrations/{id}`
* `DELETE /migration/service/rollbacks/{id}`

>[!NOTE]
>
>Workflow deletion is only available to service accounts with appropriate permissions. If you need to delete a workflow resource, contact your system administrator.

## Related topics {#related-topics}

* [Migrate from Decision management to Decisioning](migrate-to-decisioning.md) - Understand the benefits and capabilities of migrating to Decisioning
* [Get started with Decisioning](gs-experience-decisioning.md)
* [Decisioning guardrails and limitations](decisioning-guardrails.md)
* [Get started with Decisioning APIs](api-reference/getting-started.md)
