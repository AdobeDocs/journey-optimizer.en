---
solution: Journey Optimizer
product: journey optimizer
title: Journey Optimizer for teams switching platforms
description: Map the terms and concepts you know from other marketing platforms to their Adobe Journey Optimizer equivalents.
feature: Get Started
topic: Content Management
role: User
level: Beginner
keywords: migrate, switch, term map, braze, canvas, segment, workspace, equivalent, glossary
product_v2:
  - id: cb954087-f4fc-4456-afb9-e939cabcdc79
    internal-label: Journey Optimizer
subfeature_v2:
  - id: e30b0a1a-b594-47b8-af94-1e3a2be6df11
    internal-label: Get started
role_v2:
  - id: b69b2659-1057-424e-8fc5-ed9e016dc554
    internal-label: User
level_v2:
  - id: e8ccd51f-da0d-4e3b-939b-e30d5ebb1ea5
    internal-label: Beginner
---
# Journey Optimizer for teams switching platforms {#coming-from-another-platform}

>[!BEGINSHADEBOX]

**On this page:** Find the Journey Optimizer equivalent of the terms you already know, and see where the concepts differ, so you can get productive faster.

>[!ENDSHADEBOX]

<!-- DRAFT: SME review required before publishing. Confirm each mapping and "key difference" with the product team. Rows for Workspace and Currents were left out until verified. -->

If you are moving to [!DNL Journey Optimizer] from another marketing platform, most of what you know still applies. The names are different, and some concepts work differently because [!DNL Journey Optimizer] is built on Adobe Experience Platform. The mappings below are approximate. Read the **Key difference** column before you assume a one-to-one match.

New to the product as a whole? Start with the [five core concepts](understanding-ajo.md#five-concepts).

## Term map: Braze to Journey Optimizer {#braze}

| If you know… (Braze) | In Journey Optimizer | Key difference |
|---|---|---|
| User profile | [Profile](../audience/get-started-profiles.md) | Profiles are stored in Adobe Experience Platform and unify attributes, events, and identities. |
| Segment | [Audience](../audience/about-audiences.md) | Audiences can be created in Journey Optimizer or in Adobe Experience Platform. |
| Campaign | [Campaign](../campaigns/get-started-with-campaigns.md) | Journey Optimizer also offers [orchestrated campaigns](../orchestrated/gs-orchestrated-campaigns.md) for complex batch workflows. |
| Canvas | [Journey](../building-journeys/journey.md) | Journeys are driven by events and audience changes, and customers move through at their own pace. |
| Custom event | [Event](../event/about-events.md) | Events are defined through an Experience Platform schema, so schema and dataset setup comes first. |
| Custom attribute | Profile attribute (schema field) | Attributes are fields in an Experience Platform schema. |
| Content Block | [Fragment](../content-management/fragments.md) | Fragments are reusable content blocks that you update in one place. |
| Content Card | [Content card](../content-card/get-started-content-card.md) | Content cards are a channel that needs a channel configuration. |

## Where the concepts differ {#differences}

* **Data comes first.** Events, attributes, and audiences rely on schemas and datasets in Adobe Experience Platform. Ask a [data engineer](path/data-engineer.md) to set these up before marketers build. See [Roles and responsibilities](quick-start.md).
* **Sandboxes isolate environments.** Data, audiences, journeys, and settings do not carry across sandboxes. See [Use and assign sandboxes](../administration/sandboxes.md).
* **Channels need a configuration.** An administrator sets up a [channel configuration](../configuration/channel-surfaces.md) (sender, subdomain, app credentials) before any message can send.

## Bring your content and journeys with you {#migrate}

If your organization has access, you can import existing email content and journeys instead of rebuilding them. See [Migrate content and journeys](migrate-content-and-journeys.md).

## Next steps {#next-steps}

1. Read the [five core concepts](understanding-ajo.md#five-concepts).
1. Find your role in [Roles and responsibilities](quick-start.md).
1. Follow the steps in the [onboarding hub](onboarding-hub.md) to build your first experience.

For definitions of other terms, see [Key terminology](terminology.md).
