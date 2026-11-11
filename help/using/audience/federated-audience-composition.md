---
solution: Journey Optimizer
product: journey optimizer
title: Work with Federated Audience Composition audiences
description: Learn what Federated Audience Composition (FAC) is, what a federated audience is, and how to use federated audiences in Adobe Journey Optimizer
feature: Audiences, Profiles
topic: Content Management
role: User
level: Beginner
exl-id: 90328ba9-e6b0-4105-abcf-3e3a9ed41aa6
product_v2:
  - id: cb954087-f4fc-4456-afb9-e939cabcdc79
    internal-label: Journey Optimizer
feature_v2:
  - id: baecb07f-ce89-4ebb-9cd9-0f7c053f944f
    internal-label: Journey management
  - id: d2971708-e780-44bb-9e2a-72f139796afd
    internal-label: Customer
subfeature_v2:
  - id: b32bb433-f8c6-4931-8e52-e657230a3bf2
    internal-label: Audiences
  - id: ef9a83ca-eefa-47cf-aa34-f1a34715583a
    internal-label: Profiles
role_v2:
  - id: b69b2659-1057-424e-8fc5-ed9e016dc554
    internal-label: User
level_v2:
  - id: e8ccd51f-da0d-4e3b-939b-e30d5ebb1ea5
    internal-label: Beginner
---
# Federated Audience Composition {#fac}

>[!BEGINSHADEBOX]

**On this page:** Learn how to use Federated Audience Composition in Adobe Journey Optimizer to query your enterprise data warehouse and enrich Adobe Experience Platform audiences without duplicating sensitive data.

>[!ENDSHADEBOX]

While you can use the audience composition capabilities to create valuable, highly refined audiences for targeting, you can further enrich audiences for deeper personalization using data from your enterprise data warehouse and trusted partners.

The Federated Audience Composition (FAC) capability available in Adobe [!DNL Journey Optimizer] can query a data warehouse for data or profile
attributes to use in composing audiences, leaving sensitive data in the warehouse and avoiding data duplication. This can include both profile-based data and non-profile data. For example, a quick-service restaurant group could enrich profiles of customers
that recently placed orders online with each customer's preferred restaurant location, enabling the restaurant group to send customers offers that can be used at those preferred locations.

An audience created using FAC is called a *federated audience*. After you run the composition, the federated audience is saved in Adobe Experience Platform as an external audience.

* **Data integration** - Boost flexibility and efficiency with ability to query relevant pre-built audiences and datasets from your enterprise data warehouse and partners into a single environment to augment Adobe Experience Platform use cases.
* **Enhanced marketing processes** - Unlock additional support for segmentation, targeting, and activation use cases with streamlined, adaptable workflows.
* **Efficient data management** - Minimize data copy, govern sensitive
data usage, and optimize IT investments to complement real-time cross-channel use cases on Adobe Experience Platform.

For more information, read the guide on [Federated Audience Composition](https://experienceleague.adobe.com/en/docs/federated-audience-composition/using/home){target="_blank"}.

Learn more about Federated Audience Composition in video:

>[!VIDEO](https://video.tv.adobe.com/v/3432261?quality=12)

## Use federated audiences in journeys and campaigns {#use-in-journeys}

You can select a federated audience in journeys and campaigns, like any other audience. Keep the following in mind:

* Federated audiences require the Federated Audience Composition add-on. [Learn more about prerequisites](https://experienceleague.adobe.com/en/docs/federated-audience-composition/using/start/access-prerequisites){target="_blank"}
* In journeys, you can use a federated audience in [!UICONTROL Read audience] and [!UICONTROL Condition] activities, but not in [!UICONTROL Audience Qualification] activities. [Learn more](target-audiences.md#guardrails)
* A federated audience is static. Its members stay the same until the next composition run.
* The identity namespace of the audience must match the journey namespace.
* Preview and proof are not supported, and incremental read is not functionally supported. [Learn more about incremental read](../building-journeys/read-audience.md)

{{$include /help/_includes/do-not-localize/audience/ai-augmented-federated-audience-composition.md}}
