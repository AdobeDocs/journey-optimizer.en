---
solution: Journey Optimizer
product: journey optimizer
title: Early release notes
description: Journey Optimizer early Release notes
feature: Release Notes
topic: Content Management
hide: yes
hidefromtoc: yes
exl-id: 6e7d1300-8efd-4fdc-90e3-3ccdc3babd2f
---
# Early release notes {#e-release-notes}

[!DNL Adobe Journey Optimizer] continuously delivers new features, enhancements to existing features, and bug fixes. All changes are consolidated at the end of each month in the [release notes](release-notes.md). 

**Early release notes below are subject to change without prior notice until the release availability date**. Links, screens and updated documentation are published in the [release notes](release-notes.md), at the release date.


## April '25 early release notes {#25-4-rn}


**Early release notes below are subject to change without prior notice until the release availability date**. Links, screens and updated documentation are published at the release date.

**Release date**: April 29-30, 2025


### New capabilities {#25-04-features}

New capabilities coming with this release are detailed below.

<table>
<thead>
<tr>
<th><strong>Adobe Express Integration (LA)</strong><br/></th>
</tr>
</thead>
<tbody>
<tr>
<td>
<p>Adobe Journey Optimizer now integrates with Adobe Express, enabling users to seamlessly connect their creative assets with journey orchestration. This integration simplifies the process of designing and deploying personalized content across campaigns. This feature is currently in Limited Availability.</p>
</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th><strong>Calendar View for Campaign and Journey Inventory (LA)</strong><br/></th>
</tr>
</thead>
<tbody>
<tr>
<td>
<p>A new calendar view is now available for campaigns and journey activations. This feature provides a visual representation of scheduled activities, allowing users to view and manage their campaigns and journeys more effectively. Selecting a calendar item opens a right rail with detailed information. This feature is currently in Limited Availability.</p>
</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th><strong>Adobe Experience Manager as a Cloud Service Integration (GA)</strong><br/></th>
</tr>
</thead>
<tbody>
<tr>
<td>
<p>General Availability of the integration between Adobe Journey Optimizer and Adobe Experience Manager as a Cloud Service. This integration enables seamless content sourcing and management for personalized customer journeys.</p>
</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th><strong>Personalization Playground in Experience League</strong><br/></th>
</tr>
</thead>
<tbody>
<tr>
<td>
<p>Experience League now offers an interactive Personalization Playground. This feature allows users to explore and practice personalization capabilities within Adobe Journey Optimizer. Users can write personalization code, test with sample payloads, and simulate real scenarios to enhance their learning experience.</p>
</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th><strong>Trigger Journey Execution After Batch Audience Evaluation (LA)</strong><br/></th>
</tr>
</thead>
<tbody>
<tr>
<td>
<p>Users can now specify a time window to wait for a fresh evaluation of batch audiences in the Read Audience node. If the evaluation completes within the window, the journey is triggered; otherwise, it is skipped. This feature addresses delays in batch segmentation jobs and is currently in Limited Availability.</p>
</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th><strong>Next-gen Proofing (GA)</strong><br/></th>
</tr>
</thead>
<tbody>
<tr>
<td>
<p>The Next-gen Proofing feature is now generally available. This enhancement supports contextual attributes, multilingual content, experimentation, and content templates, providing a more robust and flexible proofing experience.</p>
</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th><strong>Bring Your Own SMS Provider (GA)</strong><br/></th>
</tr>
</thead>
<tbody>
<tr>
<td>
<p>Adobe Journey Optimizer now supports custom SMS providers, allowing users to integrate their preferred SMS services for enhanced communication flexibility.</p>
</td>
</tr>
</tbody>
</table>



<!--table>
<thead>
<tr>
<th><strong>Integration with Adobe Express</strong><br/></th>
</tr>
</thead>
<tbody>
<tr>
<td>
<p>The Adobe Express integration in Adobe Journey Optimizer lets you use Adobe Express's editing tools directly during content creation, enabling you to resize, remove backgrounds, crop, and convert assets to JPEG or PNG.<p>
</td>
</tr>
</tbody>
</table>


