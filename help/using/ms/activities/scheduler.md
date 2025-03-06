---
solution: Journey Optimizer
product: journey optimizer
title: Use the Scheduler workflow activity
description: Learn how to use the Scheduler workflow activity
---
# Scheduler {#scheduler}


>[!CONTEXTUALHELP]
>id="acw_orchestration_scheduler"
>title="Scheduler activity"
>abstract="The **Scheduler** activity allows you to schedule when the workflow gets started. This activity should be considered as a scheduled start. It can only be used as the first activity of the workflow."


The **Scheduler** activity is a **Flow control** activity. It allows you to schedule when the workflow gets started. This activity should be considered as a scheduled start. It can only be used as the first activity of the workflow. 

## Best practices{#scheduler-best-practices}

* Do not schedule a workflow to run more than every 15 minutes as it may impede overall system performance and create blocks in the database.
* If you want to send a one-shot delivery in your workflow, you can add a scheduler activity and set it to run **Once**. You can also define the **Schedule** in the delivery's settings.
* If you want to send a recurring delivery in your workflow, you need to use a **Scheduler** activity and set the execution frequency. The recurring delivery activity does not allow you to define a schedule.

## Configure the Scheduler activity {#scheduler-configuration}

>[!CONTEXTUALHELP]
>id="acw_orchestration_schedule_validity"
>title="Scheduler validity"
>abstract="You can define a validity period for the scheduler. It can be permanent (default), or can be valid until a specific date."


>[!CONTEXTUALHELP]
>id="acw_orchestration_schedule_options"
>title="Scheduler options"
>abstract="Define the frequency of the scheduler. It can be executed at a specific moment, once or several times a day, week or month."

Follow these steps to configure the **Scheduler** activity:

![](../assets/workflow-scheduler.png)

1. Add a **Scheduler** activity to your workflow.

1. Configure the **Execution frequency**:

   * **Once**: the workflow is executed a single time.

   * **Daily**: the workflow is executed at a specific time, once a day.

   * **Several times a day:** the workflow is regularly executed several times a day. You can set up executions at specific times or periodically.

   * **Weekly**: the workflow is executed at a specified moment, once or several times a week.

   * **Monthly**: the workflow is executed at a specified moment, once or several times a month. You can select months, when you need the workflow to be executed. You can also set up executions on specified week days of the month, such as the second Tuesday of the month.

1. Define the execution details according to the frequency selected. The detail fields may vary depending on the frequency used (time, repetition frequency, specified days, etc.).

1. Click **Preview launch times** to check the schedule of the next ten executions of your workflow.

1. Define the validity period of the scheduler:

   * **Permanent (never expires)**: the workflow is executed, according to the frequency specified, without any limits to the time frame or number of iterations.

   * **Validity period**: the workflow is executed according to the frequency specified, up until a specific date. You need to specify start and end dates. 

>[!NOTE]
>
>If you want to start the workflow right away, you can click the **Execute pending task** in the scheduler's top action bar. This button is only available when you have started the workflow.

## Example{#scheduler-example}

In the following example, the activity is configured so that the workflow runs several times a day at 9 and 12 AM, every day of the week from October 1st, 2023 to January 1st, 2024.

![](../assets/workflow-scheduler2.png)
