---
solution: Journey Optimizer
product: journey optimizer
title: Use dynamic fragments
description: Learn how to use dynamic fragment resolution in Adobe Journey Optimizer to select and inject fragments at runtime based on profile attributes, dataset lookups, or context data.
feature: Fragments
topic: Content Management
role: User, Developer
level: Intermediate, Experienced
keywords: dynamic, fragment, expression, personalization, runtime
---
# Use dynamic fragments {#dynamic-fragments}

>[!BEGINSHADEBOX]

**On this page:** Learn how to use dynamic fragment resolution in Adobe Journey Optimizer to select which published fragment is injected into a message at runtime, based on profile attributes, dataset lookups, or context data passed at send time.

>[!ENDSHADEBOX]

[!DNL Adobe Journey Optimizer] supports **dynamic fragment resolution** at runtime, allowing you to select which published fragment is injected into a message based on profile attributes, dataset lookups, or context data passed at send time. This enables highly personalized content without duplicating campaign or journey logic.

## Overview {#overview}

**Static fragments** are embedded in a message at design time — the same fragment is used for every recipient. **Dynamic fragments** resolve the fragment ID at runtime per recipient, meaning different profiles can receive entirely different content blocks within the same campaign or journey.

Dynamic fragment IDs can come from three sources:

* A **dataset lookup** — for example, a recommendations dataset keyed by style or product
* A **profile attribute** stored in Adobe Experience Platform
* **Context data** passed directly in the API request at send time

>[!NOTE]
>
>Using the `datasetLookup` helper function within expression fragments is currently available for a limited set of customers. To gain access, contact your Adobe representative.

## Prerequisites {#prerequisites}

Before using dynamic fragments, ensure the following are in place:

