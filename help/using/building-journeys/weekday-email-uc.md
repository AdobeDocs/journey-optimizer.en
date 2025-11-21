---
solution: Journey Optimizer
product: journey optimizer
title: Send emails only on weekdays
description: Learn how to configure a journey to send emails only on weekdays in Adobe Journey Optimizer
feature: Journeys, Use Cases, Email
topic: Content Management
role: User
level: Intermediate
keywords: journey, use case, weekdays, condition, email, scheduling
version: Journey Orchestration
hide: yes
hidefromtoc: yes
---
# Send emails only on weekdays {#send-emails-only-on-weekdays}

This use case demonstrates how to configure a journey in Adobe Journey Optimizer that sends emails only on weekdays (Monday through Friday). For profiles that enter the journey on weekends (Saturday or Sunday), emails are automatically queued and sent on Monday at a specified time. This ensures optimal engagement by delivering messages during the workweek.

## Use case overview

**The Challenge**: Ensuring that emails are only sent on weekdays, even though profiles may enter the journey on weekends. For weekend entries, emails should be queued and sent on Monday at a specific time.

**The Solution**: Use a condition activity to identify the day of the week. For weekend entries, Wait activities with custom formulas delay the email until Monday. Weekday entries proceed directly to the email send step.

This approach shows you how to:

* Use a condition activity to check if the current day is Saturday or Sunday
* Implement Wait activities with custom formulas for weekend entries
* Queue weekend emails for Monday delivery at a specific hour
* Send emails immediately for weekday entries (Monday-Friday)

This approach is ideal for:

* Business-to-business (B2B) email campaigns
* Professional newsletters and communications
* Business-related announcements
* Work-related product updates
* Any marketing campaign where weekend delivery is not desired

