---
solution: Journey Optimizer
product: journey optimizer
title: Campaign report
description: Learn how to use Experimentation data from the Campaign report
feature: Reporting
topic: Content Management
role: User
level: Intermediate
exl-id: 69742163-7378-49ab-929e-86213d6e65e3
TQID: https://experienceleague.adobe.com/m11Vxa3bSvaOHe1kFs5tU9oQS08lzcL0DSPyrABbXBI
product_v2:
  - id: cb954087-f4fc-4456-afb9-e939cabcdc79
    internal-label: Journey Optimizer
feature_v2:
  - id: a9f73820-6899-47c2-a597-3fec28ab756a
    internal-label: Reporting
  - id: b49ca41f-eb7a-4f4b-abeb-a97c06fd0c04
    internal-label: Track and monitor
subfeature_v2:
  - id: d145add9-d5b9-481b-aa8a-e15e6bb7f813
    internal-label: Performance monitoring
  - id: a7289281-9ae4-47b1-b8cf-4028b98af776
    internal-label: Deliverability
  - id: b5afe8bf-bda6-41b5-ba06-922638872d63
    internal-label: Metrics catalog
role_v2:
  - id: b69b2659-1057-424e-8fc5-ed9e016dc554
    internal-label: User
level_v2:
  - id: b5a62a22-46f7-4f0d-b151-3fc640bef588
    internal-label: Intermediate
topic_v2:
  - id: aa2f3246-cb95-4b30-8899-fdf7d73550cc
    internal-label: Reporting
  - id: bcc5edb5-84c3-4940-9f84-ed88b6c16274
    internal-label: Experimentation
  - id: e1e0219c-f879-479f-8427-888ed2a6e9c2
    internal-label: Insights
---
# Experimentation campaign report {#campaign-global-report-cja-experimentation}

>[!BEGINSHADEBOX]

**On this page:** Learn how to read the Experimentation campaign report in Adobe Journey Optimizer to compare variant performance using metrics such as lift, confidence, and conversion rate for your chosen success metric.

>[!ENDSHADEBOX]

>[!CONTEXTUALHELP]
>id="ajo_campaigns_content_experiment_click"
>title="Success metric"
>abstract="The total value of the Success metric, previously selected when creating your Experiments, divided by the number of profiles."

## Experimentation {#experimentation}

The **[!UICONTROL Experimentation]** tab provides key insights into the performance of each variant, and identifies the most successful one.

Note that defining the best performer might take some time. If your experiment is not successful, it will be set to **Inconclusive**.

![](assets/cja-experimentation-1.png)

### Experimentation KPIs {#experimentation-kpis}

![](assets/cja-experimentation-kpis.png)

The **[!UICONTROL Experimentation]** Key Performance Indicators (KPIs) function as an all-encompassing dashboard, delivering an analysis of essential metrics associated with your experimentation. 

+++ Learn more about Experimentation KPIs metrics

* **[!UICONTROL Lift]**: Measure of the percentage improvement in conversion rate of a given treatment over the baseline.

* **[!UICONTROL Confidence]**: Evidence that a given treatment is the same as the baseline treatment. [Learn more](../content-management/experiment-calculations.md#adobes-statistical-methodology-any-time-valid-confidence-sequences)

+++

### Variant by Success metric {#variant-inbound}

![](assets/cja-experimentation-variants.png)

The **Variant by success metrics** table shows how each variant performs based on the success metric selected when setting up the experiment.
For a deep-dive in these results and how to interpret them, refer to [this page](../content-management/get-started-experiment.md#interpret-results).

+++ Learn more about Variant by Success metric

* **[!UICONTROL People]**: Number of user profiles who qualify as target profiles for your messages.

* **[!UICONTROL Inbound Clicks]**: Total value of the Success metric, previously selected when creating your Experiments.

* **[!UICONTROL Conversion rate]**: Total value of the Success metric, previously selected when creating your Experiments, divided by the number of profiles.

* **[!UICONTROL Lift]**: Measure of the percentage improvement in conversion rate of a given treatment over the baseline.

* **[!UICONTROL Confidence Lower bound]**: Lowest estimated value of the conversion rate difference between the treatment and the baseline, within the chosen confidence interval.

* **[!UICONTROL Confidence]**: Evidence that a given treatment is the same as the baseline treatment. [Learn more](../content-management/experiment-calculations.md#adobes-statistical-methodology-any-time-valid-confidence-sequences)

* **[!UICONTROL Confidence Upper bound]**: Highest estimated value of the conversion rate difference between the treatment and the baseline, within the chosen confidence interval.

+++

### Conversion rate for Success metric {#conversion-rate}

![](assets/cja-experimentation-conversion.png)


The **[!UICONTROL Confidence interval]** graph shows the range of possible improvement, comparing the baseline with the best-performing treatment for the chosen success metric. [Learn more](../content-management/experiment-calculations.md#adobes-statistical-methodology-any-time-valid-confidence-sequences).