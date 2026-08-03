---
solution: Journey Optimizer
product: journey optimizer
title: Path experimentation
description: Learn how to use path experimentation in journeys
feature: Journeys, Activities
topic: Content Management
role: User
level: Intermediate
keywords: experimentation, experiment, journey, path, optimization, A/B testing, multi-armed bandit, scale the winner
exl-id: 7241ade3-577c-4bb3-b0c3-017133871ca5
feature_v2: []
subfeature_v2: []
---
# Use path experimentation {#experimentation}

>[!BEGINSHADEBOX]

**On this page:** Learn how to set up path experimentation with the Optimize activity to test different journey paths using A/B or multi-armed bandit experiments, identify the best-performing treatment by success metric, and scale the winner.

>[!ENDSHADEBOX]

>[!CONTEXTUALHELP]
>id="ajo_path_experiment_success_metric"
>title="Success metric"
>abstract="Success metric is used to track and evaluate the best performing treatment in an experiment."
>additional-url="https://experienceleague.adobe.com/en/docs/journey-optimizer/using/orchestrate-journeys/create-journey/success-metrics" text="Configure and track your journey metrics"

Experimentation allows you to test different paths based on a random split to determine which performs best based on predefined success metrics.

To set up path experimentation in a journey, follow the steps below.

Let's say you want to compare three paths:

* one path with one email;
* a second path with a **[!UICONTROL Wait]** node of two days and an email;
* a third path with an email and then an SMS message.

1. From the **[!UICONTROL Orchestration]** section, drag and drop the **[!UICONTROL Optimize]** activity into the journey canvas.

1. Add an optional label, which can be useful to identify the activity in reporting and test mode logs.

1. Select **[!UICONTROL Experiment]** from the **[!UICONTROL Method]** drop-down list.

    ![Path experiment configuration panel](assets/journey-optimize-experiment.png){width=65%}

1. Click **[!UICONTROL Create experiment]**.

1. Select the **[!UICONTROL Success metric]** you want to set for your experiment. Learn more on the available metrics and how to configure the list in [this section](success-metrics.md).

    ![Primary and additional metrics selection for experiment](assets/journey-optimize-experiment-metrics.png){width=80%}

1. Select the **[!UICONTROL Experiment type]** for your path experiment:

    * **[!UICONTROL A/B experiment]** — Define the traffic split between treatments at the start of the test. Performance is evaluated based on your chosen primary metric; reporting shows the observed lift between treatments.

    * **[!UICONTROL Multi-armed bandit]** — Traffic split between treatments is handled automatically. Every 7 days, performance on the primary metric is reviewed, and weights are adjusted accordingly. Reporting continues to show lift, as for A/B tests.

    ![Experiment type dropdown in path experiment](assets/journey-path-experiment-type.png){width=80%}

    ➡️ [Learn more about the difference between A/B and Multi-armed bandit experiments](../content-management/mab-vs-ab.md)

1. You can choose to add a **[!UICONTROL Holdout]** group to your delivery. This group will not enter any path from this experiment. 

    >[!NOTE]
    >
    >Switching on the toggle bar will automatically take 10% of your population. You can adjust this percentage if needed.

1. You can allocate a precise percentage to each **[!UICONTROL Treatment]**, or simply switch on the **[!UICONTROL Distribute evenly]** toggle bar.

    ![Treatment allocation slider with percentage distribution](assets/journey-optimize-experiment-treatments.png){width=80%}

