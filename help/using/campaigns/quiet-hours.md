---
solution: Journey Optimizer
product: journey optimizer
title: Quiet Hours
description: Learn how to prevent communications from being sent during specific periods using quiet hours rules
feature: Campaigns
topic: Content Management
role: User
level: Intermediate
keywords: quiet hours, time exclusions, business rules, rule sets, schedule, campaigns
hide: yes
hidefromtoc: yes
---
# Quiet Hours {#quiet-hours}

>[!AVAILABILITY]
>
>Quiet hours rules are currently only available for a set of organizations (Limited Availability). To be added to the waitlist, contact your Adobe representative.

Quiet hours let you define time-based exclusions for Email, SMS, Push, and WhatsApp channels. They ensure that no messages are sent during specific periods of time, helping you respect customer preferences and compliance requirements.

You can apply quiet hours through rule sets, which can be assigned to individual actions in campaigns or journeys for precise control.

## Why use Quiet Hours {#why-quiet-hours}

Quiet hours help you improve customer experience and maintain compliance in several ways:

* **Respect customer preferences**: Avoid sending messages during inconvenient times (e.g., late at night or early morning), which can negatively impact brand reputation and customer loyalty.

* **Improve engagement**: By sending messages when customers are more likely to see and act on them, you increase the effectiveness of your communications.

* **Legal compliance**: Certain states and regions prohibit SMS marketing messages during specific hours. Quiet hours help you stay compliant with regulations such as the TCPA and state-specific SMS laws.

* **Optimize timing**: If too much time has passed since a message was scheduled, it may no longer be relevant. Quiet hours allow you to either discard outdated messages or hold them until an appropriate time.

## How Quiet Hours work {#how-quiet-hours-work}

Quiet hours are implemented through business rules that you create and apply to your campaigns and journeys using rule sets.

When a message is scheduled to be sent during a quiet hours period, [!DNL Adobe Journey Optimizer] takes one of two actions based on your configuration:

* **Discard**: The message is permanently suppressed and never sent.
* **Queue**: The message is held and automatically sent as soon as the quiet hours period ends.

The system evaluates quiet hours based on the recipient's timezone, which can be:

* The timezone specified in the customer's profile
* An inferred timezone based on other profile and event data
* A fixed timezone that you specify in the rule

>[!NOTE]
>
>Pre-suppression window: The system begins suppressing communications 30 minutes before quiet hours start, ensuring that no messages are delivered once the quiet period begins.

## Create a Quiet Hours rule {#create-quiet-hours-rule}

To create a quiet hours rule:

1. Navigate to **[!UICONTROL Administration]** > **[!UICONTROL Business Rules]**.

1. In the **[!UICONTROL Rule sets]** section, create a new rule set or select an existing one to which you want to add the quiet hours rule.

1. Click **[!UICONTROL Create rule]** and select **[!UICONTROL Quiet Hours]** as the rule type.

1. Configure the quiet hours settings:

   * **Rule name**: Give your rule a descriptive name.
   
   * **Time period**: Define when quiet hours should apply:
      * **Hours of the day**: Set specific hours (e.g., 8:00 PM to 8:00 AM)
      * **Days of the week**: Select specific days (e.g., weekends)
      * **Custom dates**: Choose specific calendar dates (e.g., holidays)
   
   * **Timezone**: Select how to determine the timezone:
      * **User's local timezone**: Use the timezone from each recipient's profile
      * **Specific timezone**: Apply a fixed timezone (e.g., Eastern, Central)
   
   * **Action**: Choose what happens to messages during quiet hours:
      * **Discard**: Messages are permanently suppressed
      * **Queue**: Messages are held and sent when quiet hours end

1. Click **[!UICONTROL Save]** to create the rule.

## Apply Quiet Hours to campaigns and journeys {#apply-quiet-hours}

Once you have created a quiet hours rule, you need to apply it to your campaigns or journeys:

1. Open the campaign or journey where you want to apply quiet hours.

1. Navigate to the action (Email, SMS, Push, or WhatsApp) that you want to control.

1. In the action configuration, locate the **[!UICONTROL Rule set]** section.

1. Select the rule set that contains your quiet hours rule.

1. Save your changes.

The quiet hours rule will now apply to that specific action. All messages sent through this action will respect the quiet hours configuration.

>[!NOTE]
>
>Quiet hours rules apply to both scheduled and event-triggered communications. Make sure your rule set is properly configured to handle your use case.

## Timezone considerations {#timezone-considerations}

When using the **User's local timezone** option, [!DNL Adobe Journey Optimizer] looks for timezone information in the following order:

1. **Profile timezone attribute**: The timezone explicitly specified in the customer's profile
2. **Inferred timezone**: A timezone calculated based on other profile data and behavioral signals

If neither is available, the system may not apply quiet hours correctly. Ensure your customer profiles include timezone information for optimal results.

When using a **Specific timezone**, all recipients receive (or do not receive) messages based on that single timezone, regardless of their actual location.

## Guardrails and limitations {#guardrails-limitations}

Be aware of the following when using quiet hours:

* **Activation time**: It can take up to 20 minutes for a rule or rule set to be fully activated. Plan accordingly when creating or modifying rules.

* **Campaign activation delay**: After associating business rules, wait at least 10 minutes before activating a journey or sending a campaign to ensure rules are properly applied.

* **Rule set limits**: Currently, you can have up to 3 active rule sets for the channel domain and 5 for the journey domain.

* **Message release rate**: When quiet hours end and queued messages are released, they are sent at a rate of up to 5,000 messages per second per organization.

* **Not supported in**: Quiet hours rules are not currently available for Campaign Orchestration.

* **Dry run**: Quiet hours rules are not evaluated during journey dry run executions.

## Reporting {#reporting}

You can track how quiet hours impact your campaigns and journeys through the standard reporting features:

* **All-time report**: The "Excluded Reasons" section shows the volume of customers who did not receive communications due to quiet hours rules, along with the specific rule set name.

* **Live report**: (If available) Shows real-time statistics on profiles currently waiting due to quiet hours or discarded due to quiet hours.

## Next steps {#next-steps}

Once your quiet hours rules are configured and applied, you can:

* Review your campaign or journey to ensure rules are properly associated
* Activate your campaign or journey
* Monitor the impact of quiet hours in your reports