>[!VIDEO]
>
>Watch the step-by-step [video tutorial](#how-to-video) at the bottom of this page to see the complete implementation.

## Prerequisites

To implement this use case, you need:

* An active Adobe Journey Optimizer instance
* A configured [email channel surface](../configuration/channel-surfaces.md)
* An [audience](../audience/about-audiences.md) or [event](../event/about-events.md) to trigger the journey
* Basic understanding of [journey conditions](condition-activity.md) and [expressions](expression/expressionadvanced.md)

## Implementation steps

### Step 1: Create your journey

1. Navigate to **[!UICONTROL Journey Management]** > **[!UICONTROL Journeys]** in Adobe Journey Optimizer.

1. Click **[!UICONTROL Create Journey]** to create a new journey. [Learn more about creating journeys](journey-gs.md)

1. Configure the journey properties:
   * **Name**: Weekday Email Campaign
   * **Description**: Sends emails only on weekdays (Monday-Friday)
   * Set the appropriate namespace for your use case

   [Learn more about journey properties](journey-properties.md)

1. Choose your journey entry point:
   * **[Read Audience](read-audience.md)**: For batch campaigns targeting a specific audience
   * **[Event](../event/about-events.md)**: For real-time triggered journeys based on customer behavior

### Step 2: Add a Condition activity to check the day of the week

Right after the journey start, add a **[!UICONTROL Condition]** activity to check if the current day is Saturday or Sunday. This will branch the workflow accordingly.

1. Drag and drop a **[!UICONTROL Condition]** activity onto the canvas after your entry point. [Learn more about Condition activities](condition-activity.md)

1. Click on the Condition activity to open its configuration panel.

1. In the **[!UICONTROL Condition type]** section, select **[!UICONTROL Data Source Condition]**. [Learn more about condition types](condition-activity.md#data_source_condition)

### Step 3: Configure the condition to identify Saturday

Create the first condition path to identify Saturday entries.

1. Click on **[!UICONTROL Advanced mode]** to open the expression editor. [Learn more about the expression editor](expression/expressionadvanced.md)

1. Enter the following expression to check if the current day is Saturday:

   ```javascript
   dayOfWeek(now()) == 7
   ```

   This uses the `dayOfWeek()` function with `now()` to get the current day. [Learn more about date functions](functions/date-functions.md)

   ![Configuring the Saturday condition in the expression editor](assets/weekday-email-uc-condition-expression.png)

1. Click **[!UICONTROL Ok]** to save the condition.

1. Label this path as "Saturday".

### Step 4: Add a second condition path for Sunday

1. In the Condition activity, click **[!UICONTROL Add a path]** to create a second condition.

1. In the expression editor for the second path, enter:

   ```javascript
   dayOfWeek(now()) == 1
   ```

   This checks if the current day is Sunday.

1. Label this path as "Sunday".

1. Check **[!UICONTROL Show path for other cases than the one(s) above]** to create a path for weekday entries (Monday-Friday).

   **Day of week values:**
   * 1 = Sunday
   * 2 = Monday
   * 3 = Tuesday
   * 4 = Wednesday
   * 5 = Thursday
   * 6 = Friday
   * 7 = Saturday

>[!NOTE]
>
>The `dayOfWeek()` function returns an integer representing the day of the week, where 1 is Sunday and 7 is Saturday. This follows the ISO-8601 standard for day numbering.

### Step 4: Configure Wait activities for weekend entries

For profiles entering on Saturday or Sunday, use Wait activities with custom formulas to delay the email until Monday at your desired hour.

![Journey with three condition paths - Saturday, Sunday, and Weekdays](assets/weekday-email-uc-paths.png)

**For the Saturday path:**

1. Add a **[!UICONTROL Wait]** activity. [Learn more about Wait activities](wait-activity.md)

1. Select **[!UICONTROL Duration]** as the wait type.

1. Click **[!UICONTROL Advanced mode]** to enter a custom formula.

1. Enter the following formula to wait until Monday at 9 AM:

   ```javascript
   toDuration("PT" + (48 - getHourOfDay(now())) + "H")
   ```

   Or use this alternative formula:

   ```javascript
   setHours(nowWithDelta(2, "days"), 9)
   ```

   **Explanation**: This formula calculates the wait time from Saturday to Monday at 9 AM. The value X=2 represents 2 days forward (Saturday + 2 days = Monday). [Learn more about date functions](functions/date-functions.md#nowWithDelta)

**For the Sunday path:**

1. Add a **[!UICONTROL Wait]** activity.

1. Select **[!UICONTROL Duration]** as the wait type.

1. Click **[!UICONTROL Advanced mode]** to enter a custom formula.

1. Enter the following formula to wait until Monday at 9 AM:

   ```javascript
   setHours(nowWithDelta(1, "days"), 9)
   ```

   **Explanation**: This formula waits 1 day (Sunday + 1 day = Monday) and sets the time to 9 AM. The value X=1 represents 1 day forward, and H=9 represents 9 AM.

>[!TIP]
>
>You can customize the hour (H) parameter to any time you want the email sent on Monday. For example, change 9 to 10 for 10 AM, or to 14 for 2 PM.

### Step 5: Configure the weekday path

For the **Weekday path** (Monday-Friday):

1. Proceed directly to add an **[!UICONTROL Email]** action activity. No Wait activity is needed for weekday entries. [Learn more about email actions](journeys-message.md)

1. Configure your email message:
   * Select or create your [email content](../email/get-started-email-design.md)
   * Configure the [email parameters](../email/email-settings.md)
   * Set up [personalization](../personalization/personalize.md) as needed

1. Add an **[!UICONTROL End]** activity after the email.

### Step 6: Merge weekend paths to email

After the Wait activities on both the Saturday and Sunday paths, merge them to the same Email action activity:

1. From the Saturday Wait activity, add an **[!UICONTROL Email]** action.

1. From the Sunday Wait activity, connect to the same Email action.

1. The weekday path should also flow to this Email action.


### Step 7: Test your journey

Before publishing, thoroughly test your journey logic in Adobe Journey Optimizer's Test Mode to confirm everything works as expected:

1. Click the **[!UICONTROL Test]** button in the top right corner.

1. Enable test mode. [Learn how to test your journey](testing-the-journey.md)

1. Create [test profiles](../audience/creating-test-profiles.md) with simulated entry times on different days of the week:
   * **Saturday entry**: Verify the profile follows the Saturday path, waits, and receives email on Monday at the specified hour
   * **Sunday entry**: Verify the profile follows the Sunday path, waits, and receives email on Monday at the specified hour  
   * **Monday-Friday entries**: Verify emails are sent immediately without any wait

1. Review the journey visualization to ensure profiles follow the correct conditional paths (Saturday, Sunday, or weekday).

1. Check for any errors or warnings in the journey. [Learn about troubleshooting journeys](troubleshooting.md)

1. Verify that the Wait formulas calculate the correct duration for your desired Monday delivery time.

>[!IMPORTANT]
>
>Always test your journey logic thoroughly before publishing to production. Use Test Mode to simulate different entry scenarios and validate that weekend entries are correctly queued for Monday delivery. [Learn more about journey testing best practices](testing-the-journey.md)

### Step 8: Publish your journey

Once testing is complete:

1. Click **[!UICONTROL Publish]** in the top right corner.

1. Confirm the publication. [Learn more about publishing journeys](publish-journey.md)

1. Monitor the journey performance using [Journey reporting](report-journey.md) and [live reports](../reports/journey-live-report.md).

## Best practices and considerations

### Optimize workflow with enhanced formulas

To enhance your workflow and handle more complex business requirements:

* **Complex business hours**: Extend the formulas to account for holidays, time zones, or specific business hours beyond the basic weekday check.

* **Custom delivery times**: Adjust the hour parameter (H) in the Wait formula to match your optimal send time. For example, if 10 AM shows better engagement rates, change the formula to use hour 10.

* **Multiple time zone support**: Consider creating separate journeys for different geographic regions to ensure Monday delivery in each recipient's local time zone.

### Time zone management

The `now()` function and journey execution use the time zone configured at the journey level. Consider the following:

* **Journey time zone**: Ensure the journey time zone matches your needs. Configure this in the journey properties before publishing. [Learn more about timezone management](timezone-management.md).

* **Global audiences**: If your audience spans multiple time zones, the day-of-week check happens in the journey's configured time zone, not the recipient's local time zone.

* **Localized scheduling**: For time zone-specific delivery, create separate journeys for different regions or use the timezone settings in the Read Audience activity.

### Journey entry and timing

* **Read Audience journeys**: For batch journeys, [schedule the Read Audience](read-audience.md#schedule) to trigger at a time that makes sense for your audience. Early morning executions (e.g., 6:00 AM) are common for business communications.

* **Event-based journeys**: The condition will be evaluated immediately when the event is received. Profiles entering on weekends will automatically wait until Monday. [Learn more about events](../event/about-events.md)

* **Wait timeout considerations**: Ensure your [journey timeout settings](journey-properties.md#timeout) accommodate the maximum wait period (up to 2 days from Saturday to Monday).

### Testing is essential

As emphasized in the implementation guide, always test your journey logic to confirm everything works as expected:

* Use **Test Mode** to simulate different entry scenarios without sending real emails
* Test all three paths: Saturday entries, Sunday entries, and weekday entries
* Verify Wait duration calculations are correct
* Confirm Monday delivery happens at the specified hour
* Check journey visualization to ensure proper path routing

### Re-entry and frequency

* For recurring campaigns, configure the **[!UICONTROL Re-entrance]** settings appropriately. [Learn more about re-entrance settings](entry-management.md)

* If profiles can re-enter the journey, they'll be subject to the day-of-week check each time, ensuring weekend entries are always queued for Monday.

* Consider adding [frequency capping rules](../conflict-prioritization/journey-capping.md) to avoid over-messaging if profiles can re-enter frequently.

## Advanced variations

### Specific day targeting

To send emails only on specific days (e.g., Tuesdays and Thursdays), modify the condition:

```javascript
dayOfWeek(now()) == 3 or dayOfWeek(now()) == 5
```

For all other days, add a Wait activity that calculates the number of days until the next Tuesday or Thursday.

### Different send times for different days

You can create multiple paths with different Wait formulas for different weekend behaviors:

* **Saturday → Wednesday delivery**: Use `nowWithDelta(4, "days")`
* **Sunday → Tuesday delivery**: Use `nowWithDelta(2, "days")`

This allows more flexibility in your sending schedule.

### Business hours delivery

To ensure delivery during business hours, adjust the hour parameter in your Wait formula. For example, for delivery at 2 PM instead of 9 AM:

```javascript
setHours(nowWithDelta(1, "days"), 14)
```

You can also add a second condition after the Wait to check if the current time is within business hours before sending.

### Holiday exclusion

To exclude holidays, add an additional condition path that checks for specific dates:

```javascript
toDateTimeOnly(now()) == toDateTimeOnly("2024-12-25T00:00:00")
```

If the condition matches a holiday, add a Wait activity to delay until the next business day. [Learn more about date comparison functions](functions/date-functions.md)

## Related topics

* [About Condition activities](condition-activity.md) - Learn how to create different paths in your journey
* [Use conditions in a journey](conditions.md) - Detailed guide on journey conditions
* [Wait activity](wait-activity.md) - Configure wait durations and formulas
* [Date functions](functions/date-functions.md) - Complete reference for date and time functions
* [Expression editor](expression/expressionadvanced.md) - Build complex expressions
* [Test your journey](testing-the-journey.md) - Validate journey logic before publishing
* [Time zone management](timezone-management.md) - Handle different time zones in journeys
* [Journey best practices](journey-gs.md#best-practices) - Recommended approaches for journey design

## How-to video

Learn how to send emails only on weekdays using Adobe Journey Optimizer. This video demonstrates the step-by-step implementation of condition activities and Wait formulas to queue weekend entries for Monday delivery.

>[!VIDEO](https://video.tv.adobe.com/v/3469330?quality=12&learn=on)

## Additional resources

* [Expression editor documentation](expression/expressionadvanced.md) - Build and validate journey expressions
* [Journey designer guide](using-the-journey-designer.md) - Master the journey canvas
* [Journey use cases overview](jo-use-cases.md) - Explore more journey patterns and examples
* [Community blog post: How to Send Emails Only on Weekdays](https://experienceleaguecommunities.adobe.com/t5/journey-optimizer-blogs/how-to-send-emails-only-on-weekdays-in-adobe-journey-optimizer/ba-p/760400){target="_blank"} - Original blog post with detailed examples

