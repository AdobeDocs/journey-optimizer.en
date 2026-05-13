---
solution: Journey Optimizer
product: journey optimizer
title: About Adobe Experience Platform audiences
description: Learn how to work with Adobe Experience Platform audiences
feature: Audiences, Profiles
topic: Content Management
role: User
level: Beginner
exl-id: 3ec496ba-7555-49e2-992c-403c33302a90
TQID: https://experienceleague.adobe.com/Tf-a0MQ4SBclyiXPLohyD1rr-7rHq9ASNuaKN10anyw
product_v2:
  - id: cb954087-f4fc-4456-afb9-e939cabcdc79
    internal-label: Journey Optimizer
feature_v2:
  - id: bb359667-ec7d-4d4b-8663-5850fc219d32
    internal-label: Administration
  - id: d556b755-390a-43f0-be32-a08cf6236126
    internal-label: Configuration
  - id: d998adac-2f81-400b-a669-d07bb196e4eb
    internal-label: Journeys
  - id: dc22c819-3f29-4e91-8b7d-5c6719831141
    internal-label: Content management
subfeature_v2:
  - id: fb9a80eb-bebc-492f-a0e9-584595621ebb
    internal-label: Publish
role_v2:
  - id: b69b2659-1057-424e-8fc5-ed9e016dc554
    internal-label: User
level_v2:
  - id: e8ccd51f-da0d-4e3b-939b-e30d5ebb1ea5
    internal-label: Beginner
topic_v2:
  - id: e0eb8757-182f-49f3-94a4-1587d16f5094
    internal-label: Personalization
  - id: eddd9b14-83bd-4ff4-9072-54a4a484abb7
    internal-label: Administration
---
# Use audiences enrichment attributes {#enrichment}

When targeting an audience generated using composition workflows, custom (CSV file) audience, or Federated Audience Composition, you can use enrichment attributes from these audiences to build your journey and personalize your messages.

>[!NOTE]
>
>Audiences created through CSV file custom upload before October 1, 2024, are not eligible for personalization. To use attributes from these audiences and fully utilize this feature, please re-create and re-upload any external CSV audience imported before this date.
>
>Consent policies do not support enrichment attributes. Therefore, any consent policy rules should be based only on attributes found in the profile.

Here are the actions you can perform using audiences' enrichment attributes:

* **Create multiple paths in a journey** based on rules that leverage the targeted audience's enrichment attributes. To do this, target the audience using a [Read audience](../building-journeys/read-audience.md) activity then create rules in an [Optimize](../building-journeys/optimize.md) activity based on the audience's enrichment attributes.

    ![](assets/audience-enrichment-attribute-condition.png){width="70%" zoomable="yes"}

* **Personalize your messages** in journeys or campaigns by adding enrichment attributes from the targeted audience in the personalization editor. [Learn how to work with the personalization editor](../personalization/personalization-build-expressions.md)

    ![](assets/audience-enrichment-attribute-perso.png){width="70%" zoomable="yes"}

>[!IMPORTANT]
>
>To use enrichment attributes from audiences created using composition workflows, ensure that they are added to a Field Group within the "ExperiencePlatform" Data Source.
>
>+++ Learn how to add enrichment attributes to a Field Group
>
>1. Navigate to "Administration" > "Configuration" > "Data Sources". 
>1. Select "Experience Platform" and create or edit a Field Group.
>1. In the schema selector, select the appropriate schema. The name of the schema will follow this format: 'Schema for audienceId:' + the ID of the audience. You can find the ID of the audience on the audience details screen in the audience inventory.
>1. Open the field selector, find the enrichment attributes you want to add, and select the check box next to them.
>1. Save your changes.
>1. Once enrichment attributes are added to a Field Group, you can use them in Journey Optimizer at the locations listed above.
>
>Detailed information on data sources is available in these sections:
>
>* [Work with the Adobe Experience Platform data source](../datasource/adobe-experience-platform-data-source.md)
>* [Configure a data source](../datasource/configure-data-sources.md)
>
>+++


## Frequently asked questions {#faq-enrichment}

You will find below Frequently Asked Questions about enrichment attributes.

Need more details? Use the feedback options at the bottom of this page to raise your question, or connect with [Adobe Journey Optimizer community](https://experienceleaguecommunities.adobe.com/t5/adobe-journey-optimizer/ct-p/journey-optimizer?profile.language=en){target="_blank"}.

+++ What are enrichment attributes?

Enrichment attributes are additional attributes that are contextual and specific to an audience. They are not associated with the profile, and are typically used for personalization purposes. 

Enrichment attributes are linked to an audience through an Enrich activity in audience composition or the custom upload process.

+++

+++ Where can I use enrichment attributes within Journey Optimizer?

Enrichment attributes from audience composition can be leveraged in the following areas. [Learn how to use audiences enrichment attributes](#enrichment)

* Condition activity (Journeys)
* Custom action attributes (Journeys)
* Message personalization (Journeys and campaigns)

+++

+++ How do I enable enrichment attributes in Journeys?

To use enrichment attributes from audiences created using composition workflows, ensure they are added to a Field Group within the "ExperiencePlatform" Data Source. Information on how to add enrichment attributes to a Field Group is available in [this section](#enrichment)

+++

+++ Are enrichment attribute values updated after a journey starts?

Currently, no. Even after wait or event nodes, enrichment attribute values remain the same as they were when the journey started.

+++
