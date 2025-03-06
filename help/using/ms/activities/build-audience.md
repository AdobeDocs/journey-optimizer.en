---
solution: Journey Optimizer
product: journey optimizer
title: Use the Build audience activity
description: Learn how to use the Build audience activity in a multi-step campaign
hide: yes
hidefromtoc: yes
---
# Build audience {#build-audience}

>[!CONTEXTUALHELP]
>id="ajo_orchestration_build_audience"
>title="Build audience activity"
>abstract="The **Build audience** activity allows you to define the audience that will enter the multi-step campaign. When sending messages in the context of a multi-step campaign, the message audience is not defined in the channel activity, but in the **Build audience** activity."

The **Build audience** activity is a **Targeting** activity. This activity allows you to define the audience that will enter the multi-step campaign. When sending messages in the context of a multi-step campaign, the message audience is not defined in the channel activity, but in the **Build audience** activity.

To define the audience population, you can:

* Select an Adobe Experience Platform audience. 
* Build a new audience with the query modeler by defining and combining filtering criteria.

>[!NOTE]
>
>Audiences loaded from a file cannot be targeted using a Build audience activity. To do this, you need to use a **Load file** activity followed by a **Reconciliation** activity.

<!--
The **Build audience** activity can be placed at the beginning of the workflow or after any other activity. Any activity can be placed after the **Build audience**.
-->

## Configure the Build audience activity {#build-audience-configuration}

>[!CONTEXTUALHELP]
>id="ajo_orchestration_build_audience_audienceselector"
>title="Audience"
>abstract="Select your audience, the same way you use an audience when designing a new delivery."

Follow these steps to configure the **Build audience** activity:

![](../assets/workflow-audience.png)

1. Add a **Build audience** activity. 
1. Define a label.
1. Define the audience type: **Create your own** or **Read audience**. 
1. Configure your audience by following the steps detailed in the tabs below.

>[!BEGINTABS]

>[!TAB Create your own (query)]

To create your own query, follow these steps:

1. Select **Create your own (query)**.
1. Choose the **Targeting dimension**. The targeting dimension lets you define the population targeted by the operation: recipients, contract beneficiaries, operator, subscribers, etc. By default, the target is selected from the recipients.
1. Click **Continue**.
1. Use the query modeler to define your query, the same way you create an audience when designing a new email. 

>[!TAB Read audience]

To select an existing audience, follow these steps:

1. Select **Read audience**.
1. Click **Continue**.
1. Select your audience, the same way you use an audience when designing a new delivery. Refer to this [section](../../audience/add-audience.md).

>[!ENDTABS]

## Examples{#build-audience-examples}

Here is an example of a multi-step campaign with two **Build audience** activities. The first one targets the poker players audience, followed by an email delivery. The second one targets the VIP clients audience, followed by an SMS delivery.

![](../assets/workflow-audience-example.png)
