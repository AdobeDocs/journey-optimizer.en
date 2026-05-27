---
solution: Journey Optimizer, Experience Platform
product: Journey Optimizer
title: Get started with Decision Management
description: Learn how Adobe Journey Optimizer can help you send your customers the right offer at the right time
badge: label="Legacy" type="Informative"
feature: Decision Management
topic: Integrations
role: User
level: Intermediate
exl-id: 659984cb-b232-47ba-9f5a-604bf97a5e92
version: Journey Orchestration
TQID: https://experienceleague.adobe.com/-drNPR5XmWbTe050ZO3s-tymLiQXjT4gjth7-QTv01c
product_v2:
  - id: cb954087-f4fc-4456-afb9-e939cabcdc79
    internal-label: Journey Optimizer
feature_v2:
  - id: a4cb03e1-327e-499d-9de8-e0c0db8a63a2
    internal-label: Decision capabilities (AJO)
  - id: ad78185d-8f79-40ad-9bad-cbde74af74ee
    internal-label: Guardrails and limitations
role_v2:
  - id: b69b2659-1057-424e-8fc5-ed9e016dc554
    internal-label: User
level_v2:
  - id: b5a62a22-46f7-4f0d-b151-3fc640bef588
    internal-label: Intermediate
topic_v2:
  - id: e0eb8757-182f-49f3-94a4-1587d16f5094
    internal-label: Personalization
  - id: fd2e3797-f2ea-4b36-a9af-52acf5e90513
    internal-label: Customer profiles
subfeature_v2:
  - id: a7a194a0-75e2-4913-8a83-14714fbf68e6
    internal-label: Decisioning API
  - id: eb547372-2a95-4d13-b0fd-f720c9895880
    internal-label: Edge Decisioning (AJO)
  - id: e30b0a1a-b594-47b8-af94-1e3a2be6df11
    internal-label: Get started
---
# Get started with decision management {#about-decision-management}

Use [!DNL Journey Optimizer] to deliver the best offer and experience to your customers across all touch points at the right time. Once designed, target your audiences with personalized offers.

Decision management makes personalization easy with a central library of marketing offers and a decision engine that applies rules and constraints to rich, real-time profiles created by Adobe Experience Platform to help you send your customers the right offer at the right time.

The Decision Management capability consists in two main components:

* The **Centralized Offer Library** which is the interface where you create and manage the different elements that compose your offers, and define their rules and constraints.
* The **Offer Decision Engine** which leverages Adobe Experience Platform data and Real-time Customer profiles, along with the Offer Library, in order to select the right time, customers and channels to which offers will be delivered.

![](../assets/architecture.png)

Benefits include:

* Improved campaign performance by delivering personalized offers across multiple channels,
* Improved workflows: instead of creating multiple deliveries or campaigns, marketing teams can improve workflows by creating a single delivery and vary the offers in different parts of the template,
* Control over the number of times an offer is shown across campaigns and customers.

➡️ [Learn more about Decision Management in these videos](#video)

>[!NOTE]
>
>If you are an [Adobe Experience Platform](https://experienceleague.adobe.com/docs/experience-platform/landing/home.html){target="_blank"} user leveraging the **Offer Decisioning** application, all the Decision Management features described in this section also apply to you.

## About offers and decisions {#about-offers-and-decisions}

An **Offer** is made up of content, eligibility rules and constraints that define the conditions under which it is presented to your customers.

It is created using the **Offer Library**, which provides a central offer catalog where you can associate eligibility rules and constraints with multiple pieces of content to create and publish offers (see [Offer Library user interface](../get-started/user-interface.md)).

![](../assets/offer_structure.png) 

Once the Offer Library has been enriched with offers, you can integrate your offers into **decisions**.

Decisions are containers for your offers that will leverage the Offer Decision Engine in order to pick the best offer to deliver depending on the target of the delivery.

## Common use cases {#common-use-cases}

Decision Management capabilities and integration with Adobe Experience Platform allow you to cover numerous use cases to help you increase customers' engagement and conversion.

* Display on your website homepage offers that will match the visiting customer's point of interest, based on data from Adobe Experience Platform.

    ![](../assets/website.png)

* If customers walk near one of your stores, send them push notifications reminding them of available offers according to their attributes (loyalty level, gender, former purchases...).

    ![](../assets/push_sample.png)

* Decision Management also helps you enhance your customers' experience when contacting your support team. Decision Management APIs allow you to display in your call center agents' portal information about the customer's redeemed and next best offers.

    ![](../../assets/do-not-localize/call-center.png)

## Grant access to decision management {#granting-acess-to-decision-management}

Permissions to access and use decisioning capabilities are managed using the [Adobe Admin Console](https://helpx.adobe.com/enterprise/managing/user-guide.html){target="_blank"}. 

To grant access to the  Decision Management functionality, you need to create a **[!UICONTROL Product profile]** and assign the corresponding permissions to your users. Learn more about managing [!DNL Journey Optimizer] users and permissions in [this section](../../administration/permissions.md).

The permissions specific to Decision Management are listed in [this section](../../administration/high-low-permissions.md#decisions-permissions).

## Glossary {#glossary}

You can find below the list of the main concepts you will work with when using Decision Management. 

* **Capping** or **Frequency Capping**: Capping is used as a constraint to define how many times an offer is presented. There are two types of caps, how many times an offer can be proposed across the combined target audience, also known as "Total caps" and how many times an offer can be proposed to the same end user, also known as "Profile Cap".

* **Collections**: Collections are subsets of offers based on predefined conditions defined by a marketer, such as category of the offer.

* **Decision**: A decision contains the logic that informs the selection of an offer.

* **Decision Rule**: Decision rules are constraints added to a personalized offer and applied to a profile to determine eligibility.

* **Eligible Offer**: An eligible offer meets the constraints defined upstream that can be consistently offered to a profile.

* **Decision Management**: Allows you to create and deliver end-user personalized offer experiences across channels and applications using business logic and decision rules.

* **Fallback Offers**: A fallback offer is the default offer displayed when an end-user is not eligible for any of the personalized offers in the collection.

* **Offer**: An offer is a marketing message that may have rules associated with it that specify who is eligible to see the offer.

* **Offer Library**: The offer library is a central library used to manage personalized and fallback offers, decision rules and decisions.

* **Personalized Offers**: A personalized offer is a customizable marketing message based on eligibility rules and constraints.

* **Placements**: A placement is the location and or context in which an offer appears for an end-user.

* **Priority**: Priority is used to rank offers that meet all constraints, such as eligibility, calendar, and capping.

* **Representations**: A representation is information used by a channel, such as location or language to display an offer.

## How-to videos{#video}

### What is decision management? {#what-is-offer-decisioning}

The video below provides an introduction to Decision Management key capabilities, architecture and use cases:

>[!VIDEO](https://video.tv.adobe.com/v/326961?quality=12&learn=on)

### Define and manage offers {#use-offer-decisioning}

The video below shows how to use Decision Management to define and manage your offers and leverage real-time customer data.

>[!VIDEO](https://video.tv.adobe.com/v/326841?quality=12&learn=on)


