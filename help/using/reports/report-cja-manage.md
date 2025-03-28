---
solution: Journey Optimizer
product: journey optimizer
title: Reporting
description: Get started with Reporting 
feature: Reporting
topic: Content Management
role: User
level: Intermediate
exl-id: d2ff175a-8bca-4b62-931c-a909cfd9308d
---
# Manage your reports {#channel-cja-manage}

## Analyze in Customer Journey Analytics {#analyze}

>[!AVAILABILITY]
>
> The **Analyze in CJA** functionality is exclusively available to users with a [!DNL Customer Journey Analytics] license.

![](assets/cja-analyze.png)

Enhance your data analysis experience with your **[!DNL Customer Journey Analytics]** license by leveraging the **[!UICONTROL Analyze in CJA]** feature available in all reports.

This powerful option seamlessly redirects you to your **[!DNL Customer Journey Analytics]** environment, empowering you to personalize your reports extensively. You can enrich your widgets with specialized Customer Journey Analytics metrics, taking your insights to a whole new level.

[Learn more on the Customer Journey Analytics interface.](https://experienceleague.adobe.com/en/docs/analytics-platform/using/cja-overview/cja-getting-started)

## Define the report period {#report-period}

![](assets/cja-time-period.png)

When accessing a report, you can apply a time period filter, located at the top right corner of the report.

By default, the filter period for a campaign or journey is set to its start and end dates. If there is no end date, the filter will default to the current date.

To modify the filter, you can select a custom start date and duration, or choose from preset options such as last week or two months ago.

The report will automatically update once the filter is applied or modified.

## Export your reports {#export-reports}

You can easily export your different reports to PDF or CSV formats, which enables you to share or print them. Steps to export reports are detailed in the tabs below.

>[!BEGINTABS]

>[!TAB Export your report as a CSV file]

1. From your report, click **[!UICONTROL Share]** and select **[!UICONTROL Download CSV]** to generate a CSV file at overall report-level. 

   ![](assets/export_cja_csv.png)

1. Your file is automatically downloaded and can be located in your local files.

    If you generated the file at the report level, it contains detailed information for each widget, including its title and data.

>[!TAB Export your report as a PDF file]

1. From your report, click **[!UICONTROL Share]** and select **[!UICONTROL Downalod PDF]**.

   ![](assets/export_cja_pdf.png)

1. After download has been requested, click **[!UICONTROL Download]**.

   ![](assets/export_cja_pdf_2.png)

1. Your file will automatically open in your browser.

Your report is now available to view, download or share in a pdf file.

>[!ENDTABS]


## Schedule exports {#schedule-export}

The **Schedule export** lets you automate the delivery of up to 10 reports at weekly, monthly or yearly intervals. You can also easily manage your scheduled reports, with options to update, edit, cancel, or delete any of your scheduled exports.

1. From your report, click **[!UICONTROL Share]** and select **[!UICONTROL Schedule export]**.

   ![](assets/export-schedule-1.png)

1. Choose your **[!UICONTROL File type]** between CSV and PDF.

1. If needed, you can add a **[!UICONTROL Description]** to your export.

1. Enter the name of the recipients who will receive this automated delivery.

   ![](assets/export-schedule-2.png)

1. Choose the **[!UICONTROL Frequency]**.

1. Based on the selected frequency, provide the relevant scheduling details, such as:

   * Start and end dates
   
   * Interval (e.g., every few weeks)

   * Specific day of the week
   
   * Week within the month

   * Day within the month
   
   * Month of the year

1. Click **[!UICONTROL Send on schedule]**.

1. To edit previously created scheduled export, click **[!UICONTROL Share]** and select **[!UICONTROL Manage schedules]**.

   ![](assets/export-schedule-3.png)

1. From the list of scheduled exports, choose the one you want to update and make the necessary changes.

1. To delete a scheduled report, select one from the managed schedules list and click **[!UICONTROL Delete]**.

   ![](assets/export-schedule-4.png)


## Create a simple metric {#create-simple-metric}

You can create custom calculated metrics directly within your reports. You can generate more tailored insights and better analyze your data by combining two existing metrics in ways that suit your specific reporting needs.

1. Start by accessing the report where you want to add a new metric.

1. In the table within your report, select the metrics you want by holding down the `Shift` or `CTRL/CMD` keys while clicking on them. Then, right-click and select **[!UICONTROL Create metric from selection]**.

   If you select more than two metrics, only the first two will be used in the metric builder.

   ![](assets/cja-create-metric_2.png)

1. From the Calculated metric builder, name your new metric by typing in the **[!UICONTROL Title]** field. You can also add a **[!UICONTROL Description]**.
   
   >[!NOTE]
   >
   >If you own Customer Journey Analytics, you can further personalize your metrics with additional options. [Learn more](https://experienceleague.adobe.com/en/docs/analytics-platform/using/cja-components/cja-calcmetrics/cm-workflow/cm-build-metrics#areas-of-the-calculated-metrics-builder)

1. Choose the appropriate **[!UICONTROL Decimal Places]** and select a **[!UICONTROL Format]** (Decimal, Time, Percent, or Currency) based on how you want your metric to be displayed. 

1. Select the operator, such as addition, subtraction, multiplication, or division, that will determine how the metric is calculated.

   ![](assets/cja-create-metric.png)

1. You can reorder the components if needed.

1. When you're satisfied with your settings, click **[!UICONTROL Apply]** to finalize your new metric.

1. Your new metric will appear next to the original metrics in your report.

   ![](assets/cja-create-metric_3.png)

Your newly created metric will be included when you export the report as a PDF or CSV. However, it will be removed from the report once you exit it.

## Explore data with the Exploratory Analysis {#exploratory}

Use the Exploratory Analysis tool to easily create tables and visualizations from your selected **[!UICONTROL Dimensions]** and **[!UICONTROL Metrics]**. This tool streamlines data exploration, allowing you to automatically customize and analyze information with ease. Learn more in [this documentation](https://experienceleague.adobe.com/en/docs/analytics/analyze/analysis-workspace/panels/quickinsight).

1. Start by accessing the report where you want to use the Exploratory Analysis.

1. Select the Exploratory Analysis menu from the left-rail menu.

   ![](assets/exploratory_analysis_1.png)

1. Build a query by choosing a **[!UICONTROL Dimension]** and a **[!UICONTROL Metric]** using the drop-down menus. You can also select a **[!UICONTROL Segment]** if needed.

   ![](assets/exploratory_analysis_2.png)

1. Define the date range for your analysis to specify the period you wish to focus on. By default, the date range will be set to the one used in the report panel.

1. Use the **[!UICONTROL Add breakdown]** or **[!UICONTROL Add metric]** options to include additional dimensions, allowing for a more detailed data breakdown.

    Note that you can only add up to three **[!UICONTROL Dimensions]**, **[!UICONTROL Metrics]** and **[!UICONTROL Segments]**.

You can now analyze your data using your customized table and visualization tools.

<!--## Create a down-funnel metric {#down-funnel}

1. Create a new journey or open an existing one. [Learn more on journey creation](../building-journeys/journey-gs.md)

1. On the canvas editor, select the option to "add a metric".

c. In the metric selector, choose whichever conversion metric seems appropriate and publish your journey

d. Open the report for the journey that you added the metric to and ensure that the metric has been added to the table alongside all the other pre-configured metrics.
-->

## Create an Audience from reporting data {#create-audience}

>[!IMPORTANT]
>
>Each organization is limited to publishing 25 audiences. Additionally, users can publish a maximum of 5 audiences per hour and 20 per day.
> One-time audiences have a lifespan of 48 hours. Therefore, if 25 audiences are published within that timeframe, additional audiences can only be published once the 48-hour period has elapsed.

You can now select specific data within the table and directly create an audience from these selections, streamlining and simplifying the audience creation process.

1. Begin by navigating to the report table that contains the data you wish to transform into an audience.

1. Right-click on the desired cell and select **[!UICONTROL Create audience]**.

   Alternatively, you can start audience creation from the **[!UICONTROL Journey canvas]** widget by selecting a node and right-clicking it.

1. In the **[!UICONTROL Create audience]** window, enter a **[!UICONTROL Name]** and set a **[!UICONTROL One-time date range]** for the audience you plan to publish.

   >[!NOTE]
   >
   >If you own Customer Journey Analytics, you can further personalize your metrics with additional options. [Learn more](https://experienceleague.adobe.com/en/docs/analytics-platform/using/cja-components/audiences/publish)
   
   ![](assets/audience_1.png)

1. Click the **[!UICONTROL Create]** button to finalize the audience creation. Note that this process may require some time to complete.

You can now proceed to use the newly created audience with a Journey or Campaign.

## Manage templates {#cja-template}

>[!AVAILABILITY]
>
> The **Template** functionality is progressively rolled out in phases, with full General Availability planned by the end of January, and exclusively available to users with a [!DNL Customer Journey Analytics] license. 

You now have the option to enhance your Journey Optimizer reports by leveraging Customer Journey Analytics templates. [Learn more on Customer Journey Analytics template](https://experienceleague.adobe.com/en/docs/analytics-platform/using/cja-workspace/templates/use-templates#use-reports)

When accessing your reports, you can choose between two template types from the **[!UICONTROL Select a template]** dropdown:

* Adobe-provided default template 
* Customer-generated templates

![](assets/cja_template_5.png)

If no template has been created, the **[!UICONTROL Select a template]** dropdown does not appear in your reporting interface. 

To create a template, follow the steps below:

1. In [!DNL Customer Journey Analytics], navigate to the **[!UICONTROL Workspace]** menu and select **[!UICONTROL Adobe templates]**. [Learn more about the available templates](https://experienceleague.adobe.com/en/docs/analytics-platform/using/cja-workspace/templates/use-templates#available-templates)

1. Browse the available pre-built templates and click **[!UICONTROL Use template]** to select one.

   ![](assets/cja_template_1.png)

1. Adjust your report to meet your needs. Refer to [Customer Journey Analytics documentation](https://experienceleague.adobe.com/en/docs/analytics-platform/using/cja-workspace/home).

1. Once your custom template is complete, access the **[!UICONTROL Project]** menu and select **[!UICONTROL Save as template]**.

   ![](assets/cja_template_2.png)

1. Provide the necessary details for your template. Refer to [Customer Journey Analytics documentation](https://experienceleague.adobe.com/en/docs/analytics-platform/using/cja-workspace/templates/create-templates#edit-or-delete-a-template) for the detailed information.

   >[!IMPORTANT]
   >
   > Make sure to choose **Journey Optimizer** under **[!UICONTROL Use cases]** and specify the corresponding **Journey Optimizer activity type** and **activity**. This enables your report to appear in Journey Optimizer.

   ![](assets/cja_template_3.png)

1. In [!DNL Journey Optimizer], from your report, access your report and choose your previously created template from the **[!UICONTROL Select a template]** dropdown.

   ![](assets/cja_template_4.png)

To directly create a template from your Journey optimizer report, simply access your campaign or journey report, select **[!UICONTROL Analyze in CJA]** and customize the default template by following the steps outlined above.
