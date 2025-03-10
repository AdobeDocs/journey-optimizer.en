---
solution: Journey Optimizer
product: journey optimizer
title: Use the Scheduler activity
description: Learn how to use the Scheduler activity in a multi-step campaign
hide: yes
hidefromtoc: yes
exl-id: da77a0bf-7b17-40fc-b2cb-2f0940152e64
---
# Scheduler {#scheduler}


>[!CONTEXTUALHELP]
>id="ajo_orchestration_scheduler"
>title="Scheduler activity"
>abstract="The **Scheduler** activity allows you to schedule when the multi-step campaign gets started. This activity should be considered as a scheduled start. It can only be used as the first activity of the multi-step campaign."


The **Scheduler** activity is a **Flow control** activity. It allows you to schedule when the multi-step campaign gets started. This activity should be considered as a scheduled start. It can only be used as the first activity of the multi-step campaign. 

## Best practices{#scheduler-best-practices}

* Do not schedule a multi-step campaign to run more than every 15 minutes as it may impede overall system performance and create blocks in the database.
* If you want to send a one-shot delivery in your multi-step campaign, you can add a scheduler activity and set it to run **Once**. You can also define the **Schedule** in the delivery's settings.
* If you want to send a recurring delivery in your multi-step campaign, you need to use a **Scheduler** activity and set the execution frequency. The recurring delivery activity does not allow you to define a schedule.

## Configure the Scheduler activity {#scheduler-configuration}

>[!CONTEXTUALHELP]
>id="ajo_orchestration_schedule_validity"
>title="Scheduler validity"
>abstract="You can define a validity period for the scheduler. It can be permanent (default), or can be valid until a specific date."


>[!CONTEXTUALHELP]
>id="ajo_orchestration_schedule_options"
>title="Scheduler options"
>abstract="Define the frequency of the scheduler. It can be executed at a specific moment, once or several times a day, week or month."

Follow these steps to configure the **Scheduler** activity:

![](../assets/workflow-scheduler.png)

1. Add a **Scheduler** activity to your multi-step campaign.

1. Configure the **Execution frequency**:

   * **Once**: the multi-step campaign is executed a single time.

   * **Daily**: the multi-step campaign is executed at a specific time, once a day.

   * **Several times a day:** the multi-step campaign is regularly executed several times a day. You can set up executions at specific times or periodically.

   * **Weekly**: the multi-step campaign is executed at a specified moment, once or several times a week.

   * **Monthly**: the multi-step campaign is executed at a specified moment, once or several times a month. You can select months, when you need the multi-step campaign to be executed. You can also set up executions on specified week days of the month, such as the second Tuesday of the month.

1. Define the execution details according to the frequency selected. The detail fields may vary depending on the frequency used (time, repetition frequency, specified days, etc.).

1. Click **Preview launch times** to check the schedule of the next ten executions of your multi-step campaign.

1. Define the validity period of the scheduler:

   * **Permanent (never expires)**: the multi-step campaign is executed, according to the frequency specified, without any limits to the time frame or number of iterations.

   * **Validity period**: the multi-step campaign is executed according to the frequency specified, up until a specific date. You need to specify start and end dates. 

>[!NOTE]
>
>If you want to start the multi-step campaign right away, you can click the **Execute pending task** in the scheduler's top action bar. This button is only available when you have started the multi-step campaign.

## Example{#scheduler-example}

In the following example, the activity is configured so that the multi-step campaign runs several times a day at 9 and 12 AM, every day of the week from October 1st, 2025 to January 1st, 2026.

![](../assets/workflow-scheduler2.png)
