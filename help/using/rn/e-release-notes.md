---
solution: Journey Optimizer
product: journey optimizer
title: Pre release notes for Journey Optimizer
description: Adobe Journey Optimizer Pre Release notes
feature: Release Notes
hide: yes
hidefromtoc: yes
exl-id: 6e7d1300-8efd-4fdc-90e3-3ccdc3babd2f
---
# Pre-release notes {#e-release-notes}

[!DNL Adobe Journey Optimizer] continuously delivers new features, enhancements to existing features, and bug fixes. All changes are consolidated at the end of each month in the [release notes](release-notes.md). 


## August '25 pre-release notes {#25-8-rn}

**The pre-release notes below are subject to change without prior notice until the release availability date**. Links, screens and updated documentation are published in the release notes, at the release date.

See also [Adobe Experience Platform Pre-release notes](https://experienceleague.adobe.com/en/docs/experience-platform/release-notes/pre-release-notes){target="_blank"}.

**Release date**: August 19, 2025


### New capabilities {#Aug-25-8-features}

<table>
<thead>
<tr>
<th><strong>Pause and resume journeys</strong><br/></th>
</tr>
</thead>
<tbody>
<tr>
<td>
<p>You can now pause and resume your journeys. This capability gives journey practitioners greater control and flexibility by allowing live journeys to be temporarily suspended without disrupting customer experience. When paused, no communications are sent, and profiles remain in a suspended state until the journey is resumed.</p>
<p>You can pause and resume one journey only, or perform bulk pause and resume operations to a group of journeys.</p>
<p>In addition, you can apply global filters to paused journeys to exclude profiles based on their attributes.</p>
<p><!--img src="assets/do-not-localize/PauseResume.gif"/>--></p>
<p>Previously released in Limited Availability, this capability is now available to all environments (General Availability).</p>
<p><!--For more information, refer to the <a href="../building-journeys/journey-pause.md">detailed documentation</a>--></p>
</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th><strong>Calendar view</strong><br/></th>
</tr>
</thead>
<tbody>
<tr>
<td>
<p>A calendar view is now available in the journeys and campaigns lists. It allows you to visualize all journeys and campaigns activations in the respective lists.</p>
<p>Previously available in Limited Availability, this feature is now available to all environments. With this General Availability release, the feature includes:</p>
<ul>
<li>Design improvements for the navigation in dates,</li>
<li>The ability to see draft campaigns if you have set a start and end date,</li>
<li>A new setting to hide and show calendar items running for a long time.</li>
</ul>
<p><!--img src="assets/do-not-localize/calendar.gif"/>--></p>
<p><!--For more information, refer to the <a href="../building-journeys/journey-ui.md#journeys-calendar">detailed documentation</a>--></p>
</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th><strong>Dark mode in the Email Designer</strong><br/></th>
</tr>
</thead>
<tbody>
<tr>
<td>
<p>The Journey Optimizer Email Designer now offers the ability to switch to dark mode view, where you can additionally define specific custom settings that will display only for recipients reading their emails in dark mode.</p>
<p>Note the following:</p>
<ul>
<li>The dark mode final rendering may vary and depends on the recipient's email client.</li>
<li>Not all email clients support custom dark mode. Moreover, some email clients only apply their own default dark mode for all emails that are received. In both cases, the custom settings that you defined in the Email Designer cannot be rendered.</li>
</ul>
<P>This capability is currently in beta version and only available to beta customers. To join the beta program, contact your Adobe representative.</p>
<p><!--img src="assets/do-not-localize/dark-mode.gif"/>--></p>
<p><!--For more information, refer to the <a href="../email/dark-mode.md">detailed documentation</a>--></p>
</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th><strong>Use Adobe Experience Platform data for personalization</strong><br/></th>
</tr>
</thead>
<tbody>
<tr>
<td>
<p>Leverage data from Adobe Experience Platform in the personalization editor to personalize your content. To do this, datasets needed for lookup personalization must first be enabled through an API call. Once done, you can use their data to personalize your content into [!DNL Journey Optimizer].</p>
<p>Previously released in Limited Availability, this capability is now available to all environments. With this General Availability release, the following enhancements have been introduced:</p>
<ul>
<li>Support of inbound channels,</li>
<li>The "datasetLookup" helper function can now be used within expression and visual fragments to personalize content using data from Adobe Experience Platform datasets,</li>
<li>An option in the dataset now allows you to enable datasets for lookup personalization, without having to perform an API call.</li>
</ul>
<p><!--img src="assets/do-not-localize/FILE.gif"/>--></p>
<p><!--For more information, refer to the <a href="../FILE.md">detailed documentation</a>--></p>
</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th><strong>Use Decisioning in email channel</strong><br/></th>
</tr>
</thead>
<tbody>
<tr>
<td>
<p>You can now add Decision policies into email journeys and campaigns. Decision policies are containers for your offers that leverage the Decisioning engine to dynamically return the best content to deliver for each audience member.</p>
<p>Previously released in Limited Availability, this capability is now available to all environments (General Availability).</p>
<p><!--img src="assets/do-not-localize/FILE.gif"/>--></p>
<p><!--For more information, refer to the <a href="../FILE.md">detailed documentation</a>--></p>
</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th><strong>Landing page custom forms</strong><br/></th>
</tr>
</thead>
<tbody>
<tr>
<td>
<p>Journey Optimizer now allows you to create custom forms and leverage them in landing pages to capture profile attributes into the dataset defined for each form.</p>
<p>This capability is currently in beta version and only available to beta customers. To join the beta program, contact your Adobe representative.</p>
<p><!--img src="assets/do-not-localize/FILE.gif"/>--></p>
<p><!--For more information, refer to the <a href="../FILE.md">detailed documentation</a>--></p>
</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th><strong>Journey optimization</strong><br/></th>
</tr>
</thead>
<tbody>
<tr>
<td>
<p>Journey Optimizer now empowers you with the tools to optimize your journeys by leveraging AI and experimentation frameworks while ensuring seamless usability and differentiation between condition and optimization functionalities.</p>
<p><!--img src="assets/do-not-localize/FILE.gif"/>--></p>
<p><!--For more information, refer to the <a href="../FILE.md">detailed documentation</a>--></p>
</td>
</tr>
</tbody>
</table>


### Improvements {#Aug-25-8-improv}

Improvements coming with this release are listed below.

- **Administration**
  - **Channel configuration monitoring alerts** - You can now subscribe to receive system alerts, either by email or in the Journey Optimizer notification center, in case a channel configuration failure happens or if a DNS record is missing.

- **Campaigns**
  - **Rate control in outbound campaigns** - You can now enable throttling rate control for outbound campaigns (Email, SMS, Push notifications), allowing you to prevent overload on downstream systems, such as landing pages or customer care platforms.
  - **Action campaign scheduling** - The campaign daily, weekly and monthly schedulers have been updated for improved granularity. For example, you can now set the number of weeks/months between schedules, define on which day to execute, and decide to stop after a specific number of occurrences or on a specific date.

- **Channel - Push**
  - **Push notification expiration date** - You can now specify an expiration date for each Push notification, which prevents time-sensitive messages (such as Black Friday Sale) from being sent after a certain date, thus avoids delivering poor experience to your customers.

- **Channel - Email**
  - **PDF attachments to emails** - You can now attach static PDF files to email messages sent with Journey Optimizer.

- **Configuration**
  - **Dynamic domain support** - Journey Optimizer now supports personalization in tracking URLs for predefined domains listed at the channel configuration level.
  - **Custom attributes support with One-click unsubscribe URL** - With Journey Optimizer, if you are managing consent outside of Adobe, you can set an external custom endpoint by defining your own one-click unsubscribe link in the email configuration. When your recipients click the unsubscribe link, Journey Optimizer appends some default profile-specific parameters to the consent update event.
  
    To further personalize your one-click unsubscribe link, you can now define custom attributes that will be appended to the consent event.

- **Journeys**
  - **Action activity in journeys** - Journey Optimizer supports a new generic Action activity that enables you to configure both single and multi-channel outbound actions, allowing for streamlined action configuration within the journey canvas. With this new activity, you also have the ability to add targeting optimization, experiments, and multi-lingual language variants to any built-in channel action.
  - **Journey bulk operations** - From the list of your journeys, you can now select multiple items. Once selected, you can pause or resume up to 10 journeys at a time.