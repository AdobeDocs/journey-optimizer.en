---
solution: Journey Optimizer
product: journey optimizer
title: Combine targeting and experimentation
description: Learn how to combine targeting and experiments within a single journey or campaign to create sophisticated optimization strategies.
role: User
level: Intermediate
keywords: optimization, targeting, experimentation, combination, advanced
---
# Combine targeting and experimentation {#combination}

Journey Optimizer also allows you to combine targeting and experiments within a single journey or campaign to create more sophisticated strategies.

Indeed, you can use targeting to create several variants, and for each variant, use experimentation to further optimize each content. This ensures that experiments are specific to each targeting rule and do not span across variants.

For example, you can test a '50% off promotion' versus a '$50 gift card' for customers in the USA, and run a different test for customers in Europe, such as 'free shipping on orders over &euro;50' versus '20% off their next purchase'.

To combine both targeting and experiments in a journey or campaign, follow the steps below.

1. Create a journey or a campaign where you define several targeting rules. [Learn how](optimization-targeting.md)

    ![](assets/msg-optimization-create-targeting.png){width=85%}

1. Create an experiment for the first targeting rule.

1. Design and configure your content experiment as wanted. [Learn how](../content-management/content-experiment.md)

    ![](assets/msg-optimization-targeting-with-experiment.png){width=85%}

    Once the experimentation is defined, it applies only to the first targeting rule.

1. Back in the **[!UICONTROL Actions]** tab, select **[!UICONTROL Edit content]**.

1. For the group defined by your first targeting rule, you can define a specific content for each variant of your experiment.

    If you added more than one inbound action to your journey or campaign, the same combination of targeting and experiment applies to each action. However, you need to define a specific content for each variant of each action.

    ![](assets/msg-optimization-targeting-experiment-design.png){width=85%}

1. Proceed similarly for the other targeting rules, and design the corresponding content for each variant.

1. Save your changes and [activate](review-activate-campaign.md) your journey or campaign.

Once the journey/campaign is live, users from each targeted group are randomly assigned the different content variations defined for the group they belong to.

<!--
## Reporting on Message optimization

E.g. explaining how a marketer can look at the report to determine which treatment (e.g. which message content) is performing the best for the targeting audience
-->

