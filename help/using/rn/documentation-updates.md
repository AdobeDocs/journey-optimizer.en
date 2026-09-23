---
solution: Journey Optimizer
product: journey optimizer
title: Documentation Updates
description: Learn about the latest documentation updates for Adobe Journey Optimizer, including new pages, reorganizations, and clarifications.
keywords: documentation updates, release notes, journey optimizer, changelog
feature: Release Notes
topic: Content Management
role: User
level: Beginner, Intermediate
exl-id: 83c8f206-bce3-4cc8-94a3-575ec1d999bc
feature_v2:
  - id: bb359667-ec7d-4d4b-8663-5850fc219d32
    internal-label: Administration
subfeature_v2:
  - id: a7b2bfc5-be71-4740-b371-76fa6be8df02
    internal-label: Journey Optimizer release notes
---

# Documentation updates {#latest-updates}

This page lists all the latest changes in [!DNL Journey Optimizer] documentation, in addition to the updates related to the Monthly release features and improvements.

## September 2026 {#september-2026}

* The `inAudience` guardrails now include the workaround for sandboxes with more than 5,000 audiences, where older audiences can be rejected during journey authoring because validation checks only the 5,000 most recently updated audiences. [Read more](../building-journeys/functions/functioninaudience.md#guardrails)

* Guidance for email mirror pages has been expanded: the documentation now explains that mirror page URLs cannot be retrieved through a public API or dataset, recommends Message Export or BCC archiving for retaining sent content, and clarifies that mirror page links are inactive in proofs and simulations. [Read more](../email/message-tracking.md#mirror-page)

* A new **Interactive demo** page is now available for Loyalty Challenges, linking to a self-guided, clickable demo that covers the marketer's challenge creation flow (including Bring your own data and the insights dashboards), the end customer experience, and Loyalty Challenge Management in CX Coworker. [Read more](../loyalty-challenges/loyalty-challenges-demo.md)

* The **Personalize your email background** page has been expanded and improved. It now documents the full **Image placement** dropdown for background images and adds new best practices for background colors and images, including a recommendation to test background images across real email clients rather than relying solely on the Email Designer preview. [Read more](../email/backgrounds.md)

* The **Design content from scratch with the Email Designer** page has been reorganized and clarified: it distinguishes the **[!UICONTROL n:n column]** structure from the fixed-preset structures, documents that a structure's column count can be increased without losing existing content, explains column-stacking behavior on mobile, and adds a new step on using **[!UICONTROL Modules]** to quick-start email creation. [Read more](../email/content-from-scratch.md)

* The **Design your journey** page now includes a full tutorial section on the new canvas experience, covering how to add activities, use the toolbar icons, select multiple activities for bulk actions, copy and paste activities, and join or detach branches. [Read more](../building-journeys/using-the-journey-designer.md#canvas-capabilities)

* New guidance has been added for verifying custom action delivery: the **Dataset query examples** page now explains how to choose between the Message Feedback Event, Email Tracking, and Journey Step Event datasets depending on the action type, and documents how to resolve a "Table not provisioned for dataset" error. The **Journey step events overview** and **Troubleshoot your live journey execution** pages have been updated accordingly, clarifying that a successful custom action call only confirms that Journey Optimizer executed the action, not that the external system delivered a message. [Read more](../data/datasets-query-examples.md#choose-the-correct-dataset)

* Information about CX Coworker has been added to the **Work with AI** page, covering what CX Coworker is, how it relates to AI Assistant, and references to the official Coworker documentation. Dedicated skills pages have also been added to each capability guide — [CX Coworker skills for journeys](../building-journeys/journeys-coworker-skills.md), [CX Coworker skills for loyalty](../loyalty-challenges/loyalty-coworker-skills.md), and [CX Coworker content management tools](../content-management/content-management-coworker-skills.md). [Read more](../start/ai-features.md#cx-coworker)

* A new **Analyze Journey Anomalies** skill has been documented under **Journey Analyze** in the CX Coworker page. It detects unexpected spikes, drops, or flatlines in a journey's entry, exit, or send counts against historical baselines, and runs read-only diagnostics to surface a likely root cause. [Read more](../building-journeys/journeys-coworker-skills.md#journey-analyze)

* The **Guardrails and limitations** and **Journey properties** pages have been updated to document the default journey payload limit as **2 MB (2,000,000 bytes)**, clarify that the value reflects the serialized journey definition rather than activity count alone, and explain the 90% warning and 100% blocking thresholds. [Read more](../start/guardrails.md#journey-payload-size) and [learn more](../building-journeys/journey-properties.md#journey-payload-size)

* The **Guardrails and limitations** page has been corrected to reflect the fact that visual fragments over 100 KB or expression fragments over 200 KB can no longer cause truncation issues in email delivery: now a single 700 KB fragment size guardrail applies. [Read more](../start/guardrails.md#fragments-guardrails)

* The **Create a Live activity** page has been corrected: the `executionMetadata` field is available only for **API-triggered Transactional** campaigns, not for API-triggered Marketing campaigns as previously stated. [Read more](../mobile-live/create-mobile-live.md#metadata)

* The **AJO Message Feedback Event Dataset** documentation has been expanded to clarify that it covers message delivery feedback across all channels (Email, SMS/RCS/MMS, Direct Mail), not just email and push, and now includes a **Classify test and non-test executions** section explaining how to interpret the `isTestExecution` field, including `NULL` or missing values. [Read more](../data/datasets-query-examples.md#classify-test-executions)

* A new **Content Management** capability has been documented for CX Coworker, powered by 15 read/write MCP tools that let you discover, create, update, clone, and publish content templates, fragments, landing pages, and journey/campaign inline message content using natural language prompts. [Read more](../content-management/content-management-coworker-skills.md#content-management)

* The **Add content to your landing page** documentation now describes a **Make form field mandatory** option for consent checkboxes: when enabled, the form cannot be submitted unless the checkbox is selected, and the check is enforced both client-side and server-side. [Read more](../landing-pages/lp-content.md#use-form-component)

* The **Get started with Journey Simulation** page has been updated to document that Content Decision nodes and the **Optimize** activity's Targeting rule method are now supported in Simulation (previously listed as blocking), with a new **Decisioning behavior** table detailing how offer eligibility, eligibility rules and audiences, and ranking methods are evaluated during a simulation run. [Read more](../building-journeys/simulate-journey-gs.md#limitations)

* The **Convert images to email content templates** page has been corrected to remove an inaccurate permissions requirement: the **Manage content templates** permission is not required to access and create templates with the image to HTML converter — only the **Generate Content** permission is needed. [Read more](../content-management/image-to-html.md#access-image-to-html)

* The **External systems (custom actions)** page has been corrected: the circuit breaker for slow custom action endpoints now activates when more than 20% of calls in a 120-second window exceed **5 seconds** (previously documented as 10 seconds). [Read more](../configuration/external-systems.md#response-time)

* The **Configure your Channel configuration** page now includes a note clarifying that the schema used for secondary dimension must have a primary key, and that composite primary keys are not supported. [Read more](../orchestrated/channel-config.md)

* The **Loyalty data and datasets** and **Get started with sources** pages have been updated to include LAVA as a supported loyalty and rewards connector, alongside Talon.One, Capillary, and Kobie. [Read more](../loyalty-challenges/loyalty-data-and-datasets.md)

## August 2026 {#august-2026}

* The **Add visual fragments to your emails** page now clarifies that a fragment with dynamic content and an empty default state appears blank in the Email Designer — simulate with a matching profile to preview the content. [Read more](../email/use-visual-fragments.md#fragment-dynamic-content)

* The **Track your messages** page has been updated to clarify that unsupported URL characters (e.g., apostrophes) must be percent-encoded, and that leaving them unencoded can break tracked links and URL tracking parameters. [Read more](../email/message-tracking.md#insert-links)

* The **Send using waves** page has been updated to document that the last wave in a read-audience journey must be scheduled within **6 days and 18 hours** of the journey start. Exceeding this window triggers a validation error and prevents the journey from entering test mode or going live. [Read more](../delivery/send-using-waves.md#limitations-guardrails)

* A new **Suppress feedback events** section has been added to the **Decision management data collection** page, documenting how to use the `dryRun` flag to suppress decision events during testing and prevent feedback from being captured for reporting and frequency capping counters. [Read more](../offers/data-collection/data-collection.md#suppress-feedback)

* A new **Choose a validation method** page is now available. It compares Journey Simulation, Test mode, and Journey Dry run — the data each uses, whether it sends real messages, common mistakes to avoid, and a decision guide for picking the right method at each stage of building a journey. [Read more](../building-journeys/choose-validation-method.md)

* The **Guardrails and limitations** page has been updated to clarify the Audience Qualification activity and Events guardrails: wording now consistently refers to Audience Qualification **activities** (rather than nodes), including when used as exit criteria, and both guardrails now explicitly cover **live, closed, paused, test mode, and dry run** journeys. [Read more](../start/guardrails.md#audience-qualif-g)

* A note has been added to the **Test HTML size optimization** section to clarify that proof sizes reflect the HTML template size (Handlebars at minimum value), not the final delivered email size, which may be larger once dynamic expressions are resolved at delivery time. [Read more](../email/create-email.md#optimize-html-proof)

* A new **Mobile web browser limitations** section has been added to the **Get started with email design** page, documenting why emails may render differently in Gmail or Outlook when accessed via a mobile browser, along with a workaround tip. [Read more](../email/get-started-email-design.md#mobile-web-limitations)

* A new **Outlook rendering considerations** section has been added to the **Get started with email design** page, listing common Outlook quirks to account for during design: even numbers for padding and widths, pixel-based table widths, HTML image width attributes, ALT text, borders on table cells, and rounded corners. [Read more](../email/get-started-email-design.md#outlook-tips)

* The **Datasets Time-to-live (TTL) guardrails** page has been updated with a significantly expanded **Impacted datasets** table, now covering all Journey Optimizer system-generated datasets (including several not previously listed, such as the AJO Consent Service, Interactive Messaging Profile, Push Profile, and Message Export datasets) along with a new **Availability** column indicating whether each dataset is included by default or requires a specific add-on or license. The **Guardrails and limitations** page has also been updated to reflect the confirmed enforcement date for this guardrail: the change will be enforced on **existing customer sandboxes** starting **October 1, 2026**. [Read more](../data/datasets-ttl.md#datasets)

* A new **Use Image settings mode** section has been added to the generative content documentation. It explains the **Balanced**, **DAM**, and **Creative** modes available under **[!UICONTROL Image settings]**, which control whether AI-generated content sources images from your Digital Asset Management library, generates them with AI, or blends both. [Read more](../content-management/generative-uc.md#image-mode)

* The **Destinations** description under **Left navigation > Main sections** has been updated to note that organizations with [!DNL Real-Time CDP] or [!DNL Adobe Journey Optimizer] can also activate audiences to eligible personalization destinations, such as [!DNL Adobe Target], from the Experience Platform destinations catalog. [Read more](../start/user-interface.md#main-sections)

* How-to videos have been added to the Loyalty Challenges documentation for creating challenges, setting up reward providers, and monitoring challenge performance. [Watch the challenge videos](../loyalty-challenges/create-challenges.md#video), [watch the reward provider video](../loyalty-challenges/reward-definition-guide.md#video), and [watch the reporting video](../loyalty-challenges/loyalty-reporting.md#video).

## July 2026 {#july-2026} 

* A new **Delivery settings** section has been added to the documentation navigation. It groups delivery-related features that apply across journeys, campaigns, and orchestrated campaigns: **Send using waves**, **Send-Time optimization**, and **Channel optimization** have all been moved there from the Journeys section.

* The separate **Send using waves** documentation pages for journeys and action campaigns have been merged into a single page, now also covering orchestrated campaigns. [Read more](../delivery/send-using-waves.md)

* A tip pointing to the Experience League community article on **how to detach and rejoin nodes** in the new journey canvas has been added to the **Design your journey** page. [Read more](../building-journeys/using-the-journey-designer.md)

* The **Grid** component section has been added to the **Email Designer content components** page. It lets you organize content into a structured grid of rows and columns, where each cell can contain other content components. [Read more](../email/content-components.md#grid)

* The **Decisioning Migration API** documentation has been updated with a clarification that the target sandbox **can be the same as the source sandbox**. The migration process handles this scenario and ensures data integrity regardless of whether objects are migrated within the same sandbox or to a different one. [Read more](../experience-decisioning/decisioning-migration-api.md#target-sandbox-preparation)

* The **Decisioning Migration API** documentation has been enhanced with comprehensive guidance on migrating Decision management objects to Decisioning. New sections include: entity mapping reference with 10 naming conventions, in-scope vs. out-of-scope coverage, detailed request/response model comparisons, three implementation patterns (client-side, server-side, hybrid) with cookie handling, event tracking requirements with 5 event JSON examples, cross-sandbox migration prerequisites, an end-to-end 5-step migration process, and migration FAQs. [Read more](../experience-decisioning/decisioning-migration-api.md)

* A new **CX Coworker Skills** page is now available. It provides comprehensive documentation of all Journey Skills available in Journey Optimizer, including Journey Create, Channel Content Create, Loyalty Challenge Management, and Journey Analyze, with use cases, sample prompts, and best practices for each skill. [Read more](../start/ai-features.md#cx-coworker)

* The **To Precision** function documentation has been updated to clarify that `toPrecision` behaves like JavaScript `toFixed()`: it returns a string with a fixed number of decimal places, including zero-padding when needed. [Read more](../personalization/functions/math.md#to-precision)

* The **End a journey** page has been updated to clarify automatic stop timing for non-recurring Read Audience journeys: a safety buffer of approximately **96 hours (~4 days)** after the scheduled run (24-hour idle window + 72-hour Quiet Hours allowance), during which the journey can remain in **Live** status before transitioning to **Stopped** shortly after the buffer elapses. The page now also clarifies that waves-based (multi-wave) journeys, and journeys that use Send-Time Optimization, are excluded from this auto-stop and instead follow the standard 91-day journey timeout. [Read more](../building-journeys/end-journey.md#auto-stop-non-recurring)

* The **Create IP warmup campaigns** page has been updated to clarify that targeting rules can be applied to IP warmup campaigns, and to document the evaluation behavior: audience membership is fixed at run activation (daily batch segmentation), while profile attributes are read at run execution time from the most recently ingested batch data. [Read more](../configuration/ip-warmup-campaign.md)

* A warning has been added to the **Edit PTR records** page to inform customers that when adding a new forward DNS record to their platform, the forward DNS record for the old subdomain must not be removed until the move completes, as doing so will cause the edit to fail. [Read more](../configuration/ptr-records.md#edit-ptr-subdomains-cname)

* The **Send using waves** pages have been updated to clarify audience re-evaluation behavior across waves: audience membership is fixed at activation time (snapshot), but profile attributes and consent are evaluated at the time each wave processes. This means opt-outs occurring between waves are respected. Read more in the [FAQ section](../delivery/send-using-waves.md#faq).

* The **Data Governance** page has been updated to clarify that DULE policy enforcement applies to **profile attribute fields only**. Event-based fields (context attributes such as journey event fields) are not supported: labels applied to those fields in the UI will not restrict data usage. [Read more](../action/action-privacy.md)

* The **Send-Time Optimization** documentation has been updated to reflect the new **[!UICONTROL Send within next]** limit of **2-100 hours** (previously 1-168), and to document supported AEP Hub regions for this capability. [Read more](../building-journeys/send-time-optimization.md#use-send-time-optimization)


* The **Personalized optimization model** pages have been updated to reflect the latest model improvements, covering how the ensemble model works, dataset requirements, use cases, key assumptions, and cold-start behavior. Read more in the [Experience Decisioning](../experience-decisioning/ranking/personalized-optimization-model.md) and [Offer Decisioning](../offers/ranking/personalized-optimization-model.md) sections.

* A note has been added to the **Journey arbitration ranking formulas** page to specify that ranking formulas are only available to organizations that have purchased the **Decisioning** add-on offering. [Read more](../conflict-prioritization/journey-ranking-formulas.md)

* A new **Dynamic fragments** page is now available. It documents how to use dynamic fragment resolution in [!DNL Journey Optimizer] to select which published fragment is injected into a message at runtime, based on profile attributes, dataset lookups, or context data passed at send time. [Read more](../content-management/dynamic-fragments.md)

## June 2026 {#june-2026}

* The **Check & send a direct mail message** page has been updated to clarify Direct Mail export timing and batching behavior, including the fixed 4-hour UTC export schedule, why multiple files can be generated in a single day, when **[!UICONTROL Update profile]** executes in journeys, and recommendations for one-file-per-day scenarios. [Read more](../direct-mail/test-send-direct-mail.md#dm-export-timing)

* A new **Journey types: choose the right one** page is now available. It compares all journey entry points — Read Audience, Audience Qualification, Unitary event, and Business event — with decision guides and a feature compatibility matrix to help you select the right type for your use case. [Read more](../building-journeys/journey-types-selection.md)

* A new **Journeys vs. campaigns** page is now available. It compares Journeys, Action campaigns, and API-triggered campaigns across execution style, data model, and use case — including inbound channel activation for low-latency edge personalization, multi-surface inbound delivery, and guidance on when to use Orchestrated campaigns (ad-hoc audience composition, federated data). [Read more](../start/journeys-vs-campaigns.md)

* The **High throughput mode** page has been updated to reflect the expanded regional availability: the feature is now available across all regions except Switzerland for organizations licensed with the High Throughput transactional messaging add-on. [Read more](../campaigns/api-triggered-high-throughput.md)

* A new **Engageable Profiles and license usage** section has been added to the **Get started with profiles** page as the single source of truth for this concept, with targeted references added across the Audiences, Campaigns, and Decisioning sections. [Read more](../audience/get-started-profiles.md#engageable-profiles)

* The **Split** activity documentation has been updated to document the **[!UICONTROL Segment code]** field available in each subset settings, which allows you to assign a unique identifier to each audience segment for tracking and reporting purposes. [Read more](../orchestrated/activities/split.md)

* The **Configure a Targeting dimension** page has been updated to document the two targeting dimension types available in Orchestrated campaigns: the built-in **profile targeting dimension** (no configuration required) and **custom targeting dimensions** based on relational schemas. [Read more](../orchestrated/target-dimension.md)

* The **Leverage themes in a fragment** documentation has been clarified to explicitly document the 5-theme compatibility limit (including the Adobe default theme constraint) and to explain that fragment insertion is blocked when the email theme is not one of the fragment-associated themes. [Read more](../email/apply-email-themes.md#leverage-themes-fragment)

* The **Get started with datasets** and **Get started with schemas** pages have been updated with guidance on enabling datasets and schemas for Real-Time Customer Profile, including key considerations, the distinction between disabling a dataset versus its underlying schema, and links to the Adobe Experience Platform planning and best practices documentation. [Learn more about datasets](../data/get-started-datasets.md) and [Learn more about schemas](../data/get-started-schemas.md)

* A new **Get started with Adobe Journey Optimizer** onboarding hub is now available. New users can choose their path by role, explore fundamentals, or jump to day-to-day areas if already onboarded — without needing to know where to look first. [Read more](../../rp_landing_pages/get-started-landing-page.md)

* A new **Start from your goal** page lets you start from what you want to accomplish rather than a feature name. It maps business goals to the recommended [!DNL Journey Optimizer] capability across setup, journeys, campaigns, personalization, decisioning, and reporting. [Read more](../start/ajo-use-case-guide.md)

* The **Get started for developers** role guide has been updated with clearer introductions for each section and improved **Collaborate across roles** tabs that reference journeys and link to key implementation pages. [Read more](../start/path/developer.md)

* A new **Path assignment on journey re-entrance** subsection has been added to the **Path experimentation** documentation. It clarifies that path assignment is persistent for a profile across multiple entrances into the same journey version, but only within that journey version. Assignments reset when a new journey version is published, and each path experimentation activity in a journey applies an independent random assignment. [Read more](../building-journeys/path-experimentation.md#path-assignment)
* References to **Adobe Experience Cloud** have been aligned with the **[!DNL Adobe CX Enterprise]** brand across the [!DNL Journey Optimizer] documentation.

* The **`nowWithDelta()` date function** documentation has been updated to clarify month-end behavior: when the target month has fewer days than the current day-of-month, the result is normalized to the last valid day of that month. [Read more](../building-journeys/functions/date-functions.md#nowWithDelta)

* The **Get started with deliverability** page has been updated with a new **Providers without per-recipient FBL** subsection. It lists the major mailbox providers that do not return per-recipient spam complaints — Gmail / Google Workspace, Apple iCloud, and Corporate Microsoft 365 / Exchange Online — and explains why the absence of a suppression list entry is expected for recipients using these services. [Read more](../reports/deliverability.md#providers-no-fbl)

* **Experience Decisioning is now available for the direct mail channel.** A new **Batch decisioning in direct mail** page describes how to use the Decisioning engine to personalize direct mail extraction files, or to export profiles and their decisioning results for use in downstream systems. **Direct mail** has been added as a supported channel across the Decisioning documentation (Get started, Create a decision policy, Use decision policies in messages, Get started with decisions policies), including the ability to return multiple decision items per profile through the **[!UICONTROL Number of items]** field. [Read more](../experience-decisioning/batch-decisioning-direct-mail.md)

* The **Journey Fragments** documentation is no longer flagged as Limited Availability. The page now includes a note disambiguating Journey Fragments from content **[!UICONTROL Fragments]** and **AEM Content Fragments** (cross-linked from all three pages), and documents support for **Sandbox tooling**, **Audit Logs**, and **tagging**. Journey Fragments have also been added to the **Get started with journeys** page. [Read more](../building-journeys/journey-fragments.md)

* The **External data sources** and **custom action** documentation has been updated for custom authentication. The `tokenInResponse` field now lets you specify whether the `access_token` or `id_token` is used as the authentication credential when an endpoint returns both. For certificate-based custom authentication, the `subType` and `aud` fields are now mandatory, the token endpoint `method` must be `POST`, and references to "Azure Entra ID" have been corrected to "Microsoft Entra ID". [Read more](../datasource/external-data-sources.md#certificate-credential)

* The **Get started with Decisioning** page has been updated with a process chart summarizing the end-to-end Decisioning workflow, from managing decision items and configuring selection strategies to embedding decision policies into a journey or campaign. [Read more](../experience-decisioning/gs-experience-decisioning.md#process)

* The **Sender headers** documentation now clarifies that **[!UICONTROL Sender name]** and **[!UICONTROL Sender email]** must both be set or both left empty, otherwise journeys and campaigns cannot be published. [Read more](../email/header-parameters.md#sender-header)

## May 2026 {#may-2026}

* The limitations and best practices when using dynamic content in visual fragments have been merged into a single **Manage conditional content in fragments** section for improved readability. [Read more](../email/use-visual-fragments.md#fragment-dynamic-content)

* Two new high-level permissions have been added: **Manage Key Registry**, which allows users to view, create, rotate, and revoke keys in the key registry, and **View Key Registry**, which allows users to view the key registry listing and key details. [Read more](../administration/high-low-permissions.md#administration-permissions) 

* The **Use decision policies in messages** documentation now describes how to view the full structure of a decision policy from the campaign summary and copy a JSON technical summary to the clipboard for troubleshooting. [Read more](../experience-decisioning/use-decision-policy.md#decision-policy-summary)

* The legacy **Decision management** [Auto-optimization models](../offers/ranking/auto-optimization-model.md) page has been rewritten to align with the updated Decisioning documentation, including reinforcement learning overview, requirements and limitations, balancing optimization with learning, and Thompson sampling details. [Read more](../offers/ranking/auto-optimization-model.md)

* The **Release notes** page has been restructured with a topic-based layout. Changes are now grouped by product area instead of by change type, with a new dedicated **Usability improvements** section. Coming soon entries appear as expandable accordions within each topic. [Read more](release-notes.md)

* The **Orchestrated campaigns guardrails and limitations** page now documents the **channel activities** limit per Orchestrated campaign. [Read more](../orchestrated/guardrails.md#activities-limitations)

* The **Copy Journey Optimizer objects between sandboxes** documentation now includes an important note for **Orchestrated campaigns**: after import, duplicate the campaign in the target sandbox and use the duplicate for execution to ensure reporting correctly captures feedback and tracking data. [Read more](../configuration/copy-objects-to-sandbox.md#copy-to-sandbox)

* The **Key Terminology** page has been overhauled: six new terms added, a new **Conflict & prioritization terms** section introduced, and a new **When terms look similar** disambiguation guide added for four commonly confused term pairs. Adobe Experience Platform-specific terms have been removed and replaced with a note linking to the Adobe Experience Platform glossary. [Read more](../start/terminology.md)

* The **Deep links** documentation has been expanded with a new **Authoring deep links** section detailing the two options available for email (Email Designer UI and Personalization Editor code) and the URL function syntax for SMS. The **Create an SMS message** page now includes a deep link step in the content authoring flow. [Read more](../email/deeplinks.md)

* The **Url** helper reference has been updated with a dedicated section in the Personalization documentation. [Read more](../personalization/functions/helpers.md#url)

* A limitation has been added to the **Execution Metadata** helper documentation: the function is not supported in inbound channels (Web, Code-based experience, In-App Message, Content Cards). [Read more](../personalization/functions/helpers.md#execution-metadata)

* A new **Personalization recipes** page has been added, providing ready-to-use personalization patterns for the most common use cases in [!DNL Journey Optimizer]. It covers date and time recipes (current date formatting, countdown to expiry, days-before calculations, time-only display, and weekend vs. weekday detection), string recipes (using `replaceAll` with variable assignment), and conditional fallback recipes (empty-field fallbacks using `isEmpty`). [Read more](../personalization/personalization-recipes.md)

* The **Personalization syntax** documentation has been updated with an expanded introduction clarifying the difference between Handlebars (`{{...}}`) and PQL (`{%= ... %}`) syntaxes, including a usage table, guidance on escaping literal double quotes, and a new **PQL syntax rules for special attribute keys** section covering reserved keywords, hyphenated attribute keys, and numeric event IDs. The note on backtick escaping has also been corrected: hyphenated field names can be referenced directly in `{{...}}` blocks; only backtick syntax fails there. [Read more](../personalization/personalization-syntax.md)

* The **Date Time functions** documentation has been enriched with new real-world examples: a countdown pattern for `dateDiff`, a weekend vs. weekday conditional for `dayOfWeek` (with a note on using the journey Condition activity for routing use cases), and a time-only display pattern combining `extractHours` and `extractMinutes` with a leading-zero guard. [Read more](../personalization/functions/dates.md)

* The **String functions** documentation has been updated with a new example for `replaceAll` showing how to assign the result to a `{% let %}` variable for reuse across multiple expressions in the same template. [Read more](../personalization/functions/string.md#replace-all)

* The **Array functions** documentation has been updated with a new **Iterate over an array** section documenting the Handlebars `{{#each}}` block helper, including a note clarifying that `{{#each}}` is supported in the personalization editor only and cannot be used inside journey condition activities. [Read more](../personalization/functions/arrays-list.md#each-loop)

* The **Get started with datasets** page has been updated with a new **Inbound** entry in the system datasets section, documenting the _AJO Inbound Activity Event Dataset_. A note has been added to clarify that a profile must have at least one message sent from [!DNL Journey Optimizer] before incoming messages are captured in this dataset. [Read more](../data/get-started-datasets.md#system-datasets)

* The **Export message content** documentation has been expanded with a **Message Export FAQ** (personalized content, images and media, tracked links, PII, retention, use cases, etc.), and **sample exported JSON** examples for SMS and email. [Read more](../configuration/message-export.md)

* A new **AJO Message Export schema** page documents every field in the AJO Message Export Dataset, with data types and hierarchy for the exported email and SMS payload. [Read more](../configuration/message-export-schema.md)

* A new **Personalize URLs in emails** page has been added, consolidating guidance on dynamic URL personalization, complete/base URL personalization, URL tracking parameter personalization, and key guardrails. [Read more](../email/url-personalization.md)

* A new **Business rules queries** section has been added to the query examples page, providing a Data Lake query to check all profile discards due to journey frequency capping exclusions on a specific journey after a specific date. The query includes the `eventCodeReason` field to identify whether profiles were excluded because a cap was reached (`CAP_REACHED`) or due to a lower priority (`LOWER_PRIORITY`). [Read more](../reports/query-examples.md#business-rules-queries)

* The **Journey properties** documentation has been updated to document the new **Current journey payload size** indicator in the journey properties panel. This read-only field shows the current size of the journey payload compared to the configured limit (e.g. 1.5 MB out of 2 MB), helping you monitor journey complexity before publishing and avoid size-related publication errors. [Read more](../building-journeys/journey-properties.md#journey-payload-size)

## April 2026 {#april-2026}

* The **Change dimension** activity documentation has been updated to clarify that while the activity uses an external join and keeps all records at the dimension-change step, records without a matching profile in the new targeting dimension are silently excluded at message delivery time. [Read more](../orchestrated/activities/change-dimension.md)

* The guardrails in the **Add a CC field to emails** documentation have been enhanced. They now specify that the CC address is not checked against consent or suppression, and that opens and click-throughs from emails sent to the CC address are taken into account in the total opens and clicks from the send analysis. [Read more](../configuration/cc-email-field.md)

* The **Channel activities** documentation has been updated with a new **Marketing vs Transactional messages** section explaining the behavioral differences between the two channel categories: opt-in requirements, business rule application, channel configuration type, and recommended use cases. [Read more](../orchestrated/activities/channels.md#marketing-vs-transactional)

* The **Fork activity** documentation has been enriched with a new **Examples** section illustrating how to use the Fork activity to split an audience across two parallel email branches — one Marketing and one Transactional — in a single campaign run. [Read more](../orchestrated/activities/fork.md#fork-examples)

* The **Build audience activity** documentation has been enriched with a new example showing how to filter profiles by a subscription plan attribute using the rule builder. [Read more](../orchestrated/activities/build-audience.md#build-audience-examples)

* The **Get started with Orchestrated campaigns** page documents the entry-level **Build audience → Fork → Channel A + Channel B** pattern in **What's inside an Orchestrated campaign?**, with cross-references to the Fork activity and Marketing vs Transactional messages pages. [Read more](../orchestrated/gs-orchestrated-campaigns.md#gs-ms-campaign-inside)

* The **Edit email content with the advanced HTML editor** page has been moved from the Content management section to the **Email** section of the documentation. The page now documents that the advanced HTML editor is available in the Email Designer for email messages as well as for email content templates. [Read more](../email/email-expert-mode.md)

* The **Start and monitor Orchestrated campaigns** documentation has been updated with a new section detailing the internal publication-time execution sequence, along with a campaign lifecycle status table, a pre-publication checklist, and a sending confirmation warning for non-recurring campaigns. [Read more](../orchestrated/start-monitor-campaigns.md#publication-sequence)

* The **Save audience** activity documentation has been updated with a note clarifying that Save Audience activities always execute before message activities at publication time. [Read more](../orchestrated/activities/save-audience.md)

* Three new Q&As have been added to the **Orchestrated campaigns FAQ**: what happens internally at publication time, a 7-point checklist of reasons why messages may not send after publishing, and how profile snapshot lookup differs from real-time profile resolution. [Read more](../orchestrated/orchestrated-campaigns-faq.md)

* A new **[Events discarded due to a blocked journey instance](../building-journeys/troubleshooting-execution.md#max-instance-stack-events-reached)** section has been added to the journey troubleshooting documentation, explaining the `maxInstanceStackEventsReached` discard reason, when it occurs, and how to mitigate it. The guardrails and step event field list pages have also been updated accordingly.

* The **Leverage fragments in decision policies** documentation now includes guardrail notes for the **Email** channel: **[!UICONTROL Simulate content]** does not display expression fragments from the decision item, while **[!UICONTROL Send proof]** and activated campaigns do. The page also states that **[!UICONTROL Visual fragments]** cannot be assigned to a decision item — only **expression fragments** are supported in this context. [Read more](../experience-decisioning/fragments-decision-policies.md)

## March 2026 {#march-2026}

* Documentation for **previewing code-based experiences with Experience Decisioning** now clarifies that **[!UICONTROL Simulate content]** is content preview only. Context data from live Edge requests is not simulated in authoring preview. [Read more](../code-based/test-code-based.md#preview-code-based)

* The **Use Adobe Experience Platform data** documentation has been updated: the guardrails no longer state that dataset lookups cannot be chained, reflecting current product behavior. [Read more](../data/lookup-aep-data.md)

* The **Update Profile** activity documentation has been updated to document support for updating up to five profile attributes in a single action. [Read more](../building-journeys/update-profiles.md)

* The **Read Audience** activity and **Journey properties** documentation have been updated to clarify the 91-day journey lifecycle for always-on recurring journeys. The schedule section now explicitly confirms that recurring journeys with no end date remain Live past 91 days, and the global timeout FAQ has been expanded to distinguish the 91-day profile TTL from the 91-day reporting window. [Read more](../building-journeys/read-audience.md#schedule)

* The **Dataset lookup** activity documentation has been updated to clarify that the lookup key must be configured in advanced mode for the `@datasetLookup{}` syntax to work in downstream condition activities. A troubleshooting section has been added with guidance on resolving the "Dataset lookup not found" error. [Read more](../building-journeys/dataset-lookup.md#troubleshooting)

* The **Date Time functions** documentation has been updated with a new example showing how to format a timestamp from a context event attribute, including the `toDateTime()` requirement, backtick syntax for numeric event IDs, and a common error callout for the PQL "mismatched input" error. [Read more](../personalization/functions/dates.md#format-date)

* The **Orchestrated campaigns guardrails and limitations** and **Get started with Sources connectors** documentation have been updated to clarify that for file-based Change Data Capture, the `_change_request_type` field is required and its values must be lowercase `u` (upsert) or `d` (delete), not uppercase. [Read more](../orchestrated/guardrails.md)

* The **Add links & track messages** documentation has been updated with guidance on how tracking identifiers (urlID) are generated: a unique urlID is only assigned when both the URL and the label are unique. To track the same URL across multiple emails (or multiple times in one email), users must use a unique label for each similar URL; otherwise, [!DNL Journey Optimizer] cannot determine which link was clicked. [Read more](../email/message-tracking.md#track-across-multiple-emails)

* The **Create test profiles** documentation has been updated with an important note about identity descriptor requirements: when a dataset is deleted and recreated, the schema must retain the correct identity descriptor on the primary identity field. Without it, ingested profiles will not be flagged as `testProfile = true` even if ingestion completes successfully. A troubleshooting checklist has been added. [Read more](../audience/creating-test-profiles.md)

* The **Read Audience** activity documentation has been updated to clarify that a **Business Event** activity is an exception to the rule that Read Audience must be the first activity in a journey. A note has also been added referencing the **Optimize** activity as an advanced alternative for controlling audience targeting. [Read more](../building-journeys/read-audience.md)

* **Send using waves** in journeys is now generally available. The Limited Availability flag has been removed from the documentation. [Read more](../delivery/send-using-waves.md)

* The **Jump** activity documentation has been enriched with a new design strategy section — **Bite-sized sub-journeys** — explaining how to break complex end-to-end flows into smaller, focused sub-journeys connected via the Jump activity. [Read more](../building-journeys/jump.md#jump-strategy)

* The **Tags** documentation has been updated with guidance on using tag categories as an alternative to complex naming conventions. A new section explains how to set up tag categories for scalable journey management. [Read more](../building-journeys/tags.md)

* The **About data sources** documentation now includes a new section helping practitioners choose between three data access strategies: accessing external data via custom actions, using a dataset not enabled for Profile, or using a profile-enabled dataset. Each option is described with trade-offs and recommended use cases. [Read more](../datasource/about-data-sources.md#data-access-strategy)

* The **Push notification design** documentation has been updated with a note clarifying the behavior of universal links on iOS: if the notification URL is registered as a universal link, the associated app will open regardless of the chosen Web URL action. Guidance has been added on how to force a browser open. [Read more](../push/design-push.md)

* A new **Monitor your AI models** page is now available in the Decisioning documentation. It explains how to track the health, training status, and performance of personalized optimization models directly in [!DNL Journey Optimizer]. [Read more](../experience-decisioning/ranking/ai-model-observability.md)

* The **advanced HTML editor** (expert mode) for email templates is now available in Limited Availability. The documentation page is now publicly accessible. This capability lets you view and edit the raw HTML source of email content templates directly from the Email Designer. [Read more](../email/email-expert-mode.md)

* The **URL tracking** and **Journey troubleshooting** documentation have been updated to document the behavior of `context.system.source.actionId` in closed journeys. Closed or un-republished journeys may produce empty `{}` placeholders in tracking URLs. Guidance has been added on how to resolve the issue by republishing the journey or removing the affected parameter. [Read more](../email/url-tracking.md)

* The **Adobe Experience Platform data source** documentation has been updated with a note that only XDM Individual Profile-based schemas are supported in the Data Source configuration. [Read more](../datasource/adobe-experience-platform-data-source.md)

* The **Datasets Time-to-live (TTL) guardrails** documentation has been enhanced with a new FAQ entry to clearly identify which datasets are subject to TTL. TTL applies exclusively to time-series datasets — record-type datasets such as entity datasets, classification datasets, and decision object repositories are not subject to TTL and will not be impacted by the guardrail rollout. [Read more](../data/datasets-ttl.md)

* The **Journey properties** and **Pause a journey** documentation have been updated to document the new pause and resume fields now available in the journey technical details. The **Copy technical details** button now includes `lastPausedAt`, `lastPausedBy`, `lastPausedById`, `lastResumedAt`, `lastResumedBy`, and `lastResumedById`, in addition to the existing `pausedJourneySettings` block. A new section has also been added to the **Pause a journey** page explaining how to view pause and resume timestamps directly from journey properties. [Read more](../building-journeys/journey-properties.md)

## February 2026 {#february-2026}

* A new page is now available for Decision management. It lists all operators, helpers, and functions supported when personalizing offer content (representations) with the personalization editor. Use this list to avoid runtime errors. Only the documented functions are supported when personalizing content in Offer Decisioning. [Read more](../offers/offer-library/personalization-editor-supported-functions.md)

* The **Create decision policies** and **Use decision policies in messages** documentation has been updated for Email: a note now explains that when the same offer can be selected by more than one decision policy in the email body, the engine deduplicates offers (each placement receives a different offer). To display the same offer in multiple placements (for example, header and footer), use **Reuse decision output**. [Read more](../experience-decisioning/create-decision-policy.md)

* The Decision items page has been updated with information on Push channel and Custom event capping. [Read more](../experience-decisioning/items.md#capping)

* The **Experience event lookup in journeys** documentation has been updated with the deprecation timeline: starting April 1, 2026, organizations that have not used experience event attributes in journey expressions in the last 90 days will no longer have access to this capability. The FAQ now focuses on the retirement timeline and who is impacted, and the Experience event schema page has been aligned with a direct link to alternative approaches. [Read more](../building-journeys/exp-event-lookup.md)

* The **Decisioning** documentation has been updated for **dataset lookup** with Adobe Experience Platform data: the supported channels guardrail now states that dataset lookup works for all channels where Decisioning is available (code-based experience, Email, Push, SMS, and the Content Decision activity in journeys). Limited Availability and public beta notes have been removed from the decision rules, ranking formulas, and decision items pages. [Read more](../experience-decisioning/aep-data-exd.md)

* The External systems integration page has been updated with links to custom data sources and custom actions, and clarifies that the egress proxy provides a static IP for outbound calls from **Custom actions** to your external systems. [Read more](../configuration/external-systems.md)

* The Journey Dry run documentation has been clarified: the step event attributes `inDryRun` and `dryRunID` now document that they return `true`/instance ID when in Dry run mode and `null` for test or live journeys. Guidance for excluding Dry run step events in reporting queries has been updated accordingly. [Read more](../building-journeys/journey-dry-run.md)

* **Web push** is now generally available. The push notification documentation has been restructured and updated accordingly (get started, design, send, create). [Read more](../push/get-started-push.md)

* The Web push configuration page is now available in the documentation. [Read more](../push/push-configuration-web.md)

* Documentation on using fragments in Decisioning has been updated: notes have been added in the Fragments and Decisioning sections, and the Fragments in decision policies page has been updated. [Read more](../experience-decisioning/fragments-decision-policies.md)

* The SMS webhook documentation has been updated: Twilio webhook content has been removed. [Read more](../mobile/mobile-webhook.md)

* The **Convert images to content templates** documentation has been enhanced with expanded guardrails and recommendations, common use cases, and clearer guidance for converting image designs into editable HTML content templates. It also mentions the fact that you can now use a theme as input for the conversion. [Read more](../content-management/image-to-html.md)

* The Decisioning migration API documentation has been updated. [Read more](../experience-decisioning/decisioning-migration-api.md)

* The **Content Decision** activity is now generally available. The Content Decision activity page has been updated with a section on Decisioning data available in step events. [Read more](../building-journeys/content-decision.md)

* Links to the loyalty challenge API documentation have been added to the Loyalty challenges section (get started, create challenges, create tasks, access loyalty challenges). [Read more](../loyalty-challenges/get-started.md)

* The supported channels information in the campaign creation wizard documentation has been corrected. The Get started with channels and Orchestrated campaigns FAQ pages have been updated accordingly. [Read more](../campaigns/get-started-with-campaigns.md)

* The permissions documentation has been corrected regarding **Journey Manage** and **Approve** permissions. [Read more](../administration/ootb-permissions.md)

* The AEM (Adobe Experience Manager) integrations documentation has been updated with revised naming (AEM dynamic content and AEM fragments). [Read more](../integrations/aem-fragments.md)

* A new exclusion reason has been added to the exclusions list: **UnsubscribeLinkNotValid** (error code 050081). This exclusion is generated when the List-Unsubscribe mailTo subject length is greater than the RFC limit of 998 characters. [Read more](../reports/exclusion-list.md)

* The formatDate helper function documentation has been enhanced with a note that the function requires a date-time field type (not a string) and with multiple examples: formatting a date-time field, converting a string to date first, full date with day name, dynamic date from system time, and day-of-week format including lowercase output. [Read more](../personalization/functions/dates.md#format-date)

* The text version email documentation has been enhanced with comprehensive use case guidance, including decision criteria for when to use custom plain text versus auto-sync, practical examples with real-world scenarios, and an FAQ section with common questions. [Read more](../email/text-version-email.md#when-to-use)

* The Email Designer themes documentation has been updated with information about web fonts support limitations and the importance of fallback fonts. [Read more](../email/apply-email-themes.md#themes-guardrails)

* A limitation has been added to the Execution Metadata helper documentation to clarify that metadata is not captured for profiles excluded from the action. [Read more](../personalization/functions/helpers.md#execution-metadata)

* The code-based implementation samples documentation has been updated to include the tokens field in the propositionAction for accurate tracking and attribution in Decisioning. [Read more](../code-based/code-based-implementation-samples.md#client-side-how)

* A note has been added to the URL tracking and List unsubscribe documentation to clarify that the order of URL tracking parameters appended to URLs is random and cannot be controlled. [Read more](../email/url-tracking.md)

## January 2026 {#january-2026}

* The License usage dashboard documentation has been clarified with updated guidance about **Engageable Profiles**, including definition details and troubleshooting guidance. [Read more](../audience/license-usage.md#what-is-engageable-profile)

* A note has been added to the Email Designer themes documentation to clarify web fonts support limitations. [Read more](../email/apply-email-themes.md#themes-guardrails)

* A new guardrail section has been added to document journey payload size validation, including warning and error thresholds and guidance on how to optimize journeys. [Read more](../start/guardrails.md#journey-payload-size)

* The Decisioning guardrails documentation has been updated to include decision items size limitations (1KB for items including attributes with max of 30 attributes). [Read more](../experience-decisioning/decisioning-guardrails.md)

* A note has been added to the decision policy creation documentation to inform users that once a decision policy is created, any changes can take up to 15 minutes to propagate across all data regions, and up to 30 minutes for Canada. [Read more](../experience-decisioning/create-decision-policy.md#review)

* A note has been added to the fragments documentation to warn that when both the button label and URL are made editable in a fragment, the tracking dataset logs the URL value instead of the label value. [Read more](../content-management/customizable-fragments.md#visual)

* A new page is now available describing the benefits of migrating from Decision management to Decisioning, including information about upcoming migration tooling APIs. [Read more](../experience-decisioning/migrate-to-decisioning.md)

* Added a guardrail to clarify that lookup datasets are available for inbound edge-based activation only in the region where the dataset's sandbox resides. [Read more](../data/lookup-aep-data.md#guidelines)

* A new section has been added to the Orchestrated campaigns channel configuration documentation explaining how to use contextual attributes (such as campaign ID, name, and action details) in URL tracking parameters for analytics and reporting purposes. [Read more](../orchestrated/channel-config.md#url-tracking)

* The Content optimization documentation has been restructured for better clarity. The main optimization page has been split into four focused subpages: an get started page, a dedicated page for targeting, one for experimentation, and another for combining both approaches. [Read more](../content-management/gs-message-optimization.md)

* The Limited Availability notes have been removed from three journey alerts (Journey Published, Journey Finished, and Custom Action Capping Triggered) as these features are now generally available. [Read more](../reports/alerts.md)

* The Test, validate & approve landing page has been enhanced with new sections including testing capabilities overview, common questions FAQ, decision tree with navigation links, and enhanced terminology with documentation links. [Read more](../../rp_landing_pages/test-landing-page.md)

* A new section has been added to the personalization syntax documentation to clarify how to use reserved keywords in personalization expressions. Certain PQL keywords such as `next`, `last`, and `this` must be escaped with backticks when used as field names in your XDM schema. [Read more](../personalization/personalization-syntax.md#reserved-keywords)

* The [Get started with campaigns](../campaigns/get-started-with-campaigns.md) and [Manage campaigns](../campaigns/manage-campaigns.md) pages have been restructured with improved information architecture, including a comprehensive workflow with type-specific guides, enhanced campaign type comparisons, and consolidated status table.

* The Journeys landing page has been redesigned to facilitate onboarding with a new 6-step workflow, enhanced journey type comparisons, and improved navigation throughout the documentation. [Read more](../building-journeys/journey.md)

* A detailed section has been added to help users generate Base64-encoded OpenSSH private keys for SFTP authentication when configuring file routing for Direct Mail to avoid connection errors. [Read more](../direct-mail/direct-mail-configuration.md#ssh-key-generation)

* A note has been added to the subdomain delegation documentation to inform users to allow 24-48 hours for DNS propagation before attempting delegation to Adobe. [Read more](../configuration/delegate-subdomain.md#set-up-subdomain)