<table>
<thead>
<tr>
<th><strong>Calendar view for journeys (Limited Availability)</strong><br/></th>
</tr>
</thead>
<tbody>
<tr>
<td>
<p>A calendar view is now allows you to visualize all journeys activations. This capability is released as a Limited Availability to a select group of customers.<p>
<p>This change is only available for a set of organizations (Limited Availability). To gain access, contact your Adobe representative.</p>
</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th><strong>Integration with Dynamic Media (Limited Availability)</strong><br/></th>
</tr>
</thead>
<tbody>
<tr>
<td>
<p>Dynamic media assets are now directly available and accessible in Journey Optimizer. This integration enables you to:
<ul>
<li>Centrally manage assets with real-time updates</li>
<li>Modify your assets settings such as width and height instantly</li>
<li>Personalize your content using images with text overlays</li>
<li>Customize Dynamic Media templates by updating your content and adding personalization fields</li>
</ul>
<p>
<p>This integration is only available for a set of organizations (Limited Availability). To gain access, contact your Adobe representative.</p>
</td>
</tr>
</tbody>
</table>


<table>
<thead>
<tr>
<th><strong>LINE channel (Limited Availability)</strong><br/></th>
</tr>
</thead>
<tbody>
<tr>
<td>
<p>Adobe Journey Optimizer has expanded its cross-channel capabilities to include support for the LINE channel. This enhancement allows you to create, edit, and preview LINE experiences enabling more personalized and engaging interactions. With LINE, you can connect with more customers, send relevant content, and improve your engagement.<p>
<p>This capability is only available for a set of organizations (Limited Availability). To gain access, contact your Adobe representative.</p>
</td>
</tr>
</tbody>
</table-->

### Improvements {#25-04-improv}
 
**Audiences**

- **Remove Limitation for Enrichment Attributes** 

    Customers with Healthcare and Privacy shields can now use Audience Composition enrichment attributes in Adobe Journey Optimizer channels, enhancing data usage capabilities.  

**Email Channel**

- **Additional Fields to Support Accessibility**  

    Two new fields have been added to the email editor to support accessibility: the `<title>` element for document titles and the `lang` attribute for language specification in the `<html>` tag.  

- **Enhancements to Email Surface Personalization - URL Tracking**  

    URL tracking in email personalization has been enhanced, allowing for more granular tracking and reporting. Updates include improved configuration options for personalized email settings.  


- **[Beta] Email Editor Improvements with Themes**

  A new beta feature introduces themes to the email editor, allowing marketers to define reusable styles and build emails faster using pre-configured modules.  

**Sandbox Tooling**

- **Decisioning Sandbox Copy**

    Decisioning objects can now be copied between sandboxes, streamlining testing and deployment workflows. A dedicated subsection for Decisioning objects will be added to the documentation.  

- **Sandbox Tooling for Custom Actions**  

  Custom actions are now included in the list of Adobe Journey Optimizer objects that can be copied using the sandbox tooling feature, streamlining testing and deployment.  

- **Sandbox Tooling for Campaigns**  

  Campaigns can now be copied using the sandbox tooling feature, simplifying the migration of campaign objects between environments.  

**Personalization**

- **Personalization Editor - Pills Activation**  

  A new button in the personalization editor allows users to toggle pills on or off. This feature declutters the editor and enables easier editing of dynamic media image parameters and profile attributes.  

- **Personalization - Observable Schema**  

  Observable schema support has been added to the personalization editor, enabling dynamic updates to schema-based attributes.  

- **New System Context Variable**  

  A new system context variable has been introduced to uniquely identify each message sent to a targeted profile. This variable can be used for tracking and personalization purposes.  



**Decisioning**

- **AI Model - Unify Ranking - New Formula Builder**  

  Marketers can now adjust real-time scores of Adobe Decisioning AI models using a new formula builder. This feature centralizes ranking adjustments for priorities and model scores.  

**Navigation**

- **Folders - Landing Pages**  

  Enhanced folder management for landing pages in Adobe Journey Optimizer, including UI changes, flows, and API updates.  

- **Folders - Templates and Fragments** 

  The Limited Availability mention has been removed for folders in templates and fragments, indicating that this feature is now generally available.  

- **Right Rail in Campaigns List**  

  A right rail has been added to the campaigns list, providing detailed information when a campaign is selected.  



**Deliverability**

- **Improved Workflow for Top-Up IPs and Removal of Delegated Subdomains**  

  The workflow for managing top-up IPs and delegated subdomains has been improved, simplifying the process for users.

**Playbooks**

- **[Beta] Create Your Own Playbooks**
  
  Users can now create their own playbooks in Adobe Journey Optimizer, enabling greater customization and flexibility in journey planning.  