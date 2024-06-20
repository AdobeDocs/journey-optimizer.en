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
---
# Set your journey properties {#jo-properties}

>[!CONTEXTUALHELP]
>id="ajo_journey_properties"
>title="Journey properties"
>abstract="This section shows the journey properties. By default, read-only parameters are hidden. Available settings depend on the status of the journey, on your permissions and product configuration."

>[!CONTEXTUALHELP]
>id="ajo_journey_exit_criterias"
>title="Journey exit criterias"
>abstract="This section shows the exit criteria options. You can create one or multiple exit criteria rules for your journey."

Journey properties are centralized in the right rail of the journey. This section is displayed by default when creating a new journey. For existing journeys, click on the pencil icon, next to the journey's name to access its properties. 


Use this section to set the name of the journey, add a description, and:

* manage [entrance and re-entrance](#entrance),
* choose start and end [dates](#dates),
* manage [access to data](#manage-access),
* define a [timeout duration](#timeout) in journey activities (for Admin users only),
* select the journey and profile [timezones](#timezone)
* assign Adobe Experience Platform Unified Tags to your journey, to easily classify them and improve search from the campaigns list. [Learn how to work with tags](../start/search-filter-categorize.md#tags)

![](assets/journey32.png)

>[!NOTE]
>
>For live journeys, this screen displays only the publication date and the name of the user who published the journey.

The **Copy technical details** allows you to copy technical information about the journey which the support team can use to troubleshoot. The following information is copied: `JourneyVersion UID`, `OrgID`, `orgName`, `sandboxName`, `lastDeployedBy`, `lastDeployedAt.


## Entrance and re-entrance {#entrance}

By default, new journeys allow re-entrance. You can uncheck the **Allow re-entrance** option for "one shot" journeys, for example if you want to offer a one-time gift when a person enters a shop. 

When the **Allow re-entrance** option is activated, the **Re-entrance wait period** field is displayed. This field allows you to define the time to wait before allowing a profile to enter the journey again in unitary journeys (starting with an event or an audience qualification). This prevents journeys from being erroneously triggered multiple times for the same event. By default the field is set to 5 minutes. The maximum duration is 29 days.

Learn more about profile entrance and re-entrance management, in [this section](entry-management.md).

## Manage access {#manage-access}

To assign custom or core data usage labels to the journey, click the **[!UICONTROL Manage access]** button. [Learn more on Object Level Access Control (OLAC)](../administration/object-based-access.md)

![](assets/journeys-manage-access.png)

## Journey and profile timezones {#timezone}

Timezone is defined at journey level. You can enter a fixed time zone or use Adobe Experience Platform profiles to define the journey time zone. If a time zone is defined in Adobe Experience Platform profile, it can be retrieved in the journey.

For more information on timezone management, see [this page](../building-journeys/timezone-management.md).

## Start and end dates {#dates}

You can define a **Start date**. If you haven't specified one, it will be automatically defined at publication time. 

You can also add an **End date**. This allows profiles to exit automatically when the date is reached. If no end date is specified, profiles can stay until the [global journey timeout](#global_timeout) (which is generally 91 days, and reduced to 7 days with Healthcare Shield add-on offering). The only exception is recurring read audience journeys with **Force re-entrance on recurrence** activated, which end at the start date of the next occurrence. 

## Timeout {#timeout}

### Timeout or error in journey activities {#timeout_and_error}

When editing an action or condition activity, you can define an alternative path in case of error or timeout. If the processing of the activity interrogating a third-party system exceeds the timeout duration defined in **[!UICONTROL Timeout or error]** field of the journey's properties, the second path will be chosen to perform a potential fallback action.

Authorized values are between 1 and 30 seconds.

We recommend that you define a very short **[!UICONTROL Timeout or error]** value if your journey is time sensitive (example: reacting to the real-time location of a person) because you cannot delay your action for more than a few seconds. If your journey is less time sensitive, you can use a longer value to give more time to the system called to send a valid response.

Journeys also uses a global timeout as detailled below.

### Global journey timeout {#global_timeout}

In addition to the [timeout](#timeout_and_error) used in journey activities, a global journey timeout is applied. It is not displayed in the interface and cannot be changed. 

This global timeout stops the progress of individuals in the journey **91 days** after they enter. This timeout is reduced to **7 days** with Healthcare Shield add-on offering. This means that an individual's journey cannot last longer than 91 days (or 7 days). After this timeout period, the individual's data is deleted. Individuals still flowing in the journey at the end of the timeout period will be stopped and they will not be taken into account in reporting. You could therefore see more people entering the journey than exiting.

>[!NOTE]
>
>Journeys do not directly react to privacy opt-out, access or delete requests. However, the global timeout ensures that individuals never stay more than 91 days in any journey.

Due to the 91-day journey timeout, when journey re-entrance is not allowed, we cannot make sure the re-entrance blocking will work more than 91 days. Indeed, as we remove all information about persons who entered the journey 91 days after they enter, we cannot know the person entered previously, more than 91 days ago.

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
      <p>The profile will have a TTL of 91 days (7 days for HIPAA), consistent with the time the journey was originally published.</p>
    </td>
  </tr>
  <tr style="border: 1;">
    <td>
      <p>What happens to a profile which have already entered a journey when the TTL extension is launched?</p>
    </td>
    <td>
      <p>The profile will retain a TTL of 91 days (7 days for HIPAA), as per the original publication time of the journey.</p>
    </td>
  </tr>
  <tr style="border: 1;">
    <td>
      <p>What happens to a profile in a previous journey version that is republished after the TTL extension launch?</p>
    </td>
    <td>
      <p>The profile will maintain a TTL of 91 days (7 days for HIPAA), aligned with the original journey version's publication time.</p>
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
      <p>The profile will have a TTL of 91 days (7 days for HIPAA), consistent with the original publication time. For recurring journeys with forced reentrance, the TTL will match the recurrence period.</p>
    </td>
  </tr>
  <tr style="border: 1;">
    <td>
      <p>What happens to a profile running through a journey when the TTL extension is launched?</p>
    </td>
    <td>
      <p>The profile will retain a TTL of 91 days (7 days for HIPAA), as per the original publication time of the journey. For recurring journeys with forced reentrance, the TTL will match the recurrence period.</p>
    </td>
  </tr>
  <tr style="border: 1;">
    <td>
      <p>What happens to a running profile in a previous journey version that is republished after the TTL extension launch?</p>
    </td>
    <td>
      <p>The profile will maintain a TTL of 91 days (7 days for HIPPA), aligned with the original journey version's publication time. For recurring journeys with forced reentrance, the TTL will match the recurrence period.</p>
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

