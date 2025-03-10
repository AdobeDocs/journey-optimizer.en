---
solution: Journey Optimizer
product: journey optimizer
title: Use the Test activity in your multi-step campaigns
description: Learn how to use the Test activity
hide: yes
hidefromtoc: yes
---
# Test {#test}

>[!CONTEXTUALHELP]
>id="ajo_orchestration_test"
>title="Test activity"
>abstract="The **Test** activity is a **Flow control** activity. It allows you to enable transitions based on specified conditions."

>[!CONTEXTUALHELP]
>id="ajo_orchestration_test_conditions"
>title="Conditions"
>abstract="The **Test** activity can have multiple output transitions. During multi-step campaign execution, each condition is tested sequentially until one of them is met. If none of the conditions are met, the multi-step campaign continues along the path of the **[!UICONTROL Default condition]**. If no default condition is activated, the multi-step campaign stops at this point."

The **Test** activity is a **Flow control** activity. It allows you to enable transitions based on specified conditions.

## Configure the Test activity {#test-configuration}

Follow these steps to configure the **Test** activity:

1. Add a **Test** activity to your multi-step campaign.

1. By default, the **[!UICONTROL Test]** activity presents a simple boolean test. If the condition defined in the "True" transition is met, this transition will be activated. Otherwise, a default "False" transition will be activated.

1. To configure the condition associated to a transition, click the **[!UICONTROL Open personalization dialog]** icon. Use the expression editor to define the rules required to activate this transition. You can also leverage event variables, conditions, and date/time functions. [Learn how to work with event variables and the expression editor](../event-variables.md)

    Additionally, you can modify the **[!UICONTROL Label]** field to personalize the transition's name on the multi-step campaign canvas.

    ![](../assets/workflow-test-default.png)

1. You can add multiple output transitions to a **[!UICONTROL Test]** activity. To do this, click the **[!UICONTROL Add condition]** button and configure the label and associated condition for each transition.
v
1. During multi-step campaign execution, each condition is tested sequentially until one of them is met. If none of the conditions are met, the multi-step campaigns continues along the path of the **[!UICONTROL Default condition]**. If no default condition is activated, the workflows stops at this point.

## Example {#example}

In this example, different transitions are activated based on the number of profiles targeted by a **[!UICONTROL Build audience]** activity:

* If more than 10,000 profiles are targeted, an email message is sent.
* For 1,000 to 10,000 profiles, an SMS is sent.
* If the targeted profiles fall below 1,000, they are directed to a "do not contact" transition.

![](../assets/workflow-test-example.png)

To do this, the `vars.recCount` event variable has been leveraged in the "email" and "sms" conditions to count the number of targeted profiles and activate the appropriate transition.

![](../assets/workflow-test-example-config.png)
