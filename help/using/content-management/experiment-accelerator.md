---
solution: Journey Optimizer
product: journey optimizer
title: Experimentation Accelerator
description: Improve your capacity to conduct experiments effectively and generate insights
feature: Experimentation
topic: Content Management
role: User
level: Beginner
keywords: content, experiment, multiple, audience, treatment
hide: yes
hidefromtoc: yes
---
# Get started with the Experimentation Accelerator {#content-experiment}

>[!BEGINSHADEBOX]

* **[Get started with the Experimentation Accelerator](experiment-accelerator.md)**
* [Experiments tab](experiment-accelerator-monitor.md) 

>[!ENDSHADEBOX]

>[!AVAILABILITY]
>
> The Experimentation Accelerator is currently in beta, with features being rolled out progressively.

The **Experimentation Accelerator** is a powerful tool designed to streamline and enhance the experimentation process. By integrating with Adobe Target and Adobe Journey Optimizer, it provides a centralized platform for managing, analyzing, and optimizing experiments. Leveraging AI-driven insights and adaptive testing, the Experimentation Accelerator empowers you to make data-driven decisions, improve marketing strategies, and drive measurable results.

Key benefits include:

* **Faster Experimentation**: Run adaptive, always-on tests with models that adjust over time.

* **Unified Platform**: Manage all experiments from Adobe Target and Journey Optimizer in one place.

* **AI-Driven Insights**: Automatically surface key findings, performance drivers, and new opportunities.

* **Smarter Targeting**: Use behavioral and content data to prioritize high-impact experiments.

* **KPI Monitoring**: Track metrics like lift, revenue, and confidence across experiments.

* **Seamless Collaboration**: Share results easily and manage team roles with real-time alerts.

After [creating and configuring your experiment](content-experiment.md) and sending your campaigns or journeys to your profiles, you can access the **[!UICONTROL Experimentation Accelerator]** to dive deeper into how your experiment is performing.

To access the **[!UICONTROL Experimentation Accelerator]**:

* From the left-hand menu, select **[!UICONTROL Experimentation Accelerator]** in the **[!UICONTROL Experimentation]** drop-down.

* Alternatively, select **[!UICONTROL Experimentation Accelerator]** from the Apps switcher.

Note that users with only a Target license can access it only through the Apps switcher.

<!--
<table style="table-layout:fixed"><tr style="border: 0;">
<td><img alt="Overview" href="experiment-accelerator-overview.md" src="assets/do-not-localize/experiments-2.jpeg">
<div align="center"><p><strong><a href="experiment-accelerator-overview.md">Overview</a></strong></p></div></td>
<td><img alt="Experiments" href="experiment-accelerator-monitor.md" src="assets/do-not-localize/experiment-overview.jpeg">
<div align="center"><p><strong><a href="experiment-accelerator-monitor.md">Experiments</a></strong></p></div></td>
<td><img alt="Metrics" href="experiment-accelerator-metrics.md" src="assets/do-not-localize/experiment-metrics.png">
<div align="center"><p><strong><a href="experiment-accelerator-metrics.md">Metrics</a></strong></p></div></td>
</tr></table>
-->

## What Is A/B Testing?

A/B testing is the process of comparing two or more versions of something to determine which performs better against a defined goal.

Participants are randomly assigned to one version, known as a variant, and their behavior is tracked. The results show whether one version statistically outperforms the others.

## Key Terminology

|Term |Definition|
|-|-|
|Control|The original version used as a baseline for comparison.|
|Variant or Treatment|A new version created to test against the control.|
|Hypothesis|A prediction about what change will produce a better result, and why.|
|Sample Size|The number of individuals or sessions included in the test.|
|Statistical Significance| A measure of confidence that the results are not due to random chance.|
|Lift |The percentage improvement or decline of a variant compared to the control.|
|Primary Metric|The main measure used to determine the success of the test.|
|Secondary Metrics|Supporting metrics that offer additional insight or help monitor for unintended effects.|
|Confidence Interval|The estimated range within which the true effect is likely to fall.|
|Segment |A specific subset of the audience analyzed independently (e.g., new users, mobile visitors).|

## Best Practices for Running Experiments

* **Start with a clear hypothesis**

    A strong hypothesis includes what you're changing, what you expect to happen, and why.
    Example: _We believe that changing X will increase Y because of Z._

* **Define a meaningful success metric**

    Choose a metric that aligns with your broader goals. Avoid "vanity" metrics that look good but do not reflect real impact.

* **Test one change at a time (when possible)**

    Isolating variables makes it easier to interpret results accurately. If you test multiple changes at once, you may not know what caused the effect.

* **Let the test run long enough**

    Premature conclusions can be misleading. Wait for a statistically significant sample size before acting.

* **Be aware of external factors**

    Seasonality, holidays, and other changes in your environment can skew results. Document anything that might influence behavior during your test.

* **Use segmentation thoughtfully**

    Breaking down results by audience segment can reveal hidden patterns but avoid over-interpreting small sample sizes.

* **Document and share learnings**

    Keep a clear record of what was tested, why, and what you learned. This builds institutional knowledge and prevents repeat mistakes.

## Common Metrics and What They Indicate

|Metric | What It Measures | When to Use |
|-|-|-|
|Conversion Rate|The percentage of users who complete a desired action|Useful for tracking success of a goal-driven experience|
|Click-Through Rate (CTR)|The percentage of users who click on a specific element|Indicates how compelling the experience is|
|Engagement Rate|The level of interaction users have with the experience|Good for measuring interest or attention|
|Bounce Rate|The percentage of users who leave quickly without taking action|May signal a poor fit or confusing experience|
|Time on Page|The amount of time users spend on a specific part of the experience|Can reflect depth of interest or complexity|
|Revenue per Visitor (RPV)|Average revenue earned per user|Often used in commerce-focused experiments|
|Retention Rate|The percentage of users who return or remain engaged over time|Useful for long-term value assessments| 

## What Makes a Good Experiment?

A good experiment does not just produce a win, it produces a clear, actionable learning. 
Here is what to look for:

&check; **Statistical Confidence**: The difference between variants is unlikely to be due to chance.
&check; **Alignment with Goals**: The primary metric reflects meaningful progress toward a business objective.
&check; **Secondary Impact**: No significant negative side effects on related metrics.
&check; **Scalability**: The result can inform future decisions or be generalized to other areas.
&check; **Clarity**: The cause of the outcome is reasonably isolated and understood.

Experimentation is not just about finding the "best" version, it is about building knowledge through testing and iteration. When done well, experiments reveal insights that drive smarter decisions, better user experiences, and improved outcomes.

>[!BEGINSHADEBOX]

**Example:**

* **Company**: Hotel chain
* **Hypothesis**: If we use more urgent language on the home page, it will lead to more bookings.
    * **Control**: Original version
    * **Variant**: New version with urgency added
    * **Primary Metric**: Booking rate
    * **Secondary Metrics**: Bounce rate, time on site
* **Result**: The variant produced a 14% lift in booking rate, with no negative change in other metrics.
* **Action**: Consider rolling out the variant and running follow-up experiments to test similar approaches in other areas.

>[!ENDSHADEBOX]
