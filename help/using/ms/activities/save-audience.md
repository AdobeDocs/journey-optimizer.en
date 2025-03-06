---
solution: Journey Optimizer
product: journey optimizer
title: Use the Save audience activity
description: Learn how to use the Fork activity in a multi-step campaign
hide: yes
hidefromtoc: yes
---
# Save audience {#save-audience}

>[!CONTEXTUALHELP]
>id="ajo_orchestration_save_audience"
>title="Save an audience"
>abstract="Use this activity to update an existing audience or create a new audience from the population computed upstream in the multi-step campaign. The audiences created are added to the list of audiences, and available via the **Audiences** menu."

>[!CONTEXTUALHELP]
>id="ajo_orchestration_saveaudience_outbound"
>title="Generate outbound transition"
>abstract="Use this option option if you want to add a transition after the **Save audience** activity."

The **Save audience** activity is a **Targeting** activity. This activity allows you to update an existing audience or create a new audience from the population computed upstream in a multi-step campaign. The audiences created are added to the list of application audiences, and are made available via the **Audiences** menu.

This activity is essentially used to keep population groups computed in the same multi-step campaign, by converting them into reusable audiences. Connect it to other targeting activities such as a **Build audience** or a **Combine** activity. 

## Configure the Save audience activity{#save-audience-configuration}

Follow these steps to configure the **Save audience** activity:

![](../assets/workflow-save-audience.png)

1. Add a **Save audience** activity to your multi-step campaign.

1. In the **Mode** drop-down, select the action that you would like to carry out:

    * **Create or update an existing audience**: define an **Audience label**. If the audience already exists, it will be updated, otherwise a new audience will be created.

    * **Update an existing audience**: choose the **Audience** you wish to update among the list of existing audiences. 

1. Select the **Update mode** which will apply for existing audiences:

    * **Replace audience content with new data**: all audience content is replaced. The old data is lost. Only the data from the inbound transition of the save audience activity is kept. This option erases the audience type and the targeting dimension of the updated audience.

    * **Complete audience with new data**: the old audience content is kept and the data from the save audience activity's inbound transition is added to it.

1. Check the **Generate an outbound transition** option if you wish to add a transition after the **Save audience** activity.

The content of the saved audience is then available in the detail view of the audience, which can be accessed from the **Audiences** menu. The columns available from this view correspond to the columns of the inbound transition of the multi-step campaign's **Save audience** activity. 


## Example{#save-audience-example}

The following example illustrates a simple audience update from targeting. A scheduler is added to run the multi-step campaign once a month. A query recovers all the profiles subscribed to the different applications available. The **Save audience** activity updates the audience by deleting profiles that have unsubscribed from the service since the last multi-step campaign execution and by adding the newly subscribed profiles.