1. Enable the auto-scale experiment to automatically roll out the winning variation of your experiment. [Learn more on how to scale the winner](#scale-winner)

1. Click **[!UICONTROL Create]**.

1. Define the elements you want for each branch resulting from the Experiment, for example:

    * Drag and drop an [Email](../email/create-email.md) activity onto the first branch (**Treatment A**).

    * Drag and drop a [Wait](wait-activity.md) activity of two days onto the first branch, followed by an [Email](../email/create-email.md) activity (**Treatment B**).

    * Drag and drop an [Email](../email/create-email.md) activity onto the third branch, followed by an [SMS](../mobile/create-mobile-message.md) activity (**Treatment C**).

    ![Path experiment example with three treatment paths](assets/journey-optimize-experiment-ex.png){width=100%}

1. Optionally, use the **[!UICONTROL Add an alternative path in case of a timeout or an error]** to define a fallback action. [Learn more](using-the-journey-designer.md#paths)

1. [Publish](publish-journey.md) your journey.

Once the journey is live, users are randomly assigned to go down different paths. [!DNL Journey Optimizer] tracks which path performs best and provides actionable insights.

Follow the success of your journey with the Journey Path Experiment report. [Learn more](../reports/journey-global-report-cja-experimentation.md)

## Path assignment on journey re-entrance {#path-assignment}

Path assignment is persistent for a profile across multiple entrances into the same journey version. For example, if a profile enters a journey on day 1 and is assigned to path A and then re-enters the journey on day 2, it will again be assigned to path A. This ensures a consistent experience for the user and is required for statistically valid reporting and analysis.

However, the assignments are only persistent within a given journey version. Once you publish a new journey version, the randomization changes and a profile can end up getting assigned to a different path.

If you have multiple path experimentation activities in a journey, each activity applies an independent random assignment.

## Experiment use cases {#uc-experiment}

The following examples show how to use the **[!UICONTROL Optimize]** activity with the **[!UICONTROL Experiment]** method to determine which path works best overall.

+++Channel effectiveness

Test whether sending the first message by email versus SMS drives higher conversions.

➡️ Use the conversion rate as the success metric (for example: purchases, sign-ups).

![Channel effectiveness experiment comparing email versus SMS](assets/journey-optimize-experiment-uc-channel.png)

+++

+++Message frequency

Run an experiment to check if sending one email versus three emails over a week results in more purchases.

➡️ Use purchases or the unsubscribe rate as the success metric.

![Message frequency experiment testing one email versus three emails](assets/journey-optimize-experiment-uc-frequency.png)

+++

+++Wait time between communications

Compare a 24-hour wait versus a 72-hour wait before a follow-up to determine which timing maximizes engagement.

➡️ Use the click-through rate or revenue as the success metric.

![Wait time experiment comparing 24-hour versus 72-hour delays](assets/journey-optimize-experiment-uc-wait.png)

+++

## Scale the winner {#scale-winner}

>[!AVAILABILITY]
>
>For path experiments, the Scale the Winner feature is available only in unitary journeys (event-triggered and Audience qualifications).
>
>It is not available for Read audience journeys.

Scale the Winner enables you to automatically or manually roll out the winning variation of an experiment to your full audience. This feature ensures that, once a winner is determined, you can amplify its reach and effectiveness without constantly monitoring the experiment.

You can choose between two modes:

* **Auto-scaling**: Configure auto-scaling settings when creating your experiment by choosing the timing and conditions for scaling the winning treatment or a fallback option if no winner emerges.

* **Manual Scaling**: Manually review experiment results and initiate the rollout of the winning treatment, maintaining full control over timing and decisions.

### Auto-scaling {#autoscaling}

Auto-scaling lets you set predefined rules for when to roll out the winning treatment or a fallback—based on the experiment's results.

Note that once auto-scaling has occurred, manual scaling is no longer available.

To enable auto-scale in your experiments:

1. Set up your journey and configure your experiment as needed. [Learn more](#experimentation)

1. Enable the auto-scale option when setting up your experiment.

    ![Auto-scale option in path experiment](assets/journey-optimize-autoscale.png)

1. Select when the winner should be scaled:

    * As soon as winner is found.
    * After experiment is live for the selected time.
    
    The auto-scale time must be scheduled before the experiment's end date. If it is set for a time after the end date, a validation warning will appear, and the journey will not be published.

    ![Auto-scale time selection in path experiment](assets/journey-optimize-autoscale-time.png)

1. Choose the fallback behavior if no winner is found by scale time:

    * Continue experiment till its ends as scheduled.
    * Scale the alternative treatment after a specified time.

Once all parameters are met, your winning or alternative treatment is sent to your audience.

### Manual scaling {#manual-scaling}

Manual scaling gives you the ability to review experiment results and decide when to roll out the winning treatment on your own schedule.

Note that if you manually scale the winner before the scheduled auto-scale time, the auto-scale is canceled.

To manually scale the winner of your experiments:

1. Set up your journey and configure your experiment as needed. [Learn more](#experimentation)

1. Let the experiment run until a winner is identified or statistical significance is achieved.

1. Open your journey and select the **[!UICONTROL Optimize]** activity that contains the path experiment. 
    
    Review the results in the **[!UICONTROL Path experiment]** view to identify the top-performing treatment.

    ![Manual scale winner in path experiment](assets/journey-optimize-manual-scale-winner.png)

1. Click **[!UICONTROL Scale treatment]** to push the winning treatment to the rest of your audience.

    <!--![](assets/journey-optimize-scale-treatment.png)-->

1. Select the treatment you want to scale from the drop-down menu and click **[!UICONTROL Scale]**.

    ![Scale treatment selection in path experiment](assets/journey-optimize-scale-treatment.png){width=80%}

Note that scaling the treatment may take up to one hour. You will receive a notification once the manual scaling process is finished.

+++ AI Knowledge Reference

This section contains structured knowledge intended to support interpretation, retrieval, and question answering related to this topic.

For complete understanding, this information should be combined with the documentation on this page. Neither source is intended to stand alone; the page describes the feature, while this section provides additional context that helps disambiguate terminology, intent, applicability, and constraints.

* **TL;DR:** This page explains how to configure and run path experimentation in Adobe Journey Optimizer journeys using A/B or Multi-armed bandit methods, and how to scale the winning treatment automatically or manually.

**Intents:**
* Set up an A/B or Multi-armed bandit path experiment in a journey
* Define success metrics to evaluate experiment performance
* Allocate traffic between treatment paths evenly or by custom percentage
* Add a holdout group to exclude a portion of the audience from all treatments
* Enable auto-scaling to automatically roll out the winning treatment
* Manually scale the winning treatment after reviewing experiment results

**Glossary:**
* **Optimize activity**: A journey canvas activity used to split profiles into different paths for experimentation or targeting *(product-specific)*
* **Treatment**: A single path variant in a path experiment (e.g., Treatment A, Treatment B) *(product-specific)*
* **Success metric**: The KPI used to evaluate which treatment performs best in an experiment *(product-specific)*
* **Multi-armed bandit**: An experiment type where traffic split is adjusted automatically every 7 days based on primary metric performance *(product-specific)*
* **Scale the Winner**: A feature that rolls out the winning treatment to the full remaining audience, either automatically or manually *(product-specific)*
* **Holdout group**: A segment of the audience excluded from all experiment treatments, used as a control group *(product-specific)*

**Guardrails:**
* Scale the Winner is only available for unitary journeys (event-triggered and Audience Qualification); it is not available for Read Audience journeys.
* Auto-scale time must be scheduled before the experiment's end date, or the journey will not publish.
* Once auto-scaling has occurred, manual scaling is no longer available.
* Manual scaling the winner before the scheduled auto-scale time cancels the auto-scale.
* Scaling the treatment may take up to one hour.

**Terminology:**
* Canonical name: Path Experimentation — Acronym: none — variants: journey experimentation, A/B path test
* Synonyms: "Optimize activity" = "experiment activity" = "path split activity"
* Do not confuse: "A/B experiment" ≠ "Multi-armed bandit" (A/B has fixed traffic split; Multi-armed bandit adjusts weights dynamically every 7 days)

**FAQ:**
* **Q: What is the difference between A/B experiment and Multi-armed bandit?** — A/B experiment uses a fixed traffic split defined at the start, while Multi-armed bandit automatically adjusts traffic weights every 7 days based on the primary metric performance.
* **Q: Can I use Scale the Winner in a Read Audience journey?** — No; Scale the Winner is only available for unitary (event-triggered and Audience Qualification) journeys.
* **Q: What happens if no winner is found by the auto-scale time?** — You can configure a fallback: either continue the experiment until its scheduled end, or scale an alternative treatment after a specified time.
* **Q: How is traffic distributed if I do not configure treatment percentages manually?** — You can enable the Distribute evenly toggle to split traffic equally across all treatments.
* **Q: Can I edit a path experiment after the journey is published?** — The journey enters read-only mode after publishing; to make changes, create a new version of the journey.

+++
