---
solution: Journey Optimizer
product: journey optimizer
title: Use the External signal activity in a multi-step campaign
description: Learn how to use the External signal activity in a multi-step campaign
---
# External signal {#external-signal}

<!--External Signal End-->

>[!CONTEXTUALHELP]
>id="acw_orchestration_externalsignal"
>title="External Signal"
>abstract="The **External signal** activity lets you trigger the execution of a multi-step campaign from another multi-step campaign or an API call."

>[!CONTEXTUALHELP]
>id="acw_orchestration_externalsignal_parameters"
>title="External Signal Parameters"
>abstract="External Signal Parameters"

>[!CONTEXTUALHELP]
>id="acw_orchestration_end_trigger"
>title="End triggers"
>abstract="End triggers"

The **External signal** activity is a **Flow control** activity. It allows you to trigger the execution of a multi-step campaign from another multi-step campaign or from an API call.


Follow these steps to configure the **External signal** activity and trigger its execution:

1. Add an **External signal** activity into your multi-step campaign.

1. Complete the configuration of your multi-step campaign and start its execution. The **[!UICONTROL External Signal]** activity displays as "Pending", waiting to be triggered.

    ![](../assets/external-signal-pending.png)

1. Retrieve the information below:

    * The **internal name**, which displays next to its label.

        +++View example

        ![](../assets/external-signal-workflow-name.png)

        +++

    * The **External signal activity's name**, which displays in the multi-step campaign's **[!UICONTROL Execution options]**.

        +++View example

        ![](../assets/external-signal-name.png)

        +++

1. To trigger the multi-step campaign, you need to execute the `PostEvent` JavaScript function. This function allows you to pass variables with the values of your choice and leverage them in the triggered multi-step campaign.

    The `PostEvent` function can be executed either from another multi-step campaign, or from an API call.

    * To trigger an **[!UICONTROL External signal]** activity from a multi-step campaign, execute the PostEvent function from the **[!UICONTROL Initialization script]** pane, which is accessible from the activity's **[!UICONTROL Execution options]**. For the **[!UICONTROL JavaScript code]** activity, execute the function from the activity's script.

        The syntax is as follows:

        ```

        xtk.workflow.PostEvent("<workflow-internal-name>","<signal-activity-name>","",<variables <variable-name>="<value>"/>, false);

        ```

    +++View example

    In this example, we are triggering the "signal1" External signal activity that has been added to the multi-step campaign whose internal name is "WKF12345". We are also passing a variable named "customID", with the value "123456".

    ![](../assets/external-signal-sample.png)

    +++

    * To trigger an **[!UICONTROL External signal]** activity from an API call, follow the steps detailed in the Campaign API documentation. [Learn how to use the static `PostEvent` method](https://experienceleague.adobe.com/developer/campaign-api/api/sm-workflow-PostEvent.html)
