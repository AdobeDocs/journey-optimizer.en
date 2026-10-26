---
title: AI Knowledge Reference
---
# AI Knowledge Reference

+++ AI Knowledge Reference

This section contains structured knowledge intended to support interpretation, retrieval, and question answering related to this topic.

For complete understanding, this information should be combined with the documentation on this page. Neither source is intended to stand alone; the page describes the feature, while this section provides additional context that helps disambiguate terminology, intent, applicability, and constraints.

* **TL;DR:** This page explains how to access and manage loyalty challenges and reusable tasks, review challenge details and performance, and edit published challenges.

**Intents:**

* Access the Challenges and Tasks inventories
* Review challenge configuration and performance on the details page
* Review individual task details
* View or edit a published challenge
* Duplicate or delete challenges
* View, edit, duplicate, or delete reusable tasks

**Glossary:**

* **Challenge details**: The page that brings together a specific challenge's configuration and performance without opening its editor *(product-specific)*
* **[!UICONTROL State]**: The current state of the challenge, Draft or Published *(product-specific)*
* **[!UICONTROL Status]**: The current status of the auto-generated journey that delivers the challenge *(product-specific)*
* **[!UICONTROL Journey]**: A link to the auto-generated journey associated with the challenge *(product-specific)*
* **View Loyalty Insights**: The permission identified by `loyalty-insights.read` that controls access to the **[!UICONTROL Key metrics]** and **[!UICONTROL Trends]** sections *(product-specific)*
* **Tasks inventory**: The inventory of reusable tasks available when creating or editing challenges *(product-specific)*

**Guardrails:**

* The **[!UICONTROL Key metrics]** and **[!UICONTROL Trends]** sections are shown only to users with the **View Loyalty Insights** permission (`loyalty-insights.read`).
* Editing a published challenge requires reverting it to Draft state first. Reverting a published challenge to draft cannot be undone, and customizations made directly to the auto-generated journey are lost.
* After editing a published challenge, save and publish the challenge again, then publish its associated journey.
* A challenge can be deleted even when published. Consider the impact before deleting.
* A task can be deleted even when used in one or more challenges. Consider the impact on challenges that reference it before deleting.

**Terminology:**

* Do not confuse challenge **[!UICONTROL State]** (Draft or Published) with the **[!UICONTROL Status]** of its auto-generated journey.
* **[!UICONTROL Challenge summary]**, **[!UICONTROL Tasks]**, and **[!UICONTROL Rewards]** are sections of the **[!UICONTROL Details]** area; **[!UICONTROL Key metrics]** displays challenge performance.
* **[!UICONTROL Tasks]** in the challenges inventory is the number of tasks configured in a challenge; the Tasks inventory lists reusable task definitions.

**FAQ:**

* **Q: How do I open a challenge's details?** - Select the challenge name in the **[!UICONTROL Challenges]** inventory.
* **Q: What does the details page show?** - The header displays the challenge name, type, ID, and status. The Details area shows the challenge description, type, dates, targeted audience, connected journey and its status, task completion requirements, task names and descriptions, and reward details.
* **Q: Which performance metrics can I review?** - Total revenue, enrollment, completion rate, and total completions, with trend sparklines and percentage changes. Select **[!UICONTROL View report]** to explore challenge performance in more detail.
* **Q: Who can view Key metrics and Trends?** - Users with the **View Loyalty Insights** permission (`loyalty-insights.read`).
* **Q: How do I edit a published challenge?** - Select **[!UICONTROL Edit challenge]** on the details page. A published challenge first needs to be reverted to Draft state, which cannot be undone. Customizations made directly to the auto-generated journey are lost. After making changes, save and publish the challenge again, then publish the associated journey.
* **Q: What is preserved when I duplicate a challenge?** - A copy is created with all tasks, content, and messaging intact.

+++

<!-- ai-section-version: 2 | source-hash: 6b01b4aa -->