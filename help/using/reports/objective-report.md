---
solution: Journey Optimizer
product: journey optimizer
title: Campaign Global report
description: Learn how to use data from the Campaign Global report
feature: Reporting
topic: Content Management
role: User
level: Intermediate
hide: yes
hidefromtoc: yes
exl-id: ec1af88c-7b0a-4eaf-97e1-0d9676268fed
badge: label="Beta" type="Informative"
---
# Campaign global report {#objective-report}

Campaign global report can be accessed directly from your Campaign with the **[!UICONTROL View report]** button.

The Campaign **[!UICONTROL Global report]** is divided into different widgets detailing your campaign's success and errors. Each widget can be resized and deleted if needed. For more information on this, refer to this [section](../reports/global-report.md#modify-dashboard).

For a detailed list of every metric available in Adobe Journey Optimizer, refer to [this page](global-report.md#list-of-components-global.md)

## Campaign tab {#campaign-global-objectives}

### Delivery {#delivery-global-objectives}

![](assets/campaign_report_global_1.png)

The **[!UICONTROL Campaign's Statistics]** widget details the main information relative to your campaign:

* **[!UICONTROL Entered profiles]**: Number of profiles who started the journey.

* **[!UICONTROL Actions delivered]**: Total number of unique times an action in the journey has been delivered.

* **[!UICONTROL Actions failed in %]**: Total number of unique times an action failed in the journey compared to the total number of unique times an action has been delivered.

### Objectives report {#objective-global}

>[!AVAILABILITY]
>
>The **Objectives report** feature is currently only available for a set of organizations (Limited Availability). For more information, contact your Adobe representative.

![](assets/performance_report.gif)

The **[!UICONTROL Objectives]** tab allows you to better fine-tune your deliveries' reports by targeting one specific metric.

The **[!UICONTROL Objectives]** listed are linked to **[!UICONTROL Datasets]** that define a connection to a system in order to retrieve additional information. A list of built-in **[!UICONTROL Objectives]** is available but you can add your own by adding new **[!UICONTROL Dataset]**. For the detailed procedure, refer to this [section](../content-management/reporting-configuration.md).

After selecting the Objectives you want to target on, the two **[!UICONTROL Performance overview]** and **[!UICONTROL Campaign objective]** widgets will provide a detailed summary of your delivery performance. 

With the **[!UICONTROL Campaign objective]** widget, you can also choose to compare your main objective with another metric.

### Experimentation report {#experimentation-global-objectives}

![](assets/experimentation_report_3.png)

The **[!UICONTROL Experimentation]** tab provides key insights into the performance of each variant, and identifies the most successful one.

Note that defining the best performer might take some time, it will be represented by this icon ![](assets/experimentation_report_1.png).

+++Learn more on the different metrics and widgets available for the Experimentation report.

The **[!UICONTROL Experiment result]** widget details the performance of each variant. You can change your baseline by selecting one of the treatment from the **[!UICONTROL Baseline]** the drop-down. The best treatment will be represented with a star icon.

The table presents the following metrics:

* **[!UICONTROL Lift over baseline]**: Measure of the percentage improvement in conversion rate of a given treatment over the baseline.

* **[!UICONTROL Confidence]**: Evidence that a given treatment is the same as the baseline treatment. [Learn more](../content-management/experiment-calculations.md#understand-confidence)

* **[!UICONTROL Unique outbound clicks]**: Total count of clicks across outbound channels.

* **[!UICONTROL Profiles]**: Number of profiles targeted for this treatment.

* **[!UICONTROL Unique outbound clicks/profiles]**: Total value of the Success metric, previously selected when creating your Experiments, divided by the number of profiles.

The **[!UICONTROL Confidence interval]** graph measures uncertainty around improvement. It details the percentage difference in performance between the baseline and the best performing treatment. [Learn more](../content-management/experiment-calculations.md#confidence-intervals). 
+++

For a deep-dive in these results and how to interpret them, refer to [this page](../content-management/get-started-experiment.md#interpret-results).
