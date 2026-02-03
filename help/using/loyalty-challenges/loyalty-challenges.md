---
solution: Journey Optimizer
product: journey optimizer
title: Loyalty Challenges
description: Learn how to create and manage loyalty challenges in Adobe Journey Optimizer to create engaging loyalty programs.
feature: Loyalty challenges
topic: Journeys
role: User
level: Intermediate
hide: yes
hidefromtoc: yes
badge: label="Private beta" type="Informative"
version: Journey Orchestration
---

# Loyalty Challenges {#loyalty-challenges}

>[!AVAILABILITY]
>
>This feature is currently in **private beta** and may not be available in your environment. Contact your Adobe representative to gain access.

Loyalty Challenges enables you to create personalized engagement offers for your customers, helping you orchestrate loyalty programs at scale. You can design challenges with specific tasks and milestones, reward customers for completing them, and deliver the experience through Adobe Journey Optimizer channels.

>[!BEGINSHADEBOX]
>
>**In this guide:**
>
>* [Overview](#overview) - Understand what Loyalty Challenges offers
>* [How it works](#how-it-works) - Step-by-step workflow from setup to monitoring
>* [Prerequisites](#prerequisites) - Set up data ingestion and permissions
>* [Access Loyalty Challenges](#access) - Open the menu and view challenges
>* [Create challenges](#create-challenges) - Build new loyalty challenges
>* [Create tasks](#create-tasks) - Define what customers must do
>* [Manage challenges](#manage-challenges) - Edit, monitor, and optimize
>
>[!ENDSHADEBOX]

## Overview {#overview}

Loyalty Challenges enables you to design and deploy personalized engagement offers that motivate customers to complete specific actions and earn rewards. The feature provides a complete solution for creating loyalty programs at scale, from defining tasks and milestones to delivering content and tracking performance across channels. You can create three types of challenge experiences, configure rewards, send multi-channel notifications at key lifecycle stages, and monitor performance through automatically generated journeys—all while maintaining integration with your external loyalty management system.

## How it works {#how-it-works}

Creating and launching a loyalty challenge follows this workflow:

1. **Set up data ingestion** - Configure Experience Platform source connectors (like Capillary) to ingest loyalty event data that tracks customer actions and progress.

2. **Create a challenge** - Define the basic challenge properties including name, type (Standard, Streak, or Sequential), audience, and date range.

3. **Add tasks** - Define the specific actions customers must complete, including task types (purchase, spend, visit, etc.), quantities, product filters, and rewards.

4. **Design content cards** - Create the visual representation of your challenge using Journey Optimizer content cards that display on customer devices.

5. **Configure messaging** (Optional) - Set up multi-channel messages (in-app, email, push) for key stages: launch, in-progress, and completion.

6. **Review and publish** - Test your challenge with test profiles, then publish it to make it available to your target audience.

7. **Auto-generated journey** - When you publish, Journey Optimizer automatically creates a journey that orchestrates content card delivery and messaging.

8. **Activate journey** - The auto-generated journey activates on your challenge start date and manages all customer interactions.

9. **Monitor performance** - Track participation, completion rates, rewards distribution, and message engagement through built-in reports and the journey canvas.

>[!NOTE]
>
>The auto-generated journey appears in your journey inventory and can be customized if needed. However, changes made directly to the journey do not sync back to the challenge configuration.

## Key capabilities

Use Loyalty Challenges to:

* **Create three types of challenges**:
  * **Standard**: Customers complete any number of tasks to earn rewards.
  * **Streak**: Customers complete the same task multiple times.
  * **Sequential**: Customers complete tasks in a specific order.

* **Design challenge content**: Use Journey Optimizer content cards to create the visual representation of your challenge on customer devices. Content cards display the challenge information, progress, and rewards on the customer's device.

* **Set up task requirements**: Define what customers must do to earn rewards, including:
  * Task types (purchase, spend amount, visit, etc.)
  * Quantity requirements
  * Product inclusions/exclusions using SKUs
  * Custom attributes and conditions

* **Configure rewards**: Define rewards that customers earn either at task completion or after completing the entire challenge

* **Send notifications**: Deliver messages across multiple channels (in-app, email, push) at key stages:
  * **Launch**: When the challenge starts
  * **In progress**: When customers are partway through
  * **Complete**: When customers finish the challenge

* **Track performance**: Monitor automatically generated journeys and review challenge performance

### Important limitations {#limitations}

* **No ledger system**: Loyalty Challenges does not track monetary values or point balances. When customers complete a challenge and earn a reward, Journey Optimizer calls your external loyalty management system to handle point allocation.

* **Audience selection only**: You can select existing audiences but cannot create new audiences from the Loyalty Challenges UI.

## Prerequisites {#prerequisites}

Before using Loyalty Challenges, ensure you have:

* Data ingestion setup

   Loyalty Challenges relies on data ingested through Experience Platform source connectors to track customer progress and task completion.

   1. **Configure a supported source connector**: Currently, the Capillary connector is generally available. Additional connectors are planned.

   2. **Validate data ingestion**: Ensure that loyalty events and customer data are flowing into Experience Platform and available in Journey Optimizer.

   For detailed instructions, see:

   * [Experience Platform sources documentation](https://experienceleague.adobe.com/en/docs/experience-platform/sources/home)
   * [Configure source connectors in Journey Optimizer](../start/get-started-sources.md)

* Required permissions {#required-permissions}

To use Loyalty Challenges, you need appropriate permissions in Journey Optimizer. Contact your administrator if you cannot access the feature.

## Access Loyalty Challenges {#access}

To access Loyalty Challenges:

1. In Adobe Journey Optimizer, select **[!UICONTROL Loyalty challenges]** in the left navigation menu.

   <!--![Loyalty challenges menu in left navigation](assets/loyalty-challenges-menu.png)-->

2. The Loyalty Challenges inventory displays all existing challenges with information such as:
   * Challenge name and description
   * Status (Draft, Live, Stopped, etc.)
   * Challenge type (Standard, Streak, Sequential)
   * Start and end dates
   * Last modification date

   <!--![Loyalty challenges inventory showing list of challenges](assets/loyalty-challenges-inventory.png)-->

3. Select **[!UICONTROL Create challenge]** to start creating a new challenge.

### Search and filter challenges {#search-filter}

Use search and filtering capabilities to quickly find specific challenges:

#### Search {#search}

Enter challenge name or keywords to find matching challenges in **[!UICONTROL Search]** field.

#### Filter by status {#filter-by-status}

Display challenges with specific statuses in **[!UICONTROL Filter by status]**:

* Draft
* Scheduled
* Live
* Completed
* Stopped
* Archived

#### Filter by type {#filter-by-type}

Show only Standard, Streak, or Sequential challenges using **[!UICONTROL Filter by type]**.

#### Filter by date {#filter-by-date}

Display challenges within a specific date range using **[!UICONTROL Filter by date]**.

#### Filter by tags {#filter-by-tags}

Show challenges with specific tags applied using **[!UICONTROL Filter by tags]**.


**[!UICONTROL Discount]**: Provide a discount code or value.

* Enter discount type (percentage or fixed amount)
* Enter discount value
* Optionally specify discount code or let the system generate one

**[!UICONTROL Free item]**: Grant a free product or service.

* Specify the item SKU or description
* Indicate how the free item should be claimed

**[!UICONTROL Custom reward]**: Define a custom reward type.

* Enter reward description
* Provide any relevant codes or identifiers
* Configure how the reward is delivered or claimed

#### Reward configuration example {#reward-example}

**Challenge**: "Coffee Lover Challenge"

**Task 1**: Purchase 3 coffees

* Reward: 30 points (10 points per coffee)
* Timing: After task completion

**Task 2**: Try 2 new seasonal drinks

* Reward: 50 points
* Timing: After task completion

**Challenge completion reward**:

* Reward: Free coffee + 100 bonus points
* Timing: After all tasks complete

**Total possible rewards**: 180 points + 1 free coffee

### Advanced task attributes {#advanced-attributes}

For advanced use cases, you can configure additional task attributes:

**[!UICONTROL Custom conditions]**: Add custom logic or conditions beyond standard task types using Experience Platform segments or rules.

**[!UICONTROL Geofencing]**: (For Visit tasks) Require visits to specific locations defined by geographic coordinates and radius.

**[!UICONTROL Time-based requirements]**: Require tasks to be completed during specific hours, days, or date ranges.

**[!UICONTROL Cooldown period]**: Set a minimum time between task completions to prevent rapid repeated actions.

**[!UICONTROL Task dependencies]**: (For Sequential challenges) Define prerequisites that must be completed before this task becomes available.

## Create challenges {#create-challenges}

Create a loyalty challenge to define the engagement offer, configure content cards for delivery, add tasks, set up rewards, and optionally configure messaging across channels.

### Before you start {#before-you-start}

Before creating a challenge, ensure you have:

* Configured and validated data ingestion through source connectors
* Created any required audiences in Experience Platform
* Prepared content assets (images, text, etc.) for your challenge
* Defined the tasks and rewards you want to offer

### Create a challenge {#create-a-challenge}

To create a new loyalty challenge:

1. In Journey Optimizer, select **[!UICONTROL Loyalty challenges]** in the left navigation menu.

2. Select **[!UICONTROL Create challenge]** in the upper right corner.

   <!--![Create challenge button in loyalty challenges inventory](assets/create-challenge-button.png)-->

3. In the challenge properties screen, configure the following:

#### Basic properties {#basic-properties}

**[!UICONTROL Name]**: Enter a descriptive name for your challenge. This name appears in the inventory and is included in the auto-generated journey name.

**[!UICONTROL Description]**: (Optional) Add a description to help you and your team understand the purpose and details of this challenge.

**[!UICONTROL Challenge type]**: Select the type of challenge you want to create:

* **[!UICONTROL Standard]**: Customers can complete any number of specified tasks in any order to earn the reward. Example: "Make 5 purchases this month."

* **[!UICONTROL Streak]**: Customers must complete the same task repeatedly. Example: "Visit our store 10 times in a row."

* **[!UICONTROL Sequential]**: Customers must complete tasks in a specific order. Example: "First make a purchase, then write a review, then refer a friend."

<!--![Challenge type selection showing Standard, Streak, and Sequential options](assets/challenge-type-selection.png)-->

**[!UICONTROL Start date]**: Select when the challenge becomes active and available to customers.

**[!UICONTROL End date]**: Select when the challenge expires. Customers who have not completed the challenge by this date will no longer be able to earn the reward.

#### Audience selection {#audience-selection}

**[!UICONTROL Select audience]**: Choose the audience that is eligible for this challenge. You can only select existing audiences; you cannot create new audiences from the Loyalty Challenges UI.

To create or refine audiences, see [Build audiences in Journey Optimizer](../audience/about-audiences.md).

1. Select **[!UICONTROL Save as draft]** to continue configuring your challenge.

## Create tasks {#create-tasks}

Tasks define the specific actions or milestones that customers must complete to earn rewards in a loyalty challenge. You can configure task types, quantities, product requirements, and reward values to create engaging and personalized loyalty experiences.

### Task overview {#task-overview}

Each task represents a measurable action that contributes toward challenge completion. Depending on your challenge type (Standard, Streak, or Sequential), customers complete tasks differently:

* **Standard challenges**: Customers complete any specified number of tasks in any order
* **Streak challenges**: Customers complete the same task multiple times consecutively
* **Sequential challenges**: Customers complete tasks in a defined order

### Add a task {#add-task}

To add a task to your challenge:

1. Open your challenge or create a new one.

2. Navigate to the **[!UICONTROL Tasks]** section.

   <!--![Tasks section in challenge creation interface](assets/tasks-section.png)-->

3. Select **[!UICONTROL Add task]** or **[!UICONTROL Create new task]**.

4. In the task creation screen, configure the following properties.

### Task properties {#task-properties}

#### Basic task information {#basic-info}

**[!UICONTROL Task name]**: Enter a descriptive name for the task. This name is visible to you and your team but may not be shown to customers depending on your content card design.

**[!UICONTROL Task description]**: (Optional) Add details about the task purpose or requirements.

**[!UICONTROL Task type]**: Select the type of action customers must perform. Available task types include:

* **[!UICONTROL Purchase]**: Customer makes a purchase transaction
* **[!UICONTROL Spend amount]**: Customer spends a specified monetary amount
* **[!UICONTROL Visit]**: Customer visits a physical location or digital property
* **[!UICONTROL Engagement]**: Customer engages with content, such as viewing a video or reading an article
* **[!UICONTROL Custom event]**: Customer triggers a custom event tracked through your data ingestion

<!--![Task type selection dropdown showing available task types](assets/task-type-selection.png)-->

#### Quantity requirements {#quantity-requirements}

**[!UICONTROL Required quantity]**: Specify how many times the customer must perform the task to complete it.

For example:

* For a Purchase task: "Buy 2 items" (quantity = 2)
* For a Spend amount task: "Spend $50" (quantity = 50)
* For a Visit task: "Visit 5 times" (quantity = 5)

**[!UICONTROL Tracking period]**: (Optional) Define the time window for completing this task:

* Per challenge duration (default)
* Per day
* Per week
* Per month
* Custom date range

### Product and SKU filtering {#product-filtering}

For Purchase and Spend amount tasks, you can specify which products qualify toward task completion.

#### Product inclusions {#product-inclusions}

Define which products or categories count toward the task:

1. Select **[!UICONTROL Add product criteria]**.

   <!--![Add product criteria button in task configuration](assets/add-product-criteria.png)-->

2. Choose how to define qualifying products:
   * **[!UICONTROL By SKU]**: Enter specific product SKU codes
   * **[!UICONTROL By category]**: Select product categories from your catalog
   * **[!UICONTROL By attribute]**: Filter by product attributes such as brand, size, color, or custom attributes

3. Enter or select the product identifiers:

   **Example - By SKU**:

   ```text
   SKU001, SKU002, SKU003
   ```

   **Example - By category**:

   * Beverages > Coffee
   * Bakery > Pastries

   **Example - By attribute**:

   * Brand = "Premium Brand"
   * Category = "Seasonal Items"
   * Price > $20

4. Select **[!UICONTROL Add]** to save the product criteria.

#### Product exclusions {#product-exclusions}

Optionally, exclude specific products from counting toward the task:

1. Select **[!UICONTROL Add exclusions]**.

2. Use the same filtering methods as product inclusions to specify which products should be excluded.

3. Common exclusion scenarios:

   * Sale or clearance items
   * Gift cards
   * Promotional or free items
   * Specific brands or categories

>[!NOTE]
>
>**Inclusion and exclusion logic**: When both inclusions and exclusions are defined:
>
>* Products must match inclusion criteria
>* Products matching exclusion criteria are removed, even if they match inclusions
>* If no inclusions are defined, all products qualify except those explicitly excluded

#### Examples of product filtering {#product-filtering-examples}

##### Example 1: Coffee challenge {#example-1}

* Task type: Purchase
* Required quantity: 3
* Inclusions: Category = "Beverages > Coffee"
* Result: Customer must purchase 3 coffee beverages

##### Example 2: Premium spending {#example-2}

* Task type: Spend amount
* Required quantity: $100
* Inclusions: Brand = "Premium Brand"
* Exclusions: Category = "Clearance"
* Result: Customer must spend $100 on Premium Brand items, excluding clearance items

##### Example 3: Specific product purchase {#example-3}

* Task type: Purchase
* Required quantity: 1
* Inclusions: SKU = "NEWPRODUCT2024"
* Result: Customer must purchase the specific product with SKU "NEWPRODUCT2024"

### Configure rewards {#configure-rewards}

Define what customers earn for completing tasks. Rewards can be granted at the task level or at the challenge level after all tasks are complete.

#### Reward timing {#reward-timing}

Choose when customers receive rewards:

**[!UICONTROL After task completion]**: Customers receive a reward immediately after completing this specific task (also called "progressive rewards" or "milestone rewards").

**[!UICONTROL After challenge completion]**: Customers receive a reward only after completing all required tasks in the challenge (also called "final rewards" or "grand prizes").

>[!TIP]
>
>You can combine both reward types in a single challenge to maintain engagement throughout the customer journey. For example:
>
>* Give 10 points after each task completion (progressive rewards)
>* Give an additional 100 points after completing the entire challenge (final reward)

#### Reward types and values {#reward-types}

**[!UICONTROL Points]**: Award loyalty points to the customer's account.

* Enter the number of points (e.g., 100)
* Points are communicated to your external loyalty management system via API
## Configure content cards {#configure-content-cards}

Content cards are the primary way challenges are displayed to customers on their devices. You must configure a content card for your challenge.

1. In your challenge, navigate to the **[!UICONTROL Content]** tab.

2. Select **[!UICONTROL Edit content]** to open the content card editor.

   <!--![Content tab with Edit content button](assets/content-tab-edit.png)-->

3. Configure the content card properties:

   **[!UICONTROL Configuration name]**: Enter a name for this content card configuration.

   **[!UICONTROL Configuration]**: Select or create a content card configuration. This defines technical settings for how the content card is delivered.

4. In the content card editor, design your challenge card:

   * Add text to describe the challenge, tasks, and rewards
   * Include images or other visual elements
   * Use personalization to include customer-specific information
   * Display progress indicators if applicable
   * Add call-to-action buttons

   The content card editor provides the same capabilities as other Journey Optimizer channels. For detailed guidance, see [Design content cards](../content-card/design-content-card.md).

5. Select **[!UICONTROL Save]** to save your content card configuration.

>[!NOTE]
>
>The content card is delivered through the auto-generated journey. It is displayed to eligible audience members when the challenge is active.

## Configure messaging {#configure-messaging}

You can optionally configure messages to be sent to customers at key stages of the challenge lifecycle. Messaging is available for three stages:

* **[!UICONTROL Launch]**: Send a message when the challenge becomes active
* **[!UICONTROL In progress]**: Send a message when customers are partway through the challenge
* **[!UICONTROL Complete]**: Send a message when customers complete the challenge

### Add messages {#add-messages}

1. In your challenge, navigate to the **[!UICONTROL Messaging]** tab.

   <!--![Messaging tab showing Launch, In progress, and Complete stages](assets/messaging-tab-stages.png)-->

2. Select the stage where you want to add a message: Launch, In progress, or Complete.

3. Select **[!UICONTROL Add message]**.

4. Choose the channel for your message:
   * **[!UICONTROL In-app]**: Display a message within your application
   * **[!UICONTROL Email]**: Send an email notification
   * **[!UICONTROL Push]**: Send a push notification

5. Select **[!UICONTROL Edit content]** to open the content editor for the selected channel.

6. Design your message using the standard content editor:
   * Add text, images, and other content elements
   * Use personalization to include customer-specific information
   * Include challenge details like progress or rewards
   * Add dynamic content based on customer attributes or behaviors

   For channel-specific guidance, see:
   * [Create in-app messages](../in-app/create-in-app.md)
   * [Create emails](../email/create-email.md)
   * [Create push notifications](../push/create-push.md)

7. Select **[!UICONTROL Save]** to save your message.

8. Repeat these steps to add messages for other stages or channels as needed.

>[!NOTE]
>
>You can add multiple messages per stage, allowing you to reach customers across different channels. For example, you might send both an email and a push notification when a challenge launches.

### Message timing and triggers {#message-timing}

**Launch messages**: Sent when the challenge becomes active to the eligible audience.

**In progress messages**: Triggered when customers reach a specified progress point. You can configure the trigger conditions based on:

* Number of tasks completed
* Percentage of challenge completed
* Specific task completion
* Time elapsed since challenge start

**Complete messages**: Sent when customers successfully complete all required tasks.

>[!TIP]
>
>**Best practices for messaging**:
>
>* Keep messages concise and focused on the challenge
>* Clearly communicate the value and rewards
>* Use consistent branding and tone
>* Include clear calls to action
>* Test messages before publishing your challenge

## Generate and customize journeys {#generate-journey}

When you save a challenge with content and messaging configured, Journey Optimizer automatically generates a journey in the backend.

### How journey generation works {#journey-generation-process}

1. When you save a challenge and select **[!UICONTROL Generate journey]**, Journey Optimizer creates a new journey.

2. The journey is automatically named based on the challenge name (e.g., "Challenge: [Your Challenge Name]").

3. The journey canvas includes:
   * **[!UICONTROL Read audience]** activity with the audience you selected
   * **Content card** delivery action
   * **Message activities** for any messages you configured (Launch, In progress, Complete)
   * **Wait** and **Condition** activities as needed based on your configuration

   <!--![Auto-generated journey canvas showing content card and message activities](assets/generated-journey-canvas.png)-->

4. The journey appears in your journey inventory and is visible to all users with appropriate permissions.

### View the generated journey {#view-journey}

To view the auto-generated journey:

1. Navigate to **[!UICONTROL Journeys]** in the left navigation menu.

2. Search for the journey by challenge name, or filter by tags if you've assigned them.

3. Select the journey to view its canvas and configuration.

### Customize the journey {#customize-journey}

You can edit the auto-generated journey to add custom logic, additional activities, or advanced configurations.

>[!IMPORTANT]
>
>**Important considerations when editing journeys**:
>
>* Changes made to the journey canvas **do not sync back** to the Loyalty Challenges UI
>* The challenge remains the source of truth for the core experience definition
>* Journey Optimizer displays a warning when you enter custom edit mode
>* If you need to make changes to tasks, rewards, or core challenge properties, edit them in the Loyalty Challenges UI, not the journey
>* Custom journey edits are appropriate for advanced routing, timing, or integration logic

To customize the journey:

1. Open the generated journey from the journey inventory.

2. Journey Optimizer displays a warning about custom editing. Read the warning carefully and acknowledge it.

3. Make your desired changes using the journey canvas:
   * Add additional activities (waits, conditions, actions)
   * Configure advanced timing or frequency rules
   * Add custom actions or integrations
   * Modify audience entry conditions

4. Test your changes thoroughly before publishing.

5. Publish the journey when ready.

For detailed journey editing guidance, see [Build journeys](../building-journeys/journey-gs.md).

### Journey canvas considerations {#journey-considerations}

When working with auto-generated journeys:

* **Cannot edit audience in journey**: If you need to change the audience, do so in the Loyalty Challenges UI and regenerate the journey.

* **Message content updates**: Changes to message content should be made in the Loyalty Challenges UI to maintain consistency.

* **Journey status**: The journey status (Draft, Live, Stopped) is managed independently from the challenge status.

* **Testing**: Test the entire challenge experience, not just the journey, to ensure all components work together correctly.

## Review and publish {#review-and-publish}

Before publishing your challenge:

1. **Review all components**:
   * Challenge properties and dates
   * Tasks and task requirements
   * Rewards configuration
   * Content card design
   * Messaging content and timing
   * Generated journey structure

2. **Test the experience**:
   * Use test profiles to validate content rendering
   * Check that tasks trigger correctly based on test data
   * Verify reward allocation logic
   * Test messaging across all configured channels
   * Review the journey execution with test audiences

3. **Publish your challenge**:
   * When ready, select **[!UICONTROL Publish]** from the challenge properties
   * The challenge becomes active on the specified start date
   * The auto-generated journey is activated
   * Eligible audience members can see and participate in the challenge

## Manage challenges {#manage-challenges}

After creating and publishing loyalty challenges, you can view, edit, monitor, and optimize them to ensure they deliver the desired results for your loyalty program.

### Challenge statuses {#challenge-statuses}

Each challenge moves through a lifecycle reflected by its status:

**[!UICONTROL Draft]**: Challenge is being created or edited but not yet published. You can make any changes to draft challenges.

**[!UICONTROL Scheduled]**: Challenge is published and becomes active on its start date. Customers cannot yet see or participate in scheduled challenges.

**[!UICONTROL Live]**: Challenge is active and customers in the eligible audience can see and participate in it. This status appears when the current date is between the start and end dates.

**[!UICONTROL Completed]**: Challenge has passed its end date or all objectives have been met. Customers can no longer participate, but you can view historical data and results.

**[!UICONTROL Stopped]**: Challenge was manually stopped before completion. Customers can no longer participate. To reactivate a stopped challenge, you must duplicate it and create a new version.

**[!UICONTROL Archived]**: Challenge has been archived for organizational purposes. Archived challenges can be retrieved using filters but are hidden from the default view.

### View challenge details {#view-details}

To view detailed information about a challenge:

1. In the inventory, click on the challenge name or select the **[!UICONTROL More actions]** menu (three dots) and choose **[!UICONTROL View details]**.

   <!--![Challenge inventory with More actions menu highlighted](assets/challenge-more-actions.png)-->

2. The challenge details screen displays:

   **[!UICONTROL Overview]** tab:
   * Basic properties (name, description, type, dates)
   * Current status and lifecycle information
   * Audience information
   * Creation and modification history

   **[!UICONTROL Tasks]** tab:
   * List of all tasks in the challenge
   * Task types, requirements, and conditions
   * Configured rewards per task

   **[!UICONTROL Content]** tab:
   * Content card configuration and preview
   * Visual rendering of how the challenge appears to customers

   **[!UICONTROL Messaging]** tab:
   * Configured messages for Launch, In progress, and Complete stages
   * Channel assignments and content previews

   **[!UICONTROL Performance]** tab (for Live and Completed challenges):
   * Participation metrics
   * Completion rates
   * Reward distribution
   * Message engagement statistics

### Edit challenges {#edit-challenges}

You can edit challenges depending on their current status.

#### Edit draft challenges {#edit-draft}

For challenges in **[!UICONTROL Draft]** status:

1. Click on the challenge name or select **[!UICONTROL Edit]** from the actions menu.

2. Modify any aspect of the challenge:
   * Basic properties
   * Tasks and rewards
   * Content cards
   * Messaging
   * Audience selection

3. Select **[!UICONTROL Save as draft]** to save changes without publishing, or **[!UICONTROL Publish]** to make the challenge active.

#### Edit published challenges {#edit-published}

For challenges that are **[!UICONTROL Scheduled]** or **[!UICONTROL Live]**:

>[!IMPORTANT]
>
>**Impact of editing live challenges**: Changes to live challenges may affect customers already participating. Consider the following before making changes:
>
>* Modifying task requirements may invalidate customer progress
>* Changing rewards may create inconsistencies for customers who have already earned rewards
>* Audience changes may exclude customers who were previously eligible
>* Content changes appear immediately to customers
>
>For significant changes, consider stopping the current challenge and creating a new version.

**Limited editing for live challenges**:

You can make these changes to live challenges without stopping them:

* Update challenge description (internal-facing)
* Modify content card visuals and text
* Update messaging content
* Adjust end date (extend only, cannot shorten)
* Add or modify tags

**Changes requiring challenge duplication**:

To change these properties, you must duplicate the challenge and create a new version:

* Challenge type (Standard, Streak, Sequential)
* Task requirements and conditions
* Reward values and allocation rules
* Start date (for live challenges)
* Audience (major changes)

### Duplicate a challenge {#duplicate-challenge}

Duplicating creates a copy of an existing challenge that you can modify and publish as a new challenge:

1. In the inventory, select the **[!UICONTROL More actions]** menu (three dots) for the challenge you want to duplicate.

2. Select **[!UICONTROL Duplicate]**.

3. In the duplication dialog:
   * Enter a new name for the duplicated challenge
   * Optionally modify the description
   * Choose whether to copy audience settings
   * Choose whether to copy messaging configurations

4. Select **[!UICONTROL Duplicate]**.

5. The duplicated challenge opens in draft mode, where you can make changes before publishing.

**Common duplication scenarios**:

* Rerun a successful challenge for a new time period
* Create variations of a challenge for different audiences
* Update task requirements or rewards for a new version
* Reactivate a stopped or completed challenge

### Stop a challenge {#stop-challenge}

To stop a live or scheduled challenge before its natural end date:

1. Select the challenge in the inventory.

2. Select **[!UICONTROL Stop challenge]** from the actions menu.

3. In the confirmation dialog, review the impact:
   * Customers currently participating can no longer make progress
   * Customers who have completed tasks but not the full challenge will not receive final rewards
   * The associated journey is stopped
   * The challenge cannot be restarted (must duplicate to reuse)

4. Select **[!UICONTROL Stop]** to confirm.

>[!NOTE]
>
>**Stopping vs. completing**: A stopped challenge ends prematurely and does not follow the normal completion process. Customers receive partial rewards already allocated but not final challenge completion rewards. Consider communicating the early end to affected customers.

### Archive challenges {#archive}

Archive completed or stopped challenges to keep your inventory organized:

1. Select the **[!UICONTROL More actions]** menu (three dots) for the challenge.

2. Select **[!UICONTROL Archive]**.

3. The challenge moves to archived status and is hidden from the default inventory view.

To view archived challenges:

1. In the inventory, apply the **[!UICONTROL Status]** filter.

2. Select **[!UICONTROL Archived]**.

3. Archived challenges display with the same information as active challenges.

To unarchive a challenge:

1. Find the archived challenge using filters.

2. Select **[!UICONTROL Unarchive]** from the actions menu.

3. The challenge returns to its previous status (Completed or Stopped).

### Delete challenges {#delete}

Delete challenges that are no longer needed:

>[!IMPORTANT]
>
>**Deletion is permanent**: Deleted challenges cannot be recovered. Only delete challenges you are certain you will not need in the future. Consider archiving instead of deleting to maintain historical records.

**Deletion rules**:

* You can only delete challenges in **[!UICONTROL Draft]** status
* Published, scheduled, live, or completed challenges cannot be deleted
* To remove a published challenge, you must first stop it, then archive it

To delete a draft challenge:

1. Select the **[!UICONTROL More actions]** menu (three dots) for the challenge.

2. Select **[!UICONTROL Delete]**.

3. In the confirmation dialog, confirm the deletion.

## Monitor performance {#monitor-performance}

Track how customers engage with your challenges using built-in performance metrics.

### Performance metrics {#performance-metrics}

The Performance tab shows key metrics for live and completed challenges:

<!--![Performance metrics dashboard showing participation and completion data](assets/performance-metrics-dashboard.png)-->

**[!UICONTROL Participation metrics]**:

* **Total eligible customers**: Number of customers in the target audience
* **Enrolled customers**: Number of customers who viewed or engaged with the challenge
* **Enrollment rate**: Percentage of eligible customers who enrolled
* **Active participants**: Number of customers currently making progress

**[!UICONTROL Completion metrics]**:

* **Customers completed**: Number of customers who finished all tasks
* **Completion rate**: Percentage of enrolled customers who completed the challenge
* **Average completion time**: Average time from enrollment to completion
* **Tasks completed**: Total number of individual tasks completed across all customers

**[!UICONTROL Reward metrics]**:

* **Total rewards distributed**: Sum of all rewards allocated
* **Rewards by type**: Breakdown by points, discounts, free items, etc.
* **Average reward per customer**: Mean reward value for participating customers

**[!UICONTROL Engagement metrics]**:

* **Content card impressions**: Number of times the challenge was displayed
* **Content card clicks**: Number of times customers interacted with the challenge card
* **Message delivery**: Number of messages sent for Launch, In progress, and Complete stages
* **Message engagement**: Open rates, click rates for messages by stage and channel

### View performance reports {#view-reports}

To access detailed performance data:

1. Open the challenge and navigate to the **[!UICONTROL Performance]** tab.

2. Select the date range for reporting (Today, Last 7 days, Last 30 days, Custom range).

3. Review metrics by:
   * **Overview**: High-level summary of key metrics
   * **Timeline**: Performance trends over time
   * **Breakdown**: Metrics segmented by customer attributes, channels, or tasks

4. Export reports using the **[!UICONTROL Export]** button for further analysis.

### Monitor the generated journey {#monitor-journey}

The auto-generated journey contains valuable execution data:

1. From the challenge details, select **[!UICONTROL View journey]** to open the associated journey.

2. In the journey canvas, review:
   * **Journey report**: Overall execution statistics
   * **Activity reports**: Performance of individual activities
   * **Entry and exit metrics**: How many customers entered and exited
   * **Error logs**: Any execution issues or failures

3. Use journey monitoring to identify:
   * Bottlenecks where customers drop off
   * Technical issues affecting delivery
   * Message performance by channel
   * Timing optimization opportunities

For detailed journey monitoring guidance, see [Monitor your journeys](../building-journeys/report-journey.md).

### Optimize challenges {#optimize}

Use performance data to improve current and future challenges:

**[!UICONTROL Test variations]**: Create duplicate challenges with different tasks, rewards, or messaging to compare performance.

**[!UICONTROL Adjust timing]**: Modify challenge duration or task deadlines based on completion patterns.

**[!UICONTROL Refine audience]**: Expand or narrow audience selection based on engagement and completion rates.

**[!UICONTROL Update content]**: Refresh content cards and messaging to maintain interest and clarity.

**[!UICONTROL Reward optimization]**: Adjust reward values to balance cost and participation.

**[!UICONTROL Task difficulty]**: Modify task requirements if they are too easy or too difficult based on completion data.

## Task validation and testing {#validation-testing}

Before publishing your challenge, validate that tasks are configured correctly:

1. **Check task logic**:
   * Verify quantity requirements are realistic
   * Ensure product filtering criteria are correct
   * Confirm rewards are properly configured

2. **Test with test profiles**:
   * Create test profiles representing different customer scenarios
   * Send test events through your data ingestion pipeline
   * Verify that tasks trigger correctly
   * Confirm rewards are allocated as expected

3. **Review data mapping**:
   * Ensure that incoming event data maps correctly to task requirements
   * Validate that SKUs, categories, and attributes match between your source system and Journey Optimizer
   * Test edge cases (missing data, invalid values, etc.)

## Best practices {#best-practices}

### Challenge creation

**Start simple**: For your first challenge, start with a simple standard challenge to familiarize yourself with the process.

**Test thoroughly**: Always test your challenge with test profiles and audiences before publishing to your full customer base.

**Clear communication**: Ensure customers understand what they need to do, what they'll earn, and by when.

**Realistic timing**: Set appropriate start and end dates, allowing customers enough time to complete the challenge.

**Appealing rewards**: Make rewards valuable and relevant to your audience to drive participation.

### Task configuration

**Clear requirements**: Make task requirements clear and achievable. Avoid overly complex conditions.

**Appropriate difficulty**: Balance task difficulty with reward value. More difficult tasks should offer greater rewards.

**Product filtering accuracy**: Double-check SKUs, categories, and attributes to ensure accurate product matching.

**Progressive rewards**: Use milestone rewards (after task completion) to maintain customer engagement throughout the challenge.

**Flexibility**: For Standard challenges, allow flexibility in how customers complete tasks to accommodate different behaviors and preferences.

### Management and monitoring

**Regular monitoring**: Check challenge performance at least weekly for live challenges to identify issues early.

**Clear naming**: Use descriptive names that indicate the challenge purpose, audience, or time period for easy organization.

**Use tags**: Apply consistent tags to categorize challenges by campaign, season, audience segment, or other relevant attributes.

**Document changes**: Keep notes on why you made changes to challenges for future reference and learning.

**Archive consistently**: Archive completed challenges regularly to keep your inventory manageable.

**Communicate changes**: If you modify a live challenge, inform affected customers about changes that impact their participation.

**Analyze after completion**: Review performance after each challenge ends to identify lessons learned for future challenges.

**Gradual rollout**: For new challenge types or significant changes, consider starting with a smaller audience before full deployment.

**Version control**: Use clear versioning in challenge names when creating iterations (e.g., "Holiday Challenge 2024 - v2").

## Troubleshooting {#troubleshooting}

**Challenge not appearing to customers**:

* Verify the challenge is in Live status
* Check that customers are in the eligible audience
* Confirm the content card configuration is correct
* Review the journey execution logs for delivery issues

**Low participation rates**:

* Review content card visibility and appeal
* Check that messaging clearly communicates value
* Ensure tasks are achievable and rewards are attractive
* Verify audience targeting is appropriate

**Tasks not triggering**:

* Verify data is being ingested correctly from source connectors
* Check that event attributes match task requirements
* Review audience eligibility

**Rewards not allocating**:

* Confirm reward configuration is correct
* Verify connection to external loyalty management system
* Check for errors in reward delivery logs

**Product filtering not working**:

* Validate SKU codes and category names
* Ensure attribute mapping is correct
* Test with sample purchase data

**Journey not generating**:

* Confirm all required configuration is complete
* Check for errors in the Messaging tab
* Verify content card is configured
* Review system error logs

**Performance data not showing**:

* Allow time for data to propagate (up to 24 hours)
* Verify that events are being tracked correctly
* Check data ingestion status
* Ensure customers have begun participating

## Beta feedback {#beta-feedback}

During the beta phase, your feedback is valuable to help us improve Loyalty Challenges. Please share your experience, questions, and suggestions with your Adobe representative or through the beta feedback channels provided during kickoff.

## Related topics {#related-topics}

* [Build audiences in Journey Optimizer](../audience/about-audiences.md)
* [Design content cards](../content-card/design-content-card.md)
* [Create in-app messages](../in-app/create-in-app.md)
* [Create emails](../email/create-email.md)
* [Create push notifications](../push/create-push.md)
* [Build journeys](../building-journeys/journey-gs.md)
* [Monitor your journeys](../building-journeys/report-journey.md)
* [Experience Platform sources documentation](https://experienceleague.adobe.com/en/docs/experience-platform/sources/home)
* [Configure source connectors in Journey Optimizer](../start/get-started-sources.md)
