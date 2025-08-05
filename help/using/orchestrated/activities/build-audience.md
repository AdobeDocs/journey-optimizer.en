---
solution: Journey Optimizer
product: journey optimizer
title: Use the Build audience activity
description: Learn how to use the Build audience activity in an Orchestrated campaign
exl-id: 3959b5fa-0c47-42a5-828f-4d7ca9b7e72d
---

# Build audience {#build-audience}

>[!CONTEXTUALHELP]
>id="ajo_orchestration_build_audience"
>title="Build audience activity"
>abstract="The **Build audience** activity allows you to define the audience that will enter the Orchestrated campaign. When sending messages in the context of an Orchestrated campaign, the message audience is not defined in the channel activity, but in a **Build audience** activity."

As a marketer, you can create complex audience segments through an intuitive interface, allowing you to target users based on a wide range of criteria and behaviors to tailor your campaigns more effectively.

To do this, use the **[!UICONTROL Build audience]** targeting activity. This activity defines the audience that enters the Orchestrated campaign. When sending messages as part of an Orchestrated campaign, the audience is defined in the **[!UICONTROL Build audience]** activity, not within the Orchestrated campaign.

## Configure the Build audience activity {#build-audience-configuration}

>[!CONTEXTUALHELP]
>id="ajo_orchestration_build_audience_audienceselector"
>title="Audience"
>abstract="Select your audience, the same way you use an audience when designing a new delivery."

Follow these steps to configure the **[!UICONTROL Build audience]** activity:

1. Add a **[!UICONTROL Build audience]** activity.

    ![](../assets/build-audience.png)

1. Define a **[!UICONTROL Label]**.

1. Configure your audience by following the steps detailed in the tabs below.

1. Choose the **[!UICONTROL Targeting dimension]**. The targeting dimension lets you define the population targeted by the operation: recipients, contract beneficiaries, operator, subscribers, etc. By default, the target is selected from the recipients.

1. Click **[!UICONTROL Continue]**.

1. Use the rule builder to define your query. [Learn more about the Rule builder in this section](../orchestrated-rule-builder.md) 

1. Specify whether an outbound transition should be generated when the audience is empty.

## Examples{#build-audience-examples}

Here is an example of an Orchestrated campaign with two **[!UICONTROL Build audience]** activities. The first targets profiles that have items in their cart, followed by an email delivery. The second targets profiles with a wishlist, followed by an SMS delivery.

![](../assets/build-audience-2.png)
