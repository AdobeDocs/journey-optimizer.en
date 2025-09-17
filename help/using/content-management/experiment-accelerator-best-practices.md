---
solution: Journey Optimizer
product: journey optimizer
title: Journey Optimizer Experimentation Accelerator best practices
description: Improve your capacity to conduct experiments effectively and generate insights
feature: Experimentation
topic: Content Management
role: User
level: Beginner
keywords: content, experiment, multiple, audience, treatment
hide: yes
hidefromtoc: yes
---
# Journey Optimizer Experimentation Accelerator best practices {#content-experiment-best-practices}

>[!BEGINSHADEBOX]

* [Get started with the Journey Optimizer Experimentation Accelerator](experiment-accelerator.md)
* **[Journey Optimizer Experimentation Accelerator best practices](experiment-accelerator-best-practices.md)**
* [Privacy, Security, and Governance in Journey Optimizer Experimentation Accelerator](experiment-accelerator-security.md)
* [Monitor experiments](experiment-accelerator-monitor.md)
* [Experimentation metrics](experiment-accelerator-metrics.md)

>[!ENDSHADEBOX]

## What is A/B testing?

A/B testing is the process of comparing two or more versions of something to determine which performs better against a defined goal.

Participants are randomly assigned to one version, known as a variant, and their behavior is tracked. The results show whether one version statistically outperforms the others.

## Key terminology

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

## Best practices for running experiments

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

## Common metrics

|Metric | What It Measures | When to Use |
|-|-|-|
|Conversion Rate|The percentage of users who complete a desired action|Useful for tracking success of a goal-driven experience|
|Click-Through Rate (CTR)|The percentage of users who click on a specific element|Indicates how compelling the experience is|
|Engagement Rate|The level of interaction users have with the experience|Good for measuring interest or attention|
|Bounce Rate|The percentage of users who leave quickly without taking action|May signal a poor fit or confusing experience|
|Time on Page|The amount of time users spend on a specific part of the experience|Can reflect depth of interest or complexity|
|Revenue per Visitor (RPV)|Average revenue earned per user|Often used in commerce-focused experiments|
|Retention Rate|The percentage of users who return or remain engaged over time|Useful for long-term value assessments| 

## What makes a good experiment?

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
