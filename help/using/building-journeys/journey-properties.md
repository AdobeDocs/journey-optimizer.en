---
solution: Journey Optimizer
product: journey optimizer
title: Define your journey's properties
description: Learn how to set properties of your journey with Adobe Journey Optimizer
feature: Journeys, Get Started
topic: Content Management
role: User
level: Intermediate
keywords: journey, configuration, properties
exl-id: 6c21371c-6cbc-4d39-8fe6-39f1b8b13280
---
# Set your journey properties {#jo-properties}

>[!CONTEXTUALHELP]
>id="ajo_journey_properties"
>title="Journey properties"
>abstract="This section shows the journey properties. By default, read-only parameters are hidden. Available settings depend on the status of the journey, on your permissions and product configuration."

## Access the properties of a journey {#access-properties}

The properties of a journey are centralized in the right rail. This section is displayed by default when creating a new journey. For existing journeys, click on the pencil icon next to the journey's name to open it. 

From this section, you can define the name of the journey, add a description, and:

* manage [entrance and reentrance](#entrance),
* choose start and end [dates](#dates),
* manage [access to data](#manage-access),
* define a [timeout duration](#timeout) in journey activities (for Admin users only),
* select the journey and profile [timezones](#timezone)
* assign Adobe Experience Platform Unified Tags to your journey, to easily classify them and improve search from the campaigns list. [Learn how to work with tags](../start/search-filter-categorize.md#tags)
* monitor conflicts and prioritize your journeys using [conflict management tools](#conflict).

![](assets/journey32.png)

>[!NOTE]
>
>For live journeys, this screen displays only the publication date and the name of the user who published the journey.

The **Copy technical details** allows you to copy technical information about the journey which the support team can use to troubleshoot. The following information is copied: `JourneyVersion UID`, `OrgID`, `orgName`, `sandboxName`, `lastDeployedBy`, `lastDeployedAt`. 

Learn more about technical fields related to a journey for a given profile, and how to use them [in this page](expression/journey-properties.md).

## Entrance and reentrance {#entrance}

The profile entry mode is defined at the journey level, in the right configuration pane. Settings are described below.

Profile entrance management depends on the type of journeys. Learn more about profile entrance and reentrance management, in [this page](entry-management.md).

### Allow reentrance  {#allow-reentrance}

>[!CONTEXTUALHELP]
>id="ajo_journey_properties_entrance"
>title="Allow reentrance"
>abstract="By default, new journeys allow reentrance. You can uncheck the **Allow reentrance** option for example if you want to offer a one-time gift when a person enters a shop."
>additional-url="https://experienceleague.adobe.com/en/docs/journey-optimizer/using/orchestrate-journeys/manage-journey/entry-management" text="Profile entrance management"

By default, new journeys allow reentrance. You can uncheck the **Allow reentrance** option for "one shot" journeys, for example if you want to offer a one-time gift when a person enters a shop. 

### Reentrance wait period  {#reentrance-wait}

>[!CONTEXTUALHELP]
>id="ajo_journey_properties_re-entrance_wait"
>title="Reentrance wait period"
>abstract="Set time to wait before allowing a profile to enter the journey again in unitary journeys. This prevents users from reentering the journey for a chosen duration. Maximum duration: 90 days."
>additional-url="https://experienceleague.adobe.com/en/docs/journey-optimizer/using/orchestrate-journeys/manage-journey/entry-management" text="Profile entrance management"

When the **Allow reentrance** option is activated, the **Reentrance wait period** field is displayed. This field allows you to define the time to wait before allowing a profile to enter the journey again in unitary journeys (starting with an event or an audience qualification). This prevents journeys from being erroneously triggered multiple times for the same event. By default the field is set to 5 minutes. The maximum duration is 90 days.


## Manage access {#manage-access}

To assign custom or core data usage labels to the journey, click the **[!UICONTROL Manage access]** button. [Learn more on Object Level Access Control (OLAC)](../administration/object-based-access.md)

![](assets/journeys-manage-access.png)

## Journey and profile timezones {#timezone}

Timezone is defined at journey level. You can enter a fixed time zone or use Adobe Experience Platform profiles to define the journey time zone. If a time zone is defined in Adobe Experience Platform profile, it can be retrieved in the journey.

For more information on timezone management, see [this page](../building-journeys/timezone-management.md).

## Start and end dates {#dates}

>[!CONTEXTUALHELP]
>id="ajo_journey_properties_start_date"
>title="Start date"
>abstract="Choose the date entry into the journey can begin. If no start date is specified, it is automatically set at publication time."


>[!CONTEXTUALHELP]
>id="ajo_journey_properties_end_date"
>title="End date"
>abstract="Choose the end date of your journey. When that date is reached, profiles in that journey exit it automatically and new ones can no longer enter it."

You can define a **Start date**. If you haven't specified one, it will be automatically defined at publication time. 

You can also add an **End date**. This allows profiles to exit automatically when the date is reached. If no end date is specified, profiles can stay until the [global journey timeout](#global_timeout) (which is generally 91 days). The only exception is recurring read audience journeys with **Force reentrance on recurrence** activated, which end at the start date of the next occurrence. 

## Timeout {#timeout}

### Timeout or error in journey activities {#timeout_and_error}

>[!CONTEXTUALHELP]
>id="ajo_journey_properties_timeout"
>title="Timeout"
>abstract="Define the amount of time the journey will try to execute an action or verify a condition before considering it as timeout."


When editing an action or condition activity, you can define an alternative path in case of error or timeout. If the processing of the activity interrogating a third-party system exceeds the timeout duration defined in **[!UICONTROL Timeout or error]** field of the journey's properties, the second path will be chosen to perform a potential fallback action.

Authorized values are between 1 and 30 seconds.

We recommend that you define a very short **[!UICONTROL Timeout or error]** value if your journey is time sensitive (example: reacting to the real-time location of a person) because you cannot delay your action for more than a few seconds. If your journey is less time sensitive, you can use a longer value to give more time to the system called to send a valid response.

Journeys also uses a global timeout as detailled below.

### Global journey timeout {#global_timeout}

In addition to the [timeout](#timeout_and_error) used in journey activities, a global journey timeout is applied. It is not displayed in the interface and cannot be changed. 

This global timeout stops the progress of individuals in the journey **91 days** after they enter. This means that an individual's journey cannot last longer than 91 days. After this timeout period, the individual's data is deleted. Individuals still flowing in the journey at the end of the timeout period will be stopped and they will not be taken into account in reporting. You could therefore see more people entering the journey than exiting.

Due to the 91-day journey timeout, when journey reentrance is not allowed, we cannot make sure the reentrance blocking will work more than 91 days. Indeed, as we remove all information about persons who entered the journey 91 days after they enter, we cannot know the person entered previously, more than 91 days ago.

An individual can enter a wait activity only if he or she has enough time left in the journey to complete the wait duration before the 91 days journey timeout. See [this page](../building-journeys/wait-activity.md).


#### Time-to-Live (TTL) and data rentention FAQ {#timeout-faq}

Starting Adobe Journey Optimizer June 2024 release, the journey global timeout has moved from 30 to 91 days. Impacts are listed in the FAQ below:

**For Unitary Journeys**
<table style="table-layout:auto">
  <tr style="border: 1;">
    <td>
      <p>What happens to journey published after the TTL extension rolled out?</p>
    </td>
    <td>
      <p>Profiles entering the new journey will automatically have a TTL of 91 days.</p>
    </td>
  </tr>
  <tr style="border: 1;">
    <td>
      <p>What happens to a profile entering a journey that was published before the TTL extension launch?</p>
    </td>
    <td>
      <p>The profile will have a TTL of 30 days (7 days for HIPAA), consistent with the time the journey was originally published.</p>
    </td>
  </tr>
  <tr style="border: 1;">
    <td>
      <p>What happens to a profile which have already entered a journey when the TTL extension is launched?</p>
    </td>
    <td>
      <p>The profile will retain a TTL of 30 days (7 days for HIPAA), as per the original publication time of the journey.</p>
    </td>
  </tr>
  <tr style="border: 1;">
    <td>
      <p>What happens to a profile in a previous journey version that is republished after the TTL extension launch?</p>
    </td>
    <td>
      <p>The profile will maintain a TTL of 30 days (7 days for HIPAA), aligned with the original journey version's publication time.</p>
    </td>
  </tr>
  <tr style="border: 1;">
    <td>
      <p>What happens to a new profile entering a republished journey version after the TTL extension launch?</p>
    </td>
    <td>
      <p>The profile will have a TTL of 91 days, matching the TTL of the newly republished journey version.</p>
    </td>
  </tr>
</table>

**For Segment Trigger Journeys**

<table style="table-layout:auto">
  <tr style="border: 1;">
    <td>
      <p>What happens to new one-time journeys published after the TTL extension?</p>
    </td>
    <td>
      <p>Profiles entering the new journey will have a TTL of 91 days automatically.</p>
    </td>
  </tr>
  <tr style="border: 1;">
    <td>
      <p>What happens to new recurring journeys without forced reentrance published after the TTL extension?</p>
    </td>
    <td>
      <p>Profiles entering the new journey will have a TTL of 91 days automatically.</p>
    </td>
  </tr>
  <tr style="border: 1;">
    <td>
      <p>What happens to new recurring journeys with forced reentrance published after the TTL extension?</p>
    </td>
    <td>
      <p>Profiles entering the new journey will have a TTL equal to the recurrence period. For example, if the journey runs daily, the TTL will be 1 day.</p>
    </td>
  </tr>
  <tr style="border: 1;">
    <td>
      <p>What happens to a profile entering a journey that was published before the TTL extension launch?</p>
    </td>
    <td>
      <p>The profile will have a TTL of 30 days (7 days for HIPAA), consistent with the original publication time. For recurring journeys with forced reentrance, the TTL will match the recurrence period.</p>
    </td>
  </tr>
  <tr style="border: 1;">
    <td>
      <p>What happens to a profile running through a journey when the TTL extension is launched?</p>
    </td>
    <td>
      <p>The profile will retain a TTL of 30 days (7 days for HIPAA), as per the original publication time of the journey. For recurring journeys with forced reentrance, the TTL will match the recurrence period.</p>
    </td>
  </tr>
  <tr style="border: 1;">
    <td>
      <p>What happens to a running profile in a previous journey version that is republished after the TTL extension launch?</p>
    </td>
    <td>
      <p>The profile will maintain a TTL of 30 days (7 days for HIPPA), aligned with the original journey version's publication time. For recurring journeys with forced reentrance, the TTL will match the recurrence period.</p>
    </td>
  </tr>
  <tr style="border: 1;">
    <td>
      <p>What happens to a new profile entering a republished journey version after the TTL extension launch?</p>
    </td>
    <td>
      <p>The profile will have a TTL of 91 days, matching the TTL of the newly republished journey version. For recurring journeys with forced reentrance, the TTL will match the recurrence period.</p>
    </td>
  </tr>
</table>

## Merge policies {#merge-policies}

Journey uses merge policies while retrieving profile data from Adobe Experience Platform. Depending on the journey type, different merge policies are used:

* In Read audience or audience qualification journeys: the merge policy from the audience is used
* In Unitary event journeys: the default merge policy is used
* In Business event journeys: the merge policy from the targeted audience in the following Read audience activity is used

Journey will honour the merge policy used throughout the entire journey. Therefore, if multiple audiences are used in a journey (eg: in "inAudience" functions), creating inconsistencies with the merge policy used by the journey, an error is raised and publication is blocked. However, if an inconsistent audience is used in message personalisation, an alert is not raised, despite the inconsistency. For this reason, it is highly recommended to check the merge policy associated with your audience, when this audience is used in message personalisation.

To learn more on merge policies, refer to [Adobe Experience Platform documentation](https://experienceleague.adobe.com/en/docs/experience-platform/profile/merge-policies/overview){target="_blank"}.


## Exit criteria {#exit-criteria}

>[!CONTEXTUALHELP]
>id="ajo_journey_exit_criterias"
>title="Journey exit criteria"
>abstract="This section shows the exit criteria options. You can create one or multiple exit criteria rules for your journey."

### Description {#exit-criteria-desc}

By adding exit criteria, you make the profiles exit the journey as soon as an event happen (eg: Purchase) or they qualify for an audience. This will prevent the user from getting any further communications from the journey.

You may want to remove profiles from a journey when they do not meet the journey's purpose anymore. This can be achieved by **global exit criteria**, which are closely associated with goal management.

**Sample use case**

A marketer has a promotional journey that has a series of communications. Each of this communication is aimed at driving the customer to make a purchase. As soon as the purchase is made the customer should not receive rest of the messages in the series. By defining an exit criteria, any profiles who made a purchase is removed from the journey.

### Configuration and usage {#exit-criteria-config}

Exit criteria are set at journey level. One journey can have multiple exit criteria. If you have set multiple exit criteria, the evaluation happens from top to bottom with an `OR` logic. Hence, if you have Exit Criteria A and Exit Criteria B, it is evaluated as A **OR** B. The criteria are evaluated at every step of the journey.

To **create** an exit criteria, follow these steps:

1. Open your journey.

1. Click the ![](assets/do-not-localize/Smock_UserCheckedOut_18_N.svg) **[!UICONTROL Show Exit Criteria]** icon located in the upper-right section of the journey canvas.

1. Select **[!UICONTROL Add exit criteria]**.
  
1. Enter a **Label** and select if your exit criteria is based on an **Event** or an **Audience**.

    * For Exit criteria based on an event, like for example downloading an app or adding a product to a cart, pick only unitary event. 
    * For Exit criteria based on an audience,like for example an audience that checks if a customer has purchased in the last 24 hours, select an audience. Note: Exit criteria using an audience can take up to 10 mins to be effective.

You can add multiple exit criteria.

![](assets/exitcriteria-sample.png){width="40%" align="left"}

### Guardrails and limitations {#exit-criteria-guardrails}

The following guardrails and limitations apply to the journey exit criteria capability:

* Exit criteria are defined in draft state only
* Journey namespace coherence between events and event-based exit criteria

## Conflict management {#conflict}

The **[!UICONTROL Conflict management]** section in the journey's properties allows you to monitor conflicts and prioritize your journeys. You can:

* Apply a **Rule Set** to exclude this journey to part of your audience based on capping rules. [Learn how to work with rule sets](../configuration/rule-sets.md)

* Assign a **priority score** to the journey, ranging from 0 to 100. A higher number indicates a higher priority. The priority value inserted here is inherited by any inbound actions (such as In-App) contained in this journey. [learn how to work with priority scores](../conflict-prioritization/priority-scores.md)

  For situations where this same inbound channel configuration is used in other campaigns or journeys, the inbound action with the highest priority score is shown to the recipient. If multiple journeys or campaigns have the same score, the element that was most recently modified is chose.

* **View conflicts** with other journeys, campaigns, or channel configurations. If you wish to identify overlap on audience, start & end date, channel configuration, channel, or rule set you can view potential conflicts here. [Learn how to identify potential conflicts in journey](../conflict-prioritization/conflicts.md)