* You have the required permissions to create and publish fragments in [!DNL Journey Optimizer]. [Learn more](../administration/ootb-product-profiles.md#content-library-manager)
* The fragment you intend to reference is **published** (status: **Live**). Draft fragments cannot be resolved at runtime.
* If resolving the fragment ID from a dataset, the dataset schema includes a field that stores the fragment ID, and the dataset is [enabled for lookup](../data/lookup-aep-data.md).
* All profile attributes that the dynamic fragment itself references are included in the message export path or are available in the profile at send time.

>[!CAUTION]
>
>Fragment-related validations are skipped in the dynamic fragment flow. Invalid fragment IDs surface as runtime delivery failures rather than upfront validation errors. Always verify that referenced fragment IDs are valid and published before activating a campaign.

## Step 1: Create and publish the fragment {#create-fragment}

Before referencing a fragment dynamically, it must be published in [!DNL Journey Optimizer].

1. In [!DNL Journey Optimizer], navigate to **[!UICONTROL Content Management]** > **[!UICONTROL Fragments]**.

1. Select **[!UICONTROL Create fragment]** and author the content. [Learn how to create fragments](create-fragments.md)

1. When the content is ready, click **[!UICONTROL Publish]**. Publication is asynchronous and may take a few seconds. Confirm that the fragment status changes to **Live** before proceeding.

1. Note the **fragment ID** from the fragment detail view or from the Fragments API response. You will reference this ID in the message.

>[!NOTE]
>
>You can retrieve all published fragment IDs programmatically using the `GET /fragments` API. Refer to the [Journey Optimizer APIs documentation](https://developer.adobe.com/journey-optimizer-apis/references/content){target="_blank"} for details.

## Step 2: Author the message with a dynamic fragment reference {#author-message}

In the personalization editor, insert the dynamic fragment placeholder using the following syntax:

```handlebars
{{fragment id=dynamic_fragment_id}}
```

The identifier `dynamic_fragment_id` is a variable name. Its value must be resolved before the fragment lookup occurs. You resolve it using a dataset lookup expression, a profile attribute, or context data.

### Resolve from a dataset lookup {#resolve-from-dataset}

If the fragment ID is stored in an AEP dataset (for example, a style-to-fragment mapping table), use the `datasetLookup` helper function to resolve it:

```handlebars
{{
  {datasetLookup datasetId="<your-dataset-id>" key=profile.style attribute="fragmentId"}
}}

{{fragment id=dynamic_fragment_id}}
```

In this example, the dataset contains rows keyed by a style value (such as `style1`). For a given profile, the lookup retrieves the corresponding `fragmentId` column value and assigns it to `dynamic_fragment_id`, which is then used to resolve the fragment.

>[!NOTE]
>
>Using the `datasetLookup` helper function within expression fragments is currently available for a limited set of customers. To gain access, contact your Adobe representative. For more on dataset lookups in personalization, see [Use Adobe Experience Platform data](../data/lookup-aep-data.md).

### Resolve from context data {#resolve-from-context}

If the fragment ID is supplied at send time as part of the API request context, reference it using the `context` namespace:

```handlebars
{{fragment id=context.audiencePayload.fragmentId}}
```

The path `context.audiencePayload` is the required prefix for all attributes sourced from a CSV audience file or passed via the API request context. The column name from the CSV (for example, `fragmentId`) follows the prefix.

### Resolve from a profile attribute {#resolve-from-profile}

If the fragment ID is stored as a profile attribute in Adobe Experience Platform, reference it directly:

```handlebars
{{fragment id=profile.mi.fragmentId}}
```

## Step 3: Configure your dataset for the lookup approach {#configure-dataset}

If you are using the dataset lookup approach, update your dataset schema and data to carry the fragment ID.

1. In your recommendations or mapping dataset, add a column (for example, `fragmentId`) that stores the published AJO fragment ID for each row.

1. For each style or variant (for example, `style1`, `style2`), populate the `fragmentId` column with the corresponding fragment ID.

1. Ensure the dataset is ingested into Adobe Experience Platform and [enabled for lookup](../data/lookup-aep-data.md).

1. Confirm that all profile attributes referenced inside the dynamic fragment are captured in the message or in a static fragment to prevent empty rendering at export time.

**Example dataset structure:**

| Column | Example value |
|---|---|
| style | style1 |
| fragmentId | &lt;fragment-id-1&gt; |
| style | style2 |
| fragmentId | &lt;fragment-id-2&gt; |

## Step 4: Pass context data at send time {#pass-context-data}

If you are resolving the fragment ID from context data (for example, from a CSV audience recommendation file), pass the fragment ID in the API request under the required context prefix.

When using the campaign proofing API, include the fragment ID in the `context` object:

```json
{
  "recipients": [
    {
      "userId": "<profile-email>",
      "namespace": "email"
    }
  ],
  "inChannelData": {
    "channel": "email",
    "emailAddresses": ["<delivery-address>"]
  },
  "context": {
    "audiencePayload": {
      "fragmentId": "<published-fragment-id>",
      "systemSource": "<optional-system-value>"
    }
  }
}
```

The prefix `context.audiencePayload` is required. Attributes nested under this key map directly to columns in the CSV audience file when running the live campaign.

## Step 5: Proof and validate {#proof-validate}

Before activating the campaign, use the campaign proofing API to verify that the dynamic fragment resolves correctly and that the rendered email output is as expected.

1. Trigger a proof job using the `POST /campaigns/{id}/proofs` endpoint. In the proof request, pass the fragment ID you want to test under `context.audiencePayload.fragmentId`.

1. Poll the proof job status using the `GET /campaigns/{id}/proofs/{proofId}` endpoint until the status is `Submitted` or `Failed`.

1. Check the delivered email to verify that the correct fragment content is rendered.

1. If the fragment content is missing or incorrect, verify that the fragment ID is valid, the fragment is published, and all required profile attributes are present.

For more on the campaign API, refer to the [Journey Optimizer APIs documentation](https://developer.adobe.com/journey-optimizer-apis/references/campaigns-retrieve){target="_blank"}.

## Guardrails and limitations {#guardrails}

>[!CAUTION]
>
>OLAC (Object-Level Access Control) is not enforced for fragments in the dynamic fragment model. Ensure your access control requirements are accounted for at the campaign and audience level.

The following limitations apply when using dynamic fragments:

* **Profile attribute coverage at export time**: The fragment is chosen at runtime per profile. Profile attributes required by the dynamic fragment are not known in advance. If the dynamic fragment relies on a profile attribute that was not present in the original message or in any static fragment referenced in the message, that field may render empty in the export path.

* **No upfront fragment validation**: Fragment-related validations are skipped in this flow. Incorrect or unpublished fragment IDs surface as runtime delivery failures rather than validation errors shown in the UI.

* **Schema change required for the dataset approach**: Using the lookup-by-ID path requires updating the dataset schema to store and pass the fragment ID, plus the plumbing needed to feed that into the message pipeline.

* **Attribute capture for export**: Ensure all attributes used inside the dynamic fragment are captured in the message or in static fragments to prevent empty rendering in the export path.

More guardrails applying to fragments are available in [this section](../start/guardrails.md#fragments-guardrails).

## Error handling {#error-handling}

If a dynamic fragment fails to resolve at runtime, an exclusion event is generated for the affected profile. Currently, all fragment rendering failures are categorized as a single blanket error type.

To debug fragment resolution failures:

1. Check the campaign delivery reports for exclusion events.
1. Verify that the fragment ID passed at runtime matches a published fragment.
1. Confirm that all profile attributes required by the fragment are present in the profile at send time.
1. Use the [proofing API](#proof-validate) to test specific fragment IDs before activating the campaign.
