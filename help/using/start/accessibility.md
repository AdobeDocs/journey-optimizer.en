---
solution: Journey Optimizer
product: journey optimizer
title: Accessibility features in Journey Optimizer
description: Learn more about accessibility in Journey Optimizer User Interface
feature: Accessibility
role: User
level: Beginner
exl-id: d971c04c-9b37-4cd7-8a2d-b915e394079b
TQID: https://experienceleague.adobe.com/ONswG5tDxJQKJ7xm-7zlXk1HE0G7Y927Qbsdiahzf5E
product_v2:
  - id: cb954087-f4fc-4456-afb9-e939cabcdc79
    internal-label: Journey Optimizer
feature_v2:
  - id: b3538224-471e-4c63-a444-9b19d89ae29c
    internal-label: Activities
  - id: d556b755-390a-43f0-be32-a08cf6236126
    internal-label: Configuration
  - id: d998adac-2f81-400b-a669-d07bb196e4eb
    internal-label: Journeys
  - id: fe338112-e2ce-4876-8989-fc4d497613f1
    internal-label: Email
subfeature_v2:
  - id: b3a93754-a8b8-46eb-9421-7eccaeeb3dff
    internal-label: Best practices
  - id: f550d0f2-143d-4093-9463-467fbec95fcc
    internal-label: Accessibility
role_v2:
  - id: b69b2659-1057-424e-8fc5-ed9e016dc554
    internal-label: User
level_v2:
  - id: e8ccd51f-da0d-4e3b-939b-e30d5ebb1ea5
    internal-label: Beginner
topic_v2:
  - id: cc72dcf1-72e1-48cc-b434-e7c27d62d67c
    internal-label: Accessibility
  - id: e9001ce2-5245-4a8e-8601-dd958009072f
    internal-label: Web experience
---
# Accessibility in Journey Optimizer{#accessibility}

Accessibility refers to a series of features that make a software product usable, with as little effort as possible, for users with visual, auditory, cognitive, motor, or other kinds of disabilities. Adobe is an industry leader in accessibility and supports the creation of outstanding web experiences by encouraging developers to produce rich, engaging content that is accessible to all users. Learn more about Adobe's commitment to accessibility in the [Adobe Accessibility page](https://www.adobe.com/accessibility.html){target="_blank"}.

To help meet the goal of accessibility conformance, [!DNL Journey Optimizer] follows the internationally recognized best practices in the Web Content Accessibility Guidelines (WCAG) 2.1 Level A and Level AA. Learn more in the latest [Adobe Journey Optimizer Accessibility Conformance Report](https://www.adobe.com/accessibility/compliance/adobe-journey-optimizer.html){target="_blank"}.

>[!NOTE]
>
>Guidelines to design accessible content for your emails and landing pages are detailed in [this section](../email/accessible-content.md).

The accessibility features in [!DNL Adobe Journey Optimizer] are inherited from Adobe Experience Platform:

* Keyboard accessibility
* Color contrast
* Validation of required fields

Accessibility features in Adobe Experience Platform are detailed [in this documentation](https://experienceleague.adobe.com/docs/experience-platform/accessibility/features.html){target="_blank"}.

The following common keyboard shortcuts are available in [!DNL Journey Optimizer]:

| Action | Shortcut |
| --- | --- |
| Move between user interface elements, sections, and menu groups | Tab |
| Move backward between user interface elements, sections, and menu groups | Shift + Tab |
| Move within sections to set focus to individual elements | Arrow |
| Select or clear an element that is in focus | Enter or Spacebar |
| Cancel a selection, collapse a pane, or close a dialog box | Esc |

You can use these shortcuts in specific areas of [!DNL Journey Optimizer] user interface:

<table>
  <thead>
    <tr>
      <th>Interface element</th>
      <th>Action</th>
      <th>Shortcut</th>
    </tr>
  </thead>
  <tr>
    <td rowspan="8">Journey canvas in draft status</td>
    <td>Add an activity from the left palette at the first available position, from top to bottom</td>
    <td>Double-click on the activity</td>
  </tr>
  <tr>
    <td>Select all the activities</td>
    <td>CTRL + A (Windows)<br/>CMD + A (Mac)</td>
  </tr>
  <tr>
    <td>Delete the selected activities</td>
    <td>Delete or Backspace, then Enter to confirm the deletion</td>
  </tr>
  <tr>
    <td>Zoom in and out (focus on canvas or any of its child elements)</td>
    <td>CTRL +/- (Windows) or CMD +/- (Mac)</td>
  </tr>  
  <tr>
    <td>Navigate between each activity and path (focus on canvas), or between toolbar buttons (focus on toolbar)</td>
    <td>ARROW keys</td>
  </tr>   
  <tr>
    <td>Move focus to the next actionable element on the canvas, the toolbar being the first one</td>
    <td>Tab</td>
  </tr>  
  <tr>
    <td>Open the right configuration pane (focus on an activity)</td>
    <td>ENTER</td>
  </tr>   
  <tr>
    <td>Move an activity in the canvas (focus on an activity)</td>
    <td>SHIFT + ARROW keys</td>
  </tr>  
  <tr>
  <td rowspan="3">
  Configuration pane of these elements:
<ul>
  <li>Activity in a journey</li>
  <li>Event</li>
  <li>Data source</li>
  <li>Action</li>
</ul>
  </td>
    <td>Move to the next field to be configured</td>
    <td>Tab</td>
  </tr>
  <tr>
    <td>Save changes and close the configuration pane</td>
    <td>Enter</td>
  </tr>
  <tr>
    <td>Discard changes and close the configuration pane</td>
    <td>Esc</td>
  </tr>
<!--
 //Ajouter ce raccourci quand il marchera (actuellement, le raccourci Ctrl/Cmd+F du navigateur a priorité sur celui de AJO).//
  <tr>
    <td>Page with a search bar</td>
    <td>Select the search bar</td>
    <td>Ctrl/Command + F</td>
  </tr>
-->
  <tr>
    <td>Text field</td>
    <td>Select all the text in the selected field</td>
    <td>Ctrl + A (Windows)<br/>Command + A (Mac)</td>
  </tr>
  <tr>
    <td rowspan="2">Pop-up window</td>
    <td>Save changes or confirm the action</td>
    <td>Enter</td>
  </tr>
  <tr>
    <td>Close the window</td>
    <td>Esc</td>
  </tr>
  <tr>
    <td>Simple expression editor</td>
    <td>Select and add a field</td>
    <td>Double-click on a field</td>
  </tr>
  <tr>
    <td>Browsing through XDM fields</td>
    <td>Select all the fields of a node</td>
    <td>Select the parent node</td>
  </tr>
  <tr>
    <td>Payload preview</td>
    <td>Select the payload</td>
    <td>Ctrl + A (Windows)<br/>Command + A (Mac)</td>
  </tr>
</table>
